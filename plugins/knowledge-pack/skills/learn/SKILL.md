---
name: learn
description: Builds a sequenced learning path from verified official Anthropic and OpenAI course, tutorial, guide, video, and workshop catalogs. Use when the user asks where to start, which Claude or Codex course to take, how to learn prompting, skills, plugins, subagents, MCP, Cowork, or the API, or how long a study plan will take.
---

# Learn

Build a focused official learning path with accurate resource types, durations, and direct links.

## Catalogs

- `references/claude-courses.csv` — 21 official Anthropic courses.
- `references/claude-tutorials.csv` — 30 official Anthropic tutorials.
- `references/codex-learning-resources.csv` — verified OpenAI courses, guides, videos, resources, and live series.

## Procedure

1. Resolve product, goal, starting level, weekly time, and target date when they affect the plan.
2. Read the relevant catalogs and select the minimum sequence that reaches the goal.
3. Label each item with its real type. Never present a guide, video, workshop, or live event as a self-paced course.
4. Use only stated durations; write “not stated” when the official source gives none.
5. Add one practical exercise after each learning block.
6. Use at most three resources per week and end with one concrete next action.

## Default sequences

- Claude foundations: Claude 101 → AI capabilities and limitations → AI Fluency: Framework & Foundations.
- Claude Code: Claude Code 101 → Claude Code in Action → Agent Skills → Subagents → MCP.
- Codex foundations: AI Foundations → Codex Quickstart → Prompting/Best practices → one real task.
- Codex agent workflows: Applied AI Foundations → Agents and Workflows → `AGENTS.md` → Skills → Subagents.
- Codex advanced: permissions/sandboxing → plugins → SDK/non-interactive mode → automation and review.

## Output contract

Return a table with week, resource, type, duration, practical outcome, exercise, and direct link. Close with total stated time, catalog verification date, and one next step.

## Boundaries

- Do not invent resources, duration, or certification status.
- Flag live events with their date and verify availability before recommending them.
- Answer in the user's language.
