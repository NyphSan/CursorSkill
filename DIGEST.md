# 技能侦察 DIGEST — 2026-08-05（03:03Z）

- 侦察时间：2026-08-05T03:03Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T02:03Z（同日上一轮）
- 本仓入库：精选 **68** 个 `SKILL.md`（较上轮 +4；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`cursor/bc-caf7604e-bcf1-4356-b8b0-7a076cb73135-dd8e`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。**实质增量**集中在游戏 UI：`game-ui-design-workflow` 新增 `game-ui-product-design`（策划/PRD/交互门禁，流程变为 8 skills）并持续推送。新发现可装包：`888wing/game-ui-skill`、`zhijianfan/NiagaraSkill`、`HabrielStark/brilliant-blender-skill`。噪声仓（created:>2026-08-04）约 27 条，方向无关未展开。

## 建议引入（本轮增量）

| 名称 | 方向 | 一句话用途 | 仓库 | 关注点 | 建议 |
|---|---|---|---|---|---|
| game-ui-product-design | UI·游戏设计 | UI 生图前先写 GDD/PRD/交互逻辑并人工批准 | https://github.com/guiguiyan930-source/game-ui-design-workflow | MIT；本轮新 skill；工作流第 1 步 | **引入** |
| design-game-ui | UI·游戏 | 游戏内 HUD/菜单等设计·实现·打磨·审计 | https://github.com/888wing/game-ui-skill | MIT；路径 `.agents/skills/`；与上者互补 | **引入** |
| niagara-json-generator | UE | JSON 规格 → UE5.8 Niagara 无头编译/验收 | https://github.com/zhijianfan/NiagaraSkill | MIT；依赖同仓插件；非纯文档 skill | **引入** |
| blender-cinematic-scene | 3D | Blender 电影级场景生产循环（审美+迭代+导出） | https://github.com/HabrielStark/brilliant-blender-skill | MIT；2★；单文件高质量 | **引入** |

### 实质更新（已在建议引入）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| game-ui-design-workflow | **+product-design**；国风卡牌 RPG 示例升为主完整案例；工作流 7→8 skills；本仓已同步 `game-ui-workflow` | https://github.com/guiguiyan930-source/game-ui-design-workflow | 继续引入，优先试用 |
| worldwonderer/novel-to-game | Project Plateau 证据可验证性强化（★562） | https://github.com/worldwonderer/novel-to-game | 继续引入 |
| Hakhyun-Kim/agentic-gamedev-playbook | v1.30–1.31 韩文方法论（移动端/生成内容依赖） | https://github.com/Hakhyun-Kim/agentic-gamedev-playbook | 仍观望 |
| barrozo3d/unreal-sidekick | 继续采 Unreal Fest / Composure 稿 | https://github.com/barrozo3d/unreal-sidekick | 仍观望 |
| aigengame/godot-agent | balancing 公式/实验更新（★28） | https://github.com/aigengame/godot-agent | 仍观望（Godot 次优先） |

### 累计建议引入（仍有效）

1. https://github.com/gamedev-skills/awesome-gamedev-agent-skills — 411★  
2. https://github.com/kevinpbuckley/unreal-engine-skills — UE **5.8** retarget  
3. https://github.com/kevinpbuckley/VibeUE — 575★  
4. https://github.com/UnrealXu/UnrealEngine5-Skills — 492★  
5. https://github.com/quodsoler/unreal-engine-skills — 301★  
6. https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin — 171★  
7. https://github.com/db-lyon/ue-mcp — 245★  
8. https://github.com/figma/mcp-server-guide — 1850★  
9. https://github.com/anthropics/skills（frontend-design / canvas-design）  
10. https://github.com/abagames/agentic-gamedev-skills  
11. https://github.com/worldwonderer/novel-to-game — 562★  
12. https://github.com/cloudai-x/threejs-skills — 2900★  
13. https://github.com/winyunq/UnrealMotionGraphicsMCP  
14. https://github.com/dcc-mcp/dcc-mcp-unreal  
15. https://github.com/guiguiyan930-source/game-ui-design-workflow — **本轮实质更新**  
16. https://github.com/MRCalderon3D/everything-game-dev-code  
17. https://github.com/arjun988/blender-skills  
18. https://github.com/18163623522/ue-shader-skills  
19. https://github.com/mintdotgg/mint-threejs-skills  
20. **+ 本轮** design-game-ui / NiagaraSkill / brilliant-blender-skill  

## 观望（本轮新增）

| 名称 | 方向 | 一句话 | 仓库 | 原因 | 建议 |
|---|---|---|---|---|---|
| zhting/blender-skill | 3D | 效果图→Blender MCP 实现 | https://github.com/zhting/blender-skill | ★0；绑定 MCP；中文短 skill | 观望 |
| QuinsZouls/blender-skill | 3D | 通用 LLM↔Blender skill | https://github.com/QuinsZouls/blender-skill | ★0；内容薄 | 观望 |
| rksfn/blender_skills | 3D | 原型 prototyping 2 skills | https://github.com/rksfn/blender_skills | 无 license / ★0 | 观望 |
| ultras-vector-art-style | 2D | 足球 terraces/ultras 矢量插画风格 | https://github.com/w4n63r/ultras-vector-art-style | 今日新建；题材极窄 | 观望 |
| agent-skill-evolution-workflow | 工作流 | Skill 分类/冲突审计/进化交付 | https://github.com/Ivor-NCUT/agent-skill-evolution-workflow | 元工作流；非游戏向 | 观望 |
| davincidreams/agent-team-plugins | 3D | 3D 设计团队 skills（含 Blender/VRoid） | https://github.com/davincidreams/agent-team-plugins | 无 license；偏团队插件 | 观望 |
| hkuds/cli-anything | 3D·工具 | Blender/UnrealInsights CLI harness 切片 | https://github.com/hkuds/cli-anything | ★46k 巨仓；需摘切片再用 | 观望 |
| lisxa5747/unreal-angelscript-skills | UE | AngelScript skill（疑似镜像） | https://github.com/lisxa5747/unreal-angelscript-skills | ★0；与 flashpoint493 重叠 | 观望 |
| good-ui | UI | 现为 2 skills（含 bobby 变体） | https://github.com/grinchinc/good-ui | 仍偏 Web UI | 观望 |

其余观望（unreal-harness、Asset-Dump、Godot 向、Unity skills 等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 仍仅 star chore；mouadja02 仍为 Qdrant/Terraform（无关）  
- created:>2026-08-04 噪声约 **27**（新闻/股票/DePIN/办公/电商等）  
- Malik1942/product-film（录屏成片，非游戏/UE）  
- affaan-m/everything-claude-code、alvinunreal/oh-my-opencode-slim：巨仓/通用 harness，非本方向精选  

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 08-04：Qdrant / Terraform（无关） |

## 本仓入库变化（+4 → 68）

- 新增 `skills/ui-design/game-ui-product-design/`  
- 新增 `skills/ui-design/design-game-ui/`  
- 新增 `skills/unreal/niagara-json-generator/`  
- 新增 `skills/3d/blender-cinematic-scene/`  
- 更新 `skills/ui-design/game-ui-workflow/SKILL.md`（同步原仓）  
- 各含 `SOURCE.md`

## 今天可行动

1. **立刻试用**：装 `skills/ui-design/game-ui-product-design` + 已有 `game-ui-workflow`，用国风卡牌 RPG 示例跑「策划批准→再生图」。  
2. **互补对照**：同屏任务并行试 `design-game-ui`（实现/审计）与 `game-ui-*`（规范/生图交付），看哪套更贴你的 UMG 管线。  
3. **个人 skill 候选**：把 `game-ui-product-design` 的三文档门禁改成你项目的固定模板（GDD/PRD/interaction 路径与命名写死）。

## 已尝试查询

1. 种子仓 commits / meta API  
2. 跟踪仓 pushed_at / stars 增量对比（inventory 基线）  
3. `gh search repos`：unreal skills / unreal-engine-skills / gamedev agent skills / blender skill / threejs skills / game UI / UMG / Niagara / houdini / PCG / created:>2026-08-04 agent skills / 2D·UI design  
4. `gh search code`：filename SKILL.md Unreal（空/限流）；改用 `git/trees?recursive=1`  
5. skills.sh/api/search：unreal、gamedev、blender  
6. 新候选 raw SKILL.md 抽样 + CursorSkill 入库 / push / PR
