# 三仓拆分 · 迁移计划

目标：**Skill Map → GitHub** · **组织/工作流 → Gitea** · **项目规则 → 各项目**

## 现状（2026-08-07）

- 本地 `E:\dev\CursorTeam` 同时 remote：`origin`（bare）、`gitea`（CursorAiOrg）、`github`（CursorSkill / AITeam 分支）
- 领域 skill 正文主要在 `%USERPROFILE%\.cursor\skills\`，组织仓仅有少量 `skills/*.SKILL.md` 镜像
- GitHub `main` 仅有 `Skill/SkillRules.md` 骨架；`AITeam` 分支仍是组织全量镜像（历史债）

## 目标态

```text
github.com/NyphSan/CursorSkill     ← SKILL_MAP + 领域 skills（main 或 skill-map 分支）
git.bddream.site/nyph/CursorAiOrg  ← rules/workflow/templates/org skills
SCLG/SCL.git（等项目仓）            ← 代码 + 可选 docs/ai/RULES.md
```

本地：

```text
E:\dev\CursorTeam\     ← git clone/pull gitea（ORG_ROOT）
E:\dev\CursorSkill\    ← git clone/pull github（可选开发镜像）
%USERPROFILE%\.cursor\skills\  ← 从 GitHub 同步的运行时
```

## 阶段

### P0 · 制度落盘（本刀 · v1.2.0）

- [x] `rules/13_repo_authority_split.md`
- [x] 更新 README / ORG / registry / rules/06
- [x] SCL：`profiles/SCL.md` 瘦身 + `projects/SCL/RULES.md`
- [x] `docs/github/SKILL_MAP.md` 模板（待迁入 GitHub main）

### P1 · GitHub Skill 仓建仓

**前置：** 老板确认 GitHub 目标分支（建议 `main` 专 skill，组织内容从 `AITeam` 脱钩）

1. 在 GitHub 建立目录：

```text
SKILL_MAP.md
Skill/SkillRules.md
skills/
  ue-framework/SKILL.md
  ue-scl-3c/SKILL.md
  …（从 ~/.cursor/skills 复制）
  skill-evolve/SKILL.md
  write-skill-md/SKILL.md
```

2. 从 `%USERPROFILE%\.cursor\skills\` 批量复制领域 skill（**不含** cursor-admin 等组织岗）
3. `SKILL_MAP.md` 与 `workflow/registry.md` 组织岗表对齐名字

### P2 · 组织仓瘦身

1. 删除 `skills/ue-*.SKILL.md`（保留 stub 指针文件或 README 说明「已迁 GitHub」）
2. `github` remote 不再 push 组织内容；仅 `gitea` push CursorAiOrg
3. 更新 `scripts/` 若有 sync-skills 脚本（待写）

### P3 · 项目规则归位

1. 每个活跃项目：`projects/<P>/RULES.md`（SCL 已完成样板）
2. 可选：PASS 后 gitea-repo 同步摘要到游戏仓 `docs/ai/RULES.md`
3. 新项目的 profile 只写绑定，不写花名册

### P4 · 日常同步

```text
改 skill 正文 → commit GitHub → 同步到 ~/.cursor/skills
改组织规则   → commit Gitea
改 SCL 定界   → projects/SCL/RULES.md + ARCH → Gitea records；代码 → SCL.git
```

## 回滚

- 各阶段独立 commit；P2 删除文件前打 tag `pre-skill-extract`
- 本地 `~/.cursor/skills` 始终可独立于 git 恢复

## 老板确认项（P1 前必问）

1. GitHub 用 `main` 还是新分支 `skill-map` 作为 skill 权威？
2. 是否现在就把 `AITeam` 上的组织内容从 GitHub 清掉（仅保留 skill）？
3. 是否编写 `scripts/sync-skills-from-github.ps1` 自动同步到本机？
