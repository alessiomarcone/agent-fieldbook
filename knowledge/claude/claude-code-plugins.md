# Claude Code plugin rules

**Official sources:** [Discover and install plugins](https://code.claude.com/docs/en/discover-plugins), [Create plugins](https://code.claude.com/docs/en/plugins), [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), and [Plugins reference](https://code.claude.com/docs/en/plugins-reference). Verified 2026-07-21.

## Distribution boundary

A Claude Code plugin is a self-contained directory with
`.claude-plugin/plugin.json`. It may bundle supported components such as skills,
agents, hooks, and MCP configuration. Keep component files inside the plugin:
Claude Code copies installed plugins into a cache, so paths outside the plugin do
not remain valid after installation.

A repository can expose plugins through `.claude-plugin/marketplace.json`. A
marketplace entry points to the plugin directory; the plugin manifest belongs
inside that directory, not at the marketplace root unless the repository itself is
the plugin.

## Names and invocation

Installed plugin skills use a namespace: `/plugin-name:skill-name`. Test both a
direct invocation and an ordinary request that should activate the skill from its
description. Keep skill names and plugin names stable because users may depend on
the invocation path.

## Install and validate

For a GitHub marketplace, users can add `owner/repository` and then install
`plugin-name@marketplace-name` through Claude Code's plugin interface. Automation
can use `claude plugin marketplace add`. Before release, run
`claude plugin validate .` at the marketplace root and validate the plugin
directory itself.

## Release gate

1. Check the current manifest and marketplace schemas in the official reference.
2. Ensure every declared component exists inside the plugin boundary.
3. Document permissions, external systems, installation, invocation, updates, and
   removal.
4. Install from the distributable source in a clean environment.
5. Test direct and contextual activation, failure behavior, and side-effect gates.
6. Never package credentials, private material, raw transcripts, or unlicensed
   course content.

Claude Code plugins and Cowork plugins are different distribution surfaces. Do not
reuse Cowork-only packaging or capability claims for Claude Code.
