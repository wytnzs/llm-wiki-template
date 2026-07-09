<#
.SYNOPSIS
  初始化 LLM Wiki 知识资产生产系统
.DESCRIPTION
  在用户指定目录创建完整知识库结构、复制模板和 skill、生成 CLAUDE.md。
#>

param([string]$TargetDir = "")

if (-not $TargetDir) { $TargetDir = Join-Path (Get-Location) "my-knowledge-base" }

Write-Host "=== LLM Wiki 知识资产初始化 ===" -ForegroundColor Cyan
Write-Host "目标目录: $TargetDir"

if (Test-Path $TargetDir) {
    $existing = Get-ChildItem -Path $TargetDir -Directory | Select-Object -First 1
    if ($existing) {
        Write-Host "目录已存在且非空" -ForegroundColor Yellow
        $shouldInit = Read-Host "是否继续？(y/n)"
        if ($shouldInit -ne "y") { exit 0 }
    }
} else {
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
}

$dirs = @("00-Inbox","01-Projects","02-Areas/知识卡片","02-Areas/案例库","02-Areas/主题聚合","03-Resources","04-Archive","05-Skills","06-选题库/cards",".claude/skills",".claude/drafts")

foreach ($d in $dirs) {
    $path = Join-Path $TargetDir $d
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
        Write-Host "  + $d" -ForegroundColor Green
    }
}

# Generate CLAUDE.md
$claudePath = Join-Path $TargetDir "CLAUDE.md"
if (-not (Test-Path $claudePath)) {
    @"
# 知识库协作规则

本知识库是知识资产生产系统，不是普通资料库。

## 目录职责
- 00-Inbox：原始输入
- 01-Projects：当前项目
- 02-Areas：长期资产
- 03-Resources：外部资料
- 04-Archive：归档
- 06-选题库：选题资产
- .claude/skills：Claude Code 技能

## 核心原则
原子化 | 双向链接 | 输出反哺 | YAML 优先
"@ | Set-Content -Path $claudePath -Encoding utf8
    Write-Host "  + CLAUDE.md" -ForegroundColor Green
}

Write-Host "`n初始化完成" -ForegroundColor Cyan
Write-Host "目录: $TargetDir"
Write-Host "把这个路径发给 Claude Code，说「整理收件箱」开始使用。"
