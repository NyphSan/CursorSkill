# 技能侦察 DIGEST — 2026-08-06（12:00Z）

- 侦察时间：2026-08-06T12:00Z（cron）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：Memories 2026-08-06 11:00Z（inventory；PR#31 / DIGEST 286 清单）
- 本仓入库：精选 **288** 个 `SKILL.md`（相对 CursorSkillSearch 旧态 286：+2）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

种子仓无方向相关新增（JackyST0 仍仅 08-03 star chore；mouadja02 无新 commit）。按基线优先续摘 **fagemx/gstack-game**（MIT 58★）的 **player-experience** 与 **build-playability-review**。code search 发现若干 UE 自动化向候选（Randroids-Dojo unreal WIP、NAJEMWEHBE driving-unreal MCP、mike007jd game-superpowers）记入观望。今日新建含 “skills” 的仓噪声极高（API total≈1663，多为 GitHub Skills 练习/作品集）；Yuki001 / SherryCW / w-zhian / kparkov 仍无 LICENSE。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| fagemx-player-experience | 游戏设计 | 第一人称 persona 走查，找摩擦/困惑/流失 | https://github.com/fagemx/gstack-game | MIT；含 personas/phases/scoring；补「分析」之外的角色扮演链 | **引入** |
| fagemx-build-playability-review | 游戏设计·工作流 | 有构建后评「值不值得玩」（回路/留存欲） | 同上 | 与 QA/feel/实现审查分离；含 scoring；原型门禁有用 | **引入** |

本仓路径：

- `skills/game-design/fagemx-player-experience/`（+ references/）
- `skills/game-design/fagemx-build-playability-review/`（+ references/）

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| fagemx 其余 ~21 技能 | 游戏设计·工作流 | game-ship / game-qa / gameplay-implementation… | https://github.com/fagemx/gstack-game | 主体验链已摘 8；下轮可择 **game-ship** 或 **game-qa** | **观望（维持）** |
| Randroids-Dojo/unreal | UE·工作流 | UE5 Remote Control / PlayUnreal 自动化（WIP） | https://github.com/Randroids-Dojo/skills | MIT 44★；E2E/CI 向，仍 WIP | **观望（新见）** |
| NAJEMWEHBE/driving-unreal | UE·工作流 | 经 unreal-ai-connection MCP 驱动编辑器 | https://github.com/NAJEMWEHBE/unreal-ai-connection | MIT 9★；~143 工具编排 know-how；强依赖其 MCP 插件 | **观望（新见）** |
| mike007jd/game-superpowers | 游戏设计·工作流 | 可玩性/手感/HUD 等审计技能簇 | https://github.com/mike007jd/game-superpowers | MIT 4★；与 fagemx 重叠多；可作对照 | **观望（新见）** |
| educlopez/ui-craft | UI·设计 | 防 AI 味 UI 工艺系统 | https://github.com/educlopez/ui-craft | MIT 250★；10:18Z 仍有更新；偏 Web 非 UMG | **观望（有更新）** |
| alfaris / kparkov / SummerEngine / Shellishack / Yuki001 / SherryCW 大师簇 / Flue·roble3 / ARKitRemap… | 各向 | 维持上轮 | 各原仓 | LICENSE/引擎绑定/重叠未变 | 观望 |

## 可忽略

- 种子：JackyST0 无新内容；mouadja02 本小时无新 commit（上轮无关 stream-conformance 仍计历史）
- 今日新建噪声：`skills created:>=2026-08-06` API total≈1663（练习仓/作品集/营销/空仓等）；抽样无关如 speak-better、PagerDuty、Odoo、法律、GIS、learn-codebase
- 作弊/外挂类（如 brawl-stars cheat）一律忽略

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | 615 | 仍仅 08-03 star chore | 无 UE/游戏专区新增 |
| mouadja02/skills | 9 | 最新仍为 10:15Z stream-conformance | 本轮无新 commit；方向无关 |

## 今天可行动

1. 有可叙述流程/原型时跑 `fagemx-player-experience`（先选 persona，输出 journey map）
2. 有可运行构建时跑 `fagemx-build-playability-review`，对照 feel-pass / game-review 缺口
3. 若在用 UE Remote Control / 自建 MCP，抽查 Randroids WIP 与 NAJEMWEHBE driving-unreal 是否可落地

## 查询记录

1. 种子仓 commits / meta（JackyST0、mouadja02）— 无方向相关新 skill
2. 跟踪仓 license/pushed（MengTo、JetBrains、fagemx、Yuki、SherryCW、ui-craft、alfaris、kparkov、SummerEngine、Shellishack、donchitos、omer、heycat、arg-games、ARKitRemap、quodsoler、Flue、roble3 等）
3. repos search：skills created:>=2026-08-06；agent skills created:>=2026-08-05；unreal / game design / blender skills
4. code search：`Unreal filename:SKILL.md`（成功一批）；`game design path:.cursor/skills`（429）
5. skills.sh：unreal / game design / blender / ui design / playability / player experience
6. 候选探测：fagemx 续摘 2；Randroids/NAJEM/mike007jd 记观望；ui-craft 今日仍有 push
7. 入库：+2 → push `CursorSkillSearch` + 更新 PR#31
