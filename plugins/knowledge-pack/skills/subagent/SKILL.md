---
name: subagent
description: Decides whether selected delegated work needs agents and designs a strict, product-correct subagent contract with isolated context, bounded tools, authority, deliverables, and tests. Use when the user asks to create, configure, delegate to, or troubleshoot Claude or Codex subagents, parallel agents, custom agents, or managed-agent workflows; not for open mechanism comparisons.
---

# Subagent

Design the smallest delegated unit that can return a decision-ready handoff.

## References

Resolve the product first, then read only its branch:

- Claude Code: `references/claude-code-subagents.md`.
- Anthropic Managed Agents: also read `references/managed-agents.md`.
- Codex: `references/codex-subagents.md`.

Never transfer fields, commands, models, tools, or permission semantics between branches.
For a cross-product migration, read both the source and target official references,
map intent and constraints, and never map fields by analogy.

## Decision gate

Use a subagent only when at least one is true:

- independent work can proceed in parallel;
- a separate context prevents noise or context pollution;
- a specialist needs a different model, tool, or sandbox boundary;
- the parent needs a compact result rather than the full exploration.

Otherwise return only **Verdict** and **Simpler route**, then stop.

## Procedure

1. Identify the exact surface and current supported configuration format.
2. Define objective, inputs, exclusions, allowed tools, authority, deliverable, and success test.
3. Default investigations to read-only. Require explicit authority for edits, external messages, publication, or destructive effects.
4. State what context the child receives, must discover, and must not assume.
5. Prefer read-heavy parallelism; coordinate agents that share writable state.
6. Require a handoff with evidence, changes, unresolved risks, and a concise conclusion.
7. When implementation is requested, verify time-sensitive configuration against current official documentation and validate the file.

## Output contract

When the verdict is yes, return:

1. **Verdict** — why delegation is warranted.
2. **Contract** — objective, inputs, exclusions, tools, and authority.
3. **Prompt/configuration** — ready to use for the selected product.
4. **Handoff** — exact required return shape.
5. **Tests** — normal, boundary, and failure case.

## Boundaries

- Do not invent configuration fields or availability.
- Do not activate for an open comparison such as “custom agent or skill?”; route mechanism comparisons to `navigate`.
- Do not accept “research this” without a decision-ready deliverable.
- Do not permit silent external side effects.
- Answer in the user's language.
