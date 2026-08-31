---
title: "@Claude nel workspace (Slack/Teams)"
source_url: "https://academy.claude.com/tutorials"
source_type: tutorial
source_products:
  - "Claude"
source_date: null
verified_on: "2026-07-20"
language: "it"
tags:
  - "workspace"
  - "collaboration"
  - "automation"
status: current
time_sensitive: true
license_note: "Original multi-source synthesis; linked tutorial material is not redistributed."
---

# @Claude nel workspace (Slack/Teams)

**Fonti:** tasks-to-try-with-claude-tag-in-your-workspace, best-practices-using-claude-tag (claude.com, sintesi 2026-07-20).

## In una frase
@Claude lavora nei canali del team con un proprio account: legge messaggi, file e tool connessi al canale, esegue il task e risponde nello stesso thread; il lavoro continua anche quando esci.

## Concetti chiave
- **Canali vs DM:** canali = lavoro visibile al team (la storia del canale diventa contesto); DM = tool personali (calendario, email).
- **Memoria di canale:** correzioni e preferenze restano nel canale e si accumulano; il canale si "specializza" nel suo tipo di lavoro.
- **Proattività configurabile:** da "rispondi solo se taggato" a monitoraggio autonomo, per canale, via admin.
- **Forme di output:** risposta, file/chart, pagina interattiva, aggiornamento ricorrente, azione nei tool (PR, ticket).

## Procedura
1. Admin connette i tool ai canali; verifica con: *"@Claude quali tool puoi usare in questo canale?"*
2. Tagga @Claude con richiesta specifica, indicando la forma di output.
3. Claude mostra progresso (reazioni/checklist); rivedi il risultato.
4. Correggi rispondendo nel thread (mai editando il messaggio originale).
5. Consolida: task ricorrenti schedulati, poi responsabilità continuative ("Sei responsabile di tenere aggiornate le domande aperte di questo canale: controlla ogni giorno, rispondi a ciò che puoi, tagga la persona giusta per il resto").

## Prompt riutilizzabili (adattamenti IT — originali EN nel tutorial)
- Recap: *"@Claude aggiornami su questo thread: cosa è stato deciso, chi possiede ogni decisione, cosa è ancora aperto."*
- Ricorrente: *"@Claude ogni lunedì alle 9, pubblica cosa è stato deciso qui la settimana scorsa, cosa è aperto e cosa aspetta qualcuno."*
- Richieste senza risposta: *"@Claude scorri le ultime due settimane ed elenca le richieste rimaste senza risposta e chi le sta bloccando."*
- Dati: *"@Claude grafica gli utenti attivi settimanali delle ultime 8 settimane, divisi per piano. Mostrami la query."*
- Onboarding: *"@Claude costruisci la pagina della prima settimana per il nuovo assunto: mappa dei sistemi, chi possiede cosa, chi incontrare e perché, la prima PR."*
- Codice: *"@Claude correggi il bug descritto sopra e apri una PR in bozza. Segui CI e review, taggami quando è pronta al merge."*
- Prep meeting (DM): *"Ho la review prezzi alle 14. Leggi #q3-pricing-review e la proposta nel mio drive, dammi i tre punti su cui insistere."*

## Checklist transizione a lavoro continuativo
- [ ] Gestisce 2-3 task discreti in modo affidabile
- [ ] Pattern di feedback stabilito nel canale
- [ ] Scope concordato dal team + livello di proattività impostato
- [ ] Almeno un task schedulato che gira da solo
- [ ] Una responsabilità continuativa assegnata
- [ ] Self-review periodica: *"guarda i thread del canale e scrivi cosa faresti diversamente"*

## Errori da evitare
- Ri-incollare contesto già presente nella storia del canale.
- Editare messaggi inviati (nessun effetto): nuovo reply = nuovo task.
- Più task nello stesso thread.
- Test solo in DM privato: si perde il contesto del canale.
- Task ricorrenti senza criterio di stop.

## Verifica
1. Controlla accesso tool prima di delegare.
2. Fatti linkare messaggi/account/sezioni di origine.
3. Ri-esegui query SQL e rileggi codice prima di merge/deploy.
4. Primo run schedulato: rivedilo prima di lasciarlo girare da solo.
