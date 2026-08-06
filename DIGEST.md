# 技能侦察 DIGEST — 2026-08-06（07:00Z）

- 侦察时间：2026-08-06T07:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-06T06:00Z（同日上一轮，PR#29）
- 本仓入库：精选 **270** 个 `SKILL.md`（较上轮 +7；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-06-07`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。跟踪仓：`Yuki001` 06:42Z 持续改 skill 但仍无 LICENSE；`Oliyf` 再次仅 README；`affinity-help` v1.1.0 扩至 ~859 篇仍过大。按「下次优先」升级引入 **JetBrains** `ue-code-authoring` + `ue-live-debugging`，并续摘 **MengTo** 发版/敌人系统/优化/地图编辑器/音频（5）。今日新建噪声约 50+；`jas0nh/zine-poster-skill`（MIT 海报）与空仓 Roblox → 观望/忽略。kevin / Stanestane / QQstone 仍无 LICENSE。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| jetbrains-ue-code-authoring | UE·工作流 | Rider MCP 辅助写/改 UE C++（诊断/lint） | https://github.com/JetBrains/rider-skills | Apache-2.0；接上轮 test-authoring 成写码闭环 | **引入** |
| jetbrains-ue-live-debugging | UE·工作流 | Rider MCP 调试崩溃/运行时：调用链/断点/PIE | 同上 | 官方技能簇收齐；无 Rider 可降级 | **引入** |
| mengto-ship-web-games | 游戏设计·工作流 | Web/Three.js 发版：部署证明与回滚 | https://github.com/MengTo/Skills | 把「能玩」变成「已证明可上线」 | **引入** |
| mengto-build-threejs-enemy-systems | 游戏设计·3D | 数据驱动敌人原型/招式与运行时边界 | 同上 | 接 tune-enemy-ai / encounters | **引入** |
| mengto-optimize-threejs-games | 游戏设计·3D | 性能诊断与低风险优化闭环 | 同上 | 先测后改；保战斗可读性 | **引入** |
| mengto-build-game-map-editor | 游戏设计·工作流 | 生产数据派生的浏览器关卡编辑器 | 同上 | 权威边界清晰；含 references | **引入** |
| mengto-build-game-audio-feedback | 游戏设计·2D·3D | 动作/战斗音频反馈与浏览器解锁 | 同上 | 与 VFX/遭遇 telegraph 互补 | **引入** |

本仓已摘录：

- `skills/unreal/jetbrains-ue-code-authoring/`（+ reference/）
- `skills/unreal/jetbrains-ue-live-debugging/`（+ reference/）
- `skills/game-design/mengto-ship-web-games/`（+ agents/）
- `skills/game-design/mengto-build-threejs-enemy-systems/`（+ agents/）
- `skills/game-design/mengto-optimize-threejs-games/`（+ agents/）
- `skills/game-design/mengto-build-game-map-editor/`（+ agents/ + references/）
- `skills/game-design/mengto-build-game-audio-feedback/`（+ agents/）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 08-05 18:06Z idea-refine；无新 commit | https://github.com/mouadja02/skills | **忽略**（通用 coding） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| Yuki001/game-dev-skills | 06:03–06:42Z 多笔 improve/prompts；**仍无 LICENSE** | https://github.com/Yuki001/game-dev-skills | **维持观望** |
| Oliyflemishspeaking560/threejs-game-skills | 06:24Z 仅 Update README；0★ MIT | https://github.com/Oliyflemishspeaking560/threejs-game-skills | 观望/低优（疑似镜像 majid） |
| Heybinshao/affinity-help | v1.1.0：~859 篇 + 自动更新器 | https://github.com/Heybinshao/affinity-help | 维持观望（体积过大） |
| ChloeVPin/apple-design-skill | 05:56Z CI/验证；1★ MIT；偏产品 UI | https://github.com/ChloeVPin/apple-design-skill | 维持观望 |
| kevinpbuckley / Stanestane / QQstone | 仍无 LICENSE | 各原仓 | 维持观望 |
| jas0nh/zine-poster-skill | 今日新建 MIT；海报/编辑向 | https://github.com/jas0nh/zine-poster-skill | **观望（新增）** |
| AzraeLLLLL/Codex-Roblox-Studio-Skills | 今日新建空仓 | https://github.com/AzraeLLLLL/Codex-Roblox-Studio-Skills | **忽略** |

### 累计建议引入（仍有效）

1–96. 维持至上轮（含 heycat 主链、mengto encounters 等 5、arg-games CQTest、jetbrains ue-test）  
97. **+ 本轮** JetBrains：ue-code-authoring / ue-live-debugging  
98. **+ 本轮** MengTo：ship-web / enemy-systems / optimize / map-editor / audio-feedback

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| MengTo 其余（monster-system / hybrid-assets / mobile-threejs / test-playable / vesperfall…） | 游戏设计·3D | 更垂直的切片与资产技能 | https://github.com/MengTo/Skills | 主链与发版簇已齐；按需续摘 | **观望（调整）** |
| jas0nh/zine-poster-skill | 2D·设计 | 极简 zine 海报/拼贴与图像生成 | https://github.com/jas0nh/zine-poster-skill | MIT 结构完整，但偏编辑海报非游戏 UI | **观望（新增）** |
| Heybinshao/affinity-help | 2D·设计 | Affinity 官方帮助中文问答 | https://github.com/Heybinshao/affinity-help | MIT；references 近千篇过大 | 观望 |
| ChloeVPin/apple-design-skill | UI·设计 | Apple HIG/动效 Web 化 | https://github.com/ChloeVPin/apple-design-skill | 偏产品 UI | 观望 |
| kevinpbuckley/unreal-engine-skills | UE | 大而全 UE 核心技能簇 | https://github.com/kevinpbuckley/unreal-engine-skills | 25★ **无 LICENSE** | 观望 |
| QQstone / Stanestane / Yuki001 | 2D·游戏设计 | 维持上轮 | 各原仓 | 仍无 LICENSE；Yuki 活跃 | 观望 |
| bomkino / ConnorGriffin / educlopez ui-craft | UI·设计 | 维持上轮 | 各原仓 | 偏品牌/产品 Web | 观望 |
| sfkislev/flue / vladmdgolam / Oliyf | 3D·工作流 | Blender 桥 / MCP / threejs 镜像 | 各原仓 | 依赖或成熟度 | 观望 |
| gisenberg / sipher / lisxa5747 / eve / OpenGame | UE 等 | 维持上轮理由 | 各原仓 | 许可或成熟度 | 观望 |

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 idea-refine（方向无关，记数）
- ConnorGriffin 通用 orchestrate/say-less（非游戏向）
- 今日新建噪声（方向无关，约 50+）：GitHub Skills 练习仓、作品集仓、通用 agent/devops skill 等
- `AzraeLLLLL/Codex-Roblox-Studio-Skills`：空仓
- `Oliyflemishspeaking560`：仅 README 更新
- eve-skills：EVE Online API
- 作弊/外挂类新建仓一律忽略
- GitHub code search 不稳定；以 repos + skills.sh + 跟踪仓 trees 为准

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 仍为 **08-05 18:06Z** idea-refine portable（无关）；此后无新 commit |

## 本仓入库变化（+7 → 270）

- 新增 `skills/unreal/jetbrains-ue-code-authoring/`
- 新增 `skills/unreal/jetbrains-ue-live-debugging/`
- 新增 `skills/game-design/mengto-ship-web-games/`
- 新增 `skills/game-design/mengto-build-threejs-enemy-systems/`
- 新增 `skills/game-design/mengto-optimize-threejs-games/`
- 新增 `skills/game-design/mengto-build-game-map-editor/`
- 新增 `skills/game-design/mengto-build-game-audio-feedback/`
- 各含 `SOURCE.md`；JetBrains 两项含 `reference/`；mengto 五项含 `agents/`；map-editor 含 `references/`；承接上轮 263 条精选内容

## 今天可行动

1. **装**：`skills/unreal/jetbrains-ue-code-authoring` + `jetbrains-ue-live-debugging` — 在已有 CQTest/`ue-test-authoring` 之上，用 Rider MCP 做「写码诊断 → 运行时断点」闭环；无 Rider 时先读 conventions/crash-patterns 参考。
2. **试**：`mengto-build-threejs-enemy-systems` + `mengto-optimize-threejs-games`，把上轮 encounters/enemy-ai 切片收成可数据驱动的敌人定义，再跑一场景帧时对比。
3. **个人化**：把 `mengto-build-game-map-editor` 的「生产源 → 草稿 → 校验导出」边界改成你的 UE/关卡数据 checklist（勿让编辑器草稿直接改权威关卡）。
