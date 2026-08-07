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
4. **OS 管理员提权仅主控**（`rules/00_org_charter.md`）；子代理禁止自行提权  

禁止主会话换帽子冒充子代理（除非老板写明「本刀主控直干」）。

## 派工日常纪律（强制）

```text
预检 task-env-preflight.ps1
  → 绿：派 Task
  → agentn 红 + 老板确认 GPT UI 可用：-BossConfirmGpt → 软绿 → 派 Task（派工块注明）
  → 否则：禁后台 Task / 主会话薄做 / 先 network-ops
可见块 → Task（默认 background）→ 贴 agent 链接 → 更新 BOARD
Cloud 改本机文件 → worker=cursorteam-pc|scl-pc 须在线（start-org-worker）
```

## 接单摘要

0. 续温 + 环境门禁  
1–5. 派工块 → Task：ARCH → EXEC → REVIEW（默认 `run_in_background=true`）  
6. 主程完成通知 → gitea-repo 项目仓  
7. PM 自审 → 开下一项或结束  
8. 批末 → gitea-repo 组织仓  
