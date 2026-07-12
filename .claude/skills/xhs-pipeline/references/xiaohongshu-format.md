---
title: xiaohongshu-format
type: skill_reference
status: active
tags: []
created: 2026-06-16
updated: 2026-06-16
---
# 小红书轮播图设计规范

> 版本：v5 — guizang 视觉体系（2026-06-16 升级）
> 源自：guizang-social-card-skill（Editorial Magazine × E-ink / Swiss International）
> 触发词：`转小红书`、`做小红书内容`

---

## 尺寸

- 导出尺寸：**1080 × 1440 px**（小红书 3:4 标准）
- 画布比例：3:4（固定）

> 注意：v5 不再使用 2x 缩放策略。画布直接以 1080×1440 渲染，html2canvas 的 scale 设为 1 即可。

---

## 视觉体系概览

替换原来「炭白奢感」单风格，改为 **双模式选择**。两种模式适用任何内容类型——区别在于视觉姿态，不是内容分类。

| 模式 | 气质 | 字体 | 背景 | 色调 |
|------|------|------|------|------|
| **Editorial Magazine × E-ink** | 杂志深度阅读感 | 衬线宋体展示 + 无衬线正文 | 纸张纹理 + WebGL 墨迹 | 6 种暖纸主题色 |
| **Swiss International** | 工程化精确感 | 无衬线 Inter + Noto Sans SC | 纯色底 + 可选装饰矩阵 | 4 种高饱和强调色 |

---

## Editorial Magazine × E-ink

### 设计原则

- 衬线标题为主，轻量（500 weight），宽松字间距（+0.03 ~ +0.04em）
- 正文也用衬线（Noto Serif SC），斜体包容
- Mono 字体用于标签、页码、分类标识
- 每张卡片必须有纸张纹理（`.grain`），可选 WebGL 墨迹背景（`.mag-bg`）
- 不能用纯色平坦背景
- 不能使用 emoji（用 Lucide 图标替代）

### 6 种主题色

| 主题 | 纸色 | 墨色 | 强调色 | 适用场景 |
|------|------|------|--------|---------|
| `ink-classic` | `#f3f0e8` | `#0a0a0b` | `#111111` | 通用，最百搭 |
| `indigo-porcelain` | `#f2f4f5` | `#0a1f3d` | `#315d93` | 知识/专业内容 |
| `forest-ink` | `#f5f1e8` | `#16251b` | `#2e6b4f` | 自然/成长主题 |
| `kraft-paper` | `#eedfc7` | `#2a1e13` | `#9b5a2e` | 温暖/手作感 |
| `dune` | `#f0e6d2` | `#1f1a14` | `#8f7650` | 大地/沉稳 |
| `midnight-ink` | `#0e0d0c` | `#ece2cf` | `#d4a04a` | **唯一深色主题**，夜间/游戏/封面 |

### 字体层级

| 角色 | Class | 字号 | 字重 | 字距 | 字体 |
|------|-------|------|------|------|------|
| 展示标题 | `.h-display` | 124px | 500 | +.04em | serif-zh |
| 章节标题 | `.h-xl` | 88px | 500 | +.03em | serif-zh |
| 中标题 | `.h-md` | 56px | 500 | +.02em | serif-zh |
| 副标题 | `.h-sub` | 36px | 400 it | normal | serif-en |
| 引文 | `.pullquote` | 64px | 500 it | normal | serif-zh |
| 导语 | `.lead` | 28px | 400 | normal | serif-zh |
| 正文 | `.body` | 24px | 400 | normal | serif-zh |
| 分类标签 | `.kicker` | 21px | 500 | +.22em | mono |
| 元数据 | `.meta` / `.label` | 18px | 500 | +.20em | mono |

### 必备背景层

每张 `.poster` 必须包含：

```html
<canvas class="mag-bg" data-bg="ink-flow"></canvas>
<div class="grain"></div>
```

- `mag-bg`：WebGL/Canvas 墨迹渐变（由模板内置 JS 自动渲染）
- `grain`：纸张纹理（CSS 径向渐变模拟）
- `paper-wash`（可选）：底部淡入渐变

---

## Swiss International

### 设计原则

- 完全无衬线（Inter + Noto Sans SC）
- 越大越轻：≥200px → weight 200（ExtraLight）
- 严格左对齐网格，发丝线分割
- **没有圆角、阴影、渐变**（硬边绝对主义）
- Mono 字体用于所有元数据
- 使用 Lucide 图标，不用 emoji

### 4 种强调色

| 强调色 | 色值 | accent-on | 适用场景 |
|--------|------|-----------|---------|
| `ikb` (International Klein Blue) | `#002FA7` | `#ffffff` | 专业/科技感 |
| `lemon-yellow` | `#FFD500` | `#0a0a0a` | 活力/创意 |
| `lemon-green` | `#C5E803` | `#0a0a0a` | 成长/数据 |
| `safety-orange` | `#FF6B35` | `#ffffff` | 警示/行动号召 |

### 字体层级

| 角色 | Class | 字号 | 字重 | 字体 |
|------|-------|------|------|------|
| Hero 标题 | `.h-hero` | 168px | 200 | sans |
| Statement 标题 | `.h-statement` | 124px | 200 | sans |
| 章节标题 | `.h-xl` | 96px | 300 | sans |
| 中标题 | `.h-md` | 56px | 400 | sans |
| 大数字 | `.num-mega` | 168px | 200 | sans |
| 中数字 | `.num-xl` | 120px | 200 | sans |
| 导语 | `.lead` | 30px | 400 | sans-zh |
| 正文 | `.body` | 26px | 400 | sans-zh |
| 分类 | `.t-cat` | 22px | 600 | sans |
| 元数据 | `.t-meta` | 20px | 500 | mono |

### 装饰矩阵（可选）

```html
<div class="dot-mat"></div>   <!-- 圆点矩阵 -->
<div class="ring-mat"></div>  <!-- 环形矩阵 -->
<div class="cross-mat"></div> <!-- 十字矩阵 -->
```

每张卡片最多一种装饰矩阵，透明度 ≤ 0.08。

---

## 卡片类型映射

小红书标准 8-10 张卡片，映射到两种模式的布局方案：

| 位置 | 原卡片类型 | Editorial Recipe | Swiss Recipe |
|------|-----------|-----------------|-------------|
| 第 1 张 | 封面 | M01 / M16 | S01 / S02 |
| 第 2 张 | 结果页 | M04 (数值锚点) | S08 (底部数据) |
| 第 3-4 张 | 概念解释 | M07 / M10 | S11 / S12 |
| 第 5-7 张 | 流程/实战 | M14 / M05 | S10 / S09 |
| 第 8 张 | 亮点/对比 | M08 / M15 | S03 / S04 |
| 第 9 张 | 金句/方法论 | M04 | S05 |
| 第 10 张 | CTA | M07 (尾页变体) | S01 (CTA 变体) |

具体 recipe 结构和组件引用 `references/layout-recipes.md`。

---

## 页面填充规则（3:4 画布）

- **内容必须覆盖 ≥75% 画布高度**
- 任何超过 15% 的纯空白带必须有"留白理由"
- 禁止用 `<div class="grow"></div>` 把内容夹到中段
- 数据表格/矩阵在 XHS 上自动切换到 2 列
- 使用 `references/portrait-fill.md` 检查每个 3:4 recipe 的最小密度

---

## 种子模板使用规范

**不能从零写 HTML。** 必须从种子模板开始编辑：

| 模式 | 种子模板 |
|------|---------|
| Editorial | `assets/template-editorial-xhs.html` |
| Swiss | `assets/template-swiss-xhs.html` |

### 使用步骤

1. 在 `小红书/{年份}/{月份}/` 下创建项目目录
2. 复制对应种子模板到 `{主题}-小红书版.html`
3. 设置 `<html data-theme="...">` 或 `<html data-accent="...">`
4. 替换 `<!-- POSTERS_HERE -->` 之下的占位内容
5. 每个 `.poster` 用对应 Recipe 的结构填充
6. 每个页面必须包含页码/元数据条
7. CTA 页必须有微信号（从 `local/SKILL.local.md` 读取）

### 禁止操作

- ❌ 不修改种子模板的 CSS 变量和主题定义
- ❌ 不删除 grain/mag-bg（Editorial）或裁剪其默认
- ❌ 不混合 Editorial 和 Swiss 的 class 体系
- ❌ 不在 Swiss 中使用 serif 字体
- ❌ 不在 Editorial 中使用 card-fill / card-accent

---

## 下载工具栏

模板内置的下载工具栏（`.toolbar`）功能与 v4 一致：

| 按钮 | 行为 |
|------|------|
| ⬇ 全部下载 | html2canvas 逐张截图 → JSZip 打包 → 浏览器下载 ZIP |
| 下载当前 | 截图当前可视区域的那张 → 直接下载单张 PNG |

html2canvas 设置：`scale: 1`（因为模板已使用 1080 真实像素），`useCORS: true`（跨域图片支持），`backgroundColor: null`（透明背景由模板 CSS 提供）。

渲染时临时移除 `.poster` 的 `border-radius` 和 `box-shadow`，确保导出图片边缘整洁。

---

## 不可触碰规则

1. 每套卡片只选一种模式（Editorial 或 Swiss）。不混合。
2. 一个主题色贯穿全套卡片。不变换。
3. 不用 emoji。Editorial 用文字装饰，Swiss 用 Lucide 图标。
4. 不编造数据。
5. 不写内联 `font-size` + `font-weight` 在瑞士风 display 标题上——用 class。
6. 文本不能溢出、触碰边缘、或与底部元数据栏碰撞。
7. 3:4 卡片必须吃满画布。
8. CTA 页微信号必须从 `local/SKILL.local.md` 读取。
