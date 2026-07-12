---
title: components
type: skill_reference
status: active
tags: []
created: 2026-06-16
updated: 2026-06-16
---
# Components — 共享组件规范

> 适用于两种种子模板的组件规格。每个 recipe 的细节在 layout-recipes.md。

---

## 字体栈

### Editorial Magazine × E-ink

| 变量 | 字体 | 用途 |
|------|------|------|
| `--serif-zh` | Noto Serif SC, Songti SC, STSong | 展示标题 |
| `--serif-en` | Playfair Display | 副标题、斜体引用 |
| `--sans-zh` | Noto Sans SC, PingFang SC | 辅助正文 |
| `--sans-en` | Inter | 拉丁正文 |
| `--mono` | IBM Plex Mono | 标签、页码、元数据 |

### Swiss International

| 变量 | 字体 | 用途 |
|------|------|------|
| `--sans` | Inter, Helvetica Neue, Noto Sans SC | 所有文本 |
| `--sans-zh` | Noto Sans SC, PingFang SC | 中文正文 |
| `--mono` | IBM Plex Mono | 标签、元数据 |

---

## 字号层级

### Editorial（1080×1440 默认）

| 角色 | Class | 字号 | 字重 | 字距 | 字体族 |
|------|-------|------|------|------|--------|
| 展示标题 | `.h-display` | 124px | 500 | +.04em | serif-zh |
| 章节标题 | `.h-xl` | 88px | 500 | +.03em | serif-zh |
| 中标题 | `.h-md` | 56px | 500 | +.02em | serif-zh |
| 副标题 | `.h-sub` | 36px | 400 it | normal | serif-en |
| 引文 | `.pullquote` | 64px | 500 it | normal | serif-zh |
| 导语 | `.lead` | 28px | 400 | normal | serif-zh |
| 正文 | `.body` | 24px | 400 | normal | serif-zh |
| 分类 | `.kicker` | 21px | 500 | +.22em | mono |
| 元数据 | `.meta` / `.label` | 18px | 500 | +.20em | mono |

### Swiss（1080×1440 默认）

| 角色 | Class | 字号 | 字重 | 字体族 |
|------|-------|------|------|--------|
| Hero | `.h-hero` | 168px | 200 | sans |
| Statement | `.h-statement` | 124px | 200 | sans |
| 章节标题 | `.h-xl` | 96px | 300 | sans |
| 中标题 | `.h-md` | 56px | 400 | sans |
| 大数字 | `.num-mega` | 168px | 200 | sans |
| 中数字 | `.num-xl` | 120px | 200 | sans |
| 导语 | `.lead` | 30px | 400 | sans-zh |
| 正文 | `.body` | 26px | 400 | sans-zh |
| 分类 | `.t-cat` | 22px | 600 | sans |
| 元数据 | `.t-meta` | 20px | 500 | mono |

---

## 中文标题长度参考

| 标题形状 | Editorial display | Swiss h-hero |
|---------|-------------------|-------------|
| 1 行 ≤6 字 | 124px（默认） | 168px（默认） |
| 1 行 7-10 字 | 108px | 140px |
| 2 行 每行 ≤8 字 | 96px | 108px |
| 2 行 任一行 9-12 字 | 84px | 96px |
| 3 行（罕见） | 72px | 88px |

---

## 最小可读尺寸（移动端安全）

1080×1440 PNG 在手机上以约 360-420px 逻辑宽度查看。

| 角色 | 最小值 | 说明 |
|------|--------|------|
| 正文 | 28px (Editorial) / 26px (Swiss) | 低于此值不可读 |
| 导语 | 30px | 1.5× 正文基准 |
| 标签/分类 | 20px | 不低于 18px |
| 元数据 | 20px | mono 字体 |
| 网格单元格标题 | 24px | matrix/brief cards |
| 数字标注 | 22px | stat-card 标签 |

---

## Card Fills — Swiss 独有，互斥

四种 card 类，**同一节点上永不混用**：

| Class | 背景 | 文字 | 用途 |
|-------|------|------|------|
| `.card-ink` | ink | paper | 重点单卡，一张卡片最多一张 |
| `.card-accent` | accent | accent-on | 强调色卡，一套卡片最多一张 |
| `.card-fill` | grey-1 | ink | 主力卡片，多卡网格首选 |
| `.card-outlined` | 透明 | ink | 轻量卡片，1px 边框 |

多卡网格必须使用**同一种** card 类。仅允许一张 accent 高亮卡。

Editorial 模板不提供 card 类——Editorial 通过排版/ledger/column 表达层级，不是卡片背景。

---

## 图片容器

| Class | 比例 | 用途 |
|-------|------|------|
| `.r-3x4` | 3:4 | 竖版图片、现场照 |
| `.r-1x1` | 1:1 | 方形头像、产品 |
| `.r-4x3` | 4:3 | 经典杂志排版 |
| `.r-16x9` | 16:9 | 横版风景、信息图 |
| `.r-16x10` | 16:10 | 左文右图默认比例 |
| `.r-21x9` | 21:9 | 超宽横幅 |

每个 `<img>` 需要手写 `object-position`（不依赖默认 center 50%）。

Screenshot 容器用 `.frame-shot`（默认 `object-fit: contain`），普通图片用 `.frame-img`（默认 `object-fit: cover`）。

---

## 截图容器 .frame-shot

| 样式 | Swiss 默认 | Editorial 默认 |
|------|-----------|---------------|
| 圆角 | `corners-sq` (0) | `corners-sm` (6px) |
| 阴影 | `shadow-none` | `shadow-soft` |
| 背景 | `bg-grey-1` | `bg-paper-2` |
| 内边距 | `inset-sub` (20px) | `inset-sub` (24px) |

---

## 图标

- 默认图标库：Lucide（仅 Swiss 模板加载）
- Editorial 少用图标；如需用，用同款 Lucide
- **不用 emoji**
- 图标尺寸：56px（ledger 指示符）/ 32px（行内）/ 24px（chip）
- 颜色：`var(--accent)`（强调）/ `var(--grey-3)`（中性）/ `var(--ink)`（主要）
