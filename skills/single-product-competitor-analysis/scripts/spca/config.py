from pathlib import Path

CHANNEL_DEFAULTS = {
    "web": {"tier": "A", "pool": "official_pages", "platform": "official"},
    "reviews": {"tier": "B", "pool": "reviews_feedback", "platform": "review"},
    "social": {"tier": "B", "pool": "social_sentiment", "platform": "social"},
    "seo": {"tier": "A", "pool": "seo_content", "platform": "seo"},
    "pricing": {"tier": "A", "pool": "pricing_monetization", "platform": "pricing"},
    "manual": {
        "tier": "A",
        "pool": "screenshots_recordings",
        "platform": "manual",
    },
}

EVIDENCE_POOLS = [
    "official_pages",
    "feature_structure",
    "pricing_monetization",
    "reviews_feedback",
    "social_sentiment",
    "seo_content",
    "screenshots_recordings",
]

CHANNEL_BACKEND_PRIORITY = {
    "web": ["mcp:firecrawl", "browser:cursor-ide-browser", "web:search-fetch"],
    "reviews": ["mcp:app-insight", "web:search-fetch"],
    "social": [
        "mcp:user-xiaohongshu",
        "mcp:user-bilibili",
        "mcp:user-weibo",
        "web:search-fetch",
        "shell:local-crawlers(optional)",
    ],
    "seo": ["mcp:firecrawl", "web:search-fetch"],
    "pricing": ["browser:cursor-ide-browser", "web:search-fetch"],
    "manual": ["user-upload"],
}

CHANNEL_SAMPLE_TARGETS = {
    "web": 200,
    "reviews": 200,
    "social": 200,
    "seo": 200,
    "pricing": 200,
    "manual": 1,
}

CHANNEL_PLATFORM_FALLBACKS = {
    "web": "web",
    "reviews": "appstore",
    "seo": "seo",
    "pricing": "pricing",
    "manual": "manual",
}

CHANNEL_OUTPUT_PLATFORMS = {
    "web": ["web"],
    "reviews": ["appstore"],
    "social": ["xiaohongshu", "weibo", "bilibili", "zhihu"],
    "seo": ["seo"],
    "pricing": ["pricing"],
    "manual": ["manual"],
}

PLATFORM_TO_CHANNEL = {
    "web": "web",
    "appstore": "reviews",
    "xiaohongshu": "social",
    "weibo": "social",
    "bilibili": "social",
    "zhihu": "social",
    "social": "social",
    "seo": "seo",
    "pricing": "pricing",
    "manual": "manual",
}

PLATFORM_BACKEND_PRIORITY = {
    "web": CHANNEL_BACKEND_PRIORITY["web"],
    "appstore": ["mcp:user-app-insight", "web:search-fetch"],
    "xiaohongshu": ["mcp:user-xiaohongshu", "web:search-fetch", "shell:local-crawlers(optional)"],
    "weibo": ["mcp:user-weibo", "web:search-fetch", "shell:local-crawlers(optional)"],
    "bilibili": ["mcp:user-bilibili", "web:search-fetch"],
    "zhihu": ["mcp:firecrawl", "web:search-fetch"],
    "seo": CHANNEL_BACKEND_PRIORITY["seo"],
    "pricing": CHANNEL_BACKEND_PRIORITY["pricing"],
    "manual": CHANNEL_BACKEND_PRIORITY["manual"],
}

PLATFORM_SAMPLE_TARGETS = {
    "web": CHANNEL_SAMPLE_TARGETS["web"],
    "appstore": CHANNEL_SAMPLE_TARGETS["reviews"],
    "xiaohongshu": 200,
    "weibo": 200,
    "bilibili": 200,
    "zhihu": 200,
    "seo": CHANNEL_SAMPLE_TARGETS["seo"],
    "pricing": CHANNEL_SAMPLE_TARGETS["pricing"],
    "manual": CHANNEL_SAMPLE_TARGETS["manual"],
}

PLATFORM_OUTPUT_ORDER = [
    "web",
    "appstore",
    "xiaohongshu",
    "weibo",
    "bilibili",
    "zhihu",
    "seo",
    "pricing",
    "manual",
]

REQUIRED_REPORT_HEADINGS = [
    "## 1. 总结",
    "## 2. 分析建模",
    "## 3. 产品分析",
    "## 4. 用户分析",
    "## 5. 社媒分析",
    "## 6. SEO 与内容分析",
    "## 7. 商业化分析",
    "## 8. 竞争判断",
    "## 9. 对我方建议",
    "## 10. 证据附录",
]


def repo_root_from_script(script_path: Path) -> Path:
    return script_path.resolve().parents[4]
