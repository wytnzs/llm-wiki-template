---
title: theme-presets
type: skill_reference
status: active
tags: []
created: 2026-06-16
updated: 2026-06-16
---
# Theme Presets — 主题色预设

---

## Editorial Magazine × E-ink（6 种主题）

通过 `<html data-theme="...">` 设置。

| 主题 | 纸色 `--paper` | 深纸 `--paper-2` | 墨色 `--ink` | 柔和 `--muted` | 强调 `--accent` | 适用场景 |
|------|---------------|-----------------|-------------|---------------|----------------|---------|
| `ink-classic` | `#f3f0e8` | `#ebe6da` | `#0a0a0b` | `#68625a` | `#111111` | 通用首选 |
| `indigo-porcelain` | `#f2f4f5` | `#e5ebef` | `#0a1f3d` | `#5f6d78` | `#315d93` | 知识/专业 |
| `forest-ink` | `#f5f1e8` | `#e8dfcf` | `#16251b` | `#5d665d` | `#2e6b4f` | 自然/成长 |
| `kraft-paper` | `#eedfc7` | `#dfc9a8` | `#2a1e13` | `#755f49` | `#9b5a2e` | 温暖/手作 |
| `dune` | `#f0e6d2` | `#ded0b7` | `#1f1a14` | `#6f6557` | `#8f7650` | 大地/沉稳 |
| `midnight-ink` | `#0e0d0c` | `#1a1714` | `#ece2cf` | `#9a8c75` | `#d4a04a` | **深色** 仅用于游戏/夜景 |

### CSS 变量（自动从 data-theme 切换）

```css
--paper     /* 页面主背景 */
--paper-2   /* 卡片/图片占位背景 */
--ink       /* 主要文字色 */
--muted     /* 柔和文字色 */
--line      /* 分割线 */
--accent    /* 强调色 */
--accent-soft /* 强调色柔和版 */
--ink-rgb   /* ink 的 RGB 分量 */
--paper-rgb /* paper 的 RGB 分量 */
```

### 选择建议

| 内容调性 | 推荐主题 |
|---------|---------|
| 严肃/专业/保险/理赔 | `ink-classic` 或 `indigo-porcelain` |
| 教育/成长/育儿 | `forest-ink` |
| 生活/情感/温暖 | `kraft-paper` 或 `dune` |
| 旅游/生活方式 | `dune` 或 `indigo-porcelain` |
| 游戏/电影/夜摄 | `midnight-ink` |

---

## Swiss International（4 种强调色）

通过 `<html data-accent="...">` 设置。

| 强调色 | 色值 | accent-on | 适用场景 |
|--------|------|-----------|---------|
| `ikb` (International Klein Blue) | `#002FA7` | `#ffffff` | 专业/科技/金融 |
| `lemon-yellow` | `#FFD500` | `#0a0a0a` | 活力/创意/教育 |
| `lemon-green` | `#C5E803` | `#0a0a0a` | 增长/数据/健康 |
| `safety-orange` | `#FF6B35` | `#ffffff` | 行动/警示/体育 |

### CSS 变量

```css
--paper      /* #fafaf8 固定 */
--ink        /* #0a0a0a 固定 */
--grey-1     /* 浅灰背景 */
--grey-2     /* 分割线/边框 */
--grey-3     /* 柔和文字 */
--accent     /* 强调色 */
--accent-on  /* 强调色上的文字色 */
```

### 选择建议

| 内容调性 | 推荐强调色 |
|---------|-----------|
| 数据/报告/分析 | `ikb` |
| 创意/设计/灵感 | `lemon-yellow` |
| 增长/健康/环境 | `lemon-green` |
| 行动/推广/提醒 | `safety-orange` |

---

## 重要规则

1. 一套卡片只选一个主题/强调色，不切换
2. 不自行编造色值——只用上面定义的
3. Editorial 和 Swiss 的色值体系不通用（不混用 `--accent` 和 `--grey-1` 等）
