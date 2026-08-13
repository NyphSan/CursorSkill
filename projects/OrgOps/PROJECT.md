# 项目 · OrgOps（CursorSkill 组织运营）

| 键 | 值 |
|----|-----|
| ProjectId | `OrgOps` |
| **权威仓** | GitHub [`NyphSan/CursorSkill`](https://github.com/NyphSan/CursorSkill) |
| **PROJECT_ROOT** | 本仓根目录 |
| **ORG 项目根** | `projects/OrgOps/` |
| **记录根** | `projects/OrgOps/records/` |
| **项目规则** | `projects/OrgOps/RULES.md` |
| Skill Map | 本仓根 `SKILL_MAP.md` |
| 人设 | `Command/人设.md` |
| 精选库分支 | `CursorSkillSearch`（侦察 / DIGEST，不自动等于 `main`） |
| 组织章程仓 | Gitea [CursorAiOrg](https://git.bddream.site/nyph/CursorAiOrg)（本仓不镜像） |

## 本项目是什么

OrgOps 管 **本 GitHub 仓怎么接单、怎么收录 skill、怎么用 MCP**。  
它不是游戏工程 SCL，也不是把 CursorTeam 章程搬到 GitHub。

三仓对照（写死）：

| 权威 | 仓 | OrgOps 碰不碰 |
|------|-----|----------------|
| Skill Map / 领域 skill / 写作规范 | **本仓 GitHub** | **碰**（本项目写域） |
| 组织章程 / 派工纪律 / 网络运维 | Gitea CursorAiOrg | **不碰**（升级组织主控） |
| SCL 玩法 / 模块 / Content | SCL 项目仓 | **不碰** |

## 接单

```text
project=OrgOps
  → 读本文件
  → 读 RULES.md
  → 读 records/main/BOARD.md + BACKLOG.md
  → 给出续温块后再派工或直干
```

Cloud / 本仓根可重复命令（只读，不改主机环境）：

```bash
bash cloud-resume.sh OrgOps
```

SCL 不在本仓。若用户说 `project=SCL`，应到组织仓 / 游戏仓续温，不要在本仓假装 SCL 看板存在。

## 记录目录（按岗位）

| 岗位 | 目录 | 典型文件 |
|------|------|----------|
| 主控 | `records/main/` | `BOARD.md` · `BACKLOG.md` · 分发单 |
| 主程 | `records/lead-eng/` | `ARCH-D#.md` |
| 执行 | `records/exec/` | `EXEC-D#.md` |
| 审核 | `records/review/` | `REVIEW-D#.md` |
| PM | `records/pm/` | `PM-D#.md` |
| GitHub 提交 | `records/github/` | `COMMIT-D#.md` |
| 杂记 | `notes/` | 非闸门备忘 |

## 开发工作约定

1. **改本仓运营文件：** 路径相对 **PROJECT_ROOT**（本仓根）。
2. **岗位记录：** 只写 **记录根** 下对应子目录。
3. **精选 skill 正文：** 默认在 `CursorSkillSearch` 的 `skills/<方向>/<name>/`；升到 `main` 须单独刀，遵守 `Skill/SkillRules.md`。
4. **组织铁律变更：** 不要写进本仓冒充权威；记一条缺口，升级 Gitea。
