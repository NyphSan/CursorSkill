# 技能侦察 DIGEST — 2026-08-13（每日 cron 11:04+08:00）

- 侦察时间：2026-08-13T11:04+08:00（自动化 cron）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：远端 `CursorSkillSearch` commit `c7b644e`（305 SKILL；08-12 已 push）
- 本仓入库：精选 **307** 个 `SKILL.md`（相对 305：+2 新增）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

种子仓无方向相关新增（JackyST0 仍仅 star chore / mouadja02 GraphQL preflight，方向无关）。本轮抓到 2 条 **近 7 天新发现或首次定位到 SKILL.md** 的相关条目：
- `Leonxlnx/taste-skill`（**新见引入**）：MIT，~73.9k★ / ~5.06k forks / 今日 +720 stars，13 个 SKILL.md（10 代码 + 3 image-gen），v2 在 08-07 重写并引入 VARIANCE/MOTION/DENSITY 三旋钮；与 nextlevelbuilder-ui-ux-pro-max（08-11 引入）完全互补（检索驱动 vs 规则约束）
- `haxqer/godot-skill`（**新见引入**）：MIT（08-11 添加），最后 commit 2026-08-11 `b4d0e38`，覆盖 Godot 4.7（兼容 4.x）的场景/资源/项目事务式编辑、TileSet/TileMapLayer/SpriteFrames/AnimationPlayer 内容制作、2D+3D navmesh 烘焙、headless 调试、GUT/GdUnit4 测试、多端导出；2D game design 主链的实质性补充

## 建议引入（本轮增量 = 2 新增）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| leonxlnx-taste-skill | UI·2D（游戏 UI 间接） | 13 个 portable anti-slop Agent Skills：v2 设计规则 + gpt-taste 严苛版 + redesign 旧项目重构 + high-end-soft + minimalist + brutalist + image-to-code + output-enforcement + 3 个 image-gen | https://github.com/Leonxlnx/taste-skill | MIT；~73.9k★（今日 +720）；13 子技能单职责；v2 experimental 但 churn 是 frontmatter 维度；与 nextlevelbuilder 形成"代码约束 vs 风格数据库"完美互补 | **引入**（已摘录 13 子技能名称 + 三旋钮 + 互补矩阵） |
| haxqer-godot-skill | 游戏设计·2D·3D | Godot 4.7 portable skill：transactional 场景/资源/项目编辑、TileSet+TileMapLayer 自 autotile、SpriteFrames atlas 切分、AnimationPlayer/AnimationTree、Theme、2D+3D navmesh 烘焙、CSG 碰撞、glTF 导出、headless 调试、GUT/GdUnit4 测试、Android/iOS/Web/Win/Linux/macOS/dedicated server/visionOS 导出 | https://github.com/haxqer/godot-skill | MIT（08-11 添加）；08-11 merge `feat/godot-authoring-ops`（3D/theme/navmesh 实质性）；9 个 test suite 全绿；Co-Authored-By Claude 标记说明维护者在用 AI 共创，frontmatter/ops 可能在演化 | **引入**（已摘录 4 类能力面 + 9 references 摘要 + 互补矩阵 + sharp edges） |

本仓路径：
- `skills/ui-design/leonxlnx-taste-skill/`（SKILL.md + SOURCE.md）
- `skills/game-design/haxqer-godot-skill/`（SKILL.md + SOURCE.md）

## 观望（本轮维持 / 微调）

- fagemx 其余约 17 项（game-direction / ideation / pitch-review…）— 上轮已摘 12，本轮未动
- abagames/agentic-gamedev-skills — 仍是 MIT 12★、08-09 增量小游戏/Godot/Web（与 godot-skill 部分重叠但体量小）
- educlopez/ui-craft — v1.0.18 之后无新动向
- MengTo/Skills threejs-scroll-world 等 — 仍偏 Web demo，与 UE 主链不重叠
- Yuki001/game-dev-skills — **仍无 LICENSE**，维持观望
- SummerEngine/summer-engine-agent — 维持
- Randroids / NAJEM / mike007jd / alfaris / Shellishack — 维持
- opengameapp/OpenGame-skills — 维持低优
- kevinpbuckley/VibeUE — 同作者 MCP 层；等 kevinpbuckley-unreal-engine-skills 跑通后再决定是否补剩余约 32 个 SKILL.md
- affaan-m/everything-claude-code/blender-motion-state-inspection — Blender 角色/绑定/动画检查，范围窄，本轮观望
- dcc-mcp-skills-creator — DCC-MCP 技能包创建工具，基建向，本轮观望
- **addyyosmani/agent-skills** — 76k★ / 08-11 commit `be42637`（SessionStart envelope）；24 个 SKILL 中 `frontend-ui-engineering` 与 UI 设计主向相关，但与 nextlevelbuilder/taste-skill 重叠定位；不直接入库
- **MCPBlender/blender-mcp** — 25.6k★ / 08-03 commit；是 MCP server 而非 SKILL package；与 dcc-mcp-blender 互补，但范畴不在本任务
- **EpicLolia/UnrealPythonMCP** — 08-09 发布；TypeScript UE Python MCP；MCP server，非 SKILL
- **virgiliojr94/book-to-skill** — 7,750★；将 PDF 转 SKILL.md；基建向，与游戏/UE/3D/UI 主向弱相关，本轮观望
- **Matt Pocock skills（TypeScript 巫师）** — 30.8k★，个人 .claude 公开，方向是反氛围编程 + TDD/PRD；与游戏主向不重叠
- **reverse-skill** — 19.6k★ / 2.7k forks；安全逆向向；与方向无关

## 可忽略

- 种子：JackyST0/awesome-agent-skills 仍仅 star chore；mouadja02/skills 08-12 GraphQL preflight，方向无关
- 新建技能仓仍以 GitHub Skills 练习 / 作品集 / 合规 / 招聘 / WhatsApp 噪声为主
- 作弊 / 外挂 / 电竞陪玩类一律忽略

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | ~616+ | 仍仅 star chore（08-10） | 无 UE / 游戏专区新增 |
| mouadja02/skills | ~9 | 08-12 GraphQL incremental hydration preflight | **方向无关**（API/backend） |

## 今天可行动

1. **前端/UI 工作流三件套补齐**：今天 `leonxlnx-taste-skill`（anti-slop 规则）+ 既有的 `nextlevelbuilder-ui-ux-pro-max`（84 风格 / 192 调色板数据库）= "规则约束 + 检索查找" 的 UI 双引擎；可立即装：`npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend`
2. **Godot 项目自动化**：`haxqer/godot-skill` 是 Godot 4.7 当前最完整的 portable 技能包，clone `skill/godot/` 即可；如果你做 Godot 项目，配 `heycat-isometric-*`（既有）是 isometric pipeline 的搭配
3. **若做 UE 项目**：继续用 `kevinpbuckley-unreal-engine-skills`（广）+ `quodsoler-unreal-engine-skills`（深）双保险；今天没什么新 UE SKILL，UE 生态在 8 月初相对安静

## 查询记录

1. 种子仓：JackyST0（仍 star chore）/ mouadja02（08-12 GraphQL preflight）— 方向无关
2. WebSearch 查询（d7 窗口）：
   - `GitHub "SKILL.md" Unreal Engine UE5 game design C++ animation rendering 2026-08`
   - `GitHub repository SKILL.md 3D Blender Maya Houdini Substance designer agent skill August 2026`
   - `GitHub SKILL.md UI design frontend design system workflow agent skill 2026-08`
   - `GitHub "SKILL.md" game design mechanics GDD level design narrative design 2026-08`
   - `GitHub dcc-mcp new plugin Unreal Maya Houdini Substance August 2026`
   - `Leonxlnx taste-skill design-taste-frontend soft minimalist brutalist premium frontend framework`
   - `path:.cursor/skills unreal engine OR game OR 3D OR "agent skill" 2026-08 new repo`
   - `site:github.com "SKILL.md" unreal engine niagara animation render new repository August 2026`
   - `site:github.com "SKILL.md" Blender Substance Painter procedural texture 2026 2025 new`
   - `site:github.com "SKILL.md" cursor agent skill packaging ci/cd game design Unreal 2026`
   - `github repository "SKILL.md" "Godot" OR "godot4" OR "unity" 2D pixel art tilemap agent skill August 2026`
   - `github SKILL.md "asset creation" OR "Blender" OR "Substance" OR "Houdini" OR "MCP" 3D art agent skill new 2026-08`
   - `github "SKILL.md" Quest Dialogue Level Narrative design game mechanics August 2026`
   - `github repository Unreal Engine 5.7 5.8 SKILL.md MCP gameplay C++ new August 2026 toolset`
3. WebFetch 候选原仓：
   - github.com/Leonxlnx/taste-skill（MIT / ~73.9k★ / 13 SKILL / v2 实验）
   - github.com/haxqer/godot-skill（MIT 08-11 / 12 commit / Godot 4.7 / 9 suite 全绿）
   - github.com/addyosmani/agent-skills（MIT / 76k★ / 24 SKILL / 08-11 hooks 提交）
   - github.com/Leonxlnx/taste-skill/tree/main（确认 13 子技能文件夹）
   - github.com/MCPBlender/blender-mcp（mcp server 而非 SKILL package）
4. 候选去重：对照本仓 `skills/ui-design/` `skills/game-design/`，确认以上 2 个（leonxlnx-taste-skill / haxqer-godot-skill）均无重复
5. 入库：+2 → commit `CursorSkillSearch`（本日 commit 待 push）

## 遗留问题

- 08-12 commit `c7b644e` 已成功 push（08-12 修复了 credential helper selector 阻塞）
- 本轮 commit 将叠加在 `c7b644e` 之上，push 时继续使用 `git -c credential.helper= -c credential.helper=manager push origin CursorSkillSearch`
- push 修复方案：仍然使用上次 08-12 的 fix（不重新挂起 selector）
- gh CLI（2.97.0）可用：可继续用 `gh pr list --head CursorSkillSearch` 复用 PR #31
