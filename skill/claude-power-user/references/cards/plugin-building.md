# Plugin Cowork — personalizzare e costruire da zero

**Fonti:** how-to-customize-plugins-in-cowork, how-to-build-a-plugin-from-scratch-in-cowork (claude.com, sintesi 2026-07-20).

## Architettura
Un plugin = **skills** (workflow riutilizzabili, `/nome`) + **connectors** (sistemi esterni) + **subagent** (helper paralleli/sequenziali con context window indipendente). Funziona solo in Cowork, non in Chat. Resta locale finché non lo condividi.

## Personalizzare un plugin esistente
1. Sidebar → Customize → Plugins → seleziona → **Customize**.
2. Claude scansiona i tool connessi e fa domande di conferma.
3. Fornisci tre strati di informazione:
   - **Tool:** nomi esatti dei sistemi ("Salesforce", non "il CRM").
   - **Processo:** standard, terminologia, soglie di escalation, cosa significa "finito".
   - **Riferimenti:** esempi di lavoro finito, brand guideline, template.
4. Rivedi il riepilogo modifiche + i file istruzione in plain-text → **Save plugin**.
5. Itera: dopo ogni run, *"aggiungi questo al plugin così la prossima volta è giusto"*; periodicamente *"quali placeholder sono rimasti?"*.

## Costruire da zero
1. Descrivi il plugin anche in una frase ("mi serve un plugin per il team customer success").
2. Fornisci workflow, inventario tool, standard, gestione dei casi limite.
3. Esegui le skill su lavoro reale; correggi i gap direttamente in conversazione.
4. Design delle skill: scope stretto; descrizione = *cosa fa, quando usarla, cosa copre*; documenti di riferimento allegati; parametrizza le varianti; concatena skill in sequenza (output → input).
5. Workflow multi-fonte lunghi → subagent (evita esaurimento del contesto).

## Distribuzione
- File `.plugin` condiviso a mano.
- **GitHub**: push della cartella; i colleghi installano da URL e ricevono gli update al push.
- Provisioning admin per interi dipartimenti (sovrascrive le modifiche locali).

## Errori da evitare
- Skill troppo ampie: non si attivano in modo affidabile.
- Descrizioni vaghe: il trigger non scatta quando serve.
- Workflow lunghi in un solo contesto senza subagent.
- Presumere sync automatico tra dispositivi (non c'è).
- Installare senza leggere i file che Claude ha effettivamente scritto.

## Verifica
1. Esegui ogni skill su un caso di produzione; confronta formato output con lo standard.
2. Verifica attivazione da slash menu e da riconoscimento contestuale.
3. Testa i passaggi di consegna tra skill concatenate e tra subagent.
4. Confronta output tra più utenti per consistenza.

## Vincoli noti (2026-07, verificare doc corrente)
Solo desktop app; le sessioni di customizzazione editano file locali; plugin provisionati dall'org si ri-sincronizzano sopra le modifiche locali.
