<#
.SYNOPSIS
  初始化最小知识库，并在安装可选模块前征求用户意见。
#>

param(
    [string]$TargetDir = "",
    [ValidateSet("ask", "yes", "no")][string]$KnowledgeMap = "ask",
    [ValidateSet("ask", "yes", "no")][string]$CaseLibrary = "ask",
    [ValidateSet("ask", "yes", "no")][string]$TopicLibrary = "ask"
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path (Split-Path $MyInvocation.MyCommand.Path -Parent) -Parent

if (-not $TargetDir) {
    $TargetDir = Join-Path (Get-Location) "my-knowledge-base"
}

function Resolve-Choice {
    param([string]$Value, [string]$Prompt)
    if ($Value -eq "yes") { return $true }
    if ($Value -eq "no") { return $false }
    return (Read-Host "$Prompt (y/n)") -eq "y"
}

Write-Host "=== LLM Wiki 最小知识库初始化 ===" -ForegroundColor Cyan
Write-Host "目标目录: $TargetDir"

if (Test-Path $TargetDir) {
    $existing = Get-ChildItem -LiteralPath $TargetDir -Force | Select-Object -First 1
    if ($existing -and (Read-Host "目录非空。是否在保留现有内容的前提下继续？(y/n)") -ne "y") {
        exit 0
    }
} else {
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
}

$enableMap = Resolve-Choice $KnowledgeMap "是否需要知识库地图（统计和健康检查）"
$enableCases = Resolve-Choice $CaseLibrary "是否需要案例库"
$enableTopics = Resolve-Choice $TopicLibrary "是否需要选题库和内容选题 Skill"

$dirs = @(
    "00-Inbox",
    "01-Projects",
    "02-Areas/知识卡片",
    "02-Areas/主题中心/主题页",
    "03-Resources",
    "03-Resources/个人输入",
    "03-Resources/系统资料",
    "05-Skills/_templates",
    ".claude/skills",
    ".claude/drafts"
)

if ($enableCases) { $dirs += "02-Areas/案例库" }
if ($enableTopics) { $dirs += "06-选题库/cards" }

foreach ($dir in $dirs) {
    New-Item -ItemType Directory -Path (Join-Path $TargetDir $dir) -Force | Out-Null
}

$today = Get-Date -Format "yyyy-MM-dd"
$copyMap = @{
    "templates/knowledge-card.template.md" = "02-Areas/知识卡片/_template.md"
    "templates/theme-center.template.md" = "02-Areas/主题中心/README.md"
    "templates/theme-map.template.md" = "02-Areas/主题中心/主题页/_template.md"
    "templates/resource-layer.template.md" = "03-Resources/README.md"
    "templates/resource-workbench.template.md" = "03-Resources/资源工作台.md"
    "templates/project-status.template.md" = "05-Skills/_templates/project-status.md"
    "templates/review.template.md" = "05-Skills/_templates/review.md"
    "templates/content-brief.template.json" = "05-Skills/_templates/content-brief.json"
    "docs/知识库运作系统与协作边界.md" = "05-Skills/知识库运作系统与协作边界.md"
    "docs/知识关系与索引规则.md" = "05-Skills/知识关系与索引规则.md"
    "docs/定期维护与审计.md" = "05-Skills/定期维护与审计.md"
}

foreach ($item in $copyMap.GetEnumerator()) {
    $destination = Join-Path $TargetDir $item.Value
    if (-not (Test-Path $destination)) {
        if ($item.Key -in @("templates/theme-center.template.md", "templates/resource-layer.template.md", "templates/resource-workbench.template.md")) {
            $content = Get-Content (Join-Path $repoRoot $item.Key) -Encoding utf8 -Raw
            $content.Replace("YYYY-MM-DD", $today) | Set-Content -LiteralPath $destination -Encoding utf8
        } else {
            Copy-Item (Join-Path $repoRoot $item.Key) $destination
        }
    }
}

$readmePath = Join-Path $TargetDir "README.md"
if (-not (Test-Path $readmePath)) {
    Copy-Item (Join-Path $repoRoot "templates/README.template.md") $readmePath
}

$claudePath = Join-Path $TargetDir "CLAUDE.md"
if (-not (Test-Path $claudePath)) {
    Copy-Item (Join-Path $repoRoot "templates/CLAUDE.template.md") $claudePath
}

$governanceFiles = @{
    "templates/ai-review-queue.template.md" = "00-Inbox/AI待确认.md"
    "templates/knowledge-change-log.template.md" = "知识库变更日志.md"
}

foreach ($item in $governanceFiles.GetEnumerator()) {
    $destination = Join-Path $TargetDir $item.Value
    if (-not (Test-Path $destination)) {
        $content = Get-Content (Join-Path $repoRoot $item.Key) -Encoding utf8 -Raw
        $content.Replace("YYYY-MM-DD", $today) | Set-Content -LiteralPath $destination -Encoding utf8
    }
}

$agentsPath = Join-Path $TargetDir "AGENTS.md"
if (-not (Test-Path $agentsPath)) {
    Copy-Item (Join-Path $repoRoot "AGENTS.md") $agentsPath
}

Copy-Item (Join-Path $repoRoot ".claude/skills/*") (Join-Path $TargetDir ".claude/skills") -Recurse -Force

if ($enableMap) {
    Copy-Item (Join-Path $repoRoot "modules/knowledge-map/.claude/skills/*") (Join-Path $TargetDir ".claude/skills") -Recurse -Force
    $mapPath = Join-Path $TargetDir "知识库地图.md"
    if (-not (Test-Path $mapPath)) {
        $mapContent = Get-Content (Join-Path $repoRoot "modules/knowledge-map/templates/knowledge-map.template.md") -Encoding utf8 -Raw
        $mapContent.Replace("YYYY-MM-DD", $today) | Set-Content -LiteralPath $mapPath -Encoding utf8
    }
}

if ($enableCases) {
    Copy-Item (Join-Path $repoRoot "modules/case-library/.claude/skills/*") (Join-Path $TargetDir ".claude/skills") -Recurse -Force
}

if ($enableTopics) {
    Copy-Item (Join-Path $repoRoot "modules/topic-library/.claude/skills/*") (Join-Path $TargetDir ".claude/skills") -Recurse -Force
    Copy-Item (Join-Path $repoRoot "modules/topic-library/templates/topic-card.template.md") (Join-Path $TargetDir "06-选题库/_template.md")
}

Write-Host "初始化完成: $TargetDir" -ForegroundColor Green
Write-Host "请打开 README.md，补充你的目的和目录职责。"
