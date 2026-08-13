# Skill 写作与入库规则

本文件是 **GitHub CursorSkill** 的领域 skill 规范权威。组织派工纪律不写在这里。

## 本仓两条线

| 线 | 分支 | 放什么 |
|----|------|--------|
| 运营权威 | `main`（及经审核合入的 PR） | `SKILL_MAP.md`、本文件、`MCP/MCPRules.md`、`projects/OrgOps/` |
| 精选侦察 | `CursorSkillSearch` | `skills/<方向>/<name>/SKILL.md` + `SOURCE.md`、`DIGEST.md` |

`DIGEST.md` 不是收录批准书。升到本仓 `skills/` 并写入 SKILL_MAP「已入权威」须过下面 **升格** 闸门（长期环 `LOOP.md` 可自动执行；合入 `main` 仍走 PR）。

## 升格（D1 · 写死）

侦察库 `CursorSkillSearch` → 本仓权威索引，**每周期最多 3 条**。

**自动升格须全中：**

1. 当日（或周期读取的）`DIGEST.md` 建议列为 **引入**（不是观望 / 可忽略 / 不直接入库）
2. 侦察库能定位 `skills/<方向>/<name>/SKILL.md`
3. 同目录有 `SOURCE.md`，且写明 **LICENSE**（无许可、仅「观望因无 LICENSE」→ 不升）
4. 方向属于：`game-design` · `unreal` · `ui-design` · `2d` · `3d` · `workflow`
5. SKILL_MAP 里还不是「已入权威」
6. 只拷 `SKILL.md` + `SOURCE.md`（不整仓镜像 references/scripts，除非以后单独 ARCH）

**禁止自动升格：** 作弊/外挂/凭证窃取；无 DIGEST 引入；本周期已满 3 条。溢出写入 CYCLE 报告「未升格队列」。

## 目录约定

```text
skills/<方向>/<skill-name>/
  SKILL.md      ← 必须能定位到这一份
  SOURCE.md     ← 必须：原仓、LICENSE、收录理由、风险
  references/   ← 可选；大文档优先索引，不整仓镜像
  scripts/      ← 可选
```

方向目录（精选库）：`game-design` · `unreal` · `ui-design` · `2d` · `3d` · `workflow`

## 入库门槛（全中才可摘录）

1. **方向命中：** 游戏设计 / UE / 3D / 2D / UI / 研发工作流
2. **能定位到 `SKILL.md`**（或明确的 skill 包入口），不是只有 README 广告
3. **LICENSE 明确**；无许可 → 观望，不入库
4. **写 `SOURCE.md`：** 原仓 URL、作者、许可、摘录范围（全文 / 索引 / 不复制大 references）
5. **不是全网镜像：** 只摘与方向相关、可执行的部分
6. **安全：** 作弊、外挂、凭证窃取、未授权攻击类一律忽略

## SKILL.md 最低结构

- YAML frontmatter：`name`、`description`（触发词写进 description）
- 正文：何时用、前置、步骤、禁止项、验证
- 不把一次性路径、密钥、租约写进 skill

## 与三仓

- 改本文件 / SKILL_MAP / 领域 skill → **本仓 GitHub**
- 改主控派工、PM 闸门 → **Gitea CursorAiOrg**
- 改 SCL 用哪些 skill 干活 → SCL 的 `RULES.md`，不在本文件展开定界
