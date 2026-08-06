# 技能侦察 DIGEST — 2026-08-06（04:00Z）

- 侦察时间：2026-08-06T04:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-06T03:00Z（同日上一轮，PR#26）
- 本仓入库：精选 **245** 个 `SKILL.md`（较上轮 +9；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-06-04`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。跟踪仓：`lisxa5747` / `Oliyflemishspeaking560` 仅 README 抖动（无新 SKILL）；`bomkino/pitchdog-design` 03:20Z 有 ChatGPT 包与文档整理但仍偏品牌/Web。按「下次优先」升级引入 **0xheycat** 等距资产生成/管线六件套（building / object / atlas / pathfinding / terrain / depth-sorting），并补齐 **donchitos** 工作室流水线：`team-audio` / `team-qa` / `team-release`。今日新建噪声约 40；方向相关新见：`QQstone/MySkills`（3D→2D 动画，无 LICENSE）、`Stanestane/game-design-skills-bundle`（40★ 游戏设计审计包，无 LICENSE）→ 观望。GitHub code search 部分可用但不稳；以 repos + skills.sh + trees/blobs 为准。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| heycat-isometric-building-sprites | 2D | 等距建筑：多格 footprint、锚点与角色遮挡验证 | https://github.com/0xheycat/isometric-game-skills | MIT；接已入库 art-direction / character | **引入** |
| heycat-isometric-object-sprites | 2D | 等距道具：单物体、统一比例、透明底可投放 | 同上 | 场景填充量产规格；固定 seed 一致性 | **引入** |
| heycat-spritesheet-atlas-packing | 2D·工作流 | 图集打包：power-of-two + JSON 帧/锚点 | 同上 | 引擎侧性能与命名帧查找的必要步骤 | **引入** |
| heycat-isometric-pathfinding | 2D·游戏设计 | 走格层 A*、禁穿角、路径平滑 | 同上 | 接 grid-math；玩法向而非纯美术 | **引入** |
| heycat-seamless-isometric-terrain | 2D·3D | 无缝等距地砖 ComfyUI/SDXL 配方与拼缝规则 | 同上 | 含 references/scripts；农场风 tile 量产 | **引入** |
| heycat-depth-sorting-occlusion | 2D | 等距深度排序：锚点 tile 决定绘制顺序 | 同上 | building/object/character 共用的遮挡真理 | **引入** |
| donchitos-team-audio | 工作流 | 音频团队编排：方向→设计→技美→玩法落地 | https://github.com/donchitos/claude-code-game-studios | 23640★ MIT；补齐 polish 前的音频管线 | **引入** |
| donchitos-team-qa | 工作流 | QA 团队：测试计划→用例→冒烟→签核 | 同上 | 与 launch-checklist / gate-check 互补 | **引入** |
| donchitos-team-release | 工作流 | 发行团队：候选版→部署→版本与 changelog | 同上 | 接 launch-checklist 的执行侧编排 | **引入** |

本仓已摘录：

- `skills/2d/heycat-isometric-building-sprites/`
- `skills/2d/heycat-isometric-object-sprites/`
- `skills/2d/heycat-spritesheet-atlas-packing/`
- `skills/2d/heycat-isometric-pathfinding/`
- `skills/2d/heycat-seamless-isometric-terrain/`（+ references/ + scripts/；演示 PNG 见原仓）
- `skills/2d/heycat-depth-sorting-occlusion/`
- `skills/workflow/donchitos-team-audio/`
- `skills/workflow/donchitos-team-qa/`
- `skills/workflow/donchitos-team-release/`

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 18:06Z idea-refine；无新 commit | https://github.com/mouadja02/skills | **忽略**（通用 coding） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| bomkino/pitchdog-design | 03:09–03:20Z：ChatGPT 包、去残留；1★ 0BSD | https://github.com/bomkino/pitchdog-design | 仍偏品牌/Web；**维持观望** |
| lisxa5747 AngelScript | 03:44Z 仅 Update README；NOASSERTION | https://github.com/lisxa5747/unreal-angelscript-skills | **观望/降级**（优先 osseous） |
| Oliyflemishspeaking560/threejs-game-skills | 03:46Z 仅 Update README；0★ MIT | https://github.com/Oliyflemishspeaking560/threejs-game-skills | 观望/低优（疑似镜像） |
| Yuki001/game-dev-skills | 50★；仍无 LICENSE | https://github.com/Yuki001/game-dev-skills | 维持观望 |
| educlopez/ui-craft / ConnorGriffin | 无新于上轮 | 各原仓 | ui-craft 维持观望 |
| Flue / eve / OpenGame / sipher / vladmdgolam | 无实质变化 | 各原仓 | 维持观望 |

### 累计建议引入（仍有效）

1–88. 维持至上轮（含 donchitos live-ops/polish/launch、omer world-building/streamer-bait、heycat godot/canvas/character）  
89. **+ 本轮** heycat：building / object / atlas / pathfinding / terrain / depth-sorting  
90. **+ 本轮** donchitos：team-audio / team-qa / team-release

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| QQstone generating-2d-animations-from-3d | 2D·3D | 从 3D 生成 2D 动画序列的流程 skill | https://github.com/QQstone/MySkills | **本轮新建**；方向贴合但 **无 LICENSE**、0★ | **观望（新增）** |
| Stanestane/game-design-skills-bundle | 游戏设计 | 核心循环/FTUE/公平性等审计与灵感包 | https://github.com/Stanestane/game-design-skills-bundle | 40★；说明清晰但 **无 LICENSE** | **观望（新增）** |
| bomkino/pitchdog-design | UI·设计 | 品牌/作品设计：proof、soul、禁 house-style | https://github.com/bomkino/pitchdog-design | 本轮有实质文档更新；非游戏向 | 观望 |
| ConnorGriffin / educlopez ui-craft | UI·工作流 | craft→critique→audit | 各原仓 | 偏产品/Web；可改造游戏 HUD | 观望 |
| sfkislev/flue blender | 3D·工作流 | 无 MCP 的 shell→bpy 桌面桥 | https://github.com/sfkislev/flue | 65★ MIT；含本机路径 | 观望 |
| Yuki001/game-dev-skills | 游戏设计·3D·工作流 | architect / toon shader / 资产生成 | https://github.com/Yuki001/game-dev-skills | 50★；**无 LICENSE** | 观望 |
| kevin / sipher / lisxa5747 / eve | 各向 | 维持上轮理由 | 各原仓 | 许可或成熟度未变 | 观望 |
| 0xheycat 其余（autotiling、camera、atlas 以外、tilemap-data、cutout、pipeline…） | 2D | 等距管线剩余件 | https://github.com/0xheycat/isometric-game-skills | 本轮已收 building/object/atlas/pathfinding/terrain/depth；按需续摘 | 观望 |
| vladmdgolam blender-mcp / cinema4d-mcp | 3D·工作流 | 经 MCP 驱动 Blender/C4D | https://github.com/vladmdgolam/agent-skills | MIT 7★；强依赖 MCP | 观望 |
| NAJEMWEHBE driving-unreal | UE·工作流 | 经 unreal-ai-connection MCP 驱编 | https://github.com/NAJEMWEHBE/unreal-ai-connection | MIT 9★；强依赖其 MCP | 观望 |
| august-batista unreal-assets | UE | 安全读写 .uasset/.umap | https://github.com/august-batista/claude-unreal-bridge-editor | MIT 0★；强依赖桥 | 观望 |
| gisenberg/unreal-skills | UE·工作流 | ue5-angelscript/build/editor/pie/perforce | https://github.com/gisenberg/unreal-skills | 有 SKILL.md 但 **无 LICENSE**、0★ | **观望（新增）** |
| opengameapp/OpenGame-skills | 游戏设计·工作流 | 浏览器原型 + Skill/MCP 发布 | https://github.com/opengameapp/OpenGame-skills | MIT-0 0★；偏 OpenGame 生态 | 观望 |
| w-zhian / avemeva / jasonxu610 | 游戏/UI | 维持或低优 | 各原仓 | 许可/更新不足 | 观望/低优 |

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 idea-refine（方向无关，记数）
- ConnorGriffin 通用 orchestrate/say-less（非游戏向）
- 今日新建噪声（方向无关，约 40）：`hmeqo/skills`、`TheShyWR/skills`、`gemdesign-ai/skills`（空仓）、`wkentaro/skills`、`guillezorrilla/skills`、`homozzy/workbuddy-skills`（票务/邮件等）、`Events-Operating-System/bailey-skills`（活动排期）、`xxxxxxuuuu/code-review`、各类 `johnisanerd/claude-skill-*` 抓取器、练习仓等
- `lisxa5747` / `Oliyflemishspeaking560`：仅 README 更新，不计实质
- eve-skills：EVE Online API
- GitHub code search 不稳定；以 repos + skills.sh + 跟踪仓 trees 为准

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 仍为 **08-05 18:06Z** idea-refine portable（无关）；此后无新 commit |

## 本仓入库变化（+9 → 245）

- 新增 `skills/2d/heycat-isometric-building-sprites/`
- 新增 `skills/2d/heycat-isometric-object-sprites/`
- 新增 `skills/2d/heycat-spritesheet-atlas-packing/`
- 新增 `skills/2d/heycat-isometric-pathfinding/`
- 新增 `skills/2d/heycat-seamless-isometric-terrain/`（含 references/、scripts/）
- 新增 `skills/2d/heycat-depth-sorting-occlusion/`
- 新增 `skills/workflow/donchitos-team-audio/`
- 新增 `skills/workflow/donchitos-team-qa/`
- 新增 `skills/workflow/donchitos-team-release/`
- 各含 `SOURCE.md`；承接上轮 236 条精选内容

## 今天可行动

1. **装**：`skills/2d/heycat-seamless-isometric-terrain`（含 references/scripts）+ 已入库 `isometric-grid-math` — 用 ComfyUI 配方先打一套无缝草地/泥土 tile。
2. **试**：`skills/2d/heycat-isometric-pathfinding` 配 `depth-sorting-occlusion`，在 Canvas/Godot 原型里验证走格与遮挡是否一致。
3. **个人化**：把 `donchitos-team-qa` + `donchitos-team-release` 收成自己的「垂直切片签核→候选版」检查表（固定冒烟清单 + 版本/changelog 两步），接到 UE 迭代。
