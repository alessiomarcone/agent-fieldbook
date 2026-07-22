# Repository instructions

## Objective

Maintain a universal, skills-only knowledge plugin that helps Claude and Codex users operate agents from current official sources.

## Rules

- Keep the public brand `Agent Fieldbook`, marketplace `agent-fieldbook`, and plugin namespace `knowledge-pack` distinct.
- Read `knowledge-base.md` for the shared mechanism map.
- Read only `knowledge/claude/` for Claude-specific commands or configuration.
- Read only `knowledge/codex/` for Codex-specific commands or configuration.
- Never translate manifest fields, agent settings, permissions, or command names by analogy.
- Treat plans, models, limits, UI paths, commands, and feature availability as time-sensitive.
- Prefer project instructions for durable rules, a skill for on-demand expertise, a subagent for isolated context, a hook for deterministic events, and MCP/connectors for external systems.
- Require a verification step after every consequential procedure.
- Never add raw transcripts, copied course lessons, credentials, or private data.

## Development

```bash
python3 scripts/sync_pack.py
python3 scripts/validate_pack.py
python3 -m unittest discover -s tests -v
```

Keep versions aligned across `manifest.json`, both plugin manifests, and the Claude marketplace entry.
