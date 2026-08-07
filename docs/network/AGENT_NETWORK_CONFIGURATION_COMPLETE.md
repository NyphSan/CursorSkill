# AGENT_NETWORK_CONFIGURATION_COMPLETE

- OpenAI HTTPS: AUTH_BOUNDARY 401（网络可达，未带 Key，不算失败）
- Time: 2026-08-07T14:32:23.1112960+08:00
- Admin Shell: True (主控会话)
- Architecture: Priority-2 HTTP/SOCKS (v2rayN/xray); no AI system TUN
- HTTP: 127.0.0.1:10809
- SOCKS: 127.0.0.1:10808
- WinIE proxy: (pre-existing) 127.0.0.1:10809
- WinHTTP: synced to 127.0.0.1:10809 (this elevated step)
- Backup: E:\dev\CursorTeam\docs\network\backup-winhttp-20260807-143154

## Rollback WinHTTP
```
netsh winhttp reset proxy
# or restore from E:\dev\CursorTeam\docs\network\backup-winhttp-20260807-143154\winhttp-before.txt
```
