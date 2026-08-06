# 技能侦察 DIGEST — 2026-08-06（08:00Z）

- 侦察时间：2026-08-06T08:00Z（cron）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：Memories 2026-08-06 07:00Z（inventory；PR#30 / skill-digest-2026-08-06-07 的 270 清单）
- 本仓入库：精选 **275** 个 `SKILL.md`（相对 CursorSkillSearch 旧态 266：+9；相对 07:00 清单 270：+2 新摘录）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

种子仓无方向相关新 skill。`CursorSkillSearch` 落后于 07:00 automation 的 7 项「建议引入」→ **本轮已合并入库**。相对 07:00 基线的**新增量**：续摘 MengTo **test-playable-web-games** + **build-mobile-threejs-games**（补齐发版后的可玩验证与移动端）。今日新建噪声约 50+；Yuki/kevin/Stanestane/QQstone 仍无 LICENSE；zine-poster 07:52Z 有更新但仍偏海报编辑。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| jetbrains-ue-code-authoring | UE·工作流 | Rider MCP 辅助写/改 UE C++ | https://github.com/JetBrains/rider-skills | Apache-2.0；CSS 缺漏，合并自 07:00 | **引入**（已摘录） |
| jetbrains-ue-live-debugging | UE·工作流 | 崩溃/运行时调试：调用链/断点/PIE | 同上 | 官方技能簇收齐 | **引入**（已摘录） |
| mengto-ship-web-games | 游戏设计·工作流 | Web 发版：部署证明与回滚 | https://github.com/MengTo/Skills | CSS 缺漏，合并自 07:00 | **引入**（已摘录） |
| mengto-build-threejs-enemy-systems | 游戏设计·3D | 数据驱动敌人原型/招式 | 同上 | 接 tune-enemy-ai | **引入**（已摘录） |
| mengto-optimize-threejs-games | 游戏设计·3D | 性能诊断与低风险优化 | 同上 | 先测后改 | **引入**（已摘录） |
| mengto-build-game-map-editor | 游戏设计·工作流 | 生产数据派生的关卡编辑器 | 同上 | 权威边界清晰 | **引入**（已摘录） |
| mengto-build-game-audio-feedback | 游戏设计·2D·3D | 动作/战斗音频反馈 | 同上 | 与 VFX/遭遇互补 | **引入**（已摘录） |
| mengto-test-playable-web-games | 游戏设计·工作流 | 可玩性端到端测试与浏览器证据 | 同上 | 接 ship-web；防「绿构建≠好玩」 | **引入（本轮新）** |
| mengto-build-mobile-threejs-games | 游戏设计·3D·UI | 移动 Web：触控/安全区/性能预算 | 同上 | 补移动主路径；与 HUD/测试矩阵衔接 | **引入（本轮新）** |

本仓路径：

- `skills/unreal/jetbrains-ue-code-authoring/`（+ reference/）
- `skills/unreal/jetbrains-ue-live-debugging/`（+ reference/）
- `skills/game-design/mengto-ship-web-games/`（+ agents/）
- `skills/game-design/mengto-build-threejs-enemy-systems/`（+ agents/）
- `skills/game-design/mengto-optimize-threejs-games/`（+ agents/）
- `skills/game-design/mengto-build-game-map-editor/`（+ agents/ + references/）
- `skills/game-design/mengto-build-game-audio-feedback/`（+ agents/）
- `skills/game-design/mengto-test-playable-web-games/`（+ agents/）
- `skills/game-design/mengto-build-mobile-threejs-games/`（+ agents/）

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| MengTo 其余（monster-system / hybrid-assets / changelog / fog-of-war / vesperfall…） | 游戏设计·3D | 更垂直切片 | https://github.com/MengTo/Skills | 发版+测试+移动已齐；按需续摘 | **观望（调整）** |
| Dylanyz/ARKitRemap | UE·动画 | MHA→ARKit 面部曲线重映射 | https://github.com/Dylanyz/ARKitRemap | MPL-2.0 25★；有 SKILL.md，但极窄 FaceIt/MetaHuman | **观望（新增）** |
| jas0nh/zine-poster-skill | 2D·设计 | zine 海报/拼贴 | https://github.com/jas0nh/zine-poster-skill | 07:52Z 仍活跃；偏编辑海报非游戏 UI | 观望 |
| Heybinshao/affinity-help | 2D·设计 | Affinity 中文问答 | https://github.com/Heybinshao/affinity-help | MIT；体积过大 | 观望 |
| kevinpbuckley/unreal-engine-skills | UE | UE 5.8 技能簇 | https://github.com/kevinpbuckley/unreal-engine-skills | 27★ **无 LICENSE** | 观望 |
| Yuki001 / Stanestane / QQstone | 游戏设计·2D | 维持上轮 | 各原仓 | 仍无 LICENSE；Yuki 06:42Z 后无新推 | 观望 |
| educlopez/ui-craft · ConnorGriffin · bomkino · ChloeVPin | UI·设计 | Web/品牌/产品 UI | 各原仓 | 非 UMG/游戏 UI 主路径 | 观望 |
| sfkislev/flue · roble3/cc-blender-skill（增量） · Oliyf | 3D·工作流 | Blender 桥/完整插件簇/镜像 | 各原仓 | 本仓已有 blender-*；roble3 可作补源 | 观望 |
| petascale4/UnrealSkills · gisenberg · sipher · OpenGame · xsolla-ai-kit | UE 等 | UAssetAPI / 登录商店 | 各原仓 | 无 LICENSE 或厂商绑定 | 观望 |

## 可忽略

- 种子：JackyST0 仍仅 08-03 star chore；mouadja02 仍为 08-05 idea-refine（方向无关）
- 今日新建噪声约 50+：通用 coding/devops/练习/作品集仓（含 ohqay harness、kopfwelt design-thinking 等）
- gemdesign-ai/skills：平台原型 CLI，非游戏/UE
- AzraeLLLLL Roblox 空仓；作弊/外挂类一律忽略
- eve-skills：EVE Online API

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | 614 | 仍仅 08-03 star chore | 无 UE/游戏专区新增 |
| mouadja02/skills | 9 | 仍为 08-05 18:06Z idea-refine | 方向无关 |

## 今天可行动

1. 把 Cursor Remote Rule / skills 指向本仓 **`CursorSkillSearch`** 的 `skills/`（勿再跟 skill-digest-*）
2. UE：试 `jetbrains-ue-code-authoring` + `jetbrains-ue-live-debugging`（有 Rider）或继续用 `arg-games-unreal-cqtest`
3. Web/Three.js：`mengto-ship-web-games` → `mengto-test-playable-web-games` → 需要触控时再挂 `mengto-build-mobile-threejs-games`

## 查询记录

1. 种子仓 commits / meta（JackyST0、mouadja02）
2. 跟踪仓 license/pushed（MengTo、JetBrains、Yuki、kevin、Stanestane、QQstone、affinity、zine-poster、ui-craft、Flue、OpenGame、gisenberg、sipher、donchitos、omer、heycat、arg-games、ChloeVPin、Oliyf、bomkino 等）
3. repos search：skills created:>=2026-08-06；agent skills created:>=2026-08-05；unreal / game design skills
4. code search：`SKILL.md Unreal path:.cursor/skills`；skills.sh：unreal / game design / blender
5. 候选探测：MengTo 续摘、Dylanyz/ARKitRemap、toamig、GuangminJu、petascale4、roble3、gemdesign、ohqay、kopfwelt、xsolla、majid、quodsoler、dstn2000、gamedev-skills
6. 入库：合并 digest07 缺漏 7 + 新摘录 2 → push `CursorSkillSearch` + 开/更新 PR
