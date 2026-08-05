# 技能侦察 DIGEST — 2026-08-05（11:00Z）

- 侦察时间：2026-08-05T11:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T10:00Z（同日上一轮，PR#10）
- 本仓入库：精选 **116** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-05-11`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill（mouadja02 今日新增 SBOM/身份匹配属 DevOps，记数忽略）。跟踪仓无新 push。本轮以**缺口补齐 + 观望晋级**为主：① [quodsoler](https://github.com/quodsoler/unreal-engine-skills)（301★ MIT）补 Audio / SaveGame / World Partition·Streaming / AI Navigation；② [w-zhian/qa-review](https://github.com/w-zhian/game-design-skills) 从观望晋级；③ [gamedev-skills game-ai](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) 跨引擎 AI 纪律；④ [abagames](https://github.com/abagames/agentic-gamedev-skills) 平衡评估与玩法不变量（与已入库 mini-game 设计互补）。新发现 Angelscript / omer-metin UI / teixasalone 等入观望。今日 `skill` 新建噪声仍高；`path:.cursor/skills` 易 429。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| ue-audio-system | UE | SoundCue / MetaSound / 衰减 / Submix / 并发 | https://github.com/quodsoler/unreal-engine-skills | 301★ MIT；本仓无独立 UE 音频 skill；含 patterns | **引入** |
| ue-serialization-savegames | UE | USaveGame / FArchive / 多槽 / 版本化存档 | https://github.com/quodsoler/unreal-engine-skills | 补齐进度持久化缺口；含 architecture 参考 | **引入** |
| ue-world-level-streaming | UE | World Partition / Data Layer / Seamless Travel / HLOD | https://github.com/quodsoler/unreal-engine-skills | 开放世界与关卡流送核心路径 | **引入** |
| ue-ai-navigation | UE·游戏设计 | AIController / NavMesh / EQS / Perception（衔接 BT/StateTree） | https://github.com/quodsoler/unreal-engine-skills | 与上轮 BT/StateTree 形成 AI 闭环；含 EQS 参考 | **引入** |
| qa-review | 游戏设计·工作流 | 设计文档 / 数值 / 系统验收清单 | https://github.com/w-zhian/game-design-skills | 观望晋级；清单清晰可执行；无 SPDX（与系列一致） | **引入** |
| gamedev-game-ai | 游戏设计 | 跨引擎 AI：感知、决策、寻路、群体（非引擎 API） | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 413★ Apache-2.0；skills.sh 高安装；补策划层 AI | **引入** |
| evaluating-gameplay-balance | 游戏设计 | 用单调/探索策略对比评测手感与平衡 | https://github.com/abagames/agentic-gamedev-skills | MIT；可测协议清晰；补「设计→验证」 | **引入** |
| implementing-gameplay-invariants | 游戏设计 | 把设计意图落成引擎无关的玩法不变量与校验 | https://github.com/abagames/agentic-gamedev-skills | 与已入库 mini-game / 本轮 balance 成套 | **引入** |

本仓已摘录：

- `skills/unreal/ue-audio-system/`（+ references）
- `skills/unreal/ue-serialization-savegames/`（+ references）
- `skills/unreal/ue-world-level-streaming/`（+ references）
- `skills/unreal/ue-ai-navigation/`（+ references）
- `skills/game-design/qa-review/`（+ references）
- `skills/game-design/gamedev-game-ai/`（+ references）
- `skills/game-design/evaluating-gameplay-balance/`（+ references）
- `skills/game-design/implementing-gameplay-invariants/`

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 11:00Z 前新增 SBOM identity matching（#40） | https://github.com/mouadja02/skills | **忽略**（DevOps，方向无关） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| kevinpbuckley | 仍为 08-04 5.8 retarget；其余 core（audio/save/levels…）未再入 | https://github.com/kevinpbuckley/unreal-engine-skills | 无 SPDX；本轮优先 MIT 的 quodsoler 同主题 |
| sipherxyz / miramocha / Italink 子包 | 无新 push | 各原仓 | 维持观望 |

### 累计建议引入（仍有效）

1–45. 维持至上轮（含 Mover / BT / Input / Packaging / Mass / StateTree / Sequencer / Modeling 等）  
46. **+ 本轮** quodsoler：audio / savegames / world-streaming / ai-navigation  
47. **+ 本轮晋级** w-zhian `qa-review`  
48. **+ 本轮** gamedev-skills `game-ai`  
49. **+ 本轮** abagames：evaluating-gameplay-balance / implementing-gameplay-invariants

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| flashpoint493/unreal-angelscript | UE | Hazelight UE-AS：语法/网络/GAS/CommonUI + 10 份 references | https://github.com/flashpoint493/unreal-angelscript-skills | 30★；许可 NOASSERTION；仅 AS 栈需要 | 观望 |
| omer-metin game-ui-design / game-design-core / unreal-engine | UI·游戏设计·UE | 高安装通用设计/UE 入口 skill | https://github.com/omer-metin/skills-for-antigravity | 123★ Apache-2.0；偏 persona，与已有 UI/UE 精选重叠 | 观望 |
| teixasalone/UnrealEngine5-Skills | UE | 5.6/5.7 BP/C++/UI/PCG/复制工作流 | https://github.com/teixasalone/UnrealEngine5-Skills | 16★ MIT；目录结构与 UnrealXu 高度同构 | 观望 |
| liuhuagang / mrSutivu UE C++ Expert | UE | 大型 C++/课程式 skill 包 | 各原仓 | 60★/56★；无 LICENSE | 观望 |
| TerminalSkills / Randroids-Dojo unreal | UE | 通用 skill 库中的 UE 条目 | 各原仓 | Apache/MIT；单文件概览，深度不足 | 观望 |
| ibrews/ue5-mcp | UE·工作流 | MCP + Pixel Streaming + Python 编辑器 | https://github.com/ibrews/ue5-mcp | 32★；无 SPDX；与 Epic MCP/UCP 重叠 | 观望 |
| quodsoler 其余（physics / networking / game-features / niagara-effects…） | UE | 27 skills 中未精选部分 | https://github.com/quodsoler/unreal-engine-skills | 本轮已再收 4 个；其余按需 | 观望 |
| gamedev-skills camera / save / audio / physics / shader 纪律 | 游戏设计 | 跨引擎纪律包剩余项 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 高安装；本轮已收 game-ai | 观望 |
| abagames 其余（最大化 game-feel / 音频 / Godot 脚手架…） | 游戏设计·工作流 | agentic gamedev 研究向 | https://github.com/abagames/agentic-gamedev-skills | 10★ MIT；08-02 有推送 | 观望 |
| w-zhian article-curation / skill-evolution | 工作流 | 文章蒸馏 / 技能自演化 | https://github.com/w-zhian/game-design-skills | qa-review 已晋级；其余仍观望 | 观望 |
| sipherxyz / gisenberg / Italink niagara-editing+modeling-* / OpenClaw / UAssetAPI / flue / cesiumjs / alterlab_gameforge | UE·3D·工作流 | 维持上轮观望理由 | 各原仓 | 许可或重叠未变 | 观望 |

其余观望（lpf513、story-to-game、OpenGame、miramocha、fairypark/oliver-io、hkuds、pluginagentmarketplace、opusgamelabs、cowork-os、NAJEMWEHBE/UnrealMCPHub 等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 **SBOM identity matching**（方向无关，+1 无关）
- 今日新建：`mossly/flights-skill`、`raymatos/skills-mcp` 等（无关）
- code search 噪声：majiayu000 巨型镜像、modbender、j4flmao、paxlabs、VibeStudio、作业/作品展示仓
- alvinunreal/oh-my-opencode-slim：通用 agent 套件

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | **08-05 10:11Z**：SBOM identity matching（无关）；此前 Qdrant/Terraform/K8s |

## 本仓入库变化（+8 → 116）

- 新增 `skills/unreal/ue-audio-system/`
- 新增 `skills/unreal/ue-serialization-savegames/`
- 新增 `skills/unreal/ue-world-level-streaming/`
- 新增 `skills/unreal/ue-ai-navigation/`
- 新增 `skills/game-design/qa-review/`
- 新增 `skills/game-design/gamedev-game-ai/`
- 新增 `skills/game-design/evaluating-gameplay-balance/`
- 新增 `skills/game-design/implementing-gameplay-invariants/`
- 各含 `SOURCE.md`；承接上轮 108 条精选内容

## 今天可行动

1. **装 UE 基建四件套（MIT）**：`ue-audio-system` + `ue-serialization-savegames` + `ue-world-level-streaming` + `ue-ai-navigation`，与上轮 BT/StateTree/Mover 拼成「AI + 世界 + 音频 + 存档」日常包。  
2. **试策划验收闭环**：对一份现有 GDD/数值表跑一遍 `qa-review`，再用 `evaluating-gameplay-balance` 定 1 个可测对比协议。  
3. **个人 skill 候选**：若做开放世界 AI，把 `ue-ai-navigation` + 已有 `unreal-behavior-trees`/`ue-state-trees` 合成个人 `/ue-npc-ai`；若做原型验证，把 abagames 的 balance + invariants 合成 `/gameplay-validate`。

## 已尝试查询

1. 种子仓 commits / meta API（JackyST0、mouadja02）  
2. 跟踪仓 `pushed_at` / trees（kevinpbuckley、quodsoler、gamedev-skills、w-zhian、sipherxyz、Italink、gisenberg、cesiumjs、flue、alterlab、Epic plugin、microsoft/Resource2Skill 等）  
3. `gh search repos`：`skill` created≥08-05；`unreal skill` updated≥07-29；gamedev/blender/houdini/umg 关键词  
4. `gh search code`：`Unreal filename:SKILL.md`（成功）；`game design filename:SKILL.md` 一度 429  
5. skills.sh/api/search：unreal、gamedev、blender、game design、niagara、umg、houdini、3d modeling、sequencer、state tree、mover、angelscript  
6. 候选 raw/blob `SKILL.md` + 入库 / push / PR  
