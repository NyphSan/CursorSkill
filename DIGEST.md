# 技能侦察 DIGEST — 2026-08-05（10:00Z）

- 侦察时间：2026-08-05T10:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T09:00Z（同日上一轮，PR#9）
- 本仓入库：精选 **108** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-05-10`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓仍无方向相关新 skill。跟踪仓最大实质变化是 [kevinpbuckley/unreal-engine-skills](https://github.com/kevinpbuckley/unreal-engine-skills)（25★，08-04 合并 UE **5.8** retarget，并暴露此前未入库的 **Mover** skill）。本轮以**缺口补齐**为主：① Mover（CMC 继任）；② [gamedev-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) 的 Behavior Trees / Enhanced Input / Packaging；③ [quodsoler](https://github.com/quodsoler/unreal-engine-skills)（301★ MIT）的 Mass / StateTree / Sequencer；④ 观望晋级 Italink `unreal-modeling`。`path:.cursor/skills` 仍易 429；今日 `skill` 新建噪声 ≥100。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| ue-mover-movement-system | UE | UE 5.8 Experimental Mover：模块化/回滚网络移动，CMC 继任 | https://github.com/kevinpbuckley/unreal-engine-skills | 新项目移动架构关键；含 3 份 references；贴合 5.8 retarget | **引入** |
| unreal-behavior-trees | UE·游戏设计 | NPC AI：BT/Blackboard/Task/Decorator/Service | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 413★ Apache-2.0；skills.sh 高安装；本仓 AI 空白 | **引入** |
| unreal-enhanced-input | UE | IA_/IMC_、修饰器/触发器、C++/BP 绑定 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 现代 UE5 输入默认路径；含 cpp-setup 参考 | **引入** |
| unreal-packaging | UE·工作流 | Package/Cook/Shipping + RunUAT BuildCookRun | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 补齐出包/CI 流程缺口 | **引入** |
| ue-mass-entity | UE | Mass Entity ECS：人群/大规模实体模拟 | https://github.com/quodsoler/unreal-engine-skills | 301★ MIT；~18KB + patterns；本仓无 Mass 覆盖 | **引入** |
| ue-state-trees | UE | StateTree 数据驱动状态机（含 Mass 集成） | https://github.com/quodsoler/unreal-engine-skills | 与 BT 互补的现代 AI/逻辑框架 | **引入** |
| ue-sequencer-cinematics | UE·3D | Sequencer 过场 / 相机 / Movie Render Queue | https://github.com/quodsoler/unreal-engine-skills | 补齐过场与离线渲染工作流 | **引入** |
| unreal-modeling | UE·3D | 经 UCP + GeometryScript 的程序化网格建模总控 | https://github.com/Italink/UnrealClientProtocol | 从观望晋级；MIT；需编辑器+UCP；入口已入库 | **引入** |

本仓已摘录：

- `skills/unreal/ue-mover-movement-system/`（+ references）
- `skills/unreal/unreal-behavior-trees/`（+ references）
- `skills/unreal/unreal-enhanced-input/`（+ references）
- `skills/unreal/unreal-packaging/`
- `skills/unreal/ue-mass-entity/`（+ references）
- `skills/unreal/ue-state-trees/`（+ references）
- `skills/unreal/ue-sequencer-cinematics/`（+ references）
- `skills/unreal/unreal-modeling/`

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| kevinpbuckley UE 5.8 retarget | 08-04 合并 #47；全文 citation 审计；本轮已收 Mover | https://github.com/kevinpbuckley/unreal-engine-skills | 已引入子集继续用；其余 core skills 按需 |
| w-zhian/game-design-skills | 08-04 v2.3.2 curation 规则；无新设计 skill | https://github.com/w-zhian/game-design-skills | 剩余 article-curation / qa-review / skill-evolution 仍观望 |
| miramocha/blender-skills-and-rules | 仍为 08-04 推送；无 SPDX | https://github.com/miramocha/blender-skills-and-rules | 仍观望 |
| hkuds/cli-anything | ★46645；无新方向 skill | https://github.com/hkuds/cli-anything | 仍观望 |
| sipherxyz/universal-ue-skills | 仍无 SPDX；RenderDoc skill 质量尚可 | https://github.com/sipherxyz/universal-ue-skills | 仍观望（待许可） |

### 累计建议引入（仍有效）

1–41. 维持上轮清单（含 toamig / GuangminJu / gamestudio / unreal-gas-cpp 等）  
42. **+ 本轮** kevinpbuckley `mover-movement-system`  
43. **+ 本轮** gamedev-skills：behavior-trees / enhanced-input / packaging  
44. **+ 本轮** quodsoler：mass-entity / state-trees / sequencer-cinematics  
45. **+ 本轮晋级** Italink `unreal-modeling`

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| quodsoler 其余（game-features / networking / character-movement 等） | UE | 27 skills 中未精选部分 | https://github.com/quodsoler/unreal-engine-skills | 与已有 toamig/kevin/GuangminJu 部分重叠 | 观望 |
| unrealxu 其余（pcg-building / architecture / performance-packaging…） | UE | 491★ MIT 的 UE5 skill 包剩余项 | https://github.com/unrealxu/unrealengine5-skills | 本仓已有 blueprint/cpp/umg 子集 | 观望 |
| w-zhian qa-review / article-curation / skill-evolution | 游戏设计·工作流 | 设计验收 / 文章蒸馏 / 技能自演化 | https://github.com/w-zhian/game-design-skills | 无 SPDX；qa-review 清单清晰可下轮精选 | 观望 |
| sipherxyz renderdoc-gpu-debug 等 | UE·工作流 | RenderDoc/内存/XR/复制审查 | https://github.com/sipherxyz/universal-ue-skills | 质量可，缺 LICENSE | 观望 |
| gisenberg AngelScript/P4/PIE | UE·工作流 | 编辑器自动化 niche | https://github.com/gisenberg/unreal-skills | 0★ 无 SPDX | 观望 |
| TomLeeLive OpenClaw / petascale4 UAssetAPI / NoxDevelopment unrealgen | UE·工作流 | 远程驱 UE / 离线 uasset / primers | 各原仓 | 维持上轮观望 | 观望 |
| Italink niagara-editing + modeling-* 子 skill | UE·3D | Niagara/细分建模操作 | https://github.com/Italink/UnrealClientProtocol | 总控已引入；子包按需 | 观望 |
| NAJEMWEHBE/unreal-ai-connection / UnrealMCPHub / august-batista bridge | UE·工作流 | MCP/桥接类 | 各原仓 | 与已有 Epic MCP / UCP / VibeUE 重叠 | 观望 |
| cesiumgs/cesiumjs-skills | 3D | CesiumJS 地理空间 | https://github.com/cesiumgs/cesiumjs-skills | 110★ Apache-2.0；偏地球可视化非游戏核心 | 观望 |
| sfkislev/flue | 3D·工作流 | CLI 控桌面 DCC（Blender/Houdini…） | https://github.com/sfkislev/flue | 65★ MIT；安装面大但非 SKILL 精选包 | 观望 |
| alterlab-ieu/alterlab_gameforge | 游戏设计 | 34 个独立游戏工作室 skill | https://github.com/alterlab-ieu/alterlab_gameforge | 23★ MIT；与已有策划库重叠，抽样后再定 | 观望 |

其余观望（lpf513、story-to-game、OpenGame、miramocha、fairypark/oliver-io、hkuds、pluginagentmarketplace、opusgamelabs、cowork-os 等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 仍仅 08-03 star chore；mouadja02 近提交仍为 Qdrant / Terraform / K8s（无关）  
- `created:>=2026-08-05` 今日新建噪声 **≥100**  
- code search 噪声：majiayu000 巨型镜像、modbender、j4flmao（cocos 非 UE）、paxlabs/matrix-core、junainfinity/VibeStudio  
- alvinunreal/oh-my-opencode-slim：通用 agent 套件，非游戏向 skill 包  
- 含 “Unreal skills” 字样的作业/作品展示仓（非 Agent Skills）

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | 08-04：Qdrant / Terraform（无关）；无游戏/UE/设计向 |

## 本仓入库变化（+8 → 108）

- 新增 `skills/unreal/ue-mover-movement-system/`  
- 新增 `skills/unreal/unreal-behavior-trees/`  
- 新增 `skills/unreal/unreal-enhanced-input/`  
- 新增 `skills/unreal/unreal-packaging/`  
- 新增 `skills/unreal/ue-mass-entity/`  
- 新增 `skills/unreal/ue-state-trees/`  
- 新增 `skills/unreal/ue-sequencer-cinematics/`  
- 新增 `skills/unreal/unreal-modeling/`  
- 各含 `SOURCE.md`；承接上轮 100 条精选内容  

## 今天可行动

1. **评估是否上 Mover**：新角色/联机移动前先读 `ue-mover-movement-system`（含 networking-and-backends），和现有 CMC 路径做一次「继续 CMC vs 迁 Mover」决策；5.8 Experimental，勿盲目全量迁移。  
2. **装三件日常高频**：`unreal-enhanced-input` + `unreal-behavior-trees` + `unreal-packaging`（Apache-2.0，可直接进 Cursor skills）。  
3. **个人 skill 候选**：若做人群/开放世界 AI，把 `ue-mass-entity` + `ue-state-trees` 的 Mass 集成章合并成个人 `/ue-mass-ai`；若已用 UCP，把 `unreal-modeling` 链到已有 `unreal-client-protocol`。

## 已尝试查询

1. 种子仓 commits / meta API（JackyST0、mouadja02）  
2. 跟踪仓 `pushed_at`（kevinpbuckley、w-zhian、miramocha、sipherxyz、gisenberg、OpenClaw、maystudios、Italink、hkuds、flue、quodsoler、unrealxu、gamedev-skills 等）  
3. `gh search repos`：`unreal skill` created≥08-04；`skill created:>=2026-08-05`；blender/gamedev 关键词  
4. `gh search code`：`Unreal filename:SKILL.md`（成功一轮，见 Italink modeling 等；`path:.cursor/skills` 仍易 429）  
5. skills.sh/api/search：unreal、gamedev、blender、game ui/design、houdini、niagara、3d modeling、sequencer、umg、ue5、flue  
6. 候选 raw `SKILL.md` + 入库 / push / PR  
