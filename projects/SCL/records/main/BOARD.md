# 主控看板（精简）

| 域 | 状态 |
|----|------|
| 焦点 | AITeam 工作流 + **主机环境门禁 1.1.9** |
| 网络岗 | 手册 `docs/ops/NETWORK_OPS_HANDBOOK.md` · 入口 `network-ops-maintain.ps1` |
| 硬门禁 | **仍须 agentn 绿**；软绿仅临时 |
| 主机环境 | **默认只诊断**；写入/提权前问老板（`rules/10`） |
| Worker | `cursorteam-pc`（曾拉起；掉线先 maintain 再启） |
| 组织版本 | **1.1.9** |

```powershell
powershell -ExecutionPolicy Bypass -File E:\dev\CursorTeam\scripts\network-ops-maintain.ps1
```
