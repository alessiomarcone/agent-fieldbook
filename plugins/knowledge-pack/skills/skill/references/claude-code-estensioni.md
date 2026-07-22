---
title: "Claude Code — skills vs CLAUDE.md vs subagent vs hook vs MCP, remote control"
source_url: "https://code.claude.com/docs/en/skills"
source_type: documentation
source_products:
  - "Claude Code"
source_date: null
verified_on: "2026-07-20"
language: "it"
tags:
  - "claude-code"
  - "skills"
  - "extensions"
status: current
time_sensitive: true
license_note: "Original multi-source synthesis; linked documentation and transcripts are not redistributed."
---

# Claude Code — skills vs CLAUDE.md vs subagent vs hook vs MCP, remote control

**Fonti:** transcript video ufficiali (sintesi 2026-07-20): What are skills, How skills compare to other Claude Code features, Using Claude Code Remote Control. Fonte primaria per dettagli: code.claude.com/docs.

## Cos'è una skill
File markdown (`SKILL.md`) che insegna a Claude come fare una cosa **una volta sola**; Claude la applica automaticamente quando rileva un task pertinente, confrontando la richiesta con le description delle skill disponibili. Nel contesto entra solo nome+description finché la skill non serve: non intasa la context window.

Posizioni:
- **Personali**: `~/.claude/skills/` — ti seguono in tutti i progetti (stile commit, formato documentazione, come vuoi le spiegazioni).
- **Di progetto**: `.claude/skills/` nella root del repo — chi clona le riceve automaticamente (standard di team, brand guideline).

Segnale che serve una skill: ti ritrovi a spiegare la stessa cosa ripetutamente.

## Matrice di scelta del meccanismo
| Meccanismo | Caricamento | Usalo per |
|---|---|---|
| **CLAUDE.md** | sempre, ogni conversazione | standard sempre validi: "TypeScript strict mode", "mai toccare lo schema DB", preferenze framework, stile |
| **Skill** | on demand, a match della richiesta | expertise task-specifica: checklist PR review non serve mentre debuggi |
| **Slash command** | quando lo digiti tu | azioni invocate esplicitamente |
| **Subagent** | delega esplicita | contesto di esecuzione separato, tool access diverso, isolamento dal contesto principale |
| **Hook** | a evento (event-driven) | linter a ogni salvataggio, validazioni prima di certi tool call, side-effect automatici |
| **MCP** | connessione esterna | tool e dati di sistemi terzi |

Distinzioni chiave dai video:
- Skill **aggiunge conoscenza al contesto corrente**; subagent **lavora in contesto separato** e riporta il risultato.
- Skill è **request-driven** (si attiva su ciò che chiedi); hook è **event-driven** (scatta sull'evento, sempre).
- Setup tipico: CLAUDE.md per gli standard always-on + skill per l'expertise on demand + hook per l'automazione. Combinali: non forzare tutto nelle skill.

## Remote control
Continuare una sessione locale da web/mobile:
- `claude remote control` nella directory di progetto → URL per Claude Code web + barra spaziatrice = QR code per mobile.
- Da sessione già aperta: `/remote-control`.
- Tutto resta sulla tua macchina (stessi tool, MCP server, config, filesystem); la conversazione si sincronizza in tempo reale tra dispositivi.
- In `/config` puoi abilitarlo per tutte le sessioni.
- **Spawn mode** (Max/Team/Enterprise alla data del video): creare nuove sessioni da remoto scegliendo il device dall'environment button.
- Rollout su Pro e Max alla data del video — verificare disponibilità corrente.
