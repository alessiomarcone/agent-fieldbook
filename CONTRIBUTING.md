# Contributing

Thanks for improving Agent Fieldbook. The project favors small, source-backed changes that keep the installed plugin compact, product-correct, and trustworthy.

## Good contributions

- Add or update an official Anthropic or OpenAI learning resource.
- Improve a skill trigger, boundary, workflow, example, or verification step.
- Fix packaging, validation, accessibility, or cross-platform behavior.
- Translate user-facing guidance while preserving source attribution and exact product terms.

Open an issue before a large restructure or a new skill. Small fixes and source updates can go directly to a pull request.

## Source policy

1. Prefer current official documentation for commands, schemas, availability, permissions, and limits.
2. Use official courses, tutorials, Academy material, and videos as explanatory sources.
3. Record a source URL and verification date for time-sensitive claims.
4. Distinguish sourced facts, reasonable deductions, and uncertain details.
5. Label courses, guides, videos, workshops, and live events accurately.
6. Never commit course lessons, raw transcripts, subtitles, private data, or credentials.

## Product boundary

Shared concepts may be summarized once, but product behavior must stay in its own branch:

- Claude material: `knowledge/claude/`
- Codex material: `knowledge/codex/`

Do not copy configuration fields, commands, permission behavior, or plugin metadata from one ecosystem into the other without current official documentation.

## Local workflow

Use Python 3.10 or newer. Core checks have no third-party dependencies.

```bash
git clone https://github.com/alessiomarcone/agent-fieldbook.git
cd agent-fieldbook
python3 scripts/sync_pack.py
python3 scripts/validate_pack.py
python3 -m unittest discover -s tests -v
```

If Claude Code is installed:

```bash
claude plugin validate . --strict
claude plugin validate plugins/knowledge-pack --strict
```

## Catalog updates

- Preserve existing CSV columns and UTF-8 encoding.
- Use canonical `https://` URLs and avoid duplicates.
- Update the relevant file under `knowledge/`.
- Run `python3 scripts/sync_pack.py`.
- Update counts and `verified_on` in `manifest.json`.
- Run the full validation suite.

## Skill changes

- Keep the folder name equal to frontmatter `name`.
- Use lowercase hyphen-case without reserved vendor names.
- State what the skill does and when it activates in `description`.
- Keep `SKILL.md` focused; put detailed material in directly linked `references/`.
- Define failure behavior, side-effect authority, and verification.
- Update `agents/openai.yaml` and its `$skill-name` default prompt.
- Forward-test normal triggers, non-triggers, boundary cases, and failure cases.

## Releases

Before a release:

1. update `CHANGELOG.md`;
2. align versions in `manifest.json`, both plugin manifests, and the Claude marketplace;
3. update `verified_on` after the source audit;
4. run `make check` and native plugin validation;
5. run `make package` and inspect the checksum;
6. test a clean install in both ecosystems;
7. verify the five positive and three negative public-review cases.

## Pull request checklist

- [ ] The change is scoped and source-backed.
- [ ] Claude and Codex details remain separated.
- [ ] Mirrored references are synchronized.
- [ ] No transcript, secret, or private data is included.
- [ ] `make check` passes.
- [ ] User-facing behavior and changelog are updated when relevant.
