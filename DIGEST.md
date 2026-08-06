# 技能侦察 DIGEST — 2026-08-06（03:00Z）

- 侦察时间：2026-08-06T03:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-06T02:00Z（同日上一轮，PR#25）
- 本仓入库：精选 **236** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-06-03`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill（JackyST0 仍停在 08-03 star chore；mouadja02 仍为 08-05 18:06Z idea-refine）。跟踪仓无实质 skill 更新（lisxa / Oliyf 上轮 README 抖动后无新 commit）。按「下次优先」升级引入 donchitos：**team-live-ops / team-polish / launch-checklist**；omer：**ai-world-building / streamer-bait-design**；0xheycat：**godot4-isometric-tilemap / canvas2d-isometric-renderer / isometric-character-sprites**。今日新建噪声约 35（练习仓/通用工程）；方向相关新出现：`bomkino/pitchdog-design`（0BSD 设计 skill，偏品牌/Web）、`educlopez/ui-craft`（MIT 249★ UI craft 系统）→ 观望。GitHub code search 仍 429；repos + skills.sh + 树/blob API 已覆盖。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| donchitos-team-live-ops | 游戏设计·工作流 | 运营团队编排：赛季/活动、经济、叙事、社群与分析 | https://github.com/donchitos/claude-code-game-studios | 23634★ MIT；接 gate-check / 发行流水线 | **引入** |
| donchitos-team-polish | 工作流 | 打磨团队：性能/技美/音频/QA 冲到发行质量 | 同上 | 垂直切片后的必经打磨阶段 | **引入** |
| donchitos-launch-checklist | 工作流 | 发行门禁：代码/内容/商店/法务/基建 go-no-go | 同上 | 与 gate-check 互补的上市清单 | **引入** |
| omer-ai-world-building | 游戏设计·3D | AI 一致性世界观/角色/环境 DNA，可规模化资产生成 | https://github.com/omer-metin/skills-for-antigravity | 123★ Apache-2.0；补 worldbuilding 的生成侧 | **引入** |
| omer-streamer-bait-design | 游戏设计 | 为直播/短视频优化的可剪辑玩法与社交钩子 | 同上 | 独立游戏获客向设计；易改成个人 skill | **引入** |
| heycat-godot4-isometric-tilemap | 2D | Godot 4 TileMapLayer + Y-sort 等距正确配置 | https://github.com/0xheycat/isometric-game-skills | MIT；接上轮 grid-math 的引擎落地 | **引入** |
| heycat-canvas2d-isometric-renderer | 2D | Canvas2D 等距渲染：地砖背到前 + 深度排序 | 同上 | 无引擎快速原型/Web 等距的渲染骨干 | **引入** |
| heycat-isometric-character-sprites | 2D | 等距角色精灵：8 向一致性与基准线锁定 | 同上 | 接 art-direction；角色量产前的规格 | **引入** |

本仓已摘录：

- `skills/workflow/donchitos-team-live-ops/`
- `skills/workflow/donchitos-team-polish/`
- `skills/workflow/donchitos-launch-checklist/`
- `skills/game-design/omer-ai-world-building/`（+ references）
- `skills/game-design/omer-streamer-bait-design/`（+ references）
- `skills/2d/heycat-godot4-isometric-tilemap/`
- `skills/2d/heycat-canvas2d-isometric-renderer/`
- `skills/2d/heycat-isometric-character-sprites/`

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 18:06Z idea-refine；无新 commit | https://github.com/mouadja02/skills | **忽略**（通用 coding） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| ConnorGriffin/skills | 无新于 22:54Z；license NOASSERTION | https://github.com/ConnorGriffin/skills | ui-craft 维持观望 |
| lisxa5747 AngelScript | 仍停在 01:55Z README；NOASSERTION | https://github.com/lisxa5747/unreal-angelscript-skills | **观望/降级**（优先 osseous） |
| Oliyflemishspeaking560/threejs-game-skills | 仍停在 01:57Z README；0★ MIT | https://github.com/Oliyflemishspeaking560/threejs-game-skills | 观望/低优（疑似镜像 majid） |
| Yuki001/game-dev-skills | 50★；仍无 LICENSE | https://github.com/Yuki001/game-dev-skills | 维持观望 |
| Flue / eve / OpenGame / sipher | 无实质变化 | 各原仓 | 维持观望 |
| tzwkb/lqe-translator | 已入库；本轮无新实质更新 | https://github.com/tzwkb/lqe-translator | 已引入，维持 |

### 累计建议引入（仍有效）

1–85. 维持至上轮（含 donchitos team-level/narrative/gate、omer worldbuilding/tabletop/prompt-to-game、heycat art-direction/grid-math）  
86. **+ 本轮** donchitos：team-live-ops / team-polish / launch-checklist  
87. **+ 本轮** omer：ai-world-building / streamer-bait-design  
88. **+ 本轮** heycat：godot4-isometric-tilemap / canvas2d-isometric-renderer / isometric-character-sprites

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| ConnorGriffin ui-craft | UI·工作流 | 视觉 lock→build→critique→audit | https://github.com/ConnorGriffin/skills | 偏 Web/产品 UI；可改造成游戏 UI | 观望 |
| educlopez/ui-craft | UI·工作流 | 设计工程系统：craft/critique/audit 等 20+ skill | https://github.com/educlopez/ui-craft | **本轮新见** MIT 249★；偏产品/Web UI，可摘 craft→游戏 HUD | **观望（新增）** |
| bomkino/pitchdog-design | UI·设计 | 品牌/作品设计：proof、soul、禁 house-style | https://github.com/bomkino/pitchdog-design | **本轮新建** 0BSD；偏品牌/Web，非游戏向 | **观望（新增）** |
| sfkislev/flue blender | 3D·工作流 | 无 MCP 的 shell→bpy 桌面桥 | https://github.com/sfkislev/flue | 65★ MIT；含本机路径 | 观望 |
| Yuki001/game-dev-skills | 游戏设计·3D·工作流 | architect / toon shader / 资产生成 | https://github.com/Yuki001/game-dev-skills | 50★；**无 LICENSE** | 观望 |
| kevin / sipher / lisxa5747 / eve | 各向 | 维持上轮理由 | 各原仓 | 许可或成熟度未变 | 观望 |
| 0xheycat 其余（building/object sprites、atlas、pathfinding、terrain 等） | 2D·3D | 等距资产生成与管线 | https://github.com/0xheycat/isometric-game-skills | 本轮已收 godot/canvas/character；按需续摘 | 观望 |
| vladmdgolam blender-mcp / cinema4d-mcp | 3D·工作流 | 经 MCP 驱动 Blender/C4D | https://github.com/vladmdgolam/agent-skills | MIT 7★；**本轮跟踪** 强依赖 MCP | **观望（新增）** |
| NAJEMWEHBE driving-unreal | UE·工作流 | 经 unreal-ai-connection MCP 驱编 | https://github.com/NAJEMWEHBE/unreal-ai-connection | MIT 9★；强依赖其 MCP | 观望 |
| august-batista unreal-assets | UE | 安全读写 .uasset/.umap | https://github.com/august-batista/claude-unreal-bridge-editor | MIT 0★；强依赖桥 | 观望 |
| opengameapp/OpenGame-skills | 游戏设计·工作流 | 浏览器原型 + Skill/MCP 发布 | https://github.com/opengameapp/OpenGame-skills | MIT-0 0★；偏 OpenGame 生态 | 观望 |
| w-zhian / avemeva | 游戏/UI | 维持上轮 | 各原仓 | 0★ 无 LICENSE | 观望/低优 |

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 idea-refine（方向无关，记数）
- ConnorGriffin 通用 orchestrate/say-less（非游戏向）
- 今日新建噪声（方向无关，约 35）：`zizz1/agent-research-skills`、`brunolueng-netizen/sforge`、`Newbie1402/agent-skills`（FE/BE 通用）、`mrtsels/skills`（学术大杂烩）、`wkentaro/skills`（工程流程）、各类 `skills-introduction-to-github` 练习仓等
- `droolygames/ddd-games`：双许可/Web3 游戏竞技场，无 SKILL.md
- `Oliyflemishspeaking560/threejs-game-skills`：0★ 疑似镜像
- eve-skills：EVE Online API
- GitHub code search 仍 HTTP 429；以 repos + skills.sh + 跟踪仓 trees 为准

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 仍为 **08-05 18:06Z** idea-refine portable（无关）；此后无新 commit |

## 本仓入库变化（+8 → 236）

- 新增 `skills/workflow/donchitos-team-live-ops/`
- 新增 `skills/workflow/donchitos-team-polish/`
- 新增 `skills/workflow/donchitos-launch-checklist/`
- 新增 `skills/game-design/omer-ai-world-building/`
- 新增 `skills/game-design/omer-streamer-bait-design/`
- 新增 `skills/2d/heycat-godot4-isometric-tilemap/`
- 新增 `skills/2d/heycat-canvas2d-isometric-renderer/`
- 新增 `skills/2d/heycat-isometric-character-sprites/`
- 各含 `SOURCE.md`；omer 两项含 `references/`；承接上轮 228 条精选内容

## 今天可行动

1. **装**：`skills/workflow/donchitos-launch-checklist` + `skills/workflow/donchitos-team-polish` — 对当前垂直切片做一次 dry-run 发行清单，再开打磨冲刺。
2. **试**：`skills/2d/heycat-canvas2d-isometric-renderer` 配已入库的 `isometric-grid-math`，用 Canvas 快速验证等距渲染与深度排序。
3. **个人化**：把 `omer-streamer-bait-design` 收成自己的「可剪辑时刻」检查表（固定 3 个 clip 触发器 + 1 个社交钩子），接到 UE/原型迭代。
