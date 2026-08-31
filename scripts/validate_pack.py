#!/usr/bin/env python3
"""Validate repository, plugin, skill, and catalog integrity without dependencies."""

from __future__ import annotations

import csv
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "knowledge-pack"
SKILLS = PLUGIN / "skills"
CLAUDE = ROOT / "knowledge" / "claude"
CODEX = ROOT / "knowledge" / "codex"
CARDS = CLAUDE / "cards"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
RESERVED_SKILL_WORDS = {"anthropic", "claude"}
# A source audit older than this is treated as a failure, not a warning: the
# whole point of the weekly checker is that nobody notices silent drift.
MAX_VERIFIED_AGE_DAYS = 45
# scripts/apply_catalog_updates.py writes this into the columns that need a
# person. Failing on it is what stops a generated row from reaching main.
TODO_MARKER = "TODO:"
BRAND_NAME = "Agent Fieldbook"
MARKETPLACE_NAME = "agent-fieldbook"

MIRRORS = {
    ROOT / "assets" / "logo.png": [PLUGIN / "assets" / "logo.png"],
    ROOT / "LICENSE": [PLUGIN / "LICENSE"],
    ROOT / "PRIVACY.md": [PLUGIN / "PRIVACY.md"],
    ROOT / "TERMS.md": [PLUGIN / "TERMS.md"],
    ROOT / "SUPPORT.md": [PLUGIN / "SUPPORT.md"],
    ROOT / "SECURITY.md": [PLUGIN / "SECURITY.md"],
    ROOT / "knowledge-base.md": [
        SKILLS / "navigate" / "references" / "knowledge-base.md"
    ],
    CLAUDE / "knowledge-base.md": [
        SKILLS / "cowork" / "references" / "knowledge-base.md"
    ],
    CLAUDE / "sources.md": [
        SKILLS / "cowork" / "references" / "sources.md"
    ],
    CODEX / "knowledge-base.md": [
        SKILLS / "codex" / "references" / "knowledge-base.md"
    ],
    CODEX / "sources.md": [
        SKILLS / "codex" / "references" / "sources.md"
    ],
    CLAUDE / "courses.csv": [
        SKILLS / "learn" / "references" / "claude-courses.csv",
    ],
    CLAUDE / "tutorials.csv": [
        SKILLS / "learn" / "references" / "claude-tutorials.csv",
    ],
    CODEX / "learning-resources.csv": [
        SKILLS / "learn" / "references" / "codex-learning-resources.csv",
    ],
    ROOT / "knowledge-card-prompt.md": [
        SKILLS / "knowledge-card" / "references" / "knowledge-card-prompt.md"
    ],
    ROOT / "knowledge-card.schema.json": [
        SKILLS / "knowledge-card" / "references" / "knowledge-card.schema.json"
    ],
    CARDS / "ai-fluency-4d-corso.md": [
        SKILLS / "prompt" / "references" / "ai-fluency-4d-corso.md",
        SKILLS / "skill" / "references" / "ai-fluency-4d-corso.md",
    ],
    CARDS / "ai-fluency-curriculum.md": [
        SKILLS / "prompt" / "references" / "ai-fluency-curriculum.md",
    ],
    CARDS / "regole-distillate.md": [
        SKILLS / "prompt" / "references" / "regole-distillate.md",
        SKILLS / "verify" / "references" / "regole-distillate.md",
    ],
    CARDS / "ai-literacy.md": [
        SKILLS / "verify" / "references" / "ai-literacy.md",
    ],
    CARDS / "claude-code-estensioni.md": [
        SKILLS / "skill" / "references" / "claude-code-estensioni.md",
        SKILLS / "cowork" / "references" / "claude-code-estensioni.md",
    ],
    CLAUDE / "claude-code-subagents.md": [
        SKILLS / "subagent" / "references" / "claude-code-subagents.md",
    ],
    CLAUDE / "claude-code-plugins.md": [
        SKILLS / "plugin" / "references" / "claude-code-plugins.md",
    ],
    CARDS / "managed-agents.md": [
        SKILLS / "subagent" / "references" / "managed-agents.md",
    ],
    CARDS / "plugin-building.md": [
        SKILLS / "cowork" / "references" / "plugin-building.md",
    ],
    CARDS / "cowork.md": [
        SKILLS / "cowork" / "references" / "cowork.md",
    ],
    CARDS / "desktop-app.md": [
        SKILLS / "cowork" / "references" / "desktop-app.md",
    ],
    CODEX / "prompting.md": [
        SKILLS / "prompt" / "references" / "codex-prompting.md",
    ],
    CODEX / "subagents.md": [
        SKILLS / "subagent" / "references" / "codex-subagents.md",
    ],
    CODEX / "skills.md": [
        SKILLS / "skill" / "references" / "codex-skills.md",
    ],
    CODEX / "plugins.md": [
        SKILLS / "plugin" / "references" / "codex-plugins.md",
    ],
}


def load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing required file: {path.relative_to(ROOT)}")
        return {}
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(payload, dict):
        errors.append(f"expected a JSON object: {path.relative_to(ROOT)}")
        return {}
    return payload


def read_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(f"missing required file: {path.relative_to(ROOT)}")
        return {}
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        errors.append(f"missing YAML frontmatter: {path.relative_to(ROOT)}")
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        errors.append(f"unclosed YAML frontmatter: {path.relative_to(ROOT)}")
        return {}
    result: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"\'')
    return result


def read_card_frontmatter(
    path: Path, errors: list[str]
) -> tuple[dict[str, str], dict[str, list[str]]]:
    """Parse the constrained YAML subset used by knowledge-card metadata."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        errors.append(f"missing knowledge-card frontmatter: {path.relative_to(ROOT)}")
        return {}, {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        errors.append(f"unclosed knowledge-card frontmatter: {path.relative_to(ROOT)}")
        return {}, {}

    scalars: dict[str, str] = {}
    sequences: dict[str, list[str]] = {}
    current_key: str | None = None
    for raw in lines[1:end]:
        if raw.startswith("  - ") and current_key:
            sequences.setdefault(current_key, []).append(
                raw[4:].strip().strip('"\'')
            )
            continue
        if raw.startswith(" ") or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        current_key = key.strip()
        scalars[current_key] = value.strip().strip('"\'')
    return scalars, sequences


def validate_card_frontmatter(path: Path, errors: list[str]) -> None:
    scalars, sequences = read_card_frontmatter(path, errors)
    if not scalars:
        return

    schema = load_json(ROOT / "knowledge-card.schema.json", errors)
    required = set(schema.get("required", []))
    properties = set(schema.get("properties", {}))
    keys = set(scalars)
    missing = sorted(required - keys)
    unknown = sorted(keys - properties)
    if missing:
        errors.append(
            f"{path.relative_to(ROOT)} missing frontmatter fields: {', '.join(missing)}"
        )
    if unknown:
        errors.append(
            f"{path.relative_to(ROOT)} has unsupported frontmatter fields: {', '.join(unknown)}"
        )

    if not scalars.get("source_url", "").startswith("https://"):
        errors.append(f"{path.relative_to(ROOT)} source_url must start with https://")
    if scalars.get("source_type") not in {
        "course",
        "tutorial",
        "documentation",
        "article",
        "video",
        "workshop",
        "transcript",
        "other",
    }:
        errors.append(f"{path.relative_to(ROOT)} has invalid source_type")
    if scalars.get("status") not in {"current", "needs-verification", "archived"}:
        errors.append(f"{path.relative_to(ROOT)} has invalid status")
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", scalars.get("verified_on", "")) is None:
        errors.append(f"{path.relative_to(ROOT)} has invalid verified_on date")
    source_date = scalars.get("source_date", "")
    if source_date != "null" and re.fullmatch(r"\d{4}-\d{2}-\d{2}", source_date) is None:
        errors.append(f"{path.relative_to(ROOT)} has invalid source_date")
    if not sequences.get("source_products"):
        errors.append(f"{path.relative_to(ROOT)} requires source_products")
    if not sequences.get("tags"):
        errors.append(f"{path.relative_to(ROOT)} requires tags")
    if not scalars.get("license_note"):
        errors.append(f"{path.relative_to(ROOT)} requires license_note")
    if "time_sensitive" in scalars and scalars["time_sensitive"] not in {
        "true",
        "false",
    }:
        errors.append(f"{path.relative_to(ROOT)} time_sensitive must be true or false")


def validate_manifest_freshness(manifest: dict[str, Any], errors: list[str]) -> None:
    """Fail when the recorded source audit has gone stale."""
    verified_on = manifest.get("verified_on", "")
    if not isinstance(verified_on, str) or re.fullmatch(r"\d{4}-\d{2}-\d{2}", verified_on) is None:
        errors.append("manifest.json verified_on must be an ISO date (YYYY-MM-DD)")
        return
    age = (date.today() - date.fromisoformat(verified_on)).days
    if age > MAX_VERIFIED_AGE_DAYS:
        errors.append(
            f"manifest.json verified_on is {age} days old (limit {MAX_VERIFIED_AGE_DAYS}); "
            "re-run python3 check_official_sources.py, fix what it reports, "
            "then update verified_on"
        )


def validate_rendered_catalog(errors: list[str]) -> None:
    """Fail when the knowledge-base tables no longer match the catalog CSVs."""
    import render_catalog

    try:
        if render_catalog.render() != render_catalog.KNOWLEDGE_BASE.read_text(encoding="utf-8"):
            errors.append(
                "knowledge-base.md catalog tables are stale "
                "(run python3 scripts/render_catalog.py)"
            )
    except SystemExit as exc:
        errors.append(f"knowledge-base.md catalog markers are broken: {exc}")


def validate_catalog(
    path: Path, expected_count: int, errors: list[str]
) -> None:
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except FileNotFoundError:
        errors.append(f"missing catalog: {path.relative_to(ROOT)}")
        return
    if len(rows) != expected_count:
        errors.append(
            f"{path.name} has {len(rows)} rows; manifest declares {expected_count}"
        )
    urls: list[str] = []
    for line, row in enumerate(rows, start=2):
        url = (row.get("URL") or "").strip()
        if not url.startswith("https://"):
            errors.append(f"{path.name}:{line} URL must start with https://")
        urls.append(url.rstrip("/").lower())
    duplicates = sorted({url for url in urls if url and urls.count(url) > 1})
    if duplicates:
        errors.append(f"{path.name} contains duplicate URLs: {', '.join(duplicates)}")
    for line, row in enumerate(rows, start=2):
        pending = sorted(k for k, v in row.items() if v and TODO_MARKER in v)
        if pending:
            errors.append(
                f"{path.name}:{line} still has placeholder values in "
                f"{', '.join(pending)}; a generated row needs its curated "
                "columns written before it can be merged"
            )


def validate() -> list[str]:
    errors: list[str] = []

    for relative in (
        "README.md",
        "CITATION.cff",
        "assets/logo.svg",
        "assets/logo.png",
        "assets/social-preview.svg",
        "assets/social-preview.png",
        "LICENSE",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "PRIVACY.md",
        "TERMS.md",
        "SUPPORT.md",
        "manifest.json",
        "submission/review-test-cases.md",
        "submission/release-notes.md",
        "submission/listing.md",
        "submission/launch-copy.md",
        "submission/launch-checklist.md",
        ".claude-plugin/marketplace.json",
        ".agents/plugins/marketplace.json",
        "plugins/knowledge-pack/.claude-plugin/plugin.json",
        "plugins/knowledge-pack/.codex-plugin/plugin.json",
        "plugins/knowledge-pack/README.md",
    ):
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    manifest = load_json(ROOT / "manifest.json", errors)
    version = manifest.get("version")
    if not isinstance(version, str) or SEMVER_RE.fullmatch(version) is None:
        errors.append("manifest.json version must be strict semver")

    claude_plugin = load_json(PLUGIN / ".claude-plugin" / "plugin.json", errors)
    codex_plugin = load_json(PLUGIN / ".codex-plugin" / "plugin.json", errors)
    for label, plugin in (("Claude", claude_plugin), ("Codex", codex_plugin)):
        if plugin.get("name") != "knowledge-pack":
            errors.append(f"{label} plugin name must be knowledge-pack")
        if plugin.get("version") != version:
            errors.append(f"{label} plugin version does not match manifest.json")

    claude_market = load_json(ROOT / ".claude-plugin" / "marketplace.json", errors)
    codex_market = load_json(ROOT / ".agents" / "plugins" / "marketplace.json", errors)
    if manifest.get("name") != BRAND_NAME:
        errors.append(f"manifest.json name must be {BRAND_NAME}")
    if claude_plugin.get("displayName") != BRAND_NAME:
        errors.append(f"Claude plugin displayName must be {BRAND_NAME}")
    codex_interface = codex_plugin.get("interface")
    if not isinstance(codex_interface, dict):
        errors.append("Codex plugin interface must be an object")
    else:
        if codex_interface.get("displayName") != BRAND_NAME:
            errors.append(f"Codex plugin displayName must be {BRAND_NAME}")
        prompts = codex_interface.get("defaultPrompt")
        if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3:
            errors.append("Codex plugin must provide 1-3 starter prompts")
    if claude_market.get("name") != MARKETPLACE_NAME:
        errors.append(f"Claude marketplace name must be {MARKETPLACE_NAME}")
    if codex_market.get("name") != MARKETPLACE_NAME:
        errors.append(f"Codex marketplace name must be {MARKETPLACE_NAME}")
    codex_market_interface = codex_market.get("interface")
    if not isinstance(codex_market_interface, dict) or codex_market_interface.get(
        "displayName"
    ) != BRAND_NAME:
        errors.append(f"Codex marketplace displayName must be {BRAND_NAME}")
    claude_entries = claude_market.get("plugins")
    if not isinstance(claude_entries, list) or len(claude_entries) != 1:
        errors.append("Claude marketplace must contain exactly one plugin")
    else:
        entry = claude_entries[0]
        if not isinstance(entry, dict) or entry.get("name") != "knowledge-pack":
            errors.append("Claude marketplace plugin name must be knowledge-pack")
        elif entry.get("source") != "./plugins/knowledge-pack":
            errors.append("Claude marketplace source must be ./plugins/knowledge-pack")
        elif entry.get("version") != version:
            errors.append("Claude marketplace version does not match manifest.json")
    codex_entries = codex_market.get("plugins")
    if not isinstance(codex_entries, list) or len(codex_entries) != 1:
        errors.append("Codex marketplace must contain exactly one plugin")
    else:
        entry = codex_entries[0]
        source = entry.get("source") if isinstance(entry, dict) else None
        if not isinstance(entry, dict) or entry.get("name") != "knowledge-pack":
            errors.append("Codex marketplace plugin name must be knowledge-pack")
        elif source != {"source": "local", "path": "./plugins/knowledge-pack"}:
            errors.append("Codex marketplace source must point to ./plugins/knowledge-pack")

    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir()) if SKILLS.is_dir() else []
    if len(skill_dirs) != manifest.get("skills"):
        errors.append(
            f"skills directory has {len(skill_dirs)} entries; "
            f"manifest declares {manifest.get('skills')}"
        )
    for skill_dir in skill_dirs:
        metadata = read_frontmatter(skill_dir / "SKILL.md", errors)
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if name != skill_dir.name:
            errors.append(f"skill folder/name mismatch: {skill_dir.name} != {name}")
        if NAME_RE.fullmatch(name) is None:
            errors.append(f"invalid skill name: {name or skill_dir.name}")
        if RESERVED_SKILL_WORDS.intersection(name.split("-")):
            errors.append(f"skill name contains a reserved word: {name}")
        if not description or len(description) > 1024:
            errors.append(f"skill description must be 1-1024 characters: {name}")
        line_count = len((skill_dir / "SKILL.md").read_text(encoding="utf-8").splitlines())
        if line_count > 500:
            errors.append(f"skill exceeds 500 lines: {name}")
        agent_yaml = skill_dir / "agents" / "openai.yaml"
        if not agent_yaml.is_file():
            errors.append(f"missing Codex UI metadata: {agent_yaml.relative_to(ROOT)}")
        elif f"${name}" not in agent_yaml.read_text(encoding="utf-8"):
            errors.append(f"Codex default prompt must mention ${name}")

    for source, destinations in MIRRORS.items():
        if not source.is_file():
            errors.append(f"missing mirror source: {source.relative_to(ROOT)}")
            continue
        source_bytes = source.read_bytes()
        for destination in destinations:
            if not destination.is_file():
                errors.append(f"missing mirrored file: {destination.relative_to(ROOT)}")
            elif destination.read_bytes() != source_bytes:
                errors.append(
                    f"mirrored file is stale: {destination.relative_to(ROOT)} "
                    f"(run python3 scripts/sync_pack.py)"
                )

    validate_manifest_freshness(manifest, errors)
    validate_rendered_catalog(errors)

    validate_catalog(
        CLAUDE / "courses.csv",
        int(manifest.get("claude_courses", -1)),
        errors,
    )
    validate_catalog(
        CLAUDE / "tutorials.csv",
        int(manifest.get("claude_tutorials", -1)),
        errors,
    )
    validate_catalog(
        CODEX / "learning-resources.csv",
        int(manifest.get("codex_learning_resources", -1)),
        errors,
    )

    cards = list(CARDS.glob("*.md")) if CARDS.is_dir() else []
    cards = [path for path in cards if path.name != "pending-video-ingestion.md"]
    if len(cards) != manifest.get("knowledge_cards"):
        errors.append(
            f"found {len(cards)} knowledge cards; "
            f"manifest declares {manifest.get('knowledge_cards')}"
        )
    for card in cards:
        validate_card_frontmatter(card, errors)

    review_cases = ROOT / "submission" / "review-test-cases.md"
    if review_cases.is_file():
        review_text = review_cases.read_text(encoding="utf-8")
        positive_section, _, negative_section = review_text.partition(
            "## Negative test cases"
        )
        positive = re.findall(
            r"^### [1-5]\. ",
            positive_section,
            flags=re.MULTILINE,
        )
        negative = re.findall(
            r"^### [1-3]\. ",
            negative_section,
            flags=re.MULTILINE,
        )
        if len(positive) != 5 or len(negative) != 3:
            errors.append(
                "submission must contain exactly 5 positive and 3 negative cases"
            )

    stale_markers = (
        "Agent Knowledge Pack",
        "agent-knowledge-pack",
        "skill/claude-power-user",
        "`claude-power-user`",
        "`percorso-claude`",
        "`power-user-guide`",
        "`learning-path`",
        "`crea-knowledge-card`",
    )
    for path in (ROOT / "README.md", ROOT / "EXAMPLES.md", ROOT / "CLAUDE.md"):
        text = path.read_text(encoding="utf-8")
        for marker in stale_markers:
            if marker in text:
                errors.append(f"stale identifier {marker!r} in {path.name}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print(f"Pack validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Pack validation passed: 2 marketplaces, 2 plugin manifests, 10 skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
