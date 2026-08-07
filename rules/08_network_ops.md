# 网络员工（归属主控）

负责本机 **代理 / Cursor 连通 / 模型可达性**，不改游戏业务、不改 ARCH。

## 岗位

| 项 | 值 |
|----|-----|
| 岗位名 | 网络员工 / network-ops |
| Skill | `network-ops` |
| **归属** | **主控**（只接受主控派工） |
| 记录 | `docs/network/NETCHECK-*.md` · `PREFLIGHT-*.md` |

## 职责

1. **保活代理**：v2rayN/xray；系统代理优先 **HTTP `10809`**（见 `optimize-cursor-network.ps1`）  
2. **验收通路**：`cursor-gpt-netcheck.ps1` — **agentn 必须 OK**  
3. **任务前预检（强制）**：每次主控派 **Task / Cloud worker 任务前**跑 `task-env-preflight.ps1`  
4. **排障**：掉线 / TLS aborted / GPT 不可用  
5. **交付**：落盘 NETCHECK/PREFLIGHT + 老板下一步  

## 每次启动任务 · 环境检查（强制）

```text
主控准备派 Task / 云端 worker
  → 跑 scripts/task-env-preflight.ps1
  → exit 0：派工，派工块写「环境门禁：绿」
  → exit 4：默认禁 Task；若老板确认 Cursor 内 GPT 可用：
       task-env-preflight.ps1 -BossConfirmGpt → 软绿 exit 0
       派工块写「门禁：软绿（BossConfirmGpt）」
  → exit 3：先 ensure-v2ray / optimize，再预检
```

说明：curl 测 agentn 失败时 UI 仍可能通 GPT；软绿可推进，Task 仍可能偶发 TLS aborted。

派工块必须追加一行：

```text
- 环境门禁：绿 | 黄（禁 Task）| 红（代理挂） · PREFLIGHT 路径
```

主控 **不得**在 agentn 红灯时重派会吞 TLS 的后台 Task。

## 触发

```text
老板：测网络 / 完善网络 / 任务前检查
  → 主控代行或派 network-ops（轻档 composer-2.5-fast）
  → preflight 或 optimize + netcheck
  → 落盘 docs/network/
```

## Hard rules

- 不擅自改订阅/节点密钥；换节点须老板 GUI 或明示授权  
- 系统代理用 HTTP `10809`，勿把 SOCKS `10808` 写成 `http://`  
- 「api2 通」≠「可派 Task」；以 **agentn** 为准  
- 与 `rules/02_subagents.md` / `07_token_and_model.md` 联动  
