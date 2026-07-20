# Claude Desktop App — Chat, Cowork, Code

**Fonte:** navigating-the-claude-desktop-app (claude.com, sintesi 2026-07-20).

## Matrice di decisione
| Task | Modalità | Perché |
|---|---|---|
| Domanda su un dashboard | Chat (quick entry) | risposta immediata con contesto visivo |
| Report di ricerca di mercato | Cowork | multi-fonte, sforzo prolungato |
| Review + refactor di codice | Code (Plan mode) | strategia rivista prima delle modifiche |
| Brainstorming | Chat | iterazione turno per turno |
| Briefing quotidiano ricorrente | Cowork schedulato | automazione del ripetitivo |
| Sviluppo locale | Code (local) | filesystem e terminale completi |

Cowork e Code condividono lo stesso motore (Claude Code); Chat è web-nativo con estensioni desktop. Privacy: Cowork opera in spazio contenuto (solo cartelle condivise); Code ha accesso pieno alla directory di progetto e al terminale.

## Chat desktop
- Doppio tap Option (Mac): overlay di ingresso rapido senza cambiare app.
- Screenshot del dashboard invece di descriverlo a parole.
- Dettatura vocale per ragionare a voce.

## Cowork
1. Concedi accesso cartella → Claude valuta i contenuti.
2. Rispondi alle domande di chiarimento su scope/formato.
3. **Approva il piano in sidebar prima che parta.**
4. Monitora fonti, file creati, avanzamento piano.
5. Opzioni: task schedulati con ricorrenza, Chrome connesso per navigazione web, plugin specializzati.

## Code
- Ambiente: cartella locale o repo GitHub (remoto — continua nel cloud anche ad app chiusa).
- Tre modalità: **Ask** (diff visivo da approvare), **Code** (comandi terminale da approvare), **Plan** (strategia completa prima di ogni modifica).
- Git integrato: sperimenta con rollback sicuro.

## Errori da evitare
- Chat per ricerche lunghe multi-fonte; Cowork per dialogo in tempo reale.
- Cartelle condivise disordinate: Claude setaccia contenuto irrilevante.
- Copiare a mano dati dal web invece di connettere Chrome.
- Approvare modifiche Code senza guardare il diff su progetti critici.

## Vincoli (2026-07, verificare doc corrente)
Quick entry/screenshot/dettatura solo Mac; tab Code su piani Pro, Max, Team, Enterprise (rollout); sessioni remote richiedono GitHub.
