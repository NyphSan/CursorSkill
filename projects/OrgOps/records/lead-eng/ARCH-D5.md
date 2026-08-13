# ARCH_MEMO · D5 长期环（含 D1 升格策略）

- **Project：** OrgOps
- **需求 ID：** D5（含排队项 D1）
- **主程：** 主控直干（昴指令：长期优化工作流、记 token/耗时、周期汇报、自主迭代合并 skill）
- **栈适配器：** 无

## 定层

- 层：运营工作流 + Skill 升格闸门 + 度量/汇报
- 理由：本仓没有 Cursor Automation 创建接口；GitHub 也还没有 Actions。要把「长期任务」落成 **可重复脚本 + 合入 main 后的 cron + 本环立即跑第 0 周**。

## 允许改的路径

- `projects/OrgOps/LOOP.md`（长期环章程）
- `projects/OrgOps/records/metrics/` · `records/reports/`
- `projects/OrgOps/records/**`（D1/D5 闸门文件、BOARD/BACKLOG）
- `Skill/SkillRules.md`（升格策略 = D1）
- `SKILL_MAP.md`（可机写区）
- `scripts/orgops-loop.sh` · `scripts/orgops_cycle.py`
- `.github/workflows/orgops-loop.yml`
- `AGENTS.md` · `README.md` · `cloud-resume.sh`（指向长期环）
- `skills/<方向>/<name>/{SKILL.md,SOURCE.md}`：**每周期最多 3 条**，且须过闸门

## 禁止改的路径（越界红线）

- 把 `CursorSkillSearch` 全量 `skills/` 合进本分支
- 无 LICENSE / 无 SOURCE.md / DIGEST 未标引入 的条目当已升格
- 脚本改主机环境、全局 git、代理
- 把真实 API token / 邮件正文写入仓
- 伪造 token 数字（拿不到就写 `unobserved`）
- 自动 `gh pr merge` 进 `main`（合 main 仍须昴确认或以后另开闸）
- 发 Gmail（汇报默认写 `records/reports/` + 对话；发信须昴另说）

## 硬规则

- 「自主合并 skill」= 侦察库 → 本仓 `skills/` + SKILL_MAP「已入权威」，**不是**跳过 PR 直推 `main`
- 每周期升格上限 **3**
- token：优先环境变量 `CURSOR_TOKENS_IN` / `CURSOR_TOKENS_OUT`；否则 `tokens_source=unobserved`
- 耗时：墙钟（cycle start/end）；本 Cloud run 另记一行 session

## 非目标

- 不在本刀创建 Cursor.com Automation（MCP 只能按 UUID 查询，不能新建）
- 不把 Gitea 章程拷进来
- 不升格观望/无许可条目

## 主程签字

- 结论：**批准开工**
