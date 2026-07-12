---
title: theme-deepblue
type: skill_reference
status: active
tags: [公众号, 主题, 深蓝商务]
created: 2026-07-12
updated: 2026-07-12
---

# 公众号排版组件库 —— 深蓝商务

> 理性、专业、可信。适用于案例文、解读文、保险条款、数据分析。
> 深海蓝商务体系：深蓝渐变 + 橙色点缀 + 衬线金句标题。

**公众号平台限制须知**：
- ❌ `<style>`/`<script>`/`class`/`id`、`position:fixed/absolute`、`float`、`@media`、`display:grid`、外部字体/CSS
- ✅ 内联 `style`、`display:flex`（有限）、`linear-gradient`、`border-radius`、`box-shadow`、`<section>/<p>/<span>/<strong>/<img>`
- ⚠️ 装饰空元素必须在内部放 `<span leaf=""><br></span>` 占位，否则微信会剥掉样式

---

## 一、设计变量速查

| 用途 | 色值 |
|------|------|
| 主色/标题 | `#102542` |
| 深色文字 | `#0A1931` |
| 正文色 | `#1A1A1A` |
| 强调色（橙色） | `#F77F00` |
| 引用背景 | `#F7F9FC` |
| 分割线/边框 | `#E5EAF2` |
| 次要文字 | `#86909C` |
| 浅强调色 | `rgba(247,127,0,0.08)` |

字体：正文 `"Noto Sans SC", -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif` / 金句 `"Noto Serif SC", "Songti SC", serif`

---

## 二、组件库

### 组件 1：全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#FFFFFF;font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif;color:#1A1A1A;line-height:1.8;font-size:16px;">

  <!-- 所有组件放在这里 -->

</section>
```

---

### 组件 2：封面卡

**有右侧图片版**：

```html
<section style="margin:0 0 28px;background:linear-gradient(155deg,#0A1931,#102542,#162D5A);border-radius:16px;overflow:hidden;">
  <section style="display:flex;align-items:center;gap:20px;padding:32px 28px;">
    <section style="flex:1;min-width:0;">
      <section style="display:flex;gap:8px;margin-bottom:14px;">
        <span style="padding:4px 14px;border:1px solid rgba(247,127,0,0.4);border-radius:20px;background:rgba(247,127,0,0.10);color:rgba(255,255,255,0.9);font-size:12px;"><span leaf="">{{标签1}}</span></span>
        <span style="padding:4px 14px;border:1px solid rgba(247,127,0,0.4);border-radius:20px;background:rgba(247,127,0,0.10);color:rgba(255,255,255,0.9);font-size:12px;"><span leaf="">{{标签2}}</span></span>
      </section>
      <p style="font-size:24px;font-weight:900;color:#FFFFFF;margin:0 0 10px;line-height:1.2;letter-spacing:-0.02em;">
        <span leaf="">{{主标题}}</span>
      </p>
      <p style="font-size:15px;color:rgba(255,255,255,0.6);margin:0;">
        <span leaf="">{{副标题}}</span>
      </p>
    </section>
    <section style="flex-shrink:0;width:100px;height:100px;border-radius:12px;border:1px solid rgba(247,127,0,0.2);overflow:hidden;">
      <!-- 右侧预留图片位 -->
    </section>
  </section>
  <section style="height:4px;background:linear-gradient(90deg,#F77F00,transparent);"><span leaf=""><br></span></section>
</section>
```

**无图版**（文章无头像时用）：

```html
<section style="margin:0 0 28px;background:linear-gradient(155deg,#0A1931,#102542,#162D5A);border-radius:16px;overflow:hidden;">
  <section style="padding:36px 28px;">
    <p style="font-size:12px;color:rgba(247,127,0,0.7);letter-spacing:2px;margin:0 0 12px;"><span leaf="">{{顶部标签}}</span></p>
    <p style="font-size:26px;font-weight:900;color:#FFFFFF;margin:0 0 10px;line-height:1.15;letter-spacing:-0.02em;">
      <span leaf="">{{主标题行1}}</span>
      <span style="color:#F77F00;"><span leaf="">{{强调词}}</span></span>
    </p>
    <p style="font-size:26px;font-weight:900;color:#FFFFFF;margin:0 0 14px;line-height:1.15;">
      <span leaf="">{{主标题行2}}</span>
    </p>
    <section style="width:40px;height:3px;background:#F77F00;border-radius:2px;margin-bottom:10px;"><span leaf=""><br></span></section>
    <p style="font-size:14px;color:rgba(255,255,255,0.55);margin:0;"><span leaf="">{{副标题}}</span></p>
  </section>
</section>
```

---

### 组件 3：TOC 目录

```html
<section style="margin:0 0 28px;padding:0;">
  <section style="background:#F7F9FC;border-radius:12px;padding:20px 24px;">
    <p style="font-size:13px;color:#86909C;letter-spacing:2px;margin:0 0 14px;"><span leaf="">📖 本篇文章看点</span></p>
    <p style="font-size:15px;color:#102542;margin:0 0 10px;font-weight:600;"><span leaf="">01 {{章节1}}</span></p>
    <p style="font-size:15px;color:#102542;margin:0 0 10px;font-weight:600;"><span leaf="">02 {{章节2}}</span></p>
    <p style="font-size:15px;color:#102542;margin:0;font-weight:600;"><span leaf="">03 {{章节3}}</span></p>
  </section>
</section>
```

---

### 组件 4：章节标题

**常规编号节**：

```html
<section style="margin:32px 0 20px;padding:0;">
  <section style="display:flex;align-items:center;gap:14px;">
    <span style="font-size:28px;font-weight:900;color:#F77F00;line-height:1;flex-shrink:0;font-family:'Noto Serif SC','Songti SC',serif;"><span leaf="">{{01}}</span></span>
    <span style="width:1px;height:32px;background:#E5EAF2;flex-shrink:0;"><span leaf=""><br></span></span>
    <p style="font-size:19px;font-weight:700;color:#102542;margin:0;"><span leaf="">{{标题}}</span></p>
  </section>
</section>
```

**末章结语节**（∞ 编号）：

```html
<section style="margin:32px 0 20px;padding:0;">
  <section style="display:flex;align-items:center;gap:14px;">
    <span style="font-size:28px;font-weight:900;color:#F77F00;line-height:1;flex-shrink:0;"><span leaf="">∞</span></span>
    <span style="width:1px;height:32px;background:#E5EAF2;flex-shrink:0;"><span leaf=""><br></span></span>
    <p style="font-size:19px;font-weight:700;color:#102542;margin:0;"><span leaf="">{{结语标题}}</span></p>
  </section>
</section>
```

---

### 组件 5：正文段落

```html
<p style="margin-bottom:14px;font-size:16px;line-height:1.8;text-align:justify;"><span leaf="">{{正文}}</span></p>
```

---

### 组件 6：行内样式

**6a. 橙色加粗**（核心概念/关键结论）：
```html
<strong style="color:#F77F00;"><span leaf="">文字</span></strong>
```

**6b. 橙色下划线**（正文关键词标记）：
```html
<span style="border-bottom:2px solid #F77F00;font-weight:600;"><span leaf="">文字</span></span>
```

**6c. 深色加粗**（次级强调）：
```html
<strong style="color:#0A1931;"><span leaf="">文字</span></strong>
```

**6d. 橙色背景标签**：
```html
<strong style="color:#F77F00;background:rgba(247,127,0,0.08);padding:2px 6px;border-radius:3px;"><span leaf="">标签</span></strong>
```

**6e. 引用块**：
```html
<blockquote style="border-left:3px solid #F77F00;background:#F7F9FC;padding:12px 16px;margin:16px 0;border-radius:0 4px 4px 0;"><p style="font-size:15px;color:#4A4A4A;margin:0;line-height:1.7;"><span leaf="">{{引用内容}}</span></p></blockquote>
```

**6f. 金句段**（衬线体+大号）：
```html
<p style="font-size:18px;font-weight:700;color:#0A1931;margin:16px 0;line-height:1.6;font-family:'Noto Serif SC','Songti SC',serif;"><span leaf="">{{金句}}</span></p>
```

---

### 组件 7：STEP / CASE 标签

```html
<section style="margin-bottom:20px;">
  <section style="display:flex;align-items:center;gap:8px;margin-bottom:8px;">
    <span style="display:inline-block;background:#102542;color:#fff;font-size:10px;font-weight:700;padding:2px 10px;border-radius:12px;"><span leaf="">STEP 01</span></span>
    <p style="font-size:16px;font-weight:700;color:#102542;margin:0;"><span leaf="">{{步骤标题}}</span></p>
  </section>
  <p style="font-size:15px;color:#1A1A1A;margin:0;line-height:1.8;"><span leaf="">{{内容}}</span></p>
</section>
```

可替换 `STEP` 为 `CASE`、`TOOL`、`SKILL`。

---

### 组件 8：金句/亮点卡片

**完整金句卡**（带边框）：

```html
<section style="background:#FFFFFF;border:1px solid #E5EAF2;border-radius:12px;padding:20px 24px;margin-bottom:24px;">
  <section style="width:32px;height:3px;background:#F77F00;border-radius:2px;margin-bottom:12px;"><span leaf=""><br></span></section>
  <p style="font-size:17px;font-weight:700;color:#0A1931;margin:0;line-height:1.6;font-family:'Noto Serif SC','Songti SC',serif;"><span leaf="">{{金句内容}}</span></p>
  <p style="font-size:13px;color:#86909C;margin:8px 0 0;"><span leaf="">{{出处（可选）}}</span></p>
</section>
```

**简约金句行**（仅底部橙色线）：

```html
<p style="font-size:17px;font-weight:700;color:#0A1931;margin:16px 0;padding-bottom:12px;border-bottom:2px solid #F77F00;font-family:'Noto Serif SC','Songti SC',serif;"><span leaf="">{{金句}}</span></p>
```

---

### 组件 9：提示框

**9a. 信息框**：
```html
<section style="background:rgba(247,127,0,0.05);padding:14px 18px;border-radius:8px;border-left:3px solid #F77F00;margin-bottom:20px;">
  <p style="font-size:14px;color:#1A1A1A;margin:0;line-height:1.7;"><span leaf="">{{信息内容}}</span></p>
</section>
```

**9b. 警告框**：
```html
<section style="background:#FFF8F0;border:1px solid rgba(247,127,0,0.2);border-radius:8px;padding:12px 16px;margin-bottom:20px;">
  <p style="font-size:13px;color:#8B5E00;margin:0;font-weight:600;"><span leaf="">{{警告内容}}</span></p>
</section>
```

---

### 组件 10：代码/命令

**行内代码**：
```html
<span style="background:#F7F9FC;color:#0A1931;padding:2px 8px;border-radius:4px;font-size:14px;font-family:'SF Mono','Menlo',monospace;"><span leaf="">code</span></span>
```

**代码块**：
```html
<pre style="background:#102542;color:#E8F4F8;padding:16px;border-radius:8px;margin:16px 0;overflow-x:auto;font-size:13px;line-height:1.6;"><span leaf="">{{代码内容}}</span></pre>
```

---

### 组件 11：内容标签组（胶囊列表）

```html
<section style="margin-bottom:14px;">
  <p style="margin:0;">
    <span style="display:inline-block;font-size:13px;font-weight:600;color:#102542;background:rgba(16,37,66,0.06);padding:4px 12px;border-radius:999px;"><span leaf="">{{列表项}}</span></span>
  </p>
</section>
```

---

### 组件 12：作者签名区

```html
<section style="margin-top:32px;padding-top:16px;border-top:1px solid #E5EAF2;">
  <p style="font-size:14px;color:#86909C;margin:0 0 4px;"><span leaf="">我是{{作者名}}，{{一句话简介}}</span></p>
  <p style="font-size:13px;color:#86909C;margin:0;"><span leaf="">如果你觉得有收获，欢迎点赞、在看、转发 🎯</span></p>
</section>
```

---

## 三、文章类型 → 组件组合配方

### 配方 A：深度观点文

| 顺序 | 组件 | 说明 |
|------|------|------|
| 1 | 封面（无图版） | 带冲突标签 |
| 2 | TOC 目录 | 前 3 节 |
| 3 | 章节标题 + 正文 | 逐节，每节约 3-5 段 |
| 4 | 金句卡（每节末尾） | 用简约金句行 |
| 5 | 引用/信息框（按需） | 补充说明 |
| 6 | 作者签名区 | 末尾 |

### 配方 B：案例拆解文

| 顺序 | 组件 |
|------|------|
| 1 | 封面（有图版） |
| 2 | 章节标题 + CASE 标签 |
| 3 | 正文段落 + 橙色加粗关键词 |
| 4 | 信息框（补充说明） |
| 5 | 简约金句行收束 |
| 6 | 作者签名区 |

### 配方 C：教程/清单文

| 顺序 | 组件 |
|------|------|
| 1 | 封面（无图版） |
| 2 | TOC 目录 |
| 3 | 章节标题 + STEP 标签 + 正文 |
| 4 | 胶囊列表（关键点） |
| 5 | 金句卡（带边框） |
| 6 | 作者签名区 |

---

## 四、完整文章模板骨架

```
[全局容器]
  [封面卡]
  [TOC 目录] （前3节）
  [章节标题 01]
  [正文段落 × N]
  [信息框 / 金句卡]
  [章节标题 02]
  [正文段落 × N]
  [STEP 标签 + 正文]
  [简约金句行]
  ...
  [末章标题 ∞]
  [正文段落]
  [金句卡（带边框）]
  [作者签名区]
[/全局容器]
```

---

## 五、Markdown → 组件映射规则

| Markdown 元素 | 映射组件 |
|--------------|---------|
| `# 标题` | 组件 2 封面 |
| `## 01 xxx` | 组件 4 章节标题（编号节） |
| `## 结语/写在最后` | 组件 4 章节标题（末章 ∞） |
| `> 引用` | 组件 6e 引用块 |
| `**加粗**` | 组件 6a 橙色加粗（核心）或 6c 深色加粗（次级） |
| `==高亮==` | 组件 6b 橙色下划线 |
| ``` ```代码``` ``` | 组件 10 代码块 |
| 正文段落 | 组件 5 |
| `---` | 分割线（空行即可） |
| 列表 `-` | 组件 11 胶囊列表 |
| 末尾段落 + 作者 | 组件 12 作者签名区 |
