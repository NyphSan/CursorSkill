# OrgOps · 开发需求清单

- **来源需求：** 用户开场 `project=OrgOps`
- **主控会话：** 2026-08-13 Cloud Agent（Orgops project）

| ID | 标题 | 定层 | 执行 | DoD | 依赖 | 状态 |
|----|------|------|------|-----|------|------|
| D0 | 建仓：项目包 + 接单入口 + Skill/MCP 规范骨架 | 本仓运营骨架 | 主控直干 | `project=OrgOps` 能续温；main 不混入组织章程树 / 全量 skills | — | 待确认 |
| D4 | `cloud-resume.sh` 只读续温入口 | 接单入口 | 主控直干 | `bash cloud-resume.sh OrgOps` exit 0 | D0 | 待确认 |
| D1 | 定 `main` vs `CursorSkillSearch` 升格策略 | 规范 | 主控直干 | SkillRules §升格；每周期 ≤3 | D0 | 完成（并入 D5） |
| D5 | 长期环：度量 / 周期汇报 / 自主升格 | 工作流 | 主控直干 | LOOP.md + 脚本 + 第 0 周 CYCLE | D1 | 待确认 |
| D2 | SKILL_MAP 与精选库对账（抽样，不合全量） | 索引 | 待派 | 地图能指向 Search 分支真实路径；标明未升格 | D0 | 排队 |
| D3 | MCP 规则对照本环境已挂接服务做一次盘点 | MCP | 待派 | 规则点名可用服务与禁写项 | D0 | 排队 |

状态机：`排队 → 执行中 → 待审核 → 待PM → 待确认 → 完成`；FAIL 回到 `执行中`。
