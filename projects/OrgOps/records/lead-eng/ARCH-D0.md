# ARCH_MEMO · D0 建仓定界

- **Project：** OrgOps
- **需求 ID：** D0
- **主程：** 主控直干（本仓尚无独立 lead-eng 运行时；建仓刀不换帽假装子代理，书面记为直干）
- **栈适配器：** 无（文档与索引，不改游戏工程）

## 定层

- 层：本仓运营骨架（GitHub `NyphSan/CursorSkill` / `main` 线）
- 理由：用户开场 `project=OrgOps`，落盘中无该项目包；三仓规则要求 GitHub 管 Skill Map / 领域规范，不把 Gitea 组织章程整棵搬过来。

## 允许改的路径

- `projects/OrgOps/**`（项目包、records）
- `SKILL_MAP.md`（本仓 skill 索引权威）
- `Skill/SkillRules.md`、`MCP/MCPRules.md`
- `AGENTS.md`、`README.md`（接单入口）
- 根目录 `Readme`：改为指向 `README.md`，避免双份正文

## 禁止改的路径（越界红线）

- 把 `AITeam` / `cursor/repo-authority-split-*` 上的 `rules/` `workflow/` `docs/ops/` 整棵拷进 `main`
- 从 `CursorSkillSearch` 批量拷贝 `skills/**`（须单独刀 + SOURCE/LICENSE 审核）
- 任何 SCL `GAME_ROOT`、游戏模块、uasset
- 主机环境（代理 / git 全局 / 系统设置）
- `Command/人设.md` 正文（本刀只引用，不改协作人设）

## 硬规则

- 一次 commit 只做一类权威变更：本刀 = **项目包 + GitHub skill 仓入口**，不是组织章程迭代
- 记录写 `projects/OrgOps/records/`，不写已废弃的 `runs/`
- 本仓远程是 GitHub；提交岗叫 **github-repo**，不假装能推 Gitea
- 续温只认落盘文件，不认聊天记忆

## 非目标

- 不合并 300+ 精选 skill 到 `main`
- 不定 SCL 玩法 / 模块分层
- 不改 CursorAiOrg 章程（那是 Gitea 组织仓）
- 不在本刀做 skill-digest cron

## 主程签字

- 结论：**批准开工**（D0 建仓）
