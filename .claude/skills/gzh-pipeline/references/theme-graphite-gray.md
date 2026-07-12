---
title: theme-graphite-gray
type: skill_reference
status: active
tags: [公众号, 主题, 石墨灰]
created: 2026-07-12
updated: 2026-07-12
---

# 公众号排版组件库 —— 石墨灰

> 干净、理性、克制。适用于专业观点、设计/科技评论、高端品牌、行业分析。
> 纯白底 + 石墨灰细线 + 超大留白。几乎无色块，以 1px 细线和大间距建立秩序感。

---

## 一、设计变量速查

| 用途 | 色值 |
|------|------|
| 背景色 | `#FFFFFF` |
| 标题色（深炭） | `#27272A` |
| 正文色 | `#52525B`（石墨灰） |
| 细线/边框 | `#E4E4E7` |
| 辅助文字 | `#A1A1AA` |
| 标签底色 | `#F4F4F5` |
| 极浅灰底 | `#FAFAFA` |
| 点睛色（暖橙，全篇≤3处） | `#F97316` |
| 章节间距 | 56px |

字体：`-apple-system, "PingFang SC", "Microsoft YaHei", sans-serif`

---

## 二、组件库

### 组件 1：全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#FFFFFF;font-family:-apple-system,'PingFang SC','Microsoft YaHei',sans-serif;color:#52525B;line-height:1.8;letter-spacing:0.3px;">
  <!-- 所有组件 -->
</section>
```

### 组件 2：封面

```html
<section style="margin:0 0 48px;padding:32px 0;">
  <p style="font-size:11px;color:#A1A1AA;letter-spacing:2px;margin:0 0 16px;"><span leaf="">{{顶部标签}}</span></p>
  <p style="font-size:30px;font-weight:800;color:#27272A;margin:0 0 12px;line-height:1.1;letter-spacing:-1px;">
    <span leaf="">{{主标题}}</span>
    <span style="color:#F97316;"><span leaf="">{{强调词}}</span></span>
  </p>
  <section style="width:48px;height:1px;background:#E4E4E7;margin-bottom:16px;"><span leaf=""><br></span></section>
  <p style="font-size:14px;color:#A1A1AA;margin:0;"><span leaf="">{{副标题}}</span></p>
</section>
```

### 组件 3：章节标题（大号水印编号）

```html
<section style="margin-top:56px;margin-bottom:28px;">
  <p style="font-size:64px;font-weight:900;color:#F4F4F5;margin:0 0 -12px;line-height:1;letter-spacing:-4px;"><span leaf="">{{01}}</span></p>
  <p style="font-size:17px;font-weight:800;color:#27272A;margin:0;"><span leaf="">{{标题}}</span></p>
  <section style="width:24px;height:1px;background:#E4E4E7;margin-top:12px;"><span leaf=""><br></span></section>
</section>
```

### 组件 4：正文段落

```html
<p style="margin-bottom:16px;font-size:15px;line-height:1.8;text-align:justify;"><span leaf="">{{正文}}</span></p>
```

### 组件 5：行内样式

**石墨下划线**（正文关键词默认标记）：
```html
<span style="border-bottom:2px solid #52525B;font-weight:600;"><span leaf="">文字</span></span>
```

**暖橙点缀**（全篇 ≤3 处）：
```html
<span style="color:#F97316;font-weight:700;"><span leaf="">文字</span></span>
```

**引用块**（左竖线 + 极浅灰底）：
```html
<blockquote style="border-left:2px solid #E4E4E7;background:#FAFAFA;padding:12px 16px;margin:20px 0;"><p style="font-size:14px;color:#71717A;margin:0;line-height:1.7;"><span leaf="">{{引用}}</span></p></blockquote>
```

**金句段**（大号字 + 上下细线）：
```html
<p style="font-size:18px;font-weight:700;color:#27272A;margin:24px 0;padding:16px 0;border-top:1px solid #E4E4E7;border-bottom:1px solid #E4E4E7;"><span leaf="">{{金句}}</span></p>
```

### 组件 6：信息框

```html
<section style="background:#FAFAFA;padding:14px 18px;margin-bottom:20px;">
  <p style="font-size:13px;color:#71717A;margin:0;line-height:1.7;"><span leaf="">{{信息}}</span></p>
</section>
```

### 组件 7：作者签名区

```html
<section style="margin-top:48px;padding-top:16px;border-top:1px solid #E4E4E7;text-align:center;">
  <p style="font-size:12px;color:#A1A1AA;margin:0;letter-spacing:1px;"><span leaf="">{{作者名}} · {{简介}}</span></p>
</section>
```

---

## 三、配方 + 骨架

石墨灰适合专业观点/行业分析：

```
水印编号 → 正文段 → 引用块（补充）
    ↓
正文段 → 金句段（上下细线收束）
```

完整骨架：
```
[全局容器]
  [封面（标签+大标题+细线+副标题）]
  [章节标题 01（大号水印64px）]
    [正文×3]
    [引用块]
    [正文×2]
  [章节标题 02]
    [正文×2]
    [金句段（上下细线）]
  [章节标题 03]
    [正文×2]
    [信息框]
  [作者签名区]
[/全局容器]
```
