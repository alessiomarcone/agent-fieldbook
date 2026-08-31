---
title: "AI literacy — carattere, gap di conoscenza, sycophancy, allucinazioni"
source_url: "https://academy.claude.com/tutorials"
source_type: tutorial
source_products:
  - "Claude"
source_date: null
verified_on: "2026-07-20"
language: "it"
tags:
  - "ai-literacy"
  - "hallucination"
  - "sycophancy"
status: current
time_sensitive: false
license_note: "Original multi-source synthesis; linked tutorial material and transcripts are not redistributed."
---

# AI literacy — carattere, gap di conoscenza, sycophancy, allucinazioni

**Fonti:** transcript dei 4 video tutorial AI Fluency (claude.com/canale Anthropic, sintesi 2026-07-20): how-ai-gets-its-character, understanding-knowledge-gaps, what-is-sycophancy, why-do-ai-models-hallucinate.

> Alcune fonti citate sopra sono state ritirate da Anthropic nel 2026-08: vedi [`knowledge/claude/retired-sources.md`](https://github.com/alessiomarcone/agent-fieldbook/blob/main/knowledge/claude/retired-sources.md).

## Come nasce il "carattere" di un modello
Due stadi: **pre-training** (predizione della parola successiva su dati enormi — un completatore di documenti, nessun concetto di "aiutarti") + **fine-tuning** (esempi curati di comportamento utile + segnali di reward da preferenze umane — lo strato che crea l'assistente). Il fine-tuning lascia 4 zone d'ombra da riconoscere:

1. **Sycophancy** — valida facilmente e cede a un pushback leggero anche quando aveva ragione.
2. **Verbosità** — default a risposte lunghe anche quando la brevità servirebbe meglio.
3. **Ipercautela** — hedge pesanti o rifiuti su richieste in realtà sicure.
4. **Calibrazione lasca della confidenza** — la sicurezza dichiarata è legata solo debolmente all'affidabilità reale: massima vigilanza qui.

Non sono bug di un modello: emergono in tutti i modelli, in forma diversa a seconda del fine-tuning.

## Gap di conoscenza — dove fidarsi e dove no
La domanda giusta non è "l'AI lo sa?" ma **"quanto era rappresentato in ciò che ha letto?"**. Continuum: zona di capacità (scienza mainstream, linguaggi popolari, storia ben documentata — profondità straordinaria) ↔ bordo inaffidabile (temi rari, eventi post-cutoff, domini di nicchia, conoscenza locale, lingue minoritarie).

Limiti strutturali: **cutoff** (dopo la data, nulla esiste), **staleness** (vero all'epoca, cambiato dopo, il modello non può saperlo), **copertura disomogenea**, **bias ereditato** (i "default" riflettono i blind spot dei dati), **amnesia delle fonti** ("l'ho letto da qualche parte" non è una citazione).

Le feature di prodotto esistono per tappare questi buchi: web search (aggira il cutoff), MCP (documenti mai visti in training), tool (calcoli/database reali). Se non le usi, ti affidi solo a ciò che è stato assorbito in training.

**Protezioni:** verifica tutto ciò che è time-sensitive; testa prima di fidarti in un dominio nuovo (la brillantezza non si trasferisce al dominio accanto); attenzione alle assunzioni di default; attiva search/retrieval quando esistono.

## Sycophancy — quando scatta e come contrastarla
Scatta più facilmente quando: una verità soggettiva è presentata come fatto; si cita una fonte autorevole; la domanda è formulata con un punto di vista; si chiede validazione esplicita; ci sono emozioni in gioco; la conversazione è molto lunga.

**Contromisure:** linguaggio neutro di ricerca dei fatti; cross-reference con fonti affidabili; chiedi esplicitamente accuratezza o controargomenti; riformula la domanda; apri una conversazione nuova; per decisioni importanti, chiedi a una persona di fiducia. Nota di design: l'adattamento a tono/formato/livello è desiderabile — il confine è sui fatti e sul benessere.

## Allucinazioni — quando aspettarsele e come ridurle
Più probabili con: fatti specifici, statistiche o citazioni; temi oscuri, di nicchia o recentissimi; persone/luoghi reali ma poco noti; dettagli esatti (date, nomi, numeri). L'errore appare identico a una risposta giusta, con tono sicuro.

**Riduzione pratica:**
- Chiedi le fonti, poi chiedi di verificare che le fonti supportino davvero le affermazioni.
- Dichiara in anticipo: *"va bene se non lo sai"*.
- Chiedi quanto è confidente e cosa potrebbe essere sbagliato — spesso il modello "sa" di essere incerto ma voleva suonare sicuro.
- Per risposte dubbie: nuova chat, chiedi di trovare gli errori nella risposta precedente.
- Lavoro critico: cross-check con fonti fidate, scetticismo su numeri/date/citazioni specifiche.
