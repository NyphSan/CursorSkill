# 技能侦察 DIGEST — 2026-08-05

- 侦察时间：2026-08-05T02:03Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-04（06:04Z）
- 本仓入库：精选 **64** 个 `SKILL.md`（非整仓镜像），结构 `skills/<方向>/<skill-name>/`

## 本轮结论（一屏）

种子仓无方向相关新 skill。GitHub 侧新增/实质更新若干条：游戏 UI 工作流、多引擎设计脚手架、Blender 94 技能包、UE Shader 三件套、kevinpbuckley UE 技能 **retarget 至 5.8**。CursorSkill 写凭证已可用，本轮首次成功 push + 开 PR。

## 建议引入（本轮增量 + 累计入库）

### 本轮新增建议引入

| 名称 | 方向 | 一句话用途 | 仓库 | 关注点 | 建议 |
|---|---|---|---|---|---|
| game-ui-design-workflow | UI·游戏 | 游戏 UI 从规范→生图→切图→引擎交付的 Cursor Skills 工作流（7 skills） | https://github.com/guiguiyan930-source/game-ui-design-workflow | MIT；今日活跃；与方向高度契合 | **引入** |
| everything-game-dev-code | 游戏设计 | 多引擎游戏制作脚手架；含核心循环/手感/关卡等设计技能（100+ SKILL.md） | https://github.com/MRCalderon3D/everything-game-dev-code | MIT；65★；设计管线完整 | **引入** |
| blender-skills | 3D | 94 个 Blender 专家技能（建模/角色/环境/导出等） | https://github.com/arjun988/blender-skills | MIT；72★；可装 Cursor | **引入** |
| ue-shader-skills | UE | HLSL + UE Material + Niagara 三技能边界清晰 | https://github.com/18163623522/ue-shader-skills | MIT；星少但可装结构干净 | **引入** |
| mint-threejs-skills | 3D·游戏 | Three.js 游戏/应用指导（含 game-director） | https://github.com/mintdotgg/mint-threejs-skills | MIT；101★；依赖 Mint MCP | **引入** |

### 实质更新（已在建议引入）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| kevinpbuckley/unreal-engine-skills | **2026-08-04 retarget 全部技能至 UE 5.8**（★25 / 61 skills） | https://github.com/kevinpbuckley/unreal-engine-skills | 继续引入，优先同步 |
| kevinpbuckley/VibeUE | 5.8 / 蓝图联动修复（★575 / 35 skills） | https://github.com/kevinpbuckley/VibeUE | 继续引入 |
| db-lyon/ue-mcp | 1.1.44；编辑器启动卡死检测（★245 / 5 skills） | https://github.com/db-lyon/ue-mcp | 继续引入 |
| worldwonderer/novel-to-game | Project Plateau 证据门禁更新（★560 / 7 skills） | https://github.com/worldwonderer/novel-to-game | 继续引入 |
| figma/mcp-server-guide | Skills v2.2.90（★1850 / 14 skills） | https://github.com/figma/mcp-server-guide | 继续引入 |
| dcc-mcp/dcc-mcp-unreal | 0.2.17；MRQ 相机绑定修复（★2 / 19 skills） | https://github.com/dcc-mcp/dcc-mcp-unreal | 继续引入 |

### 累计建议引入（仍有效，已摘录入库）

1. https://github.com/gamedev-skills/awesome-gamedev-agent-skills — 411★ / ~67 skills  
2. https://github.com/kevinpbuckley/unreal-engine-skills  
3. https://github.com/kevinpbuckley/VibeUE  
4. https://github.com/UnrealXu/UnrealEngine5-Skills — 492★  
5. https://github.com/quodsoler/unreal-engine-skills — 301★  
6. https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin — 171★  
7. https://github.com/db-lyon/ue-mcp  
8. https://github.com/figma/mcp-server-guide  
9. https://github.com/anthropics/skills（frontend-design / canvas-design）  
10. https://github.com/abagames/agentic-gamedev-skills  
11. https://github.com/worldwonderer/novel-to-game  
12. https://github.com/cloudai-x/threejs-skills — 2900★  
13. https://github.com/winyunq/UnrealMotionGraphicsMCP  
14. https://github.com/dcc-mcp/dcc-mcp-unreal  
15. **+ 本轮 5 条**（上表）

## 观望（本轮新增/变化）

| 名称 | 方向 | 一句话 | 仓库 | 原因 | 建议 |
|---|---|---|---|---|---|
| unreal-harness | UE | ~300 Editor Actions + 22 skills 的全栈 harness | https://github.com/oliver-io/unreal-harness | 许可 NOASSERTION；绑 AWS/Neo4j 等重依赖 | 观望 |
| Unreal-MCP-Skills | UE | 中文向关卡/过场 MCP skills（3） | https://github.com/mMo66666/Unreal-MCP-Skills | 无 license / ★0 | 观望 |
| Asset-Dump | UE | uasset→可读文本 + Claude skill | https://github.com/KieranCoppins/Asset-Dump | ★0；工具向有用 | 观望 |
| titanforge-game-studio | UE·流程 | 里程碑门禁式制作流程 skills | https://github.com/Jumpsy/titanforge-game-studio | ★0 / 无 license | 观望 |
| XG-UE-Cpp-Course-Skill | UE | UE C++ 课程知识包 | https://github.com/liuhuagang/XG-UE-Cpp-Course-Skill | 课程向；60★ | 观望 |
| blender-skills-and-rules | 3D | VRoid/VRM 清理专用 | https://github.com/miramocha/blender-skills-and-rules | 细分场景 | 观望 |
| good-ui | UI | 通用 Web UI 反 slop skill | https://github.com/grinchinc/good-ui | 非游戏/UE；今日新建 ★0 | 观望 |
| agentic-gamedev-playbook | 游戏设计 | 韩文方法论持续迭代（今日 v1.31） | https://github.com/Hakhyun-Kim/agentic-gamedev-playbook | ★0；语言门槛 | 观望 |
| unreal-sidekick | UE | 影视/VFX 侧车知识（今日仍在采稿） | https://github.com/barrozo3d/unreal-sidekick | 结构单文件；持续观察 | 观望 |
| gisenberg/unreal-skills | UE | AngelScript/Build/P4 等 5 技能 | https://github.com/gisenberg/unreal-skills | ★0 | 观望 |
| claude-unreal-skills | UE | SOLID/复制架构 3 skills | https://github.com/toamig/claude-unreal-skills | ★0 | 观望 |
| UnrealSkills (petascale4) | UE | UAssetAPI 读写技能 | https://github.com/petascale4/UnrealSkills | ★0；工具链窄 | 观望 |

其余观望（Godot 向、Web UI 聚合等）维持昨日清单，不展开。

## 可忽略

- 种子仓 mouadja02/skills 今日新增：Qdrant / Terraform — 运维向，方向无关  
- JackyST0/awesome-agent-skills：仍仅 star chore，无游戏/UE 专区新增  
- created:>2026-07-28 的 agent-skills 噪声仓（DePIN/会议/股票等）约 20+，未入库  
- sickn33 镜像聚合、广告变现向 web-game-ad-skills 等维持忽略

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 08-04：Qdrant / Terraform（无关） |

## 本仓入库清单（64）

- `skills/ui-design/`：游戏 UI 工作流 7 + Figma 3 + Anthropic 2  
- `skills/unreal/`：UE 核心/UMG/MCP/Shader/VibeUE/Epic/UnrealXu/quodsoler/dcc 等  
- `skills/game-design/`：设计循环/手感/小说转游戏/gamedev router 等  
- `skills/3d/`：Blender 精选 + Three.js / Mint  
- 每个技能目录含 `SOURCE.md`（原仓链接）

## 今天可行动

1. **立刻试用**：把 `skills/ui-design/game-ui-workflow` 装进 Cursor，用一个真实 UI 屏跑「规范→生图→切图」闭环。  
2. **UE 5.8 对齐**：同步 `kevinpbuckley/unreal-engine-skills`（已 5.8 retarget）+ 本仓 `ue-gameplay-framework` / `ue-game-thread-performance`。  
3. **个人 skill 候选**：以 `game-ui-workflow` + `ue-shader-skills` 为骨架，改成你项目的「UMG 交付规范」私有 skill（命名/目录/审批门禁写死）。

## 已尝试查询

1. 种子仓 commits / meta API  
2. `gh search repos`：unreal skills / gamedev agent skills / unreal-engine-skills / blender skill / threejs skills / game UI / houdini / created:>2026-07-28 agent skills  
3. `gh search code`：filename SKILL.md（遇 429，改用 git trees）  
4. skills.sh/api/search：unreal、gamedev  
5. 候选 `git/trees?recursive=1` 定位 SKILL.md + raw 抽样  
6. CursorSkill push（本轮成功）+ open_git_pr
