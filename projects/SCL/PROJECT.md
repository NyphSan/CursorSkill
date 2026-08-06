# 项目 · SCL（Story Campus Lore）

| 键 | 值 |
|----|-----|
| ProjectId | `SCL` |
| **GAME_ROOT** | `E:\Project\Game\S_\SCL` |
| **ORG 项目根** | `E:\dev\CursorTeam\projects\SCL` |
| **记录根** | `E:\dev\CursorTeam\projects\SCL\records\` |
| Profile | `E:\dev\CursorTeam\profiles\SCL.md` |
| 引擎提示 | UE 5.6.x |
| 栈适配器 | `ue-framework` |

## 开发工作约定

1. **改游戏代码 / Content：** 路径一律相对 **GAME_ROOT**（上表）。  
2. **组织与岗位记录：** 只写 **记录根** 下对应岗位子目录，不进游戏仓（PM 额外写 `docs/pm` 除外，见 profile）。  
3. 主控接单：`project=SCL` → 读本文件 + profile → 派工。  

## 记录目录（按岗位）

| 岗位 | 目录 | 典型文件 |
|------|------|----------|
| 主控 | `records/main/` | `BOARD.md` · `BACKLOG.md` · 分发单 |
| 主程 | `records/lead-eng/` | `ARCH-D#.md` |
| 执行 | `records/exec/` | `EXEC-D#.md` |
| 审核 | `records/review/` | `REVIEW-D#.md` |
| PM | `records/pm/` | `PM-D#.md` |
| 杂记 | `notes/` | 非闸门流程的备忘 |

## 快速打开游戏工程

```text
E:\Project\Game\S_\SCL\SCL.uproject
```
