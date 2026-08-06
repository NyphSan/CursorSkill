# CursorTeam · PC 组织目录

**权威根（ORG_ROOT）：** `E:\dev\CursorTeam`

本目录承载：组织章程、规则、工作流、项目档案（profiles）、模板、**全部运行记录**。  
与具体游戏工程解耦；SCL 等只是 `profiles/` 下的档案。

Cursor 仍通过用户级 skill（`%USERPROFILE%\.cursor\skills\`）发现入口；  
那些 SKILL 只做薄入口，**读写一律指向本目录**。

## 目录

| 路径 | 用途 |
|------|------|
| `rules/` | 组织铁律（主控/主程/定界/子代理） |
| `workflow/` | 流水线与花名册核 |
| `profiles/` | 项目档案（SCL、_default…） |
| `templates/` | 分发/报告/ARCH/看板模板 |
| `runs/<Project>/` | **所有**执行/审核/PM/ARCH 记录 |
| `skills/` | 组织相关 skill 正文镜像（便于版本管理） |
| `docs/` | 组织说明、交接 |

## 主控会话

在 Cursor 中打开任意工作区，用挂了 `cursor-admin` 的 Agent 对话（可命名「PC主控」）。  
接单时加载 `profiles/<Project>.md`；报告写入 `runs/<Project>/`。
