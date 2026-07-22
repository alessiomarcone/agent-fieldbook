---
name: verify
description: Fact-checks and stress-tests AI answers or artifacts with claim-level evidence, uncertainty, anti-hallucination, and anti-sycophancy checks. Use for brief or detailed requests to check, verify, or review an answer before sending or publishing, and for consequential legal, financial, technical, or customer-facing decisions.
---

# Verify

Apply verification in proportion to risk and make uncertainty explicit.

## Evidence gate

Run this before factual analysis. Count sources supplied by the user or actually
retrieved in this task. If the count is zero, do not assess, compare, correct, or
quote facts from pretrained knowledge. Label every claim **⚠️ Unverified — no
evidence available**, name the exact authoritative retrieval step, report that a
verdict is not yet possible, and stop.

## References

- Read `references/ai-literacy.md` for knowledge gaps, sycophancy, and hallucination patterns.
- Read `references/regole-distillate.md` for cross-cutting verification rules.

## Procedure

1. After passing the evidence gate, classify risk. Use a quick check for reversible internal work and a source-backed check for consequential work.
2. Extract substantive claims, especially names, dates, figures, quotes, citations, recent changes, and niche facts.
3. Verify each claim against a source that actually supports it. A claim cannot receive ✅ or ❌ without a supplied or retrieved citation. Prefer current primary sources for product, legal, medical, financial, and technical claims.
4. Check for sycophancy: neutralize the user's framing, seek counterevidence, and distinguish agreement from support.
5. Inspect the process: undeclared assumptions, circular reasoning, missing cases, inconsistent calculations, or skipped acceptance criteria.
6. Perform an independent final pass and state what would make the verdict wrong.

## Claim labels

- ✅ **Verified** — directly supported by cited evidence.
- ⚠️ **Plausible, not verified** — include the exact verification step.
- ❌ **Contradicted or fabricated** — directly contradicted by cited evidence; provide a supported correction.

Close with an overall verdict and **What would make this output wrong?**

## Boundaries

- Absence of evidence is not evidence of absence.
- If retrieval tools or supplied sources are unavailable, every factual claim remains ⚠️. Do not provide remembered figures, dates, product history, or corrections; give only the exact authoritative source or retrieval step needed.
- If most claims remain unverified, recommend retrieval from authoritative sources.
- Never treat the model's confidence as evidence.
- Answer in the user's language.
