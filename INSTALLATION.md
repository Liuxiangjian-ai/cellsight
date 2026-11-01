# 安装、源码与网页上传

## 网页一次上传

1. 解压 cellsight-github-compact.zip，打开其中的 cellsight-compact 文件夹。
2. 在仓库根页面点击 uploading an existing file；已有文件时选择 Add file → Upload files。
3. 选中 cellsight-compact 里面的全部文件和文件夹，一起拖到网页上传区。上传的是该文件夹的内容。
4. 文件加载完成后填写提交说明，提交到 main。该版本合计 87 个文件，只需一批。

source/cellsight-full-source.zip 和 upload-zips 内的 73 个 ZIP 直接保留为仓库文件，上传前不用展开它们。GitHub 首页 README 与 Skill 下载清单可以直接浏览，完整源码下载后解压浏览。

如果已经上传旧分批版的文件，上传新文件不会自动删除旧文件，需要另行核对旧目录。本任务没有更改远程仓库。

## 部署

73 个 Skill ZIP 分别导入同一宿主智能体。系统提示词使用 system-prompt/CellSight-System-Prompt.txt，静态能力索引按宿主支持方式放入知识库。Project State 和内部评价处理器包含在控制包中，不额外计数。

按每个包内的 SKILL.md、references/model-guide.md 和 Schema 核实依赖、框架、权重、轴/通道、坐标、输入输出、设备、预算和权限。目录是能力声明，实际加载和运行须有宿主证据。原生操作配方不等于已经执行。

## 开发与测试

下载并解压 [完整源码](source/cellsight-full-source.zip)，打开其中的 cellsight 文件夹。完整归档包含所有展开源码、测试、依赖、工具、文档和原上传包，保留原版本的复现入口。

    python scripts/validate_repository.py
    python -m pip install -r requirements-test.txt
    python -B -m unittest discover -s tests -p 'test_*.py' -v
    python -B examples/run_numeric_examples.py --output work/numeric-example-001

推荐 Python 3.12。模型依赖按实际需求配置；数值例不运行真实 CV 或远程 LLM。完整归档里的发布说明记录的是其原整理状态，本精简分发方式以外层说明为准。

## 检查精简包

在精简仓库根目录执行：

    python -B verify.py

仅需标准库。工具核验文件数、哈希、73 个独立包及完整源码的 CRC、Skill 入口和名称、能力索引、文档链接，并将 73 个独立包与完整源码归档中的对应包逐字节比较。
