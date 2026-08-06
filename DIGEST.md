# 技能侦察 DIGEST — 2026-08-06（06:00Z）

- 侦察时间：2026-08-06T06:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-06T05:00Z（同日上一轮，PR#28）
- 本仓入库：精选 **263** 个 `SKILL.md`（较上轮 +9；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-06-06`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。跟踪仓：`lisxa5747` / `Oliyflemishspeaking560` 再次仅 README 抖动；`bomkino` 有文档整理但偏品牌设计。按「下次优先」续摘 **MengTo** 遭遇/背包/VFX/相机/敌人 AI（5），收齐 **0xheycat** 剩余主链 **animated-sprite** + **comfyui-lowvram**（2），并将上轮观望的 CQTest 升级引入：`arg-games/Unreal-Skill`（原 greatinterface 重定向，MIT）+ **JetBrains/rider-skills** `ue-test-authoring`（Apache-2.0）。今日新建噪声约 50+；`Heybinshao/affinity-help`（MIT，862 篇帮助缓存）→ 观望。kevinpbuckley 仍无 LICENSE。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| mengto-design-game-encounters | 游戏设计 | 遭遇设计：目标/波次/公平性与确定性验证 | https://github.com/MengTo/Skills | 接 levels + action-combat；可读压力而非堆怪 | **引入** |
| mengto-build-game-inventory | 游戏设计·UI | 背包/装备：原子转移、tooltip、无丢失回归 | 同上 | 持久化与迁移边界清晰；可接 ARPG 切片 | **引入** |
| mengto-create-game-vfx | 游戏设计·3D | 可读 VFX：含义优先、池化与减动效 | 同上 | 与 encounter/AI 的 telegraph 闭环 | **引入** |
| mengto-build-game-camera-controls | 游戏设计·2D·3D | 游戏相机：跟随/遮挡/锁定与触控 | 同上 | 与 heycat camera-pan-zoom 互补（3D/Web） | **引入** |
| mengto-tune-enemy-ai | 游戏设计 | 敌人 AI：状态机、可读攻击与确定性测试 | 同上 | 决策面可测；接 encounters | **引入** |
| heycat-animated-sprite-generation | 2D | 循环动画精灵帧条（水/火/旗帜等） | https://github.com/0xheycat/isometric-game-skills | 等距管线收尾；只动 overlay 不动画地砖 | **引入** |
| heycat-comfyui-lowvram-setup | 2D·工作流 | 12GB GPU 稳定 SDXL 等距资产生成 | 同上 | 管线主链收齐；固定 seed/采样器防 OOM | **引入** |
| arg-games-unreal-cqtest | UE·工作流 | CQTest 模板/Helper/Latent Actions | https://github.com/arg-games/Unreal-Skill | MIT；补 osseous AS 测试缺口；含可跑模板 | **引入** |
| jetbrains-ue-test-authoring | UE·工作流 | Rider MCP 辅助写 UE 自动化测试 | https://github.com/JetBrains/rider-skills | Apache-2.0 官方；无 Rider 可降级文件模式 | **引入** |

本仓已摘录：

- `skills/game-design/mengto-design-game-encounters/`（+ agents/）
- `skills/game-design/mengto-build-game-inventory/`（+ agents/）
- `skills/game-design/mengto-create-game-vfx/`（+ agents/）
- `skills/game-design/mengto-build-game-camera-controls/`（+ agents/）
- `skills/game-design/mengto-tune-enemy-ai/`（+ agents/）
- `skills/2d/heycat-animated-sprite-generation/`（+ assets/）
- `skills/2d/heycat-comfyui-lowvram-setup/`
- `skills/unreal/arg-games-unreal-cqtest/`（+ assets/ + references/）
- `skills/unreal/jetbrains-ue-test-authoring/`（+ reference/）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 18:06Z idea-refine；无新 commit | https://github.com/mouadja02/skills | **忽略**（通用 coding） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| lisxa5747 AngelScript | 05:28Z 仅 Update README | https://github.com/lisxa5747/unreal-angelscript-skills | **观望/降级**（优先 osseous） |
| Oliyflemishspeaking560/threejs-game-skills | 05:30Z 仅 Update README；0★ MIT | https://github.com/Oliyflemishspeaking560/threejs-game-skills | 观望/低优（疑似镜像 majid） |
| bomkino/pitchdog-design | 03:20Z 文档整理；偏品牌 | https://github.com/bomkino/pitchdog-design | 维持观望 |
| greatinterface → arg-games | API 重定向至 `arg-games/Unreal-Skill` | https://github.com/arg-games/Unreal-Skill | CQTest **本轮已引入**；AS 与 osseous 重叠不重复收 |
| kevinpbuckley/unreal-engine-skills | 25★ 仍无 LICENSE；内容很全 | https://github.com/kevinpbuckley/unreal-engine-skills | **维持观望**（等 SPDX） |
| educlopez / ConnorGriffin / Flue / Yuki001 / Stanestane / QQstone | 无实质 / 仍无 LICENSE（后三者） | 各原仓 | 维持观望 |

### 累计建议引入（仍有效）

1–92. 维持至上轮（含 heycat 管线主链、mengto isometric-arpg/levels）  
93. **+ 本轮** mengto：encounters / inventory / vfx / camera / enemy-ai  
94. **+ 本轮** heycat：animated-sprite / comfyui-lowvram  
95. **+ 本轮** arg-games CQTest + JetBrains ue-test-authoring

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| MengTo 其余 game-development（ship-web / enemy-systems / optimize / map-editor / audio…） | 游戏设计·3D | Web/Three.js 垂直切片技能簇 | https://github.com/MengTo/Skills | 本轮已收 encounters 等 5；按需续摘 | **观望（调整）** |
| 0xheycat using-isometric-skills | 2D | 等距技能元索引 | https://github.com/0xheycat/isometric-game-skills | 主链已齐；元索引可按需 | **观望（调整）** |
| Heybinshao/affinity-help | 2D·设计 | Affinity 官方帮助中文问答 | https://github.com/Heybinshao/affinity-help | 今日新建 MIT；**862 篇 references 过大**，先观望 | **观望（新增）** |
| ChloeVPin/apple-design-skill | UI·设计 | Apple HIG/动效 Web 化 | https://github.com/ChloeVPin/apple-design-skill | 今日新建 0★；偏产品 UI | **观望（新增）** |
| JetBrains ue-code-authoring / ue-live-debugging | UE·工作流 | Rider MCP 写码/调试 | https://github.com/JetBrains/rider-skills | 本轮先收测试；强依赖 Rider | **观望（新增）** |
| kevinpbuckley/unreal-engine-skills | UE | 大而全 UE 核心技能簇 | https://github.com/kevinpbuckley/unreal-engine-skills | 25★ **无 LICENSE** | 观望 |
| QQstone / Stanestane / Yuki001 | 2D·游戏设计 | 维持上轮 | 各原仓 | 仍无 LICENSE | 观望 |
| bomkino / ConnorGriffin / educlopez ui-craft | UI·设计 | 维持上轮 | 各原仓 | 偏品牌/产品 Web | 观望 |
| sfkislev/flue / vladmdgolam | 3D·工作流 | Blender 桥 / MCP | 各原仓 | 本机路径或强依赖 MCP | 观望 |
| gisenberg / sipher / lisxa5747 / eve / OpenGame | UE 等 | 维持上轮理由 | 各原仓 | 许可或成熟度 | 观望 |

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 idea-refine（方向无关，记数）
- ConnorGriffin 通用 orchestrate/say-less（非游戏向）
- 今日新建噪声（方向无关，约 50+）：`gemdesign-ai/skills`、`minhgv/agy-kit`、`qtalen/aidlc-skills`、`xinglongMedical/nma-research-skill`、GitHub Skills 练习仓、作品集仓等
- `lisxa5747` / `Oliyflemishspeaking560`：仅 README 更新，不计实质
- eve-skills：EVE Online API
- 作弊/外挂类新建仓一律忽略
- GitHub code search 不稳定；以 repos + skills.sh + 跟踪仓 trees 为准

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 仍为 **08-05 18:06Z** idea-refine portable（无关）；此后无新 commit |

## 本仓入库变化（+9 → 263）

- 新增 `skills/game-design/mengto-design-game-encounters/`
- 新增 `skills/game-design/mengto-build-game-inventory/`
- 新增 `skills/game-design/mengto-create-game-vfx/`
- 新增 `skills/game-design/mengto-build-game-camera-controls/`
- 新增 `skills/game-design/mengto-tune-enemy-ai/`
- 新增 `skills/2d/heycat-animated-sprite-generation/`
- 新增 `skills/2d/heycat-comfyui-lowvram-setup/`
- 新增 `skills/unreal/arg-games-unreal-cqtest/`
- 新增 `skills/unreal/jetbrains-ue-test-authoring/`
- 各含 `SOURCE.md`；mengto 五项含 `agents/`；arg-games 含 templates/helpers；承接上轮 254 条精选内容

## 今天可行动

1. **装**：`skills/unreal/arg-games-unreal-cqtest` + `jetbrains-ue-test-authoring` — 先用 CQTest 模板写一条 Actor 冒烟，再视 Rider MCP 是否开启决定是否用 JetBrains 技能做诊断闭环。
2. **试**：`mengto-design-game-encounters` + `mengto-tune-enemy-ai` + `mengto-create-game-vfx`，在已有 isometric-arpg 切片上做「一波遭遇 → 可读 telegraph → 奖励」闭环。
3. **个人化**：把 `heycat-comfyui-lowvram-setup` 的固定 seed/采样器清单收成自己的等距资产生成 checklist，接到已入库 `asset-pipeline-automation`。
