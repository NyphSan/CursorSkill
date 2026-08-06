# 技能侦察 DIGEST — 2026-08-06（01:00Z）

- 侦察时间：2026-08-06T01:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-06T00:00Z（同日上一轮，PR#23）
- 本仓入库：精选 **220** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-06-01`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。跟踪仓：lisxa5747 **00:06Z** 再改 README（无 LICENSE，维持降级）；Yuki001 50★ 仍无 LICENSE；ConnorGriffin / Flue / kevin / sipher 无实质变化。本轮按「下次优先」升级引入 donchitos：**ux-review / team-combat / vertical-slice / prototype**；omer：**game-monetization / gamification-loops / easter-egg-design / unreal-llm-integration**。新噪声仓：`Oliyflemishspeaking560/threejs-game-skills`（今日 push，0★，疑似 majid 镜像）、`opengameapp/OpenGame-skills`（MIT-0，生态绑定）、`0xheycat/isometric-game-skills`（MIT 6★，下次可摘）记入观望。GitHub code search 本轮 429；repos + skills.sh + 树/blob API 已覆盖。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| donchitos-ux-review | UI·工作流 | UX 规格门禁：完整性/无障碍/GDD 对齐 → APPROVED 等裁决 | https://github.com/donchitos/claude-code-game-studios | 23631★ MIT；接上轮 ux-design / team-ui | **引入** |
| donchitos-team-combat | 游戏设计·工作流 | 战斗功能端到端团队编排（设计→实现→QA） | 同上 | 与已有 combat-design / balance-check 成流水线 | **引入** |
| donchitos-vertical-slice | 工作流 | 预制作垂直切片，PROCEED/PIVOT/KILL 门禁 | 同上 | 量产前关键验证；工业标准 3–5 分钟切片 | **引入** |
| donchitos-prototype | 工作流 | 概念原型（HTML/Engine/Paper）快速验趣味 | 同上 | 与 vertical-slice 成对：先概念后生产切片 | **引入** |
| omer-game-monetization | 游戏设计 | F2P/IAP/通行证与伦理变现策略 | https://github.com/omer-metin/skills-for-antigravity | 123★ Apache-2.0；补齐商业化缺口 | **引入** |
| omer-gamification-loops | 游戏设计 | 积分/徽章/连胜等参与循环与伦理边界 | 同上 | 接 progression / onboarding | **引入** |
| omer-easter-egg-design | 游戏设计 | 隐藏彩蛋、发现机制与分享触发 | 同上 | 轻量「惊喜」层，易改成项目个人 skill | **引入** |
| omer-unreal-llm-integration | UE·AI | UE 内 LLM NPC：异步、蓝图友好、勿堵 GameThread | 同上 | 接上轮 llm-npc-dialogue 的引擎落地 | **引入** |

本仓已摘录：

- `skills/ui-design/donchitos-ux-review/`
- `skills/workflow/donchitos-team-combat/`
- `skills/workflow/donchitos-vertical-slice/`
- `skills/workflow/donchitos-prototype/`
- `skills/game-design/omer-game-monetization/`（+ references）
- `skills/game-design/omer-gamification-loops/`（+ references）
- `skills/game-design/omer-easter-egg-design/`（+ references）
- `skills/unreal/omer-unreal-llm-integration/`（+ references）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 18:06Z idea-refine；无新 commit | https://github.com/mouadja02/skills | **忽略**（通用 coding） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| ConnorGriffin/skills | 无新于 22:54Z；license NOASSERTION | https://github.com/ConnorGriffin/skills | ui-craft 维持观望 |
| lisxa5747 AngelScript | **00:06Z** 再 Update README；仍 NOASSERTION | https://github.com/lisxa5747/unreal-angelscript-skills | **观望/降级**（优先 osseous） |
| Yuki001/game-dev-skills | 50★（+1）；仍无 LICENSE | https://github.com/Yuki001/game-dev-skills | 维持观望 |
| kevin / sipher / Flue / eve | 无实质变化 | 各原仓 | 维持观望 |
| Oliyflemishspeaking560/threejs-game-skills | **今日 00:08Z** push；0★ MIT；结构似 majid 镜像 | https://github.com/Oliyflemishspeaking560/threejs-game-skills | 观望/低优（已有 majid 摘录） |
| opengameapp/OpenGame-skills | 08-04；MIT-0；浏览器原型+市场发布 | https://github.com/opengameapp/OpenGame-skills | 观望（生态绑定） |
| 0xheycat/isometric-game-skills | MIT 6★；等距美术/渲染技能包 | https://github.com/0xheycat/isometric-game-skills | 观望（下次可摘 art-direction） |

### 累计建议引入（仍有效）

1–80. 维持至上轮（含 donchitos balance/team-ui/playtest/ux-design、omer onboarding/vehicle/mobile/npc）  
81. **+ 本轮** donchitos：ux-review / team-combat / vertical-slice / prototype  
82. **+ 本轮** omer：game-monetization / gamification-loops / easter-egg-design / unreal-llm-integration

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| ConnorGriffin ui-craft | UI·工作流 | 视觉 lock→build→critique→audit | https://github.com/ConnorGriffin/skills | 偏 Web/产品 UI；可改造成游戏 UI | 观望 |
| sfkislev/flue blender | 3D·工作流 | 无 MCP 的 shell→bpy 桌面桥 | https://github.com/sfkislev/flue | 65★ MIT；含本机路径 | 观望 |
| Yuki001/game-dev-skills | 游戏设计·3D·工作流 | architect / toon shader / 资产生成 | https://github.com/Yuki001/game-dev-skills | 50★；**无 LICENSE** | 观望 |
| kevin / sipher / lisxa5747 / eve | 各向 | 维持上轮理由 | 各原仓 | 许可或成熟度未变 | 观望 |
| donchitos team-level / team-narrative / gate-check | 工作流 | 关卡/叙事团队与阶段门禁 | https://github.com/donchitos/claude-code-game-studios | 本轮已收 combat/slice/prototype；下次可续 | 观望 |
| omer-worldbuilding / tabletop-rpg / prompt-to-game | 游戏设计 | 世界观 / TRPG / vibe 原型 | https://github.com/omer-metin/skills-for-antigravity | 本轮优先 monetization/UE-LLM；下次可摘 | 观望 |
| NAJEMWEHBE driving-unreal | UE·工作流 | 经 unreal-ai-connection MCP 驱编 | https://github.com/NAJEMWEHBE/unreal-ai-connection | MIT 9★；强依赖其 MCP | 观望 |
| august-batista unreal-assets | UE | 安全读写 .uasset/.umap | https://github.com/august-batista/claude-unreal-bridge-editor | MIT 0★；强依赖桥 | 观望 |
| 0xheycat/isometric-game-skills | 2D·3D | 等距美术方向与 Canvas/Godot 管线 | https://github.com/0xheycat/isometric-game-skills | MIT 6★；下次可摘 `isometric-art-direction` | 观望 |
| opengameapp/OpenGame-skills | 游戏设计·工作流 | 浏览器原型 + Skill/MCP 发布 | https://github.com/opengameapp/OpenGame-skills | MIT-0 0★；偏 OpenGame 生态 | 观望 |
| w-zhian / avemeva | 游戏/UI | 维持上轮 | 各原仓 | 0★ 无 LICENSE | 观望/低优 |

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 idea-refine（方向无关，记数）
- ConnorGriffin 通用 orchestrate/say-less 增量（非游戏向）
- 今日新建噪声（方向无关，约 15+）：`snailer-team/JeffDean-Mind`、`pubudu538/agent-skills`（Synapse→Go）、`Kazppe/agent-skills`（日文通用工程）、`PeaceFamily000/Robocon`、各类 `skills-github-pages` / `skills-introduction-to-github` 练习仓等
- `Oliyflemishspeaking560/threejs-game-skills`：0★ 疑似镜像，已有 majid 摘录
- eve-skills：EVE Online API
- GitHub code search 本轮 HTTP 429（约需等 12 分钟）；以 repos + skills.sh + 跟踪仓 trees 为准

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 仍为 **08-05 18:06Z** idea-refine portable（无关）；此后无新 commit |

## 本仓入库变化（+8 → 220）

- 新增 `skills/ui-design/donchitos-ux-review/`
- 新增 `skills/workflow/donchitos-team-combat/`
- 新增 `skills/workflow/donchitos-vertical-slice/`
- 新增 `skills/workflow/donchitos-prototype/`
- 新增 `skills/game-design/omer-game-monetization/`
- 新增 `skills/game-design/omer-gamification-loops/`
- 新增 `skills/game-design/omer-easter-egg-design/`
- 新增 `skills/unreal/omer-unreal-llm-integration/`
- 各含 `SOURCE.md`；omer 四项含 `references/`；承接上轮 212 条精选内容

## 今天可行动

1. **UI 门禁闭环**：用已有 `donchitos-ux-design` 写一屏/HUD 规格 → 立刻跑 `donchitos-ux-review` 拿裁决，再进 `donchitos-team-ui`。  
2. **原型→切片**：新点子先 `donchitos-prototype`（概念）→ 定稿后再 `donchitos-vertical-slice`；战斗功能可叠 `donchitos-team-combat`。  
3. **变现 + UE LLM**：装 `omer-game-monetization` 审一版 IAP/通行证伦理边界；有 NPC 对话需求时叠 `omer-llm-npc-dialogue` + `omer-unreal-llm-integration`（勿堵 GameThread）。

## 已尝试查询

1. 种子仓 commits / repo meta（JackyST0、mouadja02）
2. 跟踪仓 pushed_at / trees / license（omer、donchitos、ConnorGriffin、eve、kevin、sipher、Yuki001、Flue、lisxa5747、NAJEMWEHBE、august-batista、osseous/skills、w-zhian、avemeva、maystudios 等）
3. repos search：`game skills` / `unreal skills` / `cursor skills`；`skills created:2026-08-05` / `2026-08-06`
4. code search：Unreal / game design / path:.agents/skills / path:.cursor/skills → **HTTP 429**（本轮未恢复）
5. skills.sh/api/search：unreal、game design、umg、blender、level design、monetization、gamification、easter egg、ux review、vertical slice、team combat、rider
6. 候选 blob SKILL.md 质量核 + 入库 + push + open_git_pr + Slack
