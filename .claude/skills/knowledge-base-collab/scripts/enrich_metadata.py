#!/usr/bin/env python3
"""Conservatively enrich existing card/topic metadata from their own bodies.

Default mode is a dry run. The script only fills missing descriptions, copies an
already documented source into YAML, repairs unquoted YAML wiki-link list
items, adds the asset type's base tag, and updates the modified date. It does
not infer new relationships or invent sources.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", re.S)
WIKI_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
SOURCE_SECTION_RE = re.compile(
    r"^##+\s*(?:来源|证据或来源|参考资料|资料来源|出处)[^\n]*\n(.*?)(?=^##+\s|\Z)", re.M | re.S
)
DATE = "2026-07-17"

CUSTOM_CARD_DESCRIPTIONS = {
    "个人表达DNA模板": "用于固定个人内容表达中的受众感受、语言边界、价值观和视觉偏好。",
    "保险合同纠纷裁判精要与规则适用_核心观点摘要": "提炼《保险合同纠纷裁判精要与规则适用》中关于告知义务、免责条款和裁判规则的核心观点。",
    "弃权与禁止反言": "区分弃权与禁止反言在保险理赔中的含义、适用条件和举证重点。",
    "叙事结构工具箱": "用注意力管理视角选择适合不同内容长度和传播目标的叙事结构。",
    "故事最小单元": "用人物、目标、障碍、行动、结果、认知变化和普遍意义构成可复用的故事最小单元。",
    "投放流量逻辑": "说明不同内容平台的流量来源、投放策略和自然流量与付费流量的配合方式。",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="从现有正文保守补齐卡片与选题元数据")
    parser.add_argument(
        "root", nargs="?", default=str(Path(__file__).resolve().parents[4]), help="知识库根目录"
    )
    parser.add_argument("--apply", action="store_true", help="实际写入；默认只干跑")
    return parser.parse_args()


def clean_markdown(text: str) -> str:
    text = re.sub(r"^>\s*", "", text)
    text = re.sub(r"^\*\*[^*]{1,20}\*\*[：:]?\s*", "", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"[*_`#]", "", text)
    return re.sub(r"\s+", " ", text).strip(" -")


def card_description(body: str, title: str, stem: str) -> str:
    if stem in CUSTOM_CARD_DESCRIPTIONS:
        return CUSTOM_CARD_DESCRIPTIONS[stem]
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith(("#", "---", "|", "- [", "- ", "* ", "+ ")):
            continue
        if re.match(r"^\d+[.)]\s", line):
            continue
        line = clean_markdown(line)
        if len(line) < 12:
            continue
        sentence = re.match(r"^(.{12,130}?[。！？])(?:\s|$)", line)
        if sentence:
            line = sentence.group(1)
        if len(line) > 130:
            cut = max(line.rfind(mark, 0, 130) for mark in "；，。")
            line = line[: cut + 1] if cut >= 30 else line[:129] + "…"
        return line
    return f"说明“{title}”的核心判断、使用场景和适用边界。"


def topic_description(body: str, title: str, target_reader: str) -> str:
    match = re.search(r"^- 核心问题[：:]\s*(.+)$", body, re.M)
    question = clean_markdown(match.group(1)) if match else title
    if target_reader:
        return f"面向{target_reader}，回答“{question}”这一内容问题。"
    return f"围绕“{question}”形成的正式内容选题。"


def quote_yaml_wiki_lists(frontmatter_text: str) -> str:
    return re.sub(
        r'^(\s*-\s*)(\[\[[^\r\n]+\]\])\s*$',
        lambda match: f'{match.group(1)}{json.dumps(match.group(2), ensure_ascii=False)}',
        frontmatter_text,
        flags=re.M,
    )


def replace_or_insert_scalar(frontmatter_text: str, key: str, value: str, after: str) -> str:
    rendered = json.dumps(value, ensure_ascii=False)
    pattern = re.compile(rf"^{re.escape(key)}\s*:\s*.*$", re.M)
    if pattern.search(frontmatter_text):
        return pattern.sub(f"{key}: {rendered}", frontmatter_text, count=1)
    after_pattern = re.compile(rf"^({re.escape(after)}\s*:\s*.*)$", re.M)
    if after_pattern.search(frontmatter_text):
        return after_pattern.sub(rf"\1\n{key}: {rendered}", frontmatter_text, count=1)
    return frontmatter_text.rstrip() + f"\n{key}: {rendered}\n"


def update_date(frontmatter_text: str) -> str:
    if re.search(r"^updated\s*:", frontmatter_text, re.M):
        return re.sub(r"^updated\s*:.*$", f"updated: {DATE}", frontmatter_text, count=1, flags=re.M)
    return frontmatter_text.rstrip() + f"\nupdated: {DATE}\n"


def ensure_base_tag(frontmatter_text: str, tags: object, required_tag: str) -> str:
    values = list(tags) if isinstance(tags, list) else []
    if required_tag in values:
        return frontmatter_text
    values.append(required_tag)
    rendered = json.dumps(values, ensure_ascii=False)
    pattern = re.compile(r"^tags\s*:.*?(?=^[A-Za-z_][\w-]*\s*:|\Z)", re.M | re.S)
    if pattern.search(frontmatter_text):
        return pattern.sub(f"tags: {rendered}\n", frontmatter_text, count=1)
    after_pattern = re.compile(r"^(status\s*:\s*.*)$", re.M)
    if after_pattern.search(frontmatter_text):
        return after_pattern.sub(rf"\1\ntags: {rendered}", frontmatter_text, count=1)
    return frontmatter_text.rstrip() + f"\ntags: {rendered}\n"


def documented_source(body: str, root: Path, title: str, stem: str) -> str | None:
    section = SOURCE_SECTION_RE.search(body)
    if section:
        for raw_line in section.group(1).splitlines():
            line = clean_markdown(raw_line)
            if not line:
                continue
            line = re.sub(r"^源文件[：:]\s*", "", line)
            line = line.replace("02-Areas/保险理赔/", "03-Resources/保险理赔/")
            line = line.replace("02-Areas/保险/", "03-Resources/保险/")
            line = re.sub(r"（扫描件，需OCR）$", "", line)
            if "wangyongtao-ip SKILL.md" in line:
                line = line.replace("wangyongtao-ip SKILL.md", ".claude/skills/wangyongtao-ip/SKILL.md")
            return line

    # A small number of cards have an exact source asset but no source section.
    normalized = re.sub(r"[-_—（）()\s]+", "", title).lower()
    normalized = re.sub(r"(素材|研究报告|核心观点摘要)$", "", normalized)
    matches: list[str] = []
    for base in ("03-Resources", "04-Archive"):
        for candidate in (root / base).rglob("*.md"):
            candidate_name = re.sub(r"[-_—（）()\s]+", "", candidate.stem).lower()
            candidate_name = re.sub(r"(素材|研究报告|核心观点摘要)$", "", candidate_name)
            if normalized and normalized == candidate_name:
                matches.append(candidate.relative_to(root).as_posix())
    if len(matches) == 1:
        return matches[0]
    return None


def repair_topic_links_field(frontmatter_text: str) -> str:
    match = re.search(r"^links\s*:\s*(.+)$", frontmatter_text, re.M)
    if not match or match.group(1).strip().startswith("[") and match.group(1).strip() == "[]":
        return frontmatter_text
    links = [f"[[{target}]]" for target in WIKI_LINK_RE.findall(match.group(1))]
    if len(links) <= 1:
        return frontmatter_text
    replacement = "links:\n" + "\n".join(
        f"  - {json.dumps(link, ensure_ascii=False)}" for link in links
    )
    return frontmatter_text[: match.start()] + replacement + frontmatter_text[match.end() :]


def process_file(path: Path, root: Path, apply: bool) -> dict[str, object] | None:
    original = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(original)
    if not match:
        return None
    frontmatter = yaml.safe_load(match.group(1)) or {}
    file_type = frontmatter.get("type")
    if file_type not in {"knowledge_card", "topic_card"}:
        return None
    if path.name == "_template.md":
        return None

    body = original[match.end() :]
    yaml_text = match.group(1)
    changes: list[str] = []

    quoted = quote_yaml_wiki_lists(yaml_text)
    if quoted != yaml_text:
        yaml_text = quoted
        changes.append("修复 YAML 双链列表")

    if file_type == "topic_card":
        repaired = repair_topic_links_field(yaml_text)
        if repaired != yaml_text:
            yaml_text = repaired
            changes.append("拆分 links 字符串")

    required_tag = "知识卡片" if file_type == "knowledge_card" else "选题"
    tagged = ensure_base_tag(yaml_text, frontmatter.get("tags"), required_tag)
    if tagged != yaml_text:
        yaml_text = tagged
        changes.append("补基础类型标签")

    if not str(frontmatter.get("description") or "").strip():
        if file_type == "knowledge_card":
            description = card_description(body, str(frontmatter.get("title") or path.stem), path.stem)
        else:
            description = topic_description(
                body,
                str(frontmatter.get("title") or path.stem),
                str(frontmatter.get("target_reader") or ""),
            )
        yaml_text = replace_or_insert_scalar(yaml_text, "description", description, "type")
        changes.append("补 description")

    if file_type == "knowledge_card" and not frontmatter.get("source"):
        source = documented_source(body, root, str(frontmatter.get("title") or path.stem), path.stem)
        if source:
            yaml_text = replace_or_insert_scalar(yaml_text, "source", source, "description")
            changes.append("回填已有来源")

    if not changes:
        return None
    yaml_text = update_date(yaml_text)
    updated = f"---\n{yaml_text.rstrip()}\n---\n\n{body.lstrip()}"
    if apply:
        path.write_text(updated, encoding="utf-8", newline="")
    return {"path": path.relative_to(root).as_posix(), "changes": changes}


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    candidates = list((root / "02-Areas/知识卡片").rglob("*.md"))
    candidates += list((root / "06-选题库/cards").rglob("*.md"))
    results = [result for path in sorted(candidates) if (result := process_file(path, root, args.apply))]
    counts: dict[str, int] = {}
    for result in results:
        for change in result["changes"]:
            counts[change] = counts.get(change, 0) + 1
    print(json.dumps({"mode": "apply" if args.apply else "dry-run", "files": len(results), "changes": counts}, ensure_ascii=False, indent=2))
    if not args.apply:
        for result in results:
            print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
