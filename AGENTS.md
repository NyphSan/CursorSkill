# AGENTS

默认中文。人设见 `Command/人设.md`（昴 = 项目所有人；蕾姆 = 工作流负责人）。人设不覆盖本仓写域。

## 接单（强制）

新开对话第一句带项目：

```text
project=OrgOps
```

可重复只读命令（本仓根）：

```bash
bash cloud-resume.sh OrgOps
```

然后按顺序读盘，回复顶部给续温块：

1. `projects/OrgOps/PROJECT.md`
2. `projects/OrgOps/RULES.md`
3. `projects/OrgOps/records/main/BOARD.md`
4. `projects/OrgOps/records/main/BACKLOG.md`

`project=SCL` **不在本仓**。去组织仓 / 游戏仓续温，不要在本仓发明 SCL 看板。

## 本仓写域

| 可写 | 不要写 |
|------|--------|
| `projects/OrgOps/` · `SKILL_MAP.md` · `Skill/` · `MCP/` · 本文件 | Gitea 组织章程镜像 |
| 经 ARCH 批准的 skill 升格 | 无批准把 `CursorSkillSearch` 全量合进 `main` |
| | SCL 游戏代码 / Content；主机环境默认写入 |

## 规范

- Skill 入库：`Skill/SkillRules.md`
- MCP：`MCP/MCPRules.md`
- 地图：`SKILL_MAP.md`
- 长期环：`projects/OrgOps/LOOP.md` · `bash scripts/orgops-loop.sh`
