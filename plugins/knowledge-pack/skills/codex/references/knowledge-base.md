# Codex knowledge base

A compact operating reference for Codex and ChatGPT Work, distilled from current official OpenAI documentation and Academy material.

**Verified:** 2026-07-21

## Start with a complete task contract

For consequential work, include:

- **Goal:** the outcome to create or change.
- **Context:** the files, sources, examples, errors, or systems that matter.
- **Boundaries:** what must not change and which actions require approval.
- **Output:** the artifact, format, audience, and useful level of detail.
- **Done when:** observable acceptance checks, including tests or review.

State the result you need before prescribing every implementation step. Add process constraints only when the process itself matters.

## Put durable guidance in the right layer

| Layer | Use it for |
|---|---|
| Prompt | One task's objective, context, constraints, and acceptance checks. |
| `AGENTS.md` | Shared repository layout, commands, conventions, risk rules, and definition of done. |
| Skill | A focused workflow that should activate explicitly or by matching user intent. |
| Custom agent | A specialist subagent configuration with a distinct model, instructions, tools, or sandbox boundary. |
| Plugin | An installable bundle of skills and optional apps, MCP servers, or hooks. |
| MCP | Tools and external context exposed through a defined protocol. |

More specific `AGENTS.md` files override broader guidance for their subtree. Keep shared instructions concise; move detailed task playbooks into skills.

## Use subagents for isolation or real parallelism

Delegate when independent work can run in parallel, a separate context prevents noise, or a specialist needs a different configuration. Keep write-heavy parallel work limited because agents share the working tree and can conflict.

A complete delegation names the objective, inputs, exclusions, allowed tools, authority, deliverable, and success test. The parent should receive distilled evidence and decisions—not raw logs.

Codex custom agents are TOML files under `.codex/agents/` for a project or `~/.codex/agents/` for a user. Required fields are `name`, `description`, and `developer_instructions`; optional configuration inherits from the parent when omitted. Confirm current fields in official documentation before generating a file.

## Build focused skills, distribute stable plugins

A skill contains `SKILL.md` plus optional references, scripts, and assets. Its `name` and `description` are discovery metadata, so the description must state both what the skill does and when it should activate. Detailed reference material should load only when the workflow needs it.

A plugin is the public distribution boundary. Codex plugins require `.codex-plugin/plugin.json`; a plugin can package skills and optionally MCP-backed apps, MCP configuration, or hooks. Keep component paths inside the plugin and validate the installed copy, not only the source tree.

Public plugin submission is a separate review flow. Skills-only submissions require the final bundle, production listing material, starter prompts, exactly five positive test cases, and three negative test cases.

## Permissions are part of the task design

Sandbox mode controls filesystem/network reach; approval policy controls when user confirmation is required. Subagents inherit the parent runtime policy unless a supported custom-agent setting overrides it. Start with the least authority that can complete the task and make all external or irreversible effects visible.

## Verification loop

For implementation work:

1. Inspect the relevant context and applicable instructions.
2. Make the smallest coherent change.
3. Add or update tests when behavior changes.
4. Run the relevant test, lint, format, or type checks.
5. Review the diff for regressions and unintended effects.
6. Report what changed, what was verified, and what remains uncertain.

## Suggested learning order

1. Quickstart and Prompting.
2. Best practices and `AGENTS.md`.
3. Permissions, sandboxing, and review.
4. Skills and plugins.
5. Subagents and custom agents.
6. SDK, non-interactive mode, and production automation.

Use the `learn` skill and its `codex-learning-resources.csv` catalog for direct links and resource types.
