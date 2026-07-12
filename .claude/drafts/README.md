---
title: README
type: draft_doc
status: active
tags: []
created: 2026-07-06
updated: 2026-07-09
---
# 内容交接层（Content Brief + Style Brief）

> 生产管线之间的标准化内容交接机制。

## 文件说明

| 文件 | 用途 | 谁生成 | 谁消费 |
|------|------|--------|--------|
| content-brief.json | 内容简报——讲什么、凭什么讲、用哪些判例/卡片 | 选题管线 / 用户 / 生产 skill | 所有生产 skill（gzh/xhs/video） |
| style-brief.json | 风格简报——谁在讲、怎么讲、长什么样、用什么图 | style-brief-pipeline / 用户 | gzh/xhs/video/image 生产 skill |

## 工作流

`
topic-selection / 认知引擎
        → content-brief.json
        → style-brief.json
        → 平台 skill（gzh/xhs/video/image）
                    ↕
             用户确认 / 修改
`

## 原则

- **content-brief 解决**：讲什么、凭什么讲、用哪些知识资产
- **style-brief 解决**：谁在讲、怎么讲、用什么视觉路线、需要什么图片
- content-brief.json 是唯一核心生产交接单（不再使用 delivery-brief.json）
- style-brief.json 不替代 content-brief，只负责表达和视觉决策
- brief 文件是临时交接文件，发布后可根据需要清理
- 内容成品头部 YAML 需记录调用卡片、调用判例、content-brief 路径、style-brief 路径
