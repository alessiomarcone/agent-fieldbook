---
title: "Claude Design — prototipi, UX, presentazioni"
source_url: "https://academy.claude.com/tutorials"
source_type: tutorial
source_products:
  - "Claude"
source_date: null
verified_on: "2026-07-20"
language: "it"
tags:
  - "design"
  - "prototyping"
  - "presentations"
status: current
time_sensitive: true
license_note: "Original multi-source synthesis; linked tutorial material is not redistributed."
---

# Claude Design — prototipi, UX, presentazioni

**Fonti:** using-claude-design-for-prototypes-and-ux, using-claude-design-for-presentations-and-slide-decks (claude.com, sintesi 2026-07-20).

## Prototipi e UX

### In una frase
Genera prototipi interattivi usando i componenti reali del tuo codebase; l'handoff a Claude Code trasforma il prototipo in spec di implementazione.

### Workflow
1. **Collega il codebase**: Import → repo GitHub o directory locale. Claude analizza componenti, styling, convenzioni. Collega solo le directory rilevanti — escludi `.git` e `node_modules/` (lag del browser).
2. **Prototipa** con prompt specifici: sezioni, sorgenti dati, azioni, ruoli utente — mai "un dashboard" generico. Riferisci i componenti per nome reale ("usa il componente ProductCard").
3. **Review**: chiedi 2-3 alternative side-by-side; condividi il link per feedback asincrono.
4. **Stati**: prima dell'handoff fai generare empty/error/loading state e volumi dati diversi.
5. **Documenta le decisioni in chat** ("tab invece di sidebar perché…"): il contesto viaggia nell'handoff.
6. **Handoff**: Export → Hand off to Claude Code → bundle (design + chat history + README) → incolla l'URL in Claude Code.

### Checklist pre-handoff
- [ ] Componenti con nomi reali del codebase
- [ ] Token di design (colori/spacing) coerenti con produzione
- [ ] Stati empty/error/loading progettati
- [ ] Razionale delle decisioni documentato in chat

## Presentazioni

### Workflow
1. claude.ai/design → descrivi deck: audience, messaggi chiave, contesto organizzativo (es. *"deck di 10 slide sui risultati Q1 con sezioni per ricavi, aggiornamenti prodotto e team"*).
2. Itera per numero di slide: *"nella slide 3 cambia…"*.
3. Visualizzazioni generate da Claude, non manuali; HTML consente animazioni.
4. Condivisione con permessi (privato / view / comment / edit); export HTML, PPTX, PDF, zip, Canva, Claude Code.

### Regole
- Struttura generata prima, rifinitura dopo — non prompt iniziale iperdettagliato.
- Design system organizzativo applicato automaticamente se disponibile.
- Verifica prima dell'uso: fatti, brand compliance, gerarchia visiva, leggibilità, test dell'export nel formato target.
