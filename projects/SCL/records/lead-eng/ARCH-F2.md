# ARCH_MEMO · 主程定界

- **Project：** SCL
- **需求 ID：** F2
- **主程：** lead-eng
- **栈适配器：** ue-framework
- **GAME_ROOT：** `E:\Project\Game\S_\SCL`
- **主题：** 首批迁入 SCLCore 清单锁定（定界刀；本文件不搬代码）
- **依据：** ARCH-F0 · DISPATCH-F2 · PM-F1 · EXEC-F1（PASS）

---

## 定层

- **层：** 工程框架 / 插件边界（SCLCore 首批搬迁清单）。
- **理由：** F0 已定依赖方向与类别建议，但未写死文件表；PM-F1 明确「不可直接开 F2 施工」。本刀只锁**可零倒灌迁入**的首批路径与施工 DoD；子系统中仍绑业务 Content 的实现**本刀不搬**。

---

## 现状核对（相对 F0/F1）

| 点 | 现场 | 结论 |
|----|------|------|
| `Plugins/SCLCore` | F1 空壳已 PASS；Public 锚点 `SCLCore::PluginApiVersion` | 施工目标模块已存在 |
| `Infrastructure/DesignData` | Types/Catalog/Manifest/PipelineTypes 叶节点干净；Mount/DesignData/Session/Pipeline **子系统** cpp 触 `USCLGameInstance` / `PlayerAction` / `WorldLayerMap` | **叶节点进首批**；子系统延后 |
| `Infrastructure/FeatureModule` | `SCLSessionManifestTypes` + Subsystem 仅依赖 `SCLGameInstanceUtil` | **整组进首批** |
| `Rules/World` | `SCLFrameworkTypes` / `Guards` / `GameplayTransitionReason` 无业务 include；`WorldLayerMapSubsystem` 重绑 Dream/PlayerAction/GI | **类型+Guards+Util+MapDefaults+RegistryRow 进首批**；WorldLayer 子系统延后 |
| `Rules/Calendar` | `EventData` / `CountdownTimer` / `DateSystem` 干净；`SCLCalendarDisplay` 绑 PlayerAction | **前三者进首批**；Display 延后 |
| `Adjudication` | `SCLAdjudicationTypes` 纯类型；`DreamExitAdjudication` 绑 DreamSession | **仅 Types 进首批**；DreamExit 留业务 |
| `Bootstrap` | `USCLCoreBootstrapSubsystem` 类名 ≠ 插件；cpp 绑 Content + DesignData 子系统 + GI | **F2 施工不搬**（见专节） |
| `SCLBPLibrary` | 聚合 3C / Presenter / ATBS / Dream | **永久留业务**（本刀与后续 F2+ 均禁止进 Core） |
| ATBS / Presenter / 3C | 未改 | **本刀禁止触碰** |

---

## 首批迁入清单（F2 施工刀 · 写死）

路径均相对 `GAME_ROOT`。源在 `Source/SCL/...`，目标落在 `Plugins/SCLCore/Source/SCLCore/`（Public/Private 按 UObject 可见性；建议目录镜像如下）。

### A. 必须迁入（首批 DoD 范围）

| # | 源路径 | 建议目标（SCLCore 内） | 说明 |
|---|--------|------------------------|------|
| 1 | `Source/SCL/Rules/World/SCLFrameworkTypes.h` | `Public/Framework/SCLFrameworkTypes.h` | 世界层/玩法状态等共享契约 |
| 2 | `Source/SCL/Rules/World/SCLFrameworkGuards.h` | `Public/Framework/SCLFrameworkGuards.h` | 铁律守卫（仅依赖 Types） |
| 3 | `Source/SCL/Rules/World/SCLGameplayTransitionReason.h` | `Public/Framework/SCLGameplayTransitionReason.h` | 过渡原因枚举 |
| 4 | `Source/SCL/Rules/World/SCLGameInstanceUtil.h` | `Public/Framework/SCLGameInstanceUtil.h` | GI 解析工具（Engine-only） |
| 5 | `Source/SCL/Rules/World/SCLMapDefaults.h` | `Public/Framework/SCLMapDefaults.h` | 默认关卡名常量 |
| 6 | `Source/SCL/Rules/World/SCLWorldMapRegistryRow.h` | `Public/Framework/SCLWorldMapRegistryRow.h` | 地图登记行（依赖 EventData+Types） |
| 7 | `Source/SCL/Rules/Calendar/EventData.h` | `Public/Calendar/EventData.h` | 历法/事件基础类型 |
| 8 | `Source/SCL/Rules/Calendar/CountdownTimer.h` | `Public/Calendar/CountdownTimer.h` | 倒计时 |
| 9 | `Source/SCL/Rules/Calendar/CountdownTimer.cpp` | `Private/Calendar/CountdownTimer.cpp` | 同上 |
| 10 | `Source/SCL/Rules/Calendar/DateSystem.h` | `Public/Calendar/DateSystem.h` | 主历+行动点钱包子系统 |
| 11 | `Source/SCL/Rules/Calendar/DateSystem.cpp` | `Private/Calendar/DateSystem.cpp` | 同上（仅 Util，无 Content） |
| 12 | `Source/SCL/Infrastructure/DesignData/SCLDesignDataTypes.h` | `Public/DesignData/SCLDesignDataTypes.h` | 配表枚举/描述符 |
| 13 | `Source/SCL/Infrastructure/DesignData/SCLDataPipelineTypes.h` | `Public/DesignData/SCLDataPipelineTypes.h` | Pipeline 类型 |
| 14 | `Source/SCL/Infrastructure/DesignData/SCLDataPipelineTypes.cpp` | `Private/DesignData/SCLDataPipelineTypes.cpp` | 同上 |
| 15 | `Source/SCL/Infrastructure/DesignData/SCLDesignDataCatalog.h` | `Public/DesignData/SCLDesignDataCatalog.h` | Catalog DataAsset |
| 16 | `Source/SCL/Infrastructure/DesignData/SCLDesignDataCatalog.cpp` | `Private/DesignData/SCLDesignDataCatalog.cpp` | 同上 |
| 17 | `Source/SCL/Infrastructure/DesignData/SCLDesignDataManifest.h` | `Public/DesignData/SCLDesignDataManifest.h` | 表描述 Manifest |
| 18 | `Source/SCL/Infrastructure/DesignData/SCLDesignDataManifest.cpp` | `Private/DesignData/SCLDesignDataManifest.cpp` | 同上 |
| 19 | `Source/SCL/Infrastructure/FeatureModule/SCLSessionManifestTypes.h` | `Public/FeatureModule/SCLSessionManifestTypes.h` | Feature Manifest 类型 |
| 20 | `Source/SCL/Infrastructure/FeatureModule/SCLSessionManifestSubsystem.h` | `Public/FeatureModule/SCLSessionManifestSubsystem.h` | Manifest 子系统 |
| 21 | `Source/SCL/Infrastructure/FeatureModule/SCLSessionManifestSubsystem.cpp` | `Private/FeatureModule/SCLSessionManifestSubsystem.cpp` | 同上 |
| 22 | `Source/SCL/Adjudication/SCLAdjudicationTypes.h` | `Public/Adjudication/SCLAdjudicationTypes.h` | DM 共享类型（无子系统） |

**迁入伴随（允许，计入施工）：**

- 上述文件内 `SCL_API` → `SCLCORE_API`（模块 API 宏）。
- 业务侧 `#include` / `PublicIncludePaths` 适配；旧路径**删除源文件**（禁止双份实现）；可用一次性转发头仅当 UHT/蓝图路径强制需要，且转发头本身不得含实现。
- `Plugins/SCLCore/Source/SCLCore/SCLCore.Build.cs` — 仅当 UObject/子系统需要时补最小官方模块（如已有 Core/CoreUObject/Engine 不足再加）。
- `Source/SCL/SCL.Build.cs` — 保持对 `SCLCore` 依赖；可改为 Public 依赖若业务大量 include Core 头（施工自选，不得引入倒灌）。
- `Plugins/SCLCore/Source/SCLCore/Public/SCLCore.h` — 可更新锚点注释/版本说明（可选）。

### B. 明确不进首批（延后刀；本施工禁止搬）

| 源路径 / 组 | 原因 |
|-------------|------|
| `Infrastructure/DesignData/SCLDesignDataMountSubsystem.*` | cpp `Cast<USCLGameInstance>` 绑业务 GI |
| `Infrastructure/DesignData/SCLDesignDataSubsystem.*` | Consumer 绑 `PlayerAction` / `WorldLayerMap` |
| `Infrastructure/DesignData/SCLSessionDataSubsystem.*` | 会话数据装配，随 DesignData 子系统链 |
| `Infrastructure/DesignData/SCLApplicationDataPipelineSubsystem.*` | Pipeline 编排，随上 |
| `Infrastructure/Bootstrap/SCLCoreBootstrapSubsystem.*` | 见下节；绑 Content |
| `Infrastructure/SCLBPLibrary.*` | 业务聚合门面（3C/Presenter/ATBS） |
| `Rules/World/WorldLayerMapSubsystem.*` | 绑 DreamSession / PlayerAction / GI |
| `Rules/Calendar/SCLCalendarDisplay.*` | 绑 PlayerAction / WorldLayer |
| `Adjudication/DreamExitAdjudication.*` | 绑 `DreamSessionTypes`（业务内容） |
| 全部 `Content/**`、`Plugins/ATBS/**`、Presenter/ViewState/3C | F0 红线；非 Core |

### C. 摘要（≤5 条，给主控/施工）

1. **Framework：** `SCLFrameworkTypes` + `Guards` + `GameplayTransitionReason` + `GameInstanceUtil` + `MapDefaults` + `WorldMapRegistryRow`
2. **Calendar：** `EventData` + `CountdownTimer` + `DateSystem`（不含 CalendarDisplay）
3. **DesignData 叶节点：** Types / DataPipelineTypes / Catalog / Manifest（**不含** Mount/DesignData/Session/Pipeline 四子系统）
4. **SessionManifest：** Types + Subsystem 整组
5. **Adjudication：** 仅 `SCLAdjudicationTypes.h`；Bootstrap / BPLibrary / WorldLayer / DreamExit **不搬**

---

## USCLCoreBootstrapSubsystem 与插件 SCLCore 处理策略

| 项 | 定版 |
|----|------|
| 命名共存 | **允许**：插件/模块名 `SCLCore` ≠ 类名 `USCLCoreBootstrapSubsystem`。禁止为此新建 `Plugins/SCL` 或改插件名为 Bootstrap。 |
| F2 施工位置 | **保留在** `Source/SCL/Infrastructure/Bootstrap/`，**不迁入** SCLCore。 |
| 理由 | 实现依赖 `USCLGameInstance`、`UPlayerActionSubsystem`、`UWorldLayerMapSubsystem` 及尚未迁入的 DesignData 子系统；迁入会迫使 Core→业务倒灌，或把业务子系统拖进 Core。 |
| API 宏 | 继续 `SCL_API`（游戏模块）；Core 内新类型用 `SCLCORE_API`。 |
| 后续（非本刀） | 待 DesignData 子系统链迁入且 Bootstrap 对业务依赖改为接口/委托后，另开 ARCH（如 F2b/F4）再评估是否下沉或改名（如 `USCLGameBootstrapSubsystem`）。 |
| 文档/注释 | 施工刀可在类头注释标明「业务模块 Bootstrap；非 SCLCore 插件本体」；非强制。 |

---

## 允许改的路径（F2 施工刀）

相对 `GAME_ROOT`：

1. **迁出删除：** 上表「A. 必须迁入」列出的 `Source/SCL/...` 源文件（迁入后不得残留双份实现）。
2. **迁入新建/写入：** `Plugins/SCLCore/Source/SCLCore/**`（对应 Public/Private 文件；可调目录名但须一对一覆盖清单文件）。
3. **模块规则：** `Plugins/SCLCore/Source/SCLCore/SCLCore.Build.cs`（最小官方依赖增补）。
4. **业务适配：** `Source/SCL/**` 内**仅**为消费已迁 API 所需的 `#include`、模块依赖方向、以及删除旧路径后的编译修复；**禁止**借机改玩法逻辑。
5. **可选：** `Plugins/SCLCore/.../Public/SCLCore.h` 锚点说明；`Source/SCL/SCL.Build.cs` Public/Private 对 SCLCore 调整。

**本定界刀（写 ARCH-F2）：** 仅组织仓本文件；禁止改 `GAME_ROOT`。

---

## 禁止改的路径（越界红线）

- `Plugins/ATBS/**`；新建 `Plugins/SCL`；新建/改名 `Plugins/SCLTactical`（属 F3）
- `Source/SCL/Content/Tactical/**`（Presenter / ViewState / Bridge / Flow 等）
- `Source/SCL/Content/Control/**`（3C / Input / Camera / Command / Character）
- `Source/SCL/Content/UI/**`、WBP 表现逻辑
- 「B. 明确不进首批」整表
- 借搬迁改数值、改可达圆、改回合公式、改 ALS/VRM4U
- **倒灌：** `SCLCore` 模块依赖游戏模块 `SCL` 或 ATBS

---

## 硬规则

1. 依赖方向永久：**业务（SCL）→ 战斗（SCLTactical/ATBS）→ 核心（SCLCore）→ Engine**；本刀不得引入任何反向模块依赖。
2. **禁止倒灌：** Core 内不得 `#include` `Source/SCL/Content/**` 或链接模块 `SCL`；发现则停工改备忘。
3. **不动 ATBS / Presenter：** 本刀零改动 ATBS 与 Presenter→ViewState 契约；3C 同禁。
4. **仅搬清单 A：** 未列文件禁止迁入；子系统链（DesignData 四子系统、Bootstrap、WorldLayer、BPLibrary）另刀。
5. **无双份真源：** 迁入后源路径删除或仅允许无实现转发；业务编译须吃 Core 头。
6. **Bootstrap 策略写死：** 类留业务模块；与插件名共存；本刀不改其实现语义（允许仅注释）。
7. 无本 ARCH「批准开工 F2 施工」→ 禁止搬迁；需越界 → 停工 → 主程改备忘。

---

## DoD（F2 施工刀）

| # | 项 |
|---|-----|
| 1 | 清单 A 全部文件已落入 `Plugins/SCLCore`，`Source/SCL` 无双份实现 |
| 2 | `SCLCore` **不**依赖模块 `SCL` / `ATBS`；`SCL` 依赖 `SCLCore`（及现有 ATBS）方向不变 |
| 3 | `USCLCoreBootstrapSubsystem` 仍在业务模块；实现未借机大改 |
| 4 | 未改 ATBS、Presenter/ViewState、3C、清单 B |
| 5 | `SCLEditor`：至少 `SCLCore` + `SCL` 模块编译 Succeeded |
| 6 | EXEC 写明「遵守 ARCH-F2 定界」+ 编译证据 + 实际搬迁文件表 |

---

## 非目标

- 本定界刀搬代码或改 `GAME_ROOT`
- F3 ATBS→SCLTactical
- 迁 DesignData 四子系统 / Bootstrap / WorldLayer / BPLibrary / DreamExit
- 重命名 `USCLCoreBootstrapSubsystem`
- 改玩法数值、Presenter 契约、3C

---

## 主程签字

- **结论：批准开工 F2 施工**
- **否决项：** 无（F1 壳就绪；首批可按「叶节点+干净子系统」零倒灌迁入；Bootstrap 策略已锁为留业务）
- 执行须严格落在上文「允许改的路径」与清单 A；交付 EXEC 对照 DoD。
- 清单 B 与 Bootstrap 下沉须另开 ARCH，不得凭本备忘扩搬。
