# 技能侦察 DIGEST — 2026-08-05（15:00Z）

- 侦察时间：2026-08-05T15:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T14:00Z（同日上一轮，PR#14）
- 本仓入库：精选 **148** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-05-15`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill（JackyST0 停在 08-03 star chore；mouadja02 仍为 10:11Z SBOM）。跟踪仓无新实质 push；kevinpbuckley / sipherxyz 许可仍缺；babysitter 的 UE Nanite/Lumen 等确认为能力清单薄层。本轮按「下次优先」做**工作流 + 类型包缺口补齐**：从 [gamedev-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)（414★ Apache-2.0）引入 game-jam / steam-publish / itch-publish，以及 roguelike / rpg / fps-shooter / platformer / survival-crafting 五类。新确认 [omer-metin/skills-for-antigravity](https://github.com/omer-metin/skills-for-antigravity)（123★ Apache-2.0）含大量 game/UI/3D skill，入观望待精选。skills.sh 上 `adobe/skills/ue-component-model` 实为 Adobe Universal Editor（AEM），**非虚幻**，记忽略。code search 仍 429。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| gamedev-game-jam | 工作流 | Jam 倒计时范围锁定 / 小时排程 / 砍功能 / 按时提交 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~734 安装；与 `prototype-fast` 互补（有截止 vs 无截止） | **引入** |
| gamedev-steam-publish | 工作流 | Steamworks / SteamPipe / depot / steamcmd 上架清单 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~763 安装；含 steampipe 参考；发行刚需 | **引入** |
| gamedev-itch-publish | 工作流 | itch.io 页面 + butler push 渠道与版本 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~739 安装；Jam/Demo 上传闭环 | **引入** |
| gamedev-genre-roguelike | 游戏设计 | 回合网格 / 程序化地城 / FOV / 永久死亡 / 掉落表 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 类型组合 skill；接已有 procgen / save | **引入** |
| gamedev-genre-rpg | 游戏设计 | 属性升级 / 背包装备 / 任务 / 对话 / 战斗公式 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 接 dialogue / economy / GAS 设计层 | **引入** |
| gamedev-genre-fps-shooter | 游戏设计 | 第一人称瞄准 / hitscan·弹道 / TTK·后坐·散布 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 与 CMC / 输入 / 手感 skill 拼装射击原型 | **引入** |
| gamedev-genre-platformer | 游戏设计 | 跑跳手感：郊狼时间 / 跳跃缓冲 / 可变高度 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 与 input-systems / physics-tuning 形成手感闭环 | **引入** |
| gamedev-genre-survival-crafting | 游戏设计 | 采集→合成→基地 / 生存需求 / 科技树 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 开放世界/生存向组合包；接 inventory·procgen | **引入** |

本仓已摘录：

- `skills/workflow/gamedev-game-jam/`
- `skills/workflow/gamedev-steam-publish/`（+ references）
- `skills/workflow/gamedev-itch-publish/`（+ references）
- `skills/game-design/gamedev-genre-roguelike/`（+ references）
- `skills/game-design/gamedev-genre-rpg/`（+ references）
- `skills/game-design/gamedev-genre-fps-shooter/`（+ references）
- `skills/game-design/gamedev-genre-platformer/`（+ references）
- `skills/game-design/gamedev-genre-survival-crafting/`（+ references）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 10:11Z SBOM；无更新 | https://github.com/mouadja02/skills | **忽略**（DevOps） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| kevinpbuckley | 仍 08-04；无 SPDX；UDS/UDW 独特 | https://github.com/kevinpbuckley/unreal-engine-skills | 维持观望 |
| sipherxyz | 仍无 LICENSE | https://github.com/sipherxyz/universal-ue-skills | 维持观望 |
| a5c-ai/babysitter | Nanite/Lumen 等确认为薄层能力表 | https://github.com/a5c-ai/babysitter | 维持观望 |
| a596116/hao-skills | 无新 push | https://github.com/a596116/hao-skills | 维持观望 |
| CesiumGS / Flue | 无新实质变化 | 各原仓 | 维持观望 |
| adobe/skills ue-component-model | skills.sh 误触「UE」；实为 AEM Universal Editor | https://github.com/adobe/skills | **忽略**（非虚幻） |

### 累计建议引入（仍有效）

1–56. 维持至上轮（含 quodsoler 核心与 gamedev disciplines / prototype-fast 等）  
57. **+ 本轮** gamedev workflows：game-jam / steam-publish / itch-publish  
58. **+ 本轮** gamedev genres：roguelike / rpg / fps-shooter / platformer / survival-crafting  

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| omer-metin/skills-for-antigravity（game-design-core / game-ui-design / vfx-realtime / 3d-modeling…） | 游戏设计·UI·3D | 大型通用 skill 库中的游戏/设计子集 | https://github.com/omer-metin/skills-for-antigravity | 123★ Apache-2.0；条目多、质量待逐条精选 | 观望 |
| gamedev 其余 genres（card-game / puzzle / tower-defense / visual-novel） | 游戏设计 | 剩余类型包 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 主流五类已收；其余按项目再取 | 观望 |
| quodsoler 重叠项（ue-input-system / ue-ui-umg-slate / ue-procedural-generation / ue-gameplay-abilities） | UE | 与已有 Enhanced Input / UMG / Procgen / GAS 重叠 | https://github.com/quodsoler/unreal-engine-skills | 核心缺口已收完；重叠项按需加深 | 观望 |
| a5c-ai/babysitter unreal-chaos / lumen / nanite… | UE·游戏 | 巨型库内 UE 薄层 specialization | https://github.com/a5c-ai/babysitter | 本轮抽查 Nanite 确认为能力清单；暂不整包引入 | 观望 |
| kevinpbuckley UDS/UDW / gameplay-tags / landscape | UE | 无 SPDX；天气/天空包独特 | https://github.com/kevinpbuckley/unreal-engine-skills | 许可未变 | 观望 |
| CesiumGS / Flue / hao-skills / sipherxyz / abagames 其余 | 3D·工作流·2D | 维持上轮观望理由 | 各原仓 | 许可或重叠未变 | 观望 |

其余观望（teixasalone、TerminalSkills、ibrews、lpf513、story-to-game、OpenGame、pluginagentmarketplace、opusgamelabs、Stanestane bundle、linny006 索引仓等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 **SBOM identity matching**（方向无关，记数）
- `adobe/skills` 的 `ue-component-model`：**非 Unreal**，为 AEM Universal Editor
- 今日新建噪声：`mossly/flights-skill`、`raymatos/skills-mcp`（基础设施）、大量 GitHub Skills 练习仓
- code search：UnrealEngine filename:SKILL.md → HTTP 429；majiayu000 巨型镜像仍属噪声源
- chris58530/gamedev-skills：0★；树中未见可用 `SKILL.md` 结构

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | **08-05 10:11Z**：SBOM identity matching（无关）；此后无新 commit |

## 本仓入库变化（+8 → 148）

- 新增 `skills/workflow/gamedev-game-jam/`
- 新增 `skills/workflow/gamedev-steam-publish/`
- 新增 `skills/workflow/gamedev-itch-publish/`
- 新增 `skills/game-design/gamedev-genre-roguelike/`
- 新增 `skills/game-design/gamedev-genre-rpg/`
- 新增 `skills/game-design/gamedev-genre-fps-shooter/`
- 新增 `skills/game-design/gamedev-genre-platformer/`
- 新增 `skills/game-design/gamedev-genre-survival-crafting/`
- 各含 `SOURCE.md`；承接上轮 140 条精选内容

## 今天可行动

1. **装发行三件套**：`gamedev-game-jam` + `gamedev-itch-publish`（Jam 周末用）；要上 Steam 再加 `gamedev-steam-publish`。  
2. **试类型→引擎拼装**：用 `gamedev-genre-fps-shooter` 定 TTK/后坐模型，再用已有 `ue-character-movement` + `gamedev-input-systems` 落到 UE 原型。  
3. **个人 skill 候选**：若常做独立发行，把 jam + itch + prototype-fast 合成 `/ship-weekend-build`；若做生存/开放世界，把 survival-crafting + procedural-gen + ue-world-level-streaming 合成 `/survival-loop-ue`。

## 已尝试查询

1. 种子仓 commits / meta API（JackyST0、mouadja02）  
2. 跟踪仓 `pushed_at` / trees / license（kevinpbuckley、quodsoler、gamedev-skills、sipherxyz、babysitter、hao-skills、cesiumjs、Flue、omer-metin、adobe/skills、abagames、Stanestane）  
3. `gh search repos`：skill created≥08-05；unreal/gamedev/game design/UE5 skills  
4. `gh search code`：`UnrealEngine filename:SKILL.md`；`path:.agents/skills Unreal`（429）  
5. skills.sh/api/search：unreal、gamedev、blender、game design、niagara、umg、houdini、ui design、nanite、lumen、cesium、steam、game jam、landscape、gameplay tags、angelscript、steam-publish、game-jam、itch-publish、ue-ui-umg-slate、ue-input-system、ue-procedural-generation、ue-gameplay-abilities、vfx-realtime  
6. 候选 raw/blob `SKILL.md` + 入库 / push / PR  
