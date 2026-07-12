#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
md2wechat_formatter.py
======================
Markdown → 公众号 HTML 排版工具（自包含实现，不依赖外部 markdown 解析库）

使用方式：
    python md2wechat_formatter.py <文章.md> --theme deepblue --font-size medium -o output.html
    python md2wechat_formatter.py <文章.md> --theme warm-story -o output.html
    python md2wechat_formatter.py <文章.md>                          # 默认 deepblue 主题

主题（新 - 与 gzh-pipeline 多主题系统对齐）：
    deepblue（默认） — 深蓝商务（#102542 + 暖橙 #F77F00）
    warm-story      — 暖橙故事（#FAFAF7 米白 + 琥珀 #C4814A）
    tech-dark       — 科技暗色（#0D0D0D 极黑 + 青 #00D4FF）

主题（旧 - 兼容遗留）：
    01fish          — 01鱼商务风
    chinese         — 中国风（深红 + 金色 + 米白）
    apple           — 极简优雅（黑 + 白 + 灰）

字号：
    small  — 14px
    medium — 15px（默认）
    large  — 16px
"""

import re
import sys
import os
import argparse
from pathlib import Path

# ─────────────────────────────────────────────────────────────
# 主题色定义
# ─────────────────────────────────────────────────────────────

THEMES = {
    # ===== 新主题（与 gzh-pipeline theme-*.md 对齐） =====
    "deepblue": {
        "body_bg": "#FFFFFF",
        "h1_color": "#102542",
        "h2_color": "#102542",
        "h3_color": "#0A1931",
        "text_color": "#1A1A1A",
        "secondary_color": "#86909C",
        "border": "#E5EAF2",
        "accent": "#F77F00",
        "accent_bg": "rgba(247,127,0,0.10)",
        "quote_bg": "#F7F9FC",
        "table_alt": "#F7F9FC",
        "tag_bg": "rgba(247,127,0,0.08)",
        "code_bg": "#F7F9FC",
        "code_color": "#F77F00",
        "pre_bg": "#102542",
        "pre_text": "#FFFFFF",
    },
    "warm-story": {
        "body_bg": "#FAFAF7",
        "h1_color": "#5C3D2E",
        "h2_color": "#5C3D2E",
        "h3_color": "#3D2E1E",
        "text_color": "#3D2E1E",
        "secondary_color": "#9B8B7A",
        "border": "#E5D8CC",
        "accent": "#C4814A",
        "accent_bg": "rgba(196,129,74,0.10)",
        "quote_bg": "#F5F0EB",
        "table_alt": "#F5F0EB",
        "tag_bg": "rgba(196,129,74,0.08)",
        "code_bg": "#F5F0EB",
        "code_color": "#C4814A",
        "pre_bg": "#3D2E1E",
        "pre_text": "#FAFAF7",
    },
    "minimal-fresh": {
        "body_bg": "#FFFFFF",
        "h1_color": "#1A1A1A",
        "h2_color": "#1A1A1A",
        "h3_color": "#444444",
        "text_color": "#333333",
        "secondary_color": "#999999",
        "border": "#EEEEEE",
        "accent": "#7A9E8E",
        "accent_bg": "rgba(122,158,142,0.08)",
        "quote_bg": "#F8F9FA",
        "table_alt": "#FBFCFC",
        "tag_bg": "rgba(122,158,142,0.06)",
        "code_bg": "#F8F9FA",
        "code_color": "#7A9E8E",
        "pre_bg": "#F5F7F6",
        "pre_text": "#333333",
    },
    "tech-dark": {
        "body_bg": "#0D0D0D",
        "h1_color": "#FFFFFF",
        "h2_color": "#FFFFFF",
        "h3_color": "#FFFFFF",
        "text_color": "#E0E0E0",
        "secondary_color": "#6A7A8A",
        "border": "#2A2A3E",
        "accent": "#00D4FF",
        "accent_bg": "rgba(0,212,255,0.12)",
        "quote_bg": "#1A1A2E",
        "table_alt": "#1A1A2E",
        "tag_bg": "rgba(0,212,255,0.08)",
        "code_bg": "#1A1A2E",
        "code_color": "#00D4FF",
        "pre_bg": "#00D4FF",
        "pre_text": "#0D0D0D",
    },
    # ===== 旧主题（兼容遗留） =====
    "01fish": {
        "body_bg": "#FFFFFF",
        "h1_color": "#1A3328",
        "h2_color": "#1A3328",
        "h3_color": "#1A3328",
        "text_color": "#1A1A2E",
        "secondary_color": "#7A8C80",
        "border": "#E5EAF2",
        "accent": "#C44536",
        "accent_bg": "rgba(196,69,54,0.06)",
        "quote_bg": "rgba(26,51,40,0.05)",
        "table_alt": "#F2EDE3",
        "tag_bg": "rgba(26,51,40,0.06)",
        "code_bg": "#F2EDE3",
        "code_color": "#C44536",
        "pre_bg": "#1A3328",
        "pre_text": "#F2EDE3",
    },
    "chinese": {
        "body_bg": "#FFFFFF",
        "h1_color": "#8B0000",
        "h2_color": "#8B0000",
        "h3_color": "#333333",
        "text_color": "#333333",
        "secondary_color": "#888888",
        "border": "#D4C5A0",
        "accent": "#C9A96E",
        "accent_bg": "rgba(201,169,110,0.08)",
        "quote_bg": "rgba(139,0,0,0.04)",
        "table_alt": "#FBF7EE",
        "tag_bg": "rgba(139,0,0,0.05)",
        "code_bg": "#FBF7EE",
        "code_color": "#8B0000",
        "pre_bg": "#8B0000",
        "pre_text": "#F5E6C8",
    },
    "apple": {
        "body_bg": "#FFFFFF",
        "h1_color": "#1D1D1F",
        "h2_color": "#1D1D1F",
        "h3_color": "#1D1D1F",
        "text_color": "#1D1D1F",
        "secondary_color": "#86868B",
        "border": "#E5E5E7",
        "accent": "#0066CC",
        "accent_bg": "rgba(0,102,204,0.05)",
        "quote_bg": "rgba(0,0,0,0.03)",
        "table_alt": "#F5F5F7",
        "tag_bg": "rgba(0,0,0,0.03)",
        "code_bg": "#F5F5F7",
        "code_color": "#0066CC",
        "pre_bg": "#1D1D1F",
        "pre_text": "#F5F5F7",
    },
}

# 主题别名映射（旧名 → 新名）
THEME_ALIASES = {
    "保险其实不难": "deepblue",
}

FONT_SIZES = {
    "small": {"body": "14px", "h1": "20px", "h2": "17px", "h3": "15px", "table": "13px"},
    "medium": {"body": "15px", "h1": "22px", "h2": "18px", "h3": "15px", "table": "14px"},
    "large": {"body": "16px", "h1": "24px", "h2": "19px", "h3": "16px", "table": "15px"},
}

def resolve_theme(name):
    """解析主题名（支持别名映射）"""
    resolved = THEME_ALIASES.get(name, name)
    if resolved in THEMES:
        return resolved
    return "deepblue"  # 默认 fallback

# ─────────────────────────────────────────────────────────────
# Markdown 解析（正则自实现，不依赖外部库）
# ─────────────────────────────────────────────────────────────

def escape_html(text):
    """HTML 实体转义"""
    return (text
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;"))

def parse_inline(text):
    """解析行内格式：加粗、斜体、删除线、行内代码、链接"""
    # 行内代码 `code`
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # 图片 ![alt](url)  — 公众号不支持图片外链，转为占位符
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<span class="img-ref">[\1]</span>', text)
    # 链接 [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)
    # 删除线 ~~text~~
    text = re.sub(r'~~([^~]+)~~', r'<del>\1</del>', text)
    # 加粗 **text** 或 __text__
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__([^_]+)__', r'<strong>\1</strong>', text)
    # 斜体 *text* 或 _text_（排除已处理的）
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'(?<!_) _([^_]+)_(?!_)', r'<em>\1</em>', text)
    return text

def parse_heading(line):
    """解析标题行"""
    m = re.match(r'^(#{1,6})\s+(.*)', line.strip())
    if not m:
        return None
    level = len(m.group(1))
    content = m.group(2).strip()
    return level, content

def parse_table(lines, line_idx):
    """解析表格块，返回 (html, consumed_lines)"""
    if line_idx >= len(lines):
        return None, 0

    table_lines = []
    i = line_idx
    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped or not stripped.startswith('|'):
            break
        table_lines.append(stripped)
        i += 1

    if len(table_lines) < 2:
        return None, 0

    align_line = table_lines[1]
    if not re.match(r'^\|[\s\-:|]+\|$', align_line):
        return None, 0

    align_cells = [c.strip() for c in align_line.split('|')[1:-1]]
    aligns = []
    for cell in align_cells:
        if cell.startswith(':') and cell.endswith(':'):
            aligns.append('center')
        elif cell.endswith(':'):
            aligns.append('right')
        else:
            aligns.append('left')

    header_cells = [c.strip() for c in table_lines[0].split('|')[1:-1]]
    th_html = ''.join(f'<th style="text-align:{aligns[i] if i < len(aligns) else "left"};">{parse_inline(header_cells[i])}</th>'
                       for i in range(len(header_cells)))

    td_rows = ''
    for row_line in table_lines[2:]:
        cells = [c.strip() for c in row_line.split('|')[1:-1]]
        td_rows += '<tr>'
        for j, cell in enumerate(cells):
            align = aligns[j] if j < len(aligns) else 'left'
            td_rows += f'<td style="text-align:{align};">{parse_inline(cell)}</td>'
        td_rows += '</tr>'

    html = f'<table><thead><tr>{th_html}</tr></thead><tbody>{td_rows}</tbody></table>'
    return html, len(table_lines)

def parse_blockquote(lines, line_idx):
    """解析引用块"""
    if line_idx >= len(lines) or not lines[line_idx].strip().startswith('>'):
        return None, 0

    content_lines = []
    i = line_idx
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('>'):
            inner = line.lstrip('>').strip()
            if inner:
                content_lines.append(inner)
            i += 1
        else:
            break

    if not content_lines:
        return None, 0

    inner_html = ' '.join(parse_inline(l) for l in content_lines)
    return f'<blockquote><p>{inner_html}</p></blockquote>', i - line_idx

def parse_code_block(lines, line_idx):
    """解析围栏代码块"""
    if line_idx >= len(lines):
        return None, 0

    stripped = lines[line_idx].strip()
    if not (stripped.startswith('```') or stripped.startswith('~~~')):
        return None, 0

    fence_char = stripped[0]
    lang = stripped[1:].strip()

    content_lines = []
    i = line_idx + 1
    while i < len(lines):
        if lines[i].strip().startswith(fence_char) and len(lines[i].strip()) >= 3:
            break
        content_lines.append(escape_html(lines[i]))
        i += 1

    code_content = '\n'.join(content_lines)
    return f'<pre><code class="language-{lang}">{code_content}</code></pre>', i - line_idx + 1

def parse_list(lines, line_idx):
    """解析无序列表"""
    if line_idx >= len(lines):
        return None, 0

    list_items = []
    i = line_idx
    while i < len(lines):
        line = lines[i].strip()
        m = re.match(r'^[-*+]\s+(.*)', line)
        if not m:
            break
        list_items.append(f'<li>{parse_inline(m.group(1))}</li>')
        i += 1

    if not list_items:
        return None, 0

    return f'<ul>{"".join(list_items)}</ul>', i - line_idx

def parse_ordered_list(lines, line_idx):
    """解析有序列表"""
    if line_idx >= len(lines):
        return None, 0

    list_items = []
    i = line_idx
    while i < len(lines):
        line = lines[i].strip()
        m = re.match(r'^\d+[.)]\s+(.*)', line)
        if not m:
            break
        list_items.append(f'<li>{parse_inline(m.group(1))}</li>')
        i += 1

    if not list_items:
        return None, 0

    return f'<ol>{"".join(list_items)}</ol>', i - line_idx

def parse_hr(line):
    """解析分隔线"""
    stripped = line.strip()
    if re.match(r'^[-*_]{3,}$', stripped):
        return '<hr />'
    return None

def parse_paragraph(lines, line_idx):
    """解析普通段落（直到遇到空行或特殊块）"""
    para_lines = []
    i = line_idx
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            break

        if stripped.startswith('#'):
            break
        if stripped.startswith('|') and re.match(r'^\|[\s\-:|]+\|$', stripped):
            break
        if stripped.startswith('```') or stripped.startswith('~~~'):
            break
        if stripped.startswith('>'):
            break
        if re.match(r'^[-*+]\s+', stripped):
            break
        if re.match(r'^\d+[.)]\s+', stripped):
            break
        if re.match(r'^[-*_]{3,}$', stripped):
            break

        para_lines.append(stripped)
        i += 1

    if not para_lines:
        return None, 0

    content = ' '.join(parse_inline(line) for line in para_lines)
    return f'<p>{content}</p>', i - line_idx

def markdown_to_html(md_text):
    """Markdown → HTML 主转换函数"""
    lines = md_text.split('\n')
    html_parts = []
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # 标题
        heading = parse_heading(line)
        if heading:
            level, content = heading
            if level == 1:
                html_parts.append(f'<h1>{parse_inline(content)}</h1>')
            elif level == 2:
                html_parts.append(f'<h2>{parse_inline(content)}</h2>')
            else:
                html_parts.append(f'<h3>{parse_inline(content)}</h3>')
            i += 1
            continue

        # 分隔线
        hr = parse_hr(stripped)
        if hr:
            html_parts.append(hr)
            i += 1
            continue

        # 表格
        table_html, consumed = parse_table(lines, i)
        if table_html:
            html_parts.append(table_html)
            i += consumed
            continue

        # 引用块
        bq_html, consumed = parse_blockquote(lines, i)
        if bq_html:
            html_parts.append(bq_html)
            i += consumed
            continue

        # 代码块
        code_html, consumed = parse_code_block(lines, i)
        if code_html:
            html_parts.append(code_html)
            i += consumed
            continue

        # 无序列表
        ul_html, consumed = parse_list(lines, i)
        if ul_html:
            html_parts.append(ul_html)
            i += consumed
            continue

        # 有序列表
        ol_html, consumed = parse_ordered_list(lines, i)
        if ol_html:
            html_parts.append(ol_html)
            i += consumed
            continue

        # 普通段落
        p_html, consumed = parse_paragraph(lines, i)
        if p_html:
            html_parts.append(p_html)
            i += consumed
            continue

        # 未匹配，默认按段落处理
        html_parts.append(f'<p>{parse_inline(stripped)}</p>')
        i += 1

    return '\n'.join(html_parts)

# ─────────────────────────────────────────────────────────────
# HTML 模板生成
# ─────────────────────────────────────────────────────────────

def build_css(theme_name, font_size_name):
    """构建完整的 CSS"""
    resolved = resolve_theme(theme_name)
    t = THEMES.get(resolved, THEMES["deepblue"])
    f = FONT_SIZES.get(font_size_name, FONT_SIZES["medium"])

    return f"""
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: -apple-system, 'PingFang SC', 'Microsoft YaHei', sans-serif;
    font-size: {f['body']};
    line-height: 1.9;
    color: {t['text_color']};
    background: {t['body_bg']};
    padding: 20px 24px;
    max-width: 677px;
    margin: 0 auto;
}}
h1 {{
    font-size: {f['h1']};
    font-weight: 700;
    color: {t['h1_color']};
    margin: 28px 0 16px;
    line-height: 1.4;
}}
h2 {{
    font-size: {f['h2']};
    font-weight: 700;
    color: {t['h2_color']};
    margin: 32px 0 14px;
    padding-left: 12px;
    border-left: 4px solid {t['accent']};
}}
h3 {{
    font-size: {f['h3']};
    font-weight: 600;
    color: {t['h3_color']};
    margin: 20px 0 10px;
}}
p {{
    margin: 12px 0;
    text-align: justify;
}}
strong {{ color: {t['h2_color']}; font-weight: 600; }}
em {{ color: {t['accent']}; font-style: normal; }}
del {{ color: {t['secondary_color']}; text-decoration: line-through; }}
blockquote {{
    background: {t['quote_bg']};
    border-left: 3px solid {t['accent']};
    padding: 12px 16px;
    margin: 16px 0;
    border-radius: 0 6px 6px 0;
    color: {t['secondary_color']};
}}
blockquote p {{ margin: 0; }}
hr {{
    border: none;
    border-top: 1px dashed {t['border']};
    margin: 28px 0;
}}
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: {f['table']};
}}
th {{
    background: {t['h1_color']};
    color: #FFFFFF;
    padding: 10px 12px;
    text-align: left;
    font-weight: 600;
    white-space: nowrap;
}}
td {{
    padding: 10px 12px;
    border-bottom: 1px solid {t['border']};
    vertical-align: top;
}}
tr:nth-child(even) td {{
    background: {t['table_alt']};
}}
ul, ol {{
    margin: 12px 0 12px 24px;
}}
li {{
    margin: 6px 0;
    line-height: 1.7;
}}
code {{
    background: {t['code_bg']};
    color: {t['code_color']};
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'SF Mono', 'Menlo', 'Consolas', monospace;
    font-size: 0.9em;
}}
pre {{
    background: {t['pre_bg']};
    color: {t['pre_text']};
    padding: 16px;
    border-radius: 8px;
    overflow-x: auto;
    margin: 16px 0;
}}
pre code {{
    background: transparent;
    color: inherit;
    padding: 0;
    font-size: 13px;
    line-height: 1.6;
}}
a {{
    color: {t['accent']};
    text-decoration: none;
    border-bottom: 1px solid {t['accent']};
}}
.img-ref {{
    background: {t['tag_bg']};
    border: 1px dashed {t['border']};
    border-radius: 4px;
    padding: 4px 8px;
    font-size: 12px;
    color: {t['secondary_color']};
    display: inline-block;
    margin: 4px 0;
}}
.author-block {{
    background: {t['accent_bg']};
    border-radius: 8px;
    padding: 12px 16px;
    margin: 24px 0;
    font-size: 13px;
    color: {t['secondary_color']};
    border-left: 3px solid {t['accent']};
}}
"""

def build_html(md_text, theme_name, font_size_name, title=None):
    """生成完整 HTML 文档"""
    if title is None:
        title = extract_title(md_text)

    content = markdown_to_html(md_text)
    css = build_css(theme_name, font_size_name)

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape_html(title)}</title>
<style>
{css}
</style>
</head>
<body>
{content}
<div class="author-block">
<strong>作者：</strong>{{作者名}} · 保险其实不难<br>
<strong>编辑：</strong>AI（Claude）<br>
<em>本文基于公开监管文件整理，AI辅助写作</em>
</div>
</body>
</html>"""

def extract_title(md_text):
    """从 MD 文本提取标题"""
    for line in md_text.strip().split('\n'):
        line = line.strip()
        if line.startswith('# '):
            return line[2:].strip()
    return '无标题'

def clean_markdown(md_text):
    """清理 MD 中的作者/审校/编辑行"""
    patterns = [
        r'\*\*作者\*\*[：:]\s*.*?\n',
        r'\*\*审校\*\*[：:]\s*.*?\n',
        r'\*\*编辑\*\*[：:]\s*.*?\n',
        r'\*\*作者：[^\n]*\*?\s*\n',
        r'\*\*审校：[^\n]*\*?\s*\n',
        r'\*\*编辑：[^\n]*\*?\s*\n',
        r'\*\*作者：\*\*.*',
        r'作者：.*',
        r'编辑：.*',
        r'审校：.*',
    ]
    for p in patterns:
        md_text = re.sub(p, '', md_text, flags=re.IGNORECASE)
    return md_text

# ─────────────────────────────────────────────────────────────
# CLI 入口
# ─────────────────────────────────────────────────────────────

def main():
    all_themes = list(THEMES.keys()) + [f"{k}→{v}" for k, v in THEME_ALIASES.items()]

    parser = argparse.ArgumentParser(
        description='Markdown → 公众号 HTML 排版工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例：
  python md2wechat_formatter.py article.md -o preview.html
  python md2wechat_formatter.py article.md --theme deepblue --font-size large
  python md2wechat_formatter.py article.md --theme warm-story
  python md2wechat_formatter.py article.md --theme chinese

新主题（对齐 gzh-pipeline 多主题系统）：
  deepblue    — 深蓝商务（默认，理性专业）
  warm-story  — 暖橙故事（温暖亲和）
  tech-dark   — 科技暗色（现代冲击）
  minimal-fresh — 极简清爽（干净透气，细体+大留白）

旧主题（兼容）：
  01fish, chinese, apple, 保险其实不难（→deepblue）
        """
    )
    parser.add_argument('input', nargs='?', help='输入 Markdown 文件路径')
    parser.add_argument('-o', '--output', default=None, help='输出 HTML 文件路径（默认：输入文件同目录下 xxx_preview.html）')
    parser.add_argument('--theme', default='deepblue',
                        help='配色主题（默认：deepblue）')
    parser.add_argument('--font-size', default='medium',
                        choices=list(FONT_SIZES.keys()),
                        help='正文字号（默认：medium）')
    parser.add_argument('--list-themes', action='store_true',
                        help='列出所有可用主题')

    args = parser.parse_args()

    if args.list_themes:
        print("可用主题：")
        print("  deepblue    — 深蓝商务（默认，理性专业）")
        print("  warm-story  — 暖橙故事（温暖亲和）")
        print("  tech-dark   — 科技暗色（现代冲击）")
        print("  --- 旧主题（兼容） ---")
        print("  01fish      — 01鱼商务风")
        print("  chinese     — 中国风（深红+金色+米白）")
        print("  apple       — 极简优雅（黑+白+灰）")
        print("  保险其实不难 → deepblue（别名）")
        sys.exit(0)

    if not args.input:
        parser.print_help()
        print("\n错误：必须指定输入文件")
        sys.exit(1)

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"错误：文件不存在：{input_path}")
        sys.exit(1)

    # 解析主题（支持别名）
    resolved = resolve_theme(args.theme)
    if resolved not in THEMES:
        print(f"错误：未知主题 '{args.theme}'，使用 --list-themes 查看可用主题")
        sys.exit(1)

    md_text = input_path.read_text(encoding='utf-8')
    md_clean = clean_markdown(md_text)

    html = build_html(md_clean, resolved, args.font_size)

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_name(f'{input_path.stem}_preview.html')

    output_path.write_text(html, encoding='utf-8')

    print(f"排版完成：{output_path}")
    print(f"主题：{resolved} | 字号：{args.font_size}")
    print("浏览器打开后全选复制，粘贴到公众号编辑器")

if __name__ == '__main__':
    main()
