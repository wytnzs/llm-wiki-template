---
title: theme-warm-story
type: skill_reference
status: active
tags: [公众号, 主题, 暖橙故事]
created: 2026-07-12
updated: 2026-07-12
---

# 暖橙故事

> 温暖、亲和、耐读。适用于个人经历、客户故事、成长感悟、复盘类内容。
> 以米白底色 + 茶色/琥珀色系营造阅读感，衬线字体增加人文气息。

---

## 一、设计变量速查

| 用途 | 色值 | CSS 变量名 |
|------|------|-----------|
| 正文背景 | `#FAFAF7` (米白) | `--bg` |
| 正文颜色 | `#3D2E1E` (深茶) | `--text` |
| 标题主色（h1/h2） | `#5C3D2E` (栗棕) | `--heading` |
| 标题深色（h3/strong） | `#3D2E1E` | `--heading-dark` |
| 强调色（装饰/标签/下划线） | `#C4814A` (琥珀) | `--accent` |
| 引用背景 | `#F5F0EB` | `--quote-bg` |
| 引用左边框 | `#C4814A` | `--quote-border` |
| 引用文字 | `#6B5A4A` | `--quote-text` |
| 表格表头背景 | `#5C3D2E` | `--th-bg` |
| 表格表头文字 | `#FFFFFF` | `--th-text` |
| 表格行间隔色 | `#F5F0EB` | `--tr-alt` |
| 表格边框 | `#E5D8CC` | `--table-border` |
| 分割线 | `#E5D8CC` | `--hr` |
| 脚注文字 | `#9B8B7A` | `--muted` |
| 正文下划线 | `#C4814A` (底部 2px) | `--underline` |
| 浅强调色 | `rgba(196,129,74,0.10)` | `--accent-soft` |

## 二、字体

- **正文/标题**：`"Noto Serif SC", "Songti SC", serif` — 衬线体读感更温暖
- **说明文字/标签**：`"Noto Sans SC", -apple-system, "PingFang SC", sans-serif`
- **序号/元数据**：`"IBM Plex Mono", ui-monospace, monospace`

## 三、封面颜色方案

| 元素 | 色值 |
|------|------|
| 基底渐变 | `#3D1F12 → #522E1A → #6B3A20` (奶油橙) |
| 柔光色（暖橙） | `rgba(196,129,74,0.10)` |
| 柔光色（浅茶） | `rgba(139,122,106,0.08)` |
| 环/点强调色 | `#C4814A` |
| 标题文字 | `#FFFFFF` |
| 副标题文字 | `rgba(255,255,255,0.62)` |

## 四、正文排版 CSS（内联样式）

### 基础容器

```css
body { background: #FAFAF7; font-family: "Noto Serif SC", "Songti SC", serif; max-width: 677px; margin: 0 auto; padding: 20px 16px; font-size: 16px; line-height: 1.9; color: #3D2E1E; }
```

### 标题

```css
h1 { font-size: 24px; font-weight: 700; color: #5C3D2E; margin: 24px 0 12px; }
h2 { font-size: 19px; font-weight: 600; color: #5C3D2E; border-left: 4px solid #C4814A; padding-left: 12px; margin: 20px 0 10px; }
h3 { font-size: 17px; font-weight: 600; color: #3D2E1E; margin: 16px 0 8px; }
```

### 正文

```css
p { margin: 0 0 14px; color: #3D2E1E; line-height: 1.9; }
strong { color: #5C3D2E; font-weight: 700; }
```

### 引用

```css
blockquote { border-left: 3px solid #C4814A; background: #F5F0EB; padding: 12px 16px; margin: 16px 0; color: #6B5A4A; border-radius: 0 4px 4px 0; font-size: 15px; line-height: 1.8; }
```

### 表格

```css
table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 15px; font-family: "Noto Sans SC", -apple-system, "PingFang SC", sans-serif; }
th { background: #5C3D2E; color: #FFFFFF; padding: 10px 12px; text-align: left; font-weight: 600; }
td { padding: 10px 12px; border-bottom: 1px solid #E5D8CC; color: #3D2E1E; }
tr:nth-child(even) td { background: #F5F0EB; }
```

### 强调与分割

```css
.em-accent { color: #C4814A; font-weight: 700; font-family: "Noto Sans SC", -apple-system, "PingFang SC", sans-serif; }
hr { border: none; border-top: 1px solid #E5D8CC; margin: 28px 0; }
.footer { margin-top: 32px; padding-top: 16px; border-top: 1px solid #E5D8CC; font-size: 14px; color: #9B8B7A; font-family: "Noto Sans SC", -apple-system, "PingFang SC", sans-serif; }
```

### 配图卡片

```css
.illu-card { position: relative; width: 100%; max-width: 677px; margin: 24px auto; border-radius: 12px; overflow: hidden; box-sizing: border-box; }
```

## 五、下划线/标记风格

正文关键词下划线：`border-bottom: 2px solid #C4814A; font-weight: 600;`

## 六、配图卡片强调色

| 卡片元素 | 色值 |
|---------|------|
| 强调左边框 | `#C4814A` 或 `rgba(196,129,74,0.6)` |
| 序号文字 | `#C4814A` |
| 暗底卡片背景 | `#3D2E1E` |
| 下载按钮悬浮色 | `#C4814A` |
