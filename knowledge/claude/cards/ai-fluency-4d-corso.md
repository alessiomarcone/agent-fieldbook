---
title: "Corso AI Fluency: Framework & Foundations — le 4D complete"
source_url: "https://anthropic.skilljar.com/ai-fluency-framework-foundations"
source_type: course
source_products:
  - "AI Fluency"
  - "Claude"
source_date: null
verified_on: "2026-07-20"
language: "it"
tags:
  - "ai-fluency"
  - "prompting"
  - "verification"
status: current
time_sensitive: false
license_note: "Original synthesis; source material and transcripts are not redistributed."
---

# Corso AI Fluency: Framework & Foundations — le 4D complete

**Fonte:** transcript delle lezioni del corso ufficiale (canale YouTube Anthropic, sintesi 2026-07-20): 4D Framework, Delegation, Description, Discernment, Diligence, Effective prompting.
Il corso Skilljar completo: https://anthropic.skilljar.com/ai-fluency-framework-foundations

**AI Fluency = lavorare con l'AI in modo efficace, efficiente, etico e sicuro.** Le 4D non sono legate a tool specifici: sopravvivono all'evoluzione della tecnologia.

## 1. Delegation — decidere cosa delegare (efficace+efficiente)
Tre componenti:
- **Problem awareness**: prima dell'AI — cosa vuoi ottenere, come è fatto il successo, che tipo di lavoro serve (semplice ma lungo? incertezza da discutere? mancanza di dati? giudizio critico?). I migliori collaboratori AI sono esperti del proprio dominio prima e delegatori poi.
- **Platform awareness**: conoscenza operativa dei sistemi disponibili — quale eccelle su cosa, velocità vs profondità. Si costruisce sperimentando, non memorizzando: il panorama cambia quasi ogni giorno.
- **Task delegation**: distribuzione strategica — cosa automatizzare, dove l'augmentation (collaborazione) crea più valore dell'automazione, cosa resta esclusivamente umano, cosa affidare ad agenti.

## 2. Description — comunicare chiaramente (il cuore dell'interazione)
Tre componenti:
- **Product description**: cosa vuoi — contesto, task esatto, formato, audience, stile. L'AI non legge nel pensiero: requisiti espliciti.
- **Process description**: come deve lavorarci — guida generale (manuale), passi (ricetta) o dimostrazione (esempi); dati da usare, ordine dei temi, tecnica di analisi.
- **Performance description**: come deve comportarsi — che thinking partner ti serve ora? Convergere o esplorare? Sfidare le tue assunzioni o seguirti? Dettaglio o sintesi? I modelli non sono database né distributori automatici: sistemi interattivi che si comportano diversamente in contesti diversi.

## 3. Discernment — valutare l'output (il controllo qualità)
Tre componenti, speculari alla Description:
- **Product discernment**: accurato? adatto ad audience e scopo? coerente? risolve il problema?
- **Process discernment**: come ci è arrivato — errori logici, salti di attenzione, fissazione su un'interpretazione, ragionamento circolare, idee scartate che rientrano.
- **Performance discernment**: qualità dell'interazione — troppe domande quando servono risposte concise? Troppo breve quando serve completezza? Risponde bene al feedback?

Feedback efficace quando trovi problemi: specifica il problema → spiega perché lo è → suggerisci concretamente → rivedi istruzioni o esempi. **Quando il discernment segnala un problema, spesso la soluzione è una description migliore; a volte va ripensata la delegation** (tool sbagliato o approccio sbagliato).

## 4. Diligence — responsabilità (etico+sicuro)
Tre componenti:
- **Creation diligence**: scelta critica dei sistemi — come è addestrato, di chi sono i dati che inserisco, chi vi accede, allineamento con policy personali/aziendali. Prima di condividere dati sensibili: verificare protezioni e permessi organizzativi.
- **Transparency diligence**: chi deve sapere del ruolo dell'AI in questo lavoro, quando e con che dettaglio. Non è solo compliance: mantiene fiducia.
- **Deployment diligence**: quando pubblichi, **tu** sei responsabile — verifica fatti, bias, accuratezza, diritti d'uso; gli stessi standard che varrebbero se l'avessi fatto interamente tu.

## Le 6 tecniche di prompting del corso (lezione 7)
1. **Contesto**: cosa, perché, chi sei, come userai la risposta.
2. **Esempi** ("n-shot"): quando lo stile è più facile da mostrare che spiegare; copri la varietà dei casi. Prova prima senza.
3. **Vincoli di output espliciti**: formato, lunghezza, linguaggio, dettagli concreti.
4. **Scomposizione in passi** (chain-of-thought): più il task ha varianza di esecuzione o dipende da expertise tua, più conviene tradurla in passi. I reasoning model lo fanno da soli, ma puoi guidarne l'ordine.
5. **Spazio per pensare prima** (non dopo): "prima di rispondere, ragiona su fattori, vincoli e approcci" — e leggere quel ragionamento ti mostra dove correggere la description.
6. **Ruolo/stile/tono**: "da esperto UX, rivedi…" o persona specifica.

**Arma segreta:** chiedi a Claude di scrivere o migliorare il tuo prompt: *"Sto cercando di ottenere X ma non so come formulare la richiesta: aiutami a costruire un prompt efficace."*

Pattern che funzionano: apertura con task chiaro, formato+esempi, vincoli espliciti, background ricco. Errori tipici: presumere lettura del pensiero, più task scollegati in un prompt, "successo" vago, nessun feedback sulle risposte precedenti. Se la conversazione va fuori strada: a volte meglio ripartire da zero che correggere.
