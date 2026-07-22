# Agent Fieldbook

Agent Fieldbook turns publicly available official training and documentation
into ten source-backed workflows Claude and Codex can apply during real work.
It helps the host choose product-correct structures instead of improvising
across instructions, skills, subagents, hooks, MCP, and plugins.

It is an execution companion, not a course or transcript archive. The plugin
has no MCP server, hooks, authentication, telemetry, or runtime background
process.

## Invoke

- Claude Code plugin: `/knowledge-pack:subagent`, `/knowledge-pack:prompt`, or another bundled skill.
- Standalone Claude skill: `/subagent`, `/prompt`, and so on.
- Codex plugin: `$knowledge-pack:subagent`, `$knowledge-pack:prompt`, and so on.
- Standalone Codex skill: `$subagent`, `$prompt`, and so on.

Available skills: `navigate`, `prompt`, `verify`, `subagent`, `skill`, `plugin`, `cowork`, `codex`, `learn`, and `knowledge-card`.

Claude and Codex use separate product references. Do not translate commands, manifests, permissions, or agent configuration by analogy.

Agent Fieldbook is not an implementation of the independent Agent Knowledge
specification. `knowledge-pack` is this plugin's technical namespace.

Source, full documentation, and updates: https://github.com/alessiomarcone/claude-knowledge-pack
