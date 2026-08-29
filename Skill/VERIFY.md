# 已收集技能验证环

这是本仓的 **常驻验证任务**，对象是侦察分支 `CursorSkillSearch` 上的技能，不是 `main` 权威库。

## 岗位

- 岗位 ID：`verify-collected-skills`
- 目标：按日验证已收集技能是否还能用（结构、许可、来源、方向）
- 非目标：不去 GitHub 再搜新技能（那是 Automation `SkillSearch`）；不把侦察库合进 main；不发邮件
- 决策权：阻断项升级给昴；警告可自行记入报告
- 写域：`records/verify/` · 本文件 · `scripts/verify-collected-skills.py`
- 交付物：`records/verify/VERIFY-YYYY-MM-DD.md`、`RUNLOG.md`、`ESCALATION.md`（有阻断时）+ 对话一屏结论
- 退出：昴说停，或关掉本会话 timer / Automation

## 节奏

SkillSearch 每天 **01:00 UTC** 写 `DIGEST.md`。本环默认 **04:00 UTC** 跑，吃到当天增量。

```text
fetch origin CursorSkillSearch
  → python3 scripts/verify-collected-skills.py
  → 独立 github 仓 HEAD、许可归一、DIGEST 目录对账、相对上次差量
  → 写 VERIFY 报告 + RUNLOG 一行，并推本验证分支
  → 对话里给昴一屏结论
```

GitHub Action 合进默认分支后每天 04:20 UTC 抽检：上传产物，并把 `records/verify/` **写回默认分支**（技能仍只在侦察分支）。本会话 timer（`0 4 * * *`）在合入前负责把报告推到验证分支。timer 约 7 天过期，临期先退订再按本文件提示词续订。会话关掉后若还要对话升级，昴到 https://cursor.com/automations 按下方提示词新建（MCP 不能代建）。

## 闸门

对照 `Skill/SkillRules.md`（orgops PR 合入前以侦察库实际结构为准）：

1. `skills/<方向>/<name>/SKILL.md` 与 `SOURCE.md` 成对且非空
2. 方向 ∈ `game-design` · `unreal` · `ui-design` · `2d` · `3d` · `workflow`
3. SKILL frontmatter 有 `name` + 足够长的 `description`
4. SOURCE 写明 GitHub URL 和 LICENSE
5. 无外挂/作弊/凭证窃取
6. 独立 github 来源 HEAD 为 2xx/3xx；DIGEST 建议引入项在 `skills/` 下有同名目录
7. 方向目录与正文关键词大致对齐（未命中记警告，不单独阻断）

失败 = 报告标「未通过」，不自动删技能、不合 main。验证器自检（`tests/test_verify_collected_skills.py`）不拉侦察分支，应保持绿，也是 PR 合入门槛。PR 上的侦察抽检只出报告、不挡合入；合进默认分支后的每日 schedule 若有结构阻断会标红（升级信号）。

## 本会话怎么挂

Cloud Agent 用 timer（`/loop`）：

- 名称：`verify-collected-skills-daily`
- cron：`0 4 * * *`（04:00 UTC）
- 到期约 7 天。距 `expiresAt` 不足 3 天时：**先退订再按下述提示词续订**（同名 timer 去重会保留旧到期时间）。续订后立刻 `list_subscriptions` 核对名称、cron、提示词和到期日。

会话 timer 提示词：

```text
你是本仓技能验证环（岗位 ID: verify-collected-skills）。这不是新任务，继续每日验证 CursorSkillSearch 上已收集的技能。

执行：
1. 读 Skill/VERIFY.md 和 records/verify/LATEST.md
2. git fetch origin CursorSkillSearch
3. python3 scripts/verify-collected-skills.py
4. 把新报告提交并 push 到本验证分支 cursor/skill-verify-loop-f9ea（更新 PR #33）
5. 回复给昴一屏结论：技能数、阻断/警告数、独立来源 HEAD 结果、DIGEST 引入是否在库、许可待核数、是否有新增 YAML 断裂
6. YAML 非法、失效来源和许可待核写进 records/verify/ESCALATION.md 并在回复里升级

禁止：不合 main、不发邮件、不去搜新技能、不删仓里技能。阻断项升级；警告只记账。跑完确认 timer verify-collected-skills-daily 仍在，然后结束回合。
```

Cursor.com Automation **不能由 MCP 代建**。昴若要会话关掉后仍跑，到 https://cursor.com/automations 新建，提示词：

```text
project=OrgOps 验证已收集技能
git fetch origin CursorSkillSearch
python3 scripts/verify-collected-skills.py
把 records/verify/LATEST.md 的一屏结论写在回复里。
不要合 main，不要发邮件，不要去搜新技能。
阻断项升级，警告只记账。
```

## timer 唤醒后做什么

1. `git fetch origin CursorSkillSearch`
2. 若侦察 SHA 与 `records/verify/LATEST.md` 已记录的 ref 相同、且当日报告已存在：不要重跑抽检；只确认 timer 仍在后结束回合
3. `python3 scripts/verify-collected-skills.py`
4. 若脚本退出码非 0：读阻断项，对失效 URL 再人工看一次 SOURCE，写入 `ESCALATION.md`
5. 提交 `records/verify/`（本验证分支 `cursor/skill-verify-loop-f9ea`），推送，更新 PR
6. 回复一屏结论；确认 timer 仍在（临期续订），结束回合。目标保持打开，不要标 complete
