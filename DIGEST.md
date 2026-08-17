# 技能侦察 DIGEST — 2026-08-17（每日 cron 01:00Z）

- 侦察时间：2026-08-17T01:04Z（自动化 cron）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：远端 `CursorSkillSearch` commit `65a7670`（312 SKILL；08-15 DIGEST）
- 本仓入库：精选 **317** 个 `SKILL.md`（相对 312：+5 新增）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

种子仓仍无方向相关新增（JackyST0 仅 star chore；mouadja02 08-15/16 为 multipart/Qdrant/产品管理，**方向无关**）。本轮最大发现是 **Schepetkov/claude-skills-game-UE**（2026-08-14 新建，MIT，UE 5.8.1 源码核对）：照明 / 性能 / 网络三件套质量显著高于多数公开 UE skill。同时补齐遗留的 **fagemx game-ideation**，并引入新仓 **rundesk-skills-gamedev** 的设计入口技能。

## 建议引入（本轮增量 = 5 新增）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| schepetkov-ue-lighting | UE（主向） | UE 5.8 照明/渲染决策树：Lumen Lite、MegaLights、VSM、Substrate；强制先 grep 引擎源码再引用 cvar | https://github.com/Schepetkov/claude-skills-game-UE/tree/main/skills/ue-lighting | MIT；对照 5.8.1 源码纠正文档漂移（如 `r.MegaLights.Allowed`）；填补本仓 UE 照明专项空白 | **引入** |
| schepetkov-ue-performance | UE（主向） | UE 5.8 性能方法论：stat unit → Insights → 分线程瓶颈 → PSO/hitch/GC/流送 | https://github.com/Schepetkov/claude-skills-game-UE/tree/main/skills/ue-performance | MIT；强调「测量→隔离→修复→复测」；含 5.8 Snapshot Hitches / Spatial Profiler | **引入** |
| schepetkov-ue-networking | UE（主向） | UE 5.8 多人：Generic+Iris 复制、Push Model、RPC、relevancy、带宽与 NetTrace | https://github.com/Schepetkov/claude-skills-game-UE/tree/main/skills/ue-networking | MIT；纠正博客里错误的 Iris `bUseIris` 启用方式；Iris 已 production-ready | **引入** |
| rundesk-designing-games | 游戏设计 | 体验契约 → MDA → 嵌套玩家循环 → 可验证设计假设的引擎无关工作流 | https://github.com/rundesk-ai/rundesk-skills-gamedev/tree/main/skills/designing-games | MIT；08-12 新仓；说明清晰、可单独安装；与 fagemx/abagames 形成互补入口 | **引入** |
| fagemx-game-ideation | 游戏设计 | Fantasy/Loop/Twist 头脑风暴 + Iceberg 验证规划（上一轮遗留计划） | https://github.com/fagemx/gstack-game/tree/main/skills/game-ideation | MIT；已摘 12 条 review 向，本轮补「从零概念」入口；本仓为去 preamble 精选摘录 | **引入** |

本仓路径：
- `skills/unreal/schepetkov-ue-lighting/`（SKILL.md + SOURCE.md）
- `skills/unreal/schepetkov-ue-performance/`（SKILL.md + SOURCE.md）
- `skills/unreal/schepetkov-ue-networking/`（SKILL.md + SOURCE.md）
- `skills/game-design/rundesk-designing-games/`（SKILL.md + SOURCE.md）
- `skills/game-design/fagemx-game-ideation/`（SKILL.md + SOURCE.md）

## 观望（本轮新增 / 维持）

- **Schepetkov 其余 skills** — `ue-ui`（CommonUI+5.8 Unified Input）、`ue-assets`（Nanite/Interchange）、`ue-mcp`（引擎内置 MCP）、`meshy-3d-generation`；本轮先入三件核心，下轮可续摘 ui/assets/mcp。
- **rundesk-skills-gamedev 其余 ~16** — levels / playtesting / 2d-art / cameras / axmol / systemic-management 等；入口已入，其余分批。
- **fagemx game-direction** — 创意总监视角挑战 premise/scope/市场；与 ideation 成对，下轮优先。
- **abagames/agentic-gamedev-skills** — 08-16 实质更新（dispatch 路由、headless Godot 校验、dot-assets/mutants/coverage 巩固）；已入库项有修订，新见 `generating-dot-assets` / `auditing-gameplay-implementation-coverage` / `dispatching-agent-work` 暂观望。
- **educlopez/ui-craft** — 08-13 v1.0.19；仍偏 Web fold/geometry，维持观望。
- **MengTo threejs-landscape / weather / towers** — 08-11 新增；偏 Web demo，维持观望。
- **Randroids-Dojo/skills (unreal)** — 08-13 更新的是 clean-slop，非 Unreal 插件实质进展；维持。
- **tzwkb/lqe-translator** — MIT；游戏本地化 LQE 流水线（ZH→EN/TH），0★，工作流边缘，观望。
- **NVIDIA/simready-foundation 其余** / **physical-ai** / **Yuki001（无 LICENSE）** — 维持。

## 可忽略

- 种子仓：JackyST0 star chore；mouadja02 multipart wire / Qdrant / product-management（方向无关，计数量不展开）。
- NVIDIA/skills 08-14 `feat: add Jetson video SDK skills` — 嵌入式视频，非游戏/UE 主向。
- 新建噪声：`davidapoe/set-it-and-forget-it`、`R1-DBT-Skills-Game`、`skillsharejr-game`、`AreUHuman` 等「skills game」字面撞车，非 Agent Skills。
- 作弊 / 外挂 / 电竞陪玩类一律忽略。
- code search `Unreal filename:SKILL.md` / `"game design" filename:SKILL.md` 本轮 **HTTP 429**，改用 repos search + trees/blobs + skills.sh。

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | 621 | 仍仅 star chore（08-10） | 无 UE / 游戏专区新增 |
| mouadja02/skills | 9 | 08-15/16 multipart / Qdrant / product-management | 方向无关 |

## 今天可行动

1. **UE 5.8 性能/照明体检**：在目标工程用 `schepetkov-ue-performance` 跑 `stat unit` + Insights 定瓶颈线程；若 GPU 高，切到 `schepetkov-ue-lighting` 核对 Lumen Lite / MegaLights / DeviceProfiles，并 grep 引擎源码确认 cvar。
2. **多人路径核对**：若项目已开或计划 Iris，用 `schepetkov-ue-networking` 对照真实启用方式（`net.Iris.UseIrisReplication` + `FIrisNetDriverConfig`），避免错误的 `bUseIris` Target.cs 写法。
3. **概念 → 体验契约**：新项目先跑 `fagemx-game-ideation` 产出 Fantasy/Loop/Twist + Iceberg 验证计划，再用 `rundesk-designing-games` 写成可测试的体验契约与嵌套循环。

## 查询记录

1. 种子仓 commits / meta：JackyST0、mouadja02
2. 跟踪仓 pushed_at：NVIDIA/skills、simready-foundation、fagemx、gamedev-skills、Yuki、abagames、MengTo、ui-craft、Randroids、NAJEM、mike007jd、JetBrains、quodsoler、arg-games、heycat、Donchitos、omer、Sttrevens、John-Sun27
3. repos search：`skills game` created:>=2026-08-10；`unreal skills`；`agent skills game`
4. code search：Unreal / game design + filename:SKILL.md → **429**
5. skills.sh/api/search：unreal、game design
6. 候选 WebFetch/API：Schepetkov/claude-skills-game-UE、rundesk-ai/rundesk-skills-gamedev、tzwkb/lqe-translator、abagames Aug-16 commits、fagemx ideation/direction
7. 入库 +5 → push `CursorSkillSearch` → 复用 PR #31 → Slack + Gmail

## 遗留问题 / 趋势记录

- 近 7 天公开游戏/UE Agent Skills 仍稀疏，但出现高质量独立小仓（Schepetkov UE 5.8、rundesk gamedev）。
- 下轮优先：Schepetkov `ue-ui` / `ue-mcp` / `ue-assets`；fagemx `game-direction`；rundesk levels/playtesting；abagames dot-assets 或 coverage；simready materials conform。
- push 继续使用 `git -c credential.helper= -c credential.helper=manager push origin CursorSkillSearch`（或当前 remote token）。
- PR #31 复用，勿新建 skill-digest-* 分支。
