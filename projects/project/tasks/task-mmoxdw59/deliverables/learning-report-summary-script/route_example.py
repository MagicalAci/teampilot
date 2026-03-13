# -*- coding: utf-8 -*-
"""
HTTP 接入示例：将「走神专注度图片+科目+时间→总结文本」暴露为 POST API。
可挂载到 Flask / FastAPI 等框架。此处为可独立运行的最小示例（需安装 flask）。
运行：pip install flask && python route_example.py
请求：
  curl -X POST http://127.0.0.1:5000/summary \\
    -H "Content-Type: application/json" \\
    -d '{"focus_image":"https://example.com/chart.png","subject":"数学","time_range":"14:00-15:30"}'
"""
from __future__ import annotations

import os

try:
    from flask import Flask, request, jsonify
    _HAS_FLASK = True
except ImportError:
    _HAS_FLASK = False

from summary_generator import run

if _HAS_FLASK:
    app = Flask(__name__)

    @app.route("/summary", methods=["POST"])
    def summary():
        """POST body: JSON { focus_image, subject?, time_range? } -> { summary }"""
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400
        payload = request.get_json() or {}
        try:
            result = run(
                payload,
                chat_url=os.environ.get("CHAT_URL"),
                api_key=os.environ.get("API_KEY"),
            )
            return jsonify(result)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
else:
    app = None


if __name__ == "__main__":
    if not _HAS_FLASK or app is None:
        raise SystemExit("请先安装: pip install flask")
    app.run(host="0.0.0.0", port=5000, debug=True)
