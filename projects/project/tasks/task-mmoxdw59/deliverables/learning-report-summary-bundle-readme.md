# AI脚本交付 README - 学习报告总结（走神专注度图片+科目+时间→总结文本）

> **适用命令**: `/AI脚本` 或 `/AI策划`  
> **交付日期**: 2025-03-13  
> **版本号**: V1.0  
> **面向对象**: Backend / 联调同学

## 1. 交付概览

- **解决什么问题**：根据走神/专注度图片 + 科目 + 时间，生成一段学习报告总结文本。
- **可直接接入**：`deliverables/learning-report-summary-script/summary_generator.run(payload)`、`client.chat(...)`；HTTP 示例见 `route_example.py`。
- **样例与参考**：`learning-report-summary-script/examples/` 下输入输出样例；`learning-report-summary-ai-prd.md` 为完整 PRD。

## 2. 目录结构

```text
deliverables/
├── learning-report-summary-ai-prd.md
├── learning-report-summary-ai-test-report.md
├── learning-report-summary-bundle-readme.md
├── learning-report-summary-bundle-manifest.md
└── learning-report-summary-script/
    ├── summary_generator.py
    ├── client.py
    ├── prompt_summary.txt
    ├── route_example.py
    ├── demo.py
    ├── test_summary.py
    ├── examples/
    │   ├── input.json
    │   └── output_sample.json
    └── README.md
```

## 3. 入口文件

| 类型 | 路径 | 作用 |
|---|---|---|
| 核心生成器 | `learning-report-summary-script/summary_generator.py` | 输入标准化、组 Prompt、调客户端、返回 `{summary}` |
| 模型客户端 | `learning-report-summary-script/client.py` | 请求多模态/视觉 API |
| Route 示例 | `learning-report-summary-script/route_example.py` | Flask POST `/summary` 示例 |
| Demo | `learning-report-summary-script/demo.py` | CLI 本地验证 |
| 测试 | `learning-report-summary-script/test_summary.py` | 单元测试（需 pytest） |

## 4. 配置项

| 配置项 | 是否必填 | 默认值 / 来源 | 说明 |
|---|---|---|---|
| CHAT_URL | 是（真实调用时） | 环境变量 | 对话/多模态 API 地址 |
| API_KEY | 是（真实调用时） | 环境变量 | Bearer 鉴权 |

## 5. 调用方式

### 5.1 CLI / Demo

```bash
cd deliverables/learning-report-summary-script
python3 demo.py --input examples/input.json
```

### 5.2 HTTP / Route（需安装 Flask）

```bash
export API_KEY=xxx CHAT_URL=xxx
python3 route_example.py
curl -X POST http://127.0.0.1:5000/summary -H "Content-Type: application/json" -d @examples/input.json
```

### 5.3 输入输出样例

| 类型 | 路径 | 说明 |
|---|---|---|
| 输入样例 | `learning-report-summary-script/examples/input.json` | focus_image, subject, time_range |
| 输出样例 | `learning-report-summary-script/examples/output_sample.json` | `{ "summary": "..." }` |

## 6. 验证命令

```bash
cd deliverables/learning-report-summary-script
python3 -m pytest test_summary.py -v
```

## 7. 已知限制

- 真实调用需配置 CHAT_URL、API_KEY；多模态接口需支持图片+文本。
- 不包含鉴权、CORS、监控，由接入方补齐。

## 8. 目标项目还需补的能力

- 鉴权 / Secret 注入
- CORS / 网关放行
- 监控 / 日志 / traceId
- 正式环境配置
