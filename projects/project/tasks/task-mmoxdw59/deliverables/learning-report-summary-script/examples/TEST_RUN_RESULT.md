# 测试运行结果

> 本地执行：`python3 run_tests.py` 与 `python3 demo.py --input examples/input.json --mock`

## 1. 单元测试（run_tests.py）

```text
test_fallback_subject_time ... ok
test_full_input ... ok
test_missing_image_raises ... ok
test_run_missing_image_raises ... ok
test_run_returns_summary ... ok
test_run_mock_returns_summary_with_subject_time ... ok
test_run_mock_with_base64_image_placeholder ... ok

Ran 7 tests in 0.001s
OK
```

- **输入标准化**：必填 `focus_image`、回退 `subject`/`time_range` 通过。
- **缺图报错**：缺 `focus_image` 时抛出 `ValueError("缺少专注度图片")`。
- **Mock 端到端**：`run(payload, use_mock=True)` 返回 `{"summary": "..."}`，且 summary 中含科目、时间。

## 2. 测试数据说明

| 文件 | 说明 |
|------|------|
| `input.json` | 图片为 URL，科目数学，时间 2025-03-13 14:00-15:30 |
| `input_base64.json` | 图片为 1×1 透明 PNG base64，用于验证 base64 路径 |
| `input_multi_subject.json` | 科目英语，时间 09:00-10:00，用于多科目场景 |

## 3. Mock 运行输出（AI 生产总结文本）

使用 `--mock` 不请求真实 API，得到确定性的「总结文本」输出，便于验收流程。

**输入**：`examples/input.json`（URL + 数学 + 时间）

**输出**：
```text
[Mock] 本段时间数学学习专注度良好，时间范围：2025-03-13 14:00-15:30。建议保持当前节奏。
```

**输入**：`examples/input_base64.json`（base64 图片 + 数学 + 时间）

**输出**：
```text
[Mock] 本段时间数学学习专注度良好，时间范围：2025-03-13 14:00-15:30。建议保持当前节奏。
```

**输入**：`examples/input_multi_subject.json`（URL + 英语 + 09:00-10:00）

**输出**：
```text
[Mock] 本段时间英语学习专注度良好，时间范围：2025-03-13 09:00-10:00。建议保持当前节奏。
```

## 4. 生成的测试输出文件（JSON）

| 文件 | 内容 |
|------|------|
| `output_test_run_url.json` | 对 input.json 的 run 输出 `{"summary": "..."}` |
| `output_test_run_base64.json` | 对 input_base64.json 的 run 输出 |
| `output_test_run_multi.json` | 对 input_multi_subject.json 的 run 输出 |

以上为 Mock 模式下的测试输出结果；真实 API 调用时由模型生成内容，格式仍为 `{"summary": "一段总结文本"}`。
