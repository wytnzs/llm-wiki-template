---
title: theme-tech-dark
type: skill_reference
status: active
tags: [公众号, 主题, 科技暗色]
created: 2026-07-12
updated: 2026-07-12
---

# 科技暗色

> 现代、冲击、利落。适用于观点文、工具文、评测、方法论、认知输出类内容。
> 暗色背景 + 亮色强调，营造科技感和冲击力。默认配 Cyan 青，可选紫/橙变体。

---

## 一、设计变量速查

| 用途 | 色值 | CSS 变量名 |
|------|------|-----------|
| 正文背景 | `#0D0D0D` (极黑) | `--bg` |
| 正文颜色 | `#E0E0E0` (浅灰) | `--text` |
| 标题主色（h1/h2） | `#FFFFFF` | `--heading` |
| 标题深色（h3/strong） | `#E0E0E0` | `--heading-dark` |
| 强调色（装饰/标签/下划线） | `#00D4FF` (青) | `--accent` |
| 引用背景 | `#1A1A2E` | `--quote-bg` |
| 引用左边框 | `#00D4FF` | `--quote-border` |
| 引用文字 | `#A0B0C0` | `--quote-text` |
| 表格表头背景 | `#00D4FF` | `--th-bg` |
| 表格表头文字 | `#0D0D0D` | `--th-text` |
| 表格行间隔色 | `#1A1A2E` | `--tr-alt` |
| 表格边框 | `#2A2A3E` | `--table-border` |
| 分割线 | `#2A2A3E` | `--hr` |
| 脚注文字 | `#6A7A8A` | `--muted` |
| 正文下划线 | `#00D4FF` (底部 2px) | `--underline` |
| 浅强调色 | `rgba(0,212,255,0.12)` | `--accent-soft` |

### 强调色变体

用户可选以下变体替代默认青色：

| 变体 | 强调色 | 适用场景 |
|------|-------|---------|
| 青色（默认） | `#00D4FF` | 科技/AI/方法论 |
| 紫色 | `#C442F5` | 认知输出/深度观点 |
| 橙色 | `#FF6B35` | 反常识/批判性观点 |

## 二、字体

- **正文/标题**：`"Noto Sans SC", -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif` — 无衬线更现代
- **数据/序号/标签**：`"Space Mono", "IBM Plex Mono", ui-monospace, monospace`
- **金句/强调**：`"Noto Sans SC", sans-serif`（加粗 900 字重）

## 三、封面颜色方案

| 元素 | 色值（青色变体） | 紫色变体 | 橙色变体 |
|------|----------------|---------|---------|
| 基底渐变 | `#0D0D0D → #1A1A2E → #16213E` | `#0D0D0D → #1A0A2E → #2A0A3E` | `#0D0D0D → #2E1A0A → #3E200A` |
| 柔光色 | `rgba(0,212,255,0.10)` | `rgba(196,66,245,0.10)` | `rgba(255,107,53,0.10)` |
| 柔光色（辅） | `rgba(22,33,62,0.12)` | `rgba(42,10,62,0.12)` | `rgba(62,32,10,0.12)` |
| 环/点强调色 | `#00D4FF` | `#C442F5` | `#FF6B35` |
| 标题文字 | `#FFFFFF` | `#FFFFFF` | `#FFFFFF` |
| 副标题文字 | `rgba(255,255,255,0.55)` | `rgba(255,255,255,0.55)` | `rgba(255,255,255,0.55)` |

## 四、正文排版 CSS（内联样式）

### 基础容器

```css
body { background: #0D0D0D; font-family: "Noto Sans SC", -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif; max-width: 677px; margin: 0 auto; padding: 20px 16px; font-size: 16px; line-height: 1.8; color: #E0E0E0; }
```

### 标题

```css
h1 { font-size: 24px; font-weight: 800; color: #FFFFFF; margin: 24px 0 12px; letter-spacing: -0.02em; }
h2 { font-size: 19px; font-weight: 700; color: #FFFFFF; border-left: 4px solid #00D4FF; padding-left: 12px; margin: 20px 0 10px; }
h3 { font-size: 17px; font-weight: 700; color: #FFFFFF; margin: 16px 0 8px; }
```

### 正文

```css
p { margin: 0 0 12px; color: #E0E0E0; }
strong { color: #FFFFFF; }
```

### 引用

```css
blockquote { border-left: 3px solid #00D4FF; background: #1A1A2E; padding: 12px 16px; margin: 16px 0; color: #A0B0C0; border-radius: 0 4px 4px 0; font-size: 15px; }
```

### 表格

```css
table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 15px; }
th { background: #00D4FF; color: #0D0D0D; padding: 10px 12px; text-align: left; font-weight: 600; }
td { padding: 10px 12px; border-bottom: 1px solid #2A2A3E; color: #E0E0E0; }
tr:nth-child(even) td { background: #1A1A2E; }
```

### 强调与分割

```css
.em-accent { color: #00D4FF; font-weight: 700; }
hr { border: none; border-top: 1px solid #2A2A3E; margin: 24px 0; }
.footer { margin-top: 32px; padding-top: 16px; border-top: 1px solid #2A2A3E; font-size: 14px; color: #6A7A8A; }
```

### 配图卡片

```css
.illu-card { position: relative; width: 100%; max-width: 677px; margin: 24px auto; border-radius: 12px; overflow: hidden; box-sizing: border-box; }
```

## 五、下划线/标记风格

正文关键词下划线：`border-bottom: 2px solid #00D4FF; font-weight: 600;`

若使用强调色变体，下划线色值同步替换为对应变体的强调色。

## 六、配图卡片强调色

| 卡片元素 | 色值（青色变体） |
|---------|----------------|
| 强调左边框 | `#00D4FF` 或 `rgba(0,212,255,0.6)` |
| 序号文字 | `#00D4FF` |
| 暗底卡片背景 | `#1A1A2E` |
| 下载按钮悬浮色 | `#00D4FF` |
