# 技能侦察 DIGEST — 2026-08-05（16:00Z）

- 侦察时间：2026-08-05T16:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T15:00Z（同日上一轮，PR#15）
- 本仓入库：精选 **156** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-05-16`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill（JackyST0 停在 08-03；mouadja02 仍为 10:11Z SBOM）。跟踪仓：hao-skills 13:11Z 删除 oil-visual、仅留个人品牌 `hao-visual`（忽略）；kevinpbuckley/sipherxyz 许可仍缺。按「下次优先」**补齐 gamedev 剩余 4 个类型包**，并自 [omer-metin/skills-for-antigravity](https://github.com/omer-metin/skills-for-antigravity)（123★ Apache-2.0）**精选引入** game-design-core / game-ui-design / vfx-realtime / 3d-modeling。新确认 [JetBrains/rider-skills](https://github.com/JetBrains/rider-skills) UE 三件套（需 Rider MCP）入观望。code search 仍 429。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| gamedev-genre-card-game | 游戏设计 | 卡牌分区/抽洗/回合/费用与效果结算 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~769 安装；补齐类型包最后一批 | **引入** |
| gamedev-genre-puzzle | 游戏设计 | 棋盘状态、规则结算、连锁、撤销与可解性 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~780 安装；含 match-3/sokoban 模式 | **引入** |
| gamedev-genre-tower-defense | 游戏设计 | 路径/波次/塔瞄准/经济与漏怪生命 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~765 安装；含平衡参考 | **引入** |
| gamedev-genre-visual-novel | 游戏设计 | 分支脚本、立绘背景、选项与存档/ backlog/skip | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~780 安装；接已有 dialogue-systems | **引入** |
| omer-game-design-core | 游戏设计 | 核心循环、动机、手感、MDA 等设计理论基础 | https://github.com/omer-metin/skills-for-antigravity | 123★ Apache-2.0；含 patterns/sharp_edges/validations | **引入** |
| omer-game-ui-design | UI 设计 | HUD/菜单/手柄导航/diegetic UI 可读性 | https://github.com/omer-metin/skills-for-antigravity | ~2445 安装；与已有 game-ui-* 工作流互补（设计原则层） | **引入** |
| omer-vfx-realtime | 3D·UE | 实时粒子/Niagara·VFX Graph 可读性与 overdraw | https://github.com/omer-metin/skills-for-antigravity | 跨引擎 VFX 原则；接已有 unreal-niagara | **引入** |
| omer-3d-modeling | 3D | 拓扑/UV/LOD/烘焙与 DCC→引擎导出管线 | https://github.com/omer-metin/skills-for-antigravity | ~886 安装；补 Blender 之外的建模生产层 | **引入** |

本仓已摘录：

- `skills/game-design/gamedev-genre-card-game/`（+ references）
- `skills/game-design/gamedev-genre-puzzle/`（+ references）
- `skills/game-design/gamedev-genre-tower-defense/`（+ references）
- `skills/game-design/gamedev-genre-visual-novel/`（+ references）
- `skills/game-design/omer-game-design-core/`（+ references）
- `skills/ui-design/omer-game-ui-design/`（+ references）
- `skills/3d/omer-vfx-realtime/`（+ references）
- `skills/3d/omer-3d-modeling/`（+ references）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 10:11Z SBOM；无更新 | https://github.com/mouadja02/skills | **忽略**（DevOps） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| a596116/hao-skills | 13:11Z 删 oil-visual；仅留 `hao-visual` 个人品牌视觉 | https://github.com/a596116/hao-skills | **忽略**（非游戏/UE） |
| kevinpbuckley | 仍无 SPDX | https://github.com/kevinpbuckley/unreal-engine-skills | 维持观望 |
| sipherxyz | 仍无 LICENSE | https://github.com/sipherxyz/universal-ue-skills | 维持观望 |
| a5c-ai/babysitter | 无新实质 UE 深化 | https://github.com/a5c-ai/babysitter | 维持观望 |
| CesiumGS / Flue | 无新实质变化 | 各原仓 | 维持观望 |

### 累计建议引入（仍有效）

1–58. 维持至上轮（含 quodsoler 核心、gamedev disciplines / jam·发行 / 主流五类 genres 等）  
59. **+ 本轮** gamedev 剩余 genres：card-game / puzzle / tower-defense / visual-novel  
60. **+ 本轮** omer-metin 精选：game-design-core / game-ui-design / vfx-realtime / 3d-modeling  

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| JetBrains/rider-skills（ue-code-authoring / ue-live-debugging / ue-test-authoring） | UE·工作流 | Rider MCP 驱动的 UE C++ 编写/调试/自动化测试 | https://github.com/JetBrains/rider-skills | 11★ Apache-2.0；质量高但强依赖 Rider MCP | 观望 |
| omer-metin 其余（card-game-design / board-game-design / character-design / ai-game-art…） | 游戏设计·2D | 大型库剩余子集 | https://github.com/omer-metin/skills-for-antigravity | 本轮已抽核心四条；其余按题材再取 | 观望 |
| quodsoler 重叠项（ue-input-system / ue-ui-umg-slate / ue-procedural-generation / ue-gameplay-abilities） | UE | 与已有 Enhanced Input / UMG / Procgen / GAS 重叠 | https://github.com/quodsoler/unreal-engine-skills | 核心缺口已收完 | 观望 |
| a5c-ai/babysitter unreal-chaos / lumen / nanite… | UE·游戏 | 巨型库内 UE 薄层 specialization | https://github.com/a5c-ai/babysitter | 能力清单薄层；暂不整包 | 观望 |
| kevinpbuckley UDS/UDW / gameplay-tags / landscape | UE | 无 SPDX；天气/天空包独特 | https://github.com/kevinpbuckley/unreal-engine-skills | 许可未变 | 观望 |
| CesiumGS / Flue / sipherxyz / abagames 其余 | 3D·工作流·2D | 维持上轮观望理由 | 各原仓 | 许可或重叠未变 | 观望 |

其余观望（teixasalone、TerminalSkills、ibrews、lpf513、story-to-game、OpenGame、pluginagentmarketplace、opusgamelabs、Stanestane bundle、linny006 索引仓等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 **SBOM identity matching**（方向无关，记数）
- `a596116/hao-skills` 的 `hao-visual`：个人暖色手帳视觉品牌，非游戏/UE
- `adobe/skills` 的 `ue-component-model`：**非 Unreal**（AEM Universal Editor）
- 今日新建噪声：`mossly/flights-skill`、`raymatos/skills-mcp`；repos search unreal/gamedev created≥08-04 为空
- code search：`filename:SKILL.md UnrealEngine` / `path:.agents/skills Unreal` → HTTP 429
- chris58530/gamedev-skills：0★；树中未见可用 `SKILL.md` 结构

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | **08-05 10:11Z**：SBOM identity matching（无关）；此后无新 commit |

## 本仓入库变化（+8 → 156）

- 新增 `skills/game-design/gamedev-genre-card-game/`
- 新增 `skills/game-design/gamedev-genre-puzzle/`
- 新增 `skills/game-design/gamedev-genre-tower-defense/`
- 新增 `skills/game-design/gamedev-genre-visual-novel/`
- 新增 `skills/game-design/omer-game-design-core/`
- 新增 `skills/ui-design/omer-game-ui-design/`
- 新增 `skills/3d/omer-vfx-realtime/`
- 新增 `skills/3d/omer-3d-modeling/`
- 各含 `SOURCE.md`；承接上轮 148 条精选内容

## 今天可行动

1. **装类型包收尾**：按当前项目选 `gamedev-genre-card-game` / `puzzle` / `tower-defense` / `visual-novel` 之一；卡牌向可叠加已有 `roguelike`（deckbuilder）。  
2. **试 omer 设计层**：用 `omer-game-design-core` 定核心循环与 MDA，再用 `omer-game-ui-design` 定 HUD 原则，落到已有 `ue-ui` / `gamedev-game-ui-ux`。  
3. **个人 skill 候选**：若常用 Rider 做 UE C++，观望并本地试 `JetBrains/rider-skills` 的 `ue-code-authoring`；确认 MCP 可用后再入库。VFX 向可把 `omer-vfx-realtime` + `unreal-niagara` 合成 `/vfx-readability-ue`。

## 已尝试查询

1. 种子仓 commits / meta API（JackyST0、mouadja02）  
2. 跟踪仓 `pushed_at` / trees / license（kevinpbuckley、quodsoler、gamedev-skills、sipherxyz、babysitter、hao-skills、cesiumjs、Flue、omer-metin、adobe/skills、abagames、JetBrains/rider-skills、prvthmpcypher）  
3. `gh search repos`：skill created≥08-05；unreal/gamedev/game design skills；updated≥07-29  
4. `gh search code`：`UnrealEngine filename:SKILL.md`；`path:.agents/skills Unreal`；`path:.cursor/skills game`（均 429）  
5. skills.sh/api/search：card-game、puzzle、tower-defense、visual-novel、game-ui-design、vfx-realtime、3d-modeling、game-design-core、unreal、gamedev、blender、umg、niagara、houdini、cesium、lumen、nanite、ue-angelscript 等  
6. 候选 raw/blob `SKILL.md` + 入库 / push / PR  
