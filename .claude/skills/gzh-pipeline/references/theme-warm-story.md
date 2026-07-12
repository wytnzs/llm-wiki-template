---
title: theme-warm-story
type: skill_reference
status: active
tags: [公众号, 主题, 暖橙故事]
created: 2026-07-12
updated: 2026-07-12
---

# 公众号排版组件库 —— 暖橙故事

> 温暖、亲和、耐读。适用于个人经历、客户故事、成长感悟、复盘类内容。
> 米白底色 + 茶色/琥珀色系 + 衬线字体，营造人文阅读感。

---

## 一、设计变量速查

| 用途 | 色值 |
|------|------|
| 背景色 | `#FAFAF7`（米白） |
| 主色/标题 | `#5C3D2E`（栗棕） |
| 正文色 | `#3D2E1E`（深茶） |
| 强调色 | `#C4814A`（琥珀） |
| 引用背景 | `#F5F0EB` |
| 分割线/边框 | `#E5D8CC` |
| 次要文字 | `#9B8B7A` |
| 浅强调色 | `rgba(196,129,74,0.08)` |

字体：正文 `"Noto Serif SC", "Songti SC", serif`（衬线） / 说明 `"Noto Sans SC", sans-serif`

---

## 二、组件库

### 组件 1：全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#FAFAF7;font-family:'Noto Serif SC','Songti SC',serif;color:#3D2E1E;line-height:1.9;font-size:16px;">
  <!-- 所有组件放在这里 -->
</section>
```

---

### 组件 2：封面卡

```html
<section style="margin:0 0 28px;background:linear-gradient(155deg,#3D1F12,#522E1A,#6B3A20);border-radius:16px;overflow:hidden;">
  <section style="padding:36px 28px;">
    <p style="font-size:12px;color:rgba(196,129,74,0.7);letter-spacing:2px;margin:0 0 12px;"><span leaf="">{{顶部标签}}</span></p>
    <p style="font-size:24px;font-weight:700;color:#FFFFFF;margin:0 0 10px;line-height:1.2;">
      <span leaf="">{{主标题行1}}</span>
      <span style="color:#C4814A;"><span leaf="">{{强调词}}</span></span>
    </p>
    <p style="font-size:16px;color:rgba(255,255,255,0.6);margin:0;"><span leaf="">{{副标题}}</span></p>
  </section>
  <section style="height:3px;background:linear-gradient(90deg,#C4814A,transparent);"><span leaf=""><br></span></section>
</section>
```

---

### 组件 3：TOC 目录

```html
<section style="margin:0 0 28px;background:#F5F0EB;border-radius:12px;padding:20px 24px;">
  <p style="font-size:13px;color:#9B8B7A;letter-spacing:2px;margin:0 0 14px;"><span leaf="">📖 本篇文章看点</span></p>
  <p style="font-size:15px;color:#5C3D2E;margin:0 0 10px;font-weight:600;"><span leaf="">01 {{章节1}}</span></p>
  <p style="font-size:15px;color:#5C3D2E;margin:0 0 10px;font-weight:600;"><span leaf="">02 {{章节2}}</span></p>
  <p style="font-size:15px;color:#5C3D2E;margin:0;font-weight:600;"><span leaf="">03 {{章节3}}</span></p>
</section>
```

---

### 组件 4：章节标题

```html
<section style="margin:32px 0 20px;">
  <section style="display:flex;align-items:center;gap:14px;">
    <span style="font-size:26px;font-weight:700;color:#C4814A;line-height:1;flex-shrink:0;"><span leaf="">{{01}}</span></span>
    <span style="width:1px;height:28px;background:#E5D8CC;flex-shrink:0;"><span leaf=""><br></span></span>
    <p style="font-size:18px;font-weight:600;color:#5C3D2E;margin:0;"><span leaf="">{{标题}}</span></p>
  </section>
</section>
```

---

### 组件 5：正文段落

```html
<p style="margin-bottom:16px;font-size:16px;line-height:1.9;text-align:justify;"><span leaf="">{{正文}}</span></p>
```

---

### 组件 6：行内样式

**6a. 琥珀加粗**（核心概念）：
```html
<strong style="color:#C4814A;"><span leaf="">文字</span></strong>
```

**6b. 琥珀下划线**（关键词标记）：
```html
<span style="border-bottom:2px solid #C4814A;font-weight:600;"><span leaf="">文字</span></span>
```

**6c. 引用块**：
```html
<blockquote style="border-left:3px solid #C4814A;background:#F5F0EB;padding:12px 16px;margin:16px 0;border-radius:0 4px 4px 0;"><p style="font-size:15px;color:#6B5A4A;margin:0;line-height:1.8;"><span leaf="">{{引用}}</span></p></blockquote>
```

**6d. 金句段**（大号衬线）：
```html
<p style="font-size:18px;font-weight:600;color:#5C3D2E;margin:16px 0;line-height:1.7;font-family:'Noto Serif SC','Songti SC',serif;"><span leaf="">{{金句}}</span></p>
```

---

### 组件 7：标签

```html
<section style="margin-bottom:20px;">
  <section style="display:flex;align-items:center;gap:8px;margin-bottom:8px;">
    <span style="display:inline-block;background:#5C3D2E;color:#FAFAF7;font-size:10px;font-weight:700;padding:2px 10px;border-radius:12px;"><span leaf="">STEP 01</span></span>
    <p style="font-size:16px;font-weight:600;color:#5C3D2E;margin:0;"><span leaf="">{{标题}}</span></p>
  </section>
  <p style="font-size:15px;color:#3D2E1E;margin:0;line-height:1.9;"><span leaf="">{{内容}}</span></p>
</section>
```

---

### 组件 8：金句卡

```html
<section style="background:#FFFFFF;border:1px solid #E5D8CC;border-radius:12px;padding:20px 24px;margin-bottom:24px;">
  <section style="width:32px;height:3px;background:#C4814A;border-radius:2px;margin-bottom:12px;"><span leaf=""><br></span></section>
  <p style="font-size:17px;font-weight:600;color:#3D2E1E;margin:0;line-height:1.6;font-family:'Noto Serif SC','Songti SC',serif;"><span leaf="">{{金句}}</span></p>
  <p style="font-size:13px;color:#9B8B7A;margin:8px 0 0;"><span leaf="">{{出处}}</span></p>
</section>
```

---

### 组件 9：作者签名区

```html
<section style="margin-top:32px;padding-top:16px;border-top:1px solid #E5D8CC;">
  <p style="font-size:14px;color:#9B8B7A;margin:0;"><span leaf="">{{作者名}} · {{简介}}</span></p>
</section>
```

---

## 三、文章类型配方

暖橙故事主要适用于故事文/个人经历，推荐配方：

```
[封面] → [TOC] → [章节标题+正文×4] → [金句卡] → [作者签名]
```

全文用琥珀下划线标记关键词，金句段收束每节。

## 四、完整骨架

```
[全局容器]
  [封面]
  [章节标题 01] [正文] [金句卡]
  [章节标题 02] [正文] [STEP标签+正文]
  ...
  [末章标签 ∞] [正文] [金句卡]
  [作者签名区]
[/全局容器]
```
