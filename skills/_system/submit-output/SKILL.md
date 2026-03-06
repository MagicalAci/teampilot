---
name: "提交产出"
description: "系统级 Skill —— 自动检查交付物完整性，运行自查，生成审核摘要，提交 PR"
category: "_system"
version: "1.0.0"
trigger: "/提交产出"
difficulty: 0
system: true
---

# 提交产出 Skill

> 这是 TeamPilot 的系统级 Skill。
> 当实习生完成任务后执行 `/提交产出`，本 Skill 自动进行质量自查并提交。

## 本 Skill 做什么

1. **交付物检查** — 按 `brief.md` 要求检查文件命名、数量、内容完整性
2. **自查评估** — 按关联 Skill 的 `review_criteria` 逐条自评
3. **关键决策提取** — 从对话历史中提取人类做出的关键决策和判断
4. **生成审核摘要** — 将自查结果、关键决策、对话历史摘要打包
5. **提交 PR** — 创建 GitHub Pull Request，触发 AI 审核 Action

## 执行流程

```
/提交产出
│
├── Step 1: 检查交付物
│   ├── 扫描 deliverables/ 目录
│   ├── 对比 brief.md 中的交付物要求
│   ├── 检查文件是否存在、大小是否合理
│   └── ❌ 不通过 → 提示缺失项，中止提交
│
├── Step 2: 质量自查
│   ├── 读取关联 Skill 的 review_criteria
│   ├── 逐条评估交付物内容（AI 辅助）
│   ├── 生成自评分数和改进建议
│   └── 展示自查报告给实习生确认
│
├── Step 3: 提取关键决策
│   ├── 回顾对话历史
│   ├── 提取人类做出的重要决策和判断
│   ├── 记录决策理由和背景
│   └── 生成 key-decisions.md
│
├── Step 4: 打包提交
│   ├── git add deliverables/ key-decisions.md
│   ├── git commit -m "提交任务产出: {task_title}"
│   ├── git push origin {branch_name}
│   └── 创建 PR → base: main, head: {branch_name}
│
└── Step 5: 提交确认
    ├── "✅ 产出已提交"
    ├── "📋 PR #{pr_number}: {pr_url}"
    ├── "🤖 AI 审核将自动运行"
    └── "⏳ 请等待负责人审核"
```

## PR 内容模板

PR 自动生成的描述包含：

```markdown
## 任务信息
- 项目: {project_name}
- 任务: {task_title}
- 执行人: {intern_name}

## 交付物清单
- [x] research-report.md (12KB)
- [x] screenshots/ (8 files)

## 自查报告
| 检查项 | 状态 | 说明 |
|--------|------|------|
| 对比至少 3 个竞品 | ✅ | 对比了 4 个 |
| 功能对比矩阵 | ✅ | 含 SWOT |
| 真实用户评价 | ⚠️ | 仅收集了应用商店，建议补充社交平台 |

## 关键决策记录
1. 选择了 X 而非 Y，因为...
2. 数据来源选择了...，考虑到...
```

## 注意事项

- 自查不通过时会提示具体问题，但不强制阻止提交（实习生可选择忽略）
- 关键决策提取依赖对话历史，确保工作过程中有充分的讨论记录
- PR 创建后自动触发 GitHub Actions AI 审核
