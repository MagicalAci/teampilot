# 脚本压缩包清单 - 学习报告总结（走神专注度图片+科目+时间→总结文本）

> **适用命令**: `/AI脚本` 或 `/AI策划`

## 1. 文件清单

| 路径 | 分类 | 是否必带 | 是否可直接复用 | 说明 |
|---|---|---|---|---|
| learning-report-summary-script/summary_generator.py | 核心源码 | 是 | 是 | 生成器入口 |
| learning-report-summary-script/client.py | 核心源码 | 是 | 是 | 模型客户端 |
| learning-report-summary-script/prompt_summary.txt | 文档 | 是 | 是 | Prompt 正文 |
| learning-report-summary-script/route_example.py | 示例 | 否 | 是 | HTTP 示例 |
| learning-report-summary-script/demo.py | 示例 | 否 | 是 | CLI 示例 |
| learning-report-summary-script/test_summary.py | 测试 | 是 | 是 | 单元测试 |
| learning-report-summary-script/examples/input.json | 样例 | 是 | 是 | 输入样例 |
| learning-report-summary-script/examples/output_sample.json | 样例 | 是 | 是 | 输出样例 |
| learning-report-summary-script/README.md | 文档 | 是 | 是 | 脚本说明 |
| learning-report-summary-ai-prd.md | 文档 | 是 | 是 | AI PRD |
| learning-report-summary-ai-test-report.md | 文档 | 是 | 是 | 测试报告 |

## 2. 打包说明

- 压缩包输出路径：可由 `package_ai_script_bundle.py` 生成至 deliverables 或指定目录
- 根目录名：learning-report-summary-script（或含 PRD/测试报告的完整包）
- 打包命令：见 Skill 内 `scripts/package_ai_script_bundle.py`

## 3. 不包含的能力

- 鉴权
- CORS
- 网关放行
- 正式环境监控 / 告警
