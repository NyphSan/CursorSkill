# 技能侦察 DIGEST — 2026-08-05（17:00Z）

- 侦察时间：2026-08-05T17:48Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T16:00Z（同日上一轮，PR#16）
- 本仓入库：精选 **164** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-05-17`

## 本轮结论（一屏）

距上轮约 1.5 小时。种子仓仍无方向相关新 skill（JackyST0 停在 08-03；mouadja02 仍为 10:11Z SBOM）。索引仓 [linny006/awesome-agent-skills](https://github.com/linny006/awesome-agent-skills) 高频 churn（17:45Z +21/−21），非可安装 skill 包。按「下次优先」继续从 [omer-metin/skills-for-antigravity](https://github.com/omer-metin/skills-for-antigravity)（123★ Apache-2.0）引入卡牌/桌游/角色/AI 美术/像素/解谜/着色，并自 [abagames/agentic-gamedev-skills](https://github.com/abagames/agentic-gamedev-skills)（10★ MIT）引入 `directing-game-visuals`。JetBrains Rider UE 三件套确认依赖 Rider MCP → 维持观望；Flue/kevin 许可/sipher 仍观望。code search 仍 429。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| omer-card-game-design | 游戏设计 | TCG/CCG 资源曲线、关键词、系列与 meta 平衡 | https://github.com/omer-metin/skills-for-antigravity | 与 genre-card-game 互补：偏设计理论层 | **引入** |
| omer-board-game-design | 游戏设计 | 桌游机制/试玩/规则书到 Kickstarter·量产 | https://github.com/omer-metin/skills-for-antigravity | 填补桌面/实体游戏空白 | **引入** |
| omer-character-design | 2D·游戏设计 | 剪影/形状语言/表情转面与可读角色设计 | https://github.com/omer-metin/skills-for-antigravity | 角色美术原则层；含 references | **引入** |
| omer-ai-game-art-generation | 2D·工作流 | ComfyUI/SD/FLUX 游戏资产一致性管线 | https://github.com/omer-metin/skills-for-antigravity | AI 美术生产向；许可与一致性提醒 | **引入** |
| omer-pixel-art-sprites | 2D | 像素角色/图块/调色板与精灵动画 | https://github.com/omer-metin/skills-for-antigravity | 补齐 2D 像素生产层 | **引入** |
| omer-puzzle-design | 游戏设计 | aha 时刻、教学曲线、提示与可解性 | https://github.com/omer-metin/skills-for-antigravity | 与 genre-puzzle 互补：偏设计哲学 | **引入** |
| omer-shader-programming | 3D·UE | 跨 GLSL/HLSL/compute 的实时着色原则 | https://github.com/omer-metin/skills-for-antigravity | 与 gamedev-shader / hlsl-shader 互补 | **引入** |
| directing-game-visuals | 游戏设计·2D | 视觉层级、调色板角色、无 HUD 可读反馈 | https://github.com/abagames/agentic-gamedev-skills | MIT；反「AI 味」视觉；可执行工作流 | **引入** |

本仓已摘录：

- `skills/game-design/omer-card-game-design/`（+ references）
- `skills/game-design/omer-board-game-design/`（+ references）
- `skills/2d/omer-character-design/`（+ references）
- `skills/2d/omer-ai-game-art-generation/`（+ references）
- `skills/2d/omer-pixel-art-sprites/`（+ references）
- `skills/game-design/omer-puzzle-design/`（+ references）
- `skills/3d/omer-shader-programming/`（+ references）
- `skills/game-design/directing-game-visuals/`（+ references）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 10:11Z SBOM；无更新 | https://github.com/mouadja02/skills | **忽略**（DevOps） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| linny006/awesome-agent-skills | 17:45Z 索引 churn +21/−21 | https://github.com/linny006/awesome-agent-skills | **忽略**（索引仓） |
| adobe/skills | 14:25 仍为 code-assessment GA；`ue-component-model` 非虚幻 | https://github.com/adobe/skills | **忽略**（AEM） |
| kevinpbuckley | 仍无 SPDX | https://github.com/kevinpbuckley/unreal-engine-skills | 维持观望 |
| sipherxyz | 仍无 LICENSE | https://github.com/sipherxyz/universal-ue-skills | 维持观望 |
| JetBrains/rider-skills | 确认 master；UE 三件套强依赖 Rider MCP | https://github.com/JetBrains/rider-skills | 维持观望 |
| SFKislev/Flue | Blender/Houdini bridge；硬编码本机路径 | https://github.com/SFKislev/Flue | 维持观望 |
| tzwkb/lqe-translator | 今日新建；游戏本地化 LQE（0★） | https://github.com/tzwkb/lqe-translator | **观望**（新仓） |

### 累计建议引入（仍有效）

1–60. 维持至上轮（含 gamedev genres 全套、omer 第一批 core/ui/vfx/3d-modeling 等）  
61. **+ 本轮** omer 第二批：card / board / character / ai-game-art / pixel-art / puzzle / shader  
62. **+ 本轮** abagames `directing-game-visuals`

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| JetBrains/rider-skills（ue-code-authoring / ue-live-debugging / ue-test-authoring） | UE·工作流 | Rider MCP 驱动的 UE C++ 编写/调试/自动化测试 | https://github.com/JetBrains/rider-skills | 11★ Apache-2.0；无 Rider MCP 则降级 | 观望 |
| SFKislev/Flue（blender / houdini） | 3D·工作流 | shell→bpy/hou 桥，非 MCP | https://github.com/SFKislev/Flue | 安装量大但依赖本机 Flue + 路径 | 观望 |
| tzwkb/lqe-translator | 工作流·本地化 | ZH→EN/TH 游戏翻译 LQE 打分管线 | https://github.com/tzwkb/lqe-translator | 今日新建 0★；脚本齐全可再评 | 观望 |
| omer-metin 其余（level-design / narrative / unreal-engine / lore…） | 游戏设计·UE | 大型库剩余子集 | https://github.com/omer-metin/skills-for-antigravity | 本轮已抽七条；其余按题材再取 | 观望 |
| abagames 其余（arcadifying / retro-concepts / turn-based verify…） | 游戏设计 | 街机/回合验证工作流 | https://github.com/abagames/agentic-gamedev-skills | 本轮已抽视觉；其余按需 | 观望 |
| quodsoler 重叠项（ue-input / umg / procgen / gas） | UE | 与已有 Enhanced Input / UMG / Procgen / GAS 重叠 | https://github.com/quodsoler/unreal-engine-skills | 核心缺口已收完 | 观望 |
| a5c-ai/babysitter unreal-chaos / lumen / nanite… | UE·游戏 | 巨型库内 UE 薄层 specialization | https://github.com/a5c-ai/babysitter | 能力清单薄层；暂不整包 | 观望 |
| kevinpbuckley UDS/UDW / gameplay-tags / landscape | UE | 无 SPDX；天气/天空包独特 | https://github.com/kevinpbuckley/unreal-engine-skills | 许可未变 | 观望 |
| CesiumGS / sipherxyz | 3D·工作流·UE | 维持上轮观望理由 | 各原仓 | 许可或场景未变 | 观望 |

其余观望（teixasalone、TerminalSkills、ibrews、lpf513、story-to-game、OpenGame、pluginagentmarketplace、opusgamelabs、Stanestane bundle、linny006 索引仓等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 **SBOM identity matching**（方向无关，记数）
- `linny006/awesome-agent-skills`：索引 churn，非可安装 skill 包
- `adobe/skills` 的 `ue-component-model`：**非 Unreal**（AEM Universal Editor）
- 今日新建噪声：`PiNocPie/claude-skill-builder`、`ecoma-io/litmus`、`Heybinshao/path-simulation-skill`、简历/portfolio 类等（方向无关，记数）
- repos search `unreal skills` / `game design skill SKILL.md` updated≥07-29：无新方向仓
- code search：`filename:SKILL.md UnrealEngine` / `path:.agents/skills Unreal` → HTTP 429
- chris58530/gamedev-skills：0★；树中未见可用 `SKILL.md` 结构

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| JackyST0/awesome-agent-skills | 613 | 仍仅 08-03 star chore；无 UE/游戏专区新增 |
| mouadja02/skills | 9 | 仍为 08-05 10:11Z SBOM；方向无关 |

## 今天可行动

1. **试装** `skills/game-design/directing-game-visuals/`：给现有原型写一版 `VISUAL_DESIGN.md`（角色/危险/奖励三可读）。
2. **试装** `skills/2d/omer-pixel-art-sprites/` 或 `omer-ai-game-art-generation/`：按你的 2D/AI 美术管线二选一落地。
3. **个人 skill**：若你做 TCG/桌游，把 `omer-card-game-design` / `omer-board-game-design` 裁成「只保留你项目约束」的短版；Rider 用户再评估 JetBrains UE 三件套。

## 已尝试查询

1. 种子仓 commits / repo meta API
2. 跟踪仓 pushed_at / trees / license（kevin、quodsoler、gamedev-skills、sipherxyz、babysitter、hao-skills、cesiumjs、Flue、omer-metin、JetBrains/rider-skills、adobe、abagames、linny006 等）
3. repos search：skill created:>=2026-08-05；unreal/gamedev/game design skills；`agent skills` game updated≥08-01
4. code search：UnrealEngine filename:SKILL.md；path:.agents/skills Unreal → 429
5. skills.sh/api/search：unreal, gamedev, game design, blender, umg, niagara, houdini, cesium, card-game-design, board-game-design, character-design, ai-game-art, ue-angelscript, lumen, nanite, rider, unreal-chaos
6. 候选 blob SKILL.md + 入库 + push + open_git_pr + Slack
