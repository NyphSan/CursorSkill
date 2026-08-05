# 技能侦察 DIGEST — 2026-08-05（14:00Z）

- 侦察时间：2026-08-05T14:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T13:00Z（同日上一轮，PR#13）
- 本仓入库：精选 **140** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-05-14`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill（JackyST0 停在 08-03 star chore；mouadja02 仍为 10:11Z SBOM）。跟踪仓无新实质 push（kevinpbuckley / sipherxyz 许可仍缺；hao-skills 13:11Z 删除 oil-visual 并改 Agent Skills 布局，仍 0★）。本轮按「下次优先」继续**缺口补齐**：① [quodsoler](https://github.com/quodsoler/unreal-engine-skills)（301★ MIT）收完剩余核心五件：async-threading / materials-rendering / testing-debugging / module-build / project-context；② [gamedev-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)（414★ Apache-2.0）补 dialogue / audio / prototype-fast。官方 [CesiumGS/cesiumjs-skills](https://github.com/CesiumGS/cesiumjs-skills)（110★ Apache-2.0）与 [SFKislev/Flue](https://github.com/SFKislev/Flue)（65★ MIT，Blender/Houdini 桥）维持观望。今日新建噪声仍高（GitHub Skills 练习仓、iOS 提交、PPT/封面等）。code search 仍偶发 429。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| ue-async-threading | UE | FRunnable / TaskGraph / UE::Tasks / ParallelFor / 线程安全 | https://github.com/quodsoler/unreal-engine-skills | 301★ MIT；补并发与任务图；与网络/流送 skill 分工清晰 | **引入** |
| ue-materials-rendering | UE | MID / MPC / 后处理 / RT / Decal / Nanite·Lumen·VSM | https://github.com/quodsoler/unreal-engine-skills | 含参数与后处理参考；与已有材质/HLSL skill 形成 C++ 运行时侧 | **引入** |
| ue-testing-debugging | UE | Automation / FunctionalTest / UE_LOG / Insights / DrawDebug | https://github.com/quodsoler/unreal-engine-skills | 本仓测试/调试缺完整 MIT 包；含 automation 与 profiling 参考 | **引入** |
| ue-module-build-system | UE | Build.cs / Target.cs / 插件 / IWYU / 常见链接错误 | https://github.com/quodsoler/unreal-engine-skills | 与 `ue-build` 互补加深；修模块依赖刚需 | **引入** |
| ue-project-context | UE·工作流 | 生成/维护 `.agents/ue-project-context.md` 供全套 UE skill 读取 | https://github.com/quodsoler/unreal-engine-skills | 整仓 quodsoler 的「枢纽」；先装它再装其余性价比最高 | **引入** |
| gamedev-dialogue-systems | 游戏设计 | 分支对话图 / Ink·Yarn / 条件·变量·本地化钩子 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~897 安装；补叙事执行层，接已有 narrative-design | **引入** |
| gamedev-audio-design | 游戏设计 | 总线混音 / ducking / 自适应音乐层 / SFX 变体 / 节拍同步 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~933 安装；与 `ue-audio-system` 形成设计→API 链路 | **引入** |
| gamedev-prototype-fast | 工作流 | 1 小时可玩原型：单一问题 / 灰盒 / keep·kill 标准 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 工作流纪律；独立游戏/关卡验证日用 | **引入** |

本仓已摘录：

- `skills/unreal/ue-async-threading/`（+ references）
- `skills/unreal/ue-materials-rendering/`（+ references）
- `skills/unreal/ue-testing-debugging/`（+ references）
- `skills/unreal/ue-module-build-system/`（+ references）
- `skills/unreal/ue-project-context/`
- `skills/game-design/gamedev-dialogue-systems/`（+ references）
- `skills/game-design/gamedev-audio-design/`（+ references）
- `skills/game-design/gamedev-prototype-fast/`

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 10:11Z SBOM；无更新 | https://github.com/mouadja02/skills | **忽略**（DevOps） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| a596116/hao-skills | 13:11Z 删 oil-visual、改 open-spec 布局；仍仅 hao-visual | https://github.com/a596116/hao-skills | 维持观望（0★，无 LICENSE） |
| kevinpbuckley | 仍为 08-04 推送；无 SPDX | https://github.com/kevinpbuckley/unreal-engine-skills | 维持观望 |
| sipherxyz | 仍无 LICENSE | https://github.com/sipherxyz/universal-ue-skills | 维持观望 |
| CesiumGS/cesiumjs-skills | 110★ Apache-2.0；15 个 CesiumJS skill | https://github.com/CesiumGS/cesiumjs-skills | 观望（偏地球/GIS，非游戏主线） |
| SFKislev/Flue | 65★ MIT；Blender/Houdini 壳桥 | https://github.com/SFKislev/Flue | 观望（需本机 Flue 运行时） |
| flashpoint493 / omer-metin / maystudios | 无新实质变化 | 各原仓 | 维持观望 |

### 累计建议引入（仍有效）

1–54. 维持至上轮（含 CMC/网络/Niagara/编辑器/物理·性能·着色·输入等）  
55. **+ 本轮** quodsoler：async-threading / materials-rendering / testing-debugging / module-build-system / project-context  
56. **+ 本轮** gamedev-skills：dialogue-systems / audio-design / prototype-fast  

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| CesiumGS/cesiumjs-skills（viewer-setup / custom-shader / 3d-tiles…） | 3D | 官方 CesiumJS Agent Skills 套件 | https://github.com/CesiumGS/cesiumjs-skills | 110★ Apache-2.0；与开放世界/地球可视化相关，非 UE 主线 | 观望 |
| SFKislev/Flue（blender / houdini） | 3D·工作流 | 无 MCP 的 shell→bpy/Houdini 桥 | https://github.com/SFKislev/Flue | 65★ MIT；安装量高但依赖本机 Flue | 观望 |
| a596116/hao-skills（hao-visual） | 2D·设计 | 暖色手帳风插画 persona | https://github.com/a596116/hao-skills | 本轮有结构清理；仍 0★ 无 LICENSE | 观望 |
| gamedev-skills genres / 其余 workflows（game-jam / itch / steam） | 游戏设计·工作流 | 类型包与发行流程 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | disciplines 已收齐主流；类型/发行按项目再取 | 观望 |
| quodsoler 其余（ue-input-system / ue-ui-umg-slate / ue-procedural-generation / ue-gameplay-abilities…） | UE | 与已有 Enhanced Input / UMG / GAS / Procgen 重叠 | https://github.com/quodsoler/unreal-engine-skills | 核心缺口已收完；重叠项按需 | 观望 |
| a5c-ai/babysitter unreal-chaos / lumen / nanite… | UE·游戏 | 巨型库内 UE 薄层 specialization | https://github.com/a5c-ai/babysitter | 1646★ MIT；质量待逐条核 | 观望 |
| aws-deadline / maystudios / omer-metin / flashpoint493 | UE·UI·AS | 维持上轮观望理由 | 各原仓 | 重叠或许可/栈特定 | 观望 |
| kevinpbuckley UDS/UDW / gameplay-tags / landscape | UE | 无 SPDX；天气/天空包独特 | https://github.com/kevinpbuckley/unreal-engine-skills | 许可未变 | 观望 |
| sipherxyz / Italink / abagames 其余 | UE·3D·工作流 | 维持上轮观望理由 | 各原仓 | 许可或重叠未变 | 观望 |

其余观望（teixasalone、TerminalSkills、ibrews、lpf513、story-to-game、OpenGame、pluginagentmarketplace、opusgamelabs、linny006/awesome-agent-skills 索引仓等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 **SBOM identity matching**（方向无关，记数）
- 今日新建噪声：大量 `skills-introduction-to-github` 练习仓、`cwoneday/ios-app-store-submit`、`liumourencn/lazyc-cover-`（自媒体封面）、`alan00205-creator/claude-video-editing-skills`（剪辑）、Expo/SpringBoot 技能仓
- code search 噪声：majiayu000 巨型镜像仍占 UnrealEngine filename:SKILL.md 结果
- chris58530/gamedev-skills：0★；树中未见可用 `SKILL.md` 结构

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | **08-05 10:11Z**：SBOM identity matching（无关）；此后无新 commit |

## 本仓入库变化（+8 → 140）

- 新增 `skills/unreal/ue-async-threading/`
- 新增 `skills/unreal/ue-materials-rendering/`
- 新增 `skills/unreal/ue-testing-debugging/`
- 新增 `skills/unreal/ue-module-build-system/`
- 新增 `skills/unreal/ue-project-context/`
- 新增 `skills/game-design/gamedev-dialogue-systems/`
- 新增 `skills/game-design/gamedev-audio-design/`
- 新增 `skills/game-design/gamedev-prototype-fast/`
- 各含 `SOURCE.md`；承接上轮 132 条精选内容

## 今天可行动

1. **先装枢纽再装其余（MIT）**：`ue-project-context` → 再挂 `ue-module-build-system` + `ue-testing-debugging`，把「项目约定 / Build.cs / 自动化测试」一次打通。  
2. **试渲染闭环**：用 `ue-materials-rendering` 定 MID/MPC/后处理，再用已有 `hlsl-shader` / Niagara 做特效层；Nanite·Lumen 决策写进 project-context。  
3. **个人 skill 候选**：叙事向把 `gamedev-dialogue-systems` + 已有 `narrative-design` 合成 `/ue-dialogue`；原型验证把 `gamedev-prototype-fast` 改成你的 `/greybox-1h`（写死 keep/kill 模板）。

## 已尝试查询

1. 种子仓 commits / meta API（JackyST0、mouadja02）  
2. 跟踪仓 `pushed_at` / trees / license（kevinpbuckley、quodsoler、gamedev-skills、sipherxyz、babysitter、hao-skills、cesiumjs-skills、Flue、flashpoint493、omer-metin、maystudios 等）  
3. `gh search repos`：`skill` created≥08-05；`unreal/gamedev/game design/UE5/3D agent/awesome agent skills`  
4. `gh search code`：`UnrealEngine filename:SKILL.md`（部分成功）；`path:.cursor/skills` / `path:.agents/skills`（429）  
5. skills.sh/api/search：unreal、gamedev、blender、game design、niagara、umg、houdini、dialogue、audio、materials、async、module build、project context、testing、nanite、lumen、cesium 等  
6. 候选 raw/blob `SKILL.md` + 入库 / push / PR  
