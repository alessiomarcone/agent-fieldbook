# Codex prompting rules

**Official sources:** [Prompting](https://learn.chatgpt.com/docs/prompting), [Best practices](https://learn.chatgpt.com/guides/best-practices). Verified 2026-07-21.

## Default contract

Use the smallest useful subset of:

- Goal — the result to create or change.
- Context — relevant files, sources, examples, errors, and prior decisions.
- Boundaries — what must stay unchanged and which actions need approval.
- Output — format, audience, length, and destination.
- Done when — observable acceptance checks.

A short prompt is enough for a short task. For complex work, ask for planning or clarification before implementation. Describe the outcome first; prescribe steps only when the steps are a requirement.

## Reliability rules

- Name current sources when facts can change and request citations when they matter.
- Tell Codex to flag missing or conflicting information instead of guessing.
- Include review, tests, or artifact checks in “done when.”
- Use follow-ups to steer a running task rather than restarting when the goal is unchanged.
- Promote repeated repository guidance to `AGENTS.md`; promote a repeated workflow to a skill.
