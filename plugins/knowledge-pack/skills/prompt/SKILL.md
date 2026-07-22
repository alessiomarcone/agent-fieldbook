---
name: prompt
description: Improves, rewrites, or designs concise prompts with clear outcomes, context, boundaries, output requirements, and verification. Use for direct requests such as “improve this prompt,” for Claude or Codex task formulation, weak-response troubleshooting, or turning a rough objective into a ready-to-run task.
---

# Prompt

Turn a rough request into the shortest prompt that reliably defines the work.

## References

- Read `references/ai-fluency-4d-corso.md` for Anthropic's Description framework and prompting techniques.
- Read `references/codex-prompting.md` for current Codex prompting rules when the target is Codex.
- Read `references/regole-distillate.md` only for cross-cutting boundaries and verification.

## Procedure

1. Resolve the target product only when product behavior changes the prompt.
2. Recover only missing parts that materially affect the result and are supported by the user's request or supplied context:
   - **Goal:** the result to create or change.
   - **Context:** relevant sources, files, examples, errors, and prior decisions.
   - **Boundaries:** what must stay unchanged, what not to invent, and which actions require approval.
   - **Output:** artifact, format, audience, length, and destination.
   - **Done when:** observable acceptance checks.
3. Add examples, role, decomposition, a checklist, or an explicit planning step only when the user requests them or they resolve a concrete ambiguity. Do not add a conventional template merely because it is common for that task type.
4. Never invent missing scope, numbers, timelines, audiences, deliverables, or acceptance criteria. Preserve a concise request and its approximate length when the user asks for brevity. Use a visible placeholder for a necessary unknown; ask one focused question only when no useful prompt can be produced without the answer.
5. Add a freshness or source requirement for time-sensitive claims.
6. Return one ready-to-copy prompt; do not execute it unless requested.

## Output contract

Return:

1. **Ready prompt** — one copyable block.
2. **Assumptions** — only unavoidable assumptions; omit if none.
3. **Why it works** — at most two lines.
4. **Verification** — the most important check on the result.

When the user explicitly requests a short or simple rewrite, return only the
**Ready prompt** and, if essential, one line of **Verification**. Do not append a
rationale, assumptions section, or follow-up question.

## Boundaries

- Do not inflate a simple request into a long template.
- Treat explicit brevity as a hard output constraint.
- Do not turn an unspecified constraint into a convenient assumption.
- Split unrelated tasks into separate prompts.
- If the actual need is a skill, project instruction, connector, or subagent, say so.
- Answer in the user's language.
