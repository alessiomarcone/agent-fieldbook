# Prompt — Distill one source into a knowledge card

Use this prompt with one course lesson, tutorial, documentation page, article,
workshop, video, or transcript at a time.

---

Analyze the supplied source as evidence. Produce a compact, operational,
reusable knowledge card for the product or topic actually covered by the source.

## Rules

1. Do not add capabilities or claims that the source does not support.
2. Distinguish explicit source claims, reasonable inferences, and details that
   require current verification.
3. Treat models, plans, limits, commands, UI paths, schemas, and availability as
   time-sensitive; check current official documentation before calling them current.
4. Remove promotion and repetition. Keep examples only when they clarify a
   decision, procedure, or failure mode.
5. Synthesize in original language. Do not reproduce long passages or raw lessons.
6. Use the exact frontmatter fields below. Validate the parsed YAML frontmatter
   against `knowledge-card.schema.json`; the schema does not validate the body.

## Output

```markdown
---
title: "Concise source-specific title"
source_url: "https://example.com/source"
source_type: documentation
source_products:
  - "Product or topic"
source_date: null
verified_on: "YYYY-MM-DD"
language: "en"
tags:
  - "focused-tag"
status: current
time_sensitive: true
license_note: "Original synthesis; source material is not redistributed."
---

# Concise source-specific title

## In one sentence

...

## When to use it

- ...

## Prerequisites

- ...

## Procedure

1. ...

## Principles and decisions

- **Source states:** ...
- **Reasonable inference:** ...

## Reusable prompts or configurations

...

## Failure modes

- ...

## Verification

- ...

## Time-sensitive items

- ...

## Related official material

- ...

## Promotion decision

- **Promote into a specialist skill:** ...
- **Keep in this card:** ...
```

Use `null` when the source publication date is not available. `license_note` is
required so downstream users can distinguish original synthesis from source
material. Omit only `time_sensitive` when it does not apply. Preserve every
required body heading; write `None identified` rather than silently deleting an
empty section.
