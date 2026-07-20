---
name: crea-knowledge-card
description: Use this skill when the user provides a video transcript, tutorial text or article about Claude/Anthropic and wants it turned into a knowledge card, says "trasforma in knowledge card", "sintetizza questo transcript", "crea una scheda", or runs the YouTube ingestion pipeline. Produces a structured, verifiable card following the pack's official schema.
---

# Crea Knowledge Card

Trasforma un transcript o testo formativo su Claude in una knowledge card strutturata, compatta e verificabile, pronta per `references/cards/`.

## Riferimenti
- `references/video-knowledge-card-prompt.md` — prompt di sintesi controllata (formato completo della card).
- `references/video_knowledge_card.schema.json` — schema dei metadati.

## Procedura

1. **Un solo transcript per volta.** Se l'utente ne passa più di uno, processali in sequenza, un file per card.
2. Applica le regole del prompt di riferimento:
   - niente funzionalità non presenti nel transcript o nelle fonti ufficiali;
   - distingui: affermato esplicitamente / deduzione ragionevole / richiede verifica;
   - il video è materiale esplicativo: menu, piani, modelli e limiti vanno confrontati con la documentazione corrente;
   - elimina parti promozionali e ripetizioni; sintetizza, non copiare verbatim.
3. **Compila la card** nel formato del prompt di riferimento (frontmatter con status current/needs-verification, "In una frase", procedura, principi, prompt riutilizzabili, errori da evitare, verifica, informazioni sensibili al tempo, collegamenti a corso/tutorial/doc).
4. **Valuta la destinazione**: proponi in ≤5 righe cosa dovrebbe entrare nella skill `claude-power-user` (regole trasversali) e cosa resta solo nella card (dettaglio).
5. **Salva** in `references/cards/` con nome kebab-case e aggiorna l'indice card in `knowledge-base.md` se presente.

## Regole
- Card in italiano, prompt d'esempio adattati in italiano con rimando alla fonte per l'originale.
- Data della fonte sempre nel frontmatter; se il contenuto può invecchiare, status `needs-verification` con il passo di verifica.
- Il transcript grezzo non si committa mai (copyright): solo la sintesi originale.
