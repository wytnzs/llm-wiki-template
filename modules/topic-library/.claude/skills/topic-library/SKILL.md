---
name: topic-library
description: 内容选题库管理器。负责选题卡片的创建、查重、评分、入库和 content-brief 交接。触发词：整理选题库、保存选题、沉淀选题、做成选题卡、生成 content-brief。
---

# 内容选题库 Topic Library

> 可选模块。只有用户明确启用选题库后才运行；候选选题需要用户确认，不宣称自动从知识卡片生成正式选题。

## 一、核心定位

回答四个问题：值不值得写？有没有重复？资产溯源是否完整？如何交给生产管线？

### 与 topic-selection 的关系
- topic-selection：选题挖掘引擎
- topic-library：选题库管理器
- 生产管线：消费 content-brief 写最终文案

## 二、好选题评分 Scale（7维度，每项1-5分）

| 维度 | 判断问题 |
|------|---------|
| 反差 | 用户以为 X，但其实 Y？ |
| 用户疼痛 | 目标用户是否在意？ |
| 证据支撑 | 有案例/卡片/经验支撑？ |
| 情绪爆点 | 有真实表达欲？ |
| 可迁移性 | 能从个案提炼方法？ |
| 人设匹配 | 强化定位？ |
| 平台适配 | 明确适合平台？ |

入库门槛：总分<24不入库；无来源资产不入正式库。

## 三、资产溯源规则

每个正式选题必须能回答"底气来自哪里？"

来源类型：知识卡片(source_cards)、案例(source_cases)、主题地图(related_theme)、个人经历、外部资料

## 四、选题卡片结构

```yaml
---
title: 选题标题
status: draft/active/published/archived
source_cards: []
source_cases: []
related_theme: ""
content_stage: idea/brief/writing/done
confidence: high/medium/low
priority: P0/P1/P2
topic_tree: ""
target_reader: ""
created: YYYY-MM-DD
---
```

## 五、硬约束

1. 没有来源资产的选题不能进入正式选题库
2. 不把个案结论包装成普遍规则
3. 不直接写最终文案，止步于 content-brief
4. 溯源字段必须写（可空数组但不能缺字段）
