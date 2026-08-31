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
make sync    # renders the knowledge-base tables, then mirrors into the plugin
make check   # validation and tests
```

If Claude Code is installed:

```bash
claude plugin validate . --strict
claude plugin validate plugins/knowledge-pack --strict
```

## Catalog updates

`knowledge/claude/courses.csv` and `knowledge/claude/tutorials.csv` are the
single source of truth. The catalog tables in `knowledge/claude/knowledge-base.md`
sit between `<!-- catalog:*:start -->` markers and are generated: edit the CSV,
never the table.

- Preserve existing CSV columns and UTF-8 encoding.
- Use canonical `https://` URLs and avoid duplicates.
- Run `python3 check_official_sources.py` to see what changed upstream.
- Update the relevant file under `knowledge/`.
- Run `make sync` (renders the tables, then mirrors into the plugin).
- Update counts and `verified_on` in `manifest.json`.
- Run `make check`.

### Generated pull requests

The weekly check no longer only reports. When it finds a catalog change it can
handle, `scripts/apply_catalog_updates.py` writes the mechanical half and opens
a pull request: title, URL, duration, lesson count, and quiz count read from the
source page, retired material moved to `retired-sources.md`, tables re-rendered,
mirrors synced, counts updated.

The columns that need judgment — `Categoria`, `Obiettivo`, `Perché è utile` —
are filled with `TODO:` and `make check` rejects them. **A generated pull
request that adds material is red on purpose.** Fill the TODO columns, push to
the branch, and it goes green. Nothing about that is a build failure to debug.

The bot refuses and opens an issue instead when a run would add more rows than
`CATALOG_MAX_NEW` (default 10), or when it could not read a source. A bulk
upstream change — a site migration, a section launch — is exactly where an
unattended edit is wrong.

Optional, off by default: set the repository variable `CATALOG_AUTOMERGE` to
`true` to let a generated pull request merge itself. It fires only when nothing
needs a person, which in practice means retirements, and a second gate refuses
any diff touching paths outside `knowledge/`, the plugin mirrors, and
`manifest.json`. Pull requests created with `GITHUB_TOKEN` do not trigger other
workflows, so the merge gate runs `make check` inline rather than waiting on the
Validate workflow.

### Scope

`knowledge/claude/catalog-scope.json` declares which Claude Academy material
this repository catalogs. Claude Academy publishes vertical and partner
integration guides (financial services, life sciences, per-connector how-tos)
that fall outside the fieldbook: the checker counts them, reports them as out
of scope, and does not raise a weekly alert for them. Removing a pattern from
that file brings the material back in scope, and the next run will report every
matching slug as uncataloged.

### Retired sources

When Anthropic retires material, move the row to
`knowledge/claude/retired-sources.md` with its original URL and last-seen date
instead of deleting it silently. Knowledge cards cite sources by name, and a
deleted row makes a cited source indistinguishable from one that never existed.

### Freshness

`manifest.json` carries `verified_on`. `make check` fails when it is more than
45 days old, so an unattended catalog breaks CI instead of drifting quietly.

The bot advances that date only on a run that came back clean — no unreadable
source, nothing to add. A date that moved on every run would be a rubber stamp,
and the guard would stop meaning anything.

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
