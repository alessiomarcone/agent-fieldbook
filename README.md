# Claude Knowledge Pack

> **EN** — A ready-to-install knowledge base that teaches Claude to be used *the way Anthropic teaches it*: a structured catalog of the 21 official Skilljar courses and 30 official tutorials (with level, duration and direct links), an installable `claude-power-user` Skill for Claude Code, Project instructions for claude.ai, and a pipeline to keep the official YouTube channel catalog up to date. Content is in Italian; links point to official English sources. Contributions and translations welcome.

> **Disclaimer** — This is an **unofficial community project**, not affiliated with or endorsed by Anthropic. "Claude" and "Anthropic" are trademarks of Anthropic PBC. This repository contains only links and factual metadata (titles, durations, categories) pointing to official sources — no course content or video transcripts are redistributed here. The transcript download scripts are for **personal study use only**: do not commit or redistribute downloaded transcripts (they are copyrighted content).

Knowledge base pronta per **Claude Projects**, **Claude Code** e **Claude Skills**, costruita esclusivamente da fonti ufficiali Anthropic: corsi Skilljar, tutorial claude.com, documentazione e canale YouTube.

**➜ [Esempi di utilizzo pratici](EXAMPLES.md)** — installazione, domande tipo, percorsi di studio, setup Project, pipeline YouTube.

## Contenuto

- `knowledge-base.md` — mappa completa, learning path e link catalogati.
- `courses.csv` — 21 corsi ufficiali Claude/Anthropic.
- `tutorials.csv` — 30 tutorial ufficiali ad alta utilità operativa.
- `claude-project-instructions.md` — istruzioni da incollare in un Claude Project.
- `session-bootstrap-prompt.md` — prompt per una chat o sessione singola.
- `CLAUDE.md` — contesto essenziale per Claude Code.
- `skill/claude-power-user/` — Skill riutilizzabile.
- `youtube.md` — accesso al canale, ricerche tematiche e metodo di aggiornamento.
- `update_youtube_catalog.py` — genera l’elenco completo e aggiornato dei video.
- `download_youtube_transcripts.py` — scarica e ripulisce sottotitoli e auto-caption.
- `youtube-ingestion-workflow.md` — pipeline per trasformare i video in knowledge card.
- `video-knowledge-card-prompt.md` — prompt di sintesi controllata di ogni transcript.
- `video_knowledge_card.schema.json` — schema per schede strutturate.
- `sources.md` — fonti ufficiali primarie.

## Installazione in Claude Projects

1. Crea un Project dedicato, per esempio **Claude Operating System**.
2. Carica:
   - `knowledge-base.md`
   - `courses.csv`
   - `tutorials.csv`
   - `youtube.md`
   - `sources.md`
3. Copia il contenuto di `claude-project-instructions.md` nelle istruzioni del Project.
4. Avvia una chat usando `session-bootstrap-prompt.md`.

## Installazione come Skill in Claude

Carica o copia la cartella:

```text
skill/claude-power-user/
├── SKILL.md
└── references/
    ├── knowledge-base.md
    ├── sources.md
    ├── courses.csv / tutorials.csv / youtube.md
    └── cards/            ← regole e procedure distillate dai tutorial ufficiali
```

La Skill è pensata per attivarsi quando chiedi come usare Claude, scegliere una funzione, progettare un workflow o trasformarlo in una procedura riutilizzabile.

## Installazione in Claude Code

Nel progetto:

```bash
mkdir -p .claude/skills
cp -R skill/claude-power-user .claude/skills/
cp CLAUDE.md ./CLAUDE.md
```

## Aggiornamento automatico

Un workflow GitHub Actions (`.github/workflows/check-updates.yml`) controlla ogni lunedì:

- l'indice ufficiale dei corsi vs `courses.csv`;
- l'indice ufficiale dei tutorial vs `tutorials.csv`;
- il numero di video del canale YouTube ufficiale.

Se trova materiale non ancora catalogato apre una issue `source-update` con l'elenco. Controllo manuale in qualsiasi momento:

```bash
python check_official_sources.py
```

## Aggiornare il catalogo YouTube

```bash
python -m pip install -U yt-dlp
python update_youtube_catalog.py
```

Lo script produce link diretti, titolo, categoria, durata e data quando disponibili. L’opzione `--archive` conserva anche una copia datata.

Per acquisire la knowledge dei video:

```bash
python download_youtube_transcripts.py --category "Claude Code"
```

Poi elabora ogni transcript con `video-knowledge-card-prompt.md` e conserva la scheda nella cartella di reference appropriata.

## Strategia consigliata

Non riversare indiscriminatamente trascrizioni lunghe nel contesto. Mantieni:

- principi e criteri nelle istruzioni;
- procedure in Skill;
- materiali lunghi nelle reference;
- dati vivi tramite connector/MCP;
- elenco YouTube aggiornato tramite script.

## Limite noto

L’elenco completo dei singoli link YouTube non è congelato nel pacchetto perché il canale cambia e YouTube espone il feed in modo dinamico. Lo script è il catalogo autorevole e rigenerabile.
