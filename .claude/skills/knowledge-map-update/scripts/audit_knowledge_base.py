#!/usr/bin/env python3
"""Read-only health audit for the active knowledge base.

The script deliberately separates actual failures from template placeholders,
pending relationship seeds, historical archives, and optional metadata gaps.
It never writes to the vault.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError:  # pragma: no cover - environment guidance
    print("缺少 PyYAML。请先运行：python -m pip install PyYAML", file=sys.stderr)
    raise SystemExit(2)


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", re.S)
WIKI_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
CODE_FENCE_RE = re.compile(r"```.*?```", re.S)

SKIP_PARTS = {".git", ".obsidian", ".playwright-cli", "node_modules", "tmp"}
RELATION_FIELDS = {
    "related_topics",
    "related_theme_maps",
    "related_projects",
    "related_cards",
    "related_cases",
    "supports",
    "contrasts",
    "examples",
    "applies_to",
    "derived_methods",
    "source_cards",
    "source_cases",
    "related_theme",
}
BASE_TAG_BY_TYPE = {
    "knowledge_card": "知识卡片",
    "theme_map": "主题地图",
    "case_law_entry": "判例",
    "topic_card": "选题",
    "content_piece": "内容成品",
    "content_draft": "内容成品",
}
PLACEHOLDER_TARGETS = {
    "卡片1",
    "卡片2",
    "卡片名",
    "具体判例或视图",
    "具体知识卡片",
    "未如实告知的边界判断",
}
OLD_ACTIVE_PATHS = {
    "02-Areas/主题聚合",
    "02-Areas/关系导航",
    "知识管理检索索引-试点",
    "01-Projects/知识库项目",
}


@dataclass
class Record:
    path: Path
    rel: str
    text: str
    frontmatter: dict[str, Any] | None
    yaml_error: str | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="只读审计知识库 YAML、标签、双链和索引")
    parser.add_argument(
        "root",
        nargs="?",
        default=str(Path(__file__).resolve().parents[4]),
        help="知识库根目录；默认从当前 Skill 位置推导",
    )
    parser.add_argument("--json", action="store_true", help="输出完整 JSON")
    parser.add_argument("--details", action="store_true", help="在人类可读输出中列出具体问题")
    return parser.parse_args()


def is_skipped(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return any(part in SKIP_PARTS for part in rel.parts)


def load_records(root: Path) -> list[Record]:
    records: list[Record] = []
    for path in sorted(root.rglob("*.md")):
        if is_skipped(path, root):
            continue
        rel = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            records.append(Record(path, rel, "", None, f"UTF-8 解码失败：{exc}"))
            continue

        match = FRONTMATTER_RE.match(text)
        if not match:
            records.append(Record(path, rel, text, None, "没有 YAML frontmatter"))
            continue
        try:
            frontmatter = yaml.safe_load(match.group(1)) or {}
            if not isinstance(frontmatter, dict):
                raise TypeError("frontmatter 不是键值映射")
            error = None
        except Exception as exc:  # noqa: BLE001 - report parser failure verbatim
            frontmatter = None
            error = str(exc).splitlines()[0]
        records.append(Record(path, rel, text, frontmatter, error))
    return records


def is_main_card(record: Record) -> bool:
    return (
        record.rel.startswith("02-Areas/知识卡片/")
        and record.path.name != "_template.md"
        and record.frontmatter is not None
        and record.frontmatter.get("type") == "knowledge_card"
    )


def is_main_theme(record: Record) -> bool:
    return (
        record.rel.startswith("02-Areas/主题中心/主题页/")
        and record.path.name != "_template.md"
        and record.frontmatter is not None
        and record.frontmatter.get("type") == "theme_map"
    )


def is_main_topic(record: Record) -> bool:
    return (
        record.rel.startswith("06-选题库/cards/")
        and record.frontmatter is not None
        and record.frontmatter.get("type") == "topic_card"
    )


def is_main_case(record: Record) -> bool:
    return (
        record.rel.startswith("02-Areas/判例库/按险种/")
        and record.frontmatter is not None
        and record.frontmatter.get("type") == "case_law_entry"
    )


def is_formal_yaml_scope(record: Record) -> bool:
    """Return whether a file belongs to the active, maintained knowledge layer.

    Inbox captures, external resources and archives may intentionally preserve
    source formatting. Operational projects, assets, human-facing standards,
    topic cards and the system entry files must keep valid minimum metadata.
    """
    if record.rel.startswith(("01-Projects/", "02-Areas/", "05-Skills/", "06-选题库/")):
        return True
    return record.rel in {
        "README.md",
        "知识库地图.md",
        "知识库变更日志.md",
        "00-Inbox/AI待确认.md",
    }


def required_base_tag(record: Record) -> str | None:
    """Return the base tag only for live assets, not packaged examples/copies."""
    file_type = str((record.frontmatter or {}).get("type") or "")
    if is_main_card(record) or is_main_theme(record) or is_main_topic(record) or is_main_case(record):
        return BASE_TAG_BY_TYPE.get(file_type)
    if record.rel.startswith("02-Areas/自媒体运营/") and file_type in {
        "content_piece",
        "content_draft",
    }:
        return BASE_TAG_BY_TYPE[file_type]
    return None


def is_active_link_scope(record: Record) -> bool:
    excluded = (
        ".claude/",
        ".agents/",
        ".codex/",
        "04-Archive/",
    )
    if record.rel.startswith(excluded):
        return False
    if "/课程包/" in record.rel or "知识库系统搭建实战课-完整课程包" in record.rel:
        return False
    return True


def is_active_old_path_scope(record: Record) -> bool:
    if record.rel == "知识库变更日志.md":
        return False
    if record.rel.startswith("03-Resources/系统资料/"):
        return False
    if record.frontmatter and record.frontmatter.get("type") == "project_handoff":
        return False
    return is_active_link_scope(record)


def scalar_text(value: Any) -> str:
    return "" if value is None else str(value).strip()


def relation_shape_is_valid(value: Any) -> bool:
    if value is None:
        return True
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def relation_names(value: Any) -> set[str]:
    if not value:
        return set()
    values = value if isinstance(value, list) else [value]
    output: set[str] = set()
    for item in values:
        if not isinstance(item, str):
            continue
        match = WIKI_LINK_RE.search(item)
        target = match.group(1) if match else item
        target = target.split("|", 1)[0].split("#", 1)[0]
        output.add(Path(target).stem)
    return output


def pending_seeds(root: Path) -> set[str]:
    index = root / "02-Areas/主题中心/README.md"
    if not index.exists():
        return set()
    text = index.read_text(encoding="utf-8")
    section = text.split("## 待补关系种子", 1)
    if len(section) != 2:
        return set()
    tail = section[1].split("\n## ", 1)[0]
    return set(re.findall(r"^- `([^`]+)`", tail, re.M))


def wiki_targets(text: str) -> Iterable[str]:
    # Code examples should not be treated as live links. Frontmatter remains.
    match = FRONTMATTER_RE.match(text)
    if match:
        frontmatter_text = match.group(0)
        body = CODE_FENCE_RE.sub("", text[match.end() :])
        scan_text = frontmatter_text + body
    else:
        scan_text = CODE_FENCE_RE.sub("", text)
    yield from WIKI_LINK_RE.findall(scan_text)


def normalize_target(raw: str) -> str:
    return raw.split("|", 1)[0].split("#", 1)[0].strip().replace("\\", "/")


def build_link_index(records: list[Record]) -> tuple[dict[str, str], dict[str, list[str]]]:
    by_path: dict[str, str] = {}
    by_stem: dict[str, list[str]] = defaultdict(list)
    for record in records:
        no_ext = record.rel[:-3] if record.rel.lower().endswith(".md") else record.rel
        by_path[no_ext] = record.rel
        by_stem[record.path.stem].append(record.rel)
    return by_path, by_stem


def resolve_link(
    record: Record,
    target: str,
    root: Path,
    by_path: dict[str, str],
    by_stem: dict[str, list[str]],
) -> tuple[str, list[str]]:
    no_ext = target[:-3] if target.lower().endswith(".md") else target
    if no_ext in by_path:
        return "resolved", [by_path[no_ext]]

    candidate = (record.path.parent / no_ext).resolve(strict=False)
    try:
        candidate_rel = candidate.relative_to(root).as_posix()
    except ValueError:
        candidate_rel = ""
    if candidate_rel in by_path:
        return "resolved", [by_path[candidate_rel]]

    matches = by_stem.get(Path(no_ext).name, [])
    if len(matches) == 1:
        return "resolved", matches
    if len(matches) > 1:
        return "ambiguous", matches
    return "unresolved", []


def audit(root: Path) -> dict[str, Any]:
    records = load_records(root)
    cards = [record for record in records if is_main_card(record)]
    themes = [record for record in records if is_main_theme(record)]
    topics = [record for record in records if is_main_topic(record)]
    cases = [record for record in records if is_main_case(record)]

    required_yaml_errors: list[dict[str, str]] = []
    relation_shape_errors: list[dict[str, Any]] = []
    tag_shape_errors: list[dict[str, Any]] = []
    missing_base_tags: list[dict[str, str]] = []
    tag_frequency: Counter[str] = Counter()

    formal = [record for record in records if is_formal_yaml_scope(record)]
    for record in formal:
        if record.yaml_error or record.frontmatter is None:
            required_yaml_errors.append({"path": record.rel, "error": record.yaml_error or "未知错误"})
            continue
        for key in ("title", "type"):
            if not scalar_text(record.frontmatter.get(key)):
                required_yaml_errors.append({"path": record.rel, "error": f"缺少 {key}"})

        tags_value = record.frontmatter.get("tags")
        tags: list[Any] = []
        if tags_value is None:
            pass
        elif isinstance(tags_value, list) and all(isinstance(tag, str) for tag in tags_value):
            tags = tags_value
            tag_frequency.update(tag.strip() for tag in tags)
        else:
            tag_shape_errors.append({"path": record.rel, "value": tags_value})
        required_tag = required_base_tag(record)
        if required_tag and required_tag not in tags:
            missing_base_tags.append({"path": record.rel, "required_tag": required_tag})

        for key, value in record.frontmatter.items():
            if key in RELATION_FIELDS and not relation_shape_is_valid(value):
                relation_shape_errors.append({"path": record.rel, "field": key, "value": value})
            if key == "links" and isinstance(value, dict):
                for subkey, subvalue in value.items():
                    if not relation_shape_is_valid(subvalue):
                        relation_shape_errors.append(
                            {"path": record.rel, "field": f"links.{subkey}", "value": subvalue}
                        )
            elif key == "links" and not relation_shape_is_valid(value):
                relation_shape_errors.append({"path": record.rel, "field": "links", "value": value})

    by_path, by_stem = build_link_index(records)
    seeds = pending_seeds(root)
    unresolved: list[dict[str, str]] = []
    ambiguous: list[dict[str, Any]] = []
    placeholders: list[dict[str, str]] = []
    seed_links: list[dict[str, str]] = []
    active_records = [record for record in records if is_active_link_scope(record)]

    for record in active_records:
        for raw in wiki_targets(record.text):
            target = normalize_target(raw)
            if not target or "{{" in target:
                continue
            stem = Path(target).name
            if record.path.name == "_template.md" or stem in PLACEHOLDER_TARGETS:
                placeholders.append({"path": record.rel, "target": raw})
                continue
            status, matches = resolve_link(record, target, root, by_path, by_stem)
            if status == "resolved":
                continue
            if stem in seeds:
                seed_links.append({"path": record.rel, "target": raw})
            elif status == "ambiguous":
                ambiguous.append({"path": record.rel, "target": raw, "matches": matches})
            else:
                unresolved.append({"path": record.rel, "target": raw})

    card_to_themes = {
        record.path.stem: relation_names(record.frontmatter.get("related_theme_maps"))
        for record in cards
        if record.frontmatter
    }
    theme_to_cards = {
        record.path.stem: relation_names(record.frontmatter.get("related_cards"))
        for record in themes
        if record.frontmatter
    }
    theme_inconsistencies: list[dict[str, str]] = []
    for card, related_themes in card_to_themes.items():
        for theme in related_themes:
            if card not in theme_to_cards.get(theme, set()):
                theme_inconsistencies.append({"side": "card_only", "card": card, "theme": theme})
    for theme, related_cards in theme_to_cards.items():
        for card in related_cards:
            if theme not in card_to_themes.get(card, set()):
                theme_inconsistencies.append({"side": "theme_only", "card": card, "theme": theme})

    old_refs: list[dict[str, Any]] = []
    replacement_chars: list[dict[str, Any]] = []
    for record in records:
        if not is_active_old_path_scope(record):
            continue
        for old_path in OLD_ACTIVE_PATHS:
            count = record.text.count(old_path)
            if count:
                old_refs.append({"path": record.rel, "old_path": old_path, "count": count})
        # Diagnostic documentation cites the replacement symbol inside inline
        # code. Exclude those literals while retaining actual damaged text.
        text_without_inline_code = re.sub(r"`[^`\n]*`", "", record.text)
        count = text_without_inline_code.count("\ufffd")
        if count:
            replacement_chars.append({"path": record.rel, "count": count})

    return {
        "root": str(root),
        "scope": {
            "formal_yaml_files": len(formal),
            "knowledge_cards": len(cards),
            "theme_maps": len(themes),
            "topic_cards": len(topics),
            "main_cases": len(cases),
            "active_link_files": len(active_records),
        },
        "yaml": {
            "required_errors": required_yaml_errors,
            "relation_shape_errors": relation_shape_errors,
        },
        "metadata": {
            "card_description_nonempty": sum(
                bool(scalar_text(record.frontmatter.get("description"))) for record in cards if record.frontmatter
            ),
            "card_source_nonempty": sum(
                bool(record.frontmatter.get("source")) for record in cards if record.frontmatter
            ),
            "topic_description_nonempty": sum(
                bool(scalar_text(record.frontmatter.get("description"))) for record in topics if record.frontmatter
            ),
            "topic_source_asset_nonempty": sum(
                bool(record.frontmatter.get("source_cards"))
                or bool(record.frontmatter.get("source_cases"))
                or bool(record.frontmatter.get("related_theme"))
                for record in topics
                if record.frontmatter
            ),
            "missing_base_tags": missing_base_tags,
            "tag_shape_errors": tag_shape_errors,
            "tag_vocabulary_size": len(tag_frequency),
            "top_tags": tag_frequency.most_common(30),
        },
        "links": {
            "unresolved": unresolved,
            "ambiguous": ambiguous,
            "pending_seeds": seed_links,
            "ignored_placeholders": placeholders,
            "theme_card_inconsistencies": theme_inconsistencies,
        },
        "structure": {
            "old_active_path_references": old_refs,
            "replacement_char_files": replacement_chars,
        },
    }


def print_human(report: dict[str, Any], details: bool) -> None:
    scope = report["scope"]
    yaml_report = report["yaml"]
    metadata = report["metadata"]
    links = report["links"]
    structure = report["structure"]

    print("知识库只读审计")
    print(
        "范围："
        f"{scope['knowledge_cards']} 张知识卡片，"
        f"{scope['theme_maps']} 张主题页，"
        f"{scope['topic_cards']} 张选题卡，"
        f"{scope['main_cases']} 条主判例"
    )
    print(
        f"YAML（{scope['formal_yaml_files']} 个正式运营文件）："
        f"{len(yaml_report['required_errors'])} 个必要字段/解析错误，"
        f"{len(yaml_report['relation_shape_errors'])} 个关系字段结构错误"
    )
    print(
        "卡片元数据："
        f"description {metadata['card_description_nonempty']}/{scope['knowledge_cards']}，"
        f"source {metadata['card_source_nonempty']}/{scope['knowledge_cards']}"
    )
    print(
        "标签："
        f"{len(metadata['tag_shape_errors'])} 个字段形态错误，"
        f"{len(metadata['missing_base_tags'])} 个基础类型标签缺失"
    )
    print(
        "链接："
        f"{len(links['unresolved'])} 个未解析，"
        f"{len(links['ambiguous'])} 个歧义，"
        f"{len(links['pending_seeds'])} 个待补种子，"
        f"{len(links['theme_card_inconsistencies'])} 个主题双向不一致"
    )
    print(
        "结构："
        f"{len(structure['old_active_path_references'])} 处旧路径引用，"
        f"{len(structure['replacement_char_files'])} 个文件包含替换字符"
    )

    if details:
        print("\n详细问题：")
        sections = {
            "必要 YAML": yaml_report["required_errors"],
            "关系字段结构": yaml_report["relation_shape_errors"],
            "标签字段结构": metadata["tag_shape_errors"],
            "基础类型标签": metadata["missing_base_tags"],
            "未解析链接": links["unresolved"],
            "歧义链接": links["ambiguous"],
            "待补关系种子": links["pending_seeds"],
            "主题双向不一致": links["theme_card_inconsistencies"],
            "旧路径": structure["old_active_path_references"],
            "替换字符": structure["replacement_char_files"],
        }
        for title, items in sections.items():
            print(f"\n[{title}] {len(items)}")
            for item in items:
                print(json.dumps(item, ensure_ascii=False))


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    if not (root / "README.md").exists():
        print(f"不是有效的知识库根目录：{root}", file=sys.stderr)
        return 2
    report = audit(root)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_human(report, args.details)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
