# 技能侦察 DIGEST — 2026-08-31（每周 cron 01:00Z）

- 侦察时间：2026-08-31T01:02Z（自动化 cron）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：远端 `CursorSkillSearch` commit `aa2d707`（322 SKILL；08-24 DIGEST）+ Memories 清单
- 本仓入库：精选 **335** 个 `SKILL.md`（相对 322：+13 新增）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

本轮最大增量是 **Wilson520403/game-design-skills**（MIT，4★，08-26~30 密集升级）：把《游戏设计梦工厂》《透镜之书》、任天堂哲学与关卡设计工业化方法做成可安装 Agent 套件 + orchestrator。同步兑现上轮观望：**rundesk** 相机/2D 艺术、**gamedev-skills** 新作 BT+Utility AI 实现层。UE 侧新发现 **snooy-dev/unreal-coding**（Live Coding/Hot Reload/UBT 验证路径）与 **unrealxu/unrealengine5-skills**（502★，UE5.6–5.8 路由包入口）。3D/UI 侧引入 **bbroeking** Blender MCP 风格化资产链路与 **MengTo no-ai-design-slop**。种子仓：JackyST0 仅 star 计数；mouadja02 持续合规类（方向无关）。**teixasalone** README 疑似污染/SEO，改以 unrealxu 为准。

## 建议引入（本轮增量 = 13 新增）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| wilson-art-of-game-design | 游戏设计 | Schell《透镜之书》：四元组、113+ 透镜、12 维平衡与间接控制 | https://github.com/Wilson520403/game-design-skills/tree/main/art-of-game-design | MIT；中文友好；方法论工程化完整 | **引入** |
| wilson-game-design-workshop | 游戏设计 | Fullerton《梦工厂》：Playcentric、形式/戏剧元素、原型与试玩协议 | https://github.com/Wilson520403/game-design-skills/tree/main/game-design-workshop | MIT；与已入 playtesting 互补的经典流程 | **引入** |
| wilson-nintendo-game-design | 游戏设计 | 任天堂哲学：玩具感、复合解题、起承转合、三角法则、隐性教学 | https://github.com/Wilson520403/game-design-skills/tree/main/nintendo-game-design | MIT；Game Feel / 隐性引导可直接压测玩法 | **引入** |
| wilson-level-design-craft | 游戏设计 | 关卡工业化：RLD 度量、宽线性遭遇、瑞士奶酪拓扑、隐性光影引导 | https://github.com/Wilson520403/game-design-skills/tree/main/level-design-craft | MIT；补强已入 rundesk levels 的「大师课」层 | **引入** |
| wilson-game-design-orchestrator | 游戏设计 | 总指挥：调度四引擎 + Python 量化工具箱，输出 Keep/Cut/Tune | https://github.com/Wilson520403/game-design-skills/tree/main/game-design-orchestrator | MIT；多 Agent 流水线入口；08-30 硬化契约 | **引入** |
| gamedev-ai-behavior-trees-utility-ai | 游戏设计 | 引擎无关 BT runtime + Utility AI（曲线/consideration）+ 混合 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/main/skills/disciplines/ai-behavior-trees-utility-ai | Apache-2.0；08-24 新合入；补 `game-ai` 实现空白 | **引入** |
| snooy-unreal-coding | UE / 工作流 | Windows 下按 Editor 状态选择 Live Coding / Hot Reload / 关编辑器 UBT | https://github.com/snooy-dev/unreal-skills/tree/main/skills/unreal-coding | MIT；填补「改 C++ 后怎么验」操作契约 | **引入** |
| unrealxu-ue5-module-router | UE（主向） | UE5.6–5.8 模块名/意图 → 精确技能路由（含 MCP 工具建议） | https://github.com/unrealxu/unrealengine5-skills/tree/main/skills/ue5-module-router | MIT；502★；08-26 升至 5.8；作该包入口 | **引入** |
| rundesk-designing-game-cameras-and-controls | 游戏设计 | 相机与操控一体：从任务信息需求推导视角/键位/舒适度契约 | https://github.com/rundesk-ai/rundesk-skills-gamedev/tree/main/skills/designing-game-cameras-and-controls | MIT；上轮观望兑现 | **引入** |
| rundesk-creating-2d-game-art | 2D | 2D 资产生产：运行时 brief、可读性、pivot/足迹、图集与进引擎验收 | https://github.com/rundesk-ai/rundesk-skills-gamedev/tree/main/skills/creating-2d-game-art | MIT；上轮观望兑现 | **引入** |
| bbroeking-blender-stylized-game-assets | 3D | Blender MCP 脚本化低模风格化资产 → GLB（three.js 向） | https://github.com/bbroeking/broeking-skills/tree/main/skills/blender-stylized-game-assets | MIT；可复现 Python 资产管线 | **引入** |
| bbroeking-concept-to-blender-plan | 3D | 概念图 → 结构化 Blender 构建计划（比例/调色板/部件/动画契约） | https://github.com/bbroeking/broeking-skills/tree/main/skills/concept-to-blender-plan | MIT；先计划后建模，减少返工 | **引入** |
| mengto-no-ai-design-slop | UI 设计 | 被动质量门：识别并清除泛 AI 默认视觉与无意义装饰 | https://github.com/MengTo/Skills/tree/main/agent-skills/ui/no-ai-design-slop | MIT；08-28 新增；适合 UI/落地页审阅 | **引入** |

本仓路径：
- `skills/game-design/wilson-*`（5）
- `skills/game-design/gamedev-ai-behavior-trees-utility-ai/`
- `skills/game-design/rundesk-designing-game-cameras-and-controls/`
- `skills/unreal/snooy-unreal-coding/`（含 references）
- `skills/unreal/unrealxu-ue5-module-router/`
- `skills/2d/rundesk-creating-2d-game-art/`
- `skills/3d/bbroeking-blender-stylized-game-assets/`
- `skills/3d/bbroeking-concept-to-blender-plan/`
- `skills/ui-design/mengto-no-ai-design-slop/`（含 ARTICLE.md）

## 观望（本轮新增 / 维持）

- **unrealxu 其余 10 技能**（architecture / cpp / umg / pcg / packaging…）— 与 quodsoler / gamedev-skills 重叠，先用 module-router 试用再择优摘录。
- **Schepetkov `ue-mcp` / `meshy-3d-generation`** — 仍无新推送；MCP Experimental。
- **bbroeking** 其余：`art-style-blender-research`（硬编码本机路径）、`build-stylized-rpg`、`character-creator-design`。
- **MengTo `audit-ai-design-slop`** — 正式审计变体；先用 no-ai-design-slop 被动门。
- **rainerpj/game-design-documentation** — 清晰 GDD 脚手架 skill，**无 LICENSE**。
- **rundesk 其余** — isometric / systemic-management / axmol / animation 等。
- **Yuki001/game-dev-skills**、**banyapon/MurdleSkillsGame** — 仍无 LICENSE。
- **educlopez/ui-craft** — 08-30 仍更新，偏 Web UX。
- **abagames generating-dot-assets** — Codex `image_gen` 绑定。

## 可忽略

- **teixasalone/UnrealEngine5-Skills** — 与 unrealxu 技能同构，但 README 下载指引疑似污染/SEO；改跟 **unrealxu**。
- 种子仓：JackyST0 仅 star chart；mouadja02 HTTP/OpenAPI/IPv6 合规类（方向无关，计数量不展开）。
- 噪声仓：`ekuutan/firefly-meadow`（mouse skills game）、`jvinu08/Breakout`（课程作业字面撞车）。
- code search `filename:SKILL.md` 仍易 **HTTP 429**；本轮靠 repos search + trees/blobs + skills.sh。

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | 629 | 08-24 仅 star counts | 无游戏/UE 专区新增 |
| mouadja02/skills | 9 | 08-25→30：合规/目录 UX | 方向无关 |

## 今天可行动

1. **设计方法论压测**：用 `wilson-game-design-orchestrator` 对当前项目跑一轮 Keep/Cut/Tune；卡点时切 `wilson-nintendo-game-design`（玩具感/复合解题）或 `wilson-art-of-game-design`（透镜诊断）。
2. **UE 迭代契约**：改 C++ 后强制走 `snooy-unreal-coding`（Live Coding vs Hot Reload vs 关编辑器）；跨模块问题先问 `unrealxu-ue5-module-router`。
3. **资产与 UI 门禁**：2D 新图走 `rundesk-creating-2d-game-art`；Blender 风格化资产先 `bbroeking-concept-to-blender-plan` 再建模；落地 UI 打开 `mengto-no-ai-design-slop`。

## 查询记录

1. 种子仓 commits/meta：JackyST0、mouadja02
2. 跟踪仓 pushed_at：Schepetkov、rundesk、teixasalone、unrealxu、gamedev-skills、MengTo、ui-craft、Yuki、JetBrains、fagemx、abagames、Donchitos、omer、heycat
3. repos search：`skills game` created:>=2026-08-24；`unreal skills` updated:>=2026-08-24；`game design skills`；`agent skills game`
4. code search：Unreal / game design + filename:SKILL.md → **429**
5. skills.sh：unreal、game design、ue5 → 发现 unrealxu、既有索引
6. 候选深挖：Wilson 五件套、gamedev BT+Utility、snooy、unrealxu vs teixasalone、bbroeking Blender、MengTo slop、rundesk cameras/2d、rainerpj GDD
7. 入库 +13 → push `CursorSkillSearch` → 复用 PR #31 → Slack + Gmail
