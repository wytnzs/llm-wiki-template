---
title: web-research
type: skill_reference
status: active
tags: []
created: 2026-04-29
updated: 2026-04-29
---
# 调研方法手册

> 适用于 gzh-pipeline 调研阶段。优先级：WebFetch → WebSearch → CDP 浏览器。

---

## 调研优先级

### 1. WebFetch（首选，最可靠）

根据主题类型直接抓取目标网站，不需要通过搜索引擎：

| 主题类型 | 目标网站 |
|---------|---------|
| 科技趋势/AI | 36kr、虎嗅、钛媒体 |
| 保险/金融 | 中国保险行业协会、财新保险频道 |
| 政策/法规 | 政府官网（gov.cn）、国家部委网站 |
| 综合热点 | 财新、澎湃、凤凰网 |
| 社区讨论 | 知乎、豆瓣 |

直接用 Claude 的 WebFetch 工具抓取内容。

### 2. WebSearch（补充）

用 Claude 原生的 WebSearch 搜索关键词补充信息。

**乱码处理**：如果搜索结果乱码（百度等搜索引擎对自动化请求的常见现象），直接弃用，切换到 WebFetch 或 CDP。

### 3. CDP 浏览器（fallback）

当 WebFetch 和 WebSearch 都拿不到干净内容时，使用 web-access skill 的 CDP 代理。

**前置检查**：

```bash
node ~/.claude/skills/web-access/scripts/check-deps.mjs
```

**通过后操作**：

1. 创建新 tab 打开目标网站
2. 用 eval 提取内容（必须用 `innerText` 避免乱码）
3. 完成后关闭自己创建的 tab

---

## 增量保存（必须）

每获取一批信息，立即追加写入 `drafts/调研简报.md`：

```bash
cat >> drafts/调研简报.md << 'EOF'

## [来源名称]

**链接**：URL

**要点**：
- 要点1
- 要点2

EOF
```

**不要等全部完成才写文件。**
