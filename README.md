# CursorTeam · PC 组织目录

**权威根（ORG_ROOT）：** `E:\dev\CursorTeam`  
**组织版本：** 见 [VERSION.md](VERSION.md)（当前 ≥ **1.0**）

本目录承载：组织章程、规则、工作流、项目档案（profiles）、模板、**全部运行记录**。  
与具体游戏工程解耦；SCL 等只是 `profiles/` 下的档案。

**主控完善制度：** 见 [rules/05_main_iterates_org.md](rules/05_main_iterates_org.md)；批末 [workflow/BATCH_CLOSEOUT.md](workflow/BATCH_CLOSEOUT.md)。

Cursor 仍通过用户级 skill（`%USERPROFILE%\.cursor\skills\`）发现入口；  
那些 SKILL 只做薄入口，**读写一律指向本目录**。

## 目录

| 路径 | 用途 |
|------|------|
| `rules/` | 组织铁律（主控/主程/定界/子代理） |
| `workflow/` | 流水线与花名册核 |
| `profiles/` | 项目档案索引（SCL、_default…） |
| `projects/<Project>/` | **项目包**：GAME_ROOT + **各岗位 records/** |
| `templates/` | 分发/报告/ARCH/看板模板 |
| `skills/` | 组织相关 skill 镜像 |
| `docs/` | 组织说明、交接 |
| `runs/` | 已废弃（见各项目 `records/`） |

SCL 快速入口：[projects/SCL/PROJECT.md](projects/SCL/PROJECT.md)  
游戏工程：`E:\Project\Game\S_\SCL`

## 主控会话

在 Cursor 中打开本仓库（或含本目录的工作区），用挂了 `cursor-admin` 的 Agent 对话（可命名「PC主控」）。  
接单时加载 `profiles/<Project>.md`；岗位记录写入 `projects/<Project>/records/`。

**防断档：** 见 [rules/03_memory_continuity.md](rules/03_memory_continuity.md)。新开对话先说 `project=SCL 续温`。
