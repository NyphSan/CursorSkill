# 技能侦察 DIGEST — 2026-08-06（05:00Z）

- 侦察时间：2026-08-06T05:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-06T04:00Z（同日上一轮，PR#27）
- 本仓入库：精选 **254** 个 `SKILL.md`（较上轮 +9；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-06-05`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。跟踪仓：`lisxa5747` / `Oliyflemishspeaking560` 再次仅 README 抖动（无新 SKILL）；lisxa 仓内 LICENSE 文件实为 **MIT**（API 仍报 NOASSERTION），但内容与 osseous 重叠，维持观望/降级。按「下次优先」**收齐 0xheycat 等距管线剩余 7 件**（autotiling / camera / tilemap-data / cutout / pipeline / tile-picking / canvas-perf），并新发现精选 **MengTo/Skills**（4108★ MIT）游戏开发包：`build-isometric-arpg`、`author-game-levels`。今日新建噪声约 45（空仓/工程通用）；`greatinterface/unreal-skill`（MIT 1★ AS/CQTest）→ 观望。skills.sh 印证 quodsoler / gamedev-skills 等已入库源仍活跃。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| heycat-autotiling-transitions | 2D | 地形自动过渡：16/47 bitmask 边角砖替代硬缝 | https://github.com/0xheycat/isometric-game-skills | MIT；接 seamless-terrain / tilemap-data | **引入** |
| heycat-camera-pan-zoom-controls | 2D | 等距相机：拖拽平移、光标锚点缩放与边界钳制 | 同上 | 与 tile-picking 成对；防 shimmer | **引入** |
| heycat-tilemap-data-format | 2D·工作流 | 引擎无关 JSON 地图：分层 + walkable 元数据 | 同上 | 设计/引擎共用真源；可 git diff | **引入** |
| heycat-transparent-cutout-cleanup | 2D | 去底抠图：去 halo/fringe 的干净 alpha | 同上 | 接 atlas packing；生成资产生成必经 | **引入** |
| heycat-asset-pipeline-automation | 2D·工作流 | 一键 clean→pack→JSON→validate 资产生成管线 | 同上 | 与 cutout/atlas 闭合；可进 CI | **引入** |
| heycat-tile-picking-interaction | 2D·游戏设计 | 屏→格拾取：反相机变换 + 高亮/放置 | 同上 | 接 camera + grid-math；可玩性交互 | **引入** |
| heycat-canvas-performance-optimization | 2D·工作流 | Canvas 等距 60fps：裁剪/批绘/静态层缓存 | 同上 | 大地图平移卡顿时的标准处方 | **引入** |
| mengto-build-isometric-arpg | 游戏设计·2D·3D | Three.js/Web 等距 ARPG：垂直切片到可玩循环 | https://github.com/MengTo/Skills | **本轮新见精选** 4108★ MIT；与 heycat 管线互补 | **引入** |
| mengto-author-game-levels | 游戏设计 | 可读关卡：单平面路线/遭遇/目标与确定性数据 | 同上 | 关卡即信息设计；可接 build-isometric-arpg | **引入** |

本仓已摘录：

- `skills/2d/heycat-autotiling-transitions/`
- `skills/2d/heycat-camera-pan-zoom-controls/`
- `skills/2d/heycat-tilemap-data-format/`
- `skills/2d/heycat-transparent-cutout-cleanup/`
- `skills/2d/heycat-asset-pipeline-automation/`
- `skills/2d/heycat-tile-picking-interaction/`
- `skills/2d/heycat-canvas-performance-optimization/`
- `skills/game-design/mengto-build-isometric-arpg/`（+ agents/）
- `skills/game-design/mengto-author-game-levels/`（+ agents/）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 18:06Z idea-refine；无新 commit | https://github.com/mouadja02/skills | **忽略**（通用 coding） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| lisxa5747 AngelScript | 04:36Z 仅 Update README；LICENSE 文件为 MIT | https://github.com/lisxa5747/unreal-angelscript-skills | **观望/降级**（优先 osseous） |
| Oliyflemishspeaking560/threejs-game-skills | 04:37Z 仅 Update README；0★ MIT | https://github.com/Oliyflemishspeaking560/threejs-game-skills | 观望/低优（疑似镜像 majid） |
| bomkino / Yuki001 / Stanestane / QQstone | 无新实质 / 仍无 LICENSE（后三者） | 各原仓 | 维持观望 |
| educlopez / ConnorGriffin / Flue / eve / OpenGame / sipher / vladmdgolam / gisenberg | 无实质变化 | 各原仓 | 维持观望 |

### 累计建议引入（仍有效）

1–90. 维持至上轮（含 heycat building/object/atlas/pathfinding/terrain/depth、donchitos team-audio/qa/release）  
91. **+ 本轮** heycat：autotiling / camera / tilemap-data / cutout / pipeline / tile-picking / canvas-perf  
92. **+ 本轮** mengto：build-isometric-arpg / author-game-levels

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| MengTo 其余 game-development（encounters/inventory/camera/vfx/ship-web…） | 游戏设计·3D | Web/Three.js 垂直切片技能簇 | https://github.com/MengTo/Skills | 本轮已收 isometric-arpg + levels；按需续摘 | **观望（调整）** |
| greatinterface/unreal-skill | UE | AS API 索引 / GameplayFramework / CQTest | https://github.com/greatinterface/unreal-skill | MIT 1★；与 osseous AS 重叠，CQTest 可补 | **观望（新增）** |
| vortechU/godot-skills | 2D·工作流 | Godot 引擎/GDScript/UI 索引 | https://github.com/vortechU/godot-skills | 0★ **无 LICENSE** | 观望/低优 |
| QQstone / Stanestane / Yuki001 | 2D·游戏设计 | 维持上轮 | 各原仓 | 仍无 LICENSE | 观望 |
| bomkino/pitchdog-design | UI·设计 | 品牌/作品设计 | https://github.com/bomkino/pitchdog-design | 偏品牌/Web | 观望 |
| ConnorGriffin / educlopez ui-craft | UI·工作流 | craft→critique→audit | 各原仓 | 偏产品/Web；可改造游戏 HUD | 观望 |
| sfkislev/flue / vladmdgolam | 3D·工作流 | Blender 桥 / MCP | 各原仓 | 本机路径或强依赖 MCP | 观望 |
| gisenberg / kevin / sipher / lisxa5747 / eve | UE 等 | 维持上轮理由 | 各原仓 | 许可或成熟度 | 观望 |
| 0xheycat 其余（animated-sprite、comfyui-lowvram、using-isometric-skills） | 2D | 动画精灵 / 低显存 Comfy / 元索引 | https://github.com/0xheycat/isometric-game-skills | 管线主链已齐；按需 | **观望（调整）** |
| NAJEMWEHBE / august-batista / OpenGame | UE·工作流 | MCP/桥/生态绑定 | 各原仓 | 强依赖 | 观望 |

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 idea-refine（方向无关，记数）
- ConnorGriffin 通用 orchestrate/say-less（非游戏向）
- 今日新建噪声（方向无关，约 45）：`daniyalasyed/skills`、`code-wangdi/agent-skills`（仅 LICENSE）、`edsonjaramillo/skills`、`whileingaa/skills`、`GUOJIE526/skills`、`fanghuaqi/skills`、`purushottam-gupta/skills`（空）、`hmeqo`/`TheShyWR`/`gemdesign-ai`/`wkentaro`/`guillezorrilla`/`homozzy` 等练习/通用仓
- `lisxa5747` / `Oliyflemishspeaking560`：仅 README 更新，不计实质
- eve-skills：EVE Online API
- 作弊/外挂类新建仓（如 Wilonity）一律忽略
- GitHub code search 不稳定；以 repos + skills.sh + 跟踪仓 trees 为准

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 仍为 **08-05 18:06Z** idea-refine portable（无关）；此后无新 commit |

## 本仓入库变化（+9 → 254）

- 新增 `skills/2d/heycat-autotiling-transitions/`
- 新增 `skills/2d/heycat-camera-pan-zoom-controls/`
- 新增 `skills/2d/heycat-tilemap-data-format/`
- 新增 `skills/2d/heycat-transparent-cutout-cleanup/`
- 新增 `skills/2d/heycat-asset-pipeline-automation/`
- 新增 `skills/2d/heycat-tile-picking-interaction/`
- 新增 `skills/2d/heycat-canvas-performance-optimization/`
- 新增 `skills/game-design/mengto-build-isometric-arpg/`
- 新增 `skills/game-design/mengto-author-game-levels/`
- 各含 `SOURCE.md`；mengto 两项含 `agents/`；承接上轮 245 条精选内容

## 今天可行动

1. **装**：`skills/2d/heycat-asset-pipeline-automation` + `transparent-cutout-cleanup` + 已入库 `spritesheet-atlas-packing` — 打通「生成→抠图→图集→校验」一键流。
2. **试**：`skills/game-design/mengto-build-isometric-arpg` 配 heycat `camera-pan-zoom` + `tile-picking` + `autotiling`，先做一条「移动→遭遇→奖励」垂直切片。
3. **个人化**：把 `mengto-author-game-levels` 的「单平面可读关卡」规则收成自己的关卡审查表（路线/地标/遭遇区 3 项），接到 UE 灰盒或 Web 原型。
