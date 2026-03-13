# -*- coding: utf-8 -*-
"""
单元测试：输入标准化、run() 返回结构、缺图时报错。
不依赖真实 API 调用时，可 mock client.chat。
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

# 保证可引用同目录模块
sys.path.insert(0, str(Path(__file__).resolve().parent))
from summary_generator import normalize_input, run


def test_normalize_input_full():
    payload = {
        "focus_image": "https://example.com/chart.png",
        "subject": "数学",
        "time_range": "14:00-15:30",
    }
    img, subj, tr = normalize_input(payload)
    assert img == "https://example.com/chart.png"
    assert subj == "数学"
    assert tr == "14:00-15:30"


def test_normalize_input_missing_image():
    with pytest.raises(ValueError, match="缺少专注度图片"):
        normalize_input({"subject": "数学", "time_range": "14:00-15:30"})


def test_normalize_input_fallback_subject_time():
    payload = {"focus_image": "https://a.com/b.png"}
    img, subj, tr = normalize_input(payload)
    assert img == "https://a.com/b.png"
    assert subj == "未指定科目"
    assert tr == "未指定时间"


@patch("summary_generator.generate_summary", return_value="本段时间数学学习专注度良好。")
def test_run_returns_summary(mock_gen):
    payload = {
        "focus_image": "https://example.com/chart.png",
        "subject": "数学",
        "time_range": "14:00-15:30",
    }
    result = run(payload)
    assert "summary" in result
    assert result["summary"] == "本段时间数学学习专注度良好。"


def test_run_missing_image():
    with pytest.raises(ValueError, match="缺少专注度图片"):
        run({"subject": "数学"})
