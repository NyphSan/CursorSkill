# CursorSkill

面向 **游戏设计 / 虚幻（UE）/ 3D·2D·UI / 研发工作流** 的 Agent Skills 仓，并带 **OrgOps** 运营项目。

本仓不是全网镜像：精选摘录在分支 `CursorSkillSearch`；`main` 先放接单入口、Skill/MCP 规范与地图。

## 接单

```text
project=OrgOps
```

```bash
bash cloud-resume.sh OrgOps
```

读：`projects/OrgOps/PROJECT.md` → `RULES.md` → `records/main/BOARD.md`。  
人设：`Command/人设.md`。工作区入口：`AGENTS.md`。长期环：`projects/OrgOps/LOOP.md`。

## 结构

```text
cloud-resume.sh        # 只读续温：bash cloud-resume.sh OrgOps
scripts/orgops-loop.sh # 长期环一轮：升格 + 度量 + CYCLE 报告
AGENTS.md              # 接单 / 写域
SKILL_MAP.md           # skill 索引（main 权威）
Command/人设.md
Skill/SkillRules.md    # 写作与入库
MCP/MCPRules.md        # MCP 纪律
projects/OrgOps/       # 本仓运营项目包 + records + LOOP.md
skills/                # 已升格摘录；全量侦察仍在分支 CursorSkillSearch
```

## 两条线

| 线 | 分支 | 说明 |
|----|------|------|
| 运营 | `main` | OrgOps、规范、地图 |
| 侦察 | `CursorSkillSearch` | `skills/` 摘录、`DIGEST.md` 日更 |

升到 `main` 须 OrgOps 单独刀，见 `Skill/SkillRules.md`。

## 安装（Cursor）

精选库在 `CursorSkillSearch`。需要某条技能时，把该目录放到 Cursor skills 路径，例如：

```bash
mkdir -p .cursor/skills
# 从 CursorSkillSearch 检出后：
cp -R skills/ui-design/<skill-name> .cursor/skills/
```

以原仓库安装说明为准；本仓为摘录。各技能许可见其 `SOURCE.md`。

## 不是本仓的事

- 组织章程 / 派工铁律 → Gitea CursorAiOrg
- SCL 游戏工程 → SCL 项目仓（`project=SCL`）
