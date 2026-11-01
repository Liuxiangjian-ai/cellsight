# CellSight-Skill-Catalog

本知识索引与配套System Prompt v1.0.0使用。初始73个顶层Skill＝2个控制Skill＋71个Execution Skill，分属12类；新注册能力可继续扩展。

**这是静态检索索引，不是已安装/已挂载/可运行清单。全部当前可用状态为待宿主核实。** 实际能力以目标SKILL.md/Manifest为准，实际挂载与运行以宿主证据为准。

执行包基线v0.2.1；控制包分发v0.5.1，新增Meta Runtime并保留v0.4.0兼容脚本。版本来自既有文件，不代表已在SciencePal验证。

## 控制入口

| 顶层Skill ID | 职责 |
|---|---|
| `cellsight-planner` | Intent → 接收Profile/Spec → 专家路由 → Plan → 有限修订 |
| `cellsight-evaluation` | Meta-Skill：Spec → Reuse/Compose/Generate → 验证 → Runtime → Report |

Project State为上述两个包内共享模块，不计第三个上传Skill。内部评价器cellsight-eval-basic、cellsight-eval-detection-consistency、cellsight-eval-llm-rubric不是默认额外宿主调用目标。

## Execution Skill名称与任务映射

Skill ID是宿主加载目标，implementation_id是执行脚本的实现选择器。documented modes表示说明覆盖范围；adapter modes仅表示当前包内CLI实际适配模式，二者不得混淆。adapter存在不证明依赖/权重/设备或科学性能可用。

### 目标检测 / detection（11）

| 完整Skill ID | implementation_id | task | 文档模式 | CLI适配模式 | 需权重 |
|---|---|---|---|---|---|
| `cellsight-detection-yolo` | `yolo` | detect | predict, train | predict | 是 |
| `cellsight-detection-rtdetr` | `rtdetr` | detect | predict, train | predict | 是 |
| `cellsight-detection-fasterrcnn` | `fasterrcnn` | detect | predict, train | predict | 是 |
| `cellsight-detection-retinanet` | `retinanet` | detect | predict, train | predict | 是 |
| `cellsight-detection-fcos` | `fcos` | detect | predict, train | predict | 是 |
| `cellsight-detection-ssdlite` | `ssdlite` | detect | predict, train | predict | 是 |
| `cellsight-detection-rf-detr` | `rf-detr` | detect | predict, train | 无；需真实原生流程 | 是 |
| `cellsight-detection-deimv2` | `deimv2` | detect | predict, train | 无；需真实原生流程 | 是 |
| `cellsight-detection-d-fine` | `d-fine` | detect | predict, train | 无；需真实原生流程 | 是 |
| `cellsight-detection-grounding-dino` | `grounding-dino` | detect | predict | 无；需真实原生流程 | 是 |
| `cellsight-detection-threshold-boxes` | `threshold-boxes` | detect | predict | predict | 否 |

### 图像分割 / segmentation（13）

| 完整Skill ID | implementation_id | task | 文档模式 | CLI适配模式 | 需权重 |
|---|---|---|---|---|---|
| `cellsight-segmentation-threshold-cc` | `threshold-cc` | instance_segment | predict | predict | 否 |
| `cellsight-segmentation-watershed` | `watershed` | instance_segment | predict | predict | 否 |
| `cellsight-segmentation-cellpose-sam` | `cellpose-sam` | instance_segment | predict, train | predict | 是 |
| `cellsight-segmentation-cellpose-dino` | `cellpose-dino` | instance_segment | predict, train | predict | 是 |
| `cellsight-segmentation-stardist` | `stardist` | instance_segment | predict, train | predict | 是 |
| `cellsight-segmentation-sam` | `sam` | prompt_segment | predict | 无；需真实原生流程 | 是 |
| `cellsight-segmentation-sam2` | `sam2` | prompt_segment | predict | 无；需真实原生流程 | 是 |
| `cellsight-segmentation-sam3` | `sam3` | prompt_segment | predict | 无；需真实原生流程 | 是 |
| `cellsight-segmentation-yolo-seg` | `yolo-seg` | instance_segment | predict, train | predict | 是 |
| `cellsight-segmentation-maskrcnn` | `maskrcnn` | instance_segment | predict, train | predict | 是 |
| `cellsight-segmentation-unet` | `unet` | semantic_segment | predict, train | 无；需真实原生流程 | 是 |
| `cellsight-segmentation-nnunet` | `nnunet` | semantic_segment | predict, train | 无；需真实原生流程 | 是 |
| `cellsight-segmentation-segformer` | `segformer` | semantic_segment | predict, train | 无；需真实原生流程 | 是 |

### 图像分类 / classification（7）

| 完整Skill ID | implementation_id | task | 文档模式 | CLI适配模式 | 需权重 |
|---|---|---|---|---|---|
| `cellsight-classification-resnet` | `resnet` | classify | predict, train | predict | 是 |
| `cellsight-classification-efficientnet` | `efficientnet` | classify | predict, train | predict | 是 |
| `cellsight-classification-mobilenet` | `mobilenet` | classify | predict, train | predict | 是 |
| `cellsight-classification-convnext` | `convnext` | classify | predict, train | predict | 是 |
| `cellsight-classification-vit` | `vit` | classify | predict, train | predict | 是 |
| `cellsight-classification-swin` | `swin` | classify | predict, train | predict | 是 |
| `cellsight-classification-dinov3-linear` | `dinov3-linear` | classify | predict, train | 无；需真实原生流程 | 是 |

### 目标追踪 / tracking（4）

| 完整Skill ID | implementation_id | task | 文档模式 | CLI适配模式 | 需权重 |
|---|---|---|---|---|---|
| `cellsight-tracking-iou-tracker` | `iou-tracker` | track | predict | predict | 否 |
| `cellsight-tracking-bytetrack` | `bytetrack` | track | predict | 无；需真实原生流程 | 否 |
| `cellsight-tracking-deepsort` | `deepsort` | track | predict | 无；需真实原生流程 | 是 |
| `cellsight-tracking-trackmate` | `trackmate` | track | predict | 无；需真实原生流程 | 否 |

### 图像处理 / processing（10）

| 完整Skill ID | implementation_id | task | 文档模式 | CLI适配模式 | 需权重 |
|---|---|---|---|---|---|
| `cellsight-processing-identity` | `identity` | process | predict | predict | 否 |
| `cellsight-processing-percentile-normalize` | `percentile-normalize` | process | predict | predict | 否 |
| `cellsight-processing-gaussian` | `gaussian` | process | predict | predict | 否 |
| `cellsight-processing-median-filter` | `median-filter` | process | predict | predict | 否 |
| `cellsight-processing-clahe` | `clahe` | process | predict | predict | 否 |
| `cellsight-processing-morph-opening` | `morph-opening` | process | predict | predict | 否 |
| `cellsight-processing-morph-closing` | `morph-closing` | process | predict | predict | 否 |
| `cellsight-processing-crop` | `crop` | process | predict | predict | 否 |
| `cellsight-processing-flatfield` | `flatfield` | process | predict | predict | 否 |
| `cellsight-processing-registration` | `registration` | register | predict | 无；需真实原生流程 | 否 |

### 图像复原 / restoration（6）

| 完整Skill ID | implementation_id | task | 文档模式 | CLI适配模式 | 需权重 |
|---|---|---|---|---|---|
| `cellsight-restoration-median-denoise` | `median-denoise` | restore | predict | predict | 否 |
| `cellsight-restoration-nlmeans` | `nlmeans` | restore | predict | 无；需真实原生流程 | 否 |
| `cellsight-restoration-richardson-lucy` | `richardson-lucy` | restore | predict | 无；需真实原生流程 | 否 |
| `cellsight-restoration-care` | `care` | restore | predict, train | 无；需真实原生流程 | 是 |
| `cellsight-restoration-noise2void` | `noise2void` | restore | predict, train | 无；需真实原生流程 | 是 |
| `cellsight-restoration-restormer` | `restormer` | restore | predict, train | 无；需真实原生流程 | 是 |

### 视觉语言与特征 / vision-language（5）

| 完整Skill ID | implementation_id | task | 文档模式 | CLI适配模式 | 需权重 |
|---|---|---|---|---|---|
| `cellsight-vision-language-clip` | `clip` | image_text_match, embedding | predict | 无；需真实原生流程 | 是 |
| `cellsight-vision-language-biomedclip` | `biomedclip` | image_text_match, embedding | predict | 无；需真实原生流程 | 是 |
| `cellsight-vision-language-siglip` | `siglip` | image_text_match, embedding | predict | 无；需真实原生流程 | 是 |
| `cellsight-vision-language-dinov3` | `dinov3` | embedding | predict | 无；需真实原生流程 | 是 |
| `cellsight-vision-language-vlm` | `vlm` | describe | predict | 无；需真实原生流程 | 是 |

### 科学定量 / quantification（4）

| 完整Skill ID | implementation_id | task | 文档模式 | CLI适配模式 | 需权重 |
|---|---|---|---|---|---|
| `cellsight-quantification-morphology` | `morphology` | morphology | predict | predict | 否 |
| `cellsight-quantification-fluorescence` | `fluorescence` | fluorescence | predict | predict | 否 |
| `cellsight-quantification-regionprops` | `regionprops` | morphology | predict | 无；需真实原生流程 | 否 |
| `cellsight-quantification-spatial-statistics` | `spatial-statistics` | spatial_statistics | predict | 无；需真实原生流程 | 否 |

### 异常与缺陷检测 / anomaly（3）

| 完整Skill ID | implementation_id | task | 文档模式 | CLI适配模式 | 需权重 |
|---|---|---|---|---|---|
| `cellsight-anomaly-patchcore` | `patchcore` | anomaly_detect | predict, train | 无；需真实原生流程 | 是 |
| `cellsight-anomaly-padim` | `padim` | anomaly_detect | predict, train | 无；需真实原生流程 | 是 |
| `cellsight-anomaly-efficientad` | `efficientad` | anomaly_detect | predict, train | 无；需真实原生流程 | 是 |

### 关键点与姿态 / pose（3）

| 完整Skill ID | implementation_id | task | 文档模式 | CLI适配模式 | 需权重 |
|---|---|---|---|---|---|
| `cellsight-pose-yolo-pose` | `yolo-pose` | pose | predict, train | predict | 是 |
| `cellsight-pose-mmpose` | `mmpose` | pose | predict, train | 无；需真实原生流程 | 是 |
| `cellsight-pose-deeplabcut` | `deeplabcut` | pose | predict, train | 无；需真实原生流程 | 是 |

### 图像文字识别 / ocr（3）

| 完整Skill ID | implementation_id | task | 文档模式 | CLI适配模式 | 需权重 |
|---|---|---|---|---|---|
| `cellsight-ocr-paddleocr` | `paddleocr` | ocr | predict | 无；需真实原生流程 | 是 |
| `cellsight-ocr-tesseract` | `tesseract` | ocr | predict | 无；需真实原生流程 | 是 |
| `cellsight-ocr-easyocr` | `easyocr` | ocr | predict | 无；需真实原生流程 | 是 |

### 深度估计 / depth（2）

| 完整Skill ID | implementation_id | task | 文档模式 | CLI适配模式 | 需权重 |
|---|---|---|---|---|---|
| `cellsight-depth-depth-anything-v2` | `depth-anything-v2` | depth | predict, train | 无；需真实原生流程 | 是 |
| `cellsight-depth-midas` | `midas` | depth | predict, train | 无；需真实原生流程 | 是 |

## 路由与扩展规则

1. 按task和数据域缩小范围，核实宿主挂载后读取目标说明，按实际Schema调用。用户明确指定模型时保留偏好，不以别的输出冒充。
2. detect与instance_segment不是同一任务。YOLO检测、YOLO分割、YOLO姿态具有不同完整ID；SAM/SAM2/SAM3、Cellpose-SAM/Cellpose-DINO也分别独立，不自动替换。
3. 训练模式出现在说明中不等于run.py支持训练。无适配器时只有实际环境具备原生流程才能运行；否则待安装/待执行。
4. 面对原始荧光定量，先确认强度来源，分割与定量分别选专家，不把增强显示值当测量。面对追踪，先核实上游detections与帧/样品身份。
5. 用户扩展Skill按同一Manifest接口登记。若宿主已挂载、接口兼容并通过必要核实，即便不在这71条中也可作为候选；未知入口和第三方代码不自动执行。
6. 当前Python辅助Registry对第三方只实现注册/校验/待安装，本索引不改变此能力；原生宿主调用需按真实能力处理。

## 事实边界

本索引没有细胞图像、标注、检测结果或性能测量。模型名称和适配模式仅转录既有项目，不提供“所有模型均可用”或“已验证领域性能”的承诺。

## v0.5.0控制层更新

cellsight-evaluation已改为Meta-Skill，优先Reuse/Compose后Generate，Planner接收Profile/Spec。新增内部Runtime ID见同目录JSON，不是新增顶层Skill。71个执行条目保持原版本，所有可用性仍须宿主验证。

控制层v0.5.1新增草案discover与独立validate-spec。生成Rubric只有缺Judge测试时不认证ready。实际完整ID与执行条目保持不变。
