# OrgOps · 开发需求清单

- **来源需求：** 用户开场 `project=OrgOps`
- **主控会话：** 2026-08-13 Cloud Agent（Orgops project）

| ID | 标题 | 定层 | 执行 | DoD | 依赖 | 状态 |
|----|------|------|------|-----|------|------|
| D0 | 建仓：项目包 + 接单入口 + Skill/MCP 规范骨架 | 本仓运营骨架 | 主控直干 | `project=OrgOps` 能续温；main 不混入组织章程树 / 全量 skills | — | 待确认 |
| D1 | 定 `main` vs `CursorSkillSearch` 升格策略 | 规范 | 待派 | ARCH 写清何时一条 skill 进入 SKILL_MAP/`main` | D0 | 排队 |
| D2 | SKILL_MAP 与精选库对账（抽样，不合全量） | 索引 | 待派 | 地图能指向 Search 分支真实路径；标明未升格 | D0 | 排队 |
| D3 | MCP 规则对照本环境已挂接服务做一次盘点 | MCP | 待派 | 规则点名可用服务与禁写项 | D0 | 排队 |

状态机：`排队 → 执行中 → 待审核 → 待PM → 待确认 → 完成`；FAIL 回到 `执行中`。
