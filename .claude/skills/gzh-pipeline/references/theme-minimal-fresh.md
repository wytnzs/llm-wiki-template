---
title: theme-minimal-fresh
type: skill_reference
status: active
tags: [公众号, 主题, 极简清爽]
created: 2026-07-12
updated: 2026-07-12
---

# 极简清爽（Minimal Fresh）

> 干净、透气、现代。适用于方法论、工具文、教程、清单型内容。
> 核心气质：大留白 + 细线条 + 克制点缀。不堆色，不重底，让内容本身成为视觉重心。

---

## 一、设计变量速查

| 用途 | 色值 | CSS 变量名 |
|------|------|-----------|
| 正文背景 | `#FFFFFF` | `--bg` |
| 正文颜色 | `#333333` | `--text` |
| 标题主色（h1/h2） | `#1A1A1A` | `--heading` |
| 标题浅色（h3） | `#444444` | `--heading-mid` |
| 强调色（装饰/标签/下划线） | `#7A9E8E` (鼠尾草绿) | `--accent` |
| 引用背景 | `#F8F9FA` | `--quote-bg` |
| 引用左边框 | `#7A9E8E` | `--quote-border` |
| 引用文字 | `#666666` | `--quote-text` |
| 表格表头背景 | `#F8F9FA` | `--th-bg` |
| 表格表头文字 | `#333333` | `--th-text` |
| 表格行间隔色 | `#FBFCFC` | `--tr-alt` |
| 表格边框 | `#EEEEEE` | `--table-border` |
| 分割线 | `#EEEEEE` | `--hr` |
| 脚注文字 | `#999999` | `--muted` |
| 正文下划线 | `#7A9E8E` (底部 1.5px) | `--underline` |
| 浅强调色 | `rgba(122,158,142,0.08)` | `--accent-soft` |

## 二、字体

- **正文**：`"Inter", "Noto Sans SC", -apple-system, "PingFang SC", sans-serif` — 字重 300~400（偏细，清爽感）
- **标题**：`"Inter", "Noto Sans SC", sans-serif` — 字重 500~600（半粗，不压人）
- **序号/元数据**：`"Inter", "JetBrains Mono", monospace` — 字重 300

## 三、封面颜色方案

| 元素 | 色值 |
|------|------|
| 基底渐变 | `#FFFFFF → #F5F7F6 → #EEF1EF` (极浅灰绿) |
| 柔光色 | `rgba(122,158,142,0.06)` |
| 环/点强调色 | `#7A9E8E` |
| 标题文字 | `#1A1A1A` |
| 副标题文字 | `#999999` |

## 四、正文排版 CSS（内联样式）

### 基础容器

```css
body { background: #FFFFFF; font-family: "Inter", "Noto Sans SC", -apple-system, "PingFang SC", sans-serif; max-width: 677px; margin: 0 auto; padding: 32px 20px; font-size: 15px; line-height: 1.9; color: #333333; font-weight: 300; }
```

### 标题

```css
h1 { font-size: 22px; font-weight: 500; color: #1A1A1A; margin: 32px 0 8px; letter-spacing: -0.01em; }
h2 { font-size: 17px; font-weight: 600; color: #1A1A1A; margin: 28px 0 6px; border-bottom: 1px solid #EEEEEE; padding-bottom: 8px; }
h3 { font-size: 16px; font-weight: 500; color: #444444; margin: 20px 0 6px; }
```

### 正文

```css
p { margin: 0 0 10px; color: #333333; font-weight: 300; }
strong { color: #1A1A1A; font-weight: 600; }
```

### 引用

```css
blockquote { border-left: 2px solid #7A9E8E; background: #F8F9FA; padding: 10px 16px; margin: 16px 0; color: #666666; border-radius: 0 2px 2px 0; font-size: 14px; font-weight: 300; }
```

### 表格

```css
table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 13px; font-weight: 300; }
th { background: #F8F9FA; color: #333333; padding: 8px 12px; text-align: left; font-weight: 500; border-bottom: 1px solid #EEEEEE; }
td { padding: 8px 12px; border-bottom: 1px solid #F0F0F0; color: #555555; }
tr:nth-child(even) td { background: #FBFCFC; }
```

### 强调与分割

```css
.em-accent { color: #7A9E8E; font-weight: 500; }
hr { border: none; border-top: 1px solid #EEEEEE; margin: 32px 0; }
.footer { margin-top: 32px; padding-top: 16px; border-top: 1px solid #EEEEEE; font-size: 13px; color: #999999; font-weight: 300; }
```

### 配图卡片

```css
.illu-card { position: relative; width: 100%; max-width: 677px; margin: 28px auto; border-radius: 4px; overflow: hidden; box-sizing: border-box; }
```

## 五、下划线/标记风格

正文关键词下划线：`border-bottom: 1.5px solid #7A9E8E; font-weight: 400;`

## 六、配图卡片强调色

| 卡片元素 | 色值 |
|---------|------|
| 强调左边框 | `#7A9E8E` 或 `rgba(122,158,142,0.5)` |
| 序号文字 | `#7A9E8E` |
| 暗底卡片背景 | `#F5F7F6` (非纯暗，是浅灰绿底) |
| 下载按钮悬浮色 | `#7A9E8E` |
