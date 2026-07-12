---
title: theme-deepblue
type: skill_reference
status: active
tags: [公众号, 主题, 深蓝商务]
created: 2026-07-12
updated: 2026-07-12
---

# 深蓝商务（默认主题）

> 理性、专业、可信。适用于案例文、解读文、保险条款、数据分析。
> 当前管线的默认风格，从 gzh-pipeline SKILL.md 硬编码 CSS 提取为独立主题。

---

## 一、设计变量速查

| 用途 | 色值 | CSS 变量名 |
|------|------|-----------|
| 正文背景 | `#FFFFFF` | `--bg` |
| 正文颜色 | `#1A1A1A` | `--text` |
| 标题主色（h1/h2） | `#102542` | `--heading` |
| 标题深色（h3/strong） | `#0A1931` | `--heading-dark` |
| 强调色（装饰/标签/下划线） | `#F77F00` (橙色) | `--accent` |
| 引用背景 | `#F7F9FC` | `--quote-bg` |
| 引用左边框 | `#F77F00` | `--quote-border` |
| 引用文字 | `#4A4A4A` | `--quote-text` |
| 表格表头背景 | `#102542` | `--th-bg` |
| 表格表头文字 | `#FFFFFF` | `--th-text` |
| 表格行间隔色 | `#F7F9FC` | `--tr-alt` |
| 表格边框 | `#E5EAF2` | `--table-border` |
| 分割线 | `#E5EAF2` | `--hr` |
| 脚注文字 | `#86909C` | `--muted` |
| 正文下划线 | `#F77F00` (底部 2px) | `--underline` |
| 浅强调色 | `rgba(247,127,0,0.10)` | `--accent-soft` |

## 二、字体

- 正文/标签：`"Noto Sans SC", -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif`
- 标题/金句：`"Noto Serif SC", "Songti SC", serif`（金句使用）
- 序号/元数据：`"IBM Plex Mono", ui-monospace, monospace`

## 三、封面颜色方案

| 元素 | 色值 |
|------|------|
| 基底渐变 | `#0A1931 → #102542 → #162D5A` |
| 柔光色（橙色） | `rgba(247,127,0,0.07)` |
| 柔光色（深蓝） | `rgba(57,73,171,0.10)` |
| 环/点强调色 | `#F77F00` |
| 标题文字 | `#FFFFFF` |
| 副标题文字 | `rgba(255,255,255,0.62)` |

## 四、正文排版 CSS（内联样式）

排版时直接使用以下 CSS。所有样式已写为内联可用格式。

### 基础容器

```css
body { background: #FFFFFF; font-family: "Noto Sans SC", -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif; max-width: 677px; margin: 0 auto; padding: 20px 16px; font-size: 16px; line-height: 1.8; color: #1A1A1A; }
```

### 标题

```css
h1 { font-size: 24px; font-weight: 800; color: #102542; margin: 24px 0 12px; }
h2 { font-size: 19px; font-weight: 700; color: #102542; border-left: 4px solid #F77F00; padding-left: 12px; margin: 20px 0 10px; }
h3 { font-size: 17px; font-weight: 700; color: #0A1931; margin: 16px 0 8px; }
```

### 正文

```css
p { margin: 0 0 12px; color: #1A1A1A; }
strong { color: #0A1931; }
```

### 引用

```css
blockquote { border-left: 3px solid #F77F00; background: #F7F9FC; padding: 12px 16px; margin: 16px 0; color: #4A4A4A; border-radius: 0 4px 4px 0; font-size: 15px; }
```

### 表格

```css
table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 15px; }
th { background: #102542; color: #FFFFFF; padding: 10px 12px; text-align: left; font-weight: 600; }
td { padding: 10px 12px; border-bottom: 1px solid #E5EAF2; }
tr:nth-child(even) td { background: #F7F9FC; }
```

### 强调与分割

```css
.em-accent { color: #F77F00; font-weight: 700; }
hr { border: none; border-top: 1px solid #E5EAF2; margin: 24px 0; }
.footer { margin-top: 32px; padding-top: 16px; border-top: 1px solid #E5EAF2; font-size: 14px; color: #86909C; }
```

### 配图卡片

```css
.illu-card { position: relative; width: 100%; max-width: 677px; margin: 24px auto; border-radius: 12px; overflow: hidden; box-sizing: border-box; }
```

## 五、下划线/标记风格

正文关键词下划线：`border-bottom: 2px solid #F77F00; font-weight: 600;`

## 六、配图卡片强调色

| 卡片元素 | 色值 |
|---------|------|
| 强调左边框 | `#F77F00` 或 `rgba(247,127,0,0.6)` |
| 序号文字 | `#315d93` |
| 暗底卡片背景 | `#0a1f3d` |
| 下载按钮悬浮色 | `#F77F00` |
