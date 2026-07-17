# Claude Power-User Knowledge Base

**Verifica delle fonti:** 17 luglio 2026  
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

| Categoria | Corso | Livello | Durata | Utilità |
|---|---|---|---|---|
| Fondamenti / AI Fluency | [AI Fluency for pK-12 Educators](https://anthropic.skilljar.com/path/ai-fluency-for-pk-12-educators) | Base | 1 hr | Metodo pratico per insegnanti pK-12 e uso responsabile dell’AI. |
| Fondamenti / AI Fluency | [AI Fluency for Builders](https://anthropic.skilljar.com/ai-fluency-for-builders) | Base–intermedio | 1 hr | Applica il framework AI Fluency alla costruzione di prodotti e workflow. |
| API / Platform | [Claude Platform 101](https://anthropic.skilljar.com/claude-platform-101) | Base | 1 hr | Orientamento iniziale alla piattaforma, Console e API Claude. |
| Business | [AI Fluency for Small Businesses](https://anthropic.skilljar.com/ai-fluency-for-small-businesses) | Base | 0.9 hr | Casi d’uso e metodo per integrare Claude in una piccola impresa. |
| Fondamenti / AI Fluency | [AI capabilities and limitations](https://anthropic.skilljar.com/ai-capabilities-and-limitations) | Base | 15 min | Capire capacità, limiti, errori e necessità di verifica. |
| Claude Code | [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) | Base | 1 hr | Primi passi con Claude Code, contesto di progetto e workflow di sviluppo. |
| Claude Code / Agenti | [Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents) | Intermedio | 20 min | Delegare attività in contesti isolati e progettare output strutturati. |
| Claude Cowork | [Introduction to Claude Cowork](https://anthropic.skilljar.com/introduction-to-claude-cowork) | Base | — | Introduzione alla delega di attività operative in Cowork. |
| Claude Code / Skills | [Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills) | Intermedio | 30 min | Creare Skill riutilizzabili con SKILL.md, riferimenti e script. |
| Fondamenti / AI Fluency | [AI Fluency: Framework & Foundations](https://anthropic.skilljar.com/ai-fluency-framework-foundations) | Base | 1.1 hr | Framework 4D: Delegation, Description, Discernment, Diligence. |
| Education | [AI Fluency for Educators](https://anthropic.skilljar.com/ai-fluency-for-educators) | Base | 24 min | Uso didattico e responsabile di Claude per educatori. |
| Education | [AI Fluency for Students](https://anthropic.skilljar.com/ai-fluency-for-students) | Base | 30 min | Metodo per studiare e collaborare con l’AI senza delegare il giudizio. |
| API / Platform | [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | Intermedio–avanzato | 8.1 hr | Corso completo su API, prompting, tool use, RAG, evals, MCP e agenti. |
| Claude Code | [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) | Intermedio | 1 hr | Workflow pratici end-to-end con Claude Code. |
| MCP / Agenti | [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) | Intermedio | 1 hr | Fondamenti MCP: server, client, strumenti, risorse e prompt. |
| MCP / Agenti | [Model Context Protocol: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) | Avanzato | 1.1 hr | Pattern avanzati, autenticazione, deployment e progettazione MCP. |
| API / Cloud | [Claude with Amazon Bedrock](https://anthropic.skilljar.com/claude-in-amazon-bedrock) | Intermedio–avanzato | 8 hr | Sviluppare con Claude tramite Amazon Bedrock. |
| API / Cloud | [Claude with Google Cloud's Vertex AI](https://anthropic.skilljar.com/claude-with-google-vertex) | Intermedio–avanzato | 8 hr | Sviluppare con Claude tramite Google Cloud Vertex AI. |
| Education | [Teaching AI Fluency](https://anthropic.skilljar.com/teaching-ai-fluency) | Intermedio | 36 min | Come insegnare il framework AI Fluency ad altri. |
| Nonprofit | [AI Fluency for nonprofits](https://anthropic.skilljar.com/ai-fluency-for-nonprofits) | Base | 54 min | Applicazioni pratiche e responsabili per organizzazioni nonprofit. |
| Claude.ai | [Claude 101](https://anthropic.skilljar.com/claude-101) | Base | 1 hr | Introduzione generale all’uso di Claude.ai. |

## Tutorial ufficiali selezionati e catalogati

| Categoria | Tutorial | Funzione | Obiettivo |
|---|---|---|---|
| AI literacy | [How AI gets its character](https://claude.com/resources/tutorials/how-ai-gets-its-character) | Modelli / comportamento | Capire come vengono modellati stile e comportamento dei sistemi AI |
| AI literacy | [Understanding knowledge gaps in AI models](https://claude.com/resources/tutorials/understanding-knowledge-gaps-in-ai-models) | Limiti / verifica | Riconoscere lacune di conoscenza e calibrare la fiducia |
| Claude.ai / Team | [Tasks to try with @Claude in your workspace](https://claude.com/resources/tutorials/tasks-to-try-with-claude-tag-in-your-workspace) | @Claude | Esempi di attività collaborative nei workspace |
| Claude.ai / Team | [Best practices using @Claude](https://claude.com/resources/tutorials/best-practices-using-claude-tag) | @Claude | Buone pratiche per menzioni, richieste e collaborazione |
| Claude Cowork | [Using Claude Cowork for legal question briefing](https://claude.com/resources/tutorials/using-claude-cowork-for-legal-question-briefing) | Cowork | Preparare briefing legali con fonti e controllo umano |
| Claude Cowork | [Using Claude Cowork for sales account research](https://claude.com/resources/tutorials/using-claude-cowork-for-sales-account-research) | Cowork | Delegare la ricerca commerciale e sintetizzare account |
| Claude Cowork | [Using Claude Cowork for marketing ops review](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review) | Cowork | Analizzare processi e materiali di marketing operations |
| Business | [Using Claude for your small business](https://claude.com/resources/tutorials/using-claude-for-your-small-business) | Claude.ai | Applicazioni operative per piccole imprese |
| Claude Cowork | [Delegating your first task in Claude Cowork](https://claude.com/resources/tutorials/delegating-your-first-task-in-claude-cowork) | Cowork | Impostare una prima delega ben definita |
| Claude Cowork | [Customize Claude Cowork](https://claude.com/resources/tutorials/customize-claude-cowork) | Cowork | Personalizzare modalità di lavoro e contesto |
| AI Fluency | [The 4 Ds of AI Fluency: behavioral indicators](https://claude.com/resources/tutorials/the-4-ds-of-ai-fluency-behavioral-indicators) | 4D framework | Usare indicatori osservabili per migliorare la collaborazione con l’AI |
| AI literacy | [What is sycophancy in AI models](https://claude.com/resources/tutorials/what-is-sycophancy-in-ai-models) | Limiti / verifica | Riconoscere risposte compiacenti e ridurre il bias di conferma |
| AI literacy | [Why do AI models hallucinate](https://claude.com/resources/tutorials/why-do-ai-models-hallucinate) | Limiti / verifica | Capire le allucinazioni e impostare verifiche |
| Design | [Using Claude Design for prototypes and UX](https://claude.com/resources/tutorials/using-claude-design-for-prototypes-and-ux) | Claude Design | Creare prototipi e supportare il processo UX |
| Design | [Using Claude Design for presentations and slide decks](https://claude.com/resources/tutorials/using-claude-design-for-presentations-and-slide-decks) | Claude Design | Produrre e iterare presentazioni |
| Agenti | [What is Claude managed agents](https://claude.com/resources/tutorials/what-is-claude-managed-agents) | Managed agents | Capire quando utilizzare agenti gestiti |
| Percorso consigliato | [Getting good at Claude: a research-backed curriculum](https://claude.com/resources/tutorials/getting-good-at-claude-a-research-backed-curriculum) | Claude.ai | Seguire un percorso progressivo basato sulla ricerca |
| Claude Code | [Using Claude Code Remote Control](https://claude.com/resources/tutorials/using-claude-code-remote-control) | Remote Control | Controllare sessioni Claude Code da remoto |
| Education | [Imagine with Claude: student guide](https://claude.com/resources/tutorials/imagine-with-claude-student-guide) | Claude.ai | Attività guidate per studenti |
| Claude.ai | [Choosing the right Claude model](https://claude.com/resources/tutorials/choosing-the-right-claude-model) | Modelli | Scegliere il modello in base a complessità, velocità e costo |
| Claude Cowork / Plugin | [How to customize plugins in Cowork](https://claude.com/resources/tutorials/how-to-customize-plugins-in-cowork) | Plugin | Adattare plugin esistenti ai propri workflow |
| Claude Cowork / Plugin | [How to build a plugin from scratch in Cowork](https://claude.com/resources/tutorials/how-to-build-a-plugin-from-scratch-in-cowork) | Plugin | Costruire un plugin Cowork da zero |
| Claude Code / Skills | [How skills compare to other Claude Code features](https://claude.com/resources/tutorials/how-skills-compare-to-other-claude-code-features) | Skills | Distinguere Skill, CLAUDE.md, subagent, MCP, hook e plugin |
| Claude Code / Skills | [What are skills](https://claude.com/resources/tutorials/what-are-skills) | Skills | Comprendere struttura e casi d’uso delle Skill |
| Claude Desktop | [Navigating the Claude desktop app](https://claude.com/resources/tutorials/navigating-the-claude-desktop-app) | Desktop app | Orientarsi nell’app desktop |
| Claude.ai | [Get the most from Claude Opus 4.6](https://claude.com/resources/tutorials/get-the-most-from-claude-opus-4-6) | Modelli | Sfruttare le capacità del modello Opus 4.6 |
| Excel | [Getting started with Claude in Excel](https://claude.com/resources/tutorials/getting-started-with-claude-in-excel) | Claude in Excel | Impostare l’integrazione e il primo workflow |
| Excel / Finance | [How to use Claude in Excel for accounting revenue model validation](https://claude.com/resources/tutorials/how-to-use-claude-in-excel-for-accounting-revenue-model-validation) | Claude in Excel | Validare modelli di ricavo e controlli contabili |
| Excel / HR | [How to use Claude in Excel for HR headcount planning](https://claude.com/resources/tutorials/how-to-use-claude-in-excel-for-hr-headcount-planning) | Claude in Excel | Analizzare e pianificare l’organico |
| Claude Code / GitHub | [Using the GitHub integration](https://claude.com/resources/tutorials/using-the-github-integration) | GitHub | Collegare repository e usare il contesto GitHub |

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
python -m pip install -U yt-dlp
python update_youtube_catalog.py         # elenco aggiornato
python update_youtube_catalog.py --archive  # + copia datata
```

Per trasformare un video in conoscenza consultabile: `python download_youtube_transcripts.py --category "Claude Code"`, poi sintetizzare ogni transcript con `VIDEO_KNOWLEDGE_CARD_PROMPT.md` seguendo `video_knowledge_card.schema.json`.

## Documentazione primaria

| Fonte | Uso |
|---|---|
| [Indice corsi ufficiali](https://claude.com/resources/courses) | Elenco aggiornato dei percorsi formativi Anthropic. |
| [Indice tutorial ufficiali](https://claude.com/resources/tutorials) | Guide operative e video lesson filtrabili. |
| [Risorse Claude Platform](https://platform.claude.com/docs/en/resources/overview) | Indice per documentazione, quickstart, cookbook, corsi e risorse ottimizzate per AI. |
| [Estendere Claude Code](https://code.claude.com/docs/en/features-overview) | Mappa decisionale tra CLAUDE.md, Skill, subagent, MCP, hook e plugin. |
| [Directory .claude](https://code.claude.com/docs/en/claude-directory) | Struttura canonica dei file di configurazione Claude Code. |
| [Subagents](https://code.claude.com/docs/en/sub-agents) | Creazione, isolamento del contesto e uso dei subagent. |
| [Claude Code docs per LLM](https://code.claude.com/docs/llms.txt) | Indice testuale della documentazione, utile per ingestion automatica. |
| [Che cosa sono le Skills](https://support.claude.com/en/articles/12512176-what-are-skills) | Differenze tra Skill, Project e connector. |
| [Usare le Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude) | Installazione, attivazione e uso delle Skills. |
| [Creare e gestire Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) | Knowledge base persistente e istruzioni di progetto. |
| [Directory Skills, connectors e plugins](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory) | Catalogo unificato delle estensioni. |
| [Getting started with connectors](https://claude.com/resources/tutorials/getting-started-with-connectors) | Collegare fonti e strumenti esterni. |

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

- Esegui `python update_youtube_catalog.py` per rigenerare il catalogo del canale.
- Controlla periodicamente gli indici `courses` e `tutorials`.
- Mantieni in alto la data dell’ultima verifica.
- Archivia i contenuti superati invece di mescolarli con le procedure correnti.
