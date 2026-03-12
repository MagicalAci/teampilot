# 文件夹结构

## Skill 包结构

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

## 目录职责

### `assets/`

放模板资产和可复用骨架。

### `examples/`

放调用示例和期望行为，帮助用户知道怎么触发。

### `references/`

放目录规范、审核标准和补充规则。

## 默认产出路径

```text
docs/workspaces/product/
├── INDEX.md
└── prd/
    ├── <slug>.md
    └── images/
        └── <slug>/
            ├── *.svg
            └── *.png
```

## 输入材料来源

任务输入材料不要求放进 Skill 目录。

常见来源：

- 用户提供的截图目录
- 会议纪要
- CSV / XLSX
- 现有 PRD
- 知识库文档
