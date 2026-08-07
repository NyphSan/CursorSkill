# 组织运行时：Cloud + 本地 Worker（≥1.1.5）

CursorTeam **默认上云编排**，**默认落盘在老板本机**（My Machines）。

## 定版

```text
Cloud Agent（决策）
  → My Machines worker（本机 tool）
  → ORG_ROOT / GAME_ROOT 文件与终端
```

权威操作手册：`docs/ops/cursor-cloud-my-machines.md`

## 主控义务

1. 派「要改本机文件」的云端任务时，环境须选 **worker**（如 `cursorteam-pc` / `scl-pc`），禁止默认纯云 VM 却要求改 `E:\…`  
2. 本机 worker 未在线 → 先派网络员工/`ensure-v2ray` + `start-org-worker`，再开云端刀  
3. 桌面主控会话（Local Agent）可继续日常调度；与 Cloud 并行时以 **records 落盘** 为准防双写  

## Worker 命名（建议）

| name | 目录 | 用途 |
|------|------|------|
| `cursorteam-pc` | `E:\dev\CursorTeam` | 组织规则 / records |
| `scl-pc` | `E:\Project\Game\S_\SCL` | 游戏工程 |

## 与 Gitea

- 组织仓远程：`https://git.bddream.site/nyph/CursorAiOrg`（已云）  
- 游戏仓：以 `PROJECT.md` 为准；若仍局域网，上云迁移另刀  
- Gitea push 在 **worker 本机凭据** 下执行（`gitea-repo` 岗）  
