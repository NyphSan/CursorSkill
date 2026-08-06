# 技能侦察 DIGEST — 2026-08-06（10:00Z）

- 侦察时间：2026-08-06T10:00Z（cron）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：Memories 2026-08-06 09:00Z（inventory；PR#31 / DIGEST 279 清单）
- 本仓入库：精选 **283** 个 `SKILL.md`（相对 CursorSkillSearch 旧态 279：+4）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

种子仓无方向相关新 skill。按基线「下次优先」从 **fagemx/gstack-game**（MIT 58★）择优引入 **triage / game-review / feel-pass**；并补齐 **quodsoler** 缺口 **ue-procedural-generation**（与已有 `unreal-pcg-python` 互补）。今日新建噪声约 100；SummerEngine（MIT 43★，引擎专属）与 Shellishack Three.js 低模簇列入观望。Yuki001 仍无 LICENSE；SherryCW 大师视角簇（宫本/小岛/宫崎/Schell）均无 LICENSE。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| fagemx-triage | 工作流·游戏设计 | 制作工作流入口：检测状态并路由到合适技能 | https://github.com/fagemx/gstack-game | MIT；解决「不知道从哪开」；可与 donchitos 并行 | **引入** |
| fagemx-game-review | 游戏设计 | 结构化 GDD 评审（循环/进度/经济/动机/风险） | 同上 | 含 references 评分维度；补 design-review | **引入** |
| fagemx-feel-pass | 游戏设计 | 可玩原型手感巡检（响应/打击/反馈链） | 同上 | 需实机或录像；补 game-feel 实操 | **引入** |
| ue-procedural-generation | UE·虚幻 | PCG / ProceduralMesh / ISM·HISM / 噪声样条生成 | https://github.com/quodsoler/unreal-engine-skills | MIT 301★；补齐 quodsoler 缺口 | **引入** |

本仓路径：

- `skills/workflow/fagemx-triage/`
- `skills/game-design/fagemx-game-review/`（+ references/）
- `skills/game-design/fagemx-feel-pass/`（+ references/）
- `skills/unreal/ue-procedural-generation/`（+ references/）

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| fagemx 其余 ~26 技能 | 游戏设计·工作流 | balance/ux/playtest/ship 等 | https://github.com/fagemx/gstack-game | 本轮已摘入口+评审+手感；余下择优 | **观望（维持）** |
| SummerEngine/summer-engine-agent | 游戏设计·工作流 | AI 游戏引擎 + 大量资产/玩法技能 | https://github.com/SummerEngine/summer-engine-agent | MIT 43★；今日有 push；**引擎专属**强绑定 | **观望（新增）** |
| Shellishack/3d-web-game-dev-skills | 3D·游戏设计 | Three.js 低模原型/HUD/光照等 | https://github.com/Shellishack/3d-web-game-dev-skills | MIT 5★；与 MengTo threejs 重叠 | **观望（新增）** |
| kparkov/skills | 游戏设计 | Blades in the Dark 桌面规则顾问 | https://github.com/kparkov/skills | 今日新建；有 SKILL.md；**无 LICENSE**；偏 TRPG | **观望（新增）** |
| alfaris/Design-AI-Skills-by-Faris | UI·设计 | 七视角设计审计面板 | https://github.com/alfaris/Design-AI-Skills-by-Faris | 今日新建；CC BY 4.0；偏产品/Web 非 UMG | **观望（新增）** |
| w-zhian/game-design-skills | 游戏设计 | 策划自进化技能包（战斗/经济/数值…） | https://github.com/w-zhian/game-design-skills | 有完整 SKILL 簇；**无 LICENSE** | **观望（新增）** |
| SherryCW/{shigeru-miyamoto,jesse-schell,miyazaki,hideo-kojima…} | 游戏设计 | 大师视角体验/叙事评审 | https://github.com/SherryCW/shigeru-miyamoto 等 | 方向贴合；**均无 LICENSE** | 观望 |
| KrickmanC / educlopez/ui-craft / Yuki001 / miramocha / ARKitRemap / Flue·roble3… | 各向 | 维持上轮 | 各原仓 | LICENSE/过窄/非游戏主路径未变 | 观望 |

## 可忽略

- 种子：JackyST0 仍仅 08-03 star chore；mouadja02 仍为 08-05 idea-refine（方向无关）
- 今日新建噪声约 100：GitHub Skills 练习仓、作品集、营销 agent（virajsutar）、通用 PM（Eggandsandwich）、etherscan、luckin-coffee、空仓（scenery-music-video、xcxxcx1996）等
- 作弊/外挂类一律忽略；kparkov 中 csharp 通用技能忽略

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | 614 | 仍仅 08-03 star chore | 无 UE/游戏专区新增 |
| mouadja02/skills | 9 | 仍为 08-05 18:06Z idea-refine | 方向无关 |

## 今天可行动

1. 新项目不确定从哪开时，先挂 `fagemx-triage`；有 GDD 时接 `fagemx-game-review`
2. 可玩原型到手感阶段跑 `fagemx-feel-pass`（准备实机录像或可玩构建）
3. UE 程序化内容用 `ue-procedural-generation`；Python 批处理仍用已有 `unreal-pcg-python`

## 查询记录

1. 种子仓 commits / meta（JackyST0、mouadja02）
2. 跟踪仓 license/pushed（MengTo、JetBrains、fagemx、Yuki、SherryCW、affinity/ui-craft/Flue/donchitos/omer/heycat/arg-games/ARKitRemap 等）
3. repos search：skills created:>=2026-08-06（约 100）；agent skills created:>=2026-08-05；unreal / game design / blender skills
4. code search：Unreal/game design filename:SKILL.md（多次 429）；blender/three.js 部分命中；skills.sh：unreal / game design / blender / ui design
5. 候选探测：fagemx 择优 3、quodsoler 缺口 1、SummerEngine、Shellishack、kparkov、alfaris、w-zhian、SherryCW 簇、KrickmanC、Eggandsandwich、lonestone/chisel、couletian 等
6. 入库：+4 → push `CursorSkillSearch` + 更新 PR#31
