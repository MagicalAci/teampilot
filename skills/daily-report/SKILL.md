---
name: "日报撰写"
description: "基于当天的工作记录和对话历史，快速生成结构化日报"
category: "通用"
version: "1.0.0"
trigger: "/写日报"
difficulty: 1
review_criteria:
  - id: "work_items"
    description: "今日完成的工作项有具体描述和产出物"
    weight: 40
  - id: "problems_status"
    description: "遇到的问题有描述当前状态和解决方向"
    weight: 20
  - id: "tomorrow_plan"
    description: "明日计划清晰可执行"
    weight: 20
  - id: "personal_insight"
    description: "包含个人思考或行业观察（可选加分项）"
    weight: 20
---

# 日报撰写 Skill

> 快速生成当日工作日报。AI 回顾你的工作记录，帮你整理和润色。

## 启动指令

在 Cursor 中输入 `/写日报`

## 工作流程

1. AI 回顾今天的对话历史和文件变更，自动提取工作内容
2. AI 生成日报草稿，包含完成事项、遇到的问题、明日计划
3. 你审核调整：补充 AI 没捕捉到的线下工作、修正描述
4. 确认后保存到 `deliverables/daily-report-{date}.md`

## 日报格式

```markdown
# 日报 — {日期}

## 今日完成
- [ ] 任务1：具体描述 + 产出物
- [ ] 任务2：具体描述 + 产出物

## 遇到的问题
- 问题描述 + 当前状态 + 解决方向

## 明日计划
- 计划1：预计耗时 + 交付物
- 计划2：预计耗时 + 交付物

## 个人思考（可选）
- 行业观察 / 技能提升 / 想法
```

## 交付物

- `deliverables/daily-report-{YYYY-MM-DD}.md`
