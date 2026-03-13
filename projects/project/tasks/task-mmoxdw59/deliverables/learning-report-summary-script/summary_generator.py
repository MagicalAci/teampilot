# -*- coding: utf-8 -*-
"""
核心生成器：输入标准化、组装 Prompt、调用客户端、返回总结文本。
与 PRD 第一章输入结构、第四章运行顺序一致。
"""
from __future__ import annotations

import os
from pathlib import Path

from client import chat

# 回退口径（与 PRD 一致）
DEFAULT_SUBJECT = "未指定科目"
DEFAULT_TIME_RANGE = "未指定时间"


def _load_prompt() -> str:
    prompt_path = Path(__file__).resolve().parent / "prompt_summary.txt"
    if prompt_path.exists():
        return prompt_path.read_text(encoding="utf-8").strip()
    return "请根据给定的走神/专注度图片、科目与时间，生成一段简短的学习总结文本。"


def normalize_input(payload: dict) -> tuple[str, str, str]:
    """
    校验并回退：focus_image 必填；subject、time_range 可回退。
    返回 (focus_image, subject, time_range)。
    """
    focus_image = (payload.get("focus_image") or "").strip()
    if not focus_image:
        raise ValueError("缺少专注度图片")
    subject = (payload.get("subject") or DEFAULT_SUBJECT).strip() or DEFAULT_SUBJECT
    time_range = (payload.get("time_range") or DEFAULT_TIME_RANGE).strip() or DEFAULT_TIME_RANGE
    return focus_image, subject, time_range


def generate_summary(
    focus_image: str,
    subject: str,
    time_range: str,
    *,
    chat_url: str | None = None,
    model: str | None = None,
    api_key: str | None = None,
    use_mock: bool | None = None,
) -> str:
    """单阶段生成总结文本。use_mock 或 USE_MOCK=1 时走 Mock，便于测试跑通。"""
    prompt_text = _load_prompt()
    return chat(
        focus_image,
        subject,
        time_range,
        prompt_text,
        chat_url=chat_url,
        model=model or "Doubao-Seed-2.0-Pro-0215",
        api_key=api_key,
        use_mock=use_mock,
    )


def run(payload: dict, use_mock: bool | None = None, **kwargs) -> dict:
    """
    对外入口：接收 PRD 约定的输入 JSON，返回 {"summary": "..."}。
    use_mock=True 或 USE_MOCK=1 时走 Mock，便于无 API 时测试跑通。
    """
    focus_image, subject, time_range = normalize_input(payload)
    summary = generate_summary(
        focus_image, subject, time_range,
        use_mock=use_mock,
        **kwargs,
    )
    return {"summary": summary}
