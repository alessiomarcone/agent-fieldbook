# Codex skill rules

**Official source:** [Build skills](https://learn.chatgpt.com/docs/build-skills). Verified 2026-07-21.

A skill is a focused directory with `SKILL.md` and optional references, scripts, and assets. It is both explicitly invocable with `$skill-name` and eligible for implicit activation when its description matches the task.

## Authoring contract

- One repeatable user intent and one primary output contract.
- Folder and frontmatter `name` match in lowercase hyphen-case.
- Description says what the skill does and when it should activate.
- `SKILL.md` contains the essential workflow and directly links only needed resources.
- `references/` contains detailed knowledge; `scripts/` contains deterministic repeated operations; `assets/` contains output resources.
- Examples include normal, boundary, and failure behavior.
- The skill does not request tools, permissions, or network access it does not need.

Use progressive disclosure: discovery metadata is always cheap, the full workflow loads when selected, and detailed references load only when required. Validate structure and forward-test both triggers and non-triggers before distribution.
