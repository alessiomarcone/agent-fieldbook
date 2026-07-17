# Workflow di ingestion della knowledge YouTube

## Obiettivo

Trasformare il canale ufficiale Anthropic in una base consultabile da Claude senza saturare il contesto con centinaia di transcript grezzi.

## Pipeline

### 1. Aggiorna l’elenco

```bash
python -m pip install -U yt-dlp
python update_youtube_catalog.py --archive
```

### 2. Scarica i transcript

Tutto il canale:

```bash
python download_youtube_transcripts.py
```

Per iniziare da una categoria:

```bash
python download_youtube_transcripts.py --category "Claude Code"
python download_youtube_transcripts.py --category "Skills / Subagents / MCP / Agents"
```

Test su dieci video:

```bash
python download_youtube_transcripts.py --limit 10
```

### 3. Sintetizza un transcript per volta

Carica il transcript e usa `VIDEO_KNOWLEDGE_CARD_PROMPT.md`.

Non chiedere a Claude di sintetizzare l’intero canale in una sola sessione: la compressione eccessiva elimina procedure, eccezioni e segnali di obsolescenza.

### 4. Organizza le knowledge card

Struttura consigliata:

```text
knowledge-cards/
├── claude-ai/
├── claude-code/
├── skills-agents-mcp/
├── api-platform/
├── prompting-ai-fluency/
└── research-safety/
```

### 5. Riversa solo la knowledge giusta

- **Project Instructions / CLAUDE.md:** principi stabili e criteri decisionali.
- **Skill:** procedure ricorrenti, trigger, controlli e output.
- **References:** spiegazioni, esempi, knowledge card e fonti.
- **Connector/MCP:** fonti che devono rimanere vive e aggiornate.
- **Archive:** procedure riferite a UI, modelli o prodotti superati.

### 6. Aggiornamento incrementale

Confronta il nuovo `youtube_videos.csv` con la copia archiviata. Elabora soltanto i nuovi Video ID. Quando un nuovo contenuto contraddice una scheda precedente:

1. conserva la vecchia scheda in `archive/`;
2. aggiorna `knowledge_checked`;
3. spiega cosa è cambiato;
4. aggiorna Skill e istruzioni solo quando il cambiamento è stabile.

## Ordine di ingestion consigliato

1. AI Fluency e limiti
2. Claude.ai e Projects
3. Skills
4. Claude Code
5. Subagents
6. MCP e connectors
7. API e tool use
8. Artifacts, Design, Excel e Cowork
9. Research e safety
10. Eventi e customer stories
