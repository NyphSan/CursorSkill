# BACKUP + CHANGE 2026-08-07T13:49:37.1745152+08:00

## Detected architecture
- TUN for AI traffic: NO (Radmin VPN is mesh, not system AI TUN)
- Scheme: Priority-2 HTTP/SOCKS via v2rayN/xray
- Confirmed: HTTP 127.0.0.1:10809 (xray), SOCKS 127.0.0.1:10808 (xray)
- System IE proxy already: 127.0.0.1:10809

BACKUP -> E:\dev\CursorTeam\docs\network\backup-20260807-134937

## CHANGE-1 User env proxy (standard vars)
SET User HTTP_PROXY=http://127.0.0.1:10809
SET User HTTPS_PROXY=http://127.0.0.1:10809
SET User ALL_PROXY=socks5://127.0.0.1:10808
SET User NO_PROXY=localhost,127.0.0.1,::1,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,.local,*.local
SET User http_proxy=http://127.0.0.1:10809
SET User https_proxy=http://127.0.0.1:10809
SET User all_proxy=socks5://127.0.0.1:10808
SET User no_proxy=localhost,127.0.0.1,::1,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,.local,*.local

## CHANGE-2 Git global proxy -> HTTP 10809 (was http://10808 which is wrong for SOCKS)
SET git http.proxy / https.proxy = http://127.0.0.1:10809

## CHANGE-3 npm proxy inherit
SET npm proxy / https-proxy = http://127.0.0.1:10809

## CHANGE-4 WinHTTP sync (may need admin)
winhttp set output: 写入代理服务器设置时出错。(5) 拒绝访问。


当前的 WinHTTP 代理服务器设置:

    直接访问(没有代理服务器)。
WinHTTP after:

当前的 WinHTTP 代理服务器设置:

    直接访问(没有代理服务器)。


STOP_NOTE: WinHTTP still direct — needs Administrator. Rollback file: winhttp-before.txt

## SKIPPED (forbidden without explicit auth)
- routes / firewall / SSL verify off / network reset / install software

## TEST after change
- HTTPS https://github.com: PASS
- HTTPS https://registry.npmjs.org/: PASS
- HTTPS https://api2.cursor.sh: PASS
- HTTPS https://api.openai.com/v1/models: PASS_AUTH_OR_APP status=401
- DNS github.com: PASS 20.205.243.166
- DNS api.openai.com: PASS 2a03:2880:f112:83:face:b00c:0:25de
- DNS api.anthropic.com: PASS 2607:6bc0::10
- DNS registry.npmjs.org: PASS 2606:4700::6810:222
- DNS pypi.org: PASS 2a04:4e42:400::223
- DNS huggingface.co: PASS 2001::c73b:9407
- DNS api2.cursor.sh: PASS 
- Git ls-remote: 2c78326f810173a4f3aefd8021f1e07575412481	HEAD
- npm ping: npm notice PONG 3284ms

BACKUP_DIR=E:\dev\CursorTeam\docs\network\backup-20260807-134937
