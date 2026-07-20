# Claude in Excel

**Fonti:** how-to-use-claude-in-excel-for-accounting-revenue-model-validation, how-to-use-claude-in-excel-for-hr-headcount-planning (claude.com, sintesi 2026-07-20). Il tutorial introduttivo getting-started è video-only: vedi pending.

## In una frase
Claude legge l'intero workbook (tutte le tab, formule incluse) prima di rispondere, individua gli errori tutti insieme, propone modifiche che esegue solo dopo conferma esplicita.

## Pattern universale (vale per ogni modello multi-foglio)
**spiega la struttura → fai emergere gli errori → correggi con permesso → estendi in conversazione**

## Procedura
1. Apri sidebar: `Ctrl+Option+C` (Mac) / `Ctrl+Alt+C` (Windows).
2. Orientamento: *"Guidami in questo modello: cosa c'è in ogni tab e come si collega tutto?"* → mappa dei flussi dati.
3. Errori: lascia che Claude elenchi tutto subito (riconciliazioni, duplicati, #REF!, dati mancanti); scegli tu da quale partire — uno alla volta.
4. Correzione: fatti mostrare logica e proposta → autorizza esplicitamente → verifica applicazione. Undo con Cmd/Ctrl+Z.
5. Estensione: nuove colonne descritte in termini di business (*"aggiungi una colonna che calcola il costo pieno per dipendente usando i tassi della tab Assumptions"*) — **sempre formule che referenziano le assunzioni, mai valori hardcodati**.
6. Scenari: *"aggiorna il piano assumendo attrition 15% invece di 10%; mostrami cosa cambia per reparto"* → confronto prima/dopo.
7. Grafici: specifica tipo e componenti (*"waterfall del rollforward deferred revenue Q3: saldo iniziale, bookings, revenue riconosciuta, aggiustamenti, saldo finale"*).

## Regole
- Struttura prima dei fix: chiarezza previene errori a cascata.
- Assunzioni centralizzate in una tab dedicata referenziata dalle formule → scenario modeling pulito.
- Un errore corretto = verifica dell'impatto su tutte le tab a valle.
- Il contesto persiste nella conversazione: torna sugli issue citandoli, senza rispiegare.

## Errori da evitare
- "Sistema gli errori" senza specificare cella e comportamento atteso.
- Accettare fix senza capire la causa radice.
- Valori statici al posto di formule.
- Chiedere di una tab isolata quando il calcolo dipende da più fogli.
- Riavviare la conversazione: si perde la memoria dei finding.

## Verifica
1. Dopo la mappa: traccia a mano un percorso dati e confronta.
2. Dopo un fix: ricalcola (F9), controlla che l'errore sia sparito senza crearne di nuovi.
3. Dopo uno scenario: verifica a mano la variazione su un reparto.
4. Dopo formule nuove: spot-check 3-5 righe.
5. Prima di condividere: controlla che i totali del Summary quadrino con il dettaglio.

## Vincoli (2026-07, verificare doc corrente)
Beta su piani Max, Team, Enterprise; integrazione Microsoft 365 via AppSource.
