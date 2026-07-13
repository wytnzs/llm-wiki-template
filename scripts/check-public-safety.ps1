<#
.SYNOPSIS
  检查公开仓库是否误包含敏感数据
#>

$issues = @()
$root = Split-Path (Split-Path $MyInvocation.MyCommand.Path -Parent) -Parent

Write-Host "=== 安全检查 ===" -ForegroundColor Cyan

$forbiddenDirs = @("00-Inbox","01-Projects","02-Areas","03-Resources",".obsidian",".codex")
foreach ($d in $forbiddenDirs) {
    $path = Join-Path $root $d
    if (Test-Path $path) {
        Write-Host " 发现可能含真实数据的目录: $d" -ForegroundColor Yellow
        $issues += $d
    }
}

$forbiddenFiles = @(".claude/settings.local.json","content-brief.json")
foreach ($f in $forbiddenFiles) {
    if (Test-Path (Join-Path $root $f)) {
        Write-Host " 发现敏感配置文件: $f" -ForegroundColor Yellow
        $issues += $f
    }
}

if ($issues.Count -eq 0) {
    Write-Host "安全检查通过，未发现敏感数据" -ForegroundColor Green
    exit 0
} else {
    Write-Host "发现 $($issues.Count) 个问题，push 前请处理" -ForegroundColor Yellow
    exit 1
}
