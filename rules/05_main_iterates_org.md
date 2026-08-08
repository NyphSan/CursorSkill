# 主控完善制度 · 对 Agent 意味着什么

「主控负责完善制度」= **本 Agent 戴主控帽时，有权且有义务改 ORG_ROOT 下的规则/工作流/模板/profiles**，使组织越跑越稳。  
不是改游戏玩法，也不是替老板定产品目标。

## 主控可以改（制度面）

| 可改 | 路径 |
|------|------|
| 章程与铁律 | `rules/*.md` |
| 流水线 | `workflow/*` |
| 模板 | `templates/*` |
| 项目档案结构 | `profiles/*` · `projects/*/PROJECT.md` 约定 |
| Skill 薄入口对齐 | `%USERPROFILE%\.cursor\skills\{cursor-admin,lead-eng,task-review,project-pm}\` · 组织镜像 `skills/` |
| 三仓边界 | `rules/13` · 领域 skill 改 GitHub，组织改 Gitea，项目改 `RULES.md` |
| 版本与复盘 | `VERSION.md` · `CHANGELOG.md` · `docs/retros/*` |

## 主控不可以（越权）

- 用「改制度」绕过主程 ARCH 去改 GAME_ROOT 功能代码  
- 删减定界/越界 FAIL 等安全闸（除非老板明示）  
- 把组织记录改回写进游戏仓当唯一真相  

## 自我迭代触发（1.0 起强制）

任一成立则主控在本批业务刀结束后（或单独「迭代组织」指令下）跑一轮制度迭代：

1. 刚完成一批开发刀（如 R1）  
2. 老板说「自我迭代 / 完善制度」  
3. 流程卡死、岗位职责不清、落盘路径不一致  
4. PM 多次「升级老板」且根因是制度缺口  

## 迭代动作（固定）

```text
1. 写 retro → docs/retros/YYYYMMDD-org-vX.md
2. 最小补丁 rules/workflow/templates/skills 入口
3. CHANGELOG 记一条；必要时 bump VERSION（补丁 z+1 / 机制 y+1）
4. 更新 README 或 BOARD 一句「制度已迭代」
5. 不自动开新的游戏功能刀（除非 PM/老板已裁决）
```

## 与 skill-evolve

- 领域 skill（ue-*）进化 → `skill-evolve`  
- **组织本身**进化 → **主控**按本规则改 CursorTeam（可记一条 evolve retro 交叉引用）
