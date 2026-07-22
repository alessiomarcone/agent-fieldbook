---
name: codex
description: Selects and designs general Codex setup and operation across the ChatGPT desktop app, CLI, IDE, cloud, AGENTS.md, permissions, MCP, scheduled tasks, and SDK. Use for Codex surface choice, repository setup, or operating workflows; specialist prompt, subagent, skill, and plugin authoring routes to those narrower skills.
---

# Codex

Turn an objective into a reviewable Codex task with the right context, authority, and completion checks.

## References

- Always read `references/knowledge-base.md` for the operating model.
- Read `references/sources.md` before making a time-sensitive product claim.
- For specialist authoring, route to `prompt`, `subagent`, `skill`, or `plugin`.

## Procedure

1. Resolve the outcome, repository or folder context, surface, risk, and definition of done.
2. Choose the surface: app for parallel local work and artifact workflows, CLI/IDE for interactive engineering, cloud for configured remote work, scheduled tasks for clock-driven recurring execution, or SDK/non-interactive mode for programmatic execution.
3. Put durable repository commands, conventions, boundaries, and verification in the nearest applicable `AGENTS.md`.
4. Add a focused skill for a repeated workflow and a custom agent only when isolation or a distinct configuration is valuable.
5. Use the least authority that can complete the task; make external and irreversible actions explicit.
6. Require relevant tests, review, and a concise final report of changes and remaining uncertainty.
7. Check current official documentation for commands, fields, models, plans, and feature availability.

## Output contract

Return:

1. **Surface and mechanism** — one primary choice and why.
2. **Context setup** — files, instructions, tools, and permissions.
3. **Ready task** — a complete Codex prompt or configuration.
4. **Done when** — observable checks.
5. **Reuse** — what belongs in `AGENTS.md`, a skill, custom agent, or plugin.

## Boundaries

- Do not invent current commands, configuration, or availability.
- Do not absorb prompt, subagent, skill, or plugin authoring when a narrower skill matches.
- Do not request broader permissions than the task needs.
- Do not transfer Claude-only configuration into Codex.
- Answer in the user's language.
