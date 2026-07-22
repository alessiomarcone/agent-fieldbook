<div align="center">

<img src="assets/logo.svg" alt="Agent Fieldbook mark" width="96">

# Agent Fieldbook

**Expert training, turned into source-backed skills your agent can use while it works.**

[![Validate](https://github.com/alessiomarcone/agent-fieldbook/actions/workflows/validate.yml/badge.svg)](https://github.com/alessiomarcone/agent-fieldbook/actions/workflows/validate.yml)
[![Source freshness](https://github.com/alessiomarcone/agent-fieldbook/actions/workflows/check-updates.yml/badge.svg)](https://github.com/alessiomarcone/agent-fieldbook/actions/workflows/check-updates.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-0f766e.svg)](LICENSE)
[![Claude plugin](https://img.shields.io/badge/Claude-plugin-D97757)](https://code.claude.com/docs/en/plugins)
[![Codex plugin](https://img.shields.io/badge/Codex-plugin-111827)](https://learn.chatgpt.com/docs/build-plugins)

The practical lessons from official Claude and Codex learning resources, available at the moment of work.

[Why](#the-gap-this-closes) · [Install](#install) · [Skills](#skills) · [Knowledge](#knowledge-library) · [Examples](EXAMPLES.md) · [Contribute](CONTRIBUTING.md)

</div>

> [!NOTE]
> This is an independent community project. “Official” describes its sources,
> not its publisher. Agent Fieldbook is not affiliated with or endorsed by
> Anthropic or OpenAI.

## The gap this closes

Ask Claude to structure a project and it will usually make a plausible decision
from the context it has: perhaps a project instruction file, a skill, a
subagent, a hook, or a plugin. Plausible is not always the same as the current
method Anthropic teaches.

File names change. Product mechanisms have boundaries that are easy to blur.
Some important techniques are explained deeply in a course or tutorial but are
not reliably applied when Claude is making an autonomous implementation choice.

That creates a strange experience: you can work with Claude every day, then
follow an official course and discover that the recommended structure,
terminology, or mechanism differs from what Claude just built.

**Agent Fieldbook puts those lessons into the workflow itself.** It converts
publicly available official training and documentation into compact,
source-backed instructions that Claude can apply during real work. You should
not need to complete every course before your agent can benefit from its
operating lessons.

```mermaid
flowchart LR
    A["Official courses, tutorials, and docs"] --> B["Original source synthesis"]
    B --> C["Knowledge cards and mechanism rules"]
    C --> D["Focused agent skills"]
    D --> E["Applied during real work"]
    E --> F["Verification against current sources"]
```

Claude is where this problem started. The Codex branch applies the same method
using OpenAI documentation and Academy resources, while keeping every command,
manifest, permission, and agent configuration in its own product branch.

> [!IMPORTANT]
> The skills answer in the user's language. Claude and Codex share operating
> principles, but not configuration formats. Every specialist skill selects one
> product branch before using commands, manifests, permissions, or agent fields.

## What is inside

The repository packages the resulting operating layer as:

- **10 focused skills** with classic names such as `/subagent`, `/prompt`, and `/verify`;
- **2 native plugin manifests** for Claude and Codex;
- **21 Anthropic courses** and **30 Anthropic tutorials** with direct links;
- **12 verified OpenAI learning resources**, including three formal Academy courses;
- **12 distilled Claude knowledge cards** with procedures, failure modes, and checks;
- **0 runtime credentials, hooks, MCP servers, or background processes**.

This is not a transcript archive or a replacement for the courses. It is the
execution companion: concise instructions for applying their stable lessons,
direct links for deeper study, and explicit verification whenever product
behavior may have changed.

## Install

### Claude Code

```bash
claude plugin marketplace add alessiomarcone/agent-fieldbook
claude plugin install knowledge-pack@agent-fieldbook
```

Start a new session, ask naturally, or invoke a skill directly:

```text
/knowledge-pack:navigate Should this project use instructions, a skill, or a subagent? Use current official guidance.
/knowledge-pack:verify Check whether this Claude setup follows current official guidance.
```

Claude plugin commands are namespaced by design. A standalone skill is invoked as `/subagent`; the installed plugin form is `/knowledge-pack:subagent`.

If you previously installed older standalone skills such as `prompt-perfetto` or
`verifica-output`, disable them before relying on implicit routing. Their discovery
descriptions overlap the new classic names; explicit `/knowledge-pack:<skill>`
invocation remains unambiguous during migration.

### Codex

```bash
codex plugin marketplace add alessiomarcone/agent-fieldbook
codex plugin add knowledge-pack@agent-fieldbook
```

Start a new task and mention the skill:

```text
Use $knowledge-pack:subagent to split this review into security, tests, and maintainability.
Use $knowledge-pack:skill to package our release checklist as a reusable workflow.
```

The installed plugin uses the `knowledge-pack` component namespace. Standalone
skills use the shorter `$subagent`, `$skill`, and similar names. You can also
install the plugin from the ChatGPT desktop app's Plugins directory after adding
the marketplace.

### One standalone skill

```bash
git clone https://github.com/alessiomarcone/agent-fieldbook.git
cd agent-fieldbook

# Claude Code
mkdir -p ~/.claude/skills
cp -R plugins/knowledge-pack/skills/subagent ~/.claude/skills/

# Codex
mkdir -p ~/.codex/skills
cp -R plugins/knowledge-pack/skills/subagent ~/.codex/skills/
```

## Skills

| Skill | Contract | Typical request |
|---|---|---|
| `navigate` | Choose one smallest adequate mechanism | “Should this be instructions, a skill, a subagent, or a plugin?” |
| `prompt` | Produce one bounded, verifiable task prompt | “Turn this rough objective into a ready Codex task.” |
| `verify` | Label claims by evidence and uncertainty | “Check this before I publish it.” |
| `subagent` | Decide on delegation and define a strict handoff | “Create a parallel reviewer with read-only authority.” |
| `skill` | Turn one repeated workflow into a tested skill | “Package our incident brief process.” |
| `plugin` | Build the correct distributable for one ecosystem | “Ship these skills for Claude and Codex.” |
| `cowork` | Design a sourced Cowork workflow with approval gates | “Create a weekly legal brief from connected sources.” |
| `codex` | Configure a complete Codex task or repository workflow | “Set up this repo for reliable agent work.” |
| `learn` | Sequence official resources with real durations | “I have three hours a week; teach me agent workflows.” |
| `knowledge-card` | Distill one source into reusable, verifiable knowledge | “Turn this workshop transcript into a card.” |

Skills use progressive disclosure: discovery metadata stays small, operating instructions load when selected, and platform references load only when required.

## One command, strict product branches

```text
                         /subagent
                             │
                 resolve target ecosystem
                    ┌────────┴────────┐
                    │                 │
             Claude branch       Codex branch
             Claude Code         .codex/agents/*.toml
             Managed Agents      parent sandbox/approvals
             Anthropic rules     OpenAI rules
```

The same boundary applies to `skill`, `plugin`, and product-sensitive prompting. Shared concepts are normalized; unsupported fields are never translated by analogy.

## Knowledge library

```text
knowledge/
├── claude/
│   ├── knowledge-base.md
│   ├── courses.csv
│   ├── tutorials.csv
│   ├── claude-code-plugins.md
│   ├── claude-code-subagents.md
│   ├── sources.md
│   ├── youtube.md
│   └── cards/
└── codex/
    ├── knowledge-base.md
    ├── learning-resources.csv
    ├── prompting.md
    ├── subagents.md
    ├── skills.md
    ├── plugins.md
    └── sources.md
```

Start with [knowledge-base.md](knowledge-base.md) for the universal mechanism map. Use the [Claude branch](knowledge/claude/knowledge-base.md) or [Codex branch](knowledge/codex/knowledge-base.md) for product details.

## Claude Project setup

To use the Claude corpus without installing a plugin:

1. Create a Claude Project.
2. Upload the five files in `knowledge/claude/`: `knowledge-base.md`, `courses.csv`, `tutorials.csv`, `youtube.md`, and `sources.md`.
3. Paste [claude-project-instructions.md](claude-project-instructions.md) into Project instructions.
4. Start with [session-bootstrap-prompt.md](session-bootstrap-prompt.md).

## Freshness and provenance

The source hierarchy is:

1. current official product documentation;
2. official course, tutorial, and Academy indexes;
3. official videos and workshops as explanatory material;
4. explicit uncertainty plus a verification step for sensitive details.

Claude catalog freshness runs weekly:

```bash
python3 check_official_sources.py
```

Raw transcripts are never committed. The YouTube pipeline stores only original distilled cards; see [youtube-ingestion-workflow.md](youtube-ingestion-workflow.md).

## Naming and compatibility

**Agent Fieldbook** is the public project name. `knowledge-pack` remains the
stable technical plugin namespace so installed invocations stay predictable.

This repository is not an implementation of, and does not claim conformance
with, the independent [Agent Knowledge specification](https://limecloud.github.io/agentknowledge/en/specification).
Its knowledge cards are human-readable source syntheses; its distributable is a
Claude and Codex skills plugin.

## Development

```bash
python3 scripts/sync_pack.py
python3 scripts/validate_pack.py
python3 -m unittest discover -s tests -v
python3 scripts/package_plugin.py
```

If Claude Code is installed:

```bash
claude plugin validate . --strict
```

Release artifacts are deterministic and include both plugin manifests. Public-review fixtures live in [submission](submission/).

## Security, privacy, and support

The plugin has no autonomous runtime component; any read or write action is performed by the host only in response to the user's task and permissions. See [SECURITY.md](SECURITY.md), [PRIVACY.md](PRIVACY.md), [TERMS.md](TERMS.md), and [SUPPORT.md](SUPPORT.md).

## License

Code and original curation are available under the [MIT License](LICENSE). Linked third-party material remains subject to its original terms. “Claude” and “Anthropic” are trademarks of Anthropic PBC; “OpenAI,” “ChatGPT,” and “Codex” are trademarks of OpenAI.
