---
title: theme-minimal-fresh
type: skill_reference
status: active
tags: [公众号, 主题, 极简清爽]
created: 2026-07-12
updated: 2026-07-12
---

# 公众号排版组件库 —— 极简清爽

> 干净、透气、现代。适用于方法论、工具文、教程、清单型内容。
> 大留白 + 细线条 + 鼠尾草绿点缀。不堆色，不重底，让内容本身成为视觉重心。

---

## 一、设计变量速查

| 用途 | 色值 |
|------|------|
| 背景色 | `#FFFFFF` |
| 正文色 | `#333333` |
| 标题色 | `#1A1A1A` |
| 强调色（鼠尾草绿） | `#7A9E8E` |
| 引用背景 | `#F8F9FA` |
| 分割线/边框 | `#EEEEEE` |
| 次要文字 | `#999999` |
| 浅强调色 | `rgba(122,158,142,0.06)` |

字体：正文 `"Inter", "Noto Sans SC", -apple-system, sans-serif` / 字重 300~400（偏细）

---

## 二、组件库

### 组件 1：全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#FFFFFF;font-family:'Inter','Noto Sans SC','PingFang SC',sans-serif;color:#333333;line-height:1.8;font-size:15px;font-weight:300;">
  <!-- 所有组件 -->
</section>
```

### 组件 2：封面

```html
<section style="margin:0 0 28px;padding:32px 0;">
  <p style="font-size:11px;color:#999999;letter-spacing:3px;margin:0 0 14px;text-transform:uppercase;"><span leaf="">{{顶部标签}}</span></p>
  <p style="font-size:28px;font-weight:400;color:#1A1A1A;margin:0 0 8px;line-height:1.2;letter-spacing:-0.02em;">
    <span leaf="">{{主标题行1}}</span>
    <span style="font-weight:500;color:#7A9E8E;"><span leaf="">{{强调词}}</span></span>
  </p>
  <section style="width:32px;height:2px;background:#7A9E8E;margin-bottom:12px;"><span leaf=""><br></span></section>
  <p style="font-size:14px;color:#999999;margin:0;font-weight:300;"><span leaf="">{{副标题}}</span></p>
</section>
```

### 组件 3：TOC 目录

```html
<section style="margin:0 0 28px;background:#F8F9FA;padding:20px 24px;">
  <p style="font-size:12px;color:#999999;letter-spacing:2px;margin:0 0 12px;"><span leaf="">看点</span></p>
  <p style="font-size:15px;color:#1A1A1A;margin:0 0 8px;font-weight:400;"><span leaf="">01 {{章节1}}</span></p>
  <p style="font-size:15px;color:#1A1A1A;margin:0 0 8px;font-weight:400;"><span leaf="">02 {{章节2}}</span></p>
  <p style="font-size:15px;color:#1A1A1A;margin:0;font-weight:400;"><span leaf="">03 {{章节3}}</span></p>
</section>
```

### 组件 4：章节标题

```html
<section style="margin:32px 0 16px;padding-bottom:8px;border-bottom:1px solid #EEEEEE;">
  <p style="font-size:13px;color:#7A9E8E;letter-spacing:2px;margin:0 0 4px;font-weight:400;"><span leaf="">{{01}}</span></p>
  <p style="font-size:17px;font-weight:500;color:#1A1A1A;margin:0;"><span leaf="">{{标题}}</span></p>
</section>
```

### 组件 5：正文段落

```html
<p style="margin-bottom:14px;font-size:15px;line-height:1.9;font-weight:300;"><span leaf="">{{正文}}</span></p>
```

### 组件 6：行内样式

**细体加粗**（仅在极简清爽中，加粗用 500 字重）：
```html
<strong style="color:#1A1A1A;font-weight:500;"><span leaf="">文字</span></strong>
```

**绿色字**（强调）：
```html
<span style="color:#7A9E8E;font-weight:400;"><span leaf="">文字</span></span>
```

**绿色下划线**：
```html
<span style="border-bottom:1.5px solid #7A9E8E;"><span leaf="">文字</span></span>
```

**引用块**：
```html
<blockquote style="border-left:2px solid #7A9E8E;background:#F8F9FA;padding:10px 16px;margin:16px 0;border-radius:0 2px 2px 0;"><p style="font-size:14px;color:#666666;margin:0;line-height:1.8;font-weight:300;"><span leaf="">{{引用}}</span></p></blockquote>
```

**金句段**：
```html
<p style="font-size:18px;font-weight:400;color:#1A1A1A;margin:20px 0;line-height:1.7;"><span leaf="">{{金句}}</span></p>
```

### 组件 7：标签

```html
<section style="margin-bottom:20px;">
  <p style="font-size:12px;color:#7A9E8E;letter-spacing:2px;margin:0 0 6px;font-weight:400;"><span leaf="">// STEP 01</span></p>
  <p style="font-size:15px;color:#333333;margin:0;line-height:1.9;font-weight:300;"><span leaf="">{{内容}}</span></p>
</section>
```

### 组件 8：金句卡

简约版——纯文字 + 顶部细线：

```html
<section style="padding:20px 0;margin-bottom:20px;">
  <section style="width:24px;height:1px;background:#7A9E8E;margin-bottom:14px;"><span leaf=""><br></span></section>
  <p style="font-size:16px;font-weight:400;color:#1A1A1A;margin:0;line-height:1.7;"><span leaf="">{{金句}}</span></p>
</section>
```

### 组件 9：表格

```html
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:13px;">
  <tr><th style="background:#F8F9FA;padding:8px 12px;text-align:left;font-weight:500;color:#333333;border-bottom:1px solid #EEEEEE;">{{表头1}}</th><th style="background:#F8F9FA;padding:8px 12px;text-align:left;font-weight:500;color:#333333;border-bottom:1px solid #EEEEEE;">{{表头2}}</th></tr>
  <tr><td style="padding:8px 12px;border-bottom:1px solid #F0F0F0;color:#555555;">{{数据}}</td><td style="padding:8px 12px;border-bottom:1px solid #F0F0F0;color:#555555;">{{数据}}</td></tr>
</table>
```

### 组件 10：作者签名区

```html
<section style="margin-top:32px;padding-top:12px;border-top:1px solid #EEEEEE;">
  <p style="font-size:13px;color:#999999;margin:0;font-weight:300;"><span leaf="">{{作者名}} · {{简介}}</span></p>
</section>
```

---

## 三、配方 + 骨架

极简清爽适合教程/清单/方法论，推荐配方：

```
[封面] → [TOC] → [章节标题+正文×3] → [金句卡] → [作者签名]
```

完整骨架：

```
[全局容器]
  [封面（无图版，顶标签+大标题+细线分隔）]
  [TOC 目录]
  [章节标题 01] [正文×3] [引用块]
  [章节标题 02] [正文×2] [标签+正文] [金句卡]
  [章节标题 03] [正文×2] [表格] [金句段]
  [作者签名区]
[/全局容器]
```
