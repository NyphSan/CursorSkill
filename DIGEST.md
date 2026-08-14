# 技能侦察 DIGEST — 2026-08-15（每日 cron 00:55+08:00）

- 侦察时间：2026-08-15T00:55+08:00（自动化 cron）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：远端 `CursorSkillSearch` commit `49c3310`（310 SKILL；08-14 已 push）
- 本仓入库：精选 **312** 个 `SKILL.md`（相对 310：+2 新增）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

种子仓无方向相关新增（JackyST0 仍仅 star chore / mouadja02 08-12 commit 后无新动作）。GitHub 近 7 天窗口内，游戏/UE/3D/UI 方向新增条目稀少。本轮完成上一轮遗留计划并补充一个独立新仓库：

1. **`NVIDIA/skills/omniverse-realtime-viewer`** — NVIDIA 官方，Apache-2.0，v0.1.0，上一轮计划摘取项；补齐「产出 / 优化 / 查看」三件套中的 viewer 端，强制 ovrtx-only、禁止浏览器端 3D 渲染器 fallback。
2. **`NVIDIA/simready-foundation`（新定位仓库）** — 2026-08-04 Release 2026.06.0，Apache-2.0；本轮先摘取其 `simready-foundation-conform-fet-000-core`，用于修复 USD 资产的 Core 命名/布局/路径/prim 问题，作为 UE Interchange USD 导入前的上游清洗步骤。

## 建议引入（本轮增量 = 2 新增）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| nvidia-omniverse-realtime-viewer | 3D（主向）/ 研发工作流 | NVIDIA 官方 Omniverse Realtime Viewer 顶层路由：按交付路径（browser-streamed / local / Tauri / Electron / native）选择参考文档，实现 USD 渲染、UI 交互、流式传输与验证；强制 `ovrtx` 用于所有 USD/3D 渲染，禁止 WebGL/Three.js/Babylon 等浏览器端 fallback | https://github.com/NVIDIA/skills/tree/main/skills/omniverse-realtime-viewer | Apache-2.0；v0.1.0；与已入库 `nvidia-omniverse-cad-to-simready` / `nvidia-omniverse-usd-performance-tuning` 构成「产出 → 优化 → 查看」完整链路；对需要 USD review/数字孪生/synthetic-data 检视的团队有直接价值 | **引入**（已摘录 Non-Negotiables + Read Order + Build Workflow + Completion Checklist） |
| nvidia-simready-foundation-conform-fet-000-core | 3D（主向）/ 研发工作流 | NVIDIA SimReady Foundation 核心 conform 技能：将 USD 资产修复为 FET000_CORE 规范，覆盖命名、布局、未解析路径、未定义 prim 失败；staging 输出，不静默修改源资产 | https://github.com/nvidia/simready-foundation/tree/main/skills/simready-foundation-conform-fet-000-core | Apache-2.0；2026.06.0 发布（2026-08-04）；新发现的独立仓库，补全「CAD → USD → conform → engine」链路中 conform 一环；对 UE 5.2+ Interchange USD 导入前的资产清洗有直接帮助 | **引入**（已摘录 Purpose + Inputs + Repair Checklist + Repair/Block Policy + Summary Format） |

本仓路径：
- `skills/3d/nvidia-omniverse-realtime-viewer/`（SKILL.md + SOURCE.md）
- `skills/3d/nvidia-simready-foundation-conform-fet-000-core/`（SKILL.md + SOURCE.md）

## 观望（本轮新增 / 维持）

- **NVIDIA/simready-foundation 其余 skills** — 同仓库还有 `simready-foundation-add-*` / `simready-foundation-update-*` / `simready-foundation-conform-fet-003/004/006` / `simready-foundation-create-package` / `simready-foundation-validate-foundation-change` 等；本轮只摘最高频的 Core conform，其余待后续分批评估。
- **NVIDIA/skills physical-ai 系列** — `physical-ai-infrastructure-setup-and-resilient-scaling` / `physical-ai-neural-reconstruction` / `physical-ai-defect-image-generation` / `physical-ai-people-attribute-search` / `physical-ai-video-data-augmentation`；与游戏/UE 主向关联较弱，维持观望。
- **Yuki001/game-dev-skills** — 08-12 新增 `lucida-remove-background`，08-13 连续 small fix；**仍无 LICENSE**，维持观望。
- **John-Sun27/creating-game-combat-vfx** — 中文 2D 战斗特效 Skill（MIT），最后 commit 2026-07-20，非近 7 天更新；方向相关但不在本轮新增窗口，纳入后续评估。
- **mike007jd/game-superpowers** — 游戏设计/UX/UI/2D Web 技能包（MIT），最后 commit 2026-04-17；非近 7 天更新，纳入后续评估。
- **Sttrevens/4dgames-skills** — 游戏制作/Steam 商业/Agent 运维技能索引（MIT），最后 commit 2026-07-10；非近 7 天更新，纳入后续评估。
- **abagames/agentic-gamedev-skills** — 08-09 仅维护性 commit（脚本/规则/文档修正，修复两个 skill 描述语气），无新增 skill；维持观望。
- **gamedev-skills/awesome-gamedev-agent-skills** — 本仓已覆盖大部分；剩余 15 Godot / 8 Unity / 6 Web / 5 Other-Engine 未单独入库。

## 可忽略

- 种子仓：JackyST0 仍仅 star chore；mouadja02 08-12 后无方向相关动作。
- NVIDIA/skills 08-11 ~ 08-14 的 commit 以元数据再生、索引刷新、CI 配置、组件注册（Warp / DeepStream）和 orphan pruning 为主；无新增游戏/UE/3D/UI 相关 skill。
- 新建技能仓仍以 GitHub Skills 练习 / 作品集 / 合规 / 招聘 / WhatsApp 噪声为主。
- 作弊 / 外挂 / 电竞陪玩类一律忽略。

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | ~616+ | 仍仅 star chore（08-10） | 无 UE / 游戏专区新增 |
| mouadja02/skills | ~9 | 08-12 `feat(api-backend): GraphQL incremental hydration preflight` | 方向无关（后端 API） |

## 今天可行动

1. **补完 NVIDIA Omniverse 链路**：若已有 CAD → SimReady USD 产出，用 `nvidia-omniverse-realtime-viewer` 搭建浏览器或本地 viewer；先跑最小 ovrtx 示例验证 GPU/runtime，再按交付路径叠加 camera / picking / hierarchy / UI。
2. **给 USD 资产做 Core conform 清洗**：在导入 UE 5.2+ 之前，用 `nvidia-simready-foundation-conform-fet-000-core` 检查并修复命名、路径、metadata、未定义 prim；输出 staged copy 供 Interchange USD 消费。
3. **评估 viewer + conform 的端到端 PoC**：取一个已知 USD 场景，走「cad-to-simready → performance-tuning → realtime-viewer」+「simready-foundation-conform-fet-000-core」组合，记录哪一步需要 GPU、哪一步可离线执行。

## 查询记录

1. 种子仓：JackyST0（仍 star chore）/ mouadja02（08-12 后端 API skill，方向无关）
2. WebSearch 查询（d7 窗口为主，部分放宽发现非近 7 天候选）：
   - `site:github.com "SKILL.md" Unreal Engine UE5 game design agent skill 2026 August`
   - `site:github.com ".cursor/skills" OR ".agents/skills" SKILL.md 3D 2D UI game design workflow August 2026`
   - `github NVIDIA skills SKILL.md Omniverse USD SimReady agent skill 2026`
   - `site:github.com SKILL.md "game design" OR "game development" agent skill 2026`
   - `site:github.com "SKILL.md" "Unreal Engine" OR "UE5" agent skill 2026 August`
   - `site:github.com "SKILL.md" "2D game" OR "3D game" OR "game design" agent skill created:2026-08-08..2026-08-15`
   - `site:github.com "SKILL.md" "blender" OR "houdini" OR "maya" agent skill 2026 August`
   - `site:github.com "SKILL.md" "Omniverse" OR "SimReady" OR "USD" created:2026-08-08..2026-08-15`
   - `site:github.com "SKILL.md" "realtime viewer" OR "ovrtx" OR "ovstream" agent skill 2026`
   - `site:skills.sh "game" OR "Unreal" OR "UE" OR "3D" OR "2D" agent skill 2026`
3. WebFetch 候选原仓：
   - github.com/JackyST0/awesome-agent-skills（种子）
   - github.com/mouadja02/skills（种子）
   - github.com/NVIDIA/skills（核心；确认近 7 天无新增游戏/UE 相关 skill）
   - github.com/nvidia/simready-foundation（新定位；2026-08-04 Release 2026.06.0）
   - github.com/Yuki001/game-dev-skills（08-12/13 更新；无 LICENSE）
   - github.com/John-Sun27/creating-game-combat-vfx（7 月；非近 7 天）
   - github.com/mike007jd/game-superpowers（4 月；非近 7 天）
   - github.com/Sttrevens/4dgames-skills（7 月；非近 7 天）
   - github.com/abagames/agentic-gamedev-skills（08-09 维护 commit，无新增 skill）
4. 候选去重：对照本仓 `skills/3d/` / `skills/unreal/` / `skills/game-design/`，确认 2 条新条目均无重复。
5. 入库：+2 → commit 计划 `CursorSkillSearch` → push 用 `git -c credential.helper= -c credential.helper=manager push origin CursorSkillSearch`。

## 遗留问题 / 趋势记录

- 08-14 commit `49c3310` 已成功 push（push 修复稳定运行 2 个 cron 周期）。
- 本轮 commit 将叠加在 `49c3310` 之上，push 继续使用 `git -c credential.helper= -c credential.helper=manager push origin CursorSkillSearch`。
- gh CLI（2.97.0）可用但本轮仍沿用 REST API + `git credential-manager get` 拿 token 的方式维护 PR #31。
- NVIDIA/skills 中游戏/UE/3D 相关未入库条目还剩 5 个 physical-ai-* + 1 个 omniverse-realtime-viewer（本轮已摘）；simready-foundation 独立仓库成为新的高价值来源。
- 近 7 天新增稀疏，说明游戏/UE 方向的公开 Agent Skills 进入维护期；后续可加大对独立仓库（如 simready-foundation、Yuki001、game-superpowers）的 stock-taking。
