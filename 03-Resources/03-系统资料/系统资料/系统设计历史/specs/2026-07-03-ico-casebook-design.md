---
title: 2026-07-03-ico-casebook-design
type: system_doc
status: active
tags: ["归档"]
created: 2026-07-03
updated: 2026-07-03
---
# ICO判例集 HTML/PDF 设计规格

## 概述
将《ICO保险理赔十大胜诉判例精解》Markdown 源稿排版为手机阅读优化的 HTML，并导出 PDF。

## 设计系统
- **风格**：Editorial Magazine × E-ink（衬线标题 + 纸张质感）
- **色板**：纸色 `#faf7f2` | 墨色 `#1a1a1a` | 朱红强调 `#8b1a1a` | 灰色辅色 `#6b6b6b`
- **字体**：标题 Noto Serif SC 500 | 正文 Noto Sans SC 400 | 元数据 IBM Plex Mono 500
- **画布**：375px 宽单栏居中，模拟手机屏
- **纹理**：CSS 噪点层 overlay

## 页面结构
1. **封面**：大字标题 + 副标题 + 事务所署名，大面积留白
2. **目录**：紧凑两列列表，序号 mono 字体
3. **案例 × 10**：编号装饰 + 标题区 + 四个信息块（案情/拒赔/判决/翻盘点）+ 代理人启示 callout
4. **三个共同规律**：表格转卡片堆叠
5. **使用建议 + 版权页**

## 排版组件
- 案例编号：大号 mono 淡色水印数字
- 信息块标签：小红条 + mono 标签文字
- 引用/金句：左竖红线 + 衬线斜体
- 案例间分隔：细横线 `border-bottom: 1px solid rgba(0,0,0,0.08)`
- 代理人启示：浅灰底 callout box，左边线强调

## PDF 输出
- 尺寸：移动端优化（~420px 宽等价）
- 页边距：最小化，充分利用屏幕宽度
- 打印 CSS：`@page` + `@media print` 优化分页，避免案例跨页断裂

## 文件输出
- HTML：`C:\Users\42124\Desktop\ICO胜诉判例精解TOP10.html`
- PDF：由 HTML 打印生成
