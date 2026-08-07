---
name: network-ops
description: >-
  网络维护岗（归属主控）：按手册常驻维护 Agent 通用网络，预检门禁、代理保活、掉线排障。
  Use for 网络、代理、v2ray、掉线、GPT不可用、agentn、preflight、maintain.
---

# Network Ops（常驻维护）

**权威手册：** `docs/ops/NETWORK_OPS_HANDBOOK.md`  
**参考原文：** `docs/ops/REF-通用网络环境指令.md`（老板 docx 副本）  
**规则：** `rules/08_network_ops.md`  

## 唯一日常入口

```powershell
powershell -ExecutionPolicy Bypass -File E:\dev\CursorTeam\scripts\network-ops-maintain.ps1
```

agentn 仍红且老板确认 UI GPT 可用时加 `-BossConfirmGpt`（软绿，须继续追硬绿）。

## 职责（始终）

1. 保持 v2rayN/xray + HTTP `10809` / SOCKS `10808`  
2. 用户代理变量 + git +（管理员时）WinHTTP 一致  
3. **硬门禁 agentn OK**；落盘 `docs/network/MAINTAIN-*.md`  
4. Task 前配合主控预检；TLS aborted → 立即 maintain  
5. My Machines worker 附带：网络通后再启 `start-org-worker.ps1`  

## 禁止

关 SSL / 防火墙 / 改路由 / 删 VPN / 擅自改订阅；不改游戏 ARCH。

## 升级老板

仅当必须 **换 v2rayN 节点** 才能通 agentn 时。
