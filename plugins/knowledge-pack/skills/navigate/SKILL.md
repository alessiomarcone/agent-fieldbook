---
name: navigate
description: Routes ambiguous mechanism comparisons to the smallest appropriate agent mechanism and skill. Use when the user is unsure whether they need instructions, a prompt, skill, subagent, hook, scheduler, MCP, plugin, Claude workflow, or Codex workflow; if the artifact is already selected, its specialist skill wins.
---

# Navigate

Route the request. Do not absorb specialist work that belongs to a narrower skill.

## Reference

Read `references/knowledge-base.md` when the mechanism boundary or product branch is not obvious.

## Routing table

| Intent | Route |
|---|---|
| Improve or design a request | `prompt` |
| Fact-check or stress-test an output | `verify` |
| Decide, design, or configure delegated agents | `subagent` |
| Create or refine an agent skill | `skill` |
| Package or distribute reusable capabilities | `plugin` |
| Design a Cowork workflow | `cowork` |
| Operate a Codex-specific surface | `codex` |
| Build an official learning path | `learn` |
| Distill source material | `knowledge-card` |
| Run work on a clock or recurring schedule | `cowork` for Claude/Cowork, `codex` for Codex, or the host scheduler/API |

If no specialist matches, select the smallest supported mechanism: normal chat/task, project knowledge, `CLAUDE.md` or `AGENTS.md`, skill, subagent, hook, scheduler/automation, MCP/connector, plugin, or API/SDK. Hooks are event-driven; they are not a substitute for clock-driven scheduling.

## Output contract

Return three fields, plus an optional fourth:

1. **Route** — one skill or mechanism.
2. **Why** — one short paragraph.
3. **Invoke** — the exact next invocation and minimum input.
4. **Freshness check** — only when a product capability may have changed.

Use `/knowledge-pack:<skill>` for the Claude Code plugin and `/<skill>` for a
standalone Claude skill. Use `$knowledge-pack:<skill>` for the Codex plugin and
`$<skill>` for a standalone Codex skill.

## Boundaries

- Choose one adequate route, not a menu of equivalent options.
- Own comparisons such as “custom agent or skill?”; once the user explicitly selects an artifact, its specialist skill wins.
- Do not execute the specialist workflow unless routing alone would block progress.
- Do not conflate a skill, subagent, hook, plugin, connector, or MCP server.
- Answer in the user's language.
