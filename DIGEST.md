# 技能侦察 DIGEST — 2026-08-06（11:00Z）

- 侦察时间：2026-08-06T11:00Z（cron）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：Memories 2026-08-06 10:00Z（inventory；PR#31 / DIGEST 283 清单）
- 本仓入库：精选 **286** 个 `SKILL.md`（相对 CursorSkillSearch 旧态 283：+3）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

种子仓：JackyST0 无新内容；mouadja02 新增 **LLM tool-call stream conformance**（方向无关，仅记数）。按基线「下次优先」续摘 **fagemx/gstack-game**（MIT 58★）的 **balance-review / game-ux-review / playtest**。今日新建噪声仍高（GitHub Skills 练习仓等）；educlopez/ui-craft（MIT ~250★）今日有 evals 合并，仍偏 Web 设计工程，维持观望。Yuki001 / SherryCW / w-zhian / kparkov 仍无 LICENSE。code search 持续 429，以 repos/trees + skills.sh 补。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| fagemx-balance-review | 游戏设计 | 经济与数值平衡评审（难度/货币/养成/付费） | https://github.com/fagemx/gstack-game | MIT；含 references 评分维度；补 economy 评审链 | **引入** |
| fagemx-game-ux-review | UI·游戏设计 | 游戏 UI/UX：HUD/菜单/商店/教程/输入/无障碍 | 同上 | 游戏向 UX，非纯产品 Web；可与 donchitos-ux 并行 | **引入** |
| fagemx-playtest | 工作流·游戏设计 | 试玩协议设计（计划/指标/问卷/分析/招募） | 同上 | 偏协议侧，补 donchitos-playtest-report | **引入** |

本仓路径：

- `skills/game-design/fagemx-balance-review/`（+ references/）
- `skills/ui-design/fagemx-game-ux-review/`（+ references/）
- `skills/workflow/fagemx-playtest/`（+ references/）

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| fagemx 其余 ~23 技能 | 游戏设计·工作流 | player-experience / build-playability / ship 等 | https://github.com/fagemx/gstack-game | 本轮已摘 balance+ux+playtest；**player-experience** 下轮优先 | **观望（维持）** |
| educlopez/ui-craft | UI·设计 | 防 AI 味 UI 工艺系统（craft/critique/polish…） | https://github.com/educlopez/ui-craft | MIT 250★；今日 evals PR 合并；偏 Web 非 UMG | **观望（有更新）** |
| alfaris/Design-AI-Skills-by-Faris | UI·设计 | 七视角设计审计面板 | https://github.com/alfaris/Design-AI-Skills-by-Faris | 今日 README/兼容性更新；CC BY；偏产品/Web | **观望（有更新）** |
| kparkov/skills | 游戏设计 | Blades TRPG 规则顾问 | https://github.com/kparkov/skills | 09:53Z 有 push；**无 LICENSE** | 观望 |
| SummerEngine / Shellishack / w-zhian / SherryCW 大师簇 / Yuki001 / Flue·roble3 / ARKitRemap… | 各向 | 维持上轮 | 各原仓 | LICENSE/引擎绑定/重叠未变 | 观望 |

## 可忽略

- 种子：JackyST0 仍仅 08-03 star chore；mouadja02 **新增** llm-tooling/stream-conformance（方向无关，计 1）
- 今日新建噪声约 100+：GitHub Skills 练习仓、作品集、GA 天气 briefing、htmx、Jira、渗透、通用 PM、roast CLI、空仓等
- 作弊/外挂类一律忽略

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | 614 | 仍仅 08-03 star chore | 无 UE/游戏专区新增 |
| mouadja02/skills | 9 | **10:15Z** 新增 tool-call stream conformance | 方向无关（LLM tooling） |

## 今天可行动

1. 有数值/经济表时跑 `fagemx-balance-review`；与已有 `economy-balancing` 对照缺口
2. HUD/菜单可用时跑 `fagemx-game-ux-review`（准备截图或可操作构建）
3. 正式试玩前用 `fagemx-playtest` 出协议，再用 `donchitos-playtest-report` 写结论

## 查询记录

1. 种子仓 commits / meta（JackyST0、mouadja02）— mouadja02 有无关新 skill
2. 跟踪仓 license/pushed（MengTo、JetBrains、fagemx、Yuki、SherryCW、ui-craft、alfaris、kparkov、SummerEngine、Shellishack、donchitos、omer、heycat、arg-games、ARKitRemap、quodsoler、Flue、roble3、gamedev-skills awesome 等）
3. repos search：skills created:>=2026-08-06；agent skills created:>=2026-08-05；unreal / game design / blender skills
4. code search：Unreal/game design filename:SKILL.md（429）；skills.sh：unreal / game design / blender / ui design
5. 候选探测：fagemx 续摘 3；ui-craft/alfaris 今日更新记观望；player-experience 留作下轮
6. 入库：+3 → push `CursorSkillSearch` + 更新 PR#31
