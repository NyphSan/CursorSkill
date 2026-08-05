# 技能侦察 DIGEST — 2026-08-05（05:04Z）

- 侦察时间：2026-08-05T05:04Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T04:03Z（同日上一轮，PR#4）
- 本仓入库：精选 **78** 个 `SKILL.md`（较上轮 +5；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`cursor/bc-dffa4ae6-0cf5-43c6-afc1-01a6006e2c3b-366a`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。跟踪 UE 主仓无新 skill 内容；`novel-to-game` / `game-ui-design-workflow` 无新提交。**主增量**：今日新建 [fenggezaici/dcc-python-skills](https://github.com/fenggezaici/dcc-python-skills)（Maya 2024 + Houdini 20.5 Python 官方文档型 skill，可安装）。补录此前未入库的策划向 [w-zhian/game-design-skills](https://github.com/w-zhian/game-design-skills)（精选 2）与 [Hanjo92/roguelike-game-designer-skill](https://github.com/Hanjo92/roguelike-game-designer-skill)。今日新建噪声约 40+；CAD 向 `mechfaber-agent` 升至 0.1.1，仍观望。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| maya-2024-python-commands | 3D·工作流 | Maya 2024.2 `maya.cmds` 命令/参数/示例速查入口 | https://github.com/fenggezaici/dcc-python-skills | 今日新建；结构清晰可安装；补齐 DCC→UE 管线缺口 | **引入** |
| houdini-20-5-python-scripting | 3D·工作流 | Houdini 20.5 HOM/`hou` 脚本与 Python SOP/COP 参考入口 | https://github.com/fenggezaici/dcc-python-skills | 同上；对程序化/特效管线直接可用 | **引入** |
| gameplay-design | 游戏设计 | 核心循环/决策密度 GATE 的玩法设计工作流 | https://github.com/w-zhian/game-design-skills | 8×SKILL 策划包；与已有 core-loop 互补；中英触发词 | **引入** |
| numerical-planning | 游戏设计 | 数值/成长曲线/经济流分析（不做最终配表） | https://github.com/w-zhian/game-design-skills | 填补本仓数值策划空白 | **引入** |
| roguelike-game-designer | 游戏设计 | Roguelike/Roguelite 族专用设计 skill（跑局/程序生成/平衡） | https://github.com/Hanjo92/roguelike-game-designer-skill | 单文件高密度；frontmatter MIT；品类深 | **引入** |

本仓已摘录：

- `skills/3d/maya-2024-python-commands/`
- `skills/3d/houdini-20-5-python-scripting/`
- `skills/game-design/gameplay-design/`
- `skills/game-design/numerical-planning/`
- `skills/game-design/roguelike-game-designer/`

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| worldwonderer/novel-to-game | 仍为 03:32Z trailer 链接恢复；无新提交 | https://github.com/worldwonderer/novel-to-game | 继续引入 |
| guiguiyan930-source/game-ui-design-workflow | 仍停在 02:53Z（8 skills，已入库） | https://github.com/guiguiyan930-source/game-ui-design-workflow | 继续引入 |
| kevinpbuckley/unreal-engine-skills | 仍为 08-04 UE 5.8 retarget | https://github.com/kevinpbuckley/unreal-engine-skills | 继续引入 |
| JanVogelsang/UE-AgentFramework | 无新推送（仍 07-30） | https://github.com/JanVogelsang/UE-AgentFramework | 继续引入，盯插件可用性 |
| Argentron-Technologies/mechfaber-agent | 04:33Z → 0.1.1；补安装/授权说明 | https://github.com/Argentron-Technologies/mechfaber-agent | 仍观望（CAD） |

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
23. https://github.com/JanVogelsang/UE-AgentFramework  
24. **+ 本轮** https://github.com/fenggezaici/dcc-python-skills  
25. **+ 本轮** https://github.com/w-zhian/game-design-skills  
26. **+ 本轮** https://github.com/Hanjo92/roguelike-game-designer-skill  

## 观望（本轮新增 / 更新）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| miramocha/blender-skills-and-rules | 3D | VRoid/VRM 清理：shapekey、骨骼、MToon、UV | https://github.com/miramocha/blender-skills-and-rules | 11×SKILL；无 license；偏虚拟形象细分 | 观望 |
| NexTechFusion/media4agents-threejs-skills | 3D·游戏 | Three.js 程序化世界 / 视觉 QA / img2threejs | https://github.com/NexTechFusion/media4agents-threejs-skills | 08-03 新建；0★；无 license；与 mint/cloudai 重叠 | 观望 |
| mechfaber-agent（更新） | 3D·工作流 | 编码 Agent 设计真实机械（skill+MCP） | https://github.com/Argentron-Technologies/mechfaber-agent | 本轮升 0.1.1；仍需账号；偏 CAD | 观望 |

其余观望（babysitter 游戏切片、flowmock、famistudio、sonic7881963、anatu iOS、unreal-harness、cli-anything、Godot/Unity 向等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 仍仅 08-03 star chore；mouadja02 仍为 Qdrant/Terraform（无关）  
- `created:>2026-08-05` 今日新建噪声约 **40+**（技能练习题、外贸背调、PPT、读图、短剧提示词、GitHub 练习等）  
- Dashuwang/zijiren-prompt-skill：AI 短剧提示词，非游戏/UE 主线  
- yongchaozhao640-crypto/image-reader-skill：通用读图，方向无关  
- zhouwei251550334/hippt：演示文稿 skill  
- ComeOnOliver/skillshub / majiayu000/claude-skill-registry：镜像聚合，不整仓收录  

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 08-04：Qdrant / Terraform（无关） |

## 本仓入库变化（+5 → 78）

- 新增 `skills/3d/maya-2024-python-commands/`  
- 新增 `skills/3d/houdini-20-5-python-scripting/`  
- 新增 `skills/game-design/gameplay-design/`  
- 新增 `skills/game-design/numerical-planning/`  
- 新增 `skills/game-design/roguelike-game-designer/`  
- 各含 `SOURCE.md`；承接上轮 73 条精选内容  

## 今天可行动

1. **立刻试用**：把 `maya-2024-python-commands` / `houdini-20-5-python-scripting` 装进 Cursor skills，用一条「导出 FBX/USD → UE」脚本题验证 DCC 入口是否好用（原仓还有 chapters，需要时再拉）。  
2. **策划双开**：同题并行 `gameplay-design`（决策密度 GATE）+ 已有 `core-loop-design`，再丢给 `numerical-planning` 做成长/经济审计。  
3. **个人 skill 候选**：若你做 Roguelite，把 `roguelike-game-designer` 裁成「你的品类支柱 + 跑局验收清单」个人版；DCC 两 skill 建议保留原仓链接、只改激活描述贴合你的 Maya/Houdini 版本。

## 已尝试查询

1. 种子仓 commits / meta API  
2. 跟踪「建议引入/观望」仓 `pushed_at` / stars / commits 增量对比  
3. `gh search repos`：unreal/gamedev/blender/threejs/game UI/UMG/Niagara/houdini/maya/roguelike；`created:>2026-08-04`；`created:>2026-08-05T00:00:00Z skill`；`created:>2026-08-05T04:00:00Z`  
4. `gh search code`：filename SKILL.md + Unreal（本轮空/限流）；`git/trees?recursive=1` 核验  
5. skills.sh/api/search：unreal、gamedev  
6. 新候选 raw SKILL.md 抽样 + CursorSkill 入库 / push / PR  
