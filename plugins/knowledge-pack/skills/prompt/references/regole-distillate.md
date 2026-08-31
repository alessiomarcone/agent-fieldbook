---
title: "Regole operative distillate dai tutorial ufficiali"
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
  - "operating-rules"
  - "verification"
  - "workflows"
status: current
time_sensitive: true
license_note: "Original multi-source synthesis; linked tutorial material is not redistributed."
---

# Regole operative distillate dai tutorial ufficiali

**Fonte:** tutorial ufficiali Anthropic — estratti e sintetizzati il 2026-07-20 da `claude.com/resources/tutorials`, indirizzo migrato in `academy.claude.com/tutorials` nel 2026-08.
**Uso:** regole trasversali da applicare in ogni sessione. Le procedure specifiche per prodotto sono nelle altre card.

## Regole universali (valgono per Chat, Code, Cowork, Excel, @Claude)

1. **Chiarisci l'obiettivo prima di eseguire.** La "mossa firma" che sblocca tutto il resto: in Chat è iterare con follow-up; in Claude Code e Cowork è dichiarare l'intento prima dell'esecuzione con un brief dettagliato.
2. **Front-load del contesto.** Fornisci subito file, vincoli, architettura, esempi. La qualità di ciò che condividi all'inizio determina la qualità dell'output.
3. **Dillo una volta sola, ma spiega il perché.** I modelli recenti seguono le istruzioni al primo colpo: spiega l'intento dietro la regola, dai 2-3 esempi, non ripetere promemoria a metà sessione.
4. **Criteri di successo espliciti.** Prima di delegare definisci cosa rende l'output accettabile e come lo verificherai.
5. **Approvazione umana prima di azioni esterne.** Tutto ciò che invia, pubblica o paga resta in bozza finché non approvi. Accesso in sola lettura sempre attivo; scrittura dietro conferma.
6. **Verifica proporzionale alla posta.** Scorri i riassunti a basso rischio; leggi integralmente tutto ciò che è customer-facing o modifica sistemi. Chiedi a Claude di linkare le fonti e spot-checka almeno un numero all'origine.
7. **Il discernimento non cresce da solo.** L'iterazione e l'uso delle feature si imparano con la pratica; la valutazione critica dell'output va esercitata deliberatamente a ogni livello. Domanda chiave prima di usare un output: "cosa lo renderebbe sbagliato?"
8. **Anti-sycophancy e anti-allucinazione.** Non accettare l'accordo di Claude come conferma. Chiedi "cosa c'è di sbagliato in questo piano?", "cosa mi sfugge?", e per analisi importanti fai fare a Claude una seconda passata a caccia di errori nella prima risposta.
9. **Feedback correttivo, non riscrittura.** Se l'output manca il bersaglio, rispondi con la correzione specifica: nei contesti persistenti (canali @Claude, skill, plugin) la correzione si accumula e migliora le esecuzioni future.
10. **Regola del riuso.** Procedura ripetuta ≥2 volte → chiedi a Claude di impacchettarla in una skill ("Package what we just did into a skill"). Regole generali → Instructions/CLAUDE.md; processi ripetibili → Skill.
11. **Chiudi il loop di apprendimento.** A fine ciclo ricorrente chiedi: "cosa abbiamo imparato che deve entrare nella skill per la prossima volta?" e fai riscrivere la skill.

## Scelta del modello (fonte: choosing-the-right-claude-model)

| Modello | Peso sui limiti | Uso |
|---|---|---|
| Haiku | minimo | lookup, categorizzazioni, risposte brevi |
| Sonnet | moderato | default quotidiano: scrittura, coding, workflow multi-step |
| Opus | alto | analisi profonda in sessione interattiva, ricerca da interrogare e ridirigere |
| Fable | massimo | task lunghi/critici, delega dell'esito con pochi check-in |

- Nel dubbio parti da Sonnet; scala su Opus se mostra limiti.
- Non usare un modello sovradimensionato: spreca token del piano.
- Regola effort/thinking prima di cambiare modello.
- A ogni nuovo modello, riprova i task che prima avevano toccato il soffitto.
- Free plan: solo Haiku/Sonnet (verificare doc corrente, info del 2026-07).

## Scelta dell'interfaccia (fonte: navigating-the-claude-desktop-app)

| Task | Modalità |
|---|---|
| Domanda rapida, iterazione, brainstorming | Chat |
| Ricerca multi-fonte, produzione documenti, task delegabili | Cowork |
| Sviluppo software con test e version control | Code |
| Task ricorrente automatico | Cowork + scheduled task |

- Cowork e Code condividono lo stesso motore; Chat è nativo web.
- Errore tipico: usare Chat per ricerche lunghe multi-fonte, o Cowork per dialogo in tempo reale.

## Gerarchia degli strumenti di personalizzazione (fonte: customize-claude-cowork)

1. **Connectors** — sistemi dove il lavoro già vive (lettura/scrittura, autorizzazione admin).
2. **Instructions** — regole permanenti a livello globale / progetto / organizzazione.
3. **Skills** — processo ripetibile, caricato on demand, invocabile con `/nome`.
4. **Plugins** — bundle connectors+skills per ruolo, installazione one-click, distribuzione via file, GitHub o admin.

Percorso tipico: connectors+instructions → skill dopo 2-3 ripetizioni → condivisione quando i colleghi chiedono il setup.

## Errori ricorrenti da evitare (aggregati da tutti i tutorial)

- Presumere accessi non configurati: chiedi sempre "cosa puoi accedere da qui?" prima di delegare.
- Richieste vaghe senza forma dell'output desiderato (reply, file, chart, pagina, azione esterna).
- Approvare modifiche senza leggere la logica proposta.
- Hardcodare valori dove servono formule/riferimenti (Excel) o testo dove serve template (skill).
- Fidarsi di un numero sorprendente senza verificarlo alla fonte.
- Sessioni monolitiche: task separati in thread separati.
- Modificare il messaggio inviato invece di rispondere con uno nuovo (@Claude: l'edit non ha effetto).
- Personalizzazione generica: dai nomi esatti dei tuoi sistemi ("Salesforce", non "il CRM").
