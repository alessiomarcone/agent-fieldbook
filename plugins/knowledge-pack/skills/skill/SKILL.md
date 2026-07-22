---
name: skill
description: Turns a repeated workflow into one narrow, reusable, validated agent skill with reliable triggers and progressive disclosure. Use when the user asks to create, revise, split, review, or test a SKILL.md workflow for Claude, Codex, or another Agent Skills-compatible surface; not when the request is to distribute a bundle as a plugin.
---

# Skill

Create a skill around one repeatable user intent and one output contract.

## References

Resolve the target product, then read its branch:

- Claude: `references/claude-code-estensioni.md`.
- Codex: `references/codex-skills.md`.
- Read `references/ai-fluency-4d-corso.md` when delegation, discernment, or diligence rules shape the workflow.

## Procedure

1. Confirm the workflow is repeatable and belongs in a skill rather than always-on instructions, a subagent, hook, plugin, or MCP integration.
2. Define at least three representative triggers and clear non-triggers.
3. Specify inputs, one primary output, failure behavior, side-effect policy, and success checks.
4. Keep essential procedure in `SKILL.md`; place detailed knowledge in directly linked `references/`; use scripts only for deterministic repeated operations.
5. Match freedom to risk: guidance for flexible work, templates for repeatable work, scripts for fragile deterministic work.
6. Follow the selected product's current naming and packaging rules.
7. Validate structure and forward-test triggers, non-triggers, normal cases, boundaries, and failures.

## Output contract

Return:

1. **Decision** — why a skill is the right mechanism.
2. **Contract** — triggers, non-triggers, inputs, output, failure behavior, and authority.
3. **File tree** — only required files.
4. **Implementation** — complete files when requested.
5. **Validation** — exact checks and forward-test prompts.

## Boundaries

- Do not create an “everything” skill.
- Do not package or publish a bundle of existing workflows; route distribution work to `plugin`.
- Do not duplicate detailed material in both `SKILL.md` and references.
- Do not add repository documentation inside a skill folder.
- Do not claim success before validation and trigger testing.
- Answer in the user's language.
