# Claude Code subagent rules

**Official source:** [Create custom subagents](https://code.claude.com/docs/en/sub-agents). Verified 2026-07-21.

## Location and minimum contract

Claude Code subagents are Markdown files with YAML frontmatter. Project agents
live under `.claude/agents/`, user agents under `~/.claude/agents/`, and plugin
agents under the plugin's `agents/` directory. Only `name` and `description` are
required; add optional fields only when the current official page supports them
and the task needs them.

Current optional frontmatter includes `tools`, `disallowedTools`, `model`,
`permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`,
`background`, `effort`, `isolation`, `color`, and `initialPrompt`. Availability and
semantics are time-sensitive. Plugin-provided subagents ignore `hooks`,
`mcpServers`, and `permissionMode`.

## Design rules

- Make `description` specific enough for delegation discovery.
- Use `tools` as an allowlist or `disallowedTools` as a denylist; grant only what
  the objective needs.
- Default investigations to read-only. Use `isolation: worktree` only when an
  isolated working tree is genuinely useful.
- Define objective, inputs, exclusions, authority, deliverable, and success test in
  the body.
- Ask Claude to create or edit the file directly. The former `/agents` creation
  wizard was removed in Claude Code 2.1.198.

## Migration rule

When migrating from another product, read both products' official references.
Translate intent, authority, tools, and handoff requirements; never translate
frontmatter or configuration fields by name alone.
