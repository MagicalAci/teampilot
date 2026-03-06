---
name: "Skill Creator"
description: "系统级 Meta-Skill —— 引导负责人创建高质量的 Skill，包含结构生成、review_criteria 定义、测试验证"
category: "_system"
version: "1.0.0"
trigger: "/创建Skill"
difficulty: 2
system: true
---

# Skill Creator — Meta-Skill

> 这是一个用来「创建 Skill 的 Skill」。
> 负责人使用 `/创建Skill` 指令，AI 将引导你设计一个新的高质量 Skill。

## 本 Skill 做什么

1. **需求理解** — 苏格拉底式引导，弄清楚这个 Skill 要教什么、代做什么
2. **结构生成** — 自动创建 SKILL.md 文件和标准子目录结构
3. **审核标准定义** — 帮你设计 `review_criteria`，确保 AI 审核有据可依
4. **工作流设计** — 分解 Skill 的执行阶段，确保苏格拉底式引导 + AI 代做平衡
5. **测试验证** — 模拟运行 Skill，检查逻辑完整性

## 执行流程

```
/创建Skill
│
├── Phase 1: 需求访谈（苏格拉底式）
│   ├── "这个 Skill 要帮实习生完成什么任务？"
│   ├── "实习生在这个任务中通常会遇到什么困难？"
│   ├── "你期望的最终交付物是什么样的？"
│   ├── "哪些环节需要人类判断，哪些可以 AI 自动完成？"
│   └── "审核时你最关注哪些质量维度？"
│
├── Phase 2: 结构设计
│   ├── 确定 Skill 元数据（name, category, trigger, difficulty）
│   ├── 设计工作流阶段（Phase 1 → Phase N）
│   ├── 定义 review_criteria（权重加总 = 100）
│   └── 确定交付物清单
│
├── Phase 3: 文件生成
│   ├── 生成 SKILL.md（含完整 frontmatter 和正文）
│   ├── 创建子目录: references/, scripts/, assets/, examples/
│   ├── 生成示例文件（如有）
│   └── 预览给负责人确认
│
├── Phase 4: 测试验证
│   ├── AI 模拟扮演实习生，走一遍 Skill 流程
│   ├── 检查引导逻辑是否有断点
│   ├── 检查 review_criteria 是否能被客观评估
│   └── 提示可能需要补充的参考资料
│
└── Phase 5: 发布
    ├── git add skills/{skill_name}/
    ├── git commit
    ├── git push
    └── 通知平台刷新 Skill 列表
```

## SKILL.md 标准结构

```yaml
---
name: "Skill 名称"
description: "一句话描述"
category: "调研 | 产品 | 运营 | 通用"
version: "1.0.0"
trigger: "/指令名"
difficulty: 1-5
review_criteria:
  - id: "criterion_1"
    description: "评审维度描述"
    weight: 20
  - id: "criterion_2"
    description: "评审维度描述"
    weight: 20
---

# {Skill 名称}

> 简介

## 启动指令
## 前置准备
## 工作流程
### Phase 1: ...
### Phase 2: ...
## 交付物
## 质量标准
```

## Skill 设计原则

1. **苏格拉底先行** — 每个 Phase 开头先问清楚、想明白，再执行
2. **AI 代做 + 人类决策** — AI 负责搜索、整理、生成初稿；人类负责判断、决策、补充见解
3. **需求感衔接** — 每个环节要让实习生理解「为什么要做这一步」
4. **可审核** — review_criteria 的每一条都应该是可以客观评估的
5. **渐进式** — 从简单到复杂，不要一上来就堆砌要求

## 注意事项

- review_criteria 的 weight 加总应等于 100
- trigger 指令要简短易记，用中文斜杠命令
- difficulty 等级：1=新手可做，3=需要一些经验，5=高难度
- 每个 Phase 预估耗时，帮助实习生管理时间
