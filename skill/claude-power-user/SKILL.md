---
name: claude-power-user
description: Use this skill when the user asks how to use Claude effectively, choose among Claude features, improve prompting, design a Claude Project, create or revise a Skill, use connectors or MCP, work with Claude Code, subagents, hooks, plugins, Artifacts, Cowork, or the Claude API.
---

# Claude Power User

Use this skill to turn an objective into the correct Claude capability and a reusable, verifiable workflow.

## Read references

Before giving feature-specific guidance, consult:

- `references/cards/regole-distillate.md` — cross-product rules distilled from the official tutorials; read this first for any "how should I use Claude" question
- `references/cards/` — per-product operational cards (@Claude workspace, Cowork, plugins, Excel, Design, desktop app, AI fluency curriculum); each card lists procedures, ready prompts, mistakes and verification steps from the official tutorials
- `references/knowledge-base.md` (courses, tutorials, and YouTube catalog are merged inline here)
- `references/sources.md`
- `references/courses.csv` / `references/tutorials.csv` / `references/youtube.md` for the raw, sortable/filterable source data behind that section

Cards marked in `references/cards/pending-video-ingestion.md` cover video-only tutorials: for those topics, answer from primary documentation and flag that the tutorial content has not been ingested yet.

Treat official documentation as primary. Treat videos and courses as explanatory material. Flag anything that may have changed since the source date.

## Capability triage

Choose the smallest adequate mechanism:

- **Chat**: one-off task with no persistent setup.
- **Project knowledge**: stable files and domain context used across chats.
- **Project Instructions / CLAUDE.md**: short persistent rules and conventions.
- **Skill**: reusable, on-demand procedure or expertise.
- **Connector / MCP**: live external data or actions.
- **Artifact**: a standalone interactive or editable output.
- **Claude Code**: repository-aware engineering work.
- **Subagent**: isolated context, parallel investigation, or specialist role.
- **Hook**: deterministic action triggered by an event.
- **Plugin**: distributable bundle of extensions.
- **API**: programmatic integration, scale, structured tools, or product embedding.

## Apply the 4D method

1. **Delegation** — state what Claude does and what remains a human decision.
2. **Description** — define goal, context, constraints, examples, success criteria, and output format.
3. **Discernment** — test assumptions, sources, edge cases, and quality.
4. **Diligence** — verify sensitive claims, protect data, document decisions, and monitor results.

## Response contract

Return:

1. **Scelta consigliata**
2. **Perché**
3. **Procedura**
4. **Prompt o file pronto all’uso**
5. **Verifica**
6. **Riutilizzo**

When the user repeats a workflow, propose a Skill structure. Keep `SKILL.md` concise and place extensive material in `references/`. Use scripts only for deterministic operations.

## Freshness and truthfulness

- Never invent a feature, interface path, model capability, plan restriction, or quota.
- State the source date for time-sensitive guidance.
- When official sources conflict, prefer the newer product documentation.
- When no current source is available, say what is uncertain and give a verification step.
