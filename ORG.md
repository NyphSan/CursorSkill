# ORG_ROOT

```text
ORG_ROOT = E:\dev\CursorTeam
```

| 类型 | 路径 |
|------|------|
| 规则 | `ORG_ROOT\rules\` |
| 工作流 | `ORG_ROOT\workflow\` |
| 档案 | `ORG_ROOT\profiles\` |
| 模板 | `ORG_ROOT\templates\` |
| **项目（含记录）** | `ORG_ROOT\projects\<Project>\` |
| 废弃 | `ORG_ROOT\runs\`（仅兼容指针，新项目勿用） |

## 项目包结构

```text
projects/<Project>/
  PROJECT.md          ← GAME_ROOT 等
  records/
    main/             ← 主控
    lead-eng/         ← 主程
    exec/             ← 执行
    review/           ← 审核
    pm/               ← PM
  notes/
```

SCL 示例：`projects\SCL\PROJECT.md` → GAME_ROOT = `E:\Project\Game\S_\SCL`
