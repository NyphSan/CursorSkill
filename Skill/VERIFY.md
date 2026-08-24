# 已收集技能验证环

这是本仓的 **常驻验证任务**，对象是侦察分支 `CursorSkillSearch` 上的技能，不是 `main` 权威库。

## 岗位

- 岗位 ID：`verify-collected-skills`
- 目标：按日验证已收集技能是否还能用（结构、许可、来源、方向）
- 非目标：不去 GitHub 再搜新技能（那是 Automation `SkillSearch`）；不把侦察库合进 main；不发邮件
- 决策权：阻断项升级给昴；警告可自行记入报告
- 写域：`records/verify/` · 本文件 · `scripts/verify-collected-skills.py`
- 交付物：`records/verify/VERIFY-YYYY-MM-DD.md` + 对话一屏结论
- 退出：昴说停，或关掉本会话 timer / Automation

## 节奏

SkillSearch 每天 **01:00 UTC** 写 `DIGEST.md`。本环默认 **04:00 UTC** 跑，吃到当天增量。

```text
fetch origin CursorSkillSearch
  → python3 scripts/verify-collected-skills.py
  → 抽检 DIGEST「建议引入」的来源 URL
  → 写 VERIFY 报告并推本验证分支
  → 对话里给昴一屏结论
```

## 闸门

对照 `Skill/SkillRules.md`（orgops PR 合入前以侦察库实际结构为准）：

1. `skills/<方向>/<name>/SKILL.md` 与 `SOURCE.md` 成对且非空
2. 方向 ∈ `game-design` · `unreal` · `ui-design` · `2d` · `3d` · `workflow`
3. SKILL frontmatter 有 `name` + 足够长的 `description`
4. SOURCE 写明 GitHub URL 和 LICENSE
5. 无外挂/作弊/凭证窃取
6. DIGEST 引入项的来源 URL 抽检应返回 2xx/3xx

失败 = 报告标「未通过」，不自动删技能、不合 main。

## 本会话怎么挂

Cloud Agent 用 timer（`/loop`）：

- cron：`0 4 * * *`（04:00 UTC）
- prompt：见下方

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
2. `python3 scripts/verify-collected-skills.py`
3. 若脚本退出码非 0：读阻断项，对失效 URL 再人工看一次 SOURCE
4. 提交 `records/verify/`（本验证分支 `cursor/skill-verify-loop-f9ea`），推送，更新 PR
5. 回复一屏结论；然后重新确认 timer 仍在，结束回合
