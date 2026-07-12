---
title: background-systems
type: skill_reference
status: active
tags: []
created: 2026-06-16
updated: 2026-06-16
---
# Background Systems — Editorial 背景系统

> 适用于 Editorial Magazine × E-ink 模式的纸张纹理+墨迹背景

---

## 三层背景系统

Editorial 卡片的背景由三层构成，从下到上：

```
z-index: 0  │  mag-bg (Canvas WebGL 墨迹)
z-index: 1  │  grain (CSS 纸张颗粒纹理)
z-index: 1  │  paper-wash (渐变淡入)
z-index: 2  │  content (文字内容)
```

### 1. mag-bg — WebGL/Canvas 墨迹

每张 `.poster` 中的 `<canvas class="mag-bg" data-bg="ink-flow"></canvas>` 由模板内置 JS 渲染。

渲染逻辑：
- 读取当前主题的 `--ink-rgb` 和 `--paper-rgb` CSS 变量
- 生成线性渐变作为底色
- 叠加 6-8 条墨迹流线（贝塞尔曲线）
- 透明度由 strength 参数控制（默认 0.32）

在以下页面 **必须使用** mag-bg：
- Cover（封面）
- Pull Quote / 金句页
- 大面积留白的过渡页

在以下页面 **可以省略**：
- 数据密集的表格/矩阵页（此时 grain + paper-wash 已足够）

### 2. grain — 纸张纹理

纯 CSS 实现，无需外部图片：

```css
.grain {
  opacity: .35;
  mix-blend-mode: multiply;
  background-image: radial-gradient(rgba(0,0,0,.045) 1px, transparent 1px);
  background-size: 3px 3px;
}
```

midnight-ink 深色主题翻转模式：
```css
[data-theme="midnight-ink"] .grain {
  opacity: .26;
  mix-blend-mode: screen;
  background-image: radial-gradient(rgba(255,244,214,.10) 1px, transparent 1px);
}
```

### 3. paper-wash — 渐变淡入

底部自然暗角，产生纸张的立体感：

```css
.paper-wash {
  background:
    linear-gradient(180deg, rgba(var(--ink-rgb),.02), rgba(var(--ink-rgb),.05) 60%, rgba(var(--ink-rgb),.08));
}
```

midnight-ink 使用暖金高光：
```css
[data-theme="midnight-ink"] .paper-wash {
  background:
    radial-gradient(80% 50% at 28% 16%, rgba(212,160,74,.12), transparent 64%),
    radial-gradient(70% 60% at 80% 86%, rgba(60,40,20,.20), transparent 72%),
    linear-gradient(180deg, rgba(236,226,207,.02), rgba(0,0,0,.32));
}
```

---

## Swiss 模式的背景

Swiss 不模拟纸张。背景只有三种可能：
1. 纯色 `var(--paper)`（默认）
2. 装饰矩阵（dot-mat / ring-mat / cross-mat，透明度 ≤0.08）
3. 图片区域（`.frame-img` 或 `.frame-shot`）

Swiss 不用渐变背景，不用纹理。
