---
title: layout-recipes
type: skill_reference
status: active
tags: []
created: 2026-06-16
updated: 2026-06-16
---
# Layout Recipes — 布局方案

> 从 guizang-social-card-skill 裁剪，聚焦小红书 3:4（1080×1440）场景
> 每种 recipe 对应一个 `.poster.xhs` 的结构方案

---

## 使用方式

1. 根据卡片类型（封面/结果/概念/流程/对比/金句/CTA）选 recipe
2. 从种子模板（template-editorial-xhs.html 或 template-swiss-xhs.html）开始
3. 替换 `<!-- POSTERS_HERE -->` 中的占位符
4. 每个 `.poster.xhs` 按对应 recipe 的结构填充内容

---

## Editorial Magazine × E-ink Recipes

### M01 · Cover（封面）

```
.h-display  [大标题, ≤2行]
.h-sub      [副标题]
.frame-img  [封面图片]
.lead       [引语]
.issue-strip [页码/元数据]
```

- 必须包含: mag-bg + grain
- 标题用 h-display（124px 500 weight）
- 图片可选 r-16x10 或 r-4x3

### M04 · Pull Quote / 金句页

```
.pullquote  [金句, 衬线斜体 64px 500]
.callout-src [来源行]
```

- 唯一允许 <60% 密度的 recipe
- 必须有 source row / date-stamp / hairline 三选一锚点

### M05 · Before / After 对比

```
.beforeafter
  .ba-block.before [方案A]
  .ba-block        [方案B]
```

- 上下分两行
- before 透明度 0.68

### M07 · Closing Note / CTA 页

```
.h-md / .h-xl  [标题]
.ledger
  .ledger-row × ≥4 [项目列表]
  .ledger-note     [细则]
.callout       [微信号/CTA]
```

- 最少 4 条 ledger 项
- 3 条以下需要换 recipe

### M08 · Field Ledger / 分类列表

```
.h-xl    [标题]
.ledger  [分类列表]
  .ledger-nb    [编号]
  .ledger-title [名称]
  .ledger-note  [说明]
```

- 5 行 ledger 填满 1440px
- 6 行需要压缩标题为 1 行

### M10 · 概念页（col-2 双列）

```
.col-2
  .stack [左列: 概念解释]
  .stack [右列: 补充说明]
```

### M11 · Marginalia Essay（侧栏文章）

```
.marginalia
  [主栏] [正文]
  .mg-col [侧栏注释]
```

- 主栏最多 3 段，每段 3-4 句
- 侧栏 5-7 条 mono 注释

### M14 · Vertical Pipeline（步骤流程）

```
.pipeline-v
  .step × 3-5
    .step-nb    [步骤编号]
    .step-title [步骤名称]
    .step-desc  [步骤说明]
```

- 3-5 步，不可少于 3 步
- 5 步 + 2 行标题 = 填满 1440px

### M15 · 数据网格

```
.grid-3 / .col-3 [三列网格]
  [数据卡片]
```

### M16 · Image-Led Cover（纯图片封面）

```
.frame-img.r-3x4 [全屏图片]
.h-display       [叠放标题]
```

- 图片需通过静区测试（≥30% 低细节区用于放标题）
- 标题用 400-500 weight，纸色 `#f5f1e8`，不用纯白
- 不连续两张 M16

---

## Swiss International Recipes

### S01 · Accent Cover（封面）

```
.chrome-min [卷号/日期]
.t-cat      [分类]
.h-statement [大标题, ≤2行]
.grow
.hr-accent  [强调色分割线]
.lead       [引语]
.t-meta × 2 [作者/日期]
```

### S02 · Statement Cover（纯文字封面）

类似 S01，不包含 chrome-min，标题更大 `.h-hero`

### S03 · 数据网格

```
.grid-3 / .grid-4 [数据网格]
.card-fill        [卡片填充]
```

- 全组用同一种 card 类

### S04 · 对比双栏

```
.row / .grid-2-9
  .card-fill [左栏]
  .card-fill [右栏]
```

### S05 · Pull Quote 金句

```
.card-ink / .card-accent
  .h-xl / .h-statement [金句]
```

- 唯一允许使用 card-ink 或 card-accent 的金句页

### S08 · Image Hero（数据+图片混合）

```
.image-hero
  .hero-img-wrap [图片]
  .hero-overlay-block [标题叠加块]
  .hero-stats
    .stat-block × 3 [三个数据]
```

### S09 · KPI Tower（柱状图）

```
.kpi-tower-row
  .tower-col × 2-4
    .num       [数值]
    .lbl       [标签]
    .bar-tower [柱状条, 用 --h 控制高度]
```

- 1080×1440 画布上 2 列
- 柱子高度通过 `style="--h: 180px"` 控制

### S10 · H-Bar Chart（横向条形图）

```
.h-bar-chart
  .bar-row × 最多 10 条
    .row-lbl   [标签]
    .row-track [轨道]
      .row-fill [填充条, 用 --w 控制宽度]
    .row-val   [数值]
```

- 标签在上，轨道在下（1080 竖版自动堆叠）
- 最多 10 行

### S11 · Stacked Ledger（编号列表）

```
.stacked-ledger
  .ledger-row × 4-8
    .ledger-num [大编号 88px]
    .ledger-lbl [标题 + .sub 细则]
    .ledger-icn [Lucide 图标]
```

- 最少 4 行

### S12 · Matrix + Hero Stat（矩阵+总结）

```
.matrix-fill
  .matrix-cell × 6-8
    .cell-nb    [编号]
    .cell-title [标题]
  .matrix-cell.is-accent [唯一强调色卡]
.hero-stat-bottom
  .num-mega [汇总数字]
  .t-meta   [汇总标签]
```

- 6-8 个单元格（2 列 × 3-4 行）
- 最多 1 个 is-accent 卡

---

## 小红书标准卡片映射速查

| 卡片位置 | 原类型 | Editorial 推荐 | Swiss 推荐 |
|---------|-------|---------------|-----------|
| 第 1 张 | 封面 | M01 / M16 | S01 / S02 |
| 第 2 张 | 结果 | M04 | S08 / S09 |
| 第 3-4 张 | 概念 | M10 / M11 | S12 |
| 第 5-7 张 | 流程 | M14 / M05 | S10 / S09 |
| 第 8 张 | 亮点 | M08 / M15 | S03 / S11 |
| 第 9 张 | 金句 | M04 | S05 |
| 第 10 张 | CTA | M07 | S01 |
