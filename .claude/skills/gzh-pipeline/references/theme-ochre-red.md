---
title: theme-ochre-red
type: skill_reference
status: active
tags: [公众号, 主题, 赭石红]
created: 2026-07-12
updated: 2026-07-12
---

# 公众号排版组件库 —— 赭石红

> 庄重、有力、可信赖。适用于政策解读、法规分析、行业趋势、重要声明。
> 米白底 + 赭石红强调 + 经典编辑风，红白色系但克制——红色只做点睛。

---

## 一、设计变量速查

| 用途 | 色值 |
|------|------|
| 背景色 | `#FFFFFF` |
| 标题色 | `#1A1A2E`（深靛） |
| 正文色 | `#333333` |
| 强调色（赭石红） | `#C53030` |
| 引用背景 | `#FFF5F5` |
| 浅红强调 | `rgba(197,48,48,0.06)` |
| 分割线/边框 | `#E5E7EB` |
| 次要文字 | `#9CA3AF` |
| 金句背景 | `#FEF2F2` |

字体：正文 `"Noto Serif SC", "Songti SC", serif`（衬线，经典编辑感）/ 标签 `"Noto Sans SC", sans-serif`

---

## 二、组件库

### 组件 1：全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#FFFFFF;font-family:'Noto Serif SC','Songti SC',serif;color:#333333;line-height:1.85;font-size:16px;">
  <!-- 所有组件 -->
</section>
```

### 组件 2：封面

```html
<section style="margin:0 0 28px;background:linear-gradient(155deg,#1A1A2E,#2A1A1A,#3A1A1A);border-radius:16px;overflow:hidden;">
  <section style="padding:36px 28px;">
    <section style="display:flex;gap:8px;margin-bottom:16px;">
      <span style="padding:3px 12px;background:rgba(197,48,48,0.15);border-radius:4px;font-size:11px;color:#C53030;font-weight:600;font-family:'Noto Sans SC',sans-serif;"><span leaf="">{{标签1}}</span></span>
      <span style="padding:3px 12px;background:rgba(255,255,255,0.06);border-radius:4px;font-size:11px;color:rgba(255,255,255,0.6);font-family:'Noto Sans SC',sans-serif;"><span leaf="">{{标签2}}</span></span>
    </section>
    <p style="font-size:24px;font-weight:700;color:#FFFFFF;margin:0 0 10px;line-height:1.2;"><span leaf="">{{主标题}}</span></p>
    <section style="width:36px;height:3px;background:#C53030;margin-bottom:10px;"><span leaf=""><br></span></section>
    <p style="font-size:14px;color:rgba(255,255,255,0.55);margin:0;"><span leaf="">{{副标题}}</span></p>
  </section>
</section>
```

### 组件 3：章节标题

```html
<section style="margin:32px 0 20px;padding-bottom:10px;border-bottom:1px solid #E5E7EB;">
  <section style="display:flex;align-items:center;gap:10px;">
    <span style="display:inline-block;background:#C53030;color:#fff;font-size:12px;font-weight:700;padding:1px 10px;border-radius:3px;font-family:'Noto Sans SC',sans-serif;"><span leaf="">{{01}}</span></span>
    <p style="font-size:18px;font-weight:700;color:#1A1A2E;margin:0;"><span leaf="">{{标题}}</span></p>
  </section>
</section>
```

### 组件 4：正文段落

```html
<p style="margin-bottom:14px;font-size:16px;line-height:1.85;text-align:justify;"><span leaf="">{{正文}}</span></p>
```

### 组件 5：行内样式

**红色加粗**（核心结论）：
```html
<strong style="color:#C53030;"><span leaf="">文字</span></strong>
```

**红色下划线**（关键词）：
```html
<span style="border-bottom:2px solid #C53030;font-weight:600;"><span leaf="">文字</span></span>
```

**引用块**：
```html
<blockquote style="border-left:3px solid #C53030;background:#FFF5F5;padding:12px 16px;margin:16px 0;border-radius:0 4px 4px 0;"><p style="font-size:15px;color:#6B5A5A;margin:0;"><span leaf="">{{引用}}</span></p></blockquote>
```

**金句段**（浅红底 + 左侧红条）：
```html
<p style="font-size:17px;font-weight:700;color:#1A1A2E;margin:20px 0;padding:14px 18px;background:#FEF2F2;border-left:3px solid #C53030;border-radius:0 6px 6px 0;"><span leaf="">{{金句}}</span></p>
```

### 组件 6：信息框

```html
<section style="background:rgba(197,48,48,0.04);border:1px solid rgba(197,48,48,0.12);border-radius:8px;padding:12px 16px;margin-bottom:20px;">
  <p style="font-size:13px;color:#333333;margin:0;"><span leaf="">{{信息}}</span></p>
</section>
```

### 组件 7：作者签名区

```html
<section style="margin-top:32px;padding-top:16px;border-top:1px solid #E5E7EB;">
  <p style="font-size:13px;color:#9CA3AF;margin:0;"><span leaf="">{{作者名}} · {{简介}}</span></p>
</section>
```

---

## 三、配方 + 骨架

赭石红适合政策解读/法规分析：

```
[封面] → [章节+正文×3+红色金句] → [章节+正文+信息框] → [章节+引用+金句] → [作者签名]
```

完整骨架：
```
[全局容器]
  [封面（标签+深靛渐变底+红条）]
  [章节标题 01] [正文×2] [红色加粗关键词] [正文] [金句段（浅红底）]
  [章节标题 02] [正文×2] [引用块] [正文]
  [章节标题 03] [正文] [信息框] [正文×2]
  [作者签名区]
[/全局容器]
```
