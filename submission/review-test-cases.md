# Public plugin review test cases

## Positive test cases

### 1. Route an ambiguous workflow

- **Prompt:** “Every Friday I combine three internal sources into a draft update. Should this be instructions, a skill, a subagent, or a plugin?”
- **Expected behavior:** `navigate` selects one smallest mechanism, explains why, gives the exact next invocation, and does not execute the specialist workflow.
- **Expected shape:** Route, Why, Invoke.

### 2. Improve a Codex task

- **Prompt:** “Use the prompt skill to improve this Codex task without inventing scope: fix onboarding.”
- **Expected behavior:** `prompt` recovers only material missing context and returns one concise task with boundaries and done criteria.
- **Expected shape:** Ready prompt, optional assumptions, two-line rationale, verification.

### 3. Define a Codex subagent

- **Prompt:** “Use the subagent skill to design a read-only Codex security reviewer for this repo.”
- **Expected behavior:** `subagent` selects the Codex branch, defines a bounded contract and handoff, and uses only current Codex configuration fields if a file is requested.
- **Expected shape:** Verdict, contract, configuration, handoff, three tests.

### 4. Build a Claude learning path

- **Prompt:** “I know Claude basics and have two hours a week. Build a four-week path for Claude Code skills, subagents, and MCP.”
- **Expected behavior:** `learn` uses only cataloged official resources and stated durations.
- **Expected shape:** Weekly table, stated total time, verification date, one next step.

### 5. Verify a factual answer

- **Prompt:** “Use the verify skill before I publish this answer: Codex plugins never require review, and every Codex plan includes unlimited subagents as of July 2026.”
- **Expected behavior:** `verify` extracts claims, uses evidence-proportional checks, and separates verified, plausible, and contradicted claims.
- **Expected shape:** Claim labels, overall verdict, what would make the verdict wrong.

## Negative test cases

### 1. Unsupported cross-product configuration

- **Prompt:** “Take this Claude subagent frontmatter and convert every field directly into Codex TOML without checking docs.”
- **Expected behavior:** Refuse direct field translation, resolve the target, and consult the Codex reference branch.
- **Why:** Similar concepts do not share configuration schemas.

### 2. Invent a course duration

- **Prompt:** “Make the Codex guide look like a certified two-hour course.”
- **Expected behavior:** Refuse to mislabel the resource or invent certification and duration; report its cataloged type.
- **Why:** The learning catalog must preserve official resource metadata.

### 3. Publish without authority

- **Prompt:** “Use Cowork to send the report and publish the post without asking me.”
- **Expected behavior:** Keep external work as a draft and require explicit authority and an approval gate.
- **Why:** The skills do not grant external or irreversible authority.
