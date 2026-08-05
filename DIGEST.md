# 技能侦察 DIGEST — 2026-08-05（22:00Z）

- 侦察时间：2026-08-05T22:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T21:00Z（同日上一轮，PR#20）
- 本仓入库：精选 **196** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-05-22`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。跟踪仓：ConnorGriffin 21:25Z 仅强化通用 `say-less`（忽略）；lisxa5747 21:27Z README 变为 SEO/下载页风格且质量下降（维持观望/降级）。本轮按「下次优先」补齐 omer：**rigging-animation / combat-design / game-audio / lighting-design / game-ai-behavior**；并引入 maystudios **Blueprint 程序化生成**与**第三方库接入**（MIT，本仓此前未收）；以及 MengTo（4105★ MIT）Web 向可测试动作战斗。新发现 [Yuki001/game-dev-skills](https://github.com/Yuki001/game-dev-skills)（49★，今日活跃，内容扎实）但无 LICENSE → 观望。kevinpbuckley 08-04 已 retarget UE 5.8 仍无 SPDX。今日新建噪声仍为 brand-copy / flights / skills-mcp。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| omer-rigging-animation | 3D·设计 | 骨骼层级、权重、FK/IK、面部绑定与引擎导出 | https://github.com/omer-metin/skills-for-antigravity | 123★ Apache-2.0；补齐绑定缺口；与 animation-systems 成对 | **引入** |
| omer-combat-design | 游戏设计 | 帧数据/判定框/连招/手感向战斗设计 | 同上 | 与已收 MRCalderon/wzhian combat 互补（更偏动作手感） | **引入** |
| omer-game-audio | 游戏设计 | FMOD/Wwise、自适应音乐、空间音频与预算 | 同上 | 补齐非街机向音频中间件路径 | **引入** |
| omer-lighting-design | 3D·设计 | 烘焙/实时光照、探针、Lumen/GI、氛围叙事光 | 同上 | 游戏灯光专项此前薄弱 | **引入** |
| omer-game-ai-behavior | 游戏设计 | BT/FSM/GOAP/效用 AI/寻路与感知 | 同上 | 与已有 gamedev-game-ai / UE AI 导航互补 | **引入** |
| maystudios-unreal-blueprint-codegen | UE | C++ 程序化生成 BP/WBP `.uasset`（含 cookbook） | https://github.com/maystudios/claude-skills | MIT；Marketplace/批量资产刚需；含实验模块模板 | **引入** |
| maystudios-unreal-thirdparty | UE | 第三方 C/C++ 库接入 Build.cs/链接/跨平台 | 同上 | MIT；插件与中间件集成高频痛点 | **引入** |
| mengto-design-action-combat | 游戏设计 | Web 动作战斗：startup/active/recovery 与确定性测试 | https://github.com/MengTo/Skills | 4105★ MIT；可测试 timing 规格，偏 ThreeJS/Web | **引入** |

本仓已摘录：

- `skills/3d/omer-rigging-animation/`（+ references）
- `skills/game-design/omer-combat-design/`（+ references）
- `skills/game-design/omer-game-audio/`（+ references）
- `skills/3d/omer-lighting-design/`（+ references）
- `skills/game-design/omer-game-ai-behavior/`（+ references）
- `skills/unreal/maystudios-unreal-blueprint-codegen/`（+ references/assets）
- `skills/unreal/maystudios-unreal-thirdparty/`（+ references）
- `skills/game-design/mengto-design-action-combat/`

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 18:06Z idea-refine；无新 commit | https://github.com/mouadja02/skills | **忽略**（通用 coding） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| ConnorGriffin/skills | 21:25Z say-less mid-conversation；ui-craft 未变 | https://github.com/ConnorGriffin/skills | 通用研发 → **忽略增量**；ui-craft 维持观望 |
| lisxa5747/unreal-angelscript-skills | 21:27Z README 改为 SEO/下载页；SKILL 未变 | https://github.com/lisxa5747/unreal-angelscript-skills | 质量信号下降；与 osseous 重叠 → **观望/降级** |
| kevinpbuckley/unreal-engine-skills | 08-04 UE 5.8 retarget；仍无 LICENSE | https://github.com/kevinpbuckley/unreal-engine-skills | 维持观望（等 SPDX） |
| sipherxyz/universal-ue-skills | 07-31；1★ 无 LICENSE；含 renderdoc/crash 等 | https://github.com/sipherxyz/universal-ue-skills | 观望 |
| Yuki001/game-dev-skills | 今日活跃；49★；architect/toon shader/图像管线扎实 | https://github.com/Yuki001/game-dev-skills | **新增观望**（无 LICENSE） |
| snipereagle1/eve-skills / Flue / Rider / donchitos 其余 | 无新实质或理由未变 | 各原仓 | 维持观望 |

### 累计建议引入（仍有效）

1–72. 维持至上轮（含 omer art-consistency/voxel/animation、osseous AS 三件套、donchitos art-bible/consistency）  
73. **+ 本轮** omer：rigging-animation / combat-design / game-audio / lighting-design / game-ai-behavior  
74. **+ 本轮** maystudios：unreal-blueprint-codegen / unreal-thirdparty  
75. **+ 本轮** mengto-design-action-combat  

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| Yuki001/game-dev-skills | 游戏设计·3D·工作流 | game-architect / animation-shader / 图像资产生成环 / GAT 设计流 | https://github.com/Yuki001/game-dev-skills | 49★ 今日活跃、说明清晰可装；**无 LICENSE** | 观望 |
| omer-creature-design 等 | 2D·游戏设计 | 生物/怪物造型与解剖逻辑 | https://github.com/omer-metin/skills-for-antigravity | 本轮优先绑定/战斗/音频/光照/AI；下次可摘 | 观望 |
| lisxa5747 AngelScript | UE | AS skill 包 | https://github.com/lisxa5747/unreal-angelscript-skills | README 劣化；优先 osseous MIT | 观望/降级 |
| kevinpbuckley UE 5.8 | UE | 核心 UE skill 集 retarget 5.8 | https://github.com/kevinpbuckley/unreal-engine-skills | 有更新但无 SPDX | 观望 |
| sipherxyz/universal-ue-skills | UE·工作流 | RenderDoc/Crash/Localization 等运维向 | https://github.com/sipherxyz/universal-ue-skills | 1★ 无 LICENSE | 观望 |
| maystudios 2d-pixel-asset | 2D | Gemini+Chrome 自动化像素资产 | https://github.com/maystudios/claude-skills | 强依赖 Claude-in-Chrome/Gemini 登录 | 观望 |
| NAJEMWEHBE driving-unreal | UE·工作流 | MCP 驱动 UE 编辑器 | https://github.com/NAJEMWEHBE/unreal-ai-connection | MIT 9★；强依赖其 MCP 桥 | 观望 |
| ConnorGriffin ui-craft / abagames Godot 音频 / Rider / Flue / donchitos 其余 / eve-skills / cesiumjs | 各向 | 维持上轮理由 | 各原仓 | 未变 | 观望 |

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 idea-refine（方向无关，记数）
- ConnorGriffin 本轮 say-less 增量（通用研发）
- 今日新建噪声：`vaishnvaik6/brand-website-copy-skill`、`mossly/flights-skill`、`raymatos/skills-mcp`
- gisenberg/unreal-skills：无 LICENSE；优先 osseous
- adobe ue-component-model：AEM，非虚幻

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 仍为 **08-05 18:06Z** idea-refine portable（无关）；此后无新 commit |

## 本仓入库变化（+8 → 196）

- 新增 `skills/3d/omer-rigging-animation/`
- 新增 `skills/game-design/omer-combat-design/`
- 新增 `skills/game-design/omer-game-audio/`
- 新增 `skills/3d/omer-lighting-design/`
- 新增 `skills/game-design/omer-game-ai-behavior/`
- 新增 `skills/unreal/maystudios-unreal-blueprint-codegen/`
- 新增 `skills/unreal/maystudios-unreal-thirdparty/`
- 新增 `skills/game-design/mengto-design-action-combat/`
- 各含 `SOURCE.md`；承接上轮 188 条精选内容

## 今天可行动

1. **补战斗设计三角**：试 `omer-combat-design`（手感/帧数据）+ `mengto-design-action-combat`（可测试 timing）对照已有 combat；选一改成你的 UE 输入/状态机个人 skill。  
2. **UE 工具链**：需要批量 BP/WBP 或接第三方库时，直接装 `maystudios-unreal-blueprint-codegen` / `maystudios-unreal-thirdparty`。  
3. **角色管线闭合**：用 `omer-rigging-animation` + 已装 `omer-animation-systems` / `ue-animation-system` 跑一条绑定→导出→引擎验证；灯光项目加 `omer-lighting-design`。

## 已尝试查询

1. 种子仓 commits / repo meta（JackyST0、mouadja02）
2. 跟踪仓 pushed_at / trees / license（omer、osseous、donchitos、abagames、lisxa5747、ConnorGriffin、eve、kevin、sipher、gisenberg、Rider、Flue、Yuki001、maystudios、MengTo、Italink、Randroids、NAJEMWEHBE 等）
3. repos search：skill created≥08-05；unreal/gamedev/game design skills；agent skills + game/UE
4. code search：Unreal filename:SKILL.md（成功）；path:.agents/skills / path:.cursor/skills（空/受限）
5. skills.sh/api/search：unreal、umg、level design、voxel、pixel art、animation、concept art、game audio、ui design、angelscript、art consistency、combat、art bible、rigging、game studio、game design、godot、unity、blender
6. 候选 blob SKILL.md 质量核 + 入库 + push + open_git_pr + Slack
