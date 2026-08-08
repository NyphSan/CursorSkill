# SKILL_MAP · Cursor Agent Skills

**权威仓：** `https://github.com/NyphSan/CursorSkill`  
**运行时：** `%USERPROFILE%\.cursor\skills\<name>\SKILL.md`  
**组织岗索引：** Gitea `workflow/registry.md`（不含本文领域表）

> 本文件模板在组织仓 `docs/github/SKILL_MAP.md`；**迁入 GitHub 后以 GitHub 为准**。

## 通用 / 元 skill

| name | 目录 | 触发 / 用途 |
|------|------|-------------|
| `skill-evolve` | `skills/skill-evolve/` | 主 skill 跑完 → 复盘进化 |
| `write-skill-md` | `skills/write-skill-md/` | 写 SKILL.md 脚手架 |

## UE / 领域 skill（通用）

| name | 目录 | 用途 |
|------|------|------|
| `ue-framework` | `skills/ue-framework/` | UE 工程框架适配 |
| `ue-uasset-type-identify` | `skills/ue-uasset-type-identify/` | uasset 类型识别 |
| `ue-pie-validate` | `skills/ue-pie-validate/` | PIE / 运行测 |
| `ue-character` | `skills/ue-character/` | 角色 / 属性 |
| `ue-ai-state-tree` | `skills/ue-ai-state-tree/` | StateTree / AI |
| `ue-rendering` | `skills/ue-rendering/` | 渲染 |
| `second-self` | `skills/second-self/` | 端到端 solo 交付 |

## 项目叠加 skill

| name | 目录 | 项目 |
|------|------|------|
| `ue-scl-3c` | `skills/ue-scl-3c/` | SCL |
| `scl-pm` | `skills/scl-pm/` | SCL PM 委托 |

项目 **用哪些 skill、对应路径** → 各项目 `projects/<P>/RULES.md`（不在此重复定界）。

## 组织岗 skill（不在本仓正文）

以下 skill **薄入口在 Gitea CursorAiOrg** `skills/`，正文读写指向 `ORG_ROOT`：

`cursor-admin` · `lead-eng` · `task-review` · `project-pm` · `gitea-repo` · `network-ops`

## 维护

- 新增领域 skill：先 `write-skill-md` → 入本 map → commit **GitHub**
- 改组织流程：改 **Gitea**，不要写进 skill 正文
- 改项目花名册：改 **projects/<P>/RULES.md**
