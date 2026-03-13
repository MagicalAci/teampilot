# -*- coding: utf-8 -*-
"""
模型客户端：请求多模态/视觉 API，支持图片 URL 或 base64 + 文本。
与 PRD 输入字段 focus_image、subject、time_range 对应。
"""
from __future__ import annotations

import os
import json
from typing import Any

import urllib.request
import urllib.error


def _build_messages(focus_image: str, subject: str, time_range: str, prompt_text: str) -> list[dict[str, Any]]:
    """构建 API messages：若 focus_image 为 URL 或 base64，按平台要求放入 content."""
    # 文本部分：注入科目与时间
    user_content: list[dict[str, Any]] = [
        {"type": "text", "text": f"科目：{subject}\n时间：{time_range}\n\n{prompt_text}"}
    ]
    # 图片：URL 或 base64
    if focus_image.startswith("http://") or focus_image.startswith("https://"):
        user_content.append({"type": "image_url", "image_url": {"url": focus_image}})
    elif focus_image.startswith("data:image") or focus_image.startswith("/9j/") or len(focus_image) > 200:
        # 视为 base64
        img_url = focus_image if focus_image.startswith("data:") else f"data:image/png;base64,{focus_image}"
        user_content.append({"type": "image_url", "image_url": {"url": img_url}})
    else:
        user_content.append({"type": "text", "text": f"[图片占位：{focus_image[:80]}...]"})
    return [{"role": "user", "content": user_content}]


def chat(
    focus_image: str,
    subject: str,
    time_range: str,
    prompt_text: str,
    *,
    chat_url: str | None = None,
    model: str = "Doubao-Seed-2.0-Pro-0215",
    api_key: str | None = None,
    timeout: int = 60,
    use_mock: bool | None = None,
) -> str:
    """
    调用对话接口，返回总结文本。
    与 PRD 一致：输入 focus_image、subject、time_range；输出为 summary 文本。
    use_mock=True 或环境变量 USE_MOCK=1 时返回模拟总结，用于测试与无 API 环境跑通。
    """
    use_mock = use_mock if use_mock is not None else (os.environ.get("USE_MOCK", "").strip() in ("1", "true", "yes"))
    if use_mock:
        return f"[Mock] 本段时间{subject}学习专注度良好，时间范围：{time_range}。建议保持当前节奏。"
    chat_url = chat_url or os.environ.get("CHAT_URL", "https://fat-aibrain-large-model-engine.hellobike.cn/v1/chat/completions")
    api_key = api_key or os.environ.get("API_KEY", "")
    messages = _build_messages(focus_image, subject, time_range, prompt_text)
    body = {
        "model": model,
        "messages": messages,
        "max_tokens": 512,
        "temperature": 0.3,
    }
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        chat_url,
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    resp = urllib.request.urlopen(req, timeout=timeout)
    result = json.loads(resp.read().decode("utf-8"))
    choice = (result.get("choices") or [{}])[0]
    message = choice.get("message") or {}
    return (message.get("content") or "").strip()
