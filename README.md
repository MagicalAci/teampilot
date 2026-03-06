# TeamPilot Workspace

TeamPilot 统一协作仓库 —— Skills、项目、任务的中心化存储。

## 目录结构

```
teampilot/
├── skills/                        # 📚 Skill 库
│   ├── _system/                   # 系统级 Skill（平台自动调用）
│   │   ├── start-task/            #   /开始任务 — 拉取上下文、安装 Skill、初始化目录
│   │   │   ├── SKILL.md
│   │   │   ├── references/
│   │   │   ├── scripts/
│   │   │   ├── assets/
│   │   │   └── examples/
│   │   ├── submit-output/         #   /提交产出 — 自查、提取决策、提交 PR
│   │   │   └── (同上结构)
│   │   └── skill-creator/         #   /创建Skill — 引导负责人创建新 Skill
│   │       └── (同上结构)
│   │
│   ├── competitive-research/      # 竞品调研 Skill
│   │   ├── SKILL.md               #   主文件（含 review_criteria）
│   │   ├── references/            #   参考资料
│   │   ├── scripts/               #   辅助脚本
│   │   ├── assets/                #   模板/素材
│   │   └── examples/              #   示例产出
│   │
│   ├── prd-writing/               # PRD 撰写 Skill
│   │   └── (同上结构)
│   │
│   └── daily-report/              # 日报撰写 Skill
│       └── (同上结构)
│
├── projects/                      # 📁 项目空间
│   └── {project-slug}/
│       ├── knowledge/             #   项目背景文档
│       │   ├── product-brief.md
│       │   └── design-spec.md
│       └── tasks/
│           └── {task-slug}/
│               ├── brief.md       #   负责人需求文档
│               ├── context/       #   前置材料
│               ├── deliverables/  #   交付物（实习生产出）
│               ├── key-decisions.md  # 关键决策记录
│               └── notes/         #   工作笔记
│
├── .github/
│   ├── workflows/
│   │   └── ai-review.yml         # AI 审核 Action
│   └── PULL_REQUEST_TEMPLATE.md   # PR 提交模板
│
└── README.md                      # 本文件
```

## 工作流程

```
负责人创建任务（平台）
    ↓
自动生成 projects/{project}/tasks/{task}/brief.md
    ↓
实习生执行 /开始任务 → 拉取上下文 + 安装 Skills
    ↓
实习生在 Cursor 中使用 Skills 完成工作
    ↓
实习生执行 /提交产出 → 自查 + 创建 PR
    ↓
GitHub Actions 自动运行 AI 审核 → PR 评论
    ↓
负责人在平台审核 → 通过/退回
    ↓
通过后发布到飞书知识库
```

## Skill 结构

每个 Skill 是一个文件夹，包含：

| 文件/目录 | 说明 |
|-----------|------|
| `SKILL.md` | 主文件 — 元数据(frontmatter) + 工作流程 + 质量标准 |
| `references/` | 参考资料（行业报告、模板等） |
| `scripts/` | 辅助脚本（数据处理、自动化等） |
| `assets/` | 素材模板（表格、图表模板等） |
| `examples/` | 示例产出（帮助实习生理解预期） |

### SKILL.md Frontmatter

```yaml
---
name: "Skill 名称"
description: "一句话描述"
category: "调研 | 产品 | 运营 | 通用 | _system"
version: "1.0.0"
trigger: "/指令名"
difficulty: 1-5
review_criteria:
  - id: "criterion_id"
    description: "评审维度描述"
    weight: 20
---
```

## 环境变量

| 变量 | 说明 |
|------|------|
| `TEAMPILOT_API_URL` | TeamPilot 平台 API 地址 |
| `TEAMPILOT_AI_REVIEW_KEY` | AI 审核认证密钥 |

## 许可

内部使用，未经授权不得外传。
