# PC 级主控流水线

**ORG_ROOT：** `E:\dev\CursorTeam`

```text
你 → 主控会话（cursor-admin）
        → 加载 profiles/<Project> + projects/<Project>/PROJECT.md
        → Task 主程 → projects/<Project>/records/lead-eng/ARCH-D?.md
        → Task 执行 → records/exec/EXEC-D?.md（代码改 GAME_ROOT）
        → Task 审核 → records/review/REVIEW-D?.md（含越界）
        → PASS → PM 自我审核 → records/pm/PM-D?.md
        → PM 裁决「开下一项」→ 主控派下一刀（不必等老板）
        → 仅「升级老板」时停
```

规则见 `ORG_ROOT/rules/`（含 `04_pm_self_audit.md`）。模板见 `ORG_ROOT/templates/`。  
SCL：`projects/SCL/` · GAME_ROOT 见该目录 `PROJECT.md`。
