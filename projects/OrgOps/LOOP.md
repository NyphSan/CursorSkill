# OrgOps 长期环

这是本仓的 **常驻任务**，不是一次性刀。

```text
每天（DIGEST 之后）
  → 续温
  → 扫 CursorSkillSearch/DIGEST 的「引入」
  → 过闸门则升格 ≤3 条到本仓 skills/ + SKILL_MAP
  → 记耗时 / token（能拿到才写数字）
  → 写 CYCLE 报告
  → 推 standing 分支；合 main 仍走 PR
```

## 怎么跑

本机 / Cloud Agent：

```bash
bash cloud-resume.sh OrgOps
bash scripts/orgops-loop.sh
```

合入 `main` 后：GitHub Action `orgops-loop` 每天 **03:20 UTC**（北京时间 11:20，接在 DIGEST 11:04+08 后面）。

Cursor Automation：本 MCP **不能代建**。昴若要 Cloud Agent 定时跑，到 [cursor.com/automations](https://cursor.com/automations) 新建，提示词用：

```text
project=OrgOps 续温
bash cloud-resume.sh OrgOps
bash scripts/orgops-loop.sh
把 CYCLE 报告结论写在回复里。不要合 main，不要发邮件。
```

## 闸门（升格）

全文见 `Skill/SkillRules.md` §升格。摘要：DIGEST 引入 + SKILL.md + SOURCE.md 且 LICENSE 明确 + 方向命中 + 本周期未满 3 条。

## 汇报

- 每周期：`projects/OrgOps/records/reports/CYCLE-YYYY-MM-DD.md`
- 台账：`projects/OrgOps/records/metrics/ledger.csv`
- 对话里给昴看 CYCLE 的「一屏结论」

## 停

昴说「停止长期环」或关掉 GitHub Action / Automation。看板闸门改为停止。
