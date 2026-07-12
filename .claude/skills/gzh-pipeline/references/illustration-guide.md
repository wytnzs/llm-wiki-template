---
title: illustration-guide
type: skill_reference
status: active
tags: []
created: 2026-06-20
updated: 2026-06-20
---
# 配图插图指南

> 内嵌于 `_preview.html` 的配图卡片模板库。每种类型附带完整 HTML+CSS 和下载机制。

---

## 两文件分离原则

配图卡片出现在两个文件中，角色不同：

| 文件 | 用途 | 配图卡片 | 下载按钮 |
|------|------|---------|---------|
| `_preview.html` | 预览文章 + 确认配图位置 | ✅ 有 | ❌ 无（保持复制干净） |
| `_配图下载.html` | 集中下载所有配图 PNG | ✅ 有 | ✅ 有 |

### 通用规范（两个文件共用）

- 卡片宽度：`width: 100%; max-width: 677px;`
- 外间距：`margin: 24px auto;`
- 内边距：`padding: 32px 28px;`
- 圆角：`border-radius: 12px;`

### 模板使用说明

以下 5 种卡片类型模板 **默认包含下载按钮**（`<button class="illu-download-btn">`），用于 `_配图下载.html`。

**插入 `_preview.html` 时**：去掉模板中的 `<button class="illu-download-btn" ...>⬇</button>` 那一行，其余 HTML 原样保留。这样预览页复制粘贴到公众号编辑器时干净无杂物。

**变量填充**：模板中使用 `{{变量名}}` 标记，根据文章上下文替换为实际内容。`{{#列表}}...{{/列表}}` 表示循环区域。

### 预览版 CSS（`_preview.html` 的 `<style>` 中）

```css
.illu-card { position: relative; width: 100%; max-width: 677px; margin: 24px auto; border-radius: 12px; overflow: hidden; box-sizing: border-box; }
```

### 下载版依赖（`_配图下载.html` 中）

**`<head>` 中必须包含 html2canvas CDN：**

```html
<script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
```

**下载按钮样式和卡片样式：**

```css
.illu-card { position: relative; width: 100%; max-width: 677px; margin: 24px auto; border-radius: 12px; overflow: hidden; box-sizing: border-box; }
.illu-download-btn { position: absolute; top: 10px; right: 10px; z-index: 10; background: rgba(255,255,255,0.9); border: 1px solid #CBD5E0; border-radius: 6px; padding: 5px 14px; font-size: 13px; cursor: pointer; color: #4A5568; font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif; line-height: 1.4; font-weight: 600; }
.illu-download-btn:hover { background: #FFFFFF; border-color: #315d93; color: #315d93; }
```

**`</body>` 前必须包含下载函数：**

```html
<script>
function downloadCard(elementId, filename) {
  var el = document.getElementById(elementId);
  if (!el) return;
  var btn = el.querySelector('.illu-download-btn');
  if (btn) btn.style.display = 'none';
  html2canvas(el, { scale: 2, backgroundColor: null, useCORS: true, logging: false })
    .then(function(canvas) {
      var link = document.createElement('a');
      link.download = (filename || '配图') + '.png';
      link.href = canvas.toDataURL('image/png');
      link.click();
      if (btn) btn.style.display = '';
    })
    .catch(function(err) { console.error('html2canvas error:', err); if (btn) btn.style.display = ''; });
}
</script>
```

### 主题色彩适配

以下各卡片类型模板的默认色值基于 **深蓝商务** 主题。使用其他主题时，全局替换以下映射：

| 卡片中的默认色 | 深蓝商务 | → 暖橙故事 | → 科技暗色 |
|---------------|---------|-----------|-----------|
| `#0a1f3d`（暗底/主色） | 保持不变 | `#3D2E1E` | `#1A1A2E` |
| `#315d93`（强调色） | 保持不变 | `#C4814A` | `#00D4FF` |
| `#f2f4f5`（浅背景） | 保持不变 | `#F5F0EB` | `rgba(255,255,255,0.06)` |
| `#e5ebef`（分割线/边框） | 保持不变 | `#E5D8CC` | `#2A2A3E` |
| `#5f6d78`（次要文字） | 保持不变 | `#9B8B7A` | `#6A7A8A` |

**生成卡片时的操作**：选定主题后，将以上色值替换为对应主题的值再填入模板。

### 完整下载页面结构

将以上依赖组装为 `_配图下载.html`，标准结构如下：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>配图下载 - {{文章标题}}</title>
<script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { background: #e5ebef; font-family: "Noto Sans SC", -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif; padding: 32px 16px 60px; }
.header { max-width: 677px; margin: 0 auto 28px; text-align: center; }
.header h1 { font-size: 20px; font-weight: 500; font-family:'Noto Serif SC','Songti SC',serif; color: #0a1f3d; margin-bottom: 6px; letter-spacing:.02em; }
.header p { font-size: 14px; color: #5f6d78; }
.illu-card { position: relative; width: 100%; max-width: 677px; margin: 24px auto; border-radius: 12px; overflow: hidden; box-sizing: border-box; }
.illu-download-btn { position: absolute; top: 10px; right: 10px; z-index: 10; background: rgba(255,255,255,0.9); border: 1px solid #CBD5E0; border-radius: 6px; padding: 5px 14px; font-size: 13px; cursor: pointer; color: #4A5568; font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif; line-height: 1.4; font-weight: 600; }
.illu-download-btn:hover { background: #FFFFFF; border-color: #F77F00; color: #F77F00; }
</style>
</head>
<body>

<div class="header">
  <h1>📥 配图下载</h1>
  <p>{{文章标题}} · 共 {{N}} 张 · 点击每张右上角按钮下载 PNG</p>
</div>

<!-- 逐一粘贴所有卡片 HTML（带下载按钮） -->

<script>
function downloadCard(elementId, filename) {
  var el = document.getElementById(elementId);
  if (!el) return;
  var btn = el.querySelector('.illu-download-btn');
  if (btn) btn.style.display = 'none';
  html2canvas(el, { scale: 2, backgroundColor: null, useCORS: true, logging: false })
    .then(function(canvas) {
      var link = document.createElement('a');
      link.download = (filename || '配图') + '.png';
      link.href = canvas.toDataURL('image/png');
      link.click();
      if (btn) btn.style.display = '';
    })
    .catch(function(err) { console.error('html2canvas error:', err); if (btn) btn.style.display = ''; });
}
</script>

</body>
</html>
```

页脚提示（放在最后一个卡片后面）：
```html
<p style="text-align:center; max-width:677px; margin:32px auto 0; font-size:13px; color:#5f6d78;">
  打开预览 HTML 确认位置，在本页下载 PNG → 上传到公众号图片库 → 回到预览页全选复制正文粘贴
</p>
```

---

## 颜色体系

### 主题适配

配图卡片的强调色应与排版阶段选定的主题一致（见 `references/theme-index.md`）。默认使用深蓝商务配色。

生成卡片时，按选定主题替换以下色值：

| 主题 | 主色/暗底 | 浅背景 | 强调色 | 序/标签色 |
|------|----------|-------|-------|----------|
| **深蓝商务**（默认） | `#0a1f3d` | `#f2f4f5` | `#315d93` | `#315d93` |
| **暖橙故事** | `#3D2E1E` | `#F5F0EB` | `#C4814A` | `#C4814A` |
| **科技暗色** | `#1A1A2E` | `rgba(255,255,255,0.06)` | `#00D4FF` | `#00D4FF` |

暗底卡片文字统一用 `#FFFFFF`，次要文字 `rgba(255,255,255,0.7)`。

### 字体

- 卡片标题：衬线 `"Noto Serif SC", "Songti SC", serif`，weight 500
- 正文/标签：无衬线 `"Noto Sans SC", -apple-system, "PingFang SC", sans-serif`
- 序号/元数据：等宽 `"IBM Plex Mono", ui-monospace, monospace`

---

## 卡片类型

### 类型 1：流程图（Flow Diagram）

**适用场景**：展示步骤、流程、工作原理

**核心原则**：步骤和箭头**必须在同一个 flex 容器中交替排列**。不要把步骤放一行、箭头另放一行再靠负 margin 拉上去——两个独立 flex 容器的 item 宽度各自计算，箭头永远对不齐圆心。

**模板：**

```html
<div class="illu-card" id="illu-N" style="padding: 32px 28px; background: #f2f4f5; font-family: 'Noto Sans SC', -apple-system, 'PingFang SC', sans-serif;">
  <button class="illu-download-btn" onclick="downloadCard('illu-N', '{{文件名}}')">⬇</button>
  <h2 style="font-size:20px; font-weight:500; font-family:'Noto Serif SC','Songti SC',serif; color:#0a1f3d; margin:0 0 8px 0; border:none; padding:0; letter-spacing:.02em;">{{卡片标题}}</h2>
  <p style="font-size:13px; color:#5f6d78; margin:0 0 24px 0; font-family:'IBM Plex Mono',monospace; letter-spacing:.10em; text-transform:uppercase;">{{卡片副标题}}</p>
  <div style="display:flex; align-items:flex-start; gap:0;">
    <!-- 步骤 1 -->
    <div style="text-align:center; flex:1; min-width:0;">
      <div style="width:48px; height:48px; background:{{步骤1颜色}}; border-radius:50%; margin:0 auto 8px; display:flex; align-items:center; justify-content:center; font-size:20px; color:#fff; flex-shrink:0; font-family:'IBM Plex Mono',monospace;">{{步骤1图标}}</div>
      <div style="font-size:14px; font-weight:500; color:#0a1f3d; margin-bottom:4px; line-height:1.4; font-family:'Noto Serif SC','Songti SC',serif;">{{步骤1名}}</div>
      <div style="font-size:11px; color:#5f6d78; line-height:1.5;">{{步骤1描述}}</div>
    </div>
    <!-- 箭头 1→2：固定宽度 36px，padding-top 与圆心对齐（48px圆 / 2 ≈ 24px，减去半线高 ≈ 20px） -->
    <div style="display:flex; align-items:center; flex-shrink:0; width:36px; padding-top:20px;">
      <div style="flex:1; height:1.5px; background:#e5ebef; position:relative;"><div style="position:absolute; right:-2px; top:-4px; border:5px solid transparent; border-left:8px solid #315d93;"></div></div>
    </div>
    <!-- 步骤 2 -->
    <div style="text-align:center; flex:1; min-width:0;">
      <div style="width:48px; height:48px; background:{{步骤2颜色}}; border-radius:50%; margin:0 auto 8px; display:flex; align-items:center; justify-content:center; font-size:20px; color:#fff; flex-shrink:0; font-family:'IBM Plex Mono',monospace;">{{步骤2图标}}</div>
      <div style="font-size:14px; font-weight:500; color:#0a1f3d; margin-bottom:4px; line-height:1.4; font-family:'Noto Serif SC','Songti SC',serif;">{{步骤2名}}</div>
      <div style="font-size:11px; color:#5f6d78; line-height:1.5;">{{步骤2描述}}</div>
    </div>
    <!-- 箭头 2→3 -->
    <div style="display:flex; align-items:center; flex-shrink:0; width:36px; padding-top:20px;">
      <div style="flex:1; height:1.5px; background:#e5ebef; position:relative;"><div style="position:absolute; right:-2px; top:-4px; border:5px solid transparent; border-left:8px solid #315d93;"></div></div>
    </div>
    <!-- 步骤 3（按需继续添加步骤+箭头，最后一个步骤后面不加箭头） -->
    <div style="text-align:center; flex:1; min-width:0;">
      <div style="width:48px; height:48px; background:{{步骤3颜色}}; border-radius:50%; margin:0 auto 8px; display:flex; align-items:center; justify-content:center; font-size:20px; color:#fff; flex-shrink:0; font-family:'IBM Plex Mono',monospace;">{{步骤3图标}}</div>
      <div style="font-size:14px; font-weight:500; color:#0a1f3d; margin-bottom:4px; line-height:1.4; font-family:'Noto Serif SC','Songti SC',serif;">{{步骤3名}}</div>
      <div style="font-size:11px; color:#5f6d78; line-height:1.5;">{{步骤3描述}}</div>
    </div>
  </div>
  <p style="text-align:center; margin:16px 0 0 0; font-size:14px; color:#0a1f3d; font-weight:500; font-family:'Noto Serif SC','Songti SC',serif;">{{底部总结}}</p>
</div>
```

**结构要点**：
- **单行交替**：步骤(step)和箭头(arrow)在同一个 `display:flex` 容器中交叉排列：`[step] [arrow] [step] [arrow] [step] ... [step]`。末尾不加箭头
- **步骤**：`flex: 1; min-width: 0;` — 等分剩余空间
- **箭头**：`flex-shrink: 0; width: 36px;` — 固定宽度，不被压缩。`padding-top: 20px` 使箭头线与 48px 圆的中心对齐
- **步骤数**：3-5 个最佳。模板默认 3 步，按需复制步骤块+箭头块扩展

**为什么旧模板（双行分离）会错位**：
旧模板把步骤和箭头放在两个独立 flex 容器中，N 个步骤 vs N-1 个箭头，`flex:1` 分到的宽度不同，再加上 `margin-top:-36px` 和 `padding:0 30px` 两个魔法数字——步骤数或内容一变就崩。单行交替从根本上消除这个问题。

---

### 类型 2：网格卡片（Grid）

**适用场景**：展示并列的能力、功能、要点（2x2 或 3x2）

**模板（2x2）：**

```html
<div class="illu-card" id="illu-N" style="padding: 32px 28px; background: #FFFFFF; border: 1px solid #e5ebef; font-family: 'Noto Sans SC', -apple-system, 'PingFang SC', sans-serif;">
  <button class="illu-download-btn" onclick="downloadCard('illu-N', '{{文件名}}')">⬇</button>
  <h2 style="font-size:20px; font-weight:500; font-family:'Noto Serif SC','Songti SC',serif; color:#0a1f3d; margin:0 0 8px 0; border:none; padding:0; letter-spacing:.02em;">{{卡片标题}}</h2>
  <p style="font-size:13px; color:#5f6d78; margin:0 0 20px 0; font-family:'IBM Plex Mono',monospace; letter-spacing:.10em; text-transform:uppercase;">{{卡片副标题}}</p>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
    {{#网格项}}
    <div style="background:#f2f4f5; border-radius:8px; padding:18px 16px; border-left:4px solid {{#强调色}}#315d93{{/强调色}}{{^强调色}}#0a1f3d{{/强调色}};">
      <div style="font-size:24px; font-weight:500; color:#315d93; margin-bottom:2px; line-height:1.2; font-family:'Noto Serif SC','Songti SC',serif;">{{序号}}</div>
      <div style="font-size:15px; font-weight:500; color:#0a1f3d; margin-bottom:4px; font-family:'Noto Serif SC','Songti SC',serif;">{{标题}}</div>
      <div style="font-size:12px; color:#5f6d78; line-height:1.6;">{{描述}}</div>
    </div>
    {{/网格项}}
  </div>
  <p style="text-align:center; margin:16px 0 0 0; font-size:13px; color:#0a1f3d; font-weight:500; font-family:'Noto Serif SC','Songti SC',serif;">{{底部总结}}</p>
</div>
```

**注意事项**：
- 建议 4 项（2x2），适配 677px 宽度最佳
- 偶数项用交替色（强调色 vs 主色左边框），增强视觉节奏
- 6 项时改为 `grid-template-columns:1fr 1fr 1fr;`（3x2）

---

### 类型 3：暗底对比卡（Dark Comparison）

**适用场景**：A vs B 对比、新旧对比、有无对比

**模板：**

```html
<div class="illu-card" id="illu-N" style="padding: 32px 28px; background: #0a1f3d; color:#FFFFFF; font-family: 'Noto Sans SC', -apple-system, 'PingFang SC', sans-serif;">
  <button class="illu-download-btn" onclick="downloadCard('illu-N', '{{文件名}}')" style="border-color:rgba(255,255,255,0.2); color:rgba(255,255,255,0.7);">⬇</button>
  <h2 style="font-size:20px; font-weight:500; font-family:'Noto Serif SC','Songti SC',serif; color:#FFFFFF; margin:0 0 8px 0; border:none; padding:0; letter-spacing:.02em;">{{卡片标题}}</h2>
  <p style="font-size:13px; color:rgba(255,255,255,0.5); margin:0 0 20px 0; font-family:'IBM Plex Mono',monospace; letter-spacing:.10em; text-transform:uppercase;">{{卡片副标题}}</p>
  <div style="display:flex; gap:16px;">
    <div style="flex:1; background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); border-radius:8px; padding:20px 16px;">
      <div style="font-size:16px; font-weight:500; color:#5f6d78; margin-bottom:14px; font-family:'IBM Plex Mono',monospace; letter-spacing:.08em; text-transform:uppercase;">{{左栏标题}}</div>
      {{#左栏项}}
      <div style="font-size:13px; color:rgba(255,255,255,0.65); margin-bottom:10px; line-height:1.6;">{{内容}}</div>
      {{/左栏项}}
    </div>
    <div style="flex:1; background:rgba(49,93,147,0.12); border:1px solid rgba(49,93,147,0.25); border-radius:8px; padding:20px 16px;">
      <div style="font-size:16px; font-weight:500; color:#d7e1ec; margin-bottom:14px; font-family:'IBM Plex Mono',monospace; letter-spacing:.08em; text-transform:uppercase;">{{右栏标题}}</div>
      {{#右栏项}}
      <div style="font-size:13px; color:rgba(255,255,255,0.9); margin-bottom:10px; line-height:1.6;">{{内容}}</div>
      {{/右栏项}}
    </div>
  </div>
  <p style="text-align:center; margin:16px 0 0 0; font-size:13px; color:#d7e1ec; font-weight:500; font-family:'Noto Serif SC','Songti SC',serif;">{{底部总结}}</p>
</div>
```

**注意事项**：
- 左右栏各 5-6 行为佳，保持高度平衡
- 右栏为重点栏（用橙色高亮），放新产品/优势方
- 底部总结收束观点

---

### 类型 4：柱状图（Bar Chart）

**适用场景**：多维度评分、数据对比、权重展示

**模板：**

```html
<div class="illu-card" id="illu-N" style="padding: 32px 28px; background: #f2f4f5; font-family: 'Noto Sans SC', -apple-system, 'PingFang SC', sans-serif;">
  <button class="illu-download-btn" onclick="downloadCard('illu-N', '{{文件名}}')">⬇</button>
  <h2 style="font-size:20px; font-weight:500; font-family:'Noto Serif SC','Songti SC',serif; color:#0a1f3d; margin:0 0 8px 0; border:none; padding:0; letter-spacing:.02em;">{{卡片标题}}</h2>
  <p style="font-size:13px; color:#5f6d78; margin:0 0 24px 0; font-family:'IBM Plex Mono',monospace; letter-spacing:.10em; text-transform:uppercase;">{{卡片副标题}}</p>
  <div style="display:flex; align-items:flex-end; gap:12px; justify-content:center; height:200px; padding-bottom:8px;">
    {{#柱状数据}}
    <div style="flex:1; max-width:100px; text-align:center;">
      <div style="font-size:22px; font-weight:900; color:{{颜色}}; margin-bottom:4px;">{{数值}}</div>
      <div style="height:{{高度}}px; background:linear-gradient(180deg, {{颜色}} 0%, {{浅色}} 100%); border-radius:6px 6px 0 0; width:100%;"></div>
      <div style="font-size:12px; font-weight:600; color:#0A1931; margin-top:8px;">{{标签}}</div>
      <div style="font-size:11px; color:#86909C;">满分 {{满分}}</div>
    </div>
    {{/柱状数据}}
  </div>
  <p style="text-align:center; margin:16px 0 0 0; font-size:14px; color:#0a1f3d; font-weight:500; font-family:'Noto Serif SC','Songti SC',serif;">{{底部总结}}</p>
</div>
```

**预设颜色方案**（按柱的顺序使用，indigo-porcelain 衍生色）：

| 柱序 | 颜色 | 浅色 |
|------|------|------|
| 1 | `#315d93` | `rgba(49,93,147,0.15)` |
| 2 | `#5f6d78` | `rgba(95,109,120,0.15)` |
| 3 | `#0a1f3d` | `rgba(10,31,61,0.15)` |
| 4 | `#d7e1ec` | `rgba(215,225,236,0.2)` |
| 5 | `#16254a` | `rgba(22,37,74,0.15)` |

**柱高计算公式**：`高度 = (数值 / 满分) * 130`（最大约 130px，留 70px 给标签）

**注意事项**：
- 建议 4-6 根柱，5 根最佳
- 最高柱不超过 140px，保持视觉协调
- 底部总结写"公式"类内容（如 意向度 = 30+25+15+15+15 = 100）

---

### 类型 5：分栏布局（Split Columns）

**适用场景**：两种视角并列、投入 vs 获得、特性 vs 限制

**模板：**

```html
<div class="illu-card" id="illu-N" style="padding: 32px 28px; background: #FFFFFF; border: 1px solid #e5ebef; font-family: 'Noto Sans SC', -apple-system, 'PingFang SC', sans-serif;">
  <button class="illu-download-btn" onclick="downloadCard('illu-N', '{{文件名}}')">⬇</button>
  <h2 style="font-size:20px; font-weight:500; font-family:'Noto Serif SC','Songti SC',serif; color:#0a1f3d; margin:0 0 8px 0; border:none; padding:0; letter-spacing:.02em;">{{卡片标题}}</h2>
  <p style="font-size:13px; color:#5f6d78; margin:0 0 20px 0; font-family:'IBM Plex Mono',monospace; letter-spacing:.10em; text-transform:uppercase;">{{卡片副标题}}</p>
  <div style="display:flex; gap:20px;">
    <div style="flex:1;">
      <div style="font-size:16px; font-weight:500; color:#5f6d78; padding-bottom:8px; border-bottom:2px solid #e5ebef; margin-bottom:12px; font-family:'IBM Plex Mono',monospace; letter-spacing:.08em; text-transform:uppercase;">{{左栏标题}}</div>
      {{#左栏项}}
      <div style="display:flex; align-items:flex-start; gap:8px; margin-bottom:8px;">
        <span style="width:18px; height:18px; border-radius:50%; background:#e5ebef; color:#5f6d78; display:flex; align-items:center; justify-content:center; font-size:10px; flex-shrink:0; margin-top:2px; font-family:'IBM Plex Mono',monospace;">{{序号}}</span>
        <span style="font-size:13px; color:#4A4A4A; line-height:1.6;">{{内容}}</span>
      </div>
      {{/左栏项}}
    </div>
    <div style="flex:1;">
      <div style="font-size:16px; font-weight:500; color:#315d93; padding-bottom:8px; border-bottom:2px solid #315d93; margin-bottom:12px; font-family:'IBM Plex Mono',monospace; letter-spacing:.08em; text-transform:uppercase;">{{右栏标题}}</div>
      {{#右栏项}}
      <div style="display:flex; align-items:flex-start; gap:8px; margin-bottom:8px;">
        <span style="width:18px; height:18px; border-radius:50%; background:rgba(49,93,147,0.12); color:#315d93; display:flex; align-items:center; justify-content:center; font-size:10px; flex-shrink:0; margin-top:2px; font-family:'IBM Plex Mono',monospace;">✓</span>
        <span style="font-size:13px; color:#0a1f3d; line-height:1.6;">{{内容}}</span>
      </div>
      {{/右栏项}}
    </div>
  </div>
  <p style="text-align:center; margin:16px 0 0 0; font-size:12px; color:#5f6d78;">{{底部总结}}</p>
</div>
```

**注意事项**：
- 左栏用灰色系（次要/投入），右栏用橙色系（重点/获得）
- 每栏 3-7 项为佳，保持两栏高度接近
- 右栏为视觉重心，放最重要的信息

---

## 卡片类型选择指引

| 内容特征 | 推荐卡片类型 |
|---------|------------|
| 有步骤/流程/时序 | 类型 1：流程图 |
| 多个并列概念/功能点 | 类型 2：网格卡片 |
| A vs B / 新旧 / 有无对比 | 类型 3：暗底对比卡 |
| 多维评分/权重/数据对比 | 类型 4：柱状图 |
| 两种视角/投入产出/方案对比 | 类型 5：分栏布局 |

---

## 配图数量参考

| 文章长度 | 参考配图数 |
|---------|----------|
| 深度长文（>2500字） | 6-10 张 |
| 中等长度（1500-2500字） | 4-6 张 |
| 短文（<1500字） | 2-3 张 |

数量灵活，核心原则：**每张配图都传递独立信息，不为配而配。**
