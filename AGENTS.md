# Repository guide

This repository distributes one skills-only, product-aware knowledge plugin for Claude and Codex. Keep changes source-backed, compact, and compatible with both manifests.

## Canonical files

- Keep the three naming layers distinct: public brand `Agent Fieldbook`, marketplace `agent-fieldbook`, and plugin namespace `knowledge-pack`.
- Treat `knowledge-base.md`, every file under `knowledge/`, `knowledge-card-prompt.md`, and `knowledge-card.schema.json` as canonical.
- After editing any of them, run `python3 scripts/sync_pack.py` to refresh the self-contained skill copies.
- Keep plugin versions aligned across `manifest.json`, both plugin manifests, and `.claude-plugin/marketplace.json`.
- Keep Claude and Codex commands, manifests, agent configuration, and permission rules in separate references. Never translate fields by analogy.

## Skill rules

- Keep each folder name equal to the `name` in `SKILL.md`.
- Use lowercase hyphen-case without reserved vendor names.
- Put activation cues in the frontmatter `description` and detailed material in `references/`.
- Keep `agents/openai.yaml` aligned with each skill and mention `$skill-name` in its default prompt.
- Do not add raw transcripts, copied course lessons, secrets, or private data.

## Validation

Run before handing off changes:

```bash
python3 scripts/validate_pack.py
python3 -m unittest discover -s tests -v
claude plugin validate . --strict
claude plugin validate plugins/knowledge-pack --strict
```

The Claude commands are optional only when the CLI is unavailable.
