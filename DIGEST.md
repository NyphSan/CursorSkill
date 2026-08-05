# 技能侦察 DIGEST — 2026-08-05（04:03Z）

- 侦察时间：2026-08-05T04:03Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T03:03Z（同日上一轮，PR#3）
- 本仓入库：精选 **73** 个 `SKILL.md`（较上轮 +5；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`cursor/bc-e015c769-10d5-4c44-af14-a313ebed520a-2026`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。跟踪「建议引入」仓无技能内容实质更新（`novel-to-game` 仅恢复 trailer/玩法链接）。**主增量**：新发现专用 UE Agent 框架仓 [JanVogelsang/UE-AgentFramework](https://github.com/JanVogelsang/UE-AgentFramework)（MIT，13×SKILL.md：Niagara/蓝图/Enhanced Input/PIE·UMG 验证等，依赖其 MCP）。今日新建噪声约 70+；方向擦边观望：`mechfaber-agent`（CAD）、`flowmock-skill`（流程低保真）、`famistudio-compose-skill`（NES 芯片音）。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| UE-AgentFramework（精选 5） | UE | Antigravity/MCP 驱动的 UE5 编辑器 Agent：Niagara、蓝图 T3D、Enhanced Input、PIE/UMG 验证 | https://github.com/JanVogelsang/UE-AgentFramework | MIT；13 个可定位 SKILL.md；与文档型 Niagara skill 互补（偏工具 SOP）；对齐 UE 5.8 | **引入** |

本仓已摘录：

- `skills/unreal/ue-af-niagara-authoring/`
- `skills/unreal/ue-af-blueprint-authoring/`
- `skills/unreal/ue-af-setup-input/`
- `skills/unreal/ue-af-pie-verifier/`
- `skills/unreal/ue-af-unreal-instructions/`（含作者本机路径，需改）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| worldwonderer/novel-to-game | 03:32Z 恢复 Project Plateau trailer/play link（#12）；非 skill 内容 | https://github.com/worldwonderer/novel-to-game | 继续引入，无新动作 |
| aigengame/godot-agent | `pushed_at` 有刷新，默认分支近提交仍为 08-03 balancing | https://github.com/aigengame/godot-agent | 仍观望 |
| guiguiyan930-source/game-ui-design-workflow | 仍停在 02:53Z（8 skills） | https://github.com/guiguiyan930-source/game-ui-design-workflow | 继续引入 |
| kevinpbuckley/unreal-engine-skills | 仍为 08-04 UE 5.8 retarget | https://github.com/kevinpbuckley/unreal-engine-skills | 继续引入 |

### 累计建议引入（仍有效）

1. https://github.com/gamedev-skills/awesome-gamedev-agent-skills  
2. https://github.com/kevinpbuckley/unreal-engine-skills — UE **5.8**  
3. https://github.com/kevinpbuckley/VibeUE  
4. https://github.com/UnrealXu/UnrealEngine5-Skills  
5. https://github.com/quodsoler/unreal-engine-skills  
6. https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin  
7. https://github.com/db-lyon/ue-mcp  
8. https://github.com/figma/mcp-server-guide  
9. https://github.com/anthropics/skills（frontend-design / canvas-design）  
10. https://github.com/abagames/agentic-gamedev-skills  
11. https://github.com/worldwonderer/novel-to-game  
12. https://github.com/cloudai-x/threejs-skills  
13. https://github.com/winyunq/UnrealMotionGraphicsMCP  
14. https://github.com/dcc-mcp/dcc-mcp-unreal  
15. https://github.com/guiguiyan930-source/game-ui-design-workflow  
16. https://github.com/MRCalderon3D/everything-game-dev-code  
17. https://github.com/arjun988/blender-skills  
18. https://github.com/18163623522/ue-shader-skills  
19. https://github.com/mintdotgg/mint-threejs-skills  
20. https://github.com/888wing/game-ui-skill  
21. https://github.com/zhijianfan/NiagaraSkill  
22. https://github.com/HabrielStark/brilliant-blender-skill  
23. **+ 本轮** https://github.com/JanVogelsang/UE-AgentFramework  

## 观望（本轮新增）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| mechfaber-agent | 3D·工作流 | 编码 Agent 设计真实机械（skill+MCP+求解器） | https://github.com/Argentron-Technologies/mechfaber-agent | 今日新建；LGPL；需账号；偏 CAD 非游戏 | 观望 |
| flowmock-skill | UI·工作流 | 从真实代码扫描流程 → 灰盒 lo-fi flow mock | https://github.com/yulonghe97/flowmock-skill | 今日新建；无 license；偏产品 UX | 观望 |
| famistudio-compose-skill | 游戏音频 | FamiStudio/NES 芯片乐谱驱动作曲与验收 | https://github.com/ROYIANS/famistudio-compose-skill | 今日新建；无 license；扩展音频向 | 观望 |
| a5c-ai/babysitter（game-development 切片） | 游戏·UE | 巨仓内含 unreal-* / blender / houdini 等百余游戏向 skill | https://github.com/a5c-ai/babysitter | ★1643；2112×SKILL；宜日后按主题摘切片 | 观望 |
| sonic7881963/gamedev-skills | 工作流·Godot | 分层 gamedev 工作流 + headless 测试 | https://github.com/sonic7881963/gamedev-skills | MIT；Godot 次优先 | 观望 |
| anatu/ios-gamedev-skills | 游戏·2D | iOS/SpriteKit 14 skills | https://github.com/anatu/ios-gamedev-skills | 无 license；非 UE 主线 | 观望 |

其余观望（unreal-harness、cli-anything、Godot/Unity 向、blender 薄仓等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 仍仅 08-03 star chore；mouadja02 仍为 Qdrant/Terraform（无关）  
- created:>2026-08-04 / 今日新建噪声约 **70+**（社交/法律/健身/GitHub 练习题/空仓等）  
- aurora1112-j/visual-essay-illustrator-skill：描述像 2D，但仓库为空  
- chris58530/gamedev-skills：仅 prompts，无 `SKILL.md`  
- ComeOnOliver/skillshub / majiayu000/claude-skill-registry：镜像聚合巨仓，不整仓收录  

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 08-04：Qdrant / Terraform（无关） |

## 本仓入库变化（+5 → 73）

- 新增 `skills/unreal/ue-af-niagara-authoring/`  
- 新增 `skills/unreal/ue-af-blueprint-authoring/`  
- 新增 `skills/unreal/ue-af-setup-input/`  
- 新增 `skills/unreal/ue-af-pie-verifier/`  
- 新增 `skills/unreal/ue-af-unreal-instructions/`  
- 各含 `SOURCE.md`；承接上轮 68 条精选内容  

## 今天可行动

1. **立刻试用**：装 `skills/unreal/ue-af-pie-verifier` + 已有 `game-ui-*`，用 PIE/UMG 抽取验证一条 HUD 交互（需能连 UE MCP）。  
2. **对照 Niagara**：同任务并行试 `ue-af-niagara-authoring`（MCP SOP）与已入库 `ue-niagara-authoring`/`niagara-json-generator`（文档/JSON 管线），看哪套贴你的 VFX 工具链。  
3. **个人 skill 候选**：把 `ue-af-unreal-instructions` 的本机路径段改成你的 UE 5.x 安装与 `.uproject`，作为固定入口 skill。

## 已尝试查询

1. 种子仓 commits / meta API  
2. 跟踪「建议引入/观望」仓 `pushed_at` / stars 增量对比  
3. `gh search repos`：unreal/gamedev/blender/threejs/game UI/UMG/Niagara/PCG；`created:>2026-08-04`；`created:>2026-08-05T03:00:00Z skill`  
4. `gh search code`：filename SKILL.md + Unreal/UE5（部分 429）；`git/trees?recursive=1` 核验  
5. skills.sh/api/search：unreal、gamedev、blender  
6. 新候选 raw SKILL.md 抽样 + CursorSkill 入库 / push / PR  
