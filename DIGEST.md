# 技能侦察 DIGEST — 2026-08-05（21:00Z）

- 侦察时间：2026-08-05T21:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T20:01Z（同日上一轮，PR#19）
- 本仓入库：精选 **188** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-05-21`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill（JackyST0 停在 08-03；mouadja02 仍为 idea-refine，无关）。跟踪仓：ConnorGriffin 20:27Z 合入 persona-review/say-less 等（偏通用研发，非游戏/UE UI，不升级）；eve-skills 持续重构（栈窄无 SPDX，维持低优观望）。本轮按「下次优先」缺口补齐：① omer **art-consistency / voxel-art / animation-systems**；② 新发现 [osseous/skills](https://github.com/osseous/skills)（MIT）AngelScript 三件套，替代无 LICENSE 的 gisenberg；③ 新发现 [donchitos/claude-code-game-studios](https://github.com/donchitos/claude-code-game-studios)（23630★ MIT）摘录 Art Bible + GDD 一致性检查。今日新建噪声含 brand-website-copy / flights-skill；[lisxa5747/unreal-angelscript-skills](https://github.com/lisxa5747/unreal-angelscript-skills) 今日 README 更新且确认 MIT，与 osseous 重叠 → 观望。code search 429；skills.sh + trees/blobs 补齐。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| omer-art-consistency | 2D·设计 | AI 角色/风格一致性：参考契约、防漂移、视觉 QA | https://github.com/omer-metin/skills-for-antigravity | 123★ Apache-2.0；含 patterns/sharp_edges/validations | **引入** |
| omer-voxel-art | 3D·设计 | MagicaVoxel 工作流、调色板、体素动画与引擎优化 | https://github.com/omer-metin/skills-for-antigravity | 体素细分此前未收；含 UE/Godot 导出要点 | **引入** |
| omer-animation-systems | 游戏设计 | 骨骼/状态机/混合树/IK/根运动/动作匹配（跨引擎） | https://github.com/omer-metin/skills-for-antigravity | 与已有 `ue-animation-system` 形成设计↔UE API 互补 | **引入** |
| osseous-unreal-engine-angelscript | UE | Hazelight AngelScript：8+ 陷阱、绑定核查、复制/热重载 | https://github.com/osseous/skills | **MIT**；脚本+references 完整；填补 gisenberg 许可缺口 | **引入** |
| osseous-ue-angelscript-tests | UE | AS `Test_*` / `IntegrationTest_*` 编写与 MCP/CLI 运行 | https://github.com/osseous/skills | 与编码 skill 成对；含 EXAMPLES/REFERENCE | **引入** |
| osseous-read-ue-logs | UE·工作流 | 合并/过滤 Saved/Logs（多客户端、JSON、分类） | https://github.com/osseous/skills | 可执行 ps1；诊断刚需薄而实用 | **引入** |
| donchitos-art-bible | 游戏设计·2D | 分段撰写 Art Bible（9 节视觉身份规格） | https://github.com/donchitos/claude-code-game-studios | 23630★ MIT；作流程模板（依赖其脚手架） | **引入** |
| donchitos-consistency-check | 工作流 | GDD vs 实体注册表交叉不一致扫描 | https://github.com/donchitos/claude-code-game-studios | 设计文档一致性网；可改写为个人 registry 流程 | **引入** |

本仓已摘录：

- `skills/2d/omer-art-consistency/`（+ references）
- `skills/3d/omer-voxel-art/`（+ references）
- `skills/game-design/omer-animation-systems/`（+ references）
- `skills/unreal/osseous-unreal-engine-angelscript/`（+ references/scripts）
- `skills/unreal/osseous-ue-angelscript-tests/`（+ EXAMPLES/REFERENCE）
- `skills/unreal/osseous-read-ue-logs/`（+ scripts）
- `skills/game-design/donchitos-art-bible/`
- `skills/workflow/donchitos-consistency-check/`

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 18:06Z idea-refine；无更新 | https://github.com/mouadja02/skills | **忽略**（通用 coding） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| ConnorGriffin/skills | 20:27Z persona-review / say-less / spin-worktree；ui-craft 未变 | https://github.com/ConnorGriffin/skills | 新提交偏通用研发 → **忽略增量**；ui-craft 维持观望 |
| snipereagle1/eve-skills | 20:03Z 多轮 ESI/SDE 文案重构 | https://github.com/snipereagle1/eve-skills | 栈窄且无 SPDX → 维持低优观望 |
| kevinpbuckley / sipherxyz / gisenberg / Flue / Rider | 无新实质或许可未变 | 各原仓 | 维持观望（gisenberg 由 osseous MIT 方案替代） |
| lisxa5747/unreal-angelscript-skills | 20:36Z README；LICENSE=MIT；references 丰富 | https://github.com/lisxa5747/unreal-angelscript-skills | 0★；与 osseous 重叠 → **观望** |

### 累计建议引入（仍有效）

1–69. 维持至上轮（含 omer 概念/环境/纹理、街机音频、LQE、game-redesign 等）  
70. **+ 本轮** omer：art-consistency / voxel-art / animation-systems  
71. **+ 本轮** osseous：unreal-engine-angelscript / ue-angelscript-tests / read-ue-logs  
72. **+ 本轮** donchitos：art-bible / consistency-check  

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| lisxa5747/unreal-angelscript-skills | UE | 厂商中立 AngelScript skill 包（GAS/UI/学习树） | https://github.com/lisxa5747/unreal-angelscript-skills | 今日活跃；MIT；与 osseous 重叠，质量待对照 | 观望 |
| osseous/skills unreal-engine（C++ 侧） | UE | 发现→搜索防幻觉的 UE C++ skill | https://github.com/osseous/skills | 本仓已有大量 UE C++；按需再取 | 观望 |
| abagames creating-godot-procedural-audio 等 | 游戏设计 | Godot 内置程序化 SFX / headless / 脚手架 | https://github.com/abagames/agentic-gamedev-skills | 栈特定；非 UE 主线 | 观望 |
| ConnorGriffin ui-craft | UI·工作流 | 视觉规格→构建→审计 | https://github.com/ConnorGriffin/skills | 偏 Web 产品 UI；许可 NOASSERTION | 观望 |
| JetBrains/rider-skills UE 三件套 | UE·工作流 | Rider MCP 驱动 UE | https://github.com/JetBrains/rider-skills | 强依赖 Rider MCP | 观望 |
| SFKislev/Flue | 3D·工作流 | CLI 控桌面软件（含 DCC） | https://github.com/SFKislev/Flue | 本机桥硬编码路径风险 | 观望 |
| kevinpbuckley / sipherxyz / babysitter 薄层 / cesiumjs | UE·3D | 维持上轮观望理由 | 各原仓 | 许可或重叠未变 | 观望 |
| snipereagle1/eve-skills | 游戏·工作流 | EVE Online ESI/SDE | https://github.com/snipereagle1/eve-skills | 活跃但栈窄无 SPDX | 观望/低优 |
| donchitos 其余（asset-spec / design-review / playtest…） | 游戏设计·工作流 | 完整游戏工作室流程 skill 集 | https://github.com/donchitos/claude-code-game-studios | 本轮先收 2 个入口；其余强依赖脚手架 | 观望 |
| gisenberg/unreal-skills | UE | 旧 AngelScript 候选 | https://github.com/gisenberg/unreal-skills | **降级**：无 LICENSE；优先 osseous | 可忽略/低优 |

其余观望（hao-skills、Stanestane、SherryCW miyamoto、chris58530 等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 idea-refine（方向无关，记数）
- ConnorGriffin 本轮通用研发增量（persona-review / say-less 等）
- 今日新建噪声：`vaishnvaik6/brand-website-copy-skill`、`mossly/flights-skill`、`raymatos/skills-mcp`、大量 Skills 练习仓/简历仓
- code search 429；练习仓与作业展示

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 仍为 **08-05 18:06Z** idea-refine portable（无关）；此后无新 commit |

## 本仓入库变化（+8 → 188）

- 新增 `skills/2d/omer-art-consistency/`
- 新增 `skills/3d/omer-voxel-art/`
- 新增 `skills/game-design/omer-animation-systems/`
- 新增 `skills/unreal/osseous-unreal-engine-angelscript/`
- 新增 `skills/unreal/osseous-ue-angelscript-tests/`
- 新增 `skills/unreal/osseous-read-ue-logs/`
- 新增 `skills/game-design/donchitos-art-bible/`
- 新增 `skills/workflow/donchitos-consistency-check/`
- 各含 `SOURCE.md`；承接上轮 180 条精选内容

## 今天可行动

1. **若用 Hazelight AngelScript**：装 `osseous-unreal-engine-angelscript` + `osseous-ue-angelscript-tests`，用 `osseous-read-ue-logs` 验插件是否加载 `Script/`。  
2. **闭合美术一致性环**：用 `omer-art-consistency` 建角色圣经，再跑已装 concept/character；体素项目试 `omer-voxel-art`。  
3. **个人化 Art Bible**：以 `donchitos-art-bible` 为骨架，剥掉其 `design/gdd` 硬依赖，改成你的 UE 项目文档路径后做成个人 skill。

## 已尝试查询

1. 种子仓 commits / repo meta（JackyST0、mouadja02）
2. 跟踪仓 pushed_at / trees / license（omer、abagames、osseous、lisxa5747、ConnorGriffin、eve-skills、kevin、sipher、gisenberg、Rider、Flue、cesiumjs、donchitos、apetrov、quodsoler、gamedev-skills 等）
3. repos search：skill created≥08-05；unreal/gamedev/game design skills；agent skills + game/UE
4. code search：Unreal filename:SKILL.md；path:.agents/skills；path:.cursor/skills（均 429）
5. skills.sh/api/search：unreal、umg、level design、voxel、pixel art、animation、concept art、game audio、ui design、angelscript、art consistency、combat、art bible、rigging、game studio
6. 候选 blob SKILL.md 质量核 + 入库 + push + open_git_pr + Slack
