# 版本来源与精简范围

日期：2026-11-01。此精简版共 87 个仓库文件。所有 73 个独立 Skill ZIP 与此前已验证完整源码版逐字节一致，System Prompt 和 Catalog 也保持原样。

| 组件 | 来源 |
|---|---|
| 71 个执行 Skill | cellsight-experts-v0.2.1 |
| Planner / Evaluation 与 System Prompt | cellsight-control-loading-patch-v1.1.1 |
| 控制 Runtime 与静态 Skill Catalog | cellsight-evaluation-meta-v0.5.1 |
| 完整源码归档 | cellsight-github-20261101.zip，原样保留 |

完整源码归档中的 registry/source-provenance.json 记录每个继承文件在原 outputs 下的相对来源与源 SHA256。控制加载补丁仅更改两份 SKILL.md 的指令文本，运行脚本与资源与 v0.5.1 一致。

精简方式：73 个 Skill 各用一个完整独立 ZIP 分发；展开源码、测试、Schema、开发工具和详细文档合并到一个完整源码归档；根目录保留关键文档、提示词、能力索引与验证工具。完整源码归档内保留其原上传包，以便原校验工具直接复现。

精简仓库不展开 skills、tests 和 .github；原 CI 配置位于完整源码归档内，GitHub 不会自动执行归档内部的工作流。若要开发或使用原 CI，可解压完整源码版后使用。

没有修改业务源码、模型适配器、评价定义或科研阈值。原始 outputs、完整仓库和旧分批交付均保持不变；本次没有推送、覆盖或删除远程 GitHub 内容。
