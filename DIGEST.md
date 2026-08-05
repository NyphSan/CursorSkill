# 技能侦察 DIGEST — 2026-08-05（13:00Z）

- 侦察时间：2026-08-05T13:00Z（cron）
- 方向：游戏设计 / UE·虚幻 / 3D / 2D / UI / 研发工作流
- 增量基线：2026-08-05T12:00Z（同日上一轮，PR#12）
- 本仓入库：精选 **132** 个 `SKILL.md`（较上轮 +8；非整仓镜像），结构 `skills/<方向>/<skill-name>/`
- 关联 PR 分支：`skill-digest-2026-08-05-13`

## 本轮结论（一屏）

距上轮约 1 小时。种子仓无方向相关新 skill（JackyST0 仍停在 08-03 star chore；mouadja02 仍为 10:11Z SBOM，无关）。跟踪仓无新实质 push。本轮按上轮「下次优先」继续**缺口补齐**：① [quodsoler](https://github.com/quodsoler/unreal-engine-skills)（301★ MIT）补 CMC / Networking·Replication / Niagara C++ / Editor Tools；② [gamedev-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)（414★ Apache-2.0）补 physics-tuning / performance / shader / input 四纪律。新发现 [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter)（1646★ MIT）内含大量 UE 薄层 skill（Chaos/Lumen/Nanite…）入观望；今日新建噪声含 `hao-skills`（插画 persona）、PPT/阅读类，方向相关性弱。code search 仍偶发 429。

## 建议引入（本轮增量）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| ue-character-movement | UE | CMC / Phys* 管线 / 自定义移动 / 网络预测 / Root Motion | https://github.com/quodsoler/unreal-engine-skills | 301★ MIT；与已有 `ue-mover-movement-system` 互补（经典 CMC vs 新 Mover） | **引入** |
| ue-networking-replication | UE | 复制 / RPC / NetRole / 权威与预测；含 patterns 参考 | https://github.com/quodsoler/unreal-engine-skills | 完整 MIT 网络包；与 `unreal-replication` 互补加深 | **引入** |
| ue-niagara-effects | UE | 从 C++ 控制 Niagara：参数 / DI / 生命周期 / 性能 | https://github.com/quodsoler/unreal-engine-skills | 补「运行时驱动」侧；与已有 Niagara 创作/MCP 形成闭环 | **引入** |
| ue-editor-tools | UE | Editor Utility / Blutility / Detail 定制 / UToolMenus | https://github.com/quodsoler/unreal-engine-skills | 本仓此前缺独立编辑器扩展 skill；工具链刚需 | **引入** |
| gamedev-physics-tuning | 游戏设计 | 固定步长 / CCD / 抖动 / 碰撞层 / 质量·阻力手感 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~902 安装；与 `ue-physics-collision` 互补（设计 vs UE API） | **引入** |
| gamedev-performance-optimization | 游戏设计 | 先测量再优化：帧预算 / 池化 / 合批 / GC / 资源预算 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~943 安装；跨引擎方法，含 UE 分析器指针 | **引入** |
| gamedev-shader-programming | 游戏设计 | 顶点→片元管线 / UV / dissolve·outline·fresnel（GLSL+HLSL） | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~884 安装；与 `hlsl-shader` / 材质 skill 互补 | **引入** |
| gamedev-input-systems | 游戏设计 | Action 映射 / 重绑 / 多设备 / deadzone / buffer·coyote | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | ~923 安装；与 `unreal-enhanced-input` 形成设计→API 链路 | **引入** |

本仓已摘录：

- `skills/unreal/ue-character-movement/`（+ references）
- `skills/unreal/ue-networking-replication/`（+ references）
- `skills/unreal/ue-niagara-effects/`（+ references）
- `skills/unreal/ue-editor-tools/`（+ references）
- `skills/game-design/gamedev-physics-tuning/`（+ references）
- `skills/game-design/gamedev-performance-optimization/`（+ references）
- `skills/game-design/gamedev-shader-programming/`（+ references）
- `skills/game-design/gamedev-input-systems/`（+ references）

### 跟踪仓变化（非实质 / 不升级建议）

| 名称 | 变化 | 仓库 | 建议 |
|---|---|---|---|
| mouadja02/skills | 仍为 10:11Z SBOM；无更新 | https://github.com/mouadja02/skills | **忽略**（DevOps） |
| JackyST0/awesome-agent-skills | 仍仅 08-03 star chore | https://github.com/JackyST0/awesome-agent-skills | 无游戏/UE 专区新增 |
| kevinpbuckley | 仍为 08-04 推送；无 SPDX；UDS/UDW 独特但许可风险 | https://github.com/kevinpbuckley/unreal-engine-skills | 维持观望 |
| sipherxyz | 仍无 LICENSE；偏工具链/合规检查 | https://github.com/sipherxyz/universal-ue-skills | 维持观望 |
| aws-deadline / maystudios / flashpoint493 / omer-metin | 无新实质变化 | 各原仓 | 维持观望 |

### 累计建议引入（仍有效）

1–52. 维持至上轮（含 Physics/Features/Data/Actor/Camera/Save/Procgen/Feel 等）  
53. **+ 本轮** quodsoler：character-movement / networking-replication / niagara-effects / editor-tools  
54. **+ 本轮** gamedev-skills：physics-tuning / performance-optimization / shader-programming / input-systems

## 观望（本轮新增 / 调整）

| 名称 | 方向标签 | 一句话用途 | 仓库链接 | 为什么值得关注 | 建议 |
|---|---|---|---|---|---|
| a5c-ai/babysitter unreal-chaos / lumen / nanite / networking… | UE·游戏 | 巨型库内大量 UE/游戏 specialization skill | https://github.com/a5c-ai/babysitter | 1646★ MIT；08-05 有推送；内容偏能力清单薄层，质量待逐条核 | 观望 |
| a596116/hao-skills（hao-visual / oil-visual） | 2D·设计 | 暖色手帳风一致插画 / 透明角色素材 | https://github.com/a596116/hao-skills | 今日新建；有明确 SKILL.md；0★ persona 向 | 观望 |
| quodsoler 其余（async-threading / materials-rendering / testing-debugging / module-build / project-context…） | UE | 27 skills 中未精选部分 | https://github.com/quodsoler/unreal-engine-skills | 本轮再收 4 个；其余按需 | 观望 |
| gamedev-skills dialogue-systems / audio-design / genres / workflows | 游戏设计·工作流 | 对话 / 类型包 / 原型·发行流程 | https://github.com/gamedev-skills/awesome-gamedev-agent-skills | 纪律四件套已收；其余按项目类型再取 | 观望 |
| aws-deadline / maystudios / omer-metin / flashpoint493 | UE·UI | 维持上轮观望理由 | 各原仓 | 重叠或许可/栈特定 | 观望 |
| kevinpbuckley UDS/UDW / gameplay-tags / landscape | UE | 无 SPDX；天气/天空包独特 | https://github.com/kevinpbuckley/unreal-engine-skills | 许可未变 | 观望 |
| sipherxyz / Italink / flue / cesiumjs / abagames 其余 | UE·3D·工作流 | 维持上轮观望理由 | 各原仓 | 许可或重叠未变 | 观望 |

其余观望（teixasalone、TerminalSkills、ibrews、lpf513、story-to-game、OpenGame、pluginagentmarketplace、opusgamelabs 等）维持上轮清单。

## 可忽略

- 种子仓：JackyST0 无实质新条目；mouadja02 **SBOM identity matching**（方向无关，记数）
- 今日新建噪声：`hao-skills` 以外大量 GitHub Skills 练习仓、`Binaryify/open-kimi-ppt-skill`（PPT）、`hec-ovi/observer-skill`（视频学习）、`nchyj/web-skill-creator`（通用工具链）
- code search 噪声：majiayu000 巨型镜像、作业/作品展示仓
- chris58530/gamedev-skills：0★；树中未见可用 `SKILL.md` 结构

## 种子仓状态

| 仓 | stars | 近况 |
|---|---:|---|
| https://github.com/JackyST0/awesome-agent-skills | 613 | 最近实质提交仍为 07-27；08-03 star chore |
| https://github.com/mouadja02/skills | 9 | **08-05 10:11Z**：SBOM identity matching（无关）；此后无新 commit |

## 本仓入库变化（+8 → 132）

- 新增 `skills/unreal/ue-character-movement/`
- 新增 `skills/unreal/ue-networking-replication/`
- 新增 `skills/unreal/ue-niagara-effects/`
- 新增 `skills/unreal/ue-editor-tools/`
- 新增 `skills/game-design/gamedev-physics-tuning/`
- 新增 `skills/game-design/gamedev-performance-optimization/`
- 新增 `skills/game-design/gamedev-shader-programming/`
- 新增 `skills/game-design/gamedev-input-systems/`
- 各含 `SOURCE.md`；承接上轮 124 条精选内容

## 今天可行动

1. **装移动/网络双件套（MIT）**：`ue-character-movement` + `ue-networking-replication`，与已有 Mover / GAS 拼成「经典 CMC + 复制权威」联机角色包。  
2. **试物理手感闭环**：先用 `gamedev-physics-tuning` 定固定步长/CCD/层掩码策略，再用 `ue-physics-collision` 落到 Chaos 通道与 Trace。  
3. **个人 skill 候选**：若做工具向，把 `ue-editor-tools` + 已有 MCP/UMG 合成 `/ue-editor-utility`；若做手感/操作，把 `gamedev-input-systems` + `unreal-enhanced-input` 合成 `/ue-input-feel`。

## 已尝试查询

1. 种子仓 commits / meta API（JackyST0、mouadja02）  
2. 跟踪仓 `pushed_at` / trees（kevinpbuckley、quodsoler、gamedev-skills、sipherxyz、aws-deadline、maystudios、abagames、omer-metin、flashpoint493 等）  
3. `gh search repos`：`unreal skills`；`gamedev skills`；`skill` created≥08-05  
4. `gh search code`：`Unreal filename:SKILL.md`（429→成功部分）；`UnrealEngine filename:SKILL.md`；`path:.cursor/skills Unreal`（429）  
5. skills.sh/api/search：unreal、gamedev、blender、game design、niagara、umg、houdini、3d modeling、sequencer、state tree、mover、angelscript、ui design、character movement、physics tuning、performance、shader、input systems  
6. 候选 raw/blob `SKILL.md` + 入库 / push / PR  
