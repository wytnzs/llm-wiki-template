---
title: cover-template
type: skill_reference
status: active
tags: []
created: 2026-06-30
updated: 2026-06-30
---
# 封面 HTML 模板

> 公众号组合封面（左长方形 + 右方形）完整 HTML 代码。
> 每次使用前从下方多套模板中轮换选择，避免同款封面重复出现。
> 被 SKILL.md 的「阶段五·头图」章节引用。使用前先读取该章节的设计规范和变量说明。

---

## 模板选择规则

每次生成封面时，按以下规则选择模板：

1. **模板轮换**：按文章序号循环使用模板 A/B/C/D（第1篇→A，第2篇→B，第3篇→C，第4篇→D，第5篇→A…）
2. **主题配色**：模板骨架固定，颜色从选定主题的「封面颜色方案」取
3. **用户指定**：用户可指定用某套模板（"用B模板"）
4. **无偏好时**：按轮换规则自动选

---

## 模板 A：几何分割（默认）

**风格**：对角线双色分割 + 几何装饰圆。现代、有力，适合观点文/案例文。

```html
（完整 HTML 见下方"完整 HTML"章节）
```

---

## 模板 B：细网格

**风格**：纯色底 + 极细网格纹理 + 单侧强调竖条。克制、精细，适合分析/数据类文章。

**HTML：**

```html
<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>封面</title>
<script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;background:#E4E4E7;gap:20px;font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif}
.btn-download{background:#27272A;color:#FFF;border:none;padding:10px 28px;font-size:14px;border-radius:4px;cursor:pointer}
.btn-download:hover{background:#F97316}
.combo{display:flex}
.left{width:900px;height:383px;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:center;padding:48px 64px;border-right:1px solid #E4E4E7;
background:
  /* 细网格 */
  linear-gradient(rgba(0,0,0,0.02) 1px,transparent 1px),
  linear-gradient(90deg,rgba(0,0,0,0.02) 1px,transparent 1px),
  /* 基底 */
  linear-gradient(135deg,{{基底暗色}} 0%,{{基底中色}} 50%,{{基底亮色}} 100%);
background-size:32px 32px,32px 32px,100% 100%;
}
/* 左侧强调竖条 */
.left::before{content:'';position:absolute;left:0;top:0;bottom:0;width:6px;background:linear-gradient(180deg,{{强调色}} 0%,transparent 100%);opacity:0.6}
.tag-row{display:flex;gap:8px;margin-bottom:20px;position:relative;z-index:2}
.tag{padding:4px 14px;border:1px solid rgba(255,255,255,0.15);border-radius:3px;background:rgba(0,0,0,0.15);color:rgba(255,255,255,0.85);font-size:11px;letter-spacing:1.5px}
.main-title{font-size:54px;font-weight:800;color:#FFF;line-height:1.15;position:relative;z-index:2;letter-spacing:-1.5px;text-shadow:0 2px 8px rgba(0,0,0,0.15)}
.sub-row{margin-top:14px;position:relative;z-index:2}
.subtitle{font-size:18px;color:rgba(255,255,255,0.55);font-weight:400}
.info-line{position:absolute;bottom:36px;left:64px;font-size:11px;color:rgba(255,255,255,0.25);letter-spacing:1px;z-index:2}
.right{width:383px;height:383px;position:relative;overflow:hidden;display:flex;justify-content:center;align-items:center;padding:40px;
background:linear-gradient(135deg,{{基底暗色}} 0%,{{基底中色}} 50%,{{基底亮色}} 100%);
background-size:32px 32px,32px 32px,100% 100%;
}
.right .title{font-size:38px;font-weight:700;color:#FFF;text-align:center;line-height:1.2;position:relative;z-index:2;text-shadow:0 2px 8px rgba(0,0,0,0.15);letter-spacing:-1px}
</style></head><body>
<button class="btn-download" onclick="downloadCover()">⬇ 下载封面 PNG</button>
<div class="combo">
  <div class="left">
    <div class="tag-row"><span class="tag">{{标签1}}</span><span class="tag">{{标签2}}</span></div>
    <div class="main-title">{{主标题}}</div>
    <div class="sub-row"><span class="subtitle">{{副标题}}</span></div>
    <div class="info-line">{{底部信息}}</div>
  </div>
  <div class="right">
    <div class="title">{{右侧标题}}</div>
  </div>
</div>
<script>
function downloadCover(){var el=document.querySelector('.combo');html2canvas(el,{scale:2,backgroundColor:null,useCORS:true,logging:false}).then(function(c){var a=document.createElement('a');a.download='封面.png';a.href=c.toDataURL('image/png');a.click();}).catch(function(e){console.error(e);})}
</script>
</body></html>
```

---

## 模板 C：斜线分割

**风格**：大幅斜角切割，上半纯色下半渐变。有张力，适合冲击型内容。

```html
<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>封面</title>
<script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;background:#E4E4E7;gap:20px;font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif}
.btn-download{background:#27272A;color:#FFF;border:none;padding:10px 28px;font-size:14px;border-radius:4px;cursor:pointer}
.btn-download:hover{background:#F97316}
.combo{display:flex}
.left{width:900px;height:383px;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:center;padding:48px 64px;border-right:1px solid #E4E4E7;
background:linear-gradient(160deg,{{基底暗色}} 0%,{{基底暗色}} 40%,{{基底中色}} 60%,{{基底亮色}} 100%);
}
/* 斜线剪切装饰 */
.left::before{content:'';position:absolute;top:0;right:0;width:200px;height:100%;background:rgba(255,255,255,0.03);transform:skewX(-15deg);transform-origin:top right}
/* 底部强调线 */
.left::after{content:'';position:absolute;bottom:0;left:0;right:0;height:3px;background:linear-gradient(90deg,{{强调色}} 0%,transparent 70%)}
.tag-row{display:flex;gap:8px;margin-bottom:20px;position:relative;z-index:2}
.tag{padding:4px 14px;border:1px solid rgba(255,255,255,0.12);border-radius:20px;color:rgba(255,255,255,0.7);font-size:11px;letter-spacing:1.5px}
.main-title{font-size:56px;font-weight:800;color:#FFF;line-height:1.1;position:relative;z-index:2;letter-spacing:-2px;text-shadow:0 2px 12px rgba(0,0,0,0.2)}
.subtitle{font-size:16px;color:rgba(255,255,255,0.5);margin-top:12px;position:relative;z-index:2;font-weight:400}
.info-line{position:absolute;bottom:28px;left:64px;font-size:11px;color:rgba(255,255,255,0.2);letter-spacing:1px;z-index:2}
.right{width:383px;height:383px;position:relative;overflow:hidden;display:flex;justify-content:center;align-items:center;padding:36px;
background:linear-gradient(160deg,{{基底暗色}} 0%,{{基底中色}} 100%);
}
.right .title{font-size:40px;font-weight:700;color:#FFF;text-align:center;line-height:1.2;position:relative;z-index:2;letter-spacing:-1px}
</style></head><body>
<button class="btn-download" onclick="downloadCover()">⬇ 下载封面 PNG</button>
<div class="combo">
  <div class="left">
    <div class="tag-row"><span class="tag">{{标签1}}</span><span class="tag">{{标签2}}</span></div>
    <div class="main-title">{{主标题}}</div>
    <div class="subtitle">{{副标题}}</div>
    <div class="info-line">{{底部信息}}</div>
  </div>
  <div class="right">
    <div class="title">{{右侧标题}}</div>
  </div>
</div>
<script>
function downloadCover(){var el=document.querySelector('.combo');html2canvas(el,{scale:2,backgroundColor:null,useCORS:true,logging:false}).then(function(c){var a=document.createElement('a');a.download='封面.png';a.href=c.toDataURL('image/png');a.click();}).catch(function(e){console.error(e);})}
</script>
</body></html>
```

---

## 模板 D：大号几何

**风格**：单侧大号几何图形（圆形/方形叠层），纯色底 + 极简几何。适合观点/品牌向内容。

```html
<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>封面</title>
<script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;background:#E4E4E7;gap:20px;font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif}
.btn-download{background:#27272A;color:#FFF;border:none;padding:10px 28px;font-size:14px;border-radius:4px;cursor:pointer}
.btn-download:hover{background:#F97316}
.combo{display:flex}
.left{width:900px;height:383px;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:center;padding:48px 64px;border-right:1px solid #E4E4E7;background:{{基底中色}}}
/* 大号圆形 */
.left::before{content:'';position:absolute;top:-60px;right:-40px;width:320px;height:320px;border-radius:50%;border:1px solid rgba(255,255,255,0.08)}
/* 小圆形 */
.left::after{content:'';position:absolute;bottom:-80px;right:120px;width:200px;height:200px;border-radius:50%;background:rgba(255,255,255,0.03)}
.tag-row{display:flex;gap:8px;margin-bottom:20px;position:relative;z-index:2}
.tag{padding:4px 14px;background:rgba(0,0,0,0.10);border-radius:3px;color:rgba(255,255,255,0.8);font-size:11px;letter-spacing:1.5px}
.main-title{font-size:50px;font-weight:800;color:#FFF;line-height:1.15;position:relative;z-index:2;letter-spacing:-1.5px;text-shadow:0 1px 6px rgba(0,0,0,0.1)}
.subtitle{font-size:16px;color:rgba(255,255,255,0.5);margin-top:12px;position:relative;z-index:2}
.info-line{position:absolute;bottom:32px;left:64px;font-size:11px;color:rgba(255,255,255,0.2);letter-spacing:1px;z-index:2}
.right{width:383px;height:383px;position:relative;overflow:hidden;display:flex;justify-content:center;align-items:center;padding:36px;background:{{基底亮色}}}
.right::before{content:'';position:absolute;bottom:-100px;left:-100px;width:300px;height:300px;border-radius:50%;border:1px solid rgba(255,255,255,0.06)}
.right .title{font-size:36px;font-weight:700;color:#FFF;text-align:center;line-height:1.2;position:relative;z-index:2;text-shadow:0 1px 6px rgba(0,0,0,0.1);letter-spacing:-1px}
</style></head><body>
<button class="btn-download" onclick="downloadCover()">⬇ 下载封面 PNG</button>
<div class="combo">
  <div class="left">
    <div class="tag-row"><span class="tag">{{标签1}}</span><span class="tag">{{标签2}}</span></div>
    <div class="main-title">{{主标题}}</div>
    <div class="subtitle">{{副标题}}</div>
    <div class="info-line">{{底部信息}}</div>
  </div>
  <div class="right">
    <div class="title">{{右侧标题}}</div>
  </div>
</div>
<script>
function downloadCover(){var el=document.querySelector('.combo');html2canvas(el,{scale:2,backgroundColor:null,useCORS:true,logging:false}).then(function(c){var a=document.createElement('a');a.download='封面.png';a.href=c.toDataURL('image/png');a.click();}).catch(function(e){console.error(e);})}
</script>
</body></html>
```

---

## 变量填写说明

| 变量 | 来源 |
|------|------|
| `{{基底暗色/中色/亮色}}` | 查颜色方案表，3 个阶梯色值 |
| `{{强调色}}` | `rgba(247,127,0,0.XX)` 格式，用于装饰线、散点等 |
| `{{标签HTML}}` | 1-3 个 `<span class="tag">...</span>`，标签使用固定 rgba 色值（不从变量派生） |
| `{{主标题}}` | 不超过 15 字，用文章主标题提炼 |
| `{{副标题}}` | 产品名/核心卖点，≤20 字 |
| `{{底部信息行}}` | 平台/技术栈/限制条件 |
| `{{右侧标题}}` | 主标题（可折行），字号 50px |
| `{{文件名安全}}` | 文章标题（去掉特殊字符） |

> 几何装饰元素（环、散点、斜线、角标）使用 **固定 rgba 色值**，不从 `{{强调色}}` 变量派生——避免 `opacity` 属性叠加 rgba 的 alpha 导致元素不可见。左侧面板背景的 3 处柔光椭圆也使用固定 rgba。

---

## 颜色方案

按 `theme-index.md` 选定的主题读取配色。当前已注册主题的封面配色：

| 主题 | 基底渐变 | 柔光色 | 环/点强调色 |
|------|---------|--------|------------|
| **深蓝商务**（默认） | `#0A1931 → #102542 → #162D5A` | `rgba(247,127,0,0.07)` + `rgba(57,73,171,0.10)` | `#F77F00` |
| **暖橙故事** | `#3D1F12 → #522E1A → #6B3A20` | `rgba(196,129,74,0.10)` + `rgba(139,122,106,0.08)` | `#C4814A` |
| **科技暗色**（青色） | `#0D0D0D → #1A1A2E → #16213E` | `rgba(0,212,255,0.10)` + `rgba(22,33,62,0.12)` | `#00D4FF` |
| **科技暗色**（紫色） | `#0D0D0D → #1A0A2E → #2A0A3E` | `rgba(196,66,245,0.10)` + `rgba(42,10,62,0.12)` | `#C442F5` |
| **科技暗色**（橙色） | `#0D0D0D → #2E1A0A → #3E200A` | `rgba(255,107,53,0.10)` + `rgba(62,32,10,0.12)` | `#FF6B35` |
| **石墨灰** | `#FFFFFF → #FAFAFA → #F4F4F5` | `rgba(249,115,22,0.06)` | `#F97316` |
| **赭石红** | `#1A1A2E → #2A1A1A → #3A1A1A` | `rgba(197,48,48,0.08)` | `#C53030` |

> **排版时**：`references/theme-index.md` 索引 → 选主题 → 读对应主题文件的"封面颜色方案"章节取色值。
> **使用前在模板中替换**：基底暗色/中色/亮色、各类柔光 rgba、环/点强调色。几何装饰元素使用固定 rgba 色值，不从强调色变量派生。
