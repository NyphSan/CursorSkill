# 技能侦察 DIGEST — 2026-08-05（07:00Z）

- 侦察时间：2026-08-05T07:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T06:04Z（同日上一轮，PR#6）
- 本仓入库：精选 **88** 个 `SKILL.md`（较上轮 +3；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`cursor/bc-a6c159de-72a0-4f2c-a09b-fcf9ae364704-7d97`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。**实质增量**：① [fenggezaici/dcc-python-skills](https://github.com/fenggezaici/dcc-python-skills) 于 **06:52Z** 新增 UE 5.3.2 Python 反射 API skill（Maya/Houdini 已入库）；② skills.sh 交叉发现并晋升 [omer-metin/skills-for-antigravity](https://github.com/omer-metin/skills-for-antigravity) 的 game-ui-design；③ 将观望中的 [freshtechbro/claudedesignskills](https://github.com/freshtechbro/claudedesignskills) `blender-web-pipeline`（~1939 installs）升为引入。GitHub code search 本轮 **429 限流**；今日 `skill` 新建噪声 ≥100。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| unreal-engine-5-3-python-scripting | UE·3D | UE 5.3.2 `unreal` 模块编辑器脚本 / Blutility / 资产自动化速查 | https://github.com/fenggezaici/dcc-python-skills | **本轮实质更新**（06:52Z）；与已有 Maya/Houdini Python skill 成套；章节在原仓按需加载 | **引入** |
| game-ui-design（本仓名 game-ui-design-principles） | UI·游戏设计 | HUD/diegetic/电竞可读性 + patterns/sharp_edges/validations | https://github.com/omer-metin/skills-for-antigravity | Apache-2.0；skills.sh 高安装；与 guiguiyan 工作流型 UI skill 互补 | **引入** |
| blender-web-pipeline | 3D·工作流 | Blender→glTF/Web（Three.js/Babylon）导出与 bpy 批处理 | https://github.com/freshtechbro/claudedesignskills | skills.sh blender 类 ~1939 installs；MIT；补齐 Web 交付管线 | **引入** |

本仓已摘录：

- `skills/unreal/unreal-engine-5-3-python-scripting/`（+ cheatsheet/glossary/patterns；不含巨型 chapters）
- `skills/ui-design/game-ui-design-principles/`（+ references）
- `skills/3d/blender-web-pipeline/`（+ references/scripts/assets）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| fenggezaici/dcc-python-skills | **实质**：新增 UE Python skill；Maya/Houdini 不变 | https://github.com/fenggezaici/dcc-python-skills | 继续引入；仍无 SPDX |
| worldwonderer/novel-to-game | 03:32Z 恢复 trailer/play link（非 SKILL） | https://github.com/worldwonderer/novel-to-game | 继续引入 |
| guiguiyan930-source/game-ui-design-workflow | 仍停 02:53Z | https://github.com/guiguiyan930-source/game-ui-design-workflow | 继续引入 |
| kevinpbuckley/unreal-engine-skills | 仍为 08-04 UE 5.8 retarget | https://github.com/kevinpbuckley/unreal-engine-skills | 继续引入 |
| db-lyon/ue-mcp | 08-04 晚版本 bump / editor 启动稳健性 | https://github.com/db-lyon/ue-mcp | 继续引入（MCP 非 SKILL 变更） |
| makesupply/lodestar-skill | 仍停 01:54Z MIT 发布 | https://github.com/makesupply/lodestar-skill | 继续引入 |
| ch1109/portable-agent-skills | 05:59Z 初始开源；⭐→10 | https://github.com/ch1109/portable-agent-skills | 仍观望（方向弱） |
| Argentron-Technologies/mechfaber-agent | 仍 04:33Z | https://github.com/Argentron-Technologies/mechfaber-agent | 仍观望（CAD） |

### 累计建议引入（仍有效）

1–30. 维持上轮清单（含 dcc-python-skills Maya/Houdini、w-zhian GATE、sickn33/dstn/roble3/lodestar 等）  
31. **+ 本轮** dcc-python-skills 精选 `unreal-engine-5-3-python-scripting`  
32. **+ 本轮** https://github.com/omer-metin/skills-for-antigravity（精选 `game-ui-design`）  
33. **+ 本轮** freshtechbro 精选 `blender-web-pipeline`（原观望→引入）  

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| omer-metin 3d-modeling | 3D | 拓扑/UV/LOD/跨 DCC 生产原则 | https://github.com/omer-metin/skills-for-antigravity | 与 arjun988/roble3 重叠；先用 game-ui | 观望 |
| hkuds/cli-anything（blender / unrealinsights / game-development） | 3D·UE·工作流 | CLI 桥接桌面软件的 agent harness | https://github.com/hkuds/cli-anything | 46638★ Apache-2.0；单体巨大，先抽样再精选 | 观望 |
| freshtechbro 其余（Pixi/Substance/R3F/Babylon…） | 3D·2D·UI | Web3D / 2D 引擎技能簇 | https://github.com/freshtechbro/claudedesignskills | 已引入 blender-web；其余按需 | 观望 |
| sfkislev/flue（blender/houdini） | 3D·工作流 | 无 MCP 的桌面 bpy/hou CLI 桥 | https://github.com/SFKislev/Flue | skills.sh blender ~2340 installs；需本机 Flue | 观望 |
| w-zhian qa-review / article-curation / skill-evolution | 游戏设计·工作流 | 跨模块验收 / 情报策展 / 技能自演化 | https://github.com/w-zhian/game-design-skills | 次优先；GATE 四件套优先 | 观望 |
| davincidreams/agent-team-plugins（3d-design） | 3D | Blender/Unity/Omniverse 团队插件 skills | https://github.com/davincidreams/agent-team-plugins | 17★ 无 SPDX；结构可用 | 观望 |
| ceorkm/mobile-app-ui-design | UI | 移动端 UI/UX skill | https://github.com/ceorkm/mobile-app-ui-design | 213★；偏 App 非游戏 HUD | 观望 |
| zhangxiao6776/houdini-skills-for-share | 3D | Houdini Claude skills（share） | https://github.com/zhangxiao6776/houdini-skills-for-share | 树中未见 `SKILL.md`；仅作线索 | 观望 |
| 4lian/skills_collector（ui/frontend-dev） | UI·工作流 | 今日新建前端 skill | https://github.com/4lian/skills_collector | 0★ 无 license；弱相关 | 观望 |

其余观望（roble3 其余 Blender、vladmdgolam、ch1109、miramocha、media4agents-threejs、mechfaber、babysitter UE 切片、flowmock、famistudio 等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 仍仅 08-03 star chore；mouadja02 近提交仍为 Qdrant / Terraform / K8s CEL（无关）  
- `created:>=2026-08-05` 今日新建噪声 **≥100**（作品集、Copilot 练习题、SEO、PPT、房产、标题 skill 等）  
- xiaozhoustefanie227/jean-gauthier-paris-gallery-skill：艺术滤镜向；非主线  
- 1173206772/photo-skills：摄影编辑；非游戏/UE  
- nexx5/skills、sunmin-jung/claude-skill、aborgx/opencode-devflow：方向弱 / 通用工作流  
- zff1/project-memory-skills：通用 topic memory；可另议工作流，非本轮主线  

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 08-04：Qdrant / Terraform（无关）；无游戏/UE/设计向 |

## 本仓入库变化（+3 → 88）

- 新增 `skills/unreal/unreal-engine-5-3-python-scripting/`  
- 新增 `skills/ui-design/game-ui-design-principles/`  
- 新增 `skills/3d/blender-web-pipeline/`  
- 各含 `SOURCE.md`；承接上轮 85 条精选内容  

## 今天可行动

1. **UE Python 试跑**：在真实 UE 5.3/5.x 编辑器里用 `unreal-engine-5-3-python-scripting` 问「选中资产重命名 / Geometry Script 布尔」，并按需从原仓加载 `chapters/ch04` 或 `ch06`（本仓未镜像巨型章节）。  
2. **Game UI 双轨**：同一 HUD 需求先跑 `game-ui-design-principles`（原则+校验），再跑 `game-ui-workflow` / `game-ui-product-design`（产出规格），对比是否减少空泛建议。  
3. **个人 skill 候选**：把 `blender-web-pipeline` 的 glTF 导出清单裁成「Blender→UE 中间格式检查表」个人版；或把 dcc 三件套（Maya/Houdini/UE Python）做成统一 `/dcc-python` 路由 skill。

## 已尝试查询

1. 种子仓 commits / meta API（JackyST0、mouadja02）  
2. 跟踪仓 `pushed_at` / commits（dcc-python、novel-to-game、kevinpbuckley、db-lyon、lodestar、w-zhian、ch1109 等 30+）  
3. `gh search repos`：`skill created:>=2026-08-05`；`unreal skill` / `gamedev|blender skill created:>=2026-08-04`；`ue5 skill` / `houdini skill`  
4. `gh search code`：filename SKILL.md + Unreal / game design / path:.cursor/skills → **HTTP 429**（约 12 分钟冷却）  
5. skills.sh/api/search：unreal、gamedev、blender、ui design → 交叉核对 omer-metin / freshtechbro / flue / hkuds  
6. 候选 raw `SKILL.md` + git trees 抽样；CursorSkill 入库 / push / PR  
