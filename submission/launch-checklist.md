# Launch checklist

## Repository release gate

- [x] `python3 scripts/sync_pack.py` reports every mirror synchronized.
- [x] Local `make check` passes.
- [x] The validation workflow passes on Python 3.10–3.13 after push.
- [x] Every bundled skill passes the Codex skill validator.
- [x] The source plugin and extracted release ZIP pass Claude's strict validator.
- [x] The Codex plugin manifest passes the current plugin validator.
- [x] Every declared knowledge-card source endpoint is reachable.
- [ ] A clean Claude install can invoke `/knowledge-pack:navigate`.
- [ ] A clean Codex install can invoke `$knowledge-pack:navigate`.
- [ ] The five positive and three negative review cases pass from the release artifact.
- [x] The ZIP checksum matches after a second deterministic build.
- [x] `v1.0.0` matches every manifest and the changelog.

## GitHub launch

- [ ] Approve the English and Italian founder story in `submission/launch-copy.md`.
- [x] Rename the remote repository to `agent-fieldbook`; GitHub redirects preserve the old URL.
- [x] Set the description to “Source-backed skills that turn official Claude and Codex training into reliable daily workflows.”
- [x] Add topics: `agent-skills`, `claude`, `codex`, `prompt-engineering`, `subagents`, `ai-fluency`.
- [x] Prepare the 1280×640 social preview at `assets/social-preview.png`.
- [ ] Upload `assets/social-preview.png` as the GitHub social preview.
- [x] Enable Discussions and private vulnerability reporting.
- [x] Push the reviewed changes, create tag `v1.0.0`, and verify the release workflow artifacts and checksum.

## Claude community submission

- [ ] Sign in to the Anthropic Console submission form.
- [ ] Submit the repository and the `knowledge-pack` plugin.
- [ ] Use Agent Fieldbook as the public display name.
- [ ] Include the listing copy, logo, release notes, launch narrative, and reviewer cases.
- [ ] Confirm `claude plugin validate` passes on the submitted commit.
- [ ] After approval, verify the pinned commit in the community catalog.

## OpenAI plugin submission

- [ ] Use an OpenAI Platform organization with Apps Management write access.
- [ ] Complete individual or business identity verification for the listed developer.
- [ ] Create a **Skills only** submission in the plugin portal.
- [ ] Upload the final ZIP, production logo, listing copy, three starter prompts, and reviewer cases.
- [ ] Select only countries where the publisher, support process, and terms are ready.
- [ ] Complete policy attestations after checking the final draft.
- [ ] After approval, publish from the portal and verify the directory listing in both ChatGPT and Codex.

Marketplace submission, account verification, social-preview upload, and final
publication approval require authenticated maintainer or reviewer action and are
not performed by repository validation.
