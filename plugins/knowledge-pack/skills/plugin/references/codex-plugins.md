# Codex plugin rules

**Official sources:** [Build plugins](https://learn.chatgpt.com/docs/build-plugins), [Submit plugins](https://learn.chatgpt.com/docs/submit-plugins). Verified 2026-07-21.

## Package boundary

A Codex plugin requires `.codex-plugin/plugin.json`. It may include `skills/`, `.mcp.json`, `.app.json`, `hooks/`, and presentation assets at the plugin root. Only `plugin.json` belongs inside `.codex-plugin/`. Every declared path must exist inside the distributable bundle.

Use stable kebab-case identifiers and SemVer. Provide accurate author, license, repository, interface, and capability metadata for public distribution. A repository marketplace lives at `.agents/plugins/marketplace.json` and points to the plugin using a `./`-prefixed path relative to the marketplace root.

## Release gate

1. Validate manifest and component paths.
2. Validate every bundled skill and its references.
3. Package from a clean, reproducible file list.
4. Install from the marketplace into a clean environment.
5. Test direct and implicit skill activation.
6. Audit permissions, data handling, external effects, legal links, and source licenses.

## Public submission

A skills-only public submission needs verified publisher identity, production-ready listing material, the final skill bundle, starter prompts, exactly five positive test cases, exactly three negative test cases, region availability, and release notes. Submission starts review; publication happens only after approval and a separate publish action.

Do not mix Claude-only manifest fields or commands into the Codex manifest. Shared concepts do not imply shared schemas.
