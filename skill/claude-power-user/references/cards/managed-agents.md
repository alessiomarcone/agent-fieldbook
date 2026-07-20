# Claude Managed Agents (API)

**Fonte:** transcript video ufficiale What is Claude managed agents (sintesi 2026-07-20). Stato alla data: research preview limitata, accesso su application (claude.com/form/claude-managed-agents). Verificare disponibilità corrente.

## In una frase
Suite di API per costruire e deployare agenti su scala: definisci agenti (tool, persona, capacità), configuri ambienti sandbox (pacchetti, controlli di rete), lanci sessioni dalla tua applicazione; Claude lavora in container isolato con filesystem, bash e web search.

## Blocchi costitutivi
- **Agents + Sessions**: sessione lanciata dal tuo backend (es. drag di un ticket Kanban su "in progress" → sessione parte in automatico).
- **Environments**: container preconfigurati (es. Lighthouse + Puppeteer preinstallati, repo GitHub montato).
- **Outcomes/rubric**: definisci "fatto" con criteri misurabili (es. Lighthouse >90, niente render-blocking); un **grader separato con proprio contesto** valuta l'output; Claude legge il feedback, corregge e riconsegna finché non passa.
- **Event stream**: ogni tool call streamma in tempo reale verso la tua UI.
- **Parallelismo**: più sessioni = più container indipendenti.
- **Memory store**: l'agente legge cosa aveva trovato la scorsa esecuzione e scrive cosa è cambiato → report incrementali ("compute -15% da settimana scorsa") e diagnosi che partono dai pattern passati invece che da zero.
- **Multi-agent coordination**: coordinatore che delega a specialisti in context window separate su filesystem condiviso, poi sintetizza.
- **Permissions policy**: azioni esterne (es. post su Slack) fermate per approvazione umana prima dell'invio.
- **MCP**: azioni su tool terzi (Slack, Asana…).

## Pattern d'uso mostrati
1. **Event-triggered**: ticket → sessione con ambiente dedicato e rubrica di accettazione.
2. **Scheduled**: ricerca prezzi SaaS settimanale → analisi Python in sandbox → Excel via skill → summary → link su Slack + task in Asana.
3. **Incident response**: alert dal monitoring come tool result → coordinatore + 3 specialisti → sintesi → approvazione umana → post.

## Principi
- Definisci l'esito, non i passi: "you define what done looks like, Claude works until it gets there".
- Rubrica esterna con grader separato = qualità verificabile.
- Memoria per miglioramento continuo; approvazione umana sulle azioni verso l'esterno.
