#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不依赖 pytest 的测试运行器：用 unittest 跑通全部用例。
用法：python3 run_tests.py
"""
from __future__ import annotations

import sys
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from summary_generator import normalize_input, run


class TestNormalizeInput(TestCase):
    def test_full_input(self):
        payload = {
            "focus_image": "https://example.com/chart.png",
            "subject": "数学",
            "time_range": "14:00-15:30",
        }
        img, subj, tr = normalize_input(payload)
        self.assertEqual(img, "https://example.com/chart.png")
        self.assertEqual(subj, "数学")
        self.assertEqual(tr, "14:00-15:30")

    def test_missing_image_raises(self):
        with self.assertRaises(ValueError) as ctx:
            normalize_input({"subject": "数学", "time_range": "14:00-15:30"})
        self.assertIn("缺少专注度图片", str(ctx.exception))

    def test_fallback_subject_time(self):
        payload = {"focus_image": "https://a.com/b.png"}
        img, subj, tr = normalize_input(payload)
        self.assertEqual(img, "https://a.com/b.png")
        self.assertEqual(subj, "未指定科目")
        self.assertEqual(tr, "未指定时间")


class TestRun(TestCase):
    @patch("summary_generator.generate_summary", return_value="本段时间数学学习专注度良好。")
    def test_run_returns_summary(self, mock_gen):
        payload = {
            "focus_image": "https://example.com/chart.png",
            "subject": "数学",
            "time_range": "14:00-15:30",
        }
        result = run(payload)
        self.assertIn("summary", result)
        self.assertEqual(result["summary"], "本段时间数学学习专注度良好。")

    def test_run_missing_image_raises(self):
        with self.assertRaises(ValueError) as ctx:
            run({"subject": "数学"})
        self.assertIn("缺少专注度图片", str(ctx.exception))


class TestRunWithMockE2E(TestCase):
    """端到端：真实调用 run(use_mock=True)，不请求 API，验证输出结构与内容。"""

    def test_run_mock_returns_summary_with_subject_time(self):
        payload = {
            "focus_image": "https://example.com/focus.png",
            "subject": "英语",
            "time_range": "2025-03-13 09:00-10:00",
        }
        result = run(payload, use_mock=True)
        self.assertIn("summary", result)
        self.assertIn("英语", result["summary"])
        self.assertIn("2025-03-13", result["summary"])

    def test_run_mock_with_base64_image_placeholder(self):
        # 使用 1x1 透明 PNG 的 base64 作为测试数据
        tiny_png_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
        payload = {
            "focus_image": f"data:image/png;base64,{tiny_png_b64}",
            "subject": "数学",
            "time_range": "14:00-15:30",
        }
        result = run(payload, use_mock=True)
        self.assertIn("summary", result)
        self.assertTrue(len(result["summary"]) > 0)


if __name__ == "__main__":
    from unittest import TestLoader, TextTestRunner
    loader = TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
