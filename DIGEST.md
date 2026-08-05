# 技能侦察 DIGEST — 2026-08-05（18:00Z）

- 侦察时间：2026-08-05T18:10Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T17:48Z（同日上一轮，PR#17）
- 本仓入库：精选 **172** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-05-18`

## 本轮结论（一屏）

距上轮约 20 分钟。种子仓 [mouadja02/skills](https://github.com/mouadja02/skills) 有新推送（18:06Z `idea-refine` 可移植性修复），但属通用 coding，方向无关；JackyST0 仍停在 08-03 star chore。跟踪仓无新实质 push。本轮按「下次优先」继续缺口补齐：① [omer-metin/skills-for-antigravity](https://github.com/omer-metin/skills-for-antigravity)（123★ Apache-2.0）补 level / narrative / lore / unreal-engine；② [abagames/agentic-gamedev-skills](https://github.com/abagames/agentic-gamedev-skills)（10★ MIT）补街机化 / 复古街机概念批量生成 / 回合制验证；③ 新发现 [apetrovCode/game-design-skills](https://github.com/apetrovCode/game-design-skills)（1★ MIT）含可执行 `matrix_analysis.py` 的游戏系统分析 skill。AngelScript（gisenberg，无 LICENSE）与 Rider UE MCP 仍观望。code search 仍偶发 429。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| omer-level-design | 游戏设计 | blockout / 玩家流 / weenie / 环境叙事与热图迭代 | https://github.com/omer-metin/skills-for-antigravity | Apache-2.0；含 patterns/sharp_edges/validations；与已有 level-design 互补加深 | **引入** |
| omer-narrative-design | 游戏设计 | 分支叙事 / bark / 环境叙事 / ludonarrative 和谐 | https://github.com/omer-metin/skills-for-antigravity | 完整参考三件套；补叙事脚手架层 | **引入** |
| omer-lore-building | 游戏设计 | 世界观深度、ARG、可发现式 lore 与一致性管理 | https://github.com/omer-metin/skills-for-antigravity | 与 narrative 分工：lore 偏宇宙层 | **引入** |
| omer-unreal-engine | UE | UE5 总览：Gameplay Framework / BP↔C++ / GAS·复制入门 | https://github.com/omer-metin/skills-for-antigravity | 作为「总控路由」；与已有专项 skill 拼成入口 | **引入** |
| arcadifying-mini-games | 游戏设计 | 给已验证核心循环加局结构 / 仪式屏 / 分数经济 / 高分榜 | https://github.com/abagames/agentic-gamedev-skills | MIT；可执行 arcade 完成度清单 | **引入** |
| generating-retro-arcade-concepts | 游戏设计 | 批量生成并评估 78–83 风固定屏街机概念 slate | https://github.com/abagames/agentic-gamedev-skills | 硬约束清晰；适合原型选题 | **引入** |
| verifying-turn-based-games | 游戏设计 | 双人交替回合引擎契约 + bot ladder / 张力指标 | https://github.com/abagames/agentic-gamedev-skills | 与 omer-board/card 形成「设计→验证」闭环 | **引入** |
| game-analysis | 游戏设计 | 8 步系统拆解：交互矩阵、趣味引擎、杠杆诊断（含脚本） | https://github.com/apetrovCode/game-design-skills | MIT；有 `matrix_analysis.py` 与报告模板，可落地审计 | **引入** |

本仓已摘录：

- `skills/game-design/omer-level-design/`（+ references）
- `skills/game-design/omer-narrative-design/`（+ references）
- `skills/game-design/omer-lore-building/`（+ references）
- `skills/unreal/omer-unreal-engine/`（+ references）
- `skills/game-design/arcadifying-mini-games/`（+ references）
- `skills/game-design/generating-retro-arcade-concepts/`（+ references）
- `skills/game-design/verifying-turn-based-games/`
- `skills/game-design/game-analysis/`（+ references + scripts）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | **18:06Z** `idea-refine` 可移植性修复（#41） | https://github.com/mouadja02/skills | **忽略**（通用 coding） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| linny006/awesome-agent-skills | 18:00Z 索引 churn +23/−23 | https://github.com/linny006/awesome-agent-skills | **忽略**（索引仓） |
| kevinpbuckley | 仍无 SPDX | https://github.com/kevinpbuckley/unreal-engine-skills | 维持观望 |
| sipherxyz | 仍无 LICENSE | https://github.com/sipherxyz/universal-ue-skills | 维持观望 |
| JetBrains/rider-skills | 无新推送；仍依赖 Rider MCP | https://github.com/JetBrains/rider-skills | 维持观望 |
| SFKislev/Flue | 无新推送；硬编码本机路径 | https://github.com/SFKislev/Flue | 维持观望 |
| tzwkb/lqe-translator | 仍为今日新建 0★ | https://github.com/tzwkb/lqe-translator | 维持观望 |
| gisenberg/unreal-skills | 含 `ue5-angelscript` 等；**无 LICENSE** | https://github.com/gisenberg/unreal-skills | **观望**（许可缺口） |

### 累计建议引入（仍有效）

1–62. 维持至上轮（含 omer 卡牌/桌游/像素等与 directing-game-visuals）  
63. **+ 本轮** omer：level-design / narrative-design / lore-building / unreal-engine  
64. **+ 本轮** abagames：arcadifying / generating-retro-arcade-concepts / verifying-turn-based-games  
65. **+ 本轮** apetrovCode：game-analysis

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| apetrovCode/game-redesign | 游戏设计 | 基于 audit 提出理论检验后的大胆再设计方案 | https://github.com/apetrovCode/game-design-skills | MIT；依赖 game-analysis 已装路径；本轮先收分析侧 | 观望 |
| gisenberg/unreal-skills（ue5-angelscript / build / PIE…） | UE | Hazelight 风格 AngelScript 游戏层 | https://github.com/gisenberg/unreal-skills | 填补 Angelscript 缺口但无 LICENSE；0★ | 观望 |
| abagames 其余（era-authentic-audio / web typography / crisp-game-lib…） | 游戏设计·2D | 复古音频 / 字体分发 / Godot·web 小游戏栈 | https://github.com/abagames/agentic-gamedev-skills | 本轮已抽街机三件套；其余按项目栈再取 | 观望 |
| omer concept-art / environment-art / texture-art / voxel… | 2D·3D | 美术向剩余子集 | https://github.com/omer-metin/skills-for-antigravity | 关卡/叙事/UE 总览已抽；美术按需 | 观望 |
| ConnorGriffin/skills ui-craft | UI·工作流 | 锁定视觉规格→构建→审计的 UI 生命周期 | https://github.com/ConnorGriffin/skills | 17★；偏 Web 产品 UI，游戏 UI 重叠有限；许可 NOASSERTION | 观望 |
| JetBrains/rider-skills UE 三件套 | UE·工作流 | Rider MCP 编写/调试/测试 | https://github.com/JetBrains/rider-skills | 无 Rider MCP 则降级 | 观望 |
| SFKislev/Flue / kevin / sipher / babysitter / cesiumjs / lqe-translator | 3D·UE·本地化 | 维持上轮观望理由 | 各原仓 | 许可或依赖未变 | 观望 |
| Stanestane/game-design-skills-bundle | 游戏设计 | 大量 audit/persona 技能包 | https://github.com/Stanestane/game-design-skills-bundle | 40★；无 SPDX LICENSE | 观望 |
| SherryCW/shigeru-miyamoto | 游戏设计 | 宫本茂视角玩法评审 persona | https://github.com/SherryCW/shigeru-miyamoto | 有完整 SKILL.md；0★ 无 LICENSE | 观望 |

其余观望（teixasalone、TerminalSkills、ibrews、lpf513、story-to-game、OpenGame、pluginagentmarketplace、opusgamelabs、quodsoler 重叠项等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 **idea-refine**（通用想法精炼，方向无关，记数）
- `linny006/awesome-agent-skills`：索引 churn，非可安装 skill 包
- 今日新建噪声：GitHub Skills 练习仓、简历/portfolio、`path-simulation`、`musk-perspective`、`weekly-status-updates`、Django teacher 等（方向无关，记数）
- `adobe/skills` 的 `ue-component-model`：**非 Unreal**（AEM Universal Editor）
- code search：`filename:SKILL.md UnrealEngine` / `path:.agents/skills Unreal` → 偶发 429（已用 skills.sh + trees + raw 补）

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 仍仅 08-03 star chore；无 UE/游戏专区新增 |
| https://github.com/mouadja02/skills | 9 | **08-05 18:06Z**：idea-refine portable setup（无关）；此前 10:11Z SBOM |

## 本仓入库变化（+8 → 172）

- 新增 `skills/game-design/omer-level-design/`
- 新增 `skills/game-design/omer-narrative-design/`
- 新增 `skills/game-design/omer-lore-building/`
- 新增 `skills/unreal/omer-unreal-engine/`
- 新增 `skills/game-design/arcadifying-mini-games/`
- 新增 `skills/game-design/generating-retro-arcade-concepts/`
- 新增 `skills/game-design/verifying-turn-based-games/`
- 新增 `skills/game-design/game-analysis/`
- 各含 `SOURCE.md`；承接上轮 164 条精选内容

## 今天可行动

1. **装叙事三件套**：`omer-narrative-design` + `omer-lore-building` + 已有 `gamedev-dialogue-systems`，先写一版分支对话与 lore 发现路径。  
2. **试街机闭环**：用 `generating-retro-arcade-concepts` 出 5 个概念 slate → 选 1 个用已有 `designing-mini-games` 硬化 → 再用 `arcadifying-mini-games` 加局结构/高分榜。  
3. **个人 skill 候选**：把 `omer-unreal-engine`（总览）裁成指向本仓已有专项（CMC / GAS / UMG / Niagara）的 `/ue-router`；若做桌游/卡牌，试装 `verifying-turn-based-games` + `game-analysis` 做可度量验证。

## 已尝试查询

1. 种子仓 commits / meta API（JackyST0、mouadja02；发现 idea-refine #41）  
2. 跟踪仓 `pushed_at` / trees / license（kevin、quodsoler、gamedev-skills、sipherxyz、babysitter、Flue、omer-metin、JetBrains/rider-skills、adobe、abagames、linny006、tzwkb、gisenberg、apetrovCode、ConnorGriffin、Stanestane、SherryCW 等）  
3. `gh search repos`：`skill` created≥08-05；`unreal skills`；`gamedev skills`；`game design skills`；`agent skills` updated≥08-01  
4. `gh search code`：`Unreal filename:SKILL.md` / `path:.agents/skills Unreal`（429）；`directing-game-visuals filename:SKILL.md`（成功）  
5. skills.sh/api/search：unreal、gamedev、game design、blender、umg、niagara、houdini、ui design、level design、narrative、state tree、angelscript、sequencer、game feel、pixel art、arcadifying、retro-concepts、verifying-turn-based  
6. 候选 raw/blob `SKILL.md` + 入库 / push / PR  
