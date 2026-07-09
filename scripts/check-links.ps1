<#
.SYNOPSIS
  检查 Markdown 文件中的断链
#>
$root = Split-Path (Split-Path $MyInvocation.MyCommand.Path -Parent) -Parent
$brokenLinks = @()
Get-ChildItem -Path $root -Recurse -Filter "*.md" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw -ErrorAction SilentlyContinue
    if ($content) {
        $matches = [regex]::Matches($content, '\[\[([^\]]+)\]\]')
        foreach ($m in $matches) {
            $linkName = $m.Groups[1].Value
            $found = Get-ChildItem -Path $root -Recurse -Filter "$linkName.md" -ErrorAction SilentlyContinue
            if (-not $found -and $linkName -notmatch "^(卡片|案例|题)") {
                $brokenLinks += "$($_.Name): [[$linkName]]"
            }
        }
    }
}
if ($brokenLinks.Count -eq 0) {
    Write-Host "断链检查通过" -ForegroundColor Green
} else {
    Write-Host "发现 $($brokenLinks.Count) 个断链：" -ForegroundColor Yellow
    $brokenLinks | ForEach-Object { Write-Host "  $_" }
}
