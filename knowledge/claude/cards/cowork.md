---
title: "Claude Cowork — delega, personalizzazione, casi d'uso"
source_url: "https://claude.com/resources/tutorials"
source_type: tutorial
source_products:
  - "Cowork"
source_date: null
verified_on: "2026-07-20"
language: "it"
tags:
  - "cowork"
  - "delegation"
  - "workflows"
status: current
time_sensitive: true
license_note: "Original multi-source synthesis; linked tutorial material is not redistributed."
---

# Claude Cowork — delega, personalizzazione, casi d'uso

**Fonti:** delegating-your-first-task, customize-claude-cowork, using-claude-cowork-for-legal-question-briefing / sales-account-research / marketing-ops-review, using-claude-for-your-small-business (claude.com, sintesi 2026-07-20).

## Prima delega
1. Configura accesso cartelle (working folder che Claude legge/edita/salva).
2. Configura connectors (Drive, email, CRM, tracker…).
3. Delega con brief chiaro; chiedi a Claude di fare 1-2 domande chiave subito se manca contesto.
4. **Rivedi il piano proposto prima di autorizzare l'esecuzione** — checkpoint di sicurezza critico.
5. Approva; verifica il risultato.

## Personalizzazione — tre livelli
1. **Connectors + Instructions**: sistemi collegati + regole permanenti (globali/progetto/organizzazione). Regole generali → Instructions.
2. **Skills**: processo ripetibile → dopo averlo eseguito una volta chiedi *"impacchetta quello che abbiamo appena fatto in una skill"*. Invocazione: `/nome-skill` o riconoscimento automatico.
3. **Plugins**: bundle skills+connectors per ruolo (Sales, Legal, Finance, Marketing…), installazione one-click da Customize → Plugins.

## Pattern operativo ricorrente (vale per ogni ruolo)
Il ciclo insegnato da tutti i casi d'uso ufficiali è identico:

**skill che conosce le fonti → brief schedulato → esecuzione on-demand → verifica umana → apprendimento salvato nella skill**

1. **Setup una tantum:** installa plugin del ruolo, connetti TUTTI i sistemi dove vivono le decisioni, scegli working folder, personalizza la skill descrivendo dove stanno i documenti e come sono strutturati.
2. **Schedulazione:** `/schedule` per il brief mattutino/settimanale che pre-smista il lavoro (es. *"/schedule ogni giorno feriale alle 8, leggi inbox, tracker e chat e scrivi un memo: cosa scade oggi, cosa è nuovo, cosa è urgente"*).
3. **On-demand:** `/brief domanda specifica` — la skill interroga le decisioni storiche e risponde con citazioni linkate.
4. **Verifica (non negoziabile):** clicca ogni citazione, leggi la riga di origine, giudica tu. Più hai fretta, più la verifica conta.
5. **Chiusura del ciclo:** prima di chiudere la sessione: *"cosa abbiamo imparato questa settimana che deve entrare nella skill?"* → Claude riscrive la skill.

### Applicazioni per ruolo (stessa struttura)
- **Legale:** "la nuova richiesta cambia la conclusione della review precedente?" — risposta con citazioni alle decisioni passate.
- **Sales:** `/account-research nome-account` prima della call (spend, stakeholder, adozione, rischi); `/call-summary` dopo (action items + messaggio interno + follow-up cliente nella tua voce).
- **Marketing ops:** prep del report settimanale schedulata la domenica; tu scegli il focus e approvi metrica per metrica prima dell'espansione.
- **Piccola impresa:** `/monday-brief` (cassa, settlements, pipeline, calendario, 3 priorità), `/close-month` (riconciliazione + P&L narrativo), `/plan-payroll` (forecast 30 giorni + solleciti calibrati sulla storia pagamenti). **Tutto resta in bozza finché non approvi.**

## Errori da evitare
- Saltare la personalizzazione: skill generica = output generico.
- Connectors incompleti: la skill non vede le decisioni che non le hai collegato.
- Fidarsi del brief senza cliccare le citazioni.
- Usare skill per regole generali (vanno nelle Instructions).
- Aspettarsi esecuzione automatica: le skill propongono e mettono in scena, tu approvi.
- Cambiare working folder: si frammenta la storia.

## Verifica
- Testa la skill su un caso noto e confronta con ciò che avresti scritto tu.
- Primo run schedulato sempre rivisto manualmente.
- Spot-check di un numero alla fonte prima di inoltrare a terzi.
- Chiedi periodicamente: *"quali placeholder sono rimasti in questo plugin?"*
