# 技能侦察 DIGEST — 2026-08-10（01:00Z）

- 侦察时间：2026-08-10T01:00Z（cron）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：Memories 2026-08-06 13:00Z（inventory；PR#31 / DIGEST 290 清单）
- 本仓入库：精选 **296** 个 `SKILL.md`（相对 CursorSkillSearch 旧态 290：+6）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

自 08-06 起间隔 4 天：种子仓仍无方向相关新增（mouadja02 近几日多为 Postgres/HTTP/SEO 合规技能）。按基线优先续摘 **fagemx** 的 **game-visual-qa** 与 **gameplay-implementation-review**；并补齐 **gamedev-skills/awesome-gamedev-agent-skills**（455★ Apache-2.0，08-08/09 有现代化资产管线与文档更新）剩余 UE 主链 **blueprints / cpp-gameplay / niagara**，以及新现代化的 **create-game-assets**。新建 skills 仓仍高噪声；Yuki001 仍无 LICENSE；ui-craft 发到 v1.0.18（观望）。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| fagemx-game-visual-qa | 游戏设计·2D/UI | 视觉 QA：风格一致性、UI 对齐、动画、多分辨率 | https://github.com/fagemx/gstack-game | MIT；含 scoring/thresholds；补 QA 视觉专通道 | **引入** |
| fagemx-gameplay-implementation-review | 游戏设计·工作流 | PR/代码变更的「实现质量 + 设计意图幸存」双审查 | 同上 | MIT；Pass0/1/2；打通设计→实现门禁 | **引入** |
| unreal-blueprints | UE | UE5.8 Blueprint 类/事件图/通信模式指南 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | Apache-2.0；与 dcc-mcp 工具向互补 | **引入** |
| unreal-cpp-gameplay | UE | UE5.8 C++ Gameplay Framework / 反射 / Build.cs | 同上 | 补齐 gamedev UE 主链；skills.sh 高安装量 | **引入** |
| unreal-niagara | UE | Niagara 系统/发射器/模块与运行时驱动 | 同上 | 补齐 VFX 作者指南（非 MCP 操作向） | **引入** |
| gamedev-create-game-assets | 2D·3D | 艺术方向→资产清单→2D/3D 管线→校验导入 | 同上 | 08-08 现代化更新；含脚本与 brief 模板 | **引入** |

本仓路径：

- `skills/game-design/fagemx-game-visual-qa/`（+ references）
- `skills/game-design/fagemx-gameplay-implementation-review/`（+ references）
- `skills/unreal/unreal-blueprints/`（+ references/communication）
- `skills/unreal/unreal-cpp-gameplay/`（+ references/components-and-gc）
- `skills/unreal/unreal-niagara/`
- `skills/2d/gamedev-create-game-assets/`（+ assets/references/scripts）

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| fagemx 其余 ~17 技能 | 游戏设计·工作流 | game-direction / game-ideation / pitch-review… | https://github.com/fagemx/gstack-game | 主体验+QA+视觉+实现审查+发布已摘 12；其余可择 ideation/direction | **观望（维持）** |
| abagames/agentic-gamedev-skills | 游戏设计·工作流 | 手感最大化、最小规则机、对抗式修复验证等 | https://github.com/abagames/agentic-gamedev-skills | MIT 12★；08-09 更新；偏小游戏/Godot/Web，与 fagemx 部分重叠 | **观望（新见）** |
| educlopez/ui-craft | UI·设计 | 防 AI 味 UI 工艺系统 | https://github.com/educlopez/ui-craft | MIT 254★；08-09 发 v1.0.18；偏 Web 非 UMG | **观望（有更新）** |
| MengTo/Skills threejs-scroll-world 等 | 3D·Web | Three.js 滚动世界 / 指针轨迹 demo 技能 | https://github.com/MengTo/Skills | 4538★ MIT；08-08/09 新增，偏 Web demo 非 UE | **观望（有更新）** |
| Yuki001/game-dev-skills | 游戏·2D | 精灵/视频等工作流 | https://github.com/Yuki001/game-dev-skills | 08-07 仍有 improve；**仍无 LICENSE** | **观望（缺许可）** |
| SummerEngine/summer-engine-agent | 游戏·引擎 | AI 游戏引擎绑定技能簇 | https://github.com/SummerEngine/summer-engine-agent | MIT 46★；08-06 更新；强引擎绑定 | **观望（维持）** |
| Randroids / NAJEM / mike007jd / alfaris / Shellishack… | 各向 | 维持上轮 | 各原仓 | WIP/MCP 依赖/重叠/许可未变 | 观望 |
| opengameapp/OpenGame-skills | 游戏·Web | 浏览器小游戏构建/发布 | https://github.com/opengameapp/OpenGame-skills | MIT-0；0★；强绑定 OpenGame | **观望（低优）** |

## 可忽略

- 种子：JackyST0 仍仅 08-03 star chore；mouadja02 08-07~09 新增均为 Postgres/HTTP2/NO_PROXY/SEO 等方向无关技能（计数量、不展开）
- `qinchaomeishenmeshi/prd-review`：今日新建，仅有 `PRD-REVIEW.md`，**无 SKILL.md 结构**
- 今日新建噪声：`skills created:>=2026-08-06` 仍以 GitHub Skills 练习、作品集、合规/招聘/WhatsApp 等为主（抽样无关）
- 作弊/外挂/电竞陪玩类一律忽略

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | 616 | 仍仅 08-03 star chore | 无 UE/游戏专区新增 |
| mouadja02/skills | 9 | 08-09 合并 SEO/Postgres 等 PR | 本轮有 commit，**方向无关** |

## 今天可行动

1. 出片/UI 改版后跑 `fagemx-game-visual-qa`（对照 thresholds + platform-requirements），再汇总进 `fagemx-game-qa`
2. 有玩法 PR 时跑 `fagemx-gameplay-implementation-review`（先 Pass0 设计意图，再 Pass1 关键）
3. UE 落地：蓝图用 `unreal-blueprints`，C++ 用 `unreal-cpp-gameplay`，VFX 用 `unreal-niagara`；做资产族时先填 `gamedev-create-game-assets` 的 art-direction-brief

## 查询记录

1. 种子仓 commits / repo meta（JackyST0、mouadja02）
2. 跟踪仓 pushed_at / license / trees（fagemx、gamedev-skills、ui-craft、MengTo、Yuki、SummerEngine、Randroids、NAJEM、mike007jd、alfaris、Shellishack、JetBrains、quodsoler、donchitos、omer、heycat、arg-games 等）
3. repos search：`skills created:>=2026-08-06`；`unreal skills`；`game skills`；`agent skills`+关键词
4. code search：`Unreal filename:SKILL.md` 等（本轮多次 429，改用 trees/blobs + skills.sh 补）
5. skills.sh：unreal / game design / game-visual
6. 候选探测：fagemx 续摘 visual-qa + implementation-review；gamedev 补齐 UE3 + create-game-assets；abagames 新见观望；OpenGame/prd-review 低优
7. 入库：+6 → push `CursorSkillSearch` + 更新 PR#31
