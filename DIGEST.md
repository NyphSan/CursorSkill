# 技能侦察 DIGEST — 2026-08-05（06:04Z）

- 侦察时间：2026-08-05T06:04Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T05:04Z（同日上一轮，PR#5）
- 本仓入库：精选 **85** 个 `SKILL.md`（较上轮 +7；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`cursor/bc-c34fcf9d-02b0-4f86-a066-0393046927e4-d9fb`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill；`dcc-python-skills` 仅 README/AGENTS 润色，**SKILL.md 内容未变**。GitHub code search 本轮空结果并触发 search API 限流。主增量来自：① 上轮点名盯梢的 [w-zhian/game-design-skills](https://github.com/w-zhian/game-design-skills) 剩余策划 GATE 三条；② skills.sh 交叉发现且此前未入库的 UE/Blender 精选；③ 今日新建 [makesupply/lodestar-skill](https://github.com/makesupply/lodestar-skill)（行为设计→UI）。今日新建噪声约 50+。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| wzhian-combat-design | 游戏设计 | 战斗范式分类 + Fantasy/张力/技能表达 GATE | https://github.com/w-zhian/game-design-skills | 与已有 everything-game-dev `combat-design` 互补；GATE 更可执行 | **引入** |
| system-design | 游戏设计 | 系统边界/依赖/配表面与元结构 | https://github.com/w-zhian/game-design-skills | 填补本仓「系统策划」空白；与 gameplay/numerical 成套 | **引入** |
| economy-design | 游戏设计 | 资源流清单 + 商业化公平性硬门槛 | https://github.com/w-zhian/game-design-skills | 比已有 economy-balancing 更偏商业化边界 | **引入** |
| unreal-engine-cpp-pro | UE | UE5 C++ UObject 卫生、Tick/反射/性能惯例 | https://github.com/sickn33/antigravity-awesome-skills | skills.sh ~1169 installs；MIT；与 ue-cpp-foundations 互补 | **引入** |
| ue-project-discovery | UE | 先发现 `.uproject`/引擎版本/插件再给建议 | https://github.com/dstn2000/claude-unreal-engine-skill | skills.sh ~462 installs；零假设发现协议实用 | **引入** |
| blender-pro-workflow | 3D·工作流 | 场景生产 11 步顺序与子 skill 编排 | https://github.com/roble3/cc-blender-skill | MIT；编排已有 blender-modeler；原仓 30+ skills 精选本条 | **引入** |
| lodestar | UI·游戏设计 | 证据分级行为设计：激活/留存/游戏化→UI 规格 | https://github.com/makesupply/lodestar-skill | **今日新建**；含 references；暗黑模式拒绝表 | **引入** |

本仓已摘录：

- `skills/game-design/wzhian-combat-design/`
- `skills/game-design/system-design/`
- `skills/game-design/economy-design/`
- `skills/unreal/unreal-engine-cpp-pro/`
- `skills/unreal/ue-project-discovery/`
- `skills/3d/blender-pro-workflow/`
- `skills/ui-design/lodestar/`（含 `references/`）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| fenggezaici/dcc-python-skills | 05:00–05:09：AGENTS.md + README 样式；SKILL.md sha 未变 | https://github.com/fenggezaici/dcc-python-skills | 继续引入；仍无 SPDX |
| guiguiyan930-source/game-ui-design-workflow | 仍停 02:53Z | https://github.com/guiguiyan930-source/game-ui-design-workflow | 继续引入 |
| kevinpbuckley/unreal-engine-skills | 仍为 08-04 UE 5.8 | https://github.com/kevinpbuckley/unreal-engine-skills | 继续引入 |
| Argentron-Technologies/mechfaber-agent | 仍 0.1.1（04:33Z） | https://github.com/Argentron-Technologies/mechfaber-agent | 仍观望（CAD） |

### 累计建议引入（仍有效）

1–26. 维持上轮清单（含 dcc-python-skills / w-zhian 精选 / roguelike）  
27. **+ 本轮** https://github.com/sickn33/antigravity-awesome-skills（精选 `unreal-engine-cpp-pro`）  
28. **+ 本轮** https://github.com/dstn2000/claude-unreal-engine-skill  
29. **+ 本轮** https://github.com/roble3/cc-blender-skill（精选 `blender-pro-workflow`）  
30. **+ 本轮** https://github.com/makesupply/lodestar-skill  

## 观望（本轮新增）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| roble3 其余 Blender skills | 3D | modeling/materials/lighting/export 等 30+ | https://github.com/roble3/cc-blender-skill | 与 arjun988 blender-modeler 重叠；先试 pro-workflow | 观望 |
| freshtechbro/claudedesignskills | 3D·2D·UI | Blender→web、PixiJS、Substance、Three.js 等 | https://github.com/freshtechbro/claudedesignskills | 660★ MIT；偏 Web3D；与 mint/cloudai 重叠 | 观望 |
| sfkislev/flue（blender/houdini） | 3D·工作流 | 无 MCP 的桌面 bpy/hou CLI 桥 | https://github.com/sfkislev/flue | 范式不同；需本机 Flue | 观望 |
| w-zhian qa-review / article-curation / skill-evolution | 游戏设计·工作流 | 跨模块验收 / 情报策展 / 技能自演化 | https://github.com/w-zhian/game-design-skills | 次优先；先把 GATE 四件套跑通 | 观望 |
| vladmdgolam/agent-skills | 3D·UI | blender-mcp / cinema4d / figma / threejs-perf | https://github.com/vladmdgolam/agent-skills | 7★；MCP 依赖重 | 观望 |
| ch1109/portable-agent-skills | 工作流 | 研究 / 部署 / skill 安全扫描 | https://github.com/ch1109/portable-agent-skills | 今日新建 MIT；方向弱相关 | 观望 |

其余观望（miramocha、media4agents-threejs、mechfaber、babysitter 游戏切片、flowmock、famistudio、sonic7881963、anatu iOS 等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 仍仅 08-03 star chore；mouadja02 仍为 Qdrant/Terraform（无关）  
- `created:>2026-08-05` 今日新建噪声约 **50+**（Copilot 练习题、SEO skill、作品集、健康分析、短剧提示词等）  
- xiaozhoustefanie227/jean-gauthier-paris-gallery-skill：仅 zip，无裸 `SKILL.md`  
- thekingsmediastudio/agent-skills：树中无 `SKILL.md`  
- Chank0710/heygen-digital-human-video：数字人视频，非 UE/游戏主线  
- AutoArchive/seo-skill、pushpendrasinghbaghel-ai/dynatrace-ai-skills：方向无关  

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 08-04：Qdrant / Terraform（无关） |

## 本仓入库变化（+7 → 85）

- 新增 `skills/game-design/wzhian-combat-design/`  
- 新增 `skills/game-design/system-design/`  
- 新增 `skills/game-design/economy-design/`  
- 新增 `skills/unreal/unreal-engine-cpp-pro/`  
- 新增 `skills/unreal/ue-project-discovery/`  
- 新增 `skills/3d/blender-pro-workflow/`  
- 新增 `skills/ui-design/lodestar/`（+ references）  
- 各含 `SOURCE.md`；承接上轮 78 条精选内容  

## 今天可行动

1. **策划四件套联调**：同题串 `gameplay-design` → `wzhian-combat-design` / `system-design` → `economy-design` → `numerical-planning`，看 GATE 硬门槛是否比散文式建议更好用。  
2. **UE 开工协议**：把 `ue-project-discovery` 放在 `unreal-engine-cpp-pro` / `ue-cpp-foundations` 之前，用真实 `.uproject` 验证「先发现再建议」是否减少幻觉。  
3. **个人 skill 候选**：`lodestar` 可裁成「游戏激活/D1 留存 + 反暗黑模式」个人版；`blender-pro-workflow` 可改激活描述指向你已装的 Blender MCP 子 skill。

## 已尝试查询

1. 种子仓 commits / meta API  
2. 跟踪仓 `pushed_at` / commits（含 dcc-python-skills、mechfaber、w-zhian、kevinpbuckley 等）  
3. `gh search repos`：`skill created:>2026-08-05T05:00:00Z`；unreal/gamedev/blender/… `created:>2026-08-04`（多为空）；后续触发 **search API 403 限流**  
4. `gh search code`：filename SKILL.md + Unreal / game design / path:.cursor/skills（空）  
5. skills.sh/api/search：unreal、gamedev、blender → 交叉核对高安装量源仓  
6. 候选 raw `SKILL.md` 抽样 + CursorSkill 入库 / push / PR  
