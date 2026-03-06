---
name: "PRD 撰写"
description: "引导实习生撰写一份结构完整、逻辑清晰的产品需求文档"
category: "产品"
version: "1.0.0"
trigger: "/写PRD"
difficulty: 3
review_criteria:
  - id: "background_objective"
    description: "背景与目标描述清晰，有数据或事实支撑"
    weight: 15
  - id: "user_stories"
    description: "用户故事符合 INVEST 原则，验收标准可量化"
    weight: 20
  - id: "feature_priority"
    description: "功能清单含优先级排序（MoSCoW 或 RICE）"
    weight: 15
  - id: "interaction_spec"
    description: "页面/交互说明覆盖核心流程和异常处理"
    weight: 20
  - id: "edge_cases"
    description: "考虑了边界情况、异常状态和错误处理"
    weight: 15
  - id: "risk_constraints"
    description: "风险与约束有识别且有应对方案"
    weight: 15
---

# PRD 撰写 Skill

> 本 Skill 引导你完成一份符合行业标准的 PRD 文档。
> AI 会帮你搜索竞品方案、生成文档框架、检查逻辑漏洞。

## 启动指令

在 Cursor 中输入 `/写PRD`

## 前置准备

AI 会自动完成：
1. 读取 `brief.md`，提炼负责人的核心需求和约束
2. 读取 `context/` 中的前置材料（竞品调研、数据报告等）
3. 读取 `knowledge/` 中的项目背景文档（产品说明、设计规范等）

## 工作流程

### Phase 1: 需求理解（15min）
- AI 解读 brief.md，提炼功能范围、目标用户、业务目标
- **需求感衔接**："PRD 的读者是谁？他们看完要做什么决策？"
- 与你确认理解是否一致

### Phase 2: 竞品参考（20min）
- AI 快速搜索同类产品的解决方案
- **需求感衔接**："站在巨人肩膀上——先看别人怎么做的，再设计自己的方案"
- 提取可借鉴的设计模式和交互范式

### Phase 3: 功能设计（30-45min）
- 拆解用户故事（INVEST 原则）
- AI 辅助定义功能清单和优先级（MoSCoW）
- 梳理页面流程和信息架构
- **需求感衔接**："每个功能都要回答：用户为什么需要它？"

### Phase 4: 文档撰写（1h）
- AI 生成文档框架和初稿
- 你填充业务逻辑细节、异常处理、边界条件
- AI 逐节审核：检查验收标准是否可量化、是否有遗漏的异常状态

### Phase 5: 自查提交
- AI 按 brief.md 要求逐条核查
- 检查验收标准是否可量化、流程是否有断点
- 确认后运行 `/提交产出` 提交

## 交付物

- `deliverables/prd.md` — PRD 文档

## PRD 结构要求

1. 背景与目标
2. 目标用户
3. 功能清单（含优先级）
4. 用户故事与验收标准
5. 页面/交互说明
6. 数据需求
7. 风险与约束
