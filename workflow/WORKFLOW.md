# PC 级主控流水线

**ORG_ROOT：** `E:\dev\CursorTeam`

```text
你 → 主控会话（cursor-admin）
        → 加载 ORG_ROOT/profiles/<Project>
        → Task 主程 lead-eng → runs/<Project>/ARCH-D?.md
        → Task 执行 → runs/<Project>/EXEC-D?.md
        → Task 审核 → runs/<Project>/REVIEW-D?.md（含越界）
        → PASS → PM → runs/<Project>/PM-D?.md
        → 主控确认闸门 → 下一刀
```

规则见 `ORG_ROOT/rules/`。模板见 `ORG_ROOT/templates/`。
