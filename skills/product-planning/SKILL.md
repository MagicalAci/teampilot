---
name: product-planning
display_name: 产品策划
description: 证据驱动的产品策划主 Skill。通过 `/产品策划` 与 `/产品策划校验` 两条指令，编排证据收集、产品定义闸门、章节写作、总览图补齐与版本校验，用于输出可评审、可交接的 PRD 与产品方案文档。
category: product
difficulty: advanced
estimated_time: 20-45min
trigger: /产品策划, /产品策划校验
version: 1.0.0
ai_capabilities:
  - orchestration
  - validation
  - document-structuring
  - evidence-synthesis
review_criteria:
  - id: decision-clarity
    label: 决策问题明确
    weight: 20
    description: 文档开头就能看清这份产出在回答什么产品决策问题
  - id: definition-consistency
    label: 产品定义一致
    weight: 20
    description: 产品定位、范围、双端关系和模块关系前后一致
  - id: evidence-grounding
    label: 证据支撑
    weight: 25
    description: 关键判断必须由真实输入材料支撑，不能把猜测写成事实
  - id: structure-completeness
    label: 结构完整
    weight: 15
    description: 至少覆盖背景、目标、方案、范围、功能、图文结构和后续动作
  - id: diagram-coverage
    label: 图文覆盖
    weight: 10
    description: 该有的总览流程图、架构图或表格已经补齐，并与正文口径一致
  - id: handoff-readiness
    label: 可交接性
    weight: 10
    description: 版本、索引、命名和交付结构足以支撑后续设计、开发与评审接手
---

# 产品策划

## 两条指令

### `/产品策划 [主题]`

用于启动或继续一份产品方案文档。

适用场景：

- 从 0 开始写 PRD
- 迭代已有 PRD
- 只补某一章
- 只补总览流程图或功能架构图
- 把一套产品文档方法沉淀成 SOP

默认执行顺序：

1. 冻结任务卡
2. 建立证据包
3. 过定义闸门
4. 路由章节写作
5. 补充图表
6. 同步版本并校验

### `/产品策划校验 [文档或主题]`

用于校验已有产品文档，而不是直接重写。

适用场景：

- 检查产品定义是否前后冲突
- 检查是否缺总领层
- 检查图文是否两套口径
- 检查版本号、索引和附件路径是否同步

默认执行顺序：

1. 读取当前文档和相关资产
2. 对照定义、结构、证据、图文关系做检查
3. 输出缺口、风险和修正建议
4. 如果用户明确要求，再进入直接修正

## 默认产出

- 主文档：`docs/workspaces/product/prd/<slug>.md`
- 图片目录：`docs/workspaces/product/prd/images/<slug>/`
- 索引同步：`docs/workspaces/product/INDEX.md`

## 关键约束

- 不要在定义未稳定前直接写后续章节
- 不要把猜测写成事实
- 不要跳过用户检查点
- 不要在最终文档里输出内部推理或工具日志
- 图和文必须使用同一套产品定义

## 成功标准

- 一开头就能看懂这份文档在回答什么问题
- 关键结论能找到真实输入材料支撑
- 结构完整，且总领层存在
- 总览图、功能图、表格与正文口径一致
- 版本、索引、命名和图片路径全部可交接

## 资源

- 总览说明：`README.md`
- 目录规范：`references/folder-structure.md`
- 审核标准：`references/review-criteria.md`
- 示例入口：`examples/example-invoke.md`
- 示例校验：`examples/example-validation-command.md`
