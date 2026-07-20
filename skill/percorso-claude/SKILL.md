---
name: percorso-claude
description: Use this skill when the user asks which official Claude/Anthropic course or tutorial to take, in what order, says "da dove comincio", "percorso di studio", "quale corso", "quanto tempo serve", or wants a learning plan for Claude, Claude Code, Cowork, MCP or the API. Builds a sequenced path from the official catalog with real durations.
---

# Percorso Claude

Costruisce un percorso di studio sequenziato dai cataloghi ufficiali, con durate reali e link diretti.

## Dati
- `references/courses.csv` — 21 corsi ufficiali (categoria, livello, durata, lezioni, quiz, utilità, URL Skilljar).
- `references/tutorials.csv` — 30 tutorial ufficiali (categoria, funzione, obiettivo, URL).

## Procedura

1. **Chiedi (se non dichiarati):** obiettivo (uso personale / team / sviluppo / insegnamento), livello di partenza, ore disponibili a settimana.
2. **Leggi i CSV** e seleziona solo ciò che serve all'obiettivo. Ordini di riferimento ufficiali:
   - Fondamenti: Claude 101 → AI capabilities and limitations → AI Fluency: Framework & Foundations + tutorial "Getting good at Claude" e "Choosing the right Claude model".
   - Claude Code: Claude Code 101 → Claude Code in Action → Introduction to agent skills → Introduction to subagents → Introduction to MCP.
   - API/agenti: Claude Platform 101 → Building with the Claude API → Introduction to MCP → MCP Advanced Topics.
   - Ruoli specifici: corso AI Fluency della categoria pertinente (Small Business, Educators, Students, Nonprofits, Builders).
3. **Distribuisci sul tempo dichiarato** usando le durate del CSV; una voce per riga: settimana, corso, durata, cosa saprai fare dopo.
4. **Affianca i tutorial** pertinenti come pratica tra un corso e l'altro (5 min l'uno).
5. **Chiudi con verifica**: per ogni blocco, un esercizio concreto ("dopo agent skills: impacchetta un tuo workflow ripetuto in una skill").

## Regole
- Mai consigliare corsi fuori catalogo o inventare durate: solo dati dai CSV.
- Nota la data di verifica del catalogo; se l'utente cerca un tema assente, indica l'indice ufficiale https://claude.com/resources/courses come fonte aggiornata.
- Massimo 3 voci a settimana: meglio finire che accumulare.
