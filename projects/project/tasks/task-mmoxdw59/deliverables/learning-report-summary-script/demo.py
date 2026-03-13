#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo 脚本：从 JSON 文件或命令行读取输入，调用生成器，输出总结文本。
用法：
  python demo.py --input examples/input.json
  python demo.py --subject 数学 --time "14:00-15:30" --image-url "https://..."
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# 保证可引用同目录模块
sys.path.insert(0, str(Path(__file__).resolve().parent))
from summary_generator import run


def main() -> int:
    ap = argparse.ArgumentParser(description="学习报告总结：走神专注度图片+科目+时间 → 总结文本")
    ap.add_argument("--input", "-i", help="输入 JSON 文件路径（含 focus_image, subject, time_range）")
    ap.add_argument("--subject", "-s", default="数学", help="科目")
    ap.add_argument("--time", "-t", default="未指定时间", dest="time_range", help="时间范围")
    ap.add_argument("--image-url", "--image", default="", dest="focus_image", help="专注度图片 URL 或 base64")
    ap.add_argument("--mock", action="store_true", help="使用 Mock 模式，不请求真实 API，用于测试跑通")
    args = ap.parse_args()

    if args.input:
        path = Path(args.input)
        if not path.exists():
            print(f"错误：文件不存在 {path}", file=sys.stderr)
            return 1
        payload = json.loads(path.read_text(encoding="utf-8"))
    else:
        payload = {
            "focus_image": args.focus_image or "https://example.com/focus-chart.png",
            "subject": args.subject,
            "time_range": args.time_range,
        }

    try:
        result = run(payload, use_mock=args.mock or (__import__("os").environ.get("USE_MOCK", "").strip() in ("1", "true", "yes")))
        print(result.get("summary", ""))
        return 0
    except ValueError as e:
        print(f"输入错误：{e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"调用失败：{e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
