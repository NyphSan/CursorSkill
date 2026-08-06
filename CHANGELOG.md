# CursorTeam CHANGELOG

## 1.1.3 — 2026-08-06

- 新增 `rules/07_token_and_model.md`：每轮 Token/上下文压力自检；按轻/中/重选 Task `model`
- `rules/02_subagents.md`：派工块强制「资源与选模」；硬名单 `composer-2.5-fast` / `inherit` / `cursor-grok-4.5-high-fast`

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
