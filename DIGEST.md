# 技能侦察 DIGEST — 2026-08-05（09:00Z）

- 侦察时间：2026-08-05T09:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T08:00Z（同日上一轮，PR#8）
- 本仓入库：精选 **100** 个 `SKILL.md`（较上轮 +7；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-05-09`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。跟踪仓（kevinpbuckley / VibeUE / db-lyon / Extreme11111 等）无新实质提交。**实质增量来自补漏扫描**：① [toamig/claude-unreal-skills](https://github.com/toamig/claude-unreal-skills)（MIT，Replication / Design Patterns / SOLID 三件套，补多人架构空白）；② [GuangminJu/UnrealSkills](https://github.com/GuangminJu/UnrealSkills)（12★ MIT，自动 `ue-build` / `ue-test` + scripts）；③ [guangyuspace/codex-gamestudio-skill](https://github.com/guangyuspace/codex-gamestudio-skill)（43★ MIT，多角色工作室工作流 + Handoff）；④ 观望晋级 [maystudios/claude-skills](https://github.com/maystudios/claude-skills) 的 `unreal-gas`（深度 GAS C++ + references）。`path:.cursor/skills` code search 仍易 **429**；今日 `skill` 新建噪声 ≥100。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| unreal-replication | UE | 服务器权威多人同步设计（状态归属 / RPC / relevancy / GAS 网络） | https://github.com/toamig/claude-unreal-skills | MIT；决策表清晰；含 `references/networking.md`；补齐多人空白 | **引入** |
| unreal-design-patterns | UE | UE5 C++ 中识别引擎已有模式 vs 手写 GoF/游戏模式 | https://github.com/toamig/claude-unreal-skills | MIT；「先用引擎再手写」纪律强；与 SOLID 成套 | **引入** |
| unreal-solid | UE | UE5 C++ 的 SOLID 落地（Subsystem / 组件 / Tag 边界） | https://github.com/toamig/claude-unreal-skills | MIT；架构评审时主动触发；与 patterns/replication 互补 | **引入** |
| ue-build | UE·工作流 | 改 C++ 后自动探测引擎/工程并编译 | https://github.com/GuangminJu/UnrealSkills | 12★ MIT；含 `detect_ue.py`；TDD 闭环入口 | **引入** |
| ue-test | UE·工作流 | 跑 UE 自动化测试并报告 | https://github.com/GuangminJu/UnrealSkills | 与 ue-build 成对；含 `run_ue_tests.py` | **引入** |
| unreal-gas-cpp | UE | 深度 GAS C++（ASC/GE/预测复制/陷阱） | https://github.com/maystudios/claude-skills | 从观望晋级；4 份 references；与已入库 kevinpbuckley GAS 互补 | **引入** |
| gamestudio | 游戏设计·工作流 | 多角色游戏工作室流程 + 手机 UI 门禁 + Handoff/Debug | https://github.com/guangyuspace/codex-gamestudio-skill | 43★ MIT；实机上架展示；流程可迁移 UE | **引入** |

本仓已摘录：

- `skills/unreal/unreal-replication/`（+ references）
- `skills/unreal/unreal-design-patterns/`（+ references）
- `skills/unreal/unreal-solid/`（+ references）
- `skills/unreal/ue-build/`（+ scripts）
- `skills/unreal/ue-test/`（+ scripts）
- `skills/unreal/unreal-gas-cpp/`（+ references）
- `skills/workflow/gamestudio/`（+ references / NOTICE）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| Extreme11111/unrealsharp-syntax-skill | 仍停 06:31Z；★1 | https://github.com/Extreme11111/unrealsharp-syntax-skill | 继续引入（已入库） |
| kevinpbuckley / VibeUE / db-lyon | 仍为 08-04 | 各原仓 | 继续引入 |
| frabcd/codex-ai-game-studio | pushed_at 仍指向 08-05 元数据；最近实质 commit 08-02 | https://github.com/frabcd/codex-ai-game-studio | 仍观望 |
| fenggezaici/dcc-python-skills | 仍停 06:53Z；无 SPDX | https://github.com/fenggezaici/dcc-python-skills | 继续引入（已入库） |
| hkuds/cli-anything | ★46644（+5）；无新方向 skill | https://github.com/hkuds/cli-anything | 仍观望 |

### 累计建议引入（仍有效）

1–37. 维持上轮清单（含 gamedev-skills、kevinpbuckley、Epic、Italink UCP、maystudios best-practices/PCG、UnrealSharp、GDD 等）  
38. **+ 本轮** https://github.com/toamig/claude-unreal-skills（三件套）  
39. **+ 本轮** https://github.com/GuangminJu/UnrealSkills（ue-build + ue-test）  
40. **+ 本轮** https://github.com/guangyuspace/codex-gamestudio-skill  
41. **+ 本轮晋级** maystudios `unreal-gas` → 精选为 `unreal-gas-cpp`

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| TomLeeLive/openclaw-unreal-skill | UE·工作流 | OpenClaw 插件远程驱 UE（关卡/Actor/PIE/截图） | https://github.com/TomLeeLive/openclaw-unreal-skill | 5★ Apache-2.0；强依赖自有插件；与 UCP/ue-mcp 同类 | 观望 |
| gisenberg/unreal-skills | UE·工作流 | AngelScript / Perforce / PIE 验证 / 编辑器自动化 | https://github.com/gisenberg/unreal-skills | 0★ 无 SPDX；AngelScript+P4  niche 可下轮精选 | 观望 |
| sipherxyz/universal-ue-skills | UE | RenderDoc/内存泄漏/XR/复制审查等专项 | https://github.com/sipherxyz/universal-ue-skills | 1★ 无 SPDX；专项质量尚可，需抽样+许可 | 观望 |
| NoxDevelopment/unrealgen | UE·游戏设计 | UE 编排器 + primers（GAS/复制/UMG…） | https://github.com/NoxDevelopment/unrealgen | 0★ MIT；与 toamig/maystudios 重叠 | 观望 |
| petascale4/UnrealSkills | UE·工作流 | 经 UAssetAPI 离线读写 uasset | https://github.com/petascale4/UnrealSkills | 0★ 无 SPDX；资产管线独特 | 观望 |
| miramocha/blender-skills-and-rules | 3D | VRoid/VRM/ARKit 清理与骨骼重映射 | https://github.com/miramocha/blender-skills-and-rules | 0★ 无 SPDX；08-04 有推送；虚拟形象向 | 观望 |
| lpf513/gameSkills | 游戏设计 | 11 个策划/数值/关卡/叙事 skill | https://github.com/lpf513/gameSkills | 1★ 无 SPDX；与已有策划库重叠 | 观望 |
| githuBlijingai/story-to-game-skill | 游戏设计 | 小说→玩家动词/核心循环原型 | https://github.com/githuBlijingai/story-to-game-skill | 2★ Apache-2.0；与已引入 novel-to-game 重叠 | 观望 |
| opengameapp/OpenGame-skills | 2D·工作流 | 浏览器游戏构建 + OpenGame 发布 | https://github.com/opengameapp/OpenGame-skills | 0★ MIT-0；偏 Web 发布平台 | 观望 |
| fairypark / oliver-io / Italink 其余领域 | UE·工作流 | MCP/Harness/UCP modeling·niagara | 各原仓 | 维持上轮观望；UCP 入口已引入 | 观望 |
| maystudios unreal-blueprint-codegen / thirdparty | UE | BP 代码生成、第三方库链接 | https://github.com/maystudios/claude-skills | GAS 已晋级；其余按需 | 观望 |

其余观望（w-zhian 剩余 3、TerminalSkills、Randroids-Dojo、hkuds/cli-anything、flue、omer-metin 其余、freshtechbro 其余、xingtongovo、cowork-os、pluginagentmarketplace game-design-theory、opusgamelabs 等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 仍仅 08-03 star chore；mouadja02 近提交仍为 Qdrant / Terraform / K8s（无关）  
- `created:>=2026-08-05` 今日新建噪声 **≥100**（Copilot 练习、简历、SEO、标书格式、Go 风格指南等）  
- 今日新建含 “Unreal/Blender” 字样但无 SKILL.md：UnrealBattleTest、BlenderNote、Runtime-Gizmo 等  
- j4flmao/agent-skills：code hit 实为 cocos2d/ecs，非 UE；paxlabs/matrix-core、junainfinity/VibeStudio：通用 agent，非游戏向  
- modbender / majiayu000 巨型镜像注册表：不入库  

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 08-04：Qdrant / Terraform（无关）；无游戏/UE/设计向 |

## 本仓入库变化（+7 → 100）

- 新增 `skills/unreal/unreal-replication/`  
- 新增 `skills/unreal/unreal-design-patterns/`  
- 新增 `skills/unreal/unreal-solid/`  
- 新增 `skills/unreal/ue-build/`  
- 新增 `skills/unreal/ue-test/`  
- 新增 `skills/unreal/unreal-gas-cpp/`  
- 新增 `skills/workflow/gamestudio/`  
- 各含 `SOURCE.md`；承接上轮 93 条精选内容  

## 今天可行动

1. **多人先过 replication 门禁**：做任何「看起来像单机但要上联机」的功能前，先跑 `unreal-replication` 的状态归属表（GameState/PlayerState/PC），再写代码。  
2. **C++ 改完即编**：把 `ue-build`（+ 可选 `ue-test`）装进 Cursor skills，验证 `detect_ue.py` 能否找到你的引擎路径；失败再裁成个人 `/ue-build-local`。  
3. **个人 skill 候选**：若主力是 GAS 联机，把 `unreal-gas-cpp` 的 prediction/replication 章节与 `unreal-replication` 合并成一份个人 `/ue-mp-gas`；或把 `gamestudio` 的 `CODEX_HANDOFF.md` 模板改成 UE 项目交接卡。

## 已尝试查询

1. 种子仓 commits / meta API（JackyST0、mouadja02）  
2. 跟踪仓 `pushed_at`（kevinpbuckley、VibeUE、db-lyon、Italink、maystudios、Extreme11111、fairypark、oliver-io、frabcd、flue、hkuds、w-zhian、dcc-python、UE-AgentFramework、Randroids、TerminalSkills 等）  
3. `gh search repos`：`unreal skill`；`skill created:>=2026-08-05`；`game skill` / `blender skill`；关键词 unreal/blender/gamedev/game-design/niagara/umg created≥08-05  
4. `gh search code`：`Unreal filename:SKILL.md`（间歇 429，成功时见 toamig/maystudios/sipherxyz/NoxDevelopment/…）；`path:.cursor/skills` / `.agents/skills` → **HTTP 429**  
5. skills.sh/api/search：unreal、gamedev、blender、game ui、game design、houdini、niagara、3d modeling、sequencer、umg  
6. 候选 raw `SKILL.md` + git clone 抽样入库；CursorSkill 入库 / push / PR  
