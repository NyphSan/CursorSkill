# CursorTeam · PC 组织目录

**权威根（ORG_ROOT）：** `E:\dev\CursorTeam`  
**组织版本：** 见 [VERSION.md](VERSION.md)（当前 ≥ **1.2.0**）

## 三仓权威（≥1.2.0）

| 类型 | 远程 | 本地 |
|------|------|------|
| **Skill Map** | [GitHub CursorSkill](https://github.com/NyphSan/CursorSkill) | `%USERPROFILE%\.cursor\skills\` |
| **组织** | [Gitea CursorAiOrg](https://git.bddream.site/nyph/CursorAiOrg) | `E:\dev\CursorTeam\`（本目录） |
| **项目规则** | 各项目 Git | `projects/<Project>/RULES.md` + `GAME_ROOT` |

详 [rules/13_repo_authority_split.md](rules/13_repo_authority_split.md) · 迁移 [docs/ops/REPO_SPLIT_MIGRATION.md](docs/ops/REPO_SPLIT_MIGRATION.md)

本目录承载：组织章程、规则、工作流、项目档案（profiles）、模板、**岗位 records**。  
与具体游戏工程解耦；SCL 等只是 `profiles/` + `projects/` 下的档案。

**主控完善制度：** 见 [rules/05_main_iterates_org.md](rules/05_main_iterates_org.md)；批末 [workflow/BATCH_CLOSEOUT.md](workflow/BATCH_CLOSEOUT.md)。  
**Gitea：** [rules/06_gitea_repo_admin.md](rules/06_gitea_repo_admin.md)

Cursor 通过用户级 skill（`%USERPROFILE%\.cursor\skills\`）发现入口；  
组织岗 SKILL 在本目录 `skills/` 做薄镜像；**领域 skill 正文在 GitHub**。

## 目录

| 路径 | 用途 |
|------|------|
| `rules/` | 组织铁律（主控/主程/定界/子代理/三仓） |
| `workflow/` | 流水线与花名册核 |
| `profiles/` | 项目 **组织绑定**（路径指针，非花名册） |
| `projects/<Project>/` | **项目包**：`PROJECT.md` · `RULES.md` · **records/** |
| `templates/` | 分发/报告/ARCH/看板模板 |
| `skills/` | **仅组织岗** skill 薄镜像 |
| `docs/github/` | SKILL_MAP 模板（权威在 GitHub） |
| `docs/` | 组织说明、运维、交接 |
| `runs/` | 已废弃（见各项目 `records/`） |

SCL 快速入口：[projects/SCL/PROJECT.md](projects/SCL/PROJECT.md)  
游戏工程：`E:\Project\Game\S_\SCL`

## 主控会话

在 Cursor 中打开本仓库（或含本目录的工作区），用挂了 `cursor-admin` 的 Agent 对话（可命名「PC主控」）。  
接单时加载 `profiles/<Project>.md`；岗位记录写入 `projects/<Project>/records/`。

**防断档：** 见 [rules/03_memory_continuity.md](rules/03_memory_continuity.md)。新开对话先说 `project=SCL 续温`。
