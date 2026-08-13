# 项目规则 · OrgOps

**权威：** 本项目（OrgOps）+ 本仓 GitHub。  
**定界真相：** 当期 `records/lead-eng/ARCH-D*.md`。  
**协作人设：** `Command/人设.md`（昴 = 项目所有人；蕾姆 = 默认工作流负责人 / 主控）。人设不覆盖本文件的写域和红线。

## 模块分层（派工锚点）

```text
接单入口（AGENTS.md / README / 人设）
  → 项目包（PROJECT.md · RULES.md · records/）
  → Skill 规范与索引（Skill/SkillRules.md · SKILL_MAP.md）
  → MCP 规范（MCP/MCPRules.md）
  → 精选库（分支 CursorSkillSearch · skills/）
```

依赖方向写死：**入口 → 项目包 → 规范/索引 → 精选库**。  
禁止用精选库 DIGEST 覆盖 PROJECT/RULES；禁止把 Gitea 章程当本仓文件真相。

## 执行花名册

| 细分岗 | 入口 | 路径锚点（相对本仓根） |
|--------|------|------------------------|
| 主控 | `AGENTS.md` + 人设 | `projects/OrgOps/records/main/` |
| 主程定界 | ARCH 模板 | `projects/OrgOps/records/lead-eng/` |
| Skill 规范 | `Skill/SkillRules.md` | `Skill/` · `SKILL_MAP.md` |
| MCP 规范 | `MCP/MCPRules.md` | `MCP/` |
| 精选入库 | SkillRules + DIGEST 纪律 | 分支 `CursorSkillSearch` 的 `skills/` `DIGEST.md` |
| 提交 | github-repo | 本仓 GitHub；记录 `records/github/` |

**本项目没有 GAME_ROOT。** 不要套用 SCL 的业务/核心/测试岗去改 UE 工程。

## 边界速判

| 任务特征 | 归岗 |
|----------|------|
| `project=OrgOps` 续温、看板、派工、制度缺口登记 | **主控** |
| 本仓目录能不能改、升 main 的范围 | **主程 ARCH** |
| 写/改 SKILL.md、SOURCE.md、SKILL_MAP 行 | **Skill 规范岗** |
| 调 MCP、写 MCP 使用纪律 | **MCP 规范岗** |
| 每日侦察、DIGEST、从网摘录 skill | **精选入库**（默认只写 `CursorSkillSearch`） |
| 改 Gitea `rules/` `workflow/` 网络手册 | **越界** → 升级组织仓，本仓只记缺口 |
| 改 SCL 代码 / Content | **越界** → `project=SCL` 去游戏仓 |

## 禁止项（写死）

- 把组织章程、网络运维脚本、主机环境门禁手册拷进本仓当权威
- 无 ARCH 批准就把 `CursorSkillSearch` 全量 `skills/` 合进 `main`
- 无 LICENSE / 无 `SKILL.md` / 方向无关的条目当「已收录」
- 把密钥、token、邮箱正文、Gmail 邮件内容写入仓
- 主机环境默认写入（代理、全局 git、系统设置）
- 主会话换帽子假装已经派过子代理（除非老板写明本刀主控直干）

## 流水线

```text
ARCH → EXEC → REVIEW → github commit/push → PM
```

- 纯文档建仓刀（如 D0）允许主控直干，但必须先有 ARCH 书面批准
- 精选入库刀：默认目标分支 `CursorSkillSearch`，不碰 `main` 项目包
- 升 main：单独 ARCH，说明为什么这条 skill 进入权威索引

## 栈与远程

| 键 | 值 |
|----|-----|
| 栈适配器 | 无强制 |
| 运行测 | 文档刀：路径与链接自检；skill 刀：SKILL.md 可定位 + SOURCE.md 齐全 |
| 项目远程 | `https://github.com/NyphSan/CursorSkill` |
| 组织远程 | `https://git.bddream.site/nyph/CursorAiOrg`（只读引用） |
