---
title: portrait-fill
type: skill_reference
status: active
tags: []
created: 2026-06-16
updated: 2026-06-16
---
# Portrait Fill — 3:4 画布填充规则

> 适用于小红书 1080×1440 卡片

---

## 核心规则

**内容必须覆盖 ≥75% 画布高度。** 任何超过 15% 画布高度的纯空白带必须有"留白理由"。

### ✅ 允许的留白理由

- Hero 图片自带呼吸感（图片本身有大量空白/天空/背景）
- 单句宣言式 hero statement（一句大标题站住整张卡片）
- 段落顶/底 leading & trailing whitespace（前后总和 ≤15%）

### ❌ 不允许的留白

- 用 `<div style="flex: 1"></div>` 上下夹击把内容塞到中段
- 一张卡片只有 3 行短文字 + 大量空白
- 内容不足预期 recipe 的最小密度

---

## Recipe 密度指引

### Editorial

| Recipe | 最小内容密度 | 备注 |
|--------|------------|------|
| M01 Cover | 封面 | 标题 + 图片 + 引语 |
| M04 Pull Quote | 60%（最低锚点） | 必须有 source row / date-stamp / hairline 之一 |
| M07 Closing Note | ≥4 ledger items + sub-lines + closing block | 3 条短 ledger 是失败模式 |
| M14 Pipeline | 3-5 steps | 少于 3 步则换 recipe |

### Swiss

| Recipe | 最小内容密度 | 备注 |
|--------|------------|------|
| S01/S02 Cover | 标题 + metadata | 封面可宽松 |
| S08 Image Hero | 图片 + overlay + 底部 3 个 stat | stat 不能少于 2 个 |
| S12 Matrix + Stat | ≥6 个 cell + 底部总结数值 | 4 个 cell 太瘦 |

---

## 检查方法

截图后肉眼检查或运行校验脚本：

```bash
# 用 Playwright 验证
node validate-social-deck.mjs <output-dir>
```

R1 检查溢出，R5 检查四横带密度。
