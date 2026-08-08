# 项目 · SCL（Story Campus Lore）

| 键 | 值 |
|----|-----|
| ProjectId | `SCL` |
| **GAME_ROOT** | `E:\Project\Game\S_\SCL` |
| **项目 Git 远程** | `http://192.168.3.23:3000/SCLG/SCL.git` |
| **ORG 项目根** | `E:\dev\CursorTeam\projects\SCL` |
| **记录根** | `E:\dev\CursorTeam\projects\SCL\records\` |
| Profile | `E:\dev\CursorTeam\profiles\SCL.md` |
| **项目规则** | `E:\dev\CursorTeam\projects\SCL\RULES.md` |
| 引擎提示 | UE 5.6.x |
| 栈适配器 | `ue-framework` |
| Gitea 提交记录 | `records/gitea/` |

## 模块分层

```text
业务 · Source/SCL  →  战斗 · Plugins/SCLTactical  →  核心 · Plugins/SCLCore  →  Engine
```

- **业务模块 `SCL`：** 模式/关卡编排、3C、Presenter→ViewState→WBP、Adjudication 关口、内容装配。  
- **战斗插件 `SCLTactical`：** 战旗 L0（单位/回合/移动射击真相）；Demo Content 非生产。  
- **核心插件 `SCLCore`：** DesignData 叶节点、Framework Types/Guards、日历等可复用底座。  

派工按 profile 花名册区分 **业务岗** vs **核心岗**；定界见 `records/lead-eng/ARCH-F0.md`。

## 开发工作约定

1. **改游戏代码 / Content：** 路径一律相对 **GAME_ROOT**（上表）。  
2. **组织与岗位记录：** 只写 **记录根** 下对应岗位子目录，不进游戏仓（PM 额外写 `docs/pm` 除外，见 profile）。  
3. 主控接单：`project=SCL` → 读本文件 + profile + **RULES.md** → 派工。  

## 记录目录（按岗位）

| 岗位 | 目录 | 典型文件 |
|------|------|----------|
| 主控 | `records/main/` | `BOARD.md` · `BACKLOG.md` · 分发单 |
| 主程 | `records/lead-eng/` | `ARCH-D#.md` |
| 执行 | `records/exec/` | `EXEC-D#.md` |
| 审核 | `records/review/` | `REVIEW-D#.md` |
| PM | `records/pm/` | `PM-D#.md` |
| Gitea | `records/gitea/` | `COMMIT-D#.md` |
| 杂记 | `notes/` | 非闸门流程的备忘 |

## 快速打开游戏工程

```text
E:\Project\Game\S_\SCL\SCL.uproject
```
