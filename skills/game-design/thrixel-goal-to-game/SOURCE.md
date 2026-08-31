# SOURCE — thrixel-goal-to-game

- **原仓**: https://github.com/thrixel/goal-to-game
- **原路径**: `skills/goal-to-game/SKILL.md` + `engines/{unity,threejs}/*`
- **许可**: MIT（源码 + SKILL.md）
  - 本仓 SKILL.md 为基于上游公开版本（5 commit，2026-08-12 latest）撰写的可移植摘录；遵循 MIT 许可，使用前请到原仓核对 LICENSE
- **最后更新**: 2026-08-12（commit `a4aefe1` — "Ship as a Claude Code plugin, unified /thrixel:goal-to-game"）
- **收录日期**: 2026-08-14（每日 cron 09:55+08:00 侦察）
- **触发词**: "make a 3D game" / "Unity prototype" / "three.js playable prototype" / "generate GLB meshes" / "Thrixel" / "AAA-quality assets" / "vertical slice with realistic assets"

## 为什么收录

1. **MIT 许可 + 紧贴 2026-08-12 的活跃 commit**（5 commits in 2 weeks；08-03 code release → 08-12 plugin 重构）
2. **本仓 game-design 首个「AI 生成 AAA 级 3D 资产 + 编码代理」端到端流程** — 覆盖 `MengTo/threejs-*` / `mint-threejs-skills` 单点工具之外的「资产质量」第三象限
3. **三路径决策树（Architect / Sculptor / Architect→Detailer）** 是 AI mesh 领域中少见的明示工程纪律 — 大多数同类仓只教"prompt 怎么写"，本条目教"什么时候不该用 prompt"
4. **`thrixel_group_parts` 强制步骤** — 解决 AI mesh 在引擎侧的 N 个 draw call 死亡陷阱，对所有 3D / Unity / three.js 用户有方法论价值
5. **`focus_on_node_names` 增量编辑模式** — `edit_model` 保留未指定节点位级一致，这是 AI mesh 编辑的"最小可工作 delta"模型
6. **价格 / 配额驱动的 build 计划模型** — 教用户（和 agent）如何按 Cube 预算规划资产列表，避免常见的"边做边超支"陷阱

## 关键工程细节

- **运行环境**：Claude Code + Thrixel MCP + Unity 或 three.js 工具链
- **强制 API**：`thrixel_start_project` 先于一切生成；`thrixel_account_status`（真实 cap）；`thrixel_pricing`（真实价格）；`thrixel_create_model` / `edit_model` / `detail_model` / `retexture_model` / `reduce_triangles` / `group_parts` / `inspect_model` / `upgrade_plan` / `buy_cubes`
- **可选资产预算**：`plus`（默认）/ `balanced`（仅用户明示）
- **决策门**：(a) 自由版 vs 付费版 → 是否在第一次生成前弹出升级建议；(b) Cube 用尽 → 停止提交，先展示当前可玩版本；(c) Plan the asset list FIRST（user 化决策之前）
- **Mesh 后处理必选**：`thrixel_group_parts` → 不可绕过（节点过多 → draw call 爆炸）

## 战略观察：上游持有的强观点

原仓 SKILL.md 持强烈工作流意见（"NEVER pass image"、"Always plus"、"Recommend upgrade ONCE then move on"、"Out-of-cubes 也要展示当前进度"），不能与其他"build me a game" 类技能混合使用，否则会冲突。一旦引入即主导整个 3D 原型流程。

## 与本仓现有条目的互补

| 现有条目 | 与本条目的关系 |
|---|---|
| `mint-threejs-skills` / `threejs-fundamentals`（3D） | 互补：本条目专攻「AI 资产 + 编码代理」三路径决策；three.js 条目教纯 API |
| `mengto-build-game-*`（game-design） | 互补：本条目偏资产生产；mengto 系列偏玩法实现 |
| `heycat-*`（2D） | 本条目仅 3D，不重叠 |
| `dcc-mcp-blender` / `blender-modeler`（3D 视觉） | 互补：本条目是 Thrixel 专属云 API；dcc-mcp-blender 是 Blender 本地工具集 |
| `gamedev-create-game-assets`（2D，跨引擎） | 概念同源：本条目是 3D 版本；该条目偏 2D 美术指导 |

## 收录摘要

本 SKILL.md 重写为可移植的 6 段工作流（Setup → Path Decision → Asset-List Planning →
Upgrade Offer → Generation Loop → Mesh Grouping），并保留所有强观点（NEVER image / Always
plus / Hard-stop on free-plan upgrade prompt / Out-of-cubes 也要展示）。完整 MCP setup +
`engines/unity.md` + `engines/threejs/threejs.md` 的引擎特定代码模板未复制，需要时到原仓安装。
