# 技能侦察 DIGEST — 2026-08-06（分支 CursorSkillSearch）

- 侦察/入库时间：2026-08-06（本地 Agent 手动跑 + 合并 Automation 最新 digest）
- 目标分支：**CursorSkillSearch**（按用户指定）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：对话内上次报告（agentic-gamedev / novel-to-game / threejs / UMG MCP / dcc-mcp）+ 仓内 `skill-digest-2026-08-06-06`
- 本仓结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）
- 来源 digest 分支：`skill-digest-2026-08-06-06`（Automation 已入库约 263→266 份 SKILL.md）

## 一屏结论

种子仓（JackyST0 / mouadja02）无方向相关新 skill 专区。本轮相对旧基线：**Automation 已持续入库**；手动侧将内容固定到 **CursorSkillSearch**。`abagames/agentic-gamedev-skills` 当前 API 查无（MISS，可能更名/删除）→ 降级跟踪。

## 建议引入（相对对话旧基线：新增/升级）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| mengto-design-game-encounters 等 5 项 | 游戏设计 | 遭遇/背包/VFX/相机/敌人 AI | https://github.com/MengTo/Skills | 设计闭环清晰，可读可测 | **引入**（已摘录） |
| heycat-animated-sprite + lowvram | 2D·工作流 | 精灵动画 + 12GB SDXL 管线 | https://github.com/0xheycat/isometric-game-skills | 等距资产生成主链 | **引入**（已摘录） |
| arg-games-unreal-cqtest | UE·工作流 | CQTest 模板 | https://github.com/arg-games/Unreal-Skill | MIT；补 UE 测试缺口 | **引入**（已摘录） |
| jetbrains-ue-test-authoring | UE·工作流 | Rider 辅助写 UE 自动化测试 | https://github.com/JetBrains/rider-skills | Apache-2.0；无 Rider 可降级 | **引入**（已摘录） |
| UnrealMotionGraphicsMCP | UE·UI | UMG + MCP + Skills | https://github.com/winyunq/UnrealMotionGraphicsMCP | 最贴 UE UI | **引入/试点** |
| frontend-design / ui-design-brain | UI | Web 非模板 UI | anthropics/skills · carmahhawwari/ui-design-brain | 仅 Web 工具页 | **观望**（勿当 UMG 主 skill） |
| threejs-skills | 3D | Three.js 全栈 | https://github.com/CloudAI-X/threejs-skills | 非 UE | **观望** |
| novel-to-game | 游戏设计 | 小说→游戏概念 | https://github.com/worldwonderer/novel-to-game | 方法向 | **观望** |
| agentic-gamedev-skills | 游戏设计 | game feel 等 | （原 abagames） | API MISS | **忽略/改追** |

## 观望 / 可忽略

- 观望：affinity-help、AngelScript skills README 抖动仓、纯品牌设计文档仓
- 忽略：通用 coding / idea-refine、无 LICENSE 噪声仓、广告变现类

## 今天可行动

1. 在 Cursor 中把 Remote Rule / skills 指向本仓 `CursorSkillSearch` 分支下的 `skills/`
2. UE 优先试：`arg-games-unreal-cqtest` + `jetbrains-ue-test-authoring`；UMG 试点 `UnrealMotionGraphicsMCP`（需插件）
3. 游戏设计试 MengTo encounters / inventory；Web UI 才装 frontend-design

## 查询记录

- 种子：JackyST0/awesome-agent-skills、mouadja02/skills
- API：repos 元数据刷新；`abagames/agentic-gamedev-skills` → MISS
- 合并：origin/skill-digest-2026-08-06-06 的 DIGEST + skills/