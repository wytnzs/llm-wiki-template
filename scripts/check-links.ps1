<#
.SYNOPSIS
  检查 Markdown 相对链接和 Obsidian 双向链接。
#>

$root = Split-Path (Split-Path $MyInvocation.MyCommand.Path -Parent) -Parent
$issues = @()
$markdownFiles = @(Get-ChildItem -Path $root -Recurse -File -Filter '*.md' |
    Where-Object { $_.FullName -notlike '*\.git\*' })
$wikiNames = @{}

foreach ($markdownFile in $markdownFiles) {
    $wikiNames[$markdownFile.BaseName] = $true
}

$markdownFiles | ForEach-Object {
        $file = $_
        $content = Get-Content -LiteralPath $file.FullName -Encoding utf8 -Raw -ErrorAction SilentlyContinue
        if (-not $content) { return }

        # Templates and documentation often contain example links inside fenced blocks.
        $contentToCheck = [regex]::Replace($content, '(?ms)^```.*?^```\s*', '')

        foreach ($match in [regex]::Matches($contentToCheck, '\[[^\]]+\]\(([^)]+)\)')) {
            $target = $match.Groups[1].Value.Split('#')[0]
            if (-not $target -or $target -match '^(https?:|mailto:|#)') { continue }
            $resolved = Join-Path $file.DirectoryName ([uri]::UnescapeDataString($target))
            if (-not (Test-Path -LiteralPath $resolved)) {
                $issues += "$($file.FullName): $target"
            }
        }

        if ($file.Name -notlike '*.template.md') {
            foreach ($match in [regex]::Matches($contentToCheck, '\[\[([^\]|#]+)')) {
                $name = $match.Groups[1].Value
                if (-not $wikiNames.ContainsKey($name)) { $issues += "$($file.FullName): [[$name]]" }
            }
        }
    }

if ($issues.Count -gt 0) {
    Write-Host "发现 $($issues.Count) 个断链" -ForegroundColor Yellow
    $issues | ForEach-Object { Write-Host "  $_" }
    exit 1
}

Write-Host '链接检查通过' -ForegroundColor Green
