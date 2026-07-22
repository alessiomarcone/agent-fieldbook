# YouTube — canale ufficiale Anthropic

**Canale:** https://www.youtube.com/@anthropic-ai  
**Video:** https://www.youtube.com/@anthropic-ai/videos  
**Playlist:** https://www.youtube.com/@anthropic-ai/playlists  
**Channel ID:** `UCrDwWp7EBBv4NwvScIpBDOA`

## Ricerche rapide nel canale

- Claude Code: https://www.youtube.com/@anthropic-ai/search?query=Claude%20Code
- Skills: https://www.youtube.com/@anthropic-ai/search?query=Skills
- Subagents: https://www.youtube.com/@anthropic-ai/search?query=subagents
- MCP: https://www.youtube.com/@anthropic-ai/search?query=MCP
- API: https://www.youtube.com/@anthropic-ai/search?query=API
- Agents: https://www.youtube.com/@anthropic-ai/search?query=agents
- Claude.ai: https://www.youtube.com/@anthropic-ai/search?query=Claude.ai
- Prompting: https://www.youtube.com/@anthropic-ai/search?query=prompt
- Artifacts: https://www.youtube.com/@anthropic-ai/search?query=Artifacts
- Research e safety: https://www.youtube.com/@anthropic-ai/search?query=safety

## Categorie prodotte dall’updater

1. Claude Code
2. Skills / Subagents / MCP / Agents
3. API / Developer Platform
4. Claude.ai / Productivity / Artifacts
5. AI Fluency / Prompting
6. Research / Safety
7. Eventi / Interviste / Customer stories
8. Altro

## Perché il catalogo è generato

YouTube carica dinamicamente l’archivio e può bloccare l’estrazione automatica in alcuni ambienti. Un elenco statico invecchia rapidamente.  
Lo script `update_youtube_catalog.py` interroga direttamente il feed del canale tramite `yt-dlp`, ricostruisce tutti i link `watch`, assegna una categoria e genera:

- `youtube_videos.csv`
- `youtube_videos.md`

## Comando

```bash
python3 -m pip install -U yt-dlp
python3 update_youtube_catalog.py
```

Per conservare la cronologia:

```bash
python3 update_youtube_catalog.py --archive
```
