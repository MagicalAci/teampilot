# 学习报告总结 - AI 脚本说明

> 输入：走神专注度图片、科目、时间 → 输出：总结文本  
> 与 `learning-report-summary-ai-prd.md` 及任务交付物同目录。

## 1. 交付概览

- **能力**：根据「走神/专注度」图片 + 科目 + 时间，生成一段学习报告总结文本。
- **可直接接入**：`summary_generator.run(payload)`、`client.chat(...)`、HTTP 示例见 `route_example.py`。
- **样例与测试**：`examples/input.json`、`examples/output_sample.json`、`test_summary.py`。

## 2. 目录结构

```text
learning-report-summary-script/
├── summary_generator.py   # 核心生成器
├── client.py              # 模型客户端
├── prompt_summary.txt     # Prompt 正文
├── route_example.py       # HTTP 接入示例（Flask）
├── demo.py                # CLI 本地验证
├── test_summary.py        # 单元测试
├── examples/
│   ├── input.json
│   └── output_sample.json
└── README.md
```

## 3. 入口与职责

| 类型         | 路径                   | 作用                         |
|--------------|------------------------|------------------------------|
| 核心生成器   | `summary_generator.py` | 输入标准化、组 Prompt、调客户端、返回 `{summary}` |
| 模型客户端   | `client.py`            | 请求多模态/视觉 API          |
| Route 示例   | `route_example.py`     | POST `/summary` HTTP 示例    |
| Demo         | `demo.py`              | 本地 CLI 验证                |
| 测试         | `test_summary.py`      | 输入校验与 run 结构          |

## 4. 配置项

| 配置项     | 必填 | 默认/来源       | 说明           |
|------------|------|-----------------|----------------|
| `CHAT_URL` | 是*  | 环境变量        | 对话/多模态 API 地址 |
| `API_KEY`  | 是*  | 环境变量        | Bearer 鉴权    |
| * 本地单测可无真实 API |  |  |  |

## 5. 调用方式

### 5.1 CLI / Demo

```bash
python demo.py --input examples/input.json
# 或
python demo.py --subject 数学 --time "14:00-15:30" --image-url "https://..."
```

### 5.2 HTTP（需安装 Flask）

```bash
export API_KEY=your_key CHAT_URL=your_chat_url
python route_example.py
# 另终端：
curl -X POST http://127.0.0.1:5000/summary \
  -H "Content-Type: application/json" \
  -d @examples/input.json
```

### 5.3 输入输出样例

| 类型     | 路径                        | 说明           |
|----------|-----------------------------|----------------|
| 输入样例 | `examples/input.json`       | 与 PRD 一致    |
| 输出样例 | `examples/output_sample.json` | 含 `summary` 字段 |

## 6. 验证命令

```bash
# 单元测试（不请求真实 API）
pytest test_summary.py -v
# 或
python -m pytest test_summary.py -v
```

## 7. 已知限制

- 图片格式依赖平台多模态能力（URL 或 base64）。
- 未包含鉴权、CORS、网关、监控；由接入方补齐。

## 8. 目标项目需补齐

- 鉴权 / Secret 注入
- CORS / 网关放行
- 监控 / 日志 / traceId
- 正式环境 `CHAT_URL` 与 `API_KEY`
