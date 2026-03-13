#!/bin/bash
# 使用 Mock 模式跑通 demo，并保存测试输出到 examples/output_test_run.json
set -e
cd "$(dirname "$0")"
echo "=== 测试数据：input.json (URL) ==="
python3 demo.py --input examples/input.json --mock > examples/summary_output_url.txt 2>&1
cat examples/summary_output_url.txt
echo ""
echo "=== 测试数据：input_base64.json (base64 图片) ==="
python3 demo.py --input examples/input_base64.json --mock > examples/summary_output_base64.txt 2>&1
cat examples/summary_output_base64.txt
echo ""
echo "=== 生成完整 JSON 输出 (output_test_run.json) ==="
python3 -c "
import json, sys
sys.path.insert(0, '.')
from summary_generator import run
for name, path in [('url', 'examples/input.json'), ('base64', 'examples/input_base64.json'), ('multi', 'examples/input_multi_subject.json')]:
    with open(path) as f:
        payload = json.load(f)
    out = run(payload, use_mock=True)
    with open(f'examples/output_test_run_{name}.json', 'w', encoding='utf-8') as g:
        json.dump(out, g, ensure_ascii=False, indent=2)
    print(f'{name}:', out['summary'][:60] + '...')
"
echo "Done. 输出文件: examples/summary_output_*.txt, examples/output_test_run_*.json"
