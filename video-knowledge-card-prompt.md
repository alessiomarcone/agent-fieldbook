# Prompt — Trasforma un video in una knowledge card Claude

Usa questo prompt insieme a **un solo transcript per volta**.

---

Analizza il transcript allegato come materiale formativo ufficiale Anthropic/Claude.

## Obiettivo
Trasformalo in una knowledge card operativa, compatta, verificabile e riutilizzabile in Claude Projects o in una Skill.

## Regole
1. Non aggiungere funzionalità non presenti nel transcript o nelle fonti ufficiali disponibili.
2. Distingui:
   - contenuto esplicitamente affermato;
   - deduzione ragionevole;
   - elemento che richiede verifica aggiornata.
3. Considera il video materiale esplicativo: per menu, piani, modelli, limiti e disponibilità richiedi il confronto con la documentazione ufficiale corrente.
4. Elimina introduzioni promozionali, ripetizioni e parti non operative.
5. Conserva esempi solo quando chiariscono un principio o una procedura.
6. Non copiare estese porzioni verbatim: sintetizza.

## Output Markdown

```markdown
---
title:
source_url:
source_type: youtube
source_date:
knowledge_checked:
products:
features:
level:
tags:
status: current|needs-verification|archived
---

# Titolo

## In una frase
...

## Quando usarlo
...

## Prerequisiti
...

## Procedura
1. ...
2. ...

## Principi e decisioni
- ...

## Prompt o configurazioni riutilizzabili
...

## Errori da evitare
- ...

## Verifica del risultato
- ...

## Informazioni sensibili al tempo
- ...

## Collegamenti consigliati
- Corso:
- Tutorial:
- Documentazione:

## Candidato per
- [ ] Project Instructions
- [ ] CLAUDE.md
- [ ] Skill
- [ ] Connector/MCP
- [ ] Subagent
- [ ] Hook
```

Dopo la scheda, indica in massimo cinque righe quale parte dovrebbe entrare nella Skill `claude-power-user` e quale dovrebbe restare solo nelle reference.
