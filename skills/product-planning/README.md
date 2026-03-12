# 产品策划

这是 TeamPilot 面向平台公开分发的 `产品策划` Skill 包。

它的目标不是“自动写文档”，而是把一份产品方案从“资料堆”推进到“可评审、可交接、可继续设计开发”的状态。

## Skill 标题

- 对外标题：`产品策划`
- 内部目录名：`product-planning`
- 版本：`1.0.0`

## Skill 描述

证据驱动的产品策划主 Skill。通过 `/产品策划` 与 `/产品策划校验` 两条指令，编排证据收集、产品定义闸门、章节写作、总览图补齐与版本校验，用于输出可评审、可交接的 PRD 与产品方案文档。

## 触发方式

### `/产品策划`

```markdown
/产品策划 和韩雪聊聊教育
目标：整理成完整 PRD，并补总览流程图和功能架构图。
```

### `/产品策划校验`

```markdown
/产品策划校验 和韩雪聊聊教育
检查当前 PRD 是否缺总领层、图文口径是否一致、版本和索引是否同步。
```

## 目录结构

```text
product-planning/
├── SKILL.md
├── README.md
├── assets/
│   └── README.md
├── examples/
│   ├── README.md
│   ├── example-invoke.md
│   └── example-validation-command.md
└── references/
    ├── README.md
    ├── folder-structure.md
    └── review-criteria.md
```

## 审核标准摘要

详细版见 `references/review-criteria.md`。

- [ ] 文档回答的产品决策问题明确
- [ ] 产品定义、范围和模块关系一致
- [ ] 关键结论有真实证据支撑
- [ ] 结构完整，总领层存在
- [ ] 该有的图表已经补齐且图文一致
- [ ] 版本、索引和命名可交接

## 与平台的关系

这个包满足平台三类消费：

- Skills 列表页：读取 `SKILL.md` frontmatter
- Skill 详情页：展示正文、README、审核标准和目录结构
- `/提交产出` 审核：读取 `review_criteria` 与 `references/review-criteria.md`
