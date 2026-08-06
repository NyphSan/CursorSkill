# 技能侦察 DIGEST — 2026-08-06（09:00Z）

- 侦察时间：2026-08-06T09:00Z（cron）
- 目标分支：**CursorSkillSearch**（强制；不使用 skill-digest-*）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：Memories 2026-08-06 08:00Z（inventory；PR#31 / DIGEST 275 清单）
- 本仓入库：精选 **279** 个 `SKILL.md`（相对 CursorSkillSearch 旧态 275：+4）
- 结构：`skills/<方向>/<skill-name>/SKILL.md`（精选摘录，非整仓镜像）

## 一屏结论

种子仓无方向相关新 skill。按基线「下次优先」续摘 MengTo 观望簇中的 **monster-system / hybrid-assets / fog-of-war / changelog**（MIT；vesperfall 仍过专属未收）。新发现 **fagemx/gstack-game**（MIT 58★，完整制作工作流 29 技能）列入观望待择优。今日新建噪声约 50+；KrickmanC 设计簇偏产品/品牌 UI；Yuki/kevin/Stanestane/QQstone 仍无 LICENSE。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| mengto-build-game-monster-system | 游戏设计·3D | 怪物资产合同：定义/绑定/运行时/视图分层 | https://github.com/MengTo/Skills | 接 enemy-systems / tune-enemy-ai / combat；含 contract 参考 | **引入** |
| mengto-build-hybrid-game-assets | 游戏设计·3D·2D | 混合资产管线：导入/程序几何/2D UI 选型 | 同上 | 防「凡事 image-to-3D」；provenance 清晰 | **引入** |
| mengto-implement-fog-of-war | 游戏设计·3D | 战争迷雾：CPU 感知真值 + 软着色 | 同上 | 感知与表现分离；含 mechanics/validation | **引入** |
| mengto-build-game-changelog | 游戏设计·工作流 | 游戏内更新日志与版本账本 | 同上 | 接 ship-web；部署 provenance | **引入** |

本仓路径：

- `skills/game-design/mengto-build-game-monster-system/`（+ agents/ + references/）
- `skills/game-design/mengto-build-hybrid-game-assets/`（+ agents/）
- `skills/game-design/mengto-implement-fog-of-war/`（+ agents/ + references/）
- `skills/game-design/mengto-build-game-changelog/`（+ agents/ + references/）

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| fagemx/gstack-game | 游戏设计·工作流 | 从创意到发版的 29 技能制作工作流 | https://github.com/fagemx/gstack-game | MIT 58★；需 Bun build；与 donchitos 有重叠，下轮择优摘 triage/review/feel | **观望（新增）** |
| MengTo vesperfall-review-assets | 游戏设计·3D | Vesperfall 资产目录评审对 | https://github.com/MengTo/Skills | 项目专属过强 | **观望（维持/降优）** |
| KrickmanC/{design,ui-styling,design-system,banner…} | UI·设计 | 离线 Codex 产品/品牌设计簇 | https://github.com/KrickmanC/design 等 | 今日新建 MIT；偏产品/WPF 非 UMG | **观望（新增）** |
| SCKOROT/game-design-document-creater | 游戏设计 | 中文交互式 GDD 生成 | https://github.com/SCKOROT/game-design-document-creater | MIT 16★；本仓已有 game-design-document | 观望 |
| miramocha/blender-skills-and-rules | 3D | VRoid/VRM 清理技能簇 | https://github.com/miramocha/blender-skills-and-rules | 有 SKILL.md；**无 LICENSE** | 观望 |
| zabrodsk/app-store-assets | UI·设计 | App Store 视觉资源 | https://github.com/zabrodsk/app-store-assets | 今日新建；**无 LICENSE**；非游戏 UI | 观望/低优 |
| SherryCW/shigeru-miyamoto | 游戏设计 | 宫本茂式体验评审 | https://github.com/SherryCW/shigeru-miyamoto | 方向贴合但 **无 LICENSE** | 观望 |
| jasonxu610/game-design-skills | 游戏设计 | 书籍提炼原则/tips | https://github.com/jasonxu610/game-design-skills | 7★ 今日有星标活动；**无 LICENSE** | 观望 |
| Dylanyz/ARKitRemap · Heybinshao/affinity · jas0nh/zine-poster · educlopez/ui-craft · kevin/Yuki/Stanestane/QQstone · Flue/roble3 · OpenGame… | 各向 | 维持上轮 | 各原仓 | LICENSE/过窄/非游戏主路径未变 | 观望 |

## 可忽略

- 种子：JackyST0 仍仅 08-03 star chore；mouadja02 仍为 08-05 idea-refine（方向无关）
- 今日新建噪声约 50+：GitHub Skills 练习仓、作品集、通用 agent/devops、Penumbra useful-skills（通用编码）、Ninglz/vox-video（空仓）、honggaofei meta-skill 等
- 作弊/外挂类一律忽略；eve-skills 非通用游戏/UE

## 种子仓状态

| 仓 | stars | 近况 | 备注 |
|---|---:|---|---|
| JackyST0/awesome-agent-skills | 614 | 仍仅 08-03 star chore | 无 UE/游戏专区新增 |
| mouadja02/skills | 9 | 仍为 08-05 18:06Z idea-refine | 方向无关 |

## 今天可行动

1. 把 Cursor Remote Rule / skills 指向本仓 **`CursorSkillSearch`** 的 `skills/`（PR#31）
2. Three.js 遭遇链试跑：`mengto-build-hybrid-game-assets` → `mengto-build-game-monster-system` → `mengto-tune-enemy-ai`（已有）
3. 需要视野/潜行时挂 `mengto-implement-fog-of-war`；发版后玩家可见变更用 `mengto-build-game-changelog`

## 查询记录

1. 种子仓 commits / meta（JackyST0、mouadja02）
2. 跟踪仓 license/pushed（MengTo、JetBrains、Yuki、kevin、Stanestane、QQstone、affinity、zine-poster、ui-craft、Flue、OpenGame、gisenberg、sipher、donchitos、omer、heycat、arg-games、ChloeVPin、bomkino、ARKitRemap、roble3 等）
3. repos search：skills created:>=2026-08-06；agent skills created:>=2026-08-05；unreal / game design / blender skills
4. code search：`game design filename:SKILL.md`（Unreal path 遇 429 后重试部分成功）；skills.sh：unreal / game design / blender / ui design
5. 候选探测：MengTo 续摘 4、fagemx/gstack-game、KrickmanC、SCKOROT、miramocha、zabrodsk、SherryCW、jasonxu、Ninglz、Penumbra、MCERQUA、roby2358、GuangminJu、apetrov（已入库）
6. 入库：+4 → push `CursorSkillSearch` + 更新 PR#31
