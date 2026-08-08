# PC 级主控流水线

**ORG_ROOT：** `E:\dev\CursorTeam`  
**版本对齐：** ≥1.1.11（含测试岗）

## A. 业务刀（功能开发）

```text
你 → 主控会话（cursor-admin）
        → 加载 profiles/<Project> + projects/<Project>/PROJECT.md + **RULES.md**
        → Task 主程 → ARCH-D?.md
        → Task 执行 → EXEC-D?.md（代码改 GAME_ROOT）
        → Task 测试 → TEST-D?.md（运行测；玩法刀强制，见 rules/12）
        → Task 审核 → REVIEW-D?.md（静态 DoD + 越界；采信 TEST）
        → PASS → 主程「主任务完成通知」→ 主控
        → 主控派 gitea-repo → 项目仓 commit/push + records/gitea/
        → PM 自我审核 → PM-D?.md
        → PM「开下一项」→ 下一刀；「结束本批」→ 批末制度迭代
        → 若本批改了组织规则 → 主控派 gitea-repo → CursorAiOrg commit/push
```

```text
ARCH → EXEC → TEST → REVIEW → gitea → PM
```

- **TEST FAIL** → 返工 EXEC，不进 REVIEW/PM  
- **纯工程刀** 可 ARCH 书面豁免 TEST 或降为编译+最小冒烟（`rules/12`）  
- 规则：`rules/04_pm_self_audit.md` · `rules/06_gitea_repo_admin.md` · `rules/12_test_runtime.md`  

SCL：`projects/SCL/PROJECT.md`。

## B. 运行时环（每批 / 每日 · 强制）

源自 `docs/ops/` 手册沉淀，详见 `rules/11_ops_runtime_workflow.md`。

```text
续温（RESUME + BOARD）
  → 预检 task-env-preflight（agentn=HTTP/2 探针）
  → 绿/软绿才派可见 Task（rules/02）
  → 主机环境默认只诊断（rules/10）；写入须老板确认
  → 需重启 Cursor：CursorSession（tools/cursor-session），禁止只甩手动重启
  → Cloud 改本机：My Machines worker 在线（rules/09）
  → 长期：network-ops-maintain / 看门狗（老板授权战役）
```

| 入口 | 命令 / 路径 |
|------|-------------|
| 预检 | `scripts/task-env-preflight.ps1` |
| 维护 | `scripts/network-ops-maintain.ps1` |
| 看门狗 | `docs/ops/NETWORK_OPS_WATCHDOG.md` |
| 续温重启 | `tools/cursor-session/CursorSession.ps1 -Action Restart` |
| 运维规则 | `rules/11_ops_runtime_workflow.md` |
| 测试岗 | `rules/12_test_runtime.md` · skill `ue-pie-validate` |

## C. 修改运维配置时

```text
CHECK → BACKUP → CHANGE → VERIFY → (失败) ROLLBACK
```

不重设计已定版代理架构；一次一层；结案写 `docs/network/*REPORT*` 或 MAINTAIN/PREFLIGHT。
