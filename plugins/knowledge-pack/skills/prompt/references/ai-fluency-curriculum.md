---
title: "AI Fluency — curriculum e discernimento"
source_url: "https://academy.claude.com/tutorials"
source_type: tutorial
source_products:
  - "Claude"
  - "Claude Code"
  - "Cowork"
source_date: null
verified_on: "2026-07-20"
language: "it"
tags:
  - "ai-fluency"
  - "curriculum"
  - "discernment"
status: current
time_sensitive: true
license_note: "Original multi-source synthesis; linked tutorial material is not redistributed."
---

# AI Fluency — curriculum e discernimento

**Fonti:** getting-good-at-claude-a-research-backed-curriculum, the-4-ds-of-ai-fluency-behavioral-indicators, get-the-most-from-claude-opus-4-6, imagine-with-claude-student-guide (claude.com, sintesi 2026-07-20).

> Alcune fonti citate sopra sono state ritirate da Anthropic nel 2026-08: vedi [`knowledge/claude/retired-sources.md`](https://github.com/alessiomarcone/agent-fieldbook/blob/main/knowledge/claude/retired-sources.md).

## Il modello di insegnamento in tre passi
1. **Insegna prima la "mossa firma"** — il comportamento che sblocca tutto il resto:
   - Chat: **iterare** (raffinare con turni di follow-up)
   - Claude Code: **chiarire l'obiettivo** (dichiarare l'intento prima dell'esecuzione)
   - Cowork: **chiarire l'obiettivo** (brief dettagliato e autosufficiente)
2. **Avanza lungo lo spettro della Description** (durabilità crescente):
   - Base: shaping della singola risposta (iterazione, upload, ricerche)
   - Media: capacità ripetibile (artifacts, skill, connectors)
   - Duratura: configurazione persistente (Projects, CLAUDE.md, workflow schedulati)
3. **Rivedi il Discernment a ogni passo** — non cresce da solo con la pratica; l'anzianità d'uso NON equivale a fluency.

## Check di discernimento per prodotto e stadio
| Prodotto | Base | Media | Duratura |
|---|---|---|---|
| Chat | La risposta è usabile o serve un altro turno? | Il ragionamento regge o Claude suonava solo sicuro? | Il Project sta dando il contesto giusto? |
| Code | Prima di accettare il diff: cosa ha assunto Claude? | Testa la capability su un caso dove può sbagliare | Audit: Claude usa la configurazione come previsto? |
| Cowork | Cosa renderebbe sbagliato questo output? | Il connector ha preso ciò che serviva o ciò che era facile? | Quand'è l'ultima verifica che il workflow funzioni ancora? |

## Regole per i modelli recenti (fonte: opus-4.6 tutorial; verificare per modelli successivi)
- Dillo una volta, spiega l'intento, dai 2-3 esempi: l'istruzione persiste.
- Front-load del contesto completo; accetta partenza più lenta (fase di comprensione).
- Fai narrare la comprensione prima dell'azione: *"spiegami come è strutturato prima di modificare"*.
- Checkpoint espliciti se vuoi progresso incrementale: *"fermati dopo ogni passo principale"*, *"chiedimi prima di provare più di 2-3 approcci"*.
- Sfrutta l'opinionatezza: *"quali sono tre modi di affrontarlo?"*, poi stress-test: *"cosa c'è di sbagliato in questo piano? cosa mi sfugge?"*.
- Scrittura: campione di stile in testa + pattern da evitare nominati esplicitamente.
- Evita: ripetere istruzioni a metà sessione, framing generico "act as expert", domande leading quando serve oggettività.

## Visual per lo studio (imagine-with-claude)
- Trigger naturale: "mostrami", "disegna", "visualizza" — i visual eccellono su meccanismi con parti in movimento o strutture annidate, non su definizioni statiche.
- L'apprendimento sta nell'**interazione** (slider, quiz incorporati), non nella visione passiva.
- I visual sono costruiti per la tua domanda, non tratti da fonte verificata: **cross-check obbligatorio** con fonti autorevoli.
- Stress-test: *"cosa potrebbe sbagliare questo visual?"*; poi spiega il visual a qualcuno per testare la ritenzione.
- Salvataggio: immagine per appunti; artifact solo per tool interattivi da riaprire.

## Approfondimenti collegati
- Framework 4D completo (Delegation/Description/Discernment/Diligence con sotto-competenze + 6 tecniche di prompting del corso): `ai-fluency-4d-corso.md`
- AI literacy (carattere del modello, gap di conoscenza, sycophancy, allucinazioni): `ai-literacy.md`
- Unico pezzo non ancora ingerito: indicatori comportamentali dettagliati delle 4D (pagina interattiva senza video) — vedi `pending-video-ingestion.md`.
