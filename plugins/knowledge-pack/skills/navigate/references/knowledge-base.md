# Agent Fieldbook

A product-aware operating map distilled from official Anthropic learning material and current OpenAI Codex documentation. Use it to choose the smallest reliable mechanism, then hand the work to one focused skill.

**Verified:** 2026-07-21
**Languages:** skills answer in the user's language; source notes may be English or Italian.

## The shared operating loop

Both source ecosystems converge on the same practical loop:

1. **Describe the outcome** — goal, relevant context, output, constraints, and what “done” means.
2. **Delegate deliberately** — use the smallest mechanism that can complete the work.
3. **Inspect the result** — verify claims, artifacts, tests, and side effects in proportion to risk.
4. **Make the lesson reusable** — move stable guidance into project instructions or a focused skill.

## Choose the mechanism

| Need | Smallest mechanism | Product note |
|---|---|---|
| One answer or one artifact | Normal chat/task | Provide goal, context, boundaries, output, and done criteria. |
| Durable repository rules | `CLAUDE.md` or `AGENTS.md` | Always-on guidance; keep it short and practical. |
| Repeatable task-specific workflow | Skill | Loaded on demand; one focused intent and output contract. |
| Isolated or parallel investigation | Subagent | Separate context; bounded objective, tools, authority, and handoff. |
| Deterministic event-driven behavior | Hook | Product-specific; do not substitute a skill for an event trigger. |
| Clock-driven recurring execution | Scheduler / automation | Use the product or host scheduler; a hook reacts to an event and does not keep time. |
| External tools or data | MCP / connector | Declare access, authentication, write effects, and approval gates. |
| Installable shared bundle | Plugin | Package skills and only the supported components for that platform. |
| Programmatic production workflow | API / SDK | Add authentication, observability, evaluation, and failure handling. |

## Product branches

- [Claude knowledge base](https://github.com/alessiomarcone/claude-knowledge-pack/blob/main/knowledge/claude/knowledge-base.md) — Claude, Claude Code, Cowork, AI Fluency, courses, tutorials, and Anthropic videos.
- [Codex knowledge base](https://github.com/alessiomarcone/claude-knowledge-pack/blob/main/knowledge/codex/knowledge-base.md) — Codex surfaces, prompting, subagents, skills, plugins, permissions, and official learning resources.

Never transfer a configuration field from one branch to the other without checking the current official documentation. The concepts often rhyme; the manifests, commands, permissions, and agent formats do not.

## Classic skill entry points

| Skill | Use it when |
|---|---|
| `navigate` | You need the correct mechanism or skill. |
| `prompt` | A request needs clearer context, boundaries, or done criteria. |
| `verify` | An answer or artifact must be fact-checked or stress-tested. |
| `subagent` | You need isolated or parallel delegated work. |
| `skill` | A repeated workflow should become a reusable skill. |
| `plugin` | Skills or integrations should become an installable bundle. |
| `cowork` | A delegated Claude Cowork workflow needs folders, sources, and approval gates. |
| `codex` | The question is specifically about Codex setup or operation. |
| `learn` | You want a sequenced path through official learning material. |
| `knowledge-card` | Source material should become a compact, verifiable card. |

## Freshness rule

Treat models, plans, UI paths, command names, configuration fields, feature availability, and limits as time-sensitive. Use the bundled corpus for stable principles and consult the current official source before presenting a sensitive detail as current.
