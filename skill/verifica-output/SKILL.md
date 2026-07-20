---
name: verifica-output
description: Use this skill when the user asks to verify, fact-check or stress-test an AI answer, says "controlla questa risposta", "è affidabile?", "verifica prima di inviare", or before using AI output in customer-facing, legal, financial or published work. Applies the official Discernment competency and the anti-hallucination/anti-sycophancy checks.
---

# Verifica Output

Passa un output AI (o una risposta appena data) al vaglio della competenza **Discernment** ufficiale, con i check anti-allucinazione e anti-sycophancy dei tutorial Anthropic.

## Procedura

1. **Classifica il rischio.** Basso (uso interno, riformulabile) → check rapido. Alto (customer-facing, legale, finanziario, pubblicato, decisione) → check completo + fonti esterne.
2. **Check allucinazione** — segnala come DA VERIFICARE ogni: fatto specifico, statistica, citazione, data, nome, numero; temi di nicchia/recenti/post-cutoff; persone o luoghi reali poco noti. Per ciascuno: fonte trovata? la fonte supporta davvero l'affermazione?
3. **Check sycophancy** — la risposta sta assecondando? Sospetta se: la domanda conteneva un punto di vista, citava un'autorità, chiedeva validazione, aveva posta emotiva, o la conversazione è lunga. Contromossa: riformula in modo neutro e confronta; chiedi esplicitamente controargomenti.
4. **Seconda passata indipendente**: rileggi l'output cercando errori nella prima risposta ("trova cosa c'è di sbagliato"), idealmente in una conversazione nuova.
5. **Check di processo**: ragionamento circolare? elementi già scartati rientrati? assunzioni non dichiarate? Chiedi: "cosa hai assunto?" e "quanto sei confidente, e su cosa meno?"
6. **Verdetto strutturato**:
   - ✅ Verificato (con fonte)
   - ⚠️ Plausibile ma non verificato — come verificarlo in un passo
   - ❌ Contraddetto / inventato
   - Domanda finale obbligatoria: **"cosa renderebbe sbagliato questo output?"**

## Regole
- La verifica è proporzionale alla posta, ma i numeri specifici si controllano sempre prima di inoltrare a terzi.
- Diligence: chi pubblica è responsabile come se l'avesse scritto da sé — stessi standard.
- Se più della metà dei claim è ⚠️, consiglia retrieval (web search, documenti, MCP) invece di conoscenza interna del modello.
