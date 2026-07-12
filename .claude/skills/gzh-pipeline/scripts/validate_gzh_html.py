#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_gzh_html.py
====================
公众号 HTML 排版合规校验脚本。

检查生成的 _preview.html 是否符合微信公众号编辑器要求：
1. 平台禁用标签检查（<style> / <script> / <div class=…>）
2. 样式内联检查（无外部 CSS，所有样式在 style="" 内）
3. 半角标点警告（正文中的半角逗号/句号/引号）
4. 预览文件配图卡片检查（不含下载按钮）
5. position 属性检查（fixed/absolute/sticky 禁用）

使用方式：
    python validate_gzh_html.py <生成的.html 文件路径>
    python validate_gzh_html.py <生成的.html 文件路径> --quiet   # 只输出结论
    python validate_gzh_html.py <生成的.html 文件路径> --fix      # 自动修复半角标点

退出码：
    0 — 校验通过（无 ERROR，WARNING 可接受）
    1 — 有 ERROR 未修复
"""

import re
import sys
import os

# ─── 平台红线 ──────────────────────────────────────────────

FORBIDDEN_TAGS = [
    ("<style", "`<style>` 标签：样式必须内联（style=\"\"），不能写在 <style> 块中"),
    ("</style>", "`</style>` 标签：同上"),
    ("<script", "`<script>` 标签：公众号编辑器中不可用"),
    ("</script>", "`</script>` 标签：同上"),
    ('<div ', "`<div>` 标签：公众号编辑器只支持 section/p/span 等容器"),
    ('</div>', "`</div>` 结束标签：同上"),
]

FORBIDDEN_STYLES = [
    ("position:fixed", "position:fixed — 公众号编辑器不支持"),
    ("position:absolute", "position:absolute — 公众号编辑器不支持"),
    ("position:sticky", "position:sticky — 公众号编辑器不支持"),
    ("@media", "@media 查询 — 公众号编辑器不支持"),
    ("@keyframes", "@keyframes 动画 — 公众号编辑器不支持"),
    ("display:grid", "display:grid — 公众号编辑器不支持"),
]

HALF_WIDTH_PUNCTUATION = re.compile(r"(?<!\w)[,\.!?:;](?!\w)|[,\.!?:;](?=\s)|[\"\']")

CODE_BLOCK_MARKERS = ["<code>", "</code>", "<pre>", "</pre>"]
HALF_WIDTH_EXCEPTIONS = ["http://", "https://", "www.", ".com", ".cn", ".org"]


def read_file(path):
    """读取 HTML 文件内容"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def check_forbidden_tags(html, filepath):
    """检查平台禁用标签"""
    errors = []
    for tag, message in FORBIDDEN_TAGS:
        if tag in html:
            # 找出具体行号
            lines = html.split("\n")
            for i, line in enumerate(lines, 1):
                if tag in line:
                    errors.append((f"  [FAIL] ERROR: {message}", i, line.strip()[:120]))
                    break
            else:
                errors.append((f"  [FAIL] ERROR: {message}", 0, ""))
    return errors


def check_forbidden_styles(html):
    """检查平台禁用样式属性"""
    errors = []
    for prop, message in FORBIDDEN_STYLES:
        if prop in html:
            errors.append((f"  [FAIL] ERROR: {message}", 0, ""))
    return errors


def check_inline_styles(html):
    """检查是否有外部 <link> 或 @import（应全部内联）"""
    errors = []
    if '<link rel="stylesheet"' in html:
        errors.append(("  [FAIL] ERROR: 外部样式表 <link> — 必须全部内联", 0, ""))
    if "@import" in html:
        errors.append(("  [FAIL] ERROR: @import 外部样式 — 必须全部内联", 0, ""))
    return errors


def check_half_width_punctuation(html):
    """检查正文中的半角标点（代码块内不检查）"""
    warnings = []
    lines = html.split("\n")
    in_code_block = False

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped:
            continue

        # 跳过代码块
        if "<code>" in stripped or "<pre>" in stripped:
            in_code_block = True
        if in_code_block:
            if "</code>" in stripped or "</pre>" in stripped:
                in_code_block = False
            continue

        # 跳过明显的 URL 行、仅标签行
        if any(e in stripped for e in HALF_WIDTH_EXCEPTIONS):
            continue
        if stripped.startswith("<") and stripped.endswith(">"):
            continue

        # 只检查正文段落（span 包裹的文字或裸文字）
        # 检查半角标点
        matches = HALF_WIDTH_PUNCTUATION.findall(stripped)
        if matches:
            # 只报告第一个匹配的上下文
            context = stripped[:100]
            warnings.append((
                f"  [WARN] WARNING: 半角标点（行 {i}）— "
                f"应将 ,.!?:;\"' 改为全角 ，。！？：；""''",
                i,
                context
            ))
    return warnings


def check_preview_no_download_buttons(html, filepath):
    """检查 _preview.html 中不应有下载按钮"""
    errors = []
    if "_preview.html" not in filepath and "preview" not in filepath.lower():
        return errors  # 只检查预览文件

    if "downloadCard" in html or "downloadCover" in html or "illu-download-btn" in html:
        # 再看是否真的在正文中（非注释代码示例中）
        # 排除代码示例中的引用
        in_example = 0
        lines = html.split("\n")
        current_line = 0
        for i, line in enumerate(lines):
            if "illu-download-btn" in line and "```" not in line and "示例" not in line:
                current_line = i + 1
                errors.append((
                    f"  [FAIL] ERROR: 预览文件包含下载按钮 class='illu-download-btn'（行 {current_line}）",
                    current_line,
                    line.strip()[:120]
                ))
            if "downloadCard" in line and "```" not in line and "示例" not in line:
                current_line = i + 1
                errors.append((
                    f"  [FAIL] ERROR: 预览文件包含 downloadCard 函数（行 {current_line}）",
                    current_line,
                    line.strip()[:120]
                ))
    return errors


def validate(html, filepath, quiet=False):
    """执行全部校验，返回 (has_error, has_warning, details)"""
    all_errors = []
    all_warnings = []

    # 1. 禁用标签
    all_errors.extend(check_forbidden_tags(html, filepath))

    # 2. 禁用样式
    all_errors.extend(check_forbidden_styles(html))

    # 3. 外部样式
    all_errors.extend(check_inline_styles(html))

    # 4. 半角标点
    all_warnings.extend(check_half_width_punctuation(html))

    # 5. 预览文件下载按钮
    all_errors.extend(check_preview_no_download_buttons(html, filepath))

    # 去重
    seen = set()
    deduped_errors = []
    for e in all_errors:
        key = e[0][:80]
        if key not in seen:
            seen.add(key)
            deduped_errors.append(e)

    has_error = len(deduped_errors) > 0
    has_warning = len(all_warnings) > 0

    return has_error, has_warning, deduped_errors, all_warnings


def fix_half_width_punctuation(html):
    """自动修复半角标点为全角（仅在正文中修复）"""
    # 逐行处理，跳过代码块
    lines = html.split("\n")
    fixed_lines = []
    in_code = False

    # 全角映射
    fullwidth_map = {
        ',': '，', '.': '。', '!': '！', '?': '？',
        ':': '：', ';': '；',
        '"': '“',  # 左弯引
        "'": '‘',  # 左弯单引
    }

    for line in lines:
        stripped = line.strip()
        if "<code>" in stripped or "<pre>" in stripped:
            in_code = True
            fixed_lines.append(line)
            continue
        if in_code:
            if "</code>" in stripped or "</pre>" in stripped:
                in_code = False
            fixed_lines.append(line)
            continue

        # 修复正文中的半角标点
        # 只在文本内容中替换，不在 HTML 标签属性中替换
        result = []
        i = 0
        while i < len(line):
            if line[i] == '<':
                # 找到标签结束
                end = line.find('>', i)
                if end != -1:
                    result.append(line[i:end+1])
                    i = end + 1
                    continue
            if line[i] in fullwidth_map:
                # 跳过 URL
                if line[max(0,i-5):i+5] in HALF_WIDTH_EXCEPTIONS or \
                   any(line[i:i+len(e)] == e for e in HALF_WIDTH_EXCEPTIONS if i+len(e) <= len(line)):
                    result.append(line[i])
                    i += 1
                    continue
                result.append(fullwidth_map[line[i]])
                i += 1
            else:
                result.append(line[i])
                i += 1
        fixed_lines.append("".join(result))

    return "\n".join(fixed_lines)


def main():
    if len(sys.argv) < 2:
        print("用法: python validate_gzh_html.py <文件路径> [--quiet] [--fix]")
        sys.exit(1)

    filepath = sys.argv[1]
    quiet = "--quiet" in sys.argv
    do_fix = "--fix" in sys.argv

    if not os.path.exists(filepath):
        print(f"[FAIL] 文件不存在: {filepath}")
        sys.exit(1)

    html = read_file(filepath)

    has_error, has_warning, errors, warnings = validate(html, filepath, quiet)

    print(f"\n== 排版校验报告 — {os.path.basename(filepath)}\n")
    print("=" * 50)

    if not errors and not warnings:
        print("\n[OK] 排版校验通过（0 ERROR, 0 WARNING）\n")
        sys.exit(0)

    if errors:
        print(f"\n[FAIL] {len(errors)} 个 ERROR（必须修复）:\n")
        for msg, line, ctx in errors:
            print(msg)
            if line:
                print(f"     行 {line}: {ctx}")
        print()

    if warnings:
        print(f"\n[WARN]  {len(warnings)} 个 WARNING（建议修复）:\n")
        shown = set()
        for msg, line, ctx in warnings:
            if ctx not in shown:
                print(msg)
                shown.add(ctx)
        if len(warnings) > len(shown):
            print(f"   （还有 {len(warnings) - len(shown)} 处同类问题未展示）")
        print()

    if has_error:
        print(f"[FAIL] 排版校验未通过，{len(errors)} 个 ERROR 待修复\n")
        if do_fix:
            print("[WARN] 自动修复仅支持半角标点，ERROR 需手动修复\n")
        sys.exit(1)

    if has_warning:
        print(f"[OK] 排版校验通过（0 ERROR, {len(warnings)} WARNING）\n")
        if do_fix:
            fixed = fix_half_width_punctuation(html)
            backup = filepath + ".bak"
            os.rename(filepath, backup)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(fixed)
            print(f"[FIX] 已自动修复半角标点（原文件备份为 {backup}）\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
