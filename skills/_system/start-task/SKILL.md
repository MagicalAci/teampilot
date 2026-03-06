---
name: "开始任务"
description: "系统级 Skill —— 拉取任务上下文、安装关联 Skills、初始化工作目录，一键启动任务"
category: "_system"
version: "1.0.0"
trigger: "/开始任务"
difficulty: 0
system: true
---

# 开始任务 Skill

> 这是 TeamPilot 的系统级 Skill。
> 当实习生在 Cursor 中执行 `/开始任务 --project=xxx --task=xxx` 时，本 Skill 自动运行。

## 本 Skill 做什么

1. **拉取任务上下文** — 从 GitHub 获取任务的 `brief.md`（负责人需求）、`context/` 前置材料、项目级 `knowledge/` 背景文档
2. **安装关联 Skills** — 读取任务关联的 Skill 列表，将对应的 Skill 文件夹拉取到本地
3. **初始化工作目录** — 创建本地工作目录结构（`deliverables/`、`notes/`），供后续工作产出存放
4. **环境就绪提示** — 告知实习生一切准备就绪，列出可用的 Skill 指令

## 执行流程

```
/开始任务 --project=ai-edu --task=competitive-research-v1
│
├── Step 1: 验证身份
│   └── 检查当前用户是否被分配了该任务
│
├── Step 2: 拉取任务信息
│   ├── GET /api/teampilot/tasks/{task_id} → 获取任务详情
│   ├── git pull → projects/{project}/tasks/{task}/brief.md
│   ├── git pull → projects/{project}/tasks/{task}/context/
│   └── git pull → projects/{project}/knowledge/
│
├── Step 3: 安装关联 Skills
│   ├── 读取任务的 skill_ids 列表
│   ├── 对每个 skill_id:
│   │   └── git pull → skills/{skill_id}/ → ~/.cursor/skills/{skill_id}/
│   └── 验证 SKILL.md 可读
│
├── Step 4: 初始化工作目录
│   ├── mkdir -p deliverables/
│   ├── mkdir -p notes/
│   └── 生成 README.md（任务摘要 + 可用指令列表）
│
└── Step 5: 就绪提示
    ├── "✅ 任务环境已就绪"
    ├── "📋 任务: {task_title}"
    ├── "📄 负责人要求: 已加载 brief.md"
    ├── "🛠 可用指令: /开始调研, /写PRD, ..."
    └── "💡 输入对应指令开始工作"
```

## 使用方式

实习生在 Cursor 终端中执行平台生成的启动命令：

```bash
/开始任务 --project=ai-edu --task=competitive-research-v1
```

或从 TeamPilot 平台的任务详情页复制启动命令。

## 注意事项

- 本 Skill 是自动执行的，实习生无需理解 Git 操作细节
- 如果拉取失败（网络问题等），会提示重试
- 本 Skill 不会修改已有文件，只会创建新的工作目录
