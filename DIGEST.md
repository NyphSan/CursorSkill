# 技能侦察 DIGEST — 2026-08-06（00:00Z）

- 侦察时间：2026-08-06T00:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T23:00Z（同日上一轮，PR#22）
- 本仓入库：精选 **212** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-06-00`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。跟踪仓：lisxa5747 **23:15Z** 仅 README SEO 改写（维持观望/降级）；ConnorGriffin 无新 push（上次 22:54Z orchestrate）；Yuki001/kevin/sipher 许可未变；osseous 主仓实为 [osseous/skills](https://github.com/osseous/skills)（MIT，AngelScript/读日志，已有摘录）。本轮按「下次优先」引入 donchitos：**balance-check / team-ui / playtest-report / ux-design**；以及 omer：**player-onboarding / vehicle-design / mobile-game-dev / llm-npc-dialogue**。Flue、ui-craft、driving-unreal、august-batista unreal-assets 继续观望。今日新建噪声多为营销/TDD/Telegram/Slideshow/投注等，方向无关只记数。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| donchitos-balance-check | 游戏设计·工作流 | 扫描数值/战斗/经济/进度数据找异常与退化策略 | https://github.com/donchitos/claude-code-game-studios | 23630★ MIT；与已有 evaluating-gameplay-balance / progression 成门禁 | **引入** |
| donchitos-team-ui | UI·工作流 | 编排 UX→视觉→实现→评审的 UI 团队流水线 | 同上 | 游戏 UI 工程化缺口；接 omer-game-ui-design | **引入** |
| donchitos-playtest-report | 游戏设计·工作流 | 试玩报告模板 / 原始笔记结构化 | 同上 | 闭环验证必备；与 balance-check 成对 | **引入** |
| donchitos-ux-design | UI·游戏设计 | 分节撰写屏幕/HUD/交互模式 UX 规格 | 同上 | team-ui 前置；补齐 UX 规格作者 | **引入** |
| omer-player-onboarding | 游戏设计 | FTUE/教程与留存导向的新手引导 | https://github.com/omer-metin/skills-for-antigravity | 123★ Apache-2.0；补齐 onboarding 缺口 | **引入** |
| omer-vehicle-design | 3D·2D | 载具/机甲/飞船造型与硬表面形式语言 | 同上 | 与 creature/weapon 成套概念美术 | **引入** |
| omer-mobile-game-dev | 游戏设计 | 手游触控/散热/功耗与商店上架约束 | 同上 | 移动端此前偏薄；可对接 UE 手游 | **引入** |
| omer-llm-npc-dialogue | 游戏设计·AI | LLM NPC 对话、人格记忆与破戏防护 | 同上 | 与已收 game-ai / narrative 互补 | **引入** |

本仓已摘录：

- `skills/workflow/donchitos-balance-check/`
- `skills/ui-design/donchitos-team-ui/`
- `skills/workflow/donchitos-playtest-report/`
- `skills/ui-design/donchitos-ux-design/`
- `skills/game-design/omer-player-onboarding/`（+ references）
- `skills/3d/omer-vehicle-design/`（+ references）
- `skills/game-design/omer-mobile-game-dev/`（+ references）
- `skills/game-design/omer-llm-npc-dialogue/`（+ references）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 18:06Z idea-refine；无新 commit | https://github.com/mouadja02/skills | **忽略**（通用 coding） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| ConnorGriffin/skills | 无新于 22:54Z；license NOASSERTION | https://github.com/ConnorGriffin/skills | ui-craft 维持观望（偏 Web UI） |
| lisxa5747 AngelScript | **23:15Z** README SEO 改写；仍 NOASSERTION | https://github.com/lisxa5747/unreal-angelscript-skills | **观望/降级**（优先 osseous） |
| snipereagle1/eve-skills | 仍为 20:03Z ESI/SDE | https://github.com/snipereagle1/eve-skills | EVE 专用 → 观望/低优 |
| Yuki001/game-dev-skills | 仍无 LICENSE；49★ | https://github.com/Yuki001/game-dev-skills | 维持观望 |
| kevinpbuckley/unreal-engine-skills | 08-04 UE 5.8；仍无 SPDX | https://github.com/kevinpbuckley/unreal-engine-skills | 维持观望 |
| sipherxyz/universal-ue-skills | 07-31；1★ 无 LICENSE | https://github.com/sipherxyz/universal-ue-skills | 观望 |
| sfkislev/flue | 无新 push | https://github.com/sfkislev/flue | 观望（需本机 Flue） |
| osseous/skills | 纠正：主仓为 osseous/skills（非 unreal-engine-skills） | https://github.com/osseous/skills | 已有摘录；低活跃 |

### 累计建议引入（仍有效）

1–78. 维持至上轮（含 omer creature/procgen/weapon/net/progression、donchitos asset-spec/design-review、blender-unreal-export）  
79. **+ 本轮** donchitos：balance-check / team-ui / playtest-report / ux-design  
80. **+ 本轮** omer：player-onboarding / vehicle-design / mobile-game-dev / llm-npc-dialogue

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| ConnorGriffin ui-craft | UI·工作流 | 视觉 lock→build→critique→audit | https://github.com/ConnorGriffin/skills | 偏 Web/产品 UI；可改造成游戏 UI 个人 skill | 观望 |
| sfkislev/flue blender | 3D·工作流 | 无 MCP 的 shell→bpy 桌面桥 | https://github.com/sfkislev/flue | 65★ MIT；含本机路径 | 观望 |
| Yuki001/game-dev-skills | 游戏设计·3D·工作流 | architect / toon shader / 资产生成 | https://github.com/Yuki001/game-dev-skills | 49★；**无 LICENSE** | 观望 |
| kevin / sipher / lisxa5747 / eve | 各向 | 维持上轮理由 | 各原仓 | 许可或成熟度未变 | 观望 |
| omer-game-monetization / gamification-loops / easter-egg-design | 游戏设计 | 变现/循环/彩蛋 | https://github.com/omer-metin/skills-for-antigravity | 本轮优先 onboarding/手游/NPC；下次可摘 | 观望 |
| donchitos ux-review / team-combat / vertical-slice | 工作流 | UX 门禁与品类流水线 | https://github.com/donchitos/claude-code-game-studios | 本轮已收 ux-design/team-ui；下次可续 | 观望 |
| NAJEMWEHBE driving-unreal | UE·工作流 | 经 unreal-ai-connection MCP 驱编 | https://github.com/NAJEMWEHBE/unreal-ai-connection | MIT 9★；强依赖其 MCP | 观望 |
| august-batista unreal-assets | UE | 安全读写 .uasset/.umap | https://github.com/august-batista/claude-unreal-bridge-editor | MIT 0★；强依赖桥 | 观望 |
| w-zhian/game-design-skills | 游戏设计 | 策划向自演化包 | https://github.com/w-zhian/game-design-skills | 0★ 无 LICENSE；重叠 | 观望/低优 |
| avemeva/design-boilerplate | UI | Next.js 设计工程样板+28 craft skills | https://github.com/avemeva/design-boilerplate | 今日新建 0★ 无 LICENSE；偏 Web | 观望/低优 |

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 idea-refine（方向无关，记数）
- ConnorGriffin 通用 orchestrate/say-less 增量（非游戏向）
- 今日新建噪声（方向无关，约 20+）：`vaishnvaik6/brand-website-copy-skill`、`brookejlacey/boring-tools`、`ChloeVPin/tdd-agent-skill`、`penkayone/media-hold-telegram-leads-skill`、`Orange-County-AI/slideshow`、`jvorndran/cfb-betting-skills`、`theocarranza/agent-plugin-template`、`0xwilliamortiz/claude-red` 等
- eve-skills：EVE Online API
- path:.agents/skills / path:.cursor/skills 本轮 code search 无新增游戏/UE 命中

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 仍为 **08-05 18:06Z** idea-refine portable（无关）；此后无新 commit |

## 本仓入库变化（+8 → 212）

- 新增 `skills/workflow/donchitos-balance-check/`
- 新增 `skills/ui-design/donchitos-team-ui/`
- 新增 `skills/workflow/donchitos-playtest-report/`
- 新增 `skills/ui-design/donchitos-ux-design/`
- 新增 `skills/game-design/omer-player-onboarding/`
- 新增 `skills/3d/omer-vehicle-design/`
- 新增 `skills/game-design/omer-mobile-game-dev/`
- 新增 `skills/game-design/omer-llm-npc-dialogue/`
- 各含 `SOURCE.md`；承接上轮 204 条精选内容

## 今天可行动

1. **UI 流水线**：先跑 `donchitos-ux-design` 写一屏/HUD 规格，再用 `donchitos-team-ui` 走实现门禁；对照已有 `omer-game-ui-design` / `ue5-ui-umg-slate`。  
2. **验证闭环**：改数值后用 `donchitos-balance-check`，试玩笔记丢进 `donchitos-playtest-report`；适合改成你项目的 data 路径个人 skill。  
3. **FTUE + LLM NPC**：装 `omer-player-onboarding` 设计 30 秒钩子，再用 `omer-llm-npc-dialogue` 约束破戏；载具概念叠 `omer-vehicle-design`。

## 已尝试查询

1. 种子仓 commits / repo meta（JackyST0、mouadja02）
2. 跟踪仓 pushed_at / trees / license（omer、donchitos、ConnorGriffin、eve、kevin、sipher、Yuki001、Flue、arjun988、maystudios、MengTo、lisxa5747、NAJEMWEHBE、august-batista、osseous/skills、teixasalone、w-zhian 等）
3. repos search：skill/skills created≥08-04/05；unreal/gamedev/game design skills；agent skills
4. code search：Unreal filename:SKILL.md；game design filename:SKILL.md；path:.agents/skills；path:.cursor/skills
5. skills.sh/api/search：unreal、balance check、playtest、team ui、player onboarding、vehicle design、mobile game、umg、level design、art bible、blender
6. 候选 blob SKILL.md 质量核 + 入库 + push + open_git_pr + Slack
