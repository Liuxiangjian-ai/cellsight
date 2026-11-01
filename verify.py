"""Verify the compact release without executing Skill code; standard library only."""
from pathlib import Path
from urllib.parse import unquote
import ast
import hashlib
import json
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parent
IGNORED = {'.git', '__pycache__', '.venv', 'work', 'unpacked-source'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    files = sorted(p for p in ROOT.rglob('*') if p.is_file()
                   and not set(p.relative_to(ROOT).parts) & IGNORED
                   and p.name not in {'.DS_Store', 'Thumbs.db'} and p.suffix not in {'.pyc', '.pyo'})
    check(len(files) == 87, f'Expected 87 release files, found {len(files)}')
    check(all(p.stat().st_size < 25*1024*1024 for p in files), 'Browser size limit exceeded')
    manifest = json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    entries = {e['path']: e for e in manifest['files']}
    current = {p.relative_to(ROOT).as_posix() for p in files}
    check(set(entries) == current-{'manifest.json', 'SHA256SUMS'}, 'Manifest coverage mismatch')
    for path, entry in entries.items():
        data = (ROOT/path).read_bytes()
        check(len(data) == entry['bytes'] and digest(data) == entry['sha256'], f'File changed: {path}')
    sums = {}
    for line in (ROOT/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
        value, path = line.split('  ', 1)
        check(path not in sums, 'Duplicate checksum path')
        sums[path] = value
    check(set(sums) == current-{'SHA256SUMS'}, 'Checksum coverage mismatch')
    for path, value in sums.items():
        check(digest((ROOT/path).read_bytes()) == value, f'Checksum mismatch: {path}')
    catalog = json.loads((ROOT/'system-prompt/CellSight-Skill-Catalog.json').read_text(encoding='utf-8-sig'))
    ids = {e['skill_id'] for e in catalog['entries']}
    check(len(catalog['entries']) == len(ids) == 73, 'Catalog must contain 73 unique IDs')
    check({'cellsight-planner', 'cellsight-evaluation'} <= ids and catalog['execution_skills'] == 71
          and catalog['category_count'] == 12, 'Catalog role/category mismatch')
    packages = sorted((ROOT/'upload-zips').glob('*.zip'))
    check(len(packages) == 73 and {p.stem for p in packages} == ids, '73 independent packages required')
    resources = 0
    for p in packages:
        with zipfile.ZipFile(p) as z:
            names = z.namelist()
            check(z.testzip() is None and len(names) == len(set(names)), f'Corrupt ZIP: {p.name}')
            check('SKILL.md' in names and sum(Path(n).name == 'SKILL.md' for n in names) == 1,
                  f'Invalid Skill entry: {p.name}')
            check(all(not n.startswith('/') and '..' not in Path(n).parts for n in names),
                  f'Unsafe ZIP paths: {p.name}')
            text = z.read('SKILL.md').decode('utf-8-sig')
            check(bool(re.search(r'^name:\s*'+re.escape(p.stem)+r'\s*$', text, re.M)), f'Wrong Skill name: {p.name}')
            resources += len(names)
    with zipfile.ZipFile(ROOT/'source/cellsight-full-source.zip') as source:
        check(source.testzip() is None, 'Full source CRC mismatch')
        for p in packages:
            check(source.read('cellsight/upload-zips/'+p.name) == p.read_bytes(),
                  f'Package differs from source: {p.name}')
        source_count = len(source.namelist())
        original = json.loads(source.read('cellsight/artifact-manifest.json'))
        check(set(source.namelist()) == {'cellsight/'+e['path'] for e in original['files']}
              | {'cellsight/artifact-manifest.json'}, 'Source manifest coverage mismatch')
        for e in original['files']:
            data = source.read('cellsight/'+e['path'])
            check(len(data) == e['bytes'] and digest(data) == e['sha256'], f'Source checksum mismatch: {e["path"]}')
    links = 0
    for p in files:
        if p.suffix == '.py':
            ast.parse(p.read_text(encoding='utf-8'), filename=p.name)
        if p.suffix == '.json':
            json.loads(p.read_text(encoding='utf-8-sig'))
        if p.suffix != '.md':
            continue
        for target in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', p.read_text(encoding='utf-8-sig')):
            if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', target) or target.startswith('#'):
                continue
            resolved = (p.parent/unquote(target.split('#', 1)[0])).resolve()
            check(resolved.is_relative_to(ROOT) and resolved.exists(), f'Broken link in {p.name}: {target}')
            links += 1
    print(json.dumps({'status': 'PASS', 'repository_files': len(files), 'independent_skills': len(packages),
                      'skill_resource_entries': resources, 'source_archive_files': source_count,
                      'local_links': links, 'all_checksums': 'PASS', 'source_byte_comparison': 'PASS'}, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError, zipfile.BadZipFile) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
