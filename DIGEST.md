# 技能侦察 DIGEST — 2026-08-11（凌晨手工复跑，相对基线 08-10 01:00Z）

- 侦察时间：2026-08-11T00:55+08:00（手工复跑，覆盖 08-10 01:00Z 之后的窗口）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：远端 `CursorSkillSearch` 2026-08-10 01:00Z 的 DIGEST（296 SKILL，已快进到本地）
- 本仓入库：精选 **302** 个 `SKILL.md`（相对 296：+6；本轮新增 5 个 SKILL + 1 个跨仓索引）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

种子仓仍无方向相关新增。本轮抓的是 6 条 **08-04 → 08-11 期间出现实质更新 / 验证可定位到 SKILL.md** 的相关条目：
- `kevinpbuckley/unreal-engine-skills`（**watch list 升级 → 引入**）：61 SKILL、全仓 216 markdown，UE 5.8 重定向已经完成
- `loomle/loomle`（**新见引入**）：MIT，UE 5.7-5.8，本地优先 + SAL 三调用 MCP，`skills/` 目录 + `agent_skill` 动态加载
- `db-lyon/ue-mcp`（**本仓补齐**）：随 npm 包分发的 5 个 SKILL.md，本仓此前已收录 workflow / blueprint；本轮补齐 niagara / native-cpp / epic-routing 三条
- `nextlevelbuilder/ui-ux-pro-max-skill`（**新见引入**）：115k★ MIT，检索驱动，含 Cyberpunk UI / Pixel Art / HUD & Sci-Fi FUI / Vaporwave / Spatial UI / 3D & Hyperrealism 等**游戏相关**风格

无方向相关的 `mouadja02/skills` 近日新增（Postgres / HTTP2 / NO_PROXY / SEO 等）依旧记数量、不展开。

## 建议引入（本轮增量 = 6）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| kevinpbuckley-unreal-engine-skills | UE | 61 个 UE 5.8 域知识 SKILL，216 markdown 文件，覆盖 C++/Gameplay/BP/动画/关卡/VFX/UMG/工具 | https://github.com/kevinpbuckley/unreal-engine-skills | 2026-08-04 完成全仓审计 + UE 5.8 重定向；**watch list 升级**；同作者另起 VibeUE 是 MCP 层，本仓 `vibeue-blueprints/materials` 已收 | **引入**（已摘录索引 + 用法，URL 链接到原仓） |
| loomle-ue-sal-mcp | UE | 本地 UE 编辑器 MCP + SAL 三调用（schema/query/patch），支持 BP/Graph/StateTree/Widget/UMG，含 Resident Skill | https://github.com/loomle/loomle | MIT，UE 5.7-5.8，08-11 仍在动；结构保留型编辑（pin 重建鲁棒）+ 强制 dry-run | **引入**（已摘录 SAL 三调用 + 选型对比） |
| ue-mcp-niagara | UE | ue-mcp 包随附：Niagara emitter/module/renderer 读写，运行时从 BP/C++ 驱动 | https://github.com/db-lyon/ue-mcp | 原仓 08-05 起把 Agent Skills 节扩到 5 条；本仓已收 workflow / blueprint；本轮补齐 niagara | **引入**（已摘录 emit/系统/模块/曲线/DI 范式） |
| ue-mcp-native-cpp | UE | Bridge C++ 扩展：最小 handler 范式、post-back 契约、仅编辑器目标隔离 | 同上 | MIT；说明如何在 `Source/ue-mcpEditor/` 加新 handler 而不动 npm wrapper | **引入**（已摘录 handler 模板 + 编译边界） |
| ue-mcp-epic-routing | UE | 决策表：什么操作走 native handler 什么走 Epic Toolset `epic_*` | 同上 | 与 `ue-mcp-blueprint` 的 DSL 节互为镜像；UE 5.8+ 决定性收益在 graph body | **引入**（已摘录决策矩阵 + 回退模式） |
| nextlevelbuilder-ui-ux-pro-max | UI·3D | 检索驱动设计智能 skill，84 风格/192 调色/74 字体，含 Cyberpunk/Pixel-Art/HUD-FUI/Spatial-UI/3D-Hyperrealism | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | 115k★ MIT；**游戏相关风格单列明确**；与 `frontend-design` 互补：检索驱动 vs 品味驱动 | **引入**（已摘录 game-relevant 风格覆盖 + 设计系统生成调用） |

本仓路径：
- `skills/unreal/kevinpbuckley-unreal-engine-skills/`（SKILL.md + SOURCE.md）
- `skills/unreal/loomle-ue-sal-mcp/`
- `skills/unreal/ue-mcp-niagara/`
- `skills/unreal/ue-mcp-native-cpp/`
- `skills/unreal/ue-mcp-epic-routing/`
- `skills/ui-design/nextlevelbuilder-ui-ux-pro-max/`

## 观望（本轮维持 / 微调）

- fagemx 其余约 17 项（game-direction / ideation / pitch-review…）— 上轮已摘 12，本轮未动
- abagames/agentic-gamedev-skills — 仍是 MIT 12★、08-09 增量小游戏/Godot/Web
- educlopez/ui-craft — v1.0.18 之后无新动向
- MengTo/Skills threejs-scroll-world 等 — 仍偏 Web demo，与 UE 主链不重叠
- Yuki001/game-dev-skills — **仍无 LICENSE**，维持观望
- SummerEngine/summer-engine-agent — 维持
- Randroids / NAJEM / mike007jd / alfaris / Shellishack — 维持
- opengameapp/OpenGame-skills — 维持低优
- kevinpbuckley/VibeUE — 同作者 MCP 层；本仓 `vibeue-blueprints` / `vibeue-materials` 已收，等本轮 `kevinpbuckley-unreal-engine-skills` 跑通后再决定是否补 vibeue-profiling 等剩余约 32 个 SKILL.md

## 可忽略

- 种子：JackyST0/awesome-agent-skills 仍仅 star chore；mouadja02/skills 08-07~09 新增 Postgres / HTTP2 / NO_PROXY / SEO 方向无关，计数量、不展开
- 新建技能仓仍以 GitHub Skills 练习 / 作品集 / 合规 / 招聘 / WhatsApp 噪声为主
- 作弊 / 外挂 / 电竞陪玩类一律忽略

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | ~616 | 仍仅 star chore（08-10） | 无 UE / 游戏专区新增 |
| mouadja02/skills | ~9 | 08-09 合并 SEO / Postgres 等 PR | 本轮有 commit，**方向无关** |

## 今天可行动

1. UE 主链续力：`kevinpbuckley-unreal-engine-skills` 用作 UE 5.8 域知识主入口；用 LOOMLE 在复杂 BP/WP 图编辑时拿到结构保留；用 `ue-mcp-niagara` / `ue-mcp-native-cpp` / `ue-mcp-epic-routing` 覆盖 Bridge 三缺角
2. 后续若做游戏 HUD（科幻 / 像素 / 赛博朋克风）：跑 `nextlevelbuilder-ui-ux-pro-max --design-system --persist` 用强制的设计系统生成器先出 system 再写屏
3. 把 `nextlevelbuilder-ui-ux-pro-max` 与现有 `frontend-design` / `ui-design-brain` 并列做 Web UI，避免 UI 风味同质化

## 查询记录

1. 种子仓：JackyST0 / mouadja02 commits 仍无方向新增
2. WebFetch 直接拉候选原仓首页：
   - github.com/kevinpbuckley/unreal-engine-skills（8 类 61 SKILL / 216 markdown / UE 5.8 重定向）
   - github.com/loomle/loomle（931 commits / MIT / SAL 三调用）
   - github.com/db-lyon/ue-mcp（npm 携带 5 SKILL.md：workflow/blueprint 已收，本轮补 niagara/native-cpp/epic-routing）
   - github.com/nextlevelbuilder/ui-ux-pro-max-skill（115k★ MIT，含 game-relevant 风格子集）
3. WebSearch：`SKILL.md` + Unreal/UE5/UE4 cursor skill 2026、`nextlevelbuilder` ui-ux-pro-max、`db-lyon` ue-mcp、`kevinpbuckley` unreal-engine-skills、`ibrews` ue5 mcp
4. 候选去重：对照本仓 `skills/unreal/` 与 `skills/ui-design/`，确认以上 6 个均无重复
5. 入库：+6 → push `CursorSkillSearch`（待本轮 commit）
