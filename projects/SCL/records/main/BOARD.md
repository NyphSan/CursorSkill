# 主控看板（精简）

| 域 | 状态 |
|----|------|
| 焦点 | AITeam 工作流 + **网络常驻维护已交接** |
| 网络岗 | 手册 `docs/ops/NETWORK_OPS_HANDBOOK.md` · 入口 `network-ops-maintain.ps1` |
| 硬门禁 | **仍须 agentn 绿**；软绿仅临时 |
| Worker | `cursorteam-pc`（曾拉起；掉线先 maintain 再启） |
| 组织版本 | **1.1.8** |

```powershell
powershell -ExecutionPolicy Bypass -File E:\dev\CursorTeam\scripts\network-ops-maintain.ps1
```
