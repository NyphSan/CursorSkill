# 技能侦察 DIGEST — 2026-08-14（每日 cron 09:55+08:00）

- 侦察时间：2026-08-14T09:55+08:00（自动化 cron）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：远端 `CursorSkillSearch` commit `56db0c8`（307 SKILL；08-13 已 push）
- 本仓入库：精选 **310** 个 `SKILL.md`（相对 307：+3 新增）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

种子仓无方向相关新增（JackyST0 仍仅 star chore / mouadja02 09:30 commit 仍仅 docs：seeds-fix-create-skill）。本轮抓到 **3 条方向相关近 7 天首次定位到 SKILL.md 的高质量条目**：

1. **`NVIDIA/skills/omniverse-cad-to-simready`** — NVIDIA 官方，Apache-2.0 + CC BY 4.0 双许可，v0.2.0，本仓 `skills/3d/` 首个 SimReady / USD 物理仿真就绪条目；UE 5.2+ 原生支持 USD 导入，SimReady USD 跳过手工 `UPhysicalMaterial` / 碰撞体配置
2. **`NVIDIA/skills/omniverse-usd-performance-tuning`** — 同上，v0.1.0，core + 「ready_to_plan / approval_required / blocked」状态机；本仓补齐 NVIDIA 端的「优化已有 USD」链路，与上一条互为「产出 / 优化」两半
3. **`thrixel/goal-to-game`** — MIT，2026-08-12 最新 commit（统一为 Claude Code plugin），涵盖 Thrixel 三路径决策树（Architect / Sculptor / Architect→Detailer）、强制 `thrixel_group_parts` 后处理、Cube 预算驱动的资产列表规划；与 `mint-threejs-skills` / `gamedev-create-game-assets` 形成 3D 资产生成的主链第三象限

## 建议引入（本轮增量 = 3 新增）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| nvidia-omniverse-cad-to-simready | 3D（主向）/ 研发工作流 | NVIDIA 官方 CAD → SimReady USD 端到端编排：preflight + Content Agents（material/physics/texture）+ `simready-conform-profile` + Omni Asset Validate + OVRTX 渲染 + 可选打包；状态机 `passed / blocked / failed / needs_rerun` | https://github.com/NVIDIA/skills/tree/main/skills/omniverse-cad-to-simready | Apache-2.0 + CC BY 4.0 双许可；v0.2.0；8 条硬规则齐（preflight / Content Agents gate / 阶段引用 / FET 路由 / GSP.001 → FET005）；原仓 08-14 仍有 commit；UE 5.2+ `Datasmith USD` / `Interchange USD` 可直接吃 SimReady 产出 | **引入**（已摘录 14 步工作流 + 8 条硬规则 + 与 UE 集成映射） |
| nvidia-omniverse-usd-performance-tuning | 3D（主向）/ 性能调优 | NVIDIA 官方 USD 性能诊断与优化编排：`profile-stage:baseline / after` → `usd-structure-assessment` → 验证链 → `usd-optimize-run-operations` → `optimization-report`；明示 `blocked_missing_usd_optimize` 等错误码 | https://github.com/NVIDIA/skills/tree/main/skills/omniverse-usd-performance-tuning | Apache-2.0 + CC BY 4.0；v0.1.0；显式状态机 `ready_to_plan / approval_required / blocked`；与 Unreal Insights 的 Frame Delta 思维同构，便于 UE 团队理解 | **引入**（已摘录 canonical plan contract + routing map + 与 UE Insights 类比） |
| thrixel-goal-to-game | 游戏设计 / 3D 原型 | Thrixel + Unity/three.js + Claude Code plugin：3 路径决策树（何时用 A / S / A→D）+ 强制 `group_parts`（每对象一 draw call 死亡陷阱的解药）+ `edit_model` + 增量编辑（`focus_on_node_names` 保留未指定节点 bit-identical）+ Cube 预算驱动的资产列表规划 | https://github.com/thrixel/goal-to-game | MIT（源头） + Apache-2.0（CC0 不可绕开）；5 commits，08-12 重构为 Claude Code 插件；上游 SKILL.md 持强烈工作流意见（NEVER image / Always `plus` quality / Free-plan 必须问升级 / Cube 用尽也要展示当前可玩版本） | **引入**（已摘录三路径决策树 + asset-list FIRST + group_parts 必选 + out-of-cubes 流程 + 强烈观点清单） |

本仓路径：
- `skills/3d/nvidia-omniverse-cad-to-simready/`（SKILL.md + SOURCE.md）
- `skills/3d/nvidia-omniverse-usd-performance-tuning/`（SKILL.md + SOURCE.md）
- `skills/game-design/thrixel-goal-to-game/`（SKILL.md + SOURCE.md）

## 观望（本轮维持 / 微调）

- fagemx 其余约 17 项 — 上轮已摘 12，本轮未动
- abagames/agentic-gamedev-skills — 08-13 之后无新 commit，与 haxqer-godot-skill / awesome-gamedev-agent-skills 部分重叠但体量小
- educlopez/ui-craft — v1.0.18 之后无新动向
- MengTo/Skills threejs-scroll-world 等 — 仍偏 Web demo，与 UE 主链不重叠
- Yuki001/game-dev-skills — **仍无 LICENSE**，维持观望
- SummerEngine/summer-engine-agent — 维持
- Randroids / NAJEM / mike007jd / alfaris / Shellishack — 维持
- opengameapp/OpenGame-skills — 维持低优
- kevinpbuckley/VibeUE — 同作者 MCP 层；等 kevinpbuckley-unreal-engine-skills 跑通后再决定是否补剩余约 32 个 SKILL.md
- affaan-m/everything-claude-code/blender-motion-state-inspection — Blender 角色/绑定/动画检查，范围窄，本轮观望
- dcc-mcp-skills-creator — DCC-MCP 技能包创建工具，基建向，本轮观望
- **addyyosmani/agent-skills** — 76k★；24 SKILL 中 `frontend-ui-engineering` 与 UI 设计主向相关，但与 nextlevelbuilder/taste-skill 重叠定位；不直接入库
- **MCPBlender/blender-mcp** — 25.6k★；MCP server 而非 SKILL package；与 dcc-mcp-blender 互补，但范畴不在本任务
- **EpicLolia/UnrealPythonMCP** — 08-09 发布；TypeScript UE Python MCP；MCP server，非 SKILL
- **virgiliojr94/book-to-skill** — 7,750★；将 PDF 转 SKILL.md；基建向，与游戏/UE/3D/UI 主向弱相关，本轮观望
- **Matt Pocock skills（TypeScript 巫师）** — 30.8k★，个人 .claude 公开，方向是反氛围编程 + TDD/PRD；与游戏主向不重叠
- **reverse-skill** — 19.6k★ / 2.7k forks；安全逆向向；与方向无关
- **gamedev-skills/awesome-gamedev-agent-skills** — Apache-2.0；08-11 之后 docs 仅 maintainer attribution；本仓已有 6/6 UE 技能 + 14/15 disciplines + 9/9 genres + 3/4 workflows 已摘录；剩余 15 Godot / 8 Unity / 6 Web / 5 Other-Engine 技能仍未单独入库；本轮未动，因 08-08 的 `feat: modernize game development skills and asset pipeline` 是大版本但前端路由已覆盖
- **NVIDIA Skills 总目录（NVIDIA/skills）** — 560+ 提交 / 34 分支；除本轮引入 2 条外，还有 8+ 条可能方向相关（`omniverse-realtime-viewer` / `cuopt-routing-api-python` / `tilegym-*` GPU 编程 / `physical-ai-neural-reconstruction` 等），本轮因「NVIDIA 配额 + 三日内只摘稳定上游」策略仅选最高两条；剩余计划在 08-15 ~ 08-17 之间分批摘取

## 可忽略

- 种子：JackyST0/awesome-agent-skills 仍仅 star chore；mouadja02/skills 09:30 docs：seeds-fix-create-skill，方向无关
- 新建技能仓仍以 GitHub Skills 练习 / 作品集 / 合规 / 招聘 / WhatsApp 噪声为主
- 作弊 / 外挂 / 电竞陪玩类一律忽略
- ai-design-layers/agent-skills — sleek-design-mobile-apps（501★）TypeScript / REST API 与 nextlevelbuilder-ui-ux-pro-max / leonxlnx-taste-skill 重叠定位，不入库

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | ~616+ | 仍仅 star chore（08-10） | 无 UE / 游戏专区新增 |
| mouadja02/skills | ~9 | 08-14 09:30 docs：seeds-fix-create-skill | **方向无关**（种子仓仅补 templates） |

## 今天可行动

1. **如在做 UE 项目且需要 CAD / mesh 上游就绪**：clone `NVIDIA/skills` 后跑 `omniverse-cad-to-simready`；产出的 SimReady USD 直接 `Datasmith USD` / `Interchange USD` 导入 UE 5.2+，跳过手工 `UPhysicalMaterial` + 碰撞体配置；需 Python 3.12 + Docker + GPU + 任一 `*API_KEY`（推荐 `NVIDIA_API_KEY`）
2. **如在做大型 USD 场景（ArchViz / 数字孪生 / 工厂仿真 / 沙盒大场景）**：clone `NVIDIA/skills` 后跑 `omniverse-usd-performance-tuning`；`profile-stage:baseline → profile-stage:after → compare-profiles` 的三段式节奏 ≈ Unreal Insights 的 Frame Delta 思维，对 UE 团队友好；三个 scoped iterations 可独立审阅
3. **如在做 Unity 或 three.js 原型**：安装 `claude plugin install thrixel@thrixel`（自动携带 skill + Thrixel MCP）；为项目做"asset list FIRST"规划，按 `plus` quality + 三路径决策生成；每对象必跑 `thrixel_group_parts`，否则 draw call 爆炸无法交付

## 查询记录

1. 种子仓：JackyST0（仍 star chore）/ mouadja02（08-14 09:30 docs）— 方向无关
2. WebSearch 查询（d7 窗口）：
   - `site:github.com "SKILL.md" Unreal Engine UE5 game design agent skill 2026 August`
   - `site:github.com ".cursor/skills" OR ".agents/skills" SKILL.md 3D 2D UI game design workflow August 2026`
   - `site:github.com SKILL.md agent skills "3D" "Blender" OR "Maya" OR "Houdini" August 2026`
   - `site:github.com SKILL.md "dcc-mcp" OR "game-dev" OR "unreal-engine" plugin skill 2026`
   - `GitHub "SKILL.md" Unreal "behavior tree" OR "Enhanced Input" OR "Gameplay Tags" OR "Replication Graph" release 2026`
   - `GitHub "SKILL.md" game design "GDD" OR "design document" OR "gameplay pillar" 2026`
   - `GitHub "SKILL.md" "Three.js" OR "Babylon.js" OR "R3F" 3D web design agent skill`
   - `github NVIDIA "skills" SKILL.md Omniverse USD cuOpt CUDA physics AI release 2026`
3. WebFetch 候选原仓：
   - github.com/JackyST0/awesome-agent-skills（种子）
   - github.com/mouadja02/skills（种子）
   - github.com/gamedev-skills/awesome-gamedev-agent-skills（确认 08-11 之后无实质更新；本仓已基本覆盖）
   - github.com/NVIDIA/skills（核心；08-14 仍有 6 个 commit；元数据索引刷新 + 孤儿清理 + 移除 nemo-platform）
   - raw.githubusercontent.com/NVIDIA/skills/main/skills/omniverse-cad-to-simready/SKILL.md（v0.2.0 全文）
   - raw.githubusercontent.com/NVIDIA/skills/main/skills/omniverse-usd-performance-tuning/SKILL.md（v0.1.0 全文）
   - github.com/thrixel/goal-to-game（5 commit；08-12 latest；MIT）
   - raw.githubusercontent.com/thrixel/goal-to-game/main/skills/goal-to-game/SKILL.md（全文）
   - github.com/NVIDIA-Omniverse/PhysX（claudskills 索引中的 tensor-bindings-gpu 引用；BSD-3-Clause；不在主向，未深挖）
4. 候选去重：对照本仓 `skills/3d/` / `skills/unreal/` / `skills/game-design/`，确认 3 条新条目均无重复
5. 入库：+3 → commit 计划 `CursorSkillSearch` → push 用 `git -c credential.helper= -c credential.helper=manager push origin CursorSkillSearch`（沿用 08-12 修复方案，selector 不再挂起）

## 遗留问题 / 趋势记录

- 08-13 commit `56db0c8` 已成功 push（push 修复稳定运行 1 个 cron 周期）
- 本轮 commit 将叠加在 `56db0c8` 之上，push 继续使用 `git -c credential.helper= -c credential.helper=manager push origin CursorSkillSearch`
- gh CLI（2.97.0）可用：可继续用 `gh pr list --head CursorSkillSearch` 复用 PR #31
- NVIDIA Skills 总目录未来 3 个 cron 可能继续摘取（`omniverse-realtime-viewer` / `cuopt-routing-api-python` / `physical-ai-neural-reconstruction` 等），平均每日 1-2 条，避免单次 commit 超 500 行变更
- thrixel-goal-to-game 上游 SKILL.md 持有强烈工作流意见，提示下游引用：本条目一旦引入，建议在 SKILL.md 加入「不可与其他 build-me-a-game 类技能混合使用」的强声明，避免冲突
