---
name: knowledge-base-collab
description: 知识库协作基础规则。定义内容归类、记灵感、卡片提炼、跨项目协同的流程。本系统是知识资产生产系统，不是普通资料库。
---

# 知识库协作 Skill

> 基于 Karpathy 三层架构 + Zettelkasten 卡片笔记法 + 概念思维 + OKF/GBrain 养护理念。
> 本 skill 只规定 HOW，不储存证据或知识观点。
> **本知识库不是普通资料库，而是一套「知识资产生产系统」——原材料加工成资产，资产按需组装产出。**

---

## 核心架构：五层生产链路

本知识库按 **输入层 → 资产层 → 项目层 → 输出层 → 反馈层** 五层组织：

```
输入层 (00-Inbox / 03-Resources)
    ↓ 提炼归类
资产层 (02-Areas: 知识卡片/案例库/主题聚合)
    ↓ 按需组装
项目层 (01-Projects)
    ↓ 调用资产 + skill
输出层 (生产管线产出)
    ↓ 复盘反哺
反馈层 (复盘与反哺)
```

**五层原则：** 每层只做自己层的事，不越界。

---

## 目录结构

```
你的知识库/
├── 00-Inbox/               ← 原始输入：想法、剪藏、临时笔记
├── 01-Projects/            ← 当前项目
├── 02-Areas/               ← 长期资产
│   ├── 知识卡片/            原子概念卡片
│   ├── 案例库/              专业案例三视图架构
│   └── 主题聚合/            长期记忆——围绕问题的当前认知
├── 03-Resources/           ← 外部参考资料
├── 04-Archive/             ← 归档
├── 05-Skills/              ← 给人看的手册和模板
├── 06-选题库/              ← 选题资产
└── .claude/skills/         ← Claude Code 执行用 skill
```

---

## 输入层 → 资产层的提炼路径

```
00-Inbox/ 或 03-Resources/ 中的原始材料
    ├── 能跨项目复用的抽象框架 → 知识卡片
    ├── 只服务某一类的具体事实 → 案例库（证据层）
    ├── 围绕某个问题的认知集合 → 主题聚合（长期记忆）
    ├── 有苗头的创作方向 → 待挖掘方向
    └── 完整外部笔记 → 03-Resources/
```

---

## OKF-like 原则：尽量带 YAML 元数据

### 知识卡片 YAML
```yaml
---
title: 概念名
tags: [domain, knowledge_card]
links: [[关联卡片]]
created: YYYY-MM-DD
updated: YYYY-MM-DD
source: 来源
---
```

### 主题地图 YAML
```yaml
---
title: 主题名
type: theme-map
tags: [theme_map]
created: YYYY-MM-DD
updated: YYYY-MM-DD
related_cards: [[卡片1]], [[卡片2]]
related_cases: [案例ID1, 案例ID2]
---
```

### 选题卡 YAML
```yaml
---
title: 选题名
type: topic-card
status: draft | active | published | archived
source_cards: [[卡片1]]
source_cases: [案例ID1]
related_theme: [[主题地图]]
content_stage: idea | brief | writing | done
created: YYYY-MM-DD
---
```

---

## 卡片格式

```markdown
---
title: 概念名
tags: [domain, knowledge_card]
links: [[关联卡片]]
created: YYYY-MM-DD
updated: YYYY-MM-DD
source: 来源
---
## 定义
## 关键要点
## 判断维度
## 案例
## 来源
```

---

## 触发场景

| 触发词 | 功能 |
|--------|------|
| `记一下：XXX` | 将灵感写入 00-Inbox |
| `整理收件箱` | 遍历 00-Inbox，分类提炼 |
| `提炼知识卡片` | 从素材提取原子概念 |
| `更新知识地图` | 扫描全库，刷新索引 |
| `查一下：XX` | 搜索知识卡片和案例库 |

---

## 原则

1. **原子化** —— 一张卡片只讲一个概念。
2. **双向链接** —— 用 `[[卡片名]]` 建立关联。
3. **概念为本** —— 卡片回答"这是什么"，不回答"具体哪个案子"。
4. **输出反哺** —— 每次生产结束，反哺到卡片/skill/主题地图。
5. **YAML 优先** —— 新资产尽量带元数据。
6. **不要跳过来源记录** —— 每篇内容头部记录调用卡片和案例。
7. **不要把 skill 变成资料库**。
