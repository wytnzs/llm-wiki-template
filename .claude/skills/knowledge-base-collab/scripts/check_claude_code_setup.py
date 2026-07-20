#!/usr/bin/env python3
"""只读检查 Claude Code 是否已完整接入当前知识库。"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]

REQUIRED_PATHS = {
    "知识库总入口": "README.md",
    "Claude Code 总控": ".claude/CLAUDE.md",
    "AI 待确认": "00-Inbox/AI待确认.md",
    "主题中心": "02-Areas/主题中心/README.md",
    "定期维护指令": "05-Skills/知识库定期维护指令.md",
    "关系规范": "05-Skills/知识关系与标签规范.md",
    "关系质量标准": "05-Skills/知识关系质量评估标准.md",
    "知识库地图": "知识库地图.md",
    "知识库变更日志": "知识库变更日志.md",
    "只读审计器": ".claude/skills/knowledge-map-update/scripts/audit_knowledge_base.py",
    "元数据干跑工具": ".claude/skills/knowledge-base-collab/scripts/enrich_metadata.py",
}

REQUIRED_SKILL_ROUTES = {
    "知识库总控": "knowledge-base-collab",
    "Inbox 处理": "inbox-processing",
    "主题维护": "theme-map-maintenance",
    "知识库体检": "knowledge-map-update",
    "判例维护": "case-law-entry",
    "候选选题": "topic-selection",
    "选题入库": "topic-library",
    "内容生产交接": "content-briefing",
    "反馈回写": "feedback-writeback",
}

CLAUDE_MARKERS = {
    "README 入口": "README.md",
    "工作区保护": "工作区已有修改",
    "定期维护": "知识库定期维护指令.md",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def parse_skill_frontmatter(path: Path) -> tuple[str | None, str | None, str | None]:
    try:
        text = read_text(path)
    except (OSError, UnicodeError) as exc:
        return None, None, f"无法以 UTF-8 读取：{exc}"

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, None, "缺少 YAML 起始分隔线"

    try:
        end = next(index for index, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return None, None, "缺少 YAML 结束分隔线"

    values: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")

    name = values.get("name")
    description = values.get("description")
    if not name or not description:
        return name, description, "必须同时包含非空 name 和 description"
    return name, description, None


def run_checks() -> dict[str, object]:
    passed: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []

    for label, relative in REQUIRED_PATHS.items():
        path = ROOT / relative
        if path.is_file():
            passed.append(f"{label}: {relative}")
        else:
            errors.append(f"缺少{label}: {relative}")

    skills_root = ROOT / ".claude" / "skills"
    discovered: set[str] = set()
    if not skills_root.is_dir():
        errors.append("缺少 Claude Code Skill 目录: .claude/skills")
    else:
        for directory in sorted(path for path in skills_root.iterdir() if path.is_dir()):
            skill_file = directory / "SKILL.md"
            if not skill_file.is_file():
                continue
            discovered.add(directory.name)
            name, _description, problem = parse_skill_frontmatter(skill_file)
            if problem:
                errors.append(f"Skill {directory.name}: {problem}")
            elif name != directory.name:
                errors.append(
                    f"Skill 目录与 name 不一致: {directory.name} != {name}"
                )
            else:
                passed.append(f"Skill 有效: {directory.name}")

        for label, skill_name in REQUIRED_SKILL_ROUTES.items():
            if skill_name not in discovered:
                errors.append(f"缺少总控路由 Skill（{label}）: {skill_name}")

    claude_path = ROOT / ".claude" / "CLAUDE.md"
    if claude_path.is_file():
        try:
            claude_text = read_text(claude_path)
            for label, marker in CLAUDE_MARKERS.items():
                if marker in claude_text:
                    passed.append(f"总控路由已声明: {label}")
                else:
                    errors.append(f"Claude Code 总控缺少路由: {label}")
            for label, skill_name in REQUIRED_SKILL_ROUTES.items():
                if skill_name in claude_text:
                    passed.append(f"总控 Skill 路由已声明: {label}")
                else:
                    errors.append(
                        f"Claude Code 总控缺少 Skill 路由（{label}）: {skill_name}"
                    )
        except (OSError, UnicodeError) as exc:
            errors.append(f"无法读取 .claude/CLAUDE.md: {exc}")

    agents_skills = ROOT / ".agents" / "skills"
    if agents_skills.exists():
        try:
            if agents_skills.resolve() == skills_root.resolve():
                passed.append("Codex 兼容入口与 Claude Code Skill 共用同一源目录")
            else:
                warnings.append(".agents/skills 未指向 .claude/skills，可能形成双份维护")
        except OSError as exc:
            warnings.append(f"无法核对 .agents/skills 兼容连接: {exc}")
    else:
        warnings.append("未配置 .agents/skills 兼容入口；不影响 Claude Code 使用")

    claude_executable = shutil.which("claude")
    if claude_executable:
        passed.append("当前终端可发现 Claude Code CLI")
    else:
        warnings.append(
            "当前终端未发现 claude 命令；项目配置有效，但无法在本终端做实际启动测试"
        )

    return {
        "root": str(ROOT),
        "ok": not errors,
        "skill_count": len(discovered),
        "passed": passed,
        "warnings": warnings,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    args = parser.parse_args()

    result = run_checks()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        status = "通过" if result["ok"] else "失败"
        print(f"Claude Code 接管自检：{status}")
        print(f"已发现 Skill：{result['skill_count']} 个")
        for item in result["warnings"]:
            print(f"警告：{item}")
        for item in result["errors"]:
            print(f"错误：{item}")
        print(
            f"检查项：{len(result['passed'])} 通过 / "
            f"{len(result['warnings'])} 警告 / {len(result['errors'])} 错误"
        )

    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
