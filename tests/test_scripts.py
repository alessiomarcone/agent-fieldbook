from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
import urllib.parse
import zipfile
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

import check_official_sources
import download_youtube_transcripts
import update_youtube_catalog

ROOT = Path(__file__).resolve().parents[1]


class CatalogTests(unittest.TestCase):
    def test_categorize_prefers_specific_rules(self) -> None:
        self.assertEqual(
            update_youtube_catalog.categorize("Build faster with Claude Code"),
            "Claude Code",
        )
        self.assertEqual(
            update_youtube_catalog.categorize("Introduction to MCP servers"),
            "Skills / Subagents / MCP / Agents",
        )

    def test_normalize_entry_builds_direct_url_and_duration(self) -> None:
        row = update_youtube_catalog.normalize_entry(
            {"id": "abc123", "title": "Prompting basics", "duration": 125}
        )
        self.assertEqual(row["URL"], "https://www.youtube.com/watch?v=abc123")
        self.assertEqual(row["Durata"], "2:05")


class TranscriptTests(unittest.TestCase):
    def test_clean_vtt_removes_cues_and_repeated_fragments(self) -> None:
        contents = """WEBVTT

00:00:00.000 --> 00:00:01.000
Hello

00:00:01.000 --> 00:00:02.000
Hello world
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.vtt"
            path.write_text(contents, encoding="utf-8")
            self.assertEqual(download_youtube_transcripts.clean_vtt(path), "Hello world")

    def test_slugify_is_stable(self) -> None:
        self.assertEqual(
            download_youtube_transcripts.slugify("Claude Code: Skills & MCP!"),
            "claude-code-skills-mcp",
        )


class SourceCheckTests(unittest.TestCase):
    def test_normalize_expands_relative_urls(self) -> None:
        self.assertEqual(
            check_official_sources.normalize("/resources/tutorials/example/"),
            "https://claude.com/resources/tutorials/example",
        )

    def test_youtube_state_changes_only_when_requested(self) -> None:
        payload = SimpleNamespace(stdout='{"entries": [{}, {}]}')
        with tempfile.TemporaryDirectory() as directory:
            state_file = Path(directory) / "state.json"
            with (
                mock.patch.object(check_official_sources, "STATE_FILE", state_file),
                mock.patch.object(
                    check_official_sources.shutil,
                    "which",
                    return_value="/fake/yt-dlp",
                ),
                mock.patch.object(
                    check_official_sources.subprocess,
                    "run",
                    return_value=payload,
                ),
            ):
                result = check_official_sources.check_youtube()
                self.assertEqual(result["count"], 2)
                self.assertFalse(state_file.exists())

                check_official_sources.check_youtube(update_state=True)
                self.assertTrue(state_file.exists())


class RepositoryTests(unittest.TestCase):
    def test_knowledge_card_prompt_matches_frontmatter_schema(self) -> None:
        prompt = (ROOT / "knowledge-card-prompt.md").read_text(encoding="utf-8")
        schema = json.loads(
            (ROOT / "knowledge-card.schema.json").read_text(encoding="utf-8")
        )
        sample = prompt.split("```markdown\n---\n", 1)[1].split("\n---", 1)[0]
        sample_keys = set(re.findall(r"^([a-z_]+):", sample, re.MULTILINE))
        self.assertEqual(sample_keys, set(schema["properties"]))
        self.assertTrue(set(schema["required"]).issubset(sample_keys))
        self.assertFalse(schema["additionalProperties"])

    def test_specialist_boundaries_remain_explicit(self) -> None:
        skills = ROOT / "plugins" / "knowledge-pack" / "skills"
        required_text = {
            "navigate": ("Own comparisons", "clock-driven scheduling"),
            "prompt": (
                "Treat explicit brevity as a hard output constraint",
                "Never invent",
            ),
            "verify": ("## Evidence gate", "every factual claim remains ⚠️"),
            "subagent": ("Simpler route", "never map fields by analogy"),
            "skill": ("route distribution work to `plugin`",),
            "plugin": ("route that work to `skill`",),
            "codex": ("narrower skill matches",),
        }
        for name, markers in required_text.items():
            contents = (skills / name / "SKILL.md").read_text(encoding="utf-8")
            for marker in markers:
                with self.subTest(skill=name, marker=marker):
                    self.assertIn(marker, contents)

    def test_pack_validator(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate_pack.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_release_archive_is_self_contained(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/package_plugin.py",
                    "--output-dir",
                    directory,
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            archive = next(Path(directory).glob("*.zip"))
            with zipfile.ZipFile(archive) as bundle:
                names = set(bundle.namelist())
            self.assertIn(".claude-plugin/plugin.json", names)
            self.assertIn(".codex-plugin/plugin.json", names)
            self.assertIn("assets/logo.png", names)
            self.assertEqual(sum(name.endswith("/SKILL.md") for name in names), 10)
            self.assertEqual(
                {Path(name).parts[0] for name in names},
                {
                    ".claude-plugin",
                    ".codex-plugin",
                    "assets",
                    "LICENSE",
                    "PRIVACY.md",
                    "README.md",
                    "SECURITY.md",
                    "SUPPORT.md",
                    "TERMS.md",
                    "skills",
                },
            )

    def test_release_archive_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            for output in (first, second):
                result = subprocess.run(
                    [
                        sys.executable,
                        "scripts/package_plugin.py",
                        "--output-dir",
                        output,
                    ],
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            first_archive = next(Path(first).glob("*.zip"))
            second_archive = next(Path(second).glob("*.zip"))
            self.assertEqual(first_archive.read_bytes(), second_archive.read_bytes())
            self.assertEqual(
                first_archive.with_suffix(".zip.sha256").read_text(encoding="utf-8"),
                second_archive.with_suffix(".zip.sha256").read_text(encoding="utf-8"),
            )

    def test_release_archive_rejects_unexpected_files(self) -> None:
        scratch = ROOT / "plugins" / "knowledge-pack" / "scratch.txt"
        try:
            scratch.write_text("must not ship\n", encoding="utf-8")
            with tempfile.TemporaryDirectory() as directory:
                result = subprocess.run(
                    [
                        sys.executable,
                        "scripts/package_plugin.py",
                        "--output-dir",
                        directory,
                    ],
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("unexpected plugin entry", result.stderr)
        finally:
            scratch.unlink(missing_ok=True)

    def test_plugin_markdown_references_resolve(self) -> None:
        plugin = ROOT / "plugins" / "knowledge-pack"
        pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
        missing: list[str] = []
        for markdown in plugin.rglob("*.md"):
            for target in pattern.findall(markdown.read_text(encoding="utf-8")):
                target = target.strip().strip("<>").split("#", 1)[0]
                parsed = urllib.parse.urlparse(target)
                if not target or parsed.scheme or target.startswith("#"):
                    continue
                resolved = markdown.parent / urllib.parse.unquote(target)
                if not resolved.exists():
                    missing.append(
                        f"{markdown.relative_to(ROOT)} -> {target}"
                    )
        self.assertEqual(missing, [])

    def test_submission_prompts_are_concrete(self) -> None:
        text = (ROOT / "submission" / "review-test-cases.md").read_text(
            encoding="utf-8"
        )
        prompts = re.findall(r"^- \*\*Prompt:\*\* (.+)$", text, re.MULTILINE)
        self.assertEqual(len(prompts), 8)
        self.assertTrue(
            all("[" not in prompt and "]" not in prompt for prompt in prompts)
        )


if __name__ == "__main__":
    unittest.main()
