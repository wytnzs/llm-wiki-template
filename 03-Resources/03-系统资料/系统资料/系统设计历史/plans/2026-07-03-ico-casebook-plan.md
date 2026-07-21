---
title: 2026-07-03-ico-casebook-plan
type: system_doc
status: active
tags: ["归档"]
created: 2026-07-03
updated: 2026-07-03
---
# ICO判例集 HTML 实现计划

> **For agentic workers:** 单文件 HTML，直接在桌面生成。

**Goal:** 将《ICO保险理赔十大胜诉判例精解》Markdown 源稿转为手机阅读优化的 HTML，支持 PDF 打印导出。

**Architecture:** 单文件 HTML（内嵌 CSS + 打印样式），375px 宽单栏居中，Editorial Magazine 风格，从 Markdown 手动转写每个案例为 HTML 排版组件。

**Tech Stack:** HTML5 + CSS3（CSS Custom Properties、@page、@media print、CSS grain texture）、Google Fonts（Noto Serif SC、Noto Sans SC、IBM Plex Mono）

## 全局约束

- 画布宽度 375px，居中显示
- 色板：纸色 `#faf7f2` | 墨色 `#1a1a1a` | 朱红 `#8b1a1a` | 辅灰 `#6b6b6b`
- 字体：标题 Noto Serif SC 500 | 正文 Noto Sans SC 400 | 元数据 IBM Plex Mono 500
- 禁止 emoji、禁止卡片背景色块、禁止渐变、禁止圆角装饰
- PDF 打印：`@page { size: A4; margin: 0 }` + `page-break-inside: avoid` 保护案例完整性
- 文件名：`C:\Users\42124\Desktop\ICO胜诉判例精解TOP10.html`

---

### Task 1: 创建 HTML 骨架与 CSS 变量体系

**Files:**
- Create: `C:\Users\42124\Desktop\ICO胜诉判例精解TOP10.html`

**Produces:** 完整 HTML 文件，包含 `<head>` 元数据、Google Fonts 加载、CSS 变量定义、噪点纹理、打印样式。

- [ ] **Step 1: 写入 HTML 骨架 + 全局 CSS**

写入完整的 `<head>` 区：charset、viewport（`width=device-width, initial-scale=1.0`）、Google Fonts 三字体链接、`<title>`。

CSS 变量：
```css
:root {
  --paper: #faf7f2;
  --ink: #1a1a1a;
  --accent: #8b1a1a;
  --grey: #6b6b6b;
  --rule: rgba(0,0,0,0.08);
  --serif: 'Noto Serif SC', 'Songti SC', serif;
  --sans: 'Noto Sans SC', 'PingFang SC', sans-serif;
  --mono: 'IBM Plex Mono', 'Courier New', monospace;
  --width: 375px;
}
```

全局 body：纸色底、墨色字、375px 宽居中、16px 正文基准、1.8 行高。

噪点纹理层：
```css
body::before {
  content: '';
  position: fixed;
  inset: 0;
  opacity: 0.03;
  background-image: url("data:image/svg+xml,...");
  pointer-events: none;
  z-index: 999;
}
```

打印样式：
```css
@media print {
  body { width: 100%; max-width: 100%; padding: 0; }
  @page { size: A4; margin: 12mm; }
  .case { page-break-inside: avoid; }
  .cover { page-break-after: always; }
  body::before { display: none; }
}
```

- [ ] **Step 2: 验证骨架** — 浏览器打开确认纸张纹理可见、375px 居中

---

### Task 2: 封面与目录

**Files:**
- Modify: `C:\Users\42124\Desktop\ICO胜诉判例精解TOP10.html`（在上一步骨架上追加）

- [ ] **Step 1: 写入封面区 HTML + CSS**

```html
<header class="cover">
  <p class="cover__kicker">ICO保险理赔事务所</p>
  <h1 class="cover__title">ICO保险理赔<br>十大胜诉判例精解</h1>
  <p class="cover__subtitle">从2021-2026年胜诉判例库中精选10个代表性案例。<br>每个案例都告诉你：保险公司用什么理由拒赔、我们怎么翻的、法院为什么判我们赢。</p>
  <div class="cover__rule"></div>
  <p class="cover__meta">定价：99元 · PDF电子书 · 2026年7月</p>
</header>
```

CSS：标题 32px serif 500，宽松字距 +0.03em；副标题 14px sans，`color: var(--grey)`；封面底部留白 ≥60px。

- [ ] **Step 2: 写入目录区 HTML + CSS**

双列网格目录（`display: grid; grid-template-columns: auto 1fr`），序号用 mono 字体、朱红色；案名用 sans 字体。

```html
<nav class="toc">
  <h2 class="toc__heading">案例目录</h2>
  <div class="toc__list">
    <span class="toc__num">01</span><span>郭成彪诉太平洋财险 — 四连拒</span>
    <!-- ... 02-10 -->
  </div>
</nav>
```

---

### Task 3: 案例排版组件 + 10个案例

**Files:**
- Modify: `C:\Users\42124\Desktop\ICO胜诉判例精解TOP10.html`

- [ ] **Step 1: 定义案例排版组件 CSS**

```css
.case { padding: 40px 0; border-bottom: 1px solid var(--rule); }
.case__num { font-family: var(--mono); font-size: 72px; color: rgba(0,0,0,0.04); position: absolute; }
.case__title { font-family: var(--serif); font-size: 22px; font-weight: 500; }
.case__meta { font-family: var(--mono); font-size: 12px; color: var(--grey); }
.case__label { font-family: var(--mono); font-size: 11px; color: var(--accent); text-transform: uppercase; letter-spacing: 0.15em; border-left: 2px solid var(--accent); padding-left: 8px; }
.case__body { font-size: 15px; line-height: 1.9; }
.callout { background: rgba(0,0,0,0.02); border-left: 3px solid var(--accent); padding: 16px 20px; margin: 24px 0; }
.callout__heading { font-family: var(--mono); font-size: 12px; color: var(--accent); }
.highlight { font-weight: 700; }
```

- [ ] **Step 2: 写入10个案例 HTML**

每个案例结构：
```html
<section class="case">
  <div class="case__num">01</div>
  <h2 class="case__title">四个拒赔理由，法院全部驳回</h2>
  <p class="case__meta">郭成彪诉中国太平洋财产保险股份有限公司河北分公司 · (2022)冀0922民初406号</p>
  
  <h3 class="case__label">案情简介</h3>
  <p class="case__body">...</p>
  
  <h3 class="case__label">保险公司拒赔理由</h3>
  <p class="case__body">...</p>
  
  <h3 class="case__label">法院判决</h3>
  <p class="case__body">...</p>
  
  <h3 class="case__label">翻盘点</h3>
  <p class="case__body">...</p>
  
  <div class="callout">
    <p class="callout__heading">代理人可以学到</p>
    <p class="case__body">...</p>
  </div>
</section>
```

逐个填写10个案例内容（案号、案情、拒赔理由、判决、翻盘点、代理人启示）。

---

### Task 4: 三个共同规律 + 使用建议 + 版权页

**Files:**
- Modify: `C:\Users\42124\Desktop\ICO胜诉判例精解TOP10.html`

- [ ] **Step 1: 三个共同规律区**

规律标题用 serif 22px，规律内容用 sans 15px。规律二的表格用卡片堆叠代替传统表格（mobile-first）：
```css
.pattern-table { display: flex; flex-direction: column; gap: 12px; }
.pattern-card { padding: 16px; border: 1px solid var(--rule); }
.pattern-card__label { font-family: var(--mono); font-size: 11px; color: var(--accent); }
```

- [ ] **Step 2: 使用建议 + 版权页**

使用建议四个板块（代理人用/群分享用/朋友圈用/客户展示用），每块用小标签区分。

版权页：细线 + 居中文本 + 事务所信息。

---

### Task 5: 整体验证与 PDF 导出

- [ ] **Step 1: 浏览器验证** — 打开 HTML，检查375px宽度、字体加载、纹理效果、10个案例完整性
- [ ] **Step 2: 打印预览** — Ctrl+P 查看 PDF 效果，确认分页不跨案例、字号可读
- [ ] **Step 3: 导出 PDF** — 浏览器"另存为 PDF"，检查文件大小和视觉质量
