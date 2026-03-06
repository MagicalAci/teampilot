---
name: "竞品深度调研"
description: "引导实习生完成一份高质量的竞品调研报告，涵盖产品体验、AI能力、商业模式、用户口碑等维度"
category: "调研"
version: "1.0.0"
trigger: "/开始调研"
difficulty: 3
review_criteria:
  - id: "competitors_count"
    description: "对比至少 3 个竞品"
    weight: 20
  - id: "ai_accuracy_test"
    description: "重点分析 AI 准确率（如适用）"
    weight: 15
  - id: "feature_matrix"
    description: "功能对比矩阵 + SWOT 分析"
    weight: 20
  - id: "pricing_comparison"
    description: "免费 vs 付费差异深度对比"
    weight: 15
  - id: "real_experience"
    description: "不只看官网宣传，需要真实体验产品"
    weight: 15
  - id: "user_reviews"
    description: "收集真实用户评价（小红书/知乎/应用商店）"
    weight: 15
---

# 竞品深度调研 Skill

> 本 Skill 将通过苏格拉底式引导，帮助你完成一份专业级的竞品调研报告。
> AI 不只是教你怎么做——它会和你一起搜索、分析、生成图表、撰写报告。

## 启动指令

在 Cursor 中输入 `/开始调研`，AI 将引导你逐步完成以下环节。

## 前置准备

AI 会自动完成：
1. 读取 `brief.md`，提炼负责人的核心关注点和具体要求
2. 读取 `context/` 中的前置材料（如有）
3. 读取 `knowledge/` 中的项目背景文档

## 工作流程

### Phase 1: 理解需求（10-15min）
- AI 解读 brief.md 中的结构化需求，帮你理解负责人真正想知道什么
- **需求感衔接**："负责人为什么要做这个调研？他在什么决策节点上？"
- 与你确认调研范围、重点维度、竞品选择
- 如果 brief.md 的要求有模糊地带，AI 会提示你主动确认

### Phase 2: 背景研究（30-45min）
- AI 自动搜索产品基本信息、融资背景、团队情况
- **需求感衔接**："了解背景才能判断竞品的战略意图，避免只看表面功能"
- 你补充个人认知和行业理解
- AI 生成初步竞品画像

### Phase 3: 产品体验（1-2h）
- 逐个体验竞品核心功能，截图记录关键界面和交互
- **需求感衔接**："只有亲手用过，才能发现文档里看不到的细节"
- AI 帮你组织截图和观察笔记，生成体验对比表

### Phase 4: 深度分析（1-1.5h）
- AI 能力测试（如适用）——AI 辅助设计测试用例、统计准确率
- 商业模式 / 定价策略分析——AI 搜索定价页面、计算对比表
- 用户口碑采集（小红书、知乎、应用商店）——AI 辅助搜索和整理

### Phase 5: 报告撰写（1-1.5h）
- AI 基于所有收集的素材生成报告框架和初稿
- 你审核、补充个人见解、调整结论
- AI 生成功能对比矩阵和 SWOT 分析表格

### Phase 6: 自查提交
- AI 按 brief.md 中的要求逐条核查，确保无遗漏
- 提示你检查：数据来源是否标注、结论是否有论据支撑
- 确认后运行 `/提交产出` 提交

## 交付物要求

- `deliverables/research-report.md` — 主报告
- `deliverables/screenshots/` — 产品截图
- `deliverables/comparison-matrix.md` — 功能对比表（可选）

## 质量标准

- 每个竞品至少覆盖：功能、体验、定价、AI能力、用户评价 5 个维度
- 数据有来源标注（URL 或截图）
- 结论有论据支撑，避免主观臆断
- SWOT 分析 Threats 要具体，不能泛泛而谈
- 免费层 vs 付费层需有功能差异的具体对比
