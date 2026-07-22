---
name: plugin
description: Designs, packages, validates, and prepares distributable plugins containing skills and optional supported extensions. Use when the user asks to build, migrate, publish, install, distribute, or troubleshoot a Claude Code, Cowork, ChatGPT, or Codex plugin or marketplace; not for creating one standalone skill.
---

# Plugin

Resolve the product and distribution surface before writing any manifest.

## References

Read only the selected product branch:

- Claude Code: `references/claude-code-plugins.md`.
- Claude Cowork: `references/plugin-building.md`.
- Codex: `references/codex-plugins.md`.

## Procedure

1. Identify target product, installation model, namespace, and public or private distribution path.
2. Inventory only required capabilities: skills, agents/subagents, hooks, MCP/connectors/apps, or supported assets.
3. Prefer several focused skills with explicit handoffs over one broad workflow.
4. Keep every declared component inside the distributable boundary.
5. Use only fields supported by the selected product's current schema.
6. Document install, direct invocation, permissions, provenance, update, and uninstall behavior.
7. Validate source and packaged artifact; install in a clean environment; test direct and contextual activation.
8. For public submission, prepare the exact listing, legal, safety, and reviewer materials required by that ecosystem.

## Output contract

Return:

1. **Target** — product, installation model, namespace, and distribution path.
2. **Architecture** — component tree and reason for each component.
3. **Files** — ready-to-use manifests and components when implementation is requested.
4. **Install and invoke** — exact current commands.
5. **Release gate** — validation, clean install, permissions audit, tests, and versioning.

## Boundaries

- Do not mix fields from different plugin ecosystems.
- Do not activate for creation or revision of a single standalone skill; route that work to `skill`.
- Do not declare components without their companion files.
- Do not claim commands, UI paths, or submission requirements without current official support.
- Do not distribute credentials, private data, raw transcripts, or unlicensed material.
- Answer in the user's language.
