# 网络员工通知 · 任务环境预检制度生效

- **时间：** 2026-08-07  
- **发自：** 主控  
- **岗位：** network-ops  

## 即时检测结果（刚跑）

| 项 | 结果 |
|----|------|
| 代理 10808/10809 | OK |
| 系统代理 → 10809 | OK |
| api2 | OK |
| openai | OK |
| **agentn** | **FAIL（HTTP/0.9）** |
| 门禁 | **黄灯 · 禁止派后台 Task** |

报告：`docs/network/PREFLIGHT-20260807-105346.md`

## 新制度（即日起）

每次启动 Task / Cloud worker **之前**：

```powershell
powershell -ExecutionPolicy Bypass -File E:\dev\CursorTeam\scripts\task-env-preflight.ps1
```

- 绿（0）→ 可派工  
- 黄（4）→ 通知老板换节点；不重派 Task  
- 红（3）→ 先修代理  

规则：`rules/08_network_ops.md` · `rules/02_subagents.md`

## 老板动作

v2rayN **换节点** → 再跑 preflight → 绿后恢复 F4c Task。
