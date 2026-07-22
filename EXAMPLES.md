# Examples

Every example shows the smallest useful entry point and the shape of a good result.

## Route an ambiguous workflow

Claude plugin:

```text
/knowledge-pack:navigate Every Friday I combine three sources into a draft update. Should this be instructions, a skill, a subagent, or a plugin?
```

Codex:

```text
Use $knowledge-pack:navigate to choose the smallest mechanism for this recurring workflow.
```

Expected: one route, one reason, one exact next invocation, and a freshness check only when necessary.

## Define a strict subagent

```text
Use $knowledge-pack:subagent to design a read-only reviewer for this repository. It should inspect security risks, return file evidence, make no edits, and stop if it needs network access.
```

Expected: a positive delegation verdict, objective, scope, tool and authority boundary, product-correct configuration, handoff format, and three tests. If delegation is unnecessary, the skill returns only a verdict and simpler route.

## Improve a task without prompt bloat

```text
/knowledge-pack:prompt Improve this request without making it longer than necessary:

“Review onboarding.”
```

Expected: one copyable prompt that preserves the short request, adds only material requirements, and leaves necessary unknowns as visible placeholders instead of inventing them.

## Verify before publishing

```text
Use $knowledge-pack:verify on the following launch post. Check every product claim, date, figure, and link against current primary sources. Label unsupported claims and give corrections.
```

Expected: claim-level ✅, ⚠️, or ❌ labels, an overall verdict, and what would make that verdict wrong.

## Build a focused skill

```text
Use $knowledge-pack:skill to package our weekly release-readiness review. It should trigger only for release reviews, read our checklist, return blockers by severity, and never publish or merge.
```

Expected: mechanism decision, trigger/non-trigger contract, minimal file tree, implementation when requested, and forward tests.

## Build a cross-platform plugin

```text
Use $knowledge-pack:plugin to package these workflows for both Claude and Codex. Keep one skills directory but separate the manifests and all product-specific references.
```

Expected: two validated packaging branches, no cross-product fields, clean-install instructions, and a release gate.

## Learn Claude Code

```text
/knowledge-pack:learn I know Claude basics and have two hours a week. Build a four-week official path for Claude Code skills, subagents, and MCP.
```

Expected: resources selected from `knowledge/claude/courses.csv` and `tutorials.csv`, real stated durations, one exercise per block, and direct links.

## Learn Codex agent workflows

```text
Use $knowledge-pack:learn to take me from Codex beginner to writing AGENTS.md, skills, and custom agents. I have three hours a week.
```

Expected: formal Academy courses labeled as courses, docs and videos labeled accurately, no invented durations, and a practical progression.

## Design a Cowork workflow

```text
/knowledge-pack:cowork Create a weekly legal question brief from connected sources. Keep citations, flag missing data, and leave all external messages as drafts.
```

Expected: one-time setup, exact brief, approval gates, verification, and the rule to promote into a reusable skill after the first successful run.

## Distill a source

```text
Use $knowledge-pack:knowledge-card on this workshop transcript. Separate explicit claims from inference, remove promotion, and flag every time-sensitive product detail.
```

Expected: an original structured card. If editing this repository, save it under `knowledge/<product>/cards/`; never commit the raw transcript.
