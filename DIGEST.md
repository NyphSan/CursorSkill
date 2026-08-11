# 技能侦察 DIGEST — 2026-08-12（每日 cron 01:00+08:00）

- 侦察时间：2026-08-12T01:00+08:00（自动化 cron）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：本地 `CursorSkillSearch` 2026-08-11 commit `37b71f5`（302 SKILL；上轮 push 未成功，远端仍停留在 `b5be267`）
- 本仓入库：精选 **305** 个 `SKILL.md`（相对 302：+3 新增 + 1 实质更新）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

种子仓仍无方向相关新增。本轮抓到 4 条 **08-07 → 08-11 期间新出现或首次定位到 SKILL.md** 的相关条目：
- `dcc-mcp/dcc-mcp-agent-plugins`（**新见引入**）：MIT-0，统一 DCC 控制层覆盖 Unreal/Blender/Maya/Houdini/3ds Max/Nuke/Photoshop/Godot/Substance/RenderDoc，v0.19.92，安全等级 A，多 agent 兼容（含 WorkBuddy/CodeBuddy）
- `dcc-mcp/dcc-mcp-blender`（**新见引入**）：MIT，Blender 4.2+ 嵌入式 MCP 服务器，200+ 工具 / 29 类别，CI 测试矩阵覆盖 Win/Linux/macOS
- `QwenLM/Qwen-MM-Plugins`（**新见引入**）：Apache-2.0，08-10 发布，Blender 22 工具 + FreeCAD 14 工具 + 3D 模型读取 + 视频编辑，~1.6k★
- `quodsoler/unreal-engine-skills`（**实质更新**）：MIT，27 个 UE5 C++ 技能，源码审计修正 160+ 处不准确，与 kevinpbuckley 互补；已在仓内（commit 9dba7bd），本轮更新 SKILL.md 内容

种子仓 mouadja02/skills 08-11 有 commit（docs 目录更新），但方向无关。

## 建议引入（本轮增量 = 3 新增 + 1 实质更新）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| dcc-mcp | 研发工作流·UE·3D | 统一 DCC 控制层：10+ DCC 应用（Unreal/Blender/Maya/Houdini/3ds Max/Nuke/Photoshop/Godot/Substance/RenderDoc）通过 CLI 或 MCP gateway 操控 | https://github.com/dcc-mcp/dcc-mcp-agent-plugins | MIT-0；v0.19.92（08-07）；安全等级 A；明确支持 WorkBuddy/CodeBuddy 安装；3 个 skill（dcc-mcp/dcc-mcp-creator/dcc-mcp-skills-creator） | **引入**（已摘录路由表 + 五步流程 + 安装命令） |
| dcc-mcp-blender | 3D | Blender 4.2+ 嵌入式 MCP 服务器，200+ 预构建工具 / 29 类别（建模/材质/灯光/渲染/绑定/动画/物理/几何节点/导出/验证/管线） | https://github.com/dcc-mcp/dcc-mcp-blender | MIT；v0.1.43；Blender Extension 格式；CI 测试 Win/Linux/macOS × Blender 4.3.2/4.4.3；与 dcc-mcp 主 skill 互补 | **引入**（已摘录 29 类工具概要 + 安装方式） |
| qwen-mm-plugins-blender | 3D·研发工作流 | 阿里 Qwen 多模态插件套件 Blender 能力：22 工具驱动运行中 Blender（建模/材质/灯光/渲染），uvx 按需启动 | https://github.com/QwenLM/Qwen-MM-Plugins | Apache-2.0；08-10 发布；~1.6k★；9 个 agent 平台兼容；uvx 依赖隔离；套件另有 FreeCAD/video-edit/video-memory 能力 | **引入**（已摘录架构 + 工具概要 + 安装方式） |
| quodsoler-unreal-engine-skills | UE | 27 个 UE5 C++ 技能，源码审计修正 160+ 处不准确（函数签名/不存在方法/已弃用 API），覆盖 Core/Gameplay/Rendering/World/AI/UI/Build | https://github.com/quodsoler/unreal-engine-skills | MIT；ue-project-context 跨引用机制；与 kevinpbuckley（61 SKILL 广覆盖）互补：quodsoler（27 SKILL 深审计）；**本轮实质更新 SKILL.md 内容** | **引入**（已更新摘录 27 技能分类 + 安装方式 + 对比表） |

本仓路径：
- `skills/workflow/dcc-mcp/`（SKILL.md + SOURCE.md）
- `skills/3d/dcc-mcp-blender/`（SKILL.md + SOURCE.md）
- `skills/3d/qwen-mm-plugins-blender/`（SKILL.md + SOURCE.md）
- `skills/unreal/quodsoler-unreal-engine-skills/`（SKILL.md + SOURCE.md）

## 观望（本轮维持 / 微调）

- fagemx 其余约 17 项（game-direction / ideation / pitch-review…）— 上轮已摘 12，本轮未动
- abagames/agentic-gamedev-skills — 仍是 MIT 12★、08-09 增量小游戏/Godot/Web
- educlopez/ui-craft — v1.0.18 之后无新动向
- MengTo/Skills threejs-scroll-world 等 — 仍偏 Web demo，与 UE 主链不重叠
- Yuki001/game-dev-skills — **仍无 LICENSE**，维持观望
- SummerEngine/summer-engine-agent — 维持
- Randroids / NAJEM / mike007jd / alfaris / Shellishack — 维持
- opengameapp/OpenGame-skills — 维持低优
- kevinpbuckley/VibeUE — 同作者 MCP 层；等 kevinpbuckley-unreal-engine-skills 跑通后再决定是否补剩余约 32 个 SKILL.md
- affaan-m/everything-claude-code/blender-motion-state-inspection — Blender 角色/绑定/动画检查，范围窄，本轮观望
- dcc-mcp-skills-creator — DCC-MCP 技能包创建工具，基建向，本轮观望

## 可忽略

- 种子：JackyST0/awesome-agent-skills 仍仅 star chore（08-10）；mouadja02/skills 08-11 docs 更新，方向无关
- 新建技能仓仍以 GitHub Skills 练习 / 作品集 / 合规 / 招聘 / WhatsApp 噪声为主
- 作弊 / 外挂 / 电竞陪玩类一律忽略

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | ~616 | 仍仅 star chore（08-10） | 无 UE / 游戏专区新增 |
| mouadja02/skills | ~9 | 08-11 docs 目录更新 | 本轮有 commit，**方向无关** |

## 今天可行动

1. **安装 dcc-mcp 主 skill**：`npx --yes skills@1.5.22 add dcc-mcp/dcc-mcp-agent-plugins --skill dcc-mcp` — 一次搞定 Unreal/Blender/Maya/Houdini 等 10+ DCC 应用的统一 AI 控制
2. **Blender 3D 工作流二选一**：重量级用 `dcc-mcp-blender`（200+ 工具，Blender Extension 原生集成）；轻量级用 `qwen-mm-plugins-blender`（22 工具，uvx 按需启动，套件协同）
3. **UE5 C++ 双保险**：`kevinpbuckley`（61 SKILL 广覆盖）+ `quodsoler`（27 SKILL 源码审计）组合使用，广度+深度互补

## 查询记录

1. 种子仓：JackyST0（08-10 star chore）/ mouadja02（08-11 docs 更新）— 方向无关
2. WebSearch 查询：
   - `GitHub SKILL.md "agent skills" Unreal Engine UE5 game design 2026`（d7）
   - `GitHub ".cursor/skills" OR ".agents/skills" SKILL.md 3D design UI design workflow 2026`（d7）
   - `GitHub "SKILL.md" game design Unreal blueprint niagara gameplay agent skill`（d7）
   - `GitHub agent skills "3D" "Blender" OR "Maya" OR "Houdini" SKILL.md 2026`（d7）
   - `site:github.com SKILL.md unreal engine game dev workflow 2026`
   - `GitHub "dcc-mcp" OR "dcc mcp" skill Unreal Blender Maya Houdini SKILL.md 2026`（d7）
3. WebFetch 候选原仓：
   - github.com/dcc-mcp/dcc-mcp-agent-plugins（MIT-0 / v0.19.92 / 3 skills / 08-07）
   - github.com/dcc-mcp/dcc-mcp-blender（MIT / v0.1.43 / 200+ tools / 29 categories）
   - github.com/QwenLM/Qwen-MM-Plugins（Apache-2.0 / 08-10 发布 / ~1.6k★ / 8 capabilities）
   - github.com/quodsoler/unreal-engine-skills（MIT / 27 skills / 源码审计 160+ 修正）
4. 候选去重：对照本仓 `skills/unreal/` `skills/3d/` `skills/workflow/`，确认以上 4 个均无重复
5. 入库：+4 → commit `CursorSkillSearch`（待 push；上轮 08-11 commit `37b71f5` 仍未 push 到远端）

## 遗留问题

- 08-11 commit `37b71f5`（6 条引入）因 git credential helper selector 交互式挂起，**仍未 push 到远端**
- 本轮 commit 将叠加在 `37b71f5` 之上，push 时一并推送
- 根因：全局 `credential.helper = helper-selector` + `credential.helperselector.selected = <no helper>` 在非交互 shell 下触发 `git config --system -e` 永久挂起
- 本轮尝试：用 `git -c credential.helper= -c credential.helper=manager` 覆盖 selector
