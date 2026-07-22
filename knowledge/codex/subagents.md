# Codex subagent rules

**Official source:** [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents). Verified 2026-07-21.

## Decision rule

Use subagents when work is meaningfully independent, parallelizable, noisy enough to isolate, or benefits from a specialist model/tool/sandbox configuration. Avoid them for a single linear task or as decoration; every agent consumes its own context and tools.

Prefer read-heavy parallelism: repository exploration, test execution, triage, review, or summarization. Coordinate write-heavy agents carefully because they share a working tree and can conflict.

## Delegation contract

Every delegated task must define:

1. objective and decision to enable;
2. inputs and scope;
3. exclusions and authority;
4. allowed tools or sandbox expectations;
5. required evidence and final output;
6. success, boundary, and failure checks.

The parent waits for requested agents, reconciles conflicting findings, and returns one consolidated result.

## Custom agents

Project agents live in `.codex/agents/*.toml`; personal agents live in `~/.codex/agents/*.toml`. Current required fields are `name`, `description`, and `developer_instructions`. Optional model, reasoning, sandbox, MCP, and skill settings inherit when omitted. Treat the format as product-specific and verify fields against current documentation before emitting configuration.

Subagents inherit the parent turn's live sandbox and approval choices unless a supported per-agent override applies. Do not promise a child more authority than the parent runtime can provide.
