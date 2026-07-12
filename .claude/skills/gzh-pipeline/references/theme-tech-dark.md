---
title: theme-tech-dark
type: skill_reference
status: active
tags: [公众号, 主题, 科技暗色]
created: 2026-07-12
updated: 2026-07-12
---

# 公众号排版组件库 —— 科技暗色

> 现代、冲击、利落。适用于观点文、工具文、方法论、评测。
> 暗色背景 + 亮色强调，默认青色，可选紫/橙变体。

---

## 一、设计变量速查

| 用途 | 青色（默认） | 紫色变体 | 橙色变体 |
|------|------------|---------|---------|
| 背景色 | `#0D0D0D` | 同左 | 同左 |
| 正文色 | `#E0E0E0` | 同左 | 同左 |
| 标题色 | `#FFFFFF` | 同左 | 同左 |
| 强调色 | `#00D4FF` | `#C442F5` | `#FF6B35` |
| 引用背景 | `#1A1A2E` | 同左 | 同左 |
| 边框 | `#2A2A3E` | 同左 | 同左 |
| 次要文字 | `#6A7A8A` | 同左 | 同左 |

字体：`"Noto Sans SC", -apple-system, sans-serif` / 数字/标签 `"Space Mono", monospace`

---

## 二、组件库

### 组件 1：全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#0D0D0D;font-family:'Noto Sans SC','PingFang SC',sans-serif;color:#E0E0E0;line-height:1.8;font-size:16px;">
  <!-- 所有组件 -->
</section>
```

### 组件 2：封面

```html
<section style="margin:0 0 28px;background:linear-gradient(155deg,#0D0D0D,#1A1A2E,#16213E);border-radius:16px;overflow:hidden;border:1px solid #2A2A3E;">
  <section style="padding:36px 28px;">
    <p style="font-size:12px;color:rgba(0,212,255,0.6);letter-spacing:2px;margin:0 0 12px;"><span leaf="">{{顶部标签}}</span></p>
    <p style="font-size:24px;font-weight:800;color:#FFFFFF;margin:0 0 10px;line-height:1.15;letter-spacing:-0.02em;">
      <span leaf="">{{主标题}}</span>
      <span style="color:#00D4FF;"><span leaf="">{{强调词}}</span></span>
    </p>
    <section style="width:40px;height:2px;background:#00D4FF;margin-bottom:10px;"><span leaf=""><br></span></section>
    <p style="font-size:14px;color:rgba(255,255,255,0.5);margin:0;"><span leaf="">{{副标题}}</span></p>
  </section>
</section>
```

### 组件 3：章节标题

```html
<section style="margin:32px 0 20px;">
  <section style="display:flex;align-items:center;gap:12px;">
    <span style="font-size:24px;font-weight:700;color:#00D4FF;line-height:1;flex-shrink:0;font-family:'Space Mono',monospace;"><span leaf="">{{01}}</span></span>
    <p style="font-size:17px;font-weight:700;color:#FFFFFF;margin:0;"><span leaf="">{{标题}}</span></p>
  </section>
</section>
```

### 组件 4：正文 + 行内样式

```html
<p style="margin-bottom:14px;font-size:15px;line-height:1.9;"><span leaf="">{{正文}}</span></p>
```

**强调色加粗**：
```html
<strong style="color:#0D0D0D;background:#00D4FF;padding:0 4px;"><span leaf="">文字</span></strong>
```

**强调色下划线**：
```html
<span style="border-bottom:2px solid #00D4FF;font-weight:600;"><span leaf="">文字</span></span>
```

**引用块**：
```html
<blockquote style="border-left:3px solid #00D4FF;background:#1A1A2E;padding:12px 16px;margin:16px 0;border-radius:0 4px 4px 0;"><p style="font-size:14px;color:#A0B0C0;margin:0;"><span leaf="">{{引用}}</span></p></blockquote>
```

**金句段**：
```html
<p style="font-size:17px;font-weight:700;color:#FFFFFF;margin:16px 0;line-height:1.6;"><span leaf="">{{金句}}</span></p>
```

### 组件 5：金句卡

```html
<section style="background:#1A1A2E;border:1px solid #2A2A3E;border-radius:12px;padding:20px 24px;margin-bottom:24px;">
  <section style="width:32px;height:2px;background:#00D4FF;margin-bottom:12px;"><span leaf=""><br></span></section>
  <p style="font-size:16px;font-weight:600;color:#FFFFFF;margin:0;line-height:1.6;"><span leaf="">{{金句}}</span></p>
</section>
```

### 组件 6：提示框

```html
<section style="background:rgba(0,212,255,0.06);border:1px solid #2A2A3E;border-radius:8px;padding:12px 16px;margin-bottom:20px;">
  <p style="font-size:13px;color:#A0B0C0;margin:0;"><span leaf="">{{提示}}</span></p>
</section>
```

### 组件 7：作者签名区

```html
<section style="margin-top:32px;padding-top:16px;border-top:1px solid #2A2A3E;">
  <p style="font-size:13px;color:#6A7A8A;margin:0;"><span leaf="">{{作者名}} · {{简介}}</span></p>
</section>
```

---

## 三、配方 + 骨架

科技暗色适合观点文/工具文，推荐配方：

```
[封面] → [章节标题01+正文+金句卡] → [章节标题02+正文+提示框] → [金句卡] → [作者签名区]
```

完整骨架：

```
[全局容器]
  [封面]
  [章节标题 01] [正文×3] [金句卡]
  [章节标题 02] [正文×2] [提示框] [正文]
  [章节标题 03] [正文×2] [金句强调段]
  [作者签名区]
[/全局容器]
```
