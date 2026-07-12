---
title: style-system
type: skill_reference
status: active
tags: []
created: 2026-06-16
updated: 2026-06-16
---
# Style System — 视觉规则体系

从 guizang-social-card-skill 裁剪适配，聚焦小红书 3:4 场景。

---

## Editorial Magazine × E-ink 视觉规则

### 核心身份

**慢、克制、手感。** 每个页面像杂志跨页中的一页——独立但属于同一个卷。

### 必须做

- 衬线展示标题（Noto Serif SC, weight 500），宽松字距 +0.03 ~ +0.04em
- 纸张纹理层（`.grain`）每张卡片必选
- Canvas/WebGL 墨迹层（`.mag-bg`）在封面/金句/大面积留白页必选
- Mono 标签所有元数据（页码、分类、作者行）
- 使用 callout/ledger/pipeline/marginalia 等排版组件，不用卡片背景

### 禁止做

- ❌ 纯色平坦背景（必须 grain + 可选 WebGL）
- ❌ 卡片背景填充（card-fill/card-accent/card-ink）
- ❌ emoji（用排版和装饰线来表达）
- ❌ 900 weight 大标题（轻量 500 是上限）
- ❌ 负字距

### 主题色完整性检查

- 6 种主题任选一，贯穿全组卡片
- midnight-ink 是唯一深色主题，仅用于游戏/夜景/电影感封面
- 所有主题的纸色/墨色/强调色已定义在 CSS 变量中，不自行编造色值

---

## Swiss International 视觉规则

### 核心身份

**快、精确、量化。** 每个页面像仪表盘一屏——信息对等，不加装饰。

### 必须做

- 完全无衬线（Inter + Noto Sans SC）
- 越大越轻：≥200px → weight 200（ExtraLight）
- 严格左对齐，发丝线（1px）分割区块
- 使用 card-fill/card-outlined/card-ink（互斥，选一种贯穿）
- 数据用 KPI Tower / H-Bar Chart / Stacked Ledger 来展示
- Lucide 图标（禁用 emoji）

### 禁止做

- ❌ 任何 serif 字体
- ❌ border-radius / box-shadow / linear-gradient
- ❌ 圆点装饰（dot-mat 透明度 ≤0.08，不能醒目）
- ❌ 混用两种 card 类（全组统一 card-fill 或 card-outlined）
- ❌ 展示标题用 700+ weight

### 画布版式约束

在 1080×1440 画布上已验证的极限：

| Class | 最大行数 | 每行最大中文字数 | 超出后果 |
|-------|---------|----------------|---------|
| `.h-xl` | 2 行 | 8 字 | 3 行会把内容区推出 1440 |
| `.h-hero` | 2 行 | 6 字 | 3 行拥挤 |
| matrix-fill | 8 单元格(2列 4行) | — | hero-stat-bottom 会被推出画布 |
| h-bar-chart | 10 行 | — | 超出需换 S09 KPI Tower |

---

## 两模式共享规则

1. **一套卡片只选一种模式。** 不混合 Editorial 和 Swiss。
2. **一个主题/强调色贯穿全套。** 不内换。
3. **用 class 控制排版。** 不写内联 font-size/font-weight。
4. **最小可读尺寸（移动端模拟 360px 宽）：**
   - 正文 ≥ 28px（Editorial）/ 26px（Swiss）
   - 标签/元数据 ≥ 18px
   - 单元格标题 ≥ 24px
5. **画布 ≥75% 被内容填充。** 不用 flex-grow 把内容挤到中间。
6. **不编造数据。** 百分比、数字必须有来源。
7. **图片必须有 `object-position` 明确的定位。** 不依赖默认 center 50%。
