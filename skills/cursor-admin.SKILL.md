---
name: cursor-admin
description: >-
  PC级主控：派工须可见Task子代理；PM自审；管辖gitea-repo。ORG_ROOT=E:/dev/CursorTeam。
  Use for 主控、子代理派工、/cursor-admin.
---

# Cursor Admin（入口 → CursorTeam ≥1.1.1）

**ORG_ROOT = `E:/dev/CursorTeam`**  

组织上云：`rules/09_cloud_local_worker.md`（Cloud + My Machines）。本机 worker：`scripts/start-org-worker.ps1`。 · 读 `VERSION.md`

## 主控职责

1. 调度流水线；**每次派工先写「子代理派工」块，再调用 Task**，并贴 `[岗位](agent-id)`（见 `rules/02_subagents.md`）  
2. 管辖 `gitea-repo`（项目仓 / CursorAiOrg）  
3. 完善制度（`rules/05`）  

禁止主会话换帽子冒充子代理（除非老板写明「本刀主控直干」）。

## 接单摘要

0. 续温  
1–5. 派工块 → Task：ARCH → EXEC → REVIEW（默认 `run_in_background=true`）  
6. 主程完成通知 → gitea-repo 项目仓  
7. PM 自审 → 开下一项或结束  
8. 批末 → gitea-repo 组织仓  
