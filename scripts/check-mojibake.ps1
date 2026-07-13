<#
.SYNOPSIS
  检查 Markdown 文件中的常见乱码标记。
#>

$root = Split-Path (Split-Path $MyInvocation.MyCommand.Path -Parent) -Parent
$patterns = @('�', '锟斤拷', 'Ã', 'Â', 'â€™', 'â€œ', 'â€')
$issues = @()

Get-ChildItem -Path $root -Recurse -File -Filter '*.md' |
    Where-Object { $_.FullName -notlike '*\.git\*' } |
    ForEach-Object {
        $content = Get-Content -LiteralPath $_.FullName -Encoding utf8 -Raw -ErrorAction SilentlyContinue
        foreach ($pattern in $patterns) {
            if ($content -and $content.Contains($pattern)) {
                $issues += "$($_.FullName): $pattern"
                break
            }
        }
    }

if ($issues.Count -gt 0) {
    Write-Host "发现 $($issues.Count) 个疑似乱码文件" -ForegroundColor Yellow
    $issues | ForEach-Object { Write-Host "  $_" }
    exit 1
}

Write-Host '乱码检查通过' -ForegroundColor Green
