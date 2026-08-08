# ORG_ROOT

```text
ORG_ROOT = E:\dev\CursorTeam          ← Gitea CursorAiOrg（组织权威）
SKILL_ROOT = %USERPROFILE%\.cursor\skills\  ← GitHub CursorSkill（领域 skill 运行时）
```

| 类型 | 路径 | 权威仓 |
|------|------|--------|
| 规则 | `ORG_ROOT\rules\` | Gitea |
| 工作流 | `ORG_ROOT\workflow\` | Gitea |
| 档案绑定 | `ORG_ROOT\profiles\` | Gitea |
| 模板 | `ORG_ROOT\templates\` | Gitea |
| **项目包** | `ORG_ROOT\projects\<Project>\` | 规则在 `RULES.md`；records 在 Gitea |
| Skill Map | GitHub `SKILL_MAP.md` | GitHub |
| 废弃 | `ORG_ROOT\runs\` | — |

三仓详表：`rules/13_repo_authority_split.md`

## 项目包结构

```text
projects/<Project>/
  PROJECT.md          ← GAME_ROOT 等
  records/
    main/             ← 主控
    lead-eng/         ← 主程
    exec/             ← 执行
    review/           ← 审核
    pm/               ← PM
  notes/
```

SCL 示例：`projects\SCL\PROJECT.md` → GAME_ROOT = `E:\Project\Game\S_\SCL`
