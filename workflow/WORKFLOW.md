# PC 级主控流水线

**ORG_ROOT：** `E:\dev\CursorTeam`

```text
你 → 主控会话（cursor-admin）
        → 加载 profiles/<Project> + projects/<Project>/PROJECT.md
        → Task 主程 → ARCH-D?.md
        → Task 执行 → EXEC-D?.md（代码改 GAME_ROOT）
        → Task 审核 → REVIEW-D?.md
        → PASS → 主程「主任务完成通知」→ 主控
        → 主控派 gitea-repo → 项目仓 commit/push + records/gitea/
        → PM 自我审核 → PM-D?.md
        → PM「开下一项」→ 下一刀；「结束本批」→ 批末制度迭代
        → 若本批改了组织规则 → 主控派 gitea-repo → CursorAiOrg commit/push
```

规则：`rules/04_pm_self_audit.md` · `rules/06_gitea_repo_admin.md`。  
SCL：`projects/SCL/PROJECT.md`（含 GAME_ROOT 与项目 remote）。
