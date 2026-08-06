# Profile · SCL

| 键 | 值 |
|----|-----|
| ProjectId | `SCL` |
| ORG_ROOT | `E:\dev\CursorTeam` |
| **项目文件夹** | `E:\dev\CursorTeam\projects\SCL\` |
| **GAME_ROOT** | `E:\Project\Game\S_\SCL` |
| **记录根** | `E:\dev\CursorTeam\projects\SCL\records\` |
| 项目说明 | `E:\dev\CursorTeam\projects\SCL\PROJECT.md` |
| 栈适配器 | `ue-framework` |
| 运行测 | `ue-pie-validate` |
| PM 委托 | `scl-pm`（可选写 GAME_ROOT/`docs/pm`）；**岗位记录必写记录根** |
| 写仓库 docs | 是（PASS 后，额外） |

## 岗位记录路径（强制）

| 岗位 | 写入 |
|------|------|
| 主控 | `projects/SCL/records/main/` |
| 主程 | `projects/SCL/records/lead-eng/` |
| 执行 | `projects/SCL/records/exec/` |
| 审核 | `projects/SCL/records/review/` |
| PM | `projects/SCL/records/pm/` |

禁止写入已废弃的 `runs/SCL/`。

## 执行花名册

| 细分岗 | Skill |
|--------|--------|
| 角色/属性 | `ue-character` |
| 3C | `ue-scl-3c` |
| AI/ST | `ue-ai-state-tree` |
| 渲染 | `ue-rendering` |
| uasset | `ue-uasset-type-identify` |
| 战旗核 ATBS | 执行子代理 + 主程定界 `Plugins/ATBS/**`（相对 GAME_ROOT） |
| Solo | `second-self` |
