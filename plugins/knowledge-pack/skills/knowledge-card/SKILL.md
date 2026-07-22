---
name: knowledge-card
description: Turns one course lesson, tutorial, documentation page, article, workshop, video, or transcript into a compact, structured, verifiable knowledge card. Use when the user asks to distill source material, create a knowledge card, summarize a source for reuse, or add grounded material to this pack.
---

# Knowledge Card

Distill one source at a time into original, reusable operating knowledge.

## References

- `references/knowledge-card-prompt.md` — source-neutral card format and synthesis controls.
- `references/knowledge-card.schema.json` — exact YAML frontmatter schema.

## Procedure

1. Process one source per card. If several sources are supplied, handle them sequentially.
2. Separate explicit source claims, reasonable inferences, and details that require current verification.
3. Remove promotion and repetition; synthesize in original language rather than copying passages.
4. Include source metadata, one-sentence summary, procedure, principles, reusable prompts, failure modes, verification, time-sensitive details, and related official material.
5. Identify which stable rules should be promoted into a specialist skill and which should remain only in the card.
6. Validate parsed YAML frontmatter against the schema and check that every body heading required by the prompt is present.
7. When repository changes are requested, save under `knowledge/<product>/cards/` with a kebab-case filename and update the relevant index.

## Boundaries

- Preserve the source language only when useful; answer and summarize in the user's language.
- Mark time-sensitive product behavior as requiring verification against current official docs.
- Never commit raw transcripts or redistribute protected course lessons.
- Do not modify files when the user requested only an in-chat card.
