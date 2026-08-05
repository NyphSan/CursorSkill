# 技能侦察 DIGEST — 2026-08-05（23:00Z）

- 侦察时间：2026-08-05T23:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T22:00Z（同日上一轮，PR#21）
- 本仓入库：精选 **204** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-05-23`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。跟踪仓：ConnorGriffin **22:54Z** 仅改通用 `orchestrate` 模型档标注（忽略）；eve-skills 20:03Z 为 EVE Online ESI/SDE 重构（方向弱相关，维持观望）；Yuki001 仍无 LICENSE；kevin/sipher 许可未变。本轮按「下次优先」引入 omer：**creature-design / procedural-generation / weapon-design / game-networking / progression-systems**；donchitos **asset-spec / design-review**；以及 arjun988 **blender→UE 导出**（MIT，与已收 export-pipeline 互补）。Flue Blender 桥、ConnorGriffin ui-craft（MIT 但偏 Web 产品 UI）继续观望。今日新建噪声仍为 brand-copy / flights / skills-mcp；另见 nickbutler/skills、w-zhian/game-design-skills（0★/无 LICENSE/与已收重叠）。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| omer-creature-design | 2D·游戏设计 | 生物/怪物解剖逻辑、剪影与生态角色 | https://github.com/omer-metin/skills-for-antigravity | 123★ Apache-2.0；补齐生物向缺口 | **引入** |
| omer-procedural-generation | 游戏设计 | PCG/噪声/WFC/L-system 与 generate-then-curate | 同上 | 与已收 gamedev-procedural-gen / UE PCG 互补（更偏设计约束） | **引入** |
| omer-weapon-design | 2D·游戏设计 | 武器剪影/材质语言/稀有度视觉 | 同上 | 战斗与美术交界刚需；与 combat 成对 | **引入** |
| omer-game-networking | 游戏设计 | 预测/和解/回滚/服务器权威与反作弊 | 同上 | 联网向此前偏薄；可对接 UE Replication | **引入** |
| omer-progression-systems | 游戏设计 | XP/技能树/元进度与奖励节奏 | 同上 | 补齐成长曲线设计 | **引入** |
| donchitos-asset-spec | 研发工作流 | 从 GDD/关卡/角色生成资产规格与 AI 提示 | https://github.com/donchitos/claude-code-game-studios | 23630★ MIT；接 art-bible 后的生产规格门 | **引入** |
| donchitos-design-review | 研发工作流 | GDD 完整性/一致性/可实现性评审 | 同上 | 与 consistency-check 成门禁链 | **引入** |
| blender-unreal-export | 3D·UE | Blender→UE FBX/LOD/UCX/Socket 导出 | https://github.com/arjun988/blender-skills | 74★ MIT；UE 专用导出清单，补 DCC→引擎缝 | **引入** |

本仓已摘录：

- `skills/2d/omer-creature-design/`（+ references）
- `skills/game-design/omer-procedural-generation/`（+ references）
- `skills/2d/omer-weapon-design/`（+ references）
- `skills/game-design/omer-game-networking/`（+ references）
- `skills/game-design/omer-progression-systems/`（+ references）
- `skills/workflow/donchitos-asset-spec/`
- `skills/workflow/donchitos-design-review/`
- `skills/3d/blender-unreal-export/`（+ references）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 18:06Z idea-refine；无新 commit | https://github.com/mouadja02/skills | **忽略**（通用 coding） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| ConnorGriffin/skills | 22:54Z orchestrate 模型档标注；ui-craft 未变 | https://github.com/ConnorGriffin/skills | 通用研发 → **忽略增量**；ui-craft 维持观望（MIT，偏 Web UI） |
| snipereagle1/eve-skills | 20:03Z ESI/SDE 文档重构 | https://github.com/snipereagle1/eve-skills | EVE Online 专用 → **观望/低优** |
| Yuki001/game-dev-skills | 仍无 LICENSE；49★ | https://github.com/Yuki001/game-dev-skills | 维持观望 |
| kevinpbuckley/unreal-engine-skills | 08-04 UE 5.8；仍无 SPDX | https://github.com/kevinpbuckley/unreal-engine-skills | 维持观望 |
| sipherxyz/universal-ue-skills | 07-31；1★ 无 LICENSE | https://github.com/sipherxyz/universal-ue-skills | 观望 |
| sfkislev/flue | Blender/Houdini 桌面桥；含硬编码本机路径 | https://github.com/sfkislev/flue | 观望（需本机 Flue 安装） |
| lisxa5747 AngelScript | README SEO 劣化未恢复 | https://github.com/lisxa5747/unreal-angelscript-skills | 观望/降级 |

### 累计建议引入（仍有效）

1–75. 维持至上轮（含 omer 绑定/战斗/音频/光照/AI、maystudios BP codegen/thirdparty、mengto action-combat）  
76. **+ 本轮** omer：creature-design / procedural-generation / weapon-design / game-networking / progression-systems  
77. **+ 本轮** donchitos：asset-spec / design-review  
78. **+ 本轮** blender-unreal-export（arjun988）

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| ConnorGriffin ui-craft | UI·工作流 | 视觉 lock→build→critique→audit 生命周期 | https://github.com/ConnorGriffin/skills | MIT 且脚本完整，但偏 Web/产品 UI；可改造成游戏 UI 个人 skill | 观望 |
| sfkislev/flue blender | 3D·工作流 | 无 MCP 的 shell→bpy 桌面桥 | https://github.com/sfkislev/flue | 65★ MIT；SKILL 薄且含本机路径 | 观望 |
| donchitos balance-check / team-ui / playtest | 游戏设计·工作流 | 数值平衡/UI 团队流水线/试玩报告 | https://github.com/donchitos/claude-code-game-studios | 本轮优先 asset-spec/design-review；下次可摘 | 观望 |
| Yuki001/game-dev-skills | 游戏设计·3D·工作流 | architect / toon shader / 图像资产生成 | https://github.com/Yuki001/game-dev-skills | 49★ 内容扎实；**无 LICENSE** | 观望 |
| kevin / sipher / lisxa5747 / eve / driving-unreal / Rider | 各向 | 维持上轮理由 | 各原仓 | 许可或成熟度未变 | 观望 |
| w-zhian/game-design-skills | 游戏设计 | 策划向自演化包 | https://github.com/w-zhian/game-design-skills | 0★ 无 LICENSE；与已收 combat/economy 重叠 | 观望/低优 |
| august-batista unreal-assets | UE | 安全读写 .uasset/.umap | https://github.com/august-batista/claude-unreal-bridge-editor | MIT 0★；强依赖其桥工具 | 观望 |

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 idea-refine（方向无关，记数）
- ConnorGriffin 本轮 orchestrate 增量（通用研发）
- 今日新建噪声：`vaishnvaik6/brand-website-copy-skill`、`mossly/flights-skill`、`raymatos/skills-mcp`、`nickbutler/skills`（commit/scrollytelling 等）
- eve-skills：EVE Online API，非通用游戏/UE
- gisenberg/unreal-skills：无 LICENSE；优先 osseous

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 仍为 **08-05 18:06Z** idea-refine portable（无关）；此后无新 commit |

## 本仓入库变化（+8 → 204）

- 新增 `skills/2d/omer-creature-design/`
- 新增 `skills/game-design/omer-procedural-generation/`
- 新增 `skills/2d/omer-weapon-design/`
- 新增 `skills/game-design/omer-game-networking/`
- 新增 `skills/game-design/omer-progression-systems/`
- 新增 `skills/workflow/donchitos-asset-spec/`
- 新增 `skills/workflow/donchitos-design-review/`
- 新增 `skills/3d/blender-unreal-export/`
- 各含 `SOURCE.md`；承接上轮 196 条精选内容

## 今天可行动

1. **美术生产链**：已有 `donchitos-art-bible` → 试 `donchitos-asset-spec` 生成实体规格，再用 `donchitos-design-review` 做 GDD 出门禁。  
2. **生物/武器概念**：装 `omer-creature-design` + `omer-weapon-design`，对照已有 combat/character-design 跑一条 Boss+武器视觉语言；适合改成你的 UE 资产命名个人 skill。  
3. **DCC→UE**：Blender 出资源时用 `blender-unreal-export`（UCX/LOD/Socket）+ 已收 `export-pipeline`；联网原型再叠 `omer-game-networking`。

## 已尝试查询

1. 种子仓 commits / repo meta（JackyST0、mouadja02）
2. 跟踪仓 pushed_at / trees / license（omer、osseous、donchitos、ConnorGriffin、eve、kevin、sipher、Yuki001、Flue、arjun988、maystudios、MengTo、Rider、lisxa5747、NAJEMWEHBE 等）
3. repos search：skill created≥08-04；unreal/gamedev/game design skills
4. code search：Unreal filename:SKILL.md；game design filename:SKILL.md；path:.agents/.cursor/skills
5. skills.sh/api/search：unreal、creature design、weapon design、procedural generation、game ui、umg、level design、godot、unity、blender、art bible、pixel art、combat、animation
6. 候选 blob SKILL.md 质量核 + 入库 + push + open_git_pr + Slack
