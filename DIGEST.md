# 技能侦察 DIGEST — 2026-08-06（13:00Z）

- 侦察时间：2026-08-06T13:00Z（cron）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：Memories 2026-08-06 12:00Z（inventory；PR#31 / DIGEST 288 清单）
- 本仓入库：精选 **290** 个 `SKILL.md`（相对 CursorSkillSearch 旧态 288：+2）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

种子仓仍无方向相关新增。按基线优先续摘 **fagemx/gstack-game**（MIT 58★）的 **game-ship** 与 **game-qa**，补齐「可玩性审查之后的 QA 门禁 + 发布上架」链路。今日新建含 “skills” 的仓仍为高噪声；Yuki001 今日有实质 commit 但仍无 LICENSE；ui-craft / alfaris 今日仍有更新（观望）；j4flmao/unreal 仅 8 行浅技能，忽略。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| fagemx-game-qa | 游戏设计·工作流 | 系统化 QA：功能/视觉/性能/音频/输入/兼容/本地化 | https://github.com/fagemx/gstack-game | MIT；含 scoring/severity；与 playability「值不值得玩」互补 | **引入** |
| fagemx-game-ship | 游戏设计·工作流 | 发布工作流：预检→构建→changelog→平台提交 | 同上 | MIT；覆盖 Steam/商店/Web；补上架缺口 | **引入** |

本仓路径：

- `skills/game-design/fagemx-game-qa/`（+ references/scoring + gotchas）
- `skills/game-design/fagemx-game-ship/`（+ references/gotchas）

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| fagemx 其余 ~19 技能 | 游戏设计·工作流 | gameplay-implementation / game-visual-qa / game-direction… | https://github.com/fagemx/gstack-game | 主体验+QA+发布链已摘 10；下轮可择 visual-qa 或 implementation-review | **观望（维持）** |
| educlopez/ui-craft | UI·设计 | 防 AI 味 UI 工艺系统 | https://github.com/educlopez/ui-craft | MIT 250★；10:18Z 仍有 evals 更新；偏 Web 非 UMG | **观望（有更新）** |
| alfaris/Design-AI-Skills-by-Faris | UI·设计 | 设计 AI 技能包 | https://github.com/alfaris/Design-AI-Skills-by-Faris | 今日 10:56Z 仍有 push；CC/NOASSERTION；偏品牌产品 | **观望（有更新）** |
| Yuki001/game-dev-skills | 游戏·2D | 精灵/视频等工作流 | https://github.com/Yuki001/game-dev-skills | 今日多次 improve；**仍无 LICENSE** | **观望（有更新·缺许可）** |
| Randroids-Dojo/unreal | UE·工作流 | UE5 Remote Control / PlayUnreal 自动化（WIP） | https://github.com/Randroids-Dojo/skills | MIT 44★；仍 WIP | **观望（维持）** |
| NAJEMWEHBE/driving-unreal | UE·工作流 | 经 MCP 驱动编辑器 | https://github.com/NAJEMWEHBE/unreal-ai-connection | MIT 9★；强依赖其 MCP | **观望（维持）** |
| mike007jd/game-superpowers | 游戏设计·工作流 | 可玩性/手感审计簇 | https://github.com/mike007jd/game-superpowers | MIT 4★；与 fagemx 重叠 | **观望（维持）** |
| SummerEngine / Shellishack / SherryCW / w-zhian / kparkov / Flue·roble3 / ARKitRemap… | 各向 | 维持上轮 | 各原仓 | 引擎绑定/LICENSE/重叠未变 | 观望 |

## 可忽略

- 种子：JackyST0 仍仅 08-03 star chore；mouadja02 最新仍为 10:15Z stream-conformance（方向无关）
- j4flmao/agent-skills `skills/game/unreal`：MIT 11★，SKILL 仅约 8 行，信息密度不足
- 今日新建噪声：`skills created:>=2026-08-06` 仍以作品集/GitHub Skills 练习/小说写作/通用工具为主（抽样无关）
- 作弊/外挂类一律忽略

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | 615 | 仍仅 08-03 star chore | 无 UE/游戏专区新增 |
| mouadja02/skills | 9 | 最新仍为 10:15Z stream-conformance | 本轮无新 commit；方向无关 |

## 今天可行动

1. 有可玩构建时先跑 `fagemx-game-qa`（按 severity 出缺陷清单），再对照 `fagemx-build-playability-review`
2. 准备试玩/软发时跑 `fagemx-game-ship` 预检（平台检测 + changelog 模板）
3. 若缺 LICENSE 阻碍引入，盯 Yuki001 是否补许可；Web UI 向再评估 ui-craft craft 入口

## 查询记录

1. 种子仓 commits / meta（JackyST0、mouadja02）— 无方向相关新 skill
2. 跟踪仓 license/pushed（fagemx、ui-craft、alfaris、Yuki、SummerEngine、Randroids、NAJEM、mike007jd、MengTo、JetBrains、quodsoler、Shellishack、donchitos、omer、heycat、arg-games 等）
3. repos search：skills created:>=2026-08-06；unreal / game design skills
4. code search：`Unreal filename:SKILL.md`、`game design filename:SKILL.md`（成功）；`path:.cursor/skills` / `.agents/skills`（429）
5. skills.sh：unreal / game design / game-ship
6. 候选探测：fagemx 续摘 game-qa + game-ship；j4flmao 浅技能忽略；maystudios/Italink 主链已齐
7. 入库：+2 → push `CursorSkillSearch` + 更新 PR#31
