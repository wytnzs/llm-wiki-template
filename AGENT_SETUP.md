# AGENT_SETUP — Claude Code 初始化指南

本文档给 Claude Code 在初始化知识库时使用。

## 任务说明

为用户创建一套 AI 知识资产生产系统。这不是普通笔记库，而是一条从输入到输出的知识生产线。

## 执行步骤

### 1. 创建目录结构

```
00-Inbox/        原始输入
01-Projects/     当前项目
02-Areas/        长期资产
  知识卡片/      原子概念卡片
  案例库/        专业案例
  主题聚合/      长期记忆
03-Resources/    外部资料
04-Archive/      归档
05-Skills/       人看的手册
06-选题库/       选题资产
.claude/skills/  AI 执行技能
```

### 2. 复制模板

从 `templates/` 复制到对应目录。

### 3. 复制 Skill

从 `.claude/skills/` 复制到目标的 `.claude/skills/`。

### 4. 创建 CLAUDE.md

参考 `templates/CLAUDE.template.md` 生成。

### 5. 选择人群方案

根据用户回答选择方案（见 `docs/03-不同人群知识库方案.md`）。

### 6. 生成使用说明

输出一份给用户的简短使用指南。

## 约束

- 不要读取用户的隐私文件
- 不要上传内容到网络
- 不要引入数据库、RAG、MCP
- 不要把 Claude Code 改写成 Agent 或 Codex
