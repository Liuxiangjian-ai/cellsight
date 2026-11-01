# 清灵之眼 · CellSight

**以自然语言组织科学计算机视觉任务，用可追溯的规划、执行与评价连接 LLM 和 CV。**

CellSight 使用 MoE-inspired Skill Routing 按任务选择能力，以 Evals as PRDs 指导研发和回归。本仓库提供 **73 个完整的独立 Skill：1 个 Planner、1 个 Evaluation Meta-Skill、71 个执行 Skill，覆盖 12 类能力**。

这是适合 GitHub 网页一次上传的精简分发版，**仓库共 87 个文件**。每个 Skill 的完整说明、脚本、Schema、参考资料与微型样例保留在其独立 ZIP 中；展开源码、测试和开发工具另以一个完整源码 ZIP 保留。精简的是仓库文件数量，没有删除 Skill 能力或业务源码。

## 快速使用

1. 使用 [System Prompt](system-prompt/CellSight-System-Prompt.txt) 配置宿主智能体。
2. 将 [73 个独立上传包](upload-zips) 分别导入 SciencePal 或兼容宿主，挂载到同一智能体。每包根目录直接包含 SKILL.md，类别仅用于检索。
3. 依据 [Skill 清单](SKILLS.md) 查找所需能力，核实依赖、权重、设备与真实调用入口，再开展科研任务。

[部署与网页上传步骤](INSTALLATION.md) · [能力索引](system-prompt/CellSight-Skill-Catalog.md) · [完整源码与测试](source/cellsight-full-source.zip)

## 工作流程

科研需求 → Planner 形成 Task Intent → Evaluation 形成规范草案 → 协作发现能力 → 保存规范版本与 hash → Planner 正式计划 → 按需执行 → Evaluation 核验真实产物 → 在预算内有限修订或交付。

宿主 LLM 理解自然语言并实际加载 Skill，Python 工具处理结构化输入。本仓库没有通用的 71 模型自动调度桥，也没有 SciencePal 私有安装 API。

## 文件结构

| 位置 | 内容 |
|---|---|
| upload-zips/ | 73 个完整独立 Skill ZIP |
| system-prompt/ | 系统提示词、JSON 与 Markdown 能力索引 |
| source/ | 完整源码、测试、Schema、开发工具与详细文档归档 |
| SKILLS.md | 全部 Skill 的分类与下载清单 |
| INSTALLATION.md | 部署、源码使用与网页上传说明 |
| RELEASE.md | 版本来源与精简范围 |
| RIGHTS.md | 项目许可状态及第三方来源边界 |
| VALIDATION.md | 软件实测范围与本次包装检查 |
| verify.py | 仅依赖标准库的分发校验工具 |
| manifest.json / SHA256SUMS | 文件清单、大小与校验码 |

## 版本与验证

执行库基线 v0.2.1，控制运行时 v0.5.1，控制指令使用 v1.1.1 加载补丁。完整源码版已在本地通过 **76 项软件回归，0 跳过**；本精简版的 73 个包与已验证版本字节一致。见 [验证记录](VALIDATION.md)。

34 个执行 Skill 带推理或计算适配器，37 个提供原生操作配方；部分条目属于同一家族或相近架构。不能据此宣称 71 种不同架构、71 个模型均已部署或均已科学验证。训练说明也不等于内置 CLI 已支持训练。

没有 GT 时，监督指标保留 NOT_EVALUABLE，基础 QA 通过不代表准确率达标。分发包不含模型权重、真实科研数据集、用户附件或影片；微型合成资源仅用于软件样例。原交付未提供项目级 LICENSE，整理时未代作者指定开源许可，见 [权利说明](RIGHTS.md)。
