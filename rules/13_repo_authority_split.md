# 三仓权威拆分（≥1.2.0）

CursorTeam 不再「一个目录三远程同推」。**权威按内容类型分仓**，本地 `ORG_ROOT` 仍是运行时聚合点。

## 三仓对照

| 权威 | 远程 | 本地路径（建议） | 管什么 |
|------|------|------------------|--------|
| **Skill Map** | `https://github.com/NyphSan/CursorSkill` | `%USERPROFILE%\.cursor\skills\`（运行时）<br>可选镜像 `E:\dev\CursorSkill\` | 领域 skill 正文、`SKILL_MAP`、skill-evolve / write-skill-md、ue-* 等 |
| **组织** | `https://git.bddream.site/nyph/CursorAiOrg` | `E:\dev\CursorTeam\`（ORG_ROOT） | 章程 `rules/`、流水线 `workflow/`、模板 `templates/`、组织岗 skill 薄镜像、运维 `docs/ops/`、`scripts/`、`VERSION` |
| **项目** | 各项目 Git（见 `PROJECT.md`） | `GAME_ROOT` + `projects/<Project>/` | 项目定界、执行花名册、ARCH 定界、岗位 records、项目专属约定 |

## 边界（写死）

### GitHub · Skill Map

**放：**

- `SKILL_MAP.md`（全量 skill 索引：name → 路径 → 触发词 → 归属项目/通用）
- 领域 skill 目录：`ue-*`、`second-self`、`skill-evolve`、`write-skill-md` 等 **完整 SKILL.md**
- Skill 写作/进化规范（`Skill/SkillRules.md` 等）

**不放：**

- 组织章程、派工纪律、PM 闸门
- 项目 ARCH / 模块分层 / 游戏仓路径
- 网络运维手册（属组织仓）

### Gitea · CursorAiOrg

**放：**

- `rules/` · `workflow/` · `templates/` · `VERSION` · `CHANGELOG`
- `profiles/<Project>.md`：**仅组织绑定**（ProjectId、ORG_ROOT、GAME_ROOT、记录根、远程 URL 指针）
- `projects/<Project>/PROJECT.md` · `records/`（岗位落盘，仍属组织运行时）
- `skills/`：**仅组织岗薄镜像**（`cursor-admin`、`lead-eng`、`task-review`、`project-pm`、`gitea-repo`、`network-ops`）
- `docs/ops/` · `scripts/` · `tools/cursor-session/`

**不放：**

- 领域 skill 正文（ue-* 等）— 只保留 **名字引用**，正文在 GitHub
- 项目执行花名册 / 模块分层 — 下沉 `projects/<Project>/RULES.md`

### 项目仓 / 项目包

**放：**

- `projects/<Project>/RULES.md`：执行花名册、模块分层、边界速判、项目专属禁止项
- 可选：游戏仓 `docs/ai/RULES.md` 镜像（与 RULES.md 同步，由 gitea-repo 岗维护）
- `records/lead-eng/ARCH-*.md`：当期定界真相

**不放：**

- 改组织章程（升级主控 → CursorAiOrg）
- 改全局 skill 正文（升级 skill-evolve → GitHub）

## 运行时加载顺序

```text
主控接单 project=<Id>
  → profiles/<Id>.md          # 组织绑定（Gitea）
  → projects/<Id>/PROJECT.md  # 项目元数据
  → projects/<Id>/RULES.md    # 项目规则（项目权威）
  → workflow/registry.md      # 组织岗 + 指向 SKILL_MAP
  → GitHub SKILL_MAP          # 领域 skill 正文路径
  → ~/.cursor/skills/         # Cursor 实际发现入口
```

## 推送纪律（gitea-repo 岗）

| 变更类型 | push 目标 | 禁止 |
|----------|-----------|------|
| rules/workflow/templates/组织 skill 薄镜像 | **gitea** CursorAiOrg | 不要 push 到 github 当组织镜像 |
| ue-* / skill-evolve / SKILL_MAP | **github** CursorSkill | 不要混进组织 commit |
| 游戏代码 / Content | **项目远程** | 不要混组织改 |
| projects/*/records | **gitea**（组织运行时） | 与游戏 commit 分开 |

**一次 commit 只做一类权威变更。**

## 迁移

分阶段见 `docs/ops/REPO_SPLIT_MIGRATION.md`。完成前：组织仓 `skills/ue-*` 视为 **待迁出副本**，以 GitHub 为准。

## 与现有规则衔接

- 组织迭代：`rules/05_main_iterates_org.md`（只改 Gitea 仓）
- Gitea 岗：`rules/06_gitea_repo_admin.md`（三仓 push 表）
- 花名册：`workflow/registry.md`（组织岗 vs Skill Map 分表）
- 定界铁律：`rules/01`（ARCH 在项目；章程在组织）
