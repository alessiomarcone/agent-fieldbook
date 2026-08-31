# Claude Power-User Knowledge Base

**Verifica delle fonti:** cataloghi corsi/tutorial e raggiungibilità dei link 31 agosto 2026; sezioni di documentazione 21 luglio 2026
**Ambito:** materiali ufficiali Anthropic/Claude, corsi, tutorial, documentazione e canale YouTube.

## Come usare questa base

Questa raccolta non va trattata come un manuale da incollare interamente in ogni chat. Usa il livello corretto:

1. **Claude Project** — conoscenza persistente per un tema o progetto.
2. **Project Instructions / `CLAUDE.md`** — regole stabili, convenzioni e criteri decisionali.
3. **Skill** — procedura riutilizzabile che Claude carica solo quando serve.
4. **Connector / MCP** — accesso a dati e azioni esterne.
5. **Subagent** — attività parallela o lunga che richiede un contesto isolato.
6. **Hook** — automazione deterministica attivata da un evento.
7. **Plugin** — pacchetto distribuibile che riunisce più estensioni.

## Mappa decisionale

| Esigenza | Strumento consigliato | Motivo |
|---|---|---|
| Claude deve ricordare documenti e contesto del progetto | Project knowledge | Le fonti restano disponibili nelle chat del progetto |
| Claude deve seguire sempre poche regole | Project Instructions / `CLAUDE.md` | Contesto persistente, breve e ad alta priorità |
| Una procedura ricorre spesso | Skill | Caricamento on demand, meno rumore nel contesto |
| Servono dati aggiornati o azioni in altri servizi | Connector / MCP | Collega fonti e strumenti esterni |
| Un’attività complessa deve restare separata | Subagent | Contesto isolato e restituzione di una sintesi |
| Un controllo deve scattare sempre a un evento | Hook | Comportamento deterministico |
| Il workflow deve essere condiviso/installato | Plugin | Distribuzione di Skill, agenti, hook e MCP |

## Percorso essenziale consigliato

### 1. Fondamenti
- **Claude 101**
- **AI capabilities and limitations**
- **AI Fluency: Framework & Foundations**
- Tutorial: **Getting good at Claude**
- Tutorial: **Choosing the right Claude model**

### 2. Uso quotidiano e qualità degli output
- Applica le **4D**:
  - **Delegation** — definisci cosa delegare e cosa resta sotto il tuo controllo.
  - **Description** — fornisci obiettivo, contesto, criteri e formato.
  - **Discernment** — valuta criticamente risultati, fonti e assunzioni.
  - **Diligence** — verifica, documenta e usa l’AI responsabilmente.
- Crea un Project per ogni dominio stabile.
- Trasforma i workflow ripetuti in Skill.
- Usa connector/MCP quando la fonte deve rimanere aggiornata.

### 3. Claude Code
Ordine: **Claude Code 101 → Claude Code in Action → Introduction to agent skills → Introduction to subagents → MCP**.

### 4. API e agenti
Ordine: **Claude Platform 101 → Building with the Claude API → Introduction to MCP → MCP Advanced Topics**.

## Corsi ufficiali

<!-- catalog:courses:start -->
| Categoria | Corso | Livello | Durata | Lezioni | Utilità |
|---|---|---|---|---|---|
| Fondamenti / AI Fluency | [AI Fluency for pK-12 Educators](https://academy.claude.com/courses/ai-fluency-for-k-12-educators) | Base | 3 hr | 10 | Metodo pratico per insegnanti pK-12 e uso responsabile dell’AI. |
| Fondamenti / AI Fluency | [AI Fluency for Builders](https://academy.claude.com/courses/ai-fluency-for-builders) | Base–intermedio | 3 hr | 9 | Applica il framework AI Fluency alla costruzione di prodotti e workflow. |
| API / Platform | [Claude Platform 101](https://academy.claude.com/courses/claude-platform-101) | Base | 1.5 hr | 13 | Orientamento iniziale alla piattaforma, Console e API Claude. |
| Business | [AI Fluency for Small Businesses](https://academy.claude.com/courses/ai-fluency-for-small-businesses) | Base | 4 hr | 9 | Casi d’uso e metodo per integrare Claude in una piccola impresa. |
| Fondamenti / AI Fluency | [AI capabilities and limitations](https://academy.claude.com/courses/ai-capabilities-and-limitations) | Base | 3.5 hr | 13 | Capire capacità, limiti, errori e necessità di verifica. |
| Claude Code | [Claude Code 101](https://academy.claude.com/courses/claude-code-101) | Base | 1.5 hr | 12 | Primi passi con Claude Code, contesto di progetto e workflow di sviluppo. |
| Claude Code / Agenti | [Introduction to subagents](https://academy.claude.com/courses/introduction-to-subagents) | Intermedio | 45 min | 4 | Delegare attività in contesti isolati e progettare output strutturati. |
| Claude Cowork | [Introduction to Claude Cowork](https://academy.claude.com/courses/introduction-to-claude-cowork) | Base | 2.5 hr | 14 | Introduzione alla delega di attività operative in Cowork. |
| Claude Code / Skills | [Introduction to agent skills](https://academy.claude.com/courses/introduction-to-agent-skills) | Intermedio | 1 hr | 6 | Creare Skill riutilizzabili con SKILL.md, riferimenti e script. |
| Fondamenti / AI Fluency | [AI Fluency: Framework & Foundations](https://academy.claude.com/courses/ai-fluency-framework-foundations) | Base | 4 hr | 14 | Framework 4D: Delegation, Description, Discernment, Diligence. |
| Education | [AI Fluency for Educators](https://academy.claude.com/courses/ai-fluency-for-educators) | Base | 1.5 hr | 4 | Uso didattico e responsabile di Claude per educatori. |
| Education | [AI Fluency for Students](https://academy.claude.com/courses/ai-fluency-for-students) | Base | 3 hr | 5 | Metodo per studiare e collaborare con l’AI senza delegare il giudizio. |
| API / Platform | [Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api) | Intermedio–avanzato | 9 hr | 67 | Corso completo su API, prompting, tool use, RAG, evals, MCP e agenti. |
| Claude Code | [Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action) | Intermedio | 1 hr | 9 | Workflow pratici end-to-end con Claude Code. |
| MCP / Agenti | [Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol) | Intermedio | 1 hr | 10 | Fondamenti MCP: server, client, strumenti, risorse e prompt. |
| MCP / Agenti | [Model Context Protocol: Advanced Topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics) | Avanzato | 1.5 hr | 11 | Pattern avanzati, autenticazione, deployment e progettazione MCP. |
| API / Cloud | [Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock) | Intermedio–avanzato | 8 hr | 65 | Sviluppare con Claude tramite Amazon Bedrock. |
| API / Cloud | [Claude with Google Cloud's Vertex AI](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai) | Intermedio–avanzato | 8.5 hr | 66 | Sviluppare con Claude tramite Google Cloud Vertex AI. |
| Education | [Teaching AI Fluency](https://academy.claude.com/courses/teaching-ai-fluency) | Intermedio | 4.5 hr | 7 | Come insegnare il framework AI Fluency ad altri. |
| Nonprofit | [AI Fluency for nonprofits](https://academy.claude.com/courses/ai-fluency-for-nonprofits) | Base | 4 hr | 9 | Applicazioni pratiche e responsabili per organizzazioni nonprofit. |
| Claude.ai | [Claude 101](https://academy.claude.com/courses/claude-101) | Base | 2.5 hr | 13 | Introduzione generale all’uso di Claude.ai. |
| Fondamenti / AI Fluency | [AI Fluency for Creative Work](https://academy.claude.com/courses/ai-fluency-for-creative-work) | Base–intermedio | 5 hr | 8 | Decidere in modo intenzionale dove usare l’AI nel lavoro creativo senza perdere la propria firma. |
| Education | [AI Fluency for pK-12 Train the Trainer](https://academy.claude.com/courses/ai-fluency-for-pk-12-train-the-trainer) | Intermedio | 45 min | 4 | Kit di workshop pronto all’uso per formare altri docenti pK-12 sul framework 4D. |
| Claude Code | [The AI-Native SDLC Playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook) | Intermedio–avanzato | 1 hr | 14 | Ridisegnare planning, review, test e deploy quando gran parte del codice la scrivono gli agenti. |
| Business | [Deploying Claude Enterprise with Confidence](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence) | Intermedio | 2.5 hr | 14 | Le cinque decisioni che definiscono un rollout enterprise: struttura e identità, accessi, governance, spesa, visibilità. |
<!-- catalog:courses:end -->

## Tutorial ufficiali selezionati e catalogati

<!-- catalog:tutorials:start -->
| Categoria | Tutorial | Funzione | Obiettivo |
|---|---|---|---|
| Claude.ai / Team | [Tasks to try with @Claude in your workspace](https://academy.claude.com/tutorials/tasks-to-try-with-claude-tag-in-your-workspace) | @Claude | Esempi di attività collaborative nei workspace |
| Claude.ai / Team | [Best practices using @Claude](https://academy.claude.com/tutorials/best-practices-using-claude-tag) | @Claude | Buone pratiche per menzioni, richieste e collaborazione |
| Claude Cowork | [Using Claude Cowork for legal question briefing](https://academy.claude.com/tutorials/using-claude-cowork-for-legal-question-briefing) | Cowork | Preparare briefing legali con fonti e controllo umano |
| Claude Cowork | [Using Claude Cowork for sales account research](https://academy.claude.com/tutorials/using-claude-cowork-for-sales-account-research) | Cowork | Delegare la ricerca commerciale e sintetizzare account |
| Claude Cowork | [Using Claude Cowork for marketing ops review](https://academy.claude.com/tutorials/using-claude-cowork-for-marketing-ops-review) | Cowork | Analizzare processi e materiali di marketing operations |
| Business | [Using Claude for your small business](https://academy.claude.com/tutorials/using-claude-for-your-small-business) | Claude.ai | Applicazioni operative per piccole imprese |
| Claude Cowork | [Delegating your first task in Claude Cowork](https://academy.claude.com/tutorials/delegating-your-first-task-in-claude-cowork) | Cowork | Impostare una prima delega ben definita |
| Claude Cowork | [Customize Claude Cowork](https://academy.claude.com/tutorials/customize-claude-cowork) | Cowork | Personalizzare modalità di lavoro e contesto |
| AI Fluency | [The 4 Ds of AI Fluency: behavioral indicators](https://academy.claude.com/tutorials/the-4-ds-of-ai-fluency-behavioral-indicators) | 4D framework | Usare indicatori osservabili per migliorare la collaborazione con l’AI |
| AI literacy | [What is sycophancy in AI models](https://academy.claude.com/tutorials/what-is-sycophancy-in-ai-models) | Limiti / verifica | Riconoscere risposte compiacenti e ridurre il bias di conferma |
| AI literacy | [Why do AI models hallucinate](https://academy.claude.com/tutorials/why-do-ai-models-hallucinate) | Limiti / verifica | Capire le allucinazioni e impostare verifiche |
| Design | [Using Claude Design for prototypes and UX](https://academy.claude.com/tutorials/using-claude-design-for-prototypes-and-ux) | Claude Design | Creare prototipi e supportare il processo UX |
| Design | [Using Claude Design for presentations and slide decks](https://academy.claude.com/tutorials/using-claude-design-for-presentations-and-slide-decks) | Claude Design | Produrre e iterare presentazioni |
| Agenti | [What is Claude managed agents](https://academy.claude.com/tutorials/what-is-claude-managed-agents) | Managed agents | Capire quando utilizzare agenti gestiti |
| Percorso consigliato | [Getting good at Claude: a research-backed curriculum](https://academy.claude.com/tutorials/getting-good-at-claude-a-research-backed-curriculum) | Claude.ai | Seguire un percorso progressivo basato sulla ricerca |
| Claude Code | [Using Claude Code Remote Control](https://academy.claude.com/tutorials/using-claude-code-remote-control) | Remote Control | Controllare sessioni Claude Code da remoto |
| Education | [Imagine with Claude: student guide](https://academy.claude.com/tutorials/imagine-with-claude-student-guide) | Claude.ai | Attività guidate per studenti |
| Claude.ai | [Choosing the right Claude model](https://academy.claude.com/tutorials/choosing-the-right-claude-model) | Modelli | Scegliere il modello in base a complessità, velocità e costo |
| Claude Cowork / Plugin | [How to customize plugins in Cowork](https://academy.claude.com/tutorials/how-to-customize-plugins-in-cowork) | Plugin | Adattare plugin esistenti ai propri workflow |
| Claude Cowork / Plugin | [How to build a plugin from scratch in Cowork](https://academy.claude.com/tutorials/how-to-build-a-plugin-from-scratch-in-cowork) | Plugin | Costruire un plugin Cowork da zero |
| Claude Code / Skills | [How skills compare to other Claude Code features](https://academy.claude.com/tutorials/how-skills-compare-to-other-claude-code-features) | Skills | Distinguere Skill, CLAUDE.md, subagent, MCP, hook e plugin |
| Claude Code / Skills | [What are skills](https://academy.claude.com/tutorials/what-are-skills) | Skills | Comprendere struttura e casi d’uso delle Skill |
| Claude Desktop | [Navigating the Claude desktop app](https://academy.claude.com/tutorials/navigating-the-claude-desktop-app) | Desktop app | Orientarsi nell’app desktop |
| Excel | [Getting started with Claude in Excel](https://academy.claude.com/tutorials/getting-started-with-claude-in-excel) | Claude in Excel | Impostare l’integrazione e il primo workflow |
| Excel / Finance | [How to use Claude in Excel for accounting revenue model validation](https://academy.claude.com/tutorials/how-to-use-claude-in-excel-for-accounting-revenue-model-validation) | Claude in Excel | Validare modelli di ricavo e controlli contabili |
| Excel / HR | [How to use Claude in Excel for HR headcount planning](https://academy.claude.com/tutorials/how-to-use-claude-in-excel-for-hr-headcount-planning) | Claude in Excel | Analizzare e pianificare l’organico |
| AI Fluency | [A discussion guide for the AI Fluency Index](https://academy.claude.com/tutorials/a-discussion-guide-for-the-ai-fluency-index) | AI Fluency Index | Guidare una discussione interna sull’AI fluency del team |
| PowerPoint | [Building a PowerPoint with Claude](https://academy.claude.com/tutorials/building-a-powerpoint-with-claude) | Claude in PowerPoint | Generare una presentazione da zero senza uscire da PowerPoint |
| AI literacy | [Can you trust what AI tells you?](https://academy.claude.com/tutorials/can-you-trust-what-ai-tells-you) | Limiti / verifica | Valutare quanto fidarsi di una risposta ben scritta e sicura di sé |
| Claude Cowork | [Choosing between Claude Cowork or Chat](https://academy.claude.com/tutorials/choosing-between-claude-cowork-or-chat) | Cowork | Scegliere tra conversazione guidata turno per turno e delega di un obiettivo |
| Claude Code | [Choosing the right effort level in Claude Code](https://academy.claude.com/tutorials/choosing-the-right-effort-level-in-claude-code) | Effort | Regolare le risorse spese per task e capire quando alzarle o abbassarle |
| Claude.ai / Team | [Claude Cowork Enterprise Admin Guide](https://academy.claude.com/tutorials/claude-cowork-enterprise-administrator-guide) | Amministrazione | Configurare e governare Cowork a livello enterprise |
| Claude.ai / Team | [Claude Enterprise Administrator Guide](https://academy.claude.com/tutorials/claude-enterprise-administrator-guide) | Amministrazione | Le quattro fasi di un deployment enterprise, dal setup tecnico alla scala |
| Education | [Claude for Teachers in action](https://academy.claude.com/tutorials/claude-for-teachers-in-action) | Claude for Teachers | Vedere un uso reale e ricorrente di Claude nella pratica didattica |
| Claude Code / Skills | [Configuration and multi-file skills](https://academy.claude.com/tutorials/configuration-and-multi-file-skills) | Skills | Configurare skill e strutturarle su più file |
| Claude.ai | [Connect your tools to unlock a smarter, more capable AI companion](https://academy.claude.com/tutorials/connect-your-tools-to-unlock-a-smarter-more-capable-ai-companion) | Connettori | Collegare app di terze parti per dare a Claude accesso ai dati |
| Claude.ai | [Create and edit files with Claude to eliminate hours of busy work](https://academy.claude.com/tutorials/create-and-edit-files-with-claude-to-eliminate-hours-of-busy-work) | File | Far creare e modificare a Claude fogli, documenti, slide e PDF |
| Claude Code / Skills | [Creating your first skill](https://academy.claude.com/tutorials/creating-your-first-skill) | Skills | Creare la prima skill dal setup all’esecuzione |
| Claude Cowork | [Delegating and scheduling tasks in Claude Cowork](https://academy.claude.com/tutorials/delegating-and-scheduling-tasks-in-claude-cowork) | Cowork | Delegare lavoro multi-step e pianificarlo nel tempo |
| Claude Cowork | [Get started in Claude Cowork in three steps](https://academy.claude.com/tutorials/get-started-in-claude-cowork-in-three-steps) | Cowork | I tre passi di setup prima del primo task |
| Claude.ai | [Getting started with Claude.ai](https://academy.claude.com/tutorials/getting-started-with-claude-ai) | Claude.ai | Prompting, upload, ricerca e funzioni avanzate di Claude.ai |
| Sicurezza | [Getting started with Claude Security](https://academy.claude.com/tutorials/getting-started-with-claude-security) | Claude Security | Primi passi con le funzioni di sicurezza di Claude |
| Claude.ai | [Getting started with connectors](https://academy.claude.com/tutorials/getting-started-with-connectors) | Connettori | Configurare connettori verso file, app e workflow |
| Claude.ai | [How to choose between Claude's Voice Mode and Dictation](https://academy.claude.com/tutorials/how-to-choose-between-voice-mode-and-dictation) | Voce | Capire quando serve voice mode e quando basta la dettatura |
| Claude Code / Skills | [How to create a skill with Claude through conversation](https://academy.claude.com/tutorials/how-to-create-a-skill-with-claude-through-conversation) | Skills | Far strutturare a Claude una skill descrivendo il workflow a parole |
| Claude.ai / Team | [How to enable Claude Code for your Enterprise team](https://academy.claude.com/tutorials/how-to-enable-claude-code-for-your-enterprise-team) | Amministrazione | Aggiungere seat Claude Code al piano enterprise con controllo di spesa |
| Business | [How to install and use the Claude for Small Business plugin](https://academy.claude.com/tutorials/how-to-install-the-claude-for-small-business-plugin) | Plugin | Installare e adattare il plugin alla propria piccola impresa |
| Claude.ai | [How to select the right effort setting for Claude Cowork and Chat](https://academy.claude.com/tutorials/how-to-select-the-right-effort-setting-for-claude-cowork-and-chat) | Effort | Regolare l’effort su un modello di frontiera invece di scendere di modello |
| Claude.ai | [Intro to Projects](https://academy.claude.com/tutorials/intro-to-projects) | Projects | Organizzare conversazioni e contesto ricorrente in Projects |
| AI literacy | [How context affects Claude's performance and cost](https://academy.claude.com/tutorials/parametric-memory-and-context) | Contesto / costi | Distinguere ciò che il modello sa per training da ciò che sta nel contesto |
| Design | [Prototype AI-Powered Apps with Claude artifacts](https://academy.claude.com/tutorials/prototype-ai-powered-apps-with-claude-artifacts) | Artifacts | Prototipare app AI senza gestire chiavi API |
| PowerPoint | [Refining a PowerPoint with Claude](https://academy.claude.com/tutorials/refining-a-powerpoint-with-claude) | Claude in PowerPoint | Rifinire slide esistenti dalla chat integrata |
| Claude Cowork | [Scaling workflows with Claude Cowork at your organization](https://academy.claude.com/tutorials/scaling-workflows-with-claude-cowork-at-your-organization) | Cowork | Playbook per estendere Cowork a tutta l’organizzazione |
| Claude Code / Skills | [Sharing skills](https://academy.claude.com/tutorials/sharing-skills) | Skills | Condividere skill con il team e con la community |
| Claude.ai | [Simplify your browsing experience with Claude in Chrome](https://academy.claude.com/tutorials/simplify-your-browsing-experience-with-claude-for-chrome) | Claude in Chrome | Far lavorare Claude nel browser con contesto visivo |
| Claude Code / Skills | [Teach Claude your way of working using skills](https://academy.claude.com/tutorials/teach-claude-your-way-of-working-using-skills) | Skills | Impacchettare metodi di lavoro riusabili tra conversazioni |
| AI Fluency | [The 4 Properties of AI](https://academy.claude.com/tutorials/the-4-properties-of-ai) | 4 proprietà | Riferimento rapido su cosa rende l’AI capace in alcuni contesti e limitata in altri |
| AI Fluency | [Anthropic Education Report: The AI Fluency Index](https://academy.claude.com/tutorials/the-ai-fluency-index) | AI Fluency Index | Gli 11 comportamenti osservabili che misurano la collaborazione con l’AI |
| AI literacy | [Tokens: why some inputs cost more than others](https://academy.claude.com/tutorials/tokens-and-embeddings) | Token / costi | Capire l’unità di misura di consumo, costo e rate limit |
| Claude Code / Skills | [Troubleshooting skills](https://academy.claude.com/tutorials/troubleshooting-skills) | Skills | Diagnosticare errori di configurazione e comportamenti inattesi |
| Design | [Use artifacts to visualize and create AI apps without ever writing a line of code](https://academy.claude.com/tutorials/use-artifacts-to-visualize-and-create-ai-apps-without-ever-writing-a-line-of-code) | Artifacts | Costruire, personalizzare e condividere mini-app senza scrivere codice |
| Claude.ai | [Using Research](https://academy.claude.com/tutorials/using-research) | Research | Usare la funzione Research per attività di pianificazione |
| AI literacy | [What does AI know about me?](https://academy.claude.com/tutorials/what-does-ai-know-about-me) | Privacy | Capire cosa il sistema sa davvero di chi lo usa |
| AI literacy | [What happens when you talk to AI?](https://academy.claude.com/tutorials/what-happens-when-you-talk-to-ai) | Modelli | Cosa succede sotto il cofano tra l’invio del messaggio e la risposta |
| AI literacy | [Why does bias exist in AI models?](https://academy.claude.com/tutorials/why-does-bias-exist-in-ai-models) | Limiti / verifica | Riconoscere il bias nelle proprie conversazioni e come mitigarlo |
| PowerPoint | [Working smarter with Claude in PowerPoint](https://academy.claude.com/tutorials/working-smarter-with-claude-in-powerpoint) | Claude in PowerPoint | Portare dati esterni nel deck e analizzarli senza uscirne |
| AI Fluency | [Writing an AI diligence statement](https://academy.claude.com/tutorials/writing-an-ai-diligence-statement) | Diligence | Dichiarare in modo trasparente e specifico l’uso di AI nel proprio lavoro |
<!-- catalog:tutorials:end -->

## Canale YouTube ufficiale

**Canale:** https://www.youtube.com/@anthropic-ai
**Video:** https://www.youtube.com/@anthropic-ai/videos
**Playlist:** https://www.youtube.com/@anthropic-ai/playlists
**Channel ID:** `UCrDwWp7EBBv4NwvScIpBDOA`

### Ricerche rapide nel canale

| Argomento | Link ricerca |
|---|---|
| Claude Code | https://www.youtube.com/@anthropic-ai/search?query=Claude%20Code |
| Skills | https://www.youtube.com/@anthropic-ai/search?query=Skills |
| Subagents | https://www.youtube.com/@anthropic-ai/search?query=subagents |
| MCP | https://www.youtube.com/@anthropic-ai/search?query=MCP |
| API | https://www.youtube.com/@anthropic-ai/search?query=API |
| Agents | https://www.youtube.com/@anthropic-ai/search?query=agents |
| Claude.ai | https://www.youtube.com/@anthropic-ai/search?query=Claude.ai |
| Prompting | https://www.youtube.com/@anthropic-ai/search?query=prompt |
| Artifacts | https://www.youtube.com/@anthropic-ai/search?query=Artifacts |
| Research e safety | https://www.youtube.com/@anthropic-ai/search?query=safety |

### Categorie prodotte dall'updater

1. Claude Code
2. Skills / Subagents / MCP / Agents
3. API / Developer Platform
4. Claude.ai / Productivity / Artifacts
5. AI Fluency / Prompting
6. Research / Safety
7. Eventi / Interviste / Customer stories
8. Altro

### Perché il catalogo è generato, non congelato

YouTube carica dinamicamente l'archivio e può bloccare l'estrazione automatica in alcuni ambienti. Un elenco statico di link `watch` invecchierebbe rapidamente ed è per questo che non è incluso qui riga per riga. Lo script `update_youtube_catalog.py` interroga il feed del canale tramite `yt-dlp`, ricostruisce tutti i link, assegna una categoria e genera `youtube_videos.csv` / `youtube_videos.md` aggiornati.

```bash
python3 -m pip install -U yt-dlp
python3 update_youtube_catalog.py         # elenco aggiornato
python3 update_youtube_catalog.py --archive  # + copia datata
```

Per trasformare un video in conoscenza consultabile: `python3 download_youtube_transcripts.py --category "Claude Code"`, poi sintetizzare ogni transcript con `knowledge-card-prompt.md` seguendo `knowledge-card.schema.json`.

## Documentazione primaria

| Fonte | Uso |
|---|---|
| [Indice corsi ufficiali](https://academy.claude.com/courses) | Elenco aggiornato dei percorsi formativi Anthropic. |
| [Indice tutorial ufficiali](https://academy.claude.com/tutorials) | Guide operative e video lesson filtrabili. |
| [Risorse Claude Platform](https://platform.claude.com/docs/en/resources/overview) | Indice per documentazione, quickstart, cookbook, corsi e risorse ottimizzate per AI. |
| [Estendere Claude Code](https://code.claude.com/docs/en/features-overview) | Mappa decisionale tra CLAUDE.md, Skill, subagent, MCP, hook e plugin. |
| [Directory .claude](https://code.claude.com/docs/en/claude-directory) | Struttura canonica dei file di configurazione Claude Code. |
| [Subagents](https://code.claude.com/docs/en/sub-agents) | Creazione, isolamento del contesto e uso dei subagent. |
| [Claude Code docs per LLM](https://code.claude.com/docs/llms.txt) | Indice testuale della documentazione, utile per ingestion automatica. |
| [Che cosa sono le Skills](https://support.claude.com/en/articles/12512176-what-are-skills) | Differenze tra Skill, Project e connector. |
| [Usare le Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude) | Installazione, attivazione e uso delle Skills. |
| [Creare e gestire Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) | Knowledge base persistente e istruzioni di progetto. |
| [Directory Skills, connectors e plugins](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory) | Catalogo unificato delle estensioni. |
| [Getting started with connectors](https://academy.claude.com/tutorials/getting-started-with-connectors) | Collegare fonti e strumenti esterni. |

## Knowledge card distillate dai tutorial

Il contenuto operativo dei tutorial ufficiali è stato estratto e distillato in card (sintesi 2026-07-20, cartella `cards/`):

| Card | Copre |
|---|---|
| `cards/regole-distillate.md` | **Leggi prima questa**: 11 regole universali, scelta modello, scelta interfaccia, gerarchia strumenti, errori ricorrenti |
| `cards/claude-tag-workspace.md` | @Claude in Slack/Teams: delega nei canali, memoria, prompt pronti, checklist |
| `cards/cowork.md` | Cowork: prima delega, pattern skill→schedule→verifica, casi legale/sales/marketing/PMI |
| `cards/plugin-building.md` | Plugin Cowork: personalizzazione, costruzione da zero, distribuzione |
| `cards/claude-excel.md` | Excel: pattern struttura→errori→fix con permesso→estensione |
| `cards/claude-design.md` | Design: prototipi da codebase, handoff a Claude Code, presentazioni |
| `cards/ai-fluency-curriculum.md` | Curriculum research-backed, mosse firma, check di discernimento, regole modelli recenti |
| `cards/ai-fluency-4d-corso.md` | Corso Framework & Foundations completo: le 4D con sotto-competenze + 6 tecniche di prompting |
| `cards/ai-literacy.md` | Carattere del modello, gap di conoscenza, sycophancy, allucinazioni: cause e contromisure |
| `cards/claude-code-estensioni.md` | Skill vs CLAUDE.md vs subagent vs hook vs MCP; remote control |
| `cards/managed-agents.md` | API Managed Agents: sessioni, environment, rubric, memoria, multi-agent |
| `cards/desktop-app.md` | Chat vs Cowork vs Code: matrice di decisione e procedure |
| `cards/pending-video-ingestion.md` | Stato ingestione transcript (9/11 tutorial video completati) |

## Principi operativi da riversare nelle sessioni

### Prompt minimo ad alta qualità
Ogni richiesta importante dovrebbe contenere:

- **Obiettivo:** risultato finale e destinatario.
- **Contesto:** dati, vincoli, esempi e fonti disponibili.
- **Criteri di successo:** cosa rende l’output accettabile.
- **Processo:** verifiche o passaggi obbligatori.
- **Formato:** struttura, lunghezza, lingua, file o schema.
- **Confini:** cosa non inventare e quando dichiarare incertezza.

### Regola per la conoscenza
- La documentazione ufficiale è fonte primaria.
- I video sono materiale esplicativo, non necessariamente la versione più aggiornata.
- Quando una funzione può essere cambiata, Claude deve controllare la data e segnalare il rischio di obsolescenza.
- Non dedurre la disponibilità di una funzione dal solo nome del modello o dal piano: verificare la documentazione corrente.

### Regola per il riuso
Quando una procedura viene eseguita almeno due volte:
1. estrarre il processo;
2. separare istruzioni da esempi e reference;
3. creare una Skill;
4. mantenere `SKILL.md` breve;
5. spostare materiale lungo in `references/`;
6. includere script solo per passaggi deterministici.

## Aggiornamento

Il controllo è automatico ogni lunedì (`.github/workflows/check-updates.yml`);
questi comandi servono per chiuderne il risultato o per una verifica manuale.

1. `python3 check_official_sources.py` — confronta la sitemap di Claude Academy
   con i cataloghi e verifica che ogni URL catalogato risponda ancora.
2. Modifica `courses.csv` o `tutorials.csv`: sono l’unica fonte di verità.
3. `python3 scripts/render_catalog.py` — rigenera le tabelle qui sopra dai CSV.
   Non modificarle a mano: sono racchiuse tra marcatori `catalog:*` e vengono
   sovrascritte.
4. `python3 update_youtube_catalog.py` per rigenerare il catalogo del canale.
5. `python3 scripts/sync_pack.py`, poi aggiorna conteggi e `verified_on` in
   `manifest.json` e chiudi con `make check`.

Cosa entra nel catalogo è dichiarato in `catalog-scope.json`. Le voci ritirate
da Anthropic si registrano in `retired-sources.md` invece di sparire, così una
card che le cita resta tracciabile.

Un audit più vecchio di 45 giorni fa fallire `make check`: la data in
`manifest.json` non è decorativa.
