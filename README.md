# TeamPilot Workspace

Skills-Driven Team Collaboration Platform — 中央仓库

## 目录结构

```
teampilot/
├── skills/                    # 公共 Skills（所有项目可用）
│   ├── competitive-research/  # 竞品调研 Skill
│   │   └── SKILL.md
│   ├── prd-writing/           # PRD 撰写 Skill
│   │   └── SKILL.md
│   └── daily-report/          # 日报撰写 Skill
│       └── SKILL.md
├── projects/                  # 项目目录
│   └── {project-slug}/
│       ├── README.md          # 项目说明
│       ├── skills/            # 项目级 Skills
│       │   └── {skill-name}/
│       │       └── SKILL.md
│       └── tasks/             # 任务目录
│           └── {task-slug}/
│               ├── brief.md           # 任务简报（负责人编写）
│               ├── deliverables/      # 交付物（实习生产出）
│               └── .meta/             # 元数据
│                   ├── key-decisions.md
│                   └── conversation-log.json
└── README.md
```

## 工作流

1. **负责人** 在 TeamPilot 平台创建项目和任务
2. 平台自动在本仓库创建对应目录结构
3. **实习生** 在 Cursor 中拉取 Skill，按引导完成任务
4. 实习生提交 PR → AI 自动审核 → 负责人终审
5. 通过后自动合并 PR + 发布到飞书知识库

## Skills 规范

每个 Skill 是一个文件夹，必须包含 `SKILL.md`：

```yaml
---
name: "Skill 名称"
description: "一句话描述"
category: "调研/产品/运营/通用"
version: "1.0.0"
trigger: "/开始调研"
---

# Skill 正文（苏格拉底式引导 + AI 代做）
```
