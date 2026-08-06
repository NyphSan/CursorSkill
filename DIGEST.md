# 技能侦察 DIGEST — 2026-08-06（02:00Z）

- 侦察时间：2026-08-06T02:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-06T01:00Z（同日上一轮，PR#24）
- 本仓入库：精选 **228** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-06-02`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。跟踪仓：lisxa5747 **01:55Z**、Oliyf **01:57Z** 仅 Update README（无实质 skill 变化；lisxa 仍无 LICENSE）。Yuki001 仍无 LICENSE；ConnorGriffin / Flue / kevin / sipher 无新实质更新。本轮按「下次优先」升级引入 donchitos：**team-level / team-narrative / gate-check**；omer：**worldbuilding / tabletop-rpg-design / prompt-to-game**；0xheycat：**isometric-art-direction / isometric-grid-math**（MIT 6★，从观望升引入）。今日新建噪声约 30（空仓/通用工程/练习仓），方向相关 0。GitHub code search 仍 429；repos + skills.sh + 树/blob API 已覆盖。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| donchitos-team-level | 游戏设计·工作流 | 关卡团队编排：叙事/世界观/关卡/系统/美术/无障碍/QA | https://github.com/donchitos/claude-code-game-studios | 23632★ MIT；接上轮 team-combat / vertical-slice | **引入** |
| donchitos-team-narrative | 游戏设计·工作流 | 叙事团队编排：导演/编剧/世界观/关卡叙事与本地化就绪 | 同上 | 与 narrative-design / worldbuilding 成流水线 | **引入** |
| donchitos-gate-check | 工作流 | 阶段门禁：PASS/CONCERNS/FAIL + 阻塞项与必备产物 | 同上 | 预制作→量产→发行的硬门禁；工业流程核心 | **引入** |
| omer-worldbuilding | 游戏设计 | 虚构世界观、魔法体系与传说一致性（冰山法则） | https://github.com/omer-metin/skills-for-antigravity | 123★ Apache-2.0；补齐 lore / 世界观缺口 | **引入** |
| omer-tabletop-rpg-design | 游戏设计 | 桌面 RPG：骰子机制、角色创建、GM 工具与试玩 | 同上 | 系统向设计可反哺数字 RPG / 规则原型 | **引入** |
| omer-prompt-to-game | 游戏设计·工作流 | 自然语言 vibe coding 快速出可玩原型 | 同上 | 接 prototype / vertical-slice；易改成个人 jam skill | **引入** |
| heycat-isometric-art-direction | 2D·3D | 等距项目先锁 STYLE.md（投影/光/色板/尺度） | https://github.com/0xheycat/isometric-game-skills | MIT 6★；量产资产生成前的一致性锚点 | **引入** |
| heycat-isometric-grid-math | 2D | 等距网格↔屏幕坐标与点选公式（2:1） | 同上 | 与 art-direction 成对；渲染/点选必用 | **引入** |

本仓已摘录：

- `skills/workflow/donchitos-team-level/`
- `skills/workflow/donchitos-team-narrative/`
- `skills/workflow/donchitos-gate-check/`
- `skills/game-design/omer-worldbuilding/`（+ references）
- `skills/game-design/omer-tabletop-rpg-design/`（+ references）
- `skills/game-design/omer-prompt-to-game/`（+ references）
- `skills/2d/heycat-isometric-art-direction/`
- `skills/2d/heycat-isometric-grid-math/`

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 18:06Z idea-refine；无新 commit | https://github.com/mouadja02/skills | **忽略**（通用 coding） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| ConnorGriffin/skills | 无新于 22:54Z；license NOASSERTION | https://github.com/ConnorGriffin/skills | ui-craft 维持观望 |
| lisxa5747 AngelScript | **01:55Z** 再 Update README；仍 NOASSERTION | https://github.com/lisxa5747/unreal-angelscript-skills | **观望/降级**（优先 osseous） |
| Oliyflemishspeaking560/threejs-game-skills | **01:57Z** Update README；0★ MIT | https://github.com/Oliyflemishspeaking560/threejs-game-skills | 观望/低优（疑似镜像） |
| Yuki001/game-dev-skills | 50★；仍无 LICENSE | https://github.com/Yuki001/game-dev-skills | 维持观望 |
| kevin / sipher / Flue / eve | 无实质变化 | 各原仓 | 维持观望 |
| opengameapp/OpenGame-skills | 无新；MIT-0 生态绑定 | https://github.com/opengameapp/OpenGame-skills | 观望 |
| 0xheycat 其余等距技能 | art-direction/grid-math 已引入；余下 sprite/godot/canvas 等 | https://github.com/0xheycat/isometric-game-skills | 观望（下次可续摘） |

### 累计建议引入（仍有效）

1–82. 维持至上轮（含 donchitos ux-review/team-combat/vertical-slice/prototype、omer monetization/gamification/easter-egg/unreal-llm）  
83. **+ 本轮** donchitos：team-level / team-narrative / gate-check  
84. **+ 本轮** omer：worldbuilding / tabletop-rpg-design / prompt-to-game  
85. **+ 本轮** heycat：isometric-art-direction / isometric-grid-math

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| ConnorGriffin ui-craft | UI·工作流 | 视觉 lock→build→critique→audit | https://github.com/ConnorGriffin/skills | 偏 Web/产品 UI；可改造成游戏 UI | 观望 |
| sfkislev/flue blender | 3D·工作流 | 无 MCP 的 shell→bpy 桌面桥 | https://github.com/sfkislev/flue | 65★ MIT；含本机路径 | 观望 |
| Yuki001/game-dev-skills | 游戏设计·3D·工作流 | architect / toon shader / 资产生成 | https://github.com/Yuki001/game-dev-skills | 50★；**无 LICENSE** | 观望 |
| kevin / sipher / lisxa5747 / eve | 各向 | 维持上轮理由 | 各原仓 | 许可或成熟度未变 | 观望 |
| donchitos team-live-ops / team-polish / launch-checklist | 工作流 | 运营/打磨/发行清单团队技能 | https://github.com/donchitos/claude-code-game-studios | 本轮已收 level/narrative/gate；下次可续 | 观望 |
| omer-ai-world-building / streamer-bait-design | 游戏设计 | AI 世界观生成 / 直播友好设计钩子 | https://github.com/omer-metin/skills-for-antigravity | 本轮优先 worldbuilding/tabletop/prompt-to-game | 观望 |
| 0xheycat 其余（godot4-tilemap / canvas2d-renderer / sprites 等） | 2D·3D | 等距渲染与资产生成管线 | https://github.com/0xheycat/isometric-game-skills | art-direction+grid-math 已引入；按需续摘 | 观望 |
| NAJEMWEHBE driving-unreal | UE·工作流 | 经 unreal-ai-connection MCP 驱编 | https://github.com/NAJEMWEHBE/unreal-ai-connection | MIT 9★；强依赖其 MCP | 观望 |
| august-batista unreal-assets | UE | 安全读写 .uasset/.umap | https://github.com/august-batista/claude-unreal-bridge-editor | MIT 0★；强依赖桥 | 观望 |
| opengameapp/OpenGame-skills | 游戏设计·工作流 | 浏览器原型 + Skill/MCP 发布 | https://github.com/opengameapp/OpenGame-skills | MIT-0 0★；偏 OpenGame 生态 | 观望 |
| w-zhian / avemeva | 游戏/UI | 维持上轮 | 各原仓 | 0★ 无 LICENSE | 观望/低优 |

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 idea-refine（方向无关，记数）
- ConnorGriffin 通用 orchestrate/say-less 增量（非游戏向）
- 今日新建噪声（方向无关，约 30）：`YuyaoLin042/art-skills`（空仓）、`TwilightRainDev/claude-skills`（提示词/编码指南）、`snailer-team/JeffDean-Mind`、`pubudu538/agent-skills`、`Kazppe/agent-skills`、`PeaceFamily000/Robocon`、各类 skills 练习仓等
- `Oliyflemishspeaking560/threejs-game-skills`：0★ 疑似镜像，仅 README 抖动
- eve-skills：EVE Online API
- GitHub code search 仍 HTTP 429；以 repos + skills.sh + 跟踪仓 trees 为准

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 仍为 **08-05 18:06Z** idea-refine portable（无关）；此后无新 commit |

## 本仓入库变化（+8 → 228）

- 新增 `skills/workflow/donchitos-team-level/`
- 新增 `skills/workflow/donchitos-team-narrative/`
- 新增 `skills/workflow/donchitos-gate-check/`
- 新增 `skills/game-design/omer-worldbuilding/`
- 新增 `skills/game-design/omer-tabletop-rpg-design/`
- 新增 `skills/game-design/omer-prompt-to-game/`
- 新增 `skills/2d/heycat-isometric-art-direction/`
- 新增 `skills/2d/heycat-isometric-grid-math/`
- 各含 `SOURCE.md`；omer 三项含 `references/`；承接上轮 220 条精选内容

## 今天可行动

1. **装**：`skills/workflow/donchitos-gate-check` + `skills/workflow/donchitos-team-level` — 用阶段门禁卡住预制作→量产，再用关卡团队编排跑一个区域。
2. **试**：`skills/2d/heycat-isometric-art-direction` 先写 STYLE.md，再配 `isometric-grid-math` 验证坐标往返；适合等距原型开场。
3. **个人化**：把 `omer-prompt-to-game` 收成自己的 jam/原型 skill（固定引擎=UE 或 HTML、固定输出目录与验收清单）。
