# 技能侦察 DIGEST — 2026-08-24（每日 cron 01:00Z）

- 侦察时间：2026-08-24T01:04Z（自动化 cron）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：远端 `CursorSkillSearch` commit `3657eb2`（317 SKILL；08-17 DIGEST）+ Memories 清单
- 本仓入库：精选 **322** 个 `SKILL.md`（相对 317：+5 新增；另同步 JetBrains UE 2 项实质更新）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

种子仓：JackyST0 新增 **Suede Creator Skills** 索引（偏营销/创作者工作流，**非游戏/UE 主向**）；mouadja02 持续加 JSON/WebAuthn/OAuth/gRPC 合规技能（**方向无关**）。本轮落实上轮遗留：补齐 **Schepetkov** UE 5.8 UI/资产管线、**fagemx game-direction**、**rundesk** 关卡与试玩；并同步 **JetBrains rider-skills** 08-21 对 UE C++/测试技能的实质修订。新发现 **teixasalone/UnrealEngine5-Skills**（UE 5.6/5.7 路由包）暂观望。

## 建议引入（本轮增量 = 5 新增）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| schepetkov-ue-ui | UE（主向） | UE 5.8 UI：CommonUI、Unified Input、手柄导航/焦点、DPI/安全区、UMG 性能与调试 | https://github.com/Schepetkov/claude-skills-game-UE/tree/main/skills/ue-ui | MIT；强调源码核对 cvar；补齐本仓 UE UI 专项空白 | **引入** |
| schepetkov-ue-assets | UE（主向）/3D | UE 5.8 资产管线：Interchange/Nanite/LOD/碰撞/UV/材质预算/HLOD | https://github.com/Schepetkov/claude-skills-game-UE/tree/main/skills/ue-assets | MIT；Nanite vs LOD 决策清晰；AI mesh 导入注意点 | **引入** |
| fagemx-game-direction | 游戏设计 | 制作人/创意总监视角：挑战 premise、scope vs 产能、市场定位、continue/pivot/shelve | https://github.com/fagemx/gstack-game/tree/main/skills/game-direction | MIT；与已入 ideation 成对；反谄媚 + 范围数学 | **引入** |
| rundesk-designing-game-levels | 游戏设计 | 引擎无关关卡/空间契约：从玩家/相机/移动指标推导几何再验证 | https://github.com/rundesk-ai/rundesk-skills-gamedev/tree/main/skills/designing-game-levels | MIT；与 designing-games 入口衔接；可单独安装 | **引入** |
| rundesk-playtesting-games | 游戏设计 | 假设驱动的玩家研究：问题框定、招募、主持、证据→改动（非自动化 QA） | https://github.com/rundesk-ai/rundesk-skills-gamedev/tree/main/skills/playtesting-games | MIT；填补「真人试玩方法论」空白 | **引入** |

本仓路径：
- `skills/unreal/schepetkov-ue-ui/`（SKILL.md + SOURCE.md）
- `skills/unreal/schepetkov-ue-assets/`（SKILL.md + SOURCE.md）
- `skills/game-design/fagemx-game-direction/`（SKILL.md + SOURCE.md）
- `skills/game-design/rundesk-designing-game-levels/`（SKILL.md + SOURCE.md）
- `skills/game-design/rundesk-playtesting-games/`（SKILL.md + SOURCE.md）

## 实质更新（已入库同步）

| 名称 | 方向标签 | 变更要点 | 仓库链接 | 建议 |
|---|---|---|---|---|
| jetbrains-ue-code-authoring | UE / 工作流 | 08-21 `AIIDEAS-31`：重写「done=shape+observed behaviour」、programmatic-use invariants、Rider `execute_tool` 模型 | https://github.com/JetBrains/rider-skills/tree/master/skills/ue-code-authoring | **已同步** |
| jetbrains-ue-test-authoring | UE / 工作流 | 同提交：测试技能与 reference 微调 | https://github.com/JetBrains/rider-skills/tree/master/skills/ue-test-authoring | **已同步** |

## 观望（本轮新增 / 维持）

- **Schepetkov `ue-mcp` / `meshy-3d-generation`** — MCP 为 Experimental 一等公民但仍变；Meshy 偏外包管线；下轮可续摘 ue-mcp。
- **teixasalone/UnrealEngine5-Skills** — MIT；16★；UE 5.6/5.7 模块路由 + Blueprint/C++/PCG/UMG 等 11 技能；08-23 仅 README；与 quodsoler/gamedev-skills 重叠，先观望对比质量。
- **rundesk 其余** — 2d-art / cameras / isometric / systemic-management / axmol 等。
- **abagames `generating-dot-assets`** — 依赖 Codex `image_gen` + ImageMagick；主机可移植性弱，维持观望。
- **educlopez/ui-craft v1.0.20** — 08-19；仍偏 Web UX coverage，维持观望。
- **MengTo** — 08-18 新增 particle trail / mouse orbit / wireframe scan；偏 Web demo。
- **NVIDIA Omniverse Realtime Viewer 0.2.0** — 本仓已有条目；上游刷新，非紧急。
- **tzwkb/lqe-translator** — 08-21 仍更新；本地化 LQE，0★，工作流边缘。
- **banyapon/MurdleSkillsGame** — 有清晰 SKILL.md（逻辑推理谜题游戏），**无 LICENSE**，观望至许可明确。
- **Yuki001/game-dev-skills** — 08-18–21 持续 recipes；仍 **无 LICENSE**。

## 可忽略

- 种子仓：JackyST0 索引 **JasonColapietro/suede-creator-skills**（营销/SEO/创作者增长为主，非游戏/UE）；mouadja02 合规/协议类（方向无关，计数量不展开）。
- 新建噪声：「skills game」字面撞车（frong-funhouse、three-second-challenge、baseball skill game 等）。
- 作弊 / 外挂 / 电竞陪玩类一律忽略。
- code search `filename:SKILL.md` 本轮多次 **HTTP 429**；改用 repos search + trees/blobs + skills.sh。

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | 624 | 08-18 合入 Suede Creator Skills + installer harden；08-19 star chart | 无 UE/游戏专区新增 |
| mouadja02/skills | 9 | 08-17→23：JSON/WebAuthn/OAuth/gRPC/Qdrant | 方向无关 |

## 今天可行动

1. **UE UI 体检**：用 `schepetkov-ue-ui` 核对项目是否该上 CommonUI、手柄焦点栈与 Unified Input；UI 卡顿时查 invalidation/retainer/bindings。
2. **资产导入门禁**：新 mesh/AI 资产生成后走 `schepetkov-ue-assets`（Nanite vs LOD、碰撞/UV、纹理预算）再进关卡。
3. **方向压力测试**：已有概念的项目跑 `fagemx-game-direction`（premise → scope 数学），再用 `rundesk-designing-game-levels` + `rundesk-playtesting-games` 把空间契约与试玩假设写死。

## 查询记录

1. 种子仓 commits/meta：JackyST0、mouadja02
2. 跟踪仓 pushed_at：Schepetkov、rundesk、fagemx、abagames、gamedev-skills、quodsoler、arg-games、simready、NVIDIA/skills、Yuki、MengTo、ui-craft、Randroids、JetBrains、heycat、Donchitos、omer、tzwkb
3. repos search：`skills game` created:>=2026-08-17；`unreal skills` updated:>=2026-08-17；`agent skills game`；`game design skills agent`
4. code search：Unreal / game design / path:.cursor/skills + filename:SKILL.md → **429**
5. skills.sh：unreal、game design、ue5 → 发现 teixasalone/chacelow 等线索
6. 候选深挖：Schepetkov 余项、fagemx game-direction、rundesk levels/playtesting、JetBrains AIIDEAS-31、teixasalone、MurdleSkillsGame、suede
7. 入库 +5 + JetBrains 同步 → push `CursorSkillSearch` → 复用 PR #31 → Slack + Gmail

## 遗留问题 / 趋势记录

- 近一周公开游戏/UE Agent Skills 仍稀疏；高质量增量主要来自既有仓续摘（Schepetkov/rundesk/fagemx）与 Rider UE 技能打磨。
- 下轮优先：Schepetkov `ue-mcp`；teixasalone 质量对比；rundesk 2d-art/cameras；abagames dot-assets（若可移植）；Yuki LICENSE；Murdle LICENSE。
- PR #31 复用，勿新建 skill-digest-* 分支。
