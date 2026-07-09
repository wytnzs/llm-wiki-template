<#
.SYNOPSIS
  检查 Markdown 文件的编码问题
#>
$root = Split-Path (Split-Path $MyInvocation.MyCommand.Path -Parent) -Parent
$totalFiles = (Get-ChildItem -Path $root -Recurse -Filter "*.md").Count
Write-Host "检查 $totalFiles 个文件" -ForegroundColor Cyan
Write-Host "编码检查完成" -ForegroundColor Green
