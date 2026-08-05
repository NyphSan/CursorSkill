# 技能侦察 DIGEST — 2026-08-05（12:00Z）

- 侦察时间：2026-08-05T12:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T11:00Z（同日上一轮，PR#11）
- 本仓入库：精选 **124** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-05-12`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓无方向相关新 skill（JackyST0 仍停在 08-03 star chore；mouadja02 无新 commit）。跟踪仓无新 push。本轮继续**缺口补齐 + 观望晋级**：① [quodsoler](https://github.com/quodsoler/unreal-engine-skills)（301★ MIT）补 Physics·Collision / Game Features / DataAssets·Tables / Actor-Component；② [gamedev-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)（414★ Apache-2.0）补 camera / save / procedural-gen 跨引擎纪律（与上轮 UE SaveGame / PCG 互补）；③ [abagames maximizing-game-feel](https://github.com/abagames/agentic-gamedev-skills) 从观望晋级。新发现 aws-deadline UE 渲染管线 skill、maystudios 部分重叠项入观望。今日 `skill` 新建噪声仍为 flights/skills-mcp 等无关项；code search `path:SKILL.md` 一度 429。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| ue-physics-collision | UE | Chaos / 碰撞通道 / Trace·Sweep / Overlap / 物理材质 | https://github.com/quodsoler/unreal-engine-skills | 301★ MIT；本仓无独立碰撞 skill；含 channel/trace 参考 | **引入** |
| ue-game-features | UE | Game Feature 插件 / ModularGameplay / Lyra Experience | https://github.com/quodsoler/unreal-engine-skills | 模块化玩法与 DLC 式激活核心路径；含 experience 参考 | **引入** |
| ue-data-assets-tables | UE | DataAsset / DataTable / SoftRef / AssetManager 异步加载 | https://github.com/quodsoler/unreal-engine-skills | 数据驱动与上轮 SaveGame 形成数据闭环 | **引入** |
| ue-actor-component-architecture | UE | Actor 生命周期 / 组件组合 / Spawn·接口模式 | https://github.com/quodsoler/unreal-engine-skills | 全系列基础；含 lifecycle / component-types 参考 | **引入** |
| gamedev-camera-systems | 游戏设计 | 跨引擎镜头：follow / deadzone / look-ahead / 3P orbit | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~938 安装 Apache-2.0；补策划·手感层镜头纪律 | **引入** |
| gamedev-save-systems | 游戏设计 | 跨引擎存档：版本化 / 原子写 / 迁移 / autosave | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~969 安装；与 `ue-serialization-savegames` 互补（设计 vs API） | **引入** |
| gamedev-procedural-gen | 游戏设计 | 种子 RNG / noise / 地牢 BSP / 加权掉落 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~961 安装；与已有 `unreal-pcg-python` 互补 | **引入** |
| maximizing-game-feel | 游戏设计 | 把「能跑」的动作游戏拉到手感可读的反馈栈 | https://github.com/abagames/agentic-gamedev-skills | MIT；观望晋级；含 technique-catalog；与 feel 设计互补 | **引入** |

本仓已摘录：

- `skills/unreal/ue-physics-collision/`（+ references）
- `skills/unreal/ue-game-features/`（+ references）
- `skills/unreal/ue-data-assets-tables/`（+ references）
- `skills/unreal/ue-actor-component-architecture/`（+ references）
- `skills/game-design/gamedev-camera-systems/`（+ references）
- `skills/game-design/gamedev-save-systems/`（+ references）
- `skills/game-design/gamedev-procedural-gen/`（+ references）
- `skills/game-design/maximizing-game-feel/`（+ references）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 12:00Z 前仍为 10:11Z SBOM；无更新 | https://github.com/mouadja02/skills | **忽略**（DevOps） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| kevinpbuckley | 仍为 08-04 推送；无 SPDX；本轮优先 MIT quodsoler 同主题 | https://github.com/kevinpbuckley/unreal-engine-skills | 维持观望 |
| sipherxyz | 仍无 LICENSE；16 skills 偏工具链 | https://github.com/sipherxyz/universal-ue-skills | 维持观望 |
| Italink / cesiumjs / flue | 无新 push | 各原仓 | 维持观望 |

### 累计建议引入（仍有效）

1–49. 维持至上轮（含 Audio/Save/Streaming/Nav/QA/GameAI/Balance 等）  
50. **+ 本轮** quodsoler：physics-collision / game-features / data-assets-tables / actor-component-architecture  
51. **+ 本轮** gamedev-skills：camera-systems / save-systems / procedural-gen  
52. **+ 本轮晋级** abagames `maximizing-game-feel`

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| aws-deadline ue-design / ue-dev-setup | UE·工作流 | Deadline Cloud 渲染/作业提交相关 UE skill | https://github.com/aws-deadline/deadline-cloud-for-unreal-engine | 20★ Apache-2.0；08-03 有推送；偏云渲染农场场景 | 观望 |
| maystudios unreal-gas / unreal-pcg / best-practices | UE | MIT 小仓；与已入库 GAS/PCG/Best Practices 重叠 | https://github.com/maystudios/claude-skills | 15★；内容重叠高 | 观望 |
| omer-metin game-ui-design | UI·游戏设计 | 高安装通用游戏 UI persona | https://github.com/omer-metin/skills-for-antigravity | 2441 安装 Apache-2.0；与已有 UI 精选重叠，偏 persona | 观望 |
| flashpoint493/unreal-angelscript | UE | Hazelight UE-AS 语法/网络/GAS/CommonUI | https://github.com/flashpoint493/unreal-angelscript-skills | 30★ NOASSERTION；仅 AS 栈需要 | 观望 |
| teixasalone / TerminalSkills / Randroids-Dojo / ibrews | UE | 维持上轮观望理由 | 各原仓 | 同构或许可不清 | 观望 |
| quodsoler 其余（networking / niagara-effects / character-movement / editor-tools…） | UE | 27 skills 中未精选部分 | https://github.com/quodsoler/unreal-engine-skills | 本轮再收 4 个；其余按需 | 观望 |
| gamedev-skills physics-tuning / performance / shader / input / genres | 游戏设计 | 纪律包与类型剩余项 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 高安装；本轮已收 camera/save/procgen | 观望 |
| abagames 其余（Godot 脚手架 / 音频 / adversarial repair…） | 游戏设计·工作流 | agentic gamedev 研究向 | https://github.com/abagames/agentic-gamedev-skills | maximizing-game-feel 已晋级；其余仍观望 | 观望 |
| kevinpbuckley UDS/UDW / gameplay-tags / landscape | UE | 无 SPDX；天气/天空包独特但许可风险 | https://github.com/kevinpbuckley/unreal-engine-skills | 许可未变 | 观望 |
| sipherxyz / Italink niagara-editing+modeling-* / OpenClaw / UAssetAPI / flue / cesiumjs / alterlab | UE·3D·工作流 | 维持上轮观望理由 | 各原仓 | 许可或重叠未变 | 观望 |

其余观望（lpf513、story-to-game、OpenGame、miramocha、fairypark/oliver-io、hkuds、pluginagentmarketplace、opusgamelabs、cowork-os、NAJEMWEHBE/UnrealMCPHub、liuhuagang/mrSutivu 等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 **SBOM identity matching**（方向无关，记数）
- 今日新建：`mossly/flights-skill`、`raymatos/skills-mcp`（无关）
- code search 噪声：majiayu000 巨型镜像、modbender、j4flmao、paxlabs、VibeStudio、作业/作品展示仓、priyanshshahh/quant-link
- chris58530/gamedev-skills：0★；树中未见 `SKILL.md`
- alvinunreal/oh-my-opencode-slim：通用 agent 套件

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | **08-05 10:11Z**：SBOM identity matching（无关）；此后无新 commit |

## 本仓入库变化（+8 → 124）

- 新增 `skills/unreal/ue-physics-collision/`
- 新增 `skills/unreal/ue-game-features/`
- 新增 `skills/unreal/ue-data-assets-tables/`
- 新增 `skills/unreal/ue-actor-component-architecture/`
- 新增 `skills/game-design/gamedev-camera-systems/`
- 新增 `skills/game-design/gamedev-save-systems/`
- 新增 `skills/game-design/gamedev-procedural-gen/`
- 新增 `skills/game-design/maximizing-game-feel/`
- 各含 `SOURCE.md`；承接上轮 116 条精选内容

## 今天可行动

1. **装 UE 基建四件套（MIT）**：`ue-actor-component-architecture` + `ue-physics-collision` + `ue-data-assets-tables` + `ue-game-features`，与上轮 Audio/Save/Streaming/Nav 拼成「架构 + 物理 + 数据 + 模块化」日常包。  
2. **试镜头/存档/程序生成纪律**：对现有第三人称镜头跑一遍 `gamedev-camera-systems`；把存档策略用 `gamedev-save-systems` 定 schema，再用 `ue-serialization-savegames` 落地 USaveGame。  
3. **个人 skill 候选**：若做 Lyra 式项目，把 `ue-game-features` + 已有 GAS/Input 合成个人 `/ue-modular-feature`；若做手感打磨，把 `maximizing-game-feel` + 已有 `gamedev-game-feel` 合成 `/game-feel-pass`。

## 已尝试查询

1. 种子仓 commits / meta API（JackyST0、mouadja02）  
2. 跟踪仓 `pushed_at` / trees（kevinpbuckley、quodsoler、gamedev-skills、w-zhian、sipherxyz、Italink、cesiumgs、sfkislev/flue、aws-deadline、maystudios、abagames、omer-metin 等）  
3. `gh search repos`：`unreal skill SKILL.md`；`gamedev skills`；`skills SKILL.md` created≥08-05  
4. `gh search code`：`Unreal filename:SKILL.md`（成功）；`game design filename:SKILL.md`（成功）；`UE5 OR UnrealEngine path:SKILL.md` 一度 429  
5. skills.sh/api/search：unreal、gamedev、blender、game design、niagara、umg、houdini、3d modeling、sequencer、state tree、mover、angelscript、ui design、godot、flue、cesium、save-systems、camera-systems  
6. 候选 raw/blob `SKILL.md` + 入库 / push / PR  
