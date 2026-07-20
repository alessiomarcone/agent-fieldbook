# Esempi di utilizzo

Scenari concreti, dal più semplice al più avanzato. Ogni esempio indica cosa scrivere e cosa aspettarsi.

---

## 1. Installare la Skill in Claude Code (2 minuti)

```bash
git clone https://github.com/alessiomarconebe2be-pixel/claude-knowledge-pack.git
cd claude-knowledge-pack

# Globale: disponibile in ogni sessione Claude Code
mkdir -p ~/.claude/skills
cp -R skill/claude-power-user ~/.claude/skills/

# Oppure per un solo progetto
mkdir -p /percorso/progetto/.claude/skills
cp -R skill/claude-power-user /percorso/progetto/.claude/skills/
cp CLAUDE.md /percorso/progetto/CLAUDE.md
```

Verifica: apri una sessione Claude Code e chiedi

> Quali skill hai disponibili?

`claude-power-user` deve comparire nell'elenco.

---

## 2. Fare domande sulle funzionalità di Claude

Con la Skill installata, domande come queste attivano automaticamente la knowledge base e ottengono risposte basate sulle fonti ufficiali, con link a corso o tutorial pertinente:

> Cos'è un subagent e quando conviene usarlo invece di una skill?

> Devo far ricordare a Claude le convenzioni del mio team: CLAUDE.md, Project o Skill?

> Come collego Claude ai dati live del mio CRM?

> Voglio automatizzare un controllo che scatti a ogni commit: hook o skill?

La Skill risponde seguendo il formato: **scelta consigliata → perché → procedura → prompt pronto → verifica → riutilizzo**.

---

## 3. Farsi consigliare un percorso di studio

> Non ho mai usato Claude Code. In che ordine dovrei seguire i corsi ufficiali? Ho circa 3 ore a settimana.

Claude attinge da `courses.csv` (livello + durata reali) e propone un percorso sequenziato, ad esempio: Claude Code 101 (1h) → Claude Code in Action (1h) → Introduction to agent skills (30 min) → Introduction to subagents (20 min).

Filtro manuale rapido, senza Claude:

```bash
# Solo corsi base, con durata
awk -F',' '$3 ~ /Base/ {print $2, "—", $4}' courses.csv
```

---

## 4. Configurare un Claude Project (claude.ai)

1. Su claude.ai crea un Project, es. **Claude Operating System**.
2. Carica come Project knowledge: `knowledge-base.md`, `courses.csv`, `tutorials.csv`, `youtube.md`, `sources.md`.
3. Incolla il contenuto di `claude-project-instructions.md` nelle istruzioni del Project.
4. Avvia la prima chat incollando `session-bootstrap-prompt.md`.

Da quel momento ogni chat del Project risponde su funzionalità Claude citando le fonti ufficiali invece di andare a memoria.

Esempio di richiesta nel Project:

> Il mio team vuole usare @Claude in Slack per il triage dei ticket. Preparami una procedura partendo dai tutorial ufficiali.

---

## 5. Aggiornare il catalogo YouTube

```bash
python -m pip install -U yt-dlp
python update_youtube_catalog.py            # genera youtube_videos.csv + .md
python update_youtube_catalog.py --archive  # conserva anche copia datata
```

Output: elenco completo dei video del canale ufficiale con link diretto, titolo, categoria, durata e data. I file generati non vanno committati (sono in `.gitignore`): lo script è il catalogo autorevole.

---

## 6. Trasformare un video in una knowledge card

Pipeline completa (uso personale — i transcript non vanno ridistribuiti):

```bash
# 1. Scarica i sottotitoli dei video di una categoria
python download_youtube_transcripts.py --category "Claude Code"

# 2. Apri Claude Code nella cartella e chiedi:
```

> Prendi il transcript in transcripts/<video>.md e produci una knowledge card seguendo video-knowledge-card-prompt.md, valida rispetto a video_knowledge_card.schema.json.

Risultato: scheda strutturata con procedura passo-passo, prompt riutilizzabili, errori da evitare e segnalazione delle informazioni potenzialmente superate. Salvala in `skill/claude-power-user/references/` per renderla parte della knowledge base.

---

## 7. Verificare che una funzione esista davvero

La Skill impone la regola anti-allucinazione: mai inventare funzioni, piani o limiti. Esempio:

> Claude può eseguire codice direttamente dentro un Artifact?

Risposta attesa: verifica sulla documentazione citata in `sources.md`, indicazione della data della fonte e — se l'informazione può essere cambiata — un passo di verifica esplicito invece di una risposta inventata.

---

## 8. Trasformare un workflow ricorrente in una Skill

Quando ripeti una procedura almeno due volte:

> Questa procedura di report settimanale l'ho già fatta tre volte. Trasformala in una Skill seguendo le regole della knowledge base.

Claude applica la regola di riuso: `SKILL.md` breve, materiale lungo in `references/`, script solo per i passaggi deterministici.
