# 工具调用与安装协议

这份协议定义搜索子代理在每个平台上如何选工具、如何做初始化、以及工具缺失时如何处理。

核心原则：

- 先检查工具状态，再开始采集
- 默认优先用已接入 MCP，其次用浏览器 / WebSearch / WebFetch，再其次用本地 crawler
- 没安装要安装，没登录要初始化，不能直接假设工具可用
- 不能因为工具没准备好，就跳过该平台或偷换成“凭空总结”

## 1. 开始前必须先看

- 本文件
- `platform-output-contract.md`
- `subagent-search-protocol.md`

如果当前项目仓库里额外维护了 MCP / crawler 索引，可以把它们当“项目级补充信息”再读取，但不是启动本 skill 的前置要求。

目的：

- 确认当前 skill 约定了哪些默认工具优先级
- 确认哪些工具需要登录、Cookie 或扫码
- 确认本地 crawler 是否可作为降级方案

## 2. 平台级工具优先级

| 平台 | 首选工具 | 初始化要求 | 降级方案 | 最终产物 |
|---|---|---|---|---|
| `web` | Firecrawl + 浏览器 | 确认 MCP 可用 | WebFetch / WebSearch | `03-platforms/web/summary.md` `03-platforms/web/data.csv` |
| `appstore` | AppInsight | 确认 MCP 可用 | WebSearch + WebFetch | `03-platforms/appstore/summary.md` `03-platforms/appstore/data.csv` |
| `xiaohongshu` | 小红书 MCP + 本地 crawler detail | 首次使用检查登录 / 扫码 | WebSearch + WebFetch + 本地 crawler | `03-platforms/xiaohongshu/summary.md` `03-platforms/xiaohongshu/data.csv` |
| `weibo` | 微博 MCP | 检查 Cookie | WebSearch + WebFetch + 本地 crawler | `03-platforms/weibo/summary.md` `03-platforms/weibo/data.csv` |
| `bilibili` | B站 MCP | 确认 MCP 可用 | WebSearch + WebFetch | `03-platforms/bilibili/summary.md` `03-platforms/bilibili/data.csv` |
| `zhihu` | Firecrawl + WebSearch | 无专用 MCP 时直接走抓取链路 | WebFetch | `03-platforms/zhihu/summary.md` `03-platforms/zhihu/data.csv` |
| `seo` | Firecrawl + WebSearch | 确认搜索链路可用 | 浏览器 + WebFetch | `03-platforms/seo/summary.md` `03-platforms/seo/data.csv` |
| `pricing` | 浏览器 + WebFetch | 确认可访问定价页 | WebSearch | `03-platforms/pricing/summary.md` `03-platforms/pricing/data.csv` |

## 3. 工具状态处理顺序

每个平台子代理都按这个顺序执行：

1. 查工具文档和当前可用性
2. 尝试首选 MCP
3. 如果缺安装、缺登录、缺 Cookie，先完成安装或初始化
4. 如果仍不可用，记录原因并降级
5. 降级后继续采集，不允许空手进入总结阶段

### 小红书补充规则

- 如果 MCP 只能拿到帖子层信息，必须继续用本地 crawler 跑 `detail xhs` 抓评论层
- 小红书评论层不是可选增强，而是高标准交付的默认要求
- 只有当评论层因为登录、反爬或平台限制拿不到时，才允许降级，并且必须在 `summary.md` 里明确说明缺口

## 4. 必须记录的内容

子代理的 `summary.md` 必须写明：

- 实际用了什么工具
- 为什么没有用首选工具
- 是否发生安装 / 登录 / Cookie 初始化
- 当前是否处于降级模式
- 降级后有哪些证据盲区

## 5. 安装与初始化红线

- 不允许因为首选工具失效就直接跳过平台
- 不允许把“工具没装好”伪装成“平台没数据”
- 不允许只写总结、不落 `data.csv`
- 不允许跨平台共用一个 CSV
