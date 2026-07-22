# Tutorial video-only — stato ingestione transcript

Aggiornamento 2026-07-20: transcript estratti via yt-dlp (auto-caption YouTube) per 9 tutorial su 11 + 6 lezioni del corso AI Fluency Framework & Foundations. Contenuto distillato nelle card di questa cartella. I transcript grezzi restano locali (non committati — copyright).

## Completati (card di destinazione)
| Tutorial | Card |
|---|---|
| How AI gets its character | `ai-literacy.md` |
| Understanding knowledge gaps in AI models | `ai-literacy.md` |
| What is sycophancy in AI models | `ai-literacy.md` |
| Why do AI models hallucinate | `ai-literacy.md` |
| What are skills | `claude-code-estensioni.md` |
| How skills compare to other Claude Code features | `claude-code-estensioni.md` |
| Using Claude Code Remote Control | `claude-code-estensioni.md` |
| Getting started with Claude in Excel | `claude-excel.md` |
| What is Claude managed agents | `managed-agents.md` |
| Corso AI Fluency: 4D framework + Delegation + Description + Discernment + Diligence + Prompting | `ai-fluency-4d-corso.md` |

## Ancora mancanti
| Tutorial | URL | Motivo |
|---|---|---|
| The 4 Ds — behavioral indicators | https://claude.com/resources/tutorials/the-4-ds-of-ai-fluency-behavioral-indicators | nessun video YouTube embeddato; contenuto = prompt scorecard interattivo. Framework 4D già coperto da `ai-fluency-4d-corso.md` |
| Using the GitHub integration | https://claude.com/resources/tutorials/using-the-github-integration | nessun video YouTube embeddato nella pagina. Fonte alternativa: doc ufficiale code.claude.com |

## Come rigenerare/estendere
1. `python3 update_youtube_catalog.py` per il catalogo canale.
2. Embed ID da una pagina tutorial: cercare `youtube.com%2Fembed%2F` nell'HTML.
3. `yt-dlp --skip-download --write-auto-subs --sub-langs en <url>` → pulizia VTT → sintesi con `knowledge-card-prompt.md`.
