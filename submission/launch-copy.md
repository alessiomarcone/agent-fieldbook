# Launch messaging

## Positioning

- **Category:** source-backed agent operating layer
- **Core promise:** make the practical lessons from official training available while the agent works
- **Primary audience:** Claude and Codex users who want current, product-correct project structures and reusable workflows
- **Contrast:** the agent does not have to improvise from general model knowledge, and the user does not have to finish every course before applying its lessons
- **Boundary:** independent synthesis, not an official product, course replacement, or transcript archive

## One-line options

**Primary tagline**

Expert training, turned into source-backed skills your agent can use while it works.

**GitHub description**

Source-backed skills that turn official Claude and Codex training into reliable daily workflows.

**Short pitch**

Agent Fieldbook converts publicly available official agent training and
documentation into focused skills that Claude and Codex can apply during real
work.

## Founder story — English

I kept running into the same contradiction while working with Claude.

I would ask it to structure a project and it would confidently choose a
reasonable combination of instruction files, skills, agents, or other
extensions. Then I would follow an official Anthropic course and discover that
the product was being taught differently: a different filename, a clearer
boundary between mechanisms, or a capability I had never encountered because
it was explained only in the course.

The knowledge existed. It just was not available at the moment Claude and I
were making the decision.

Agent Fieldbook closes that gap. It turns publicly available official courses,
tutorials, and documentation into concise, source-backed instructions that an
agent can use while it works. The goal is not to copy or replace the courses.
It is to make their practical lessons operational, link back to the originals,
and verify time-sensitive behavior against current documentation.

The project started with Claude. I added a separate Codex branch using the same
method and OpenAI sources, without pretending that the two products share
commands, manifests, permissions, or agent configuration.

## Storia del progetto — Italiano

Continuavo a incontrare la stessa contraddizione lavorando con Claude.

Gli chiedevo di strutturare un progetto e Claude sceglieva con sicurezza una
combinazione plausibile di file di istruzioni, skill, agenti o altre estensioni.
Poi seguivo un corso ufficiale Anthropic e scoprivo che il prodotto veniva
insegnato in modo diverso: un altro nome di file, un confine più preciso tra i
meccanismi, oppure una funzionalità che non avevo mai incontrato perché veniva
approfondita soltanto nel corso.

La conoscenza esisteva, ma non era disponibile nel momento in cui io e Claude
stavamo prendendo la decisione.

Agent Fieldbook nasce per colmare questo divario. Trasforma corsi, tutorial e
documentazione ufficiale pubblicamente disponibili in istruzioni concise e
supportate dalle fonti, utilizzabili dall'agente mentre lavora. Non copia e non
sostituisce i corsi: ne rende operative le lezioni pratiche, rimanda agli
originali e verifica sulla documentazione corrente tutto ciò che può cambiare.

Il progetto è nato da Claude. In seguito ho applicato lo stesso metodo a Codex,
con una sezione e fonti OpenAI separate, senza fingere che i due prodotti
condividano comandi, manifest, permessi o configurazioni degli agenti.

## Short launch post

Today I am open-sourcing **Agent Fieldbook**.

I built it after repeatedly seeing Claude choose a plausible project structure,
then learning a different current approach in an official Anthropic course.
The knowledge existed, but it was outside the task where the decision happened.

Agent Fieldbook turns official Claude and Codex learning resources into ten
source-backed skills for structure, prompting, verification, delegation,
plugins, and learning paths.

It is independent, multilingual, MIT licensed, and has no telemetry, accounts,
MCP server, or background runtime.

https://github.com/alessiomarcone/claude-knowledge-pack

## Post di lancio breve — Italiano

Oggi rendo open source **Agent Fieldbook**.

L'ho creato dopo aver visto più volte Claude scegliere una struttura di progetto
plausibile, per poi scoprire un approccio corrente diverso in un corso ufficiale
Anthropic. La conoscenza esisteva, ma restava fuori dal task in cui serviva.

Agent Fieldbook trasforma le risorse formative ufficiali di Claude e Codex in
dieci skill supportate dalle fonti per struttura, prompting, verifica, delega,
plugin e percorsi di apprendimento.

È indipendente, multilingue, MIT licensed e non contiene telemetria, account,
server MCP o processi in background.

https://github.com/alessiomarcone/claude-knowledge-pack

## Long launch post

Models are very good at producing a plausible answer. That does not guarantee
they will choose the current structure their own product team teaches.

While working with Claude, I often saw it make autonomous decisions about
instruction files, skills, subagents, hooks, or plugins. Later, an official
Anthropic course would explain a different filename, mechanism boundary, or
workflow. The lesson was useful, but it arrived after the project decision.

That is the problem Agent Fieldbook addresses: move the practical lessons from
official training into the moment of work.

The repository currently includes:

- ten focused Claude and Codex skills;
- separate product branches for commands, manifests, permissions, and agents;
- catalogs of 21 Anthropic courses, 30 tutorials, and 12 OpenAI learning resources;
- distilled knowledge cards with source, status, verification date, and license metadata;
- deterministic packaging and native validation for both plugin ecosystems.

It does not redistribute course lessons or transcripts, and it does not claim
to be an official Anthropic or OpenAI project. It is an execution companion:
apply the lesson now, inspect the source when needed, and verify anything that
may have changed.

## FAQ answers

### Does this replace the official courses?

No. It operationalizes selected practical lessons and links to the original
material. The courses remain the best place for full explanations and context.

### Is Agent Fieldbook official?

No. It is an independent community project. Its sources are official; the
project itself is not affiliated with or endorsed by Anthropic or OpenAI.

### Why not rely on the model's existing knowledge?

General model knowledge can be stale, incomplete, or imprecise about product
boundaries. Agent Fieldbook supplies focused instructions and requires current
documentation for time-sensitive claims.

### Why support both Claude and Codex?

The original problem appeared with Claude, but the method is portable. The
repository keeps product-specific details separate rather than translating
configuration by analogy.

### What code runs after installation?

None from the plugin itself. It contains skills and reference files only, with
no telemetry, authentication, MCP server, hook, or background process.
