# Changelog

All notable changes are documented here. This project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.2.0] - 2026-08-31

Version 1.1.0 made the weekly check reliable. This one makes it do the work it
had only been reporting.

### Added

- `scripts/apply_catalog_updates.py`: writes the mechanical half of a catalog update — title, URL, duration, lesson count, and quiz count read from the source page — and moves retired material into `retired-sources.md`. Columns needing judgment are filled with a `TODO:` marker.
- The weekly workflow opens a pull request with those changes instead of only describing them. It refuses and opens an issue when a run would add more rows than `CATALOG_MAX_NEW` (default 10), or when a source could not be read.
- Optional auto-merge behind the repository variable `CATALOG_AUTOMERGE`, off by default. It fires only when nothing needs a person, and a diff allowlist refuses anything outside `knowledge/`, the plugin mirrors, and `manifest.json`.
- Machine-editable markers in `retired-sources.md`.

### Changed

- `make check` now fails on any `TODO:` placeholder in a catalog. This is what keeps a generated row from reaching `main`: a pull request adding material is red until its curated columns are written.
- `verified_on` advances only on a run that came back clean. A date that moved on every run would make the 45-day freshness guard a rubber stamp.
- The `source-update` issue is now reserved for changes the bot declined to make on its own, rather than for every catalog change.

## [1.1.0] - 2026-08-31

Anthropic moved its learning material from `anthropic.skilljar.com` and
`claude.com/resources/*` to `academy.claude.com`. The move renamed some slugs,
promoted several tutorials into course lessons, and retired others. The weekly
checker scraped the old index pages, so from 2026-08-24 it reported
`page_structure_changed` and stopped seeing new material entirely.

### Added

- `knowledge/claude/catalog-scope.json`: declares which Academy material this repository catalogs, so vertical and per-connector guides are counted and reported as out of scope instead of raising a weekly alert.
- `knowledge/claude/retired-sources.md`: records material Anthropic no longer publishes, with the original URL and where the content went.
- `scripts/render_catalog.py`: generates the catalog tables in `knowledge-base.md` from the CSVs; `make render` runs it and `make sync` runs it first.
- A `verified_on` freshness guard: `make check` fails when the recorded source audit is more than 45 days old.
- 4 courses (AI Fluency for Creative Work, AI Fluency for pK-12 Train the Trainer, The AI-Native SDLC Playbook, Deploying Claude Enterprise with Confidence) and 41 tutorials.
- Link-health probing for the Claude catalogs, not only the Codex one.
- Tests for scope filtering, sitemap parsing, retired-item detection, freshness, and table rendering.

### Changed

- `check_official_sources.py` reads `academy.claude.com/sitemap.xml` instead of scraping the index pages: `/courses` and `/tutorials` render only a curated subset, so index scraping under-reported the catalog by 88 tutorials.
- The checker now reports two independent signals — `CATALOG_UPDATE_NEEDED` (editorial backlog) and `SOURCE_CHECK_FAILED` (the checker cannot read a source) — and the workflow opens a separate labeled issue for each, superseding the previous run's issue instead of commenting on it.
- Every catalog URL migrated to `academy.claude.com`; 4 course slugs were renamed upstream.
- Refreshed lesson counts, durations, and quiz counts for all 25 courses from the source pages.
- The knowledge-base catalog tables are generated from the CSVs and must not be edited by hand.

### Removed

- 4 tutorials retired by Anthropic: How AI gets its character (now a lesson of AI capabilities and limitations), Understanding knowledge gaps in AI models, Get the most from Claude Opus 4.6, Using the GitHub integration. See `retired-sources.md`.

## [1.0.0] - 2026-07-21

### Added

- Ten classic, product-aware skills: navigate, prompt, verify, subagent, skill, plugin, cowork, codex, learn, and knowledge-card.
- Separate Claude and Codex knowledge branches with strict configuration boundaries.
- Verified OpenAI documentation, Academy courses, Codex training, and bootcamp resources.
- Claude and Codex marketplace packaging with native manifests.
- Deterministic release archives, dependency-free validation, regression tests, and weekly Claude source checks.
- Privacy, terms, support, contribution, security, conduct, issue, and public-submission materials.
- Distinctive Agent Fieldbook branding with the stable `knowledge-pack` plugin namespace.
- Launch positioning centered on turning official training into instructions agents can apply while they work.

### Changed

- Reorganized the repository from a Claude-only corpus into a universal agent operating pack.
- Replaced project-specific skill names with classic public entry points such as `subagent`, `prompt`, and `verify`.
- Moved canonical material under `knowledge/claude/` and `knowledge/codex/`.

[Unreleased]: https://github.com/alessiomarcone/agent-fieldbook/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/alessiomarcone/agent-fieldbook/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/alessiomarcone/agent-fieldbook/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/alessiomarcone/agent-fieldbook/releases/tag/v1.0.0
