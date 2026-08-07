# CursorTeam CHANGELOG

## 1.1.8 — 2026-08-07

- 网络维护定版：`docs/ops/NETWORK_OPS_HANDBOOK.md`（交给 network-ops 常驻）  
- 参考原文入库：`docs/ops/REF-通用网络环境指令.md`  
- 日常入口：`scripts/network-ops-maintain.ps1`；强化 `rules/08` + `skills/network-ops`  
- 目标：持续绿门禁（agentn），保障全部 Task 可跑  

## 1.1.7 — 2026-08-07

- **工作流三件套落地**：组织仓收口 + 派工纪律固化 + My Machines worker 闭环  
- `rules/02`：门禁表（绿 / 软绿 BossConfirmGpt / 黄红禁派）与 `rules/08` 对齐  
- `rules/00`：OS 管理员提权仅主控；脚本 `elevate-cursor-for-main.ps1`  
- `skills/cursor-admin`：预检→软绿→可见 Task→worker 在线日常纪律  
- 通用 Agent 网络环境结案：`docs/network/AGENT_NETWORK_CONFIGURATION_COMPLETE.md`

## 1.1.6 — 2026-08-07

- 网络员工：每次 Task 前强制 `task-env-preflight.ps1`（`rules/08` + `rules/02`）
- agentn 非绿禁止派后台 Task（无老板确认时）；`-BossConfirmGpt` 为软绿例外

## 1.1.5 — 2026-08-07

- 组织上云定版：`rules/09_cloud_local_worker.md` + `docs/ops/cursor-cloud-my-machines.md`
- Cloud Agent 编排 + **My Machines** 落 `ORG_ROOT`/`GAME_ROOT`；脚本 `start-org-worker.ps1` / `start-scl-worker.ps1`
- 明确：纯云 VM 不保证能直接用 Gitea；落本地再 push

## 1.1.4 — 2026-08-06

- 新增岗位 **网络员工**（`rules/08_network_ops.md` · skill `network-ops`）
- 脚本：`ensure-v2ray.ps1`（代理保活）+ `cursor-gpt-netcheck.ps1`（agentn 验收）
- 掉线复盘：代理进程退出会导致主控/Agent 突然不可用

## 1.1.3 — 2026-08-06

- 新增 `rules/07_token_and_model.md`：每轮 Token/上下文压力自检；按轻/中/重选 Task `model`
- `rules/02_subagents.md`：派工块强制「资源与选模」；硬名单 `composer-2.5-fast` / `inherit` / `cursor-grok-4.5-high-fast`
- 主控主会话默认高配（俗称 max）；子代理分流；澄清 Max Mode ≠ 主控高配；补充模型不可用排查

## 1.1.2 — 2026-08-06

- 组织仓远程改云端：`https://git.bddream.site/nyph/CursorAiOrg`（替代局域网 `192.168.3.23:3000`）

## 1.1.1 — 2026-08-06

- `rules/02_subagents.md`：强制「子代理派工」可见块、Task 真派工、agent 链接、默认 background
- 禁止主会话换帽子假装子代理（除非老板明示主控直干）
- **SCL 验证：** F0–F5 框架迁移批全 PASS；retro `docs/retros/20260806-scl-f0-f5-framework-migration.md`

## 1.1.0 — 2026-08-06

- 新增岗位 **Gitea 员工**（`gitea-repo`），归属主控；规则 `rules/06_gitea_repo_admin.md`
- 组织远程：`http://192.168.3.23:3000/nyph/CursorAiOrg.git`
- 主程主任务完成后通知主控 → 安排项目仓提交；组织规则更新 → 提交组织仓
- 提交规范：Conventional Commits（`templates/GIT_COMMIT.md`）
- 参考：https://docs.gitea.com/

## 1.0.1 — 2026-08-06

- 明确主控「完善制度」职责与自我迭代触发（`rules/05_main_iterates_org.md`）
- 钉死 1.0.0 基线说明（`VERSION.md`）；本条为基线后首个制度补丁
- 批末强制 org retro（`docs/retros/`）
- 对齐 skill 入口与 workflow：PM 自审闸门、记录路径 `projects/*/records/`
- R1 复盘入库

## 1.0.0 — 2026-08-06

- 首版可运行组织：岗位、定界、子代理、项目包、续温、PM 自审
- SCL 样板；R1 高低差 D1/D2 实跑验证
