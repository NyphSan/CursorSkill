# ARCH_MEMO · 主程定界

- **Project：** SCL
- **需求 ID：** F4
- **主程：** lead-eng
- **栈适配器：** ue-framework
- **GAME_ROOT：** `E:\Project\Game\S_\SCL`
- **主题：** 业务层收口 — `SCL.Build.cs` 依赖方向；业务不承载已迁 Core 实现；无 include/模块倒灌；Presenter/3C 仍在业务
- **依据：** ARCH-F0 · ARCH-F2 · ARCH-F3 · DONE-F2 · DONE-F3 · PM-F3

---

## 定层

- **层：** 工程框架 / 业务模块边界收口（**验证 + 文档 + 极小删改**；非大搬迁）。
- **理由（ue-framework + F0/F2/F3 现场）：**
  1. F2 已将清单 A（22 文件）迁入 `SCLCore` 并自 `Source/SCL` 删除源实现；F3 已将 ATBS 迁为 `SCLTactical` 且 `SCL.Build.cs` Private 依赖已改名。
  2. F4 目标是**确认业务侧无双份真源、依赖单向、include 吃 Core 模块头**，并修正仍指向旧路径的模块内 README；**不**借机下沉 ARCH-F2 清单 B 或 Bootstrap。
  3. Presenter→ViewState 与 3C 契约（ARCH-F0 / 战旗定版）**永久留业务**；禁止以「收口」名义塞进 Core。

---

## 现状核对（GAME_ROOT 扫描，定界依据）

| 点 | 现场 | 结论 |
|----|------|------|
| F2 双份实现 | `Source/SCL` 无 `SCLFrameworkTypes` / `DateSystem` / `SCLDesignDataCatalog` 等已迁 `.h/.cpp` | ✅ 无双份；业务 `#include "Framework/…"` / `"Calendar/…"` / `"DesignData/…"` 经 **Public `SCLCore`** 解析 |
| 转发头 | `Source/SCL` 未发现仅 `#include` 转发的薄头 | ✅ 无需删转发（本刀若发现则删） |
| 旧路径 include | 业务 `.h/.cpp` **无** `#include "Rules/World/…"` / `"World/SCL…"` / `"Infrastructure/DesignData/SCLDesignDataCatalog.h"` 等 | ✅ 代码 include 已对齐 Core |
| 模块倒灌 | `SCLCore.Build.cs` → Engine only；`SCLTactical.Build.cs` → `SCLCore` + Engine；**均不**依赖 `SCL` | ✅ 无倒灌 |
| 业务依赖 | `SCL.Build.cs`：Public `SCLCore`；Private `SCLTactical` | ✅ 符合 F0 链 `SCL → SCLTactical → SCLCore → Engine` |
| 业务残留 Rules | `Rules/World/WorldLayerMapSubsystem.*`、`Rules/Calendar/SCLCalendarDisplay.*` | 属 **清单 B**（F2 延后）；**本刀不搬** |
| 业务残留 Infrastructure | DesignData **四子系统** + `Bootstrap/SCLCoreBootstrapSubsystem.*` + `SCLBPLibrary.*` | 属 **清单 B / Bootstrap**；**本刀不搬** |
| Adjudication | `DreamExitAdjudication.*` 留业务；`SCLAdjudicationTypes.h` 已在 Core | ✅ 符合 F2 |
| Presenter / 3C | 均在 `Content/Tactical/`、`Content/Control/`、`Content/UI/` | ✅ 未进 Core；**本刀禁止改契约/实现** |
| UATBS* 过渡 | ~30 个业务文件仍 `#include "ATBS*.h"` / `UATBS*` | F3 **刻意保留**；完整更名 **非 F4**（另开 ARCH） |
| 文档债 | `Source/SCL/README.md`、`Rules/README.md`、`Adjudication/README.md` 仍写旧路径；`docs/dev/SCL_SourceLayout.md` 仍写 `Plugins/ATBS` | **F4 允许修**（见允许路径） |
| 脏文件 | `HostileVisionComponent.*`、`SCLPlayerBotSmokeCommands.cpp` 工作区改动 | **非 F4**；EXEC 勿混入 gitea commit |

---

## F4 允许 / 禁止路径（写死）

### 依赖与 include 原则（施工须遵守）

```text
业务 Source/SCL
  │  Public  → SCLCore（消费 Framework / Calendar / DesignData 叶 / AdjudicationTypes / SessionManifest）
  │  Private → SCLTactical（消费 ATBS 过渡头 / UATBS* 战旗 API）
  ▼
Plugins/SCLTactical → SCLCore → Engine

禁止：SCLCore 或 SCLTactical → 模块 SCL
禁止：业务 Public 头再暴露「已删的旧 Source/SCL 路径」
禁止：为蓝图/UHT 在 Source/SCL 重建已迁 Core 的实现或双份类型
```

| 允许 | 禁止 |
|------|------|
| 业务 `#include` Core Public 头（`Framework/`、`Calendar/`、`DesignData/` 叶节点、`Adjudication/SCLAdjudicationTypes.h`、`FeatureModule/`） | 把 Presenter / ViewState / Bridge / Flow / 3C 迁入 Core |
| `SCL.Build.cs` 注释/依赖微调（须保持 Public SCLCore + Private SCLTactical） | 改 `SCLCore.Build.cs` / `SCLTactical.Build.cs` 引入对 `SCL` 的依赖 |
| 删除 `Source/SCL` 内**已确认**的 F2 残留双份或纯转发头（扫描当前为 0） | 搬迁 ARCH-F2 清单 B 任一文件 |
| 更新模块内 README + `docs/dev/SCL_SourceLayout.md` 中 **ATBS/SCLCore 路径** 说明 | 大范围改 `docs/design/**`（另债） |
| `Bootstrap` 头文件**仅注释**标明「业务 Bootstrap，非 SCLCore 插件」 | 改 Bootstrap / 四子系统 **实现语义** |
| 编译修复（include 路径、模块依赖）且 **零玩法变更** | 改 Bridge/开战/EndTurn/Presenter 行为；改 D3 可达圆；改 UATBS* 类型名 |

---

## 当刀文件清单（可薄 · F4 施工范围）

路径均相对 `GAME_ROOT`。**默认仅下列 + 编译连带修复**；未列禁止改。

### A. 必做（DoD 硬项）

| # | 路径 | 动作 |
|---|------|------|
| 1 | `Source/SCL/SCL.Build.cs` | 验证 Public `SCLCore` + Private `SCLTactical`；补 **依赖链注释**（F0 定版）；无倒灌模块 |
| 2 | `Source/SCL/README.md` | 修正 Include 示例与目录表：Core 类型指向 `Plugins/SCLCore`；业务留 WorldLayer / CalendarDisplay / DesignData 子系统 |
| 3 | `Source/SCL/Rules/README.md` | 区分「已迁 Core」与「仍留业务」文件 |
| 4 | `Source/SCL/Adjudication/README.md` | `SCLAdjudicationTypes` → Core；`DreamExitAdjudication` 留业务 |
| 5 | `docs/dev/SCL_SourceLayout.md` | `Plugins/ATBS` → `Plugins/SCLTactical`；注明 Demo NON-PRODUCTION |

### B. 可选（施工自选，不计 FAIL）

| # | 路径 | 动作 |
|---|------|------|
| 6 | `Source/SCL/Infrastructure/README.md` | 注明 DesignData 叶节点在 Core、四子系统在业务 |
| 7 | `Source/SCL/Infrastructure/Bootstrap/SCLCoreBootstrapSubsystem.h` | 一行注释：类名 ≠ 插件 `SCLCore`；留业务模块（ARCH-F2 策略） |

### C. 明确不动（红线）

- `Source/SCL/Content/Tactical/**`（Presenter / ViewState / Bridge / Flow）
- `Source/SCL/Content/Control/**`（3C / Input / Camera / Command / Bot）
- `Source/SCL/Content/UI/**`
- `Infrastructure/DesignData/*Subsystem.*`（四子系统）
- `Infrastructure/Bootstrap/SCLCoreBootstrapSubsystem.cpp`（实现）
- `Infrastructure/SCLBPLibrary.*`
- `Rules/World/WorldLayerMapSubsystem.*`、`Rules/Calendar/SCLCalendarDisplay.*`
- `Adjudication/DreamExitAdjudication.*`
- `Plugins/SCLCore/**`、`Plugins/SCLTactical/**`（除编译报错且仅因业务 include 的连带，须 EXEC 说明）
- `HostileVisionComponent.*`、`SCLPlayerBotSmokeCommands.cpp` 等工作区脏文件

---

## 清单 B / Bootstrap 裁定

| 组 | ARCH-F2 状态 | **F4 裁定** | 理由 |
|----|--------------|-------------|------|
| DesignData 四子系统（Mount / DesignData / Session / Pipeline） | 清单 B，绑 `USCLGameInstance` / `PlayerAction` / `WorldLayerMap` | **不纳入 F4** → 另开 **F4b（或 F5 前独立 ARCH）** | 下沉需 GI/Consumer 接口化，否则 Core→业务倒灌 |
| `USCLCoreBootstrapSubsystem` | F2 定版留业务 | **不纳入 F4**（仅允许头注释） | cpp 绑 Content + 四子系统 + GI；与 F4「收口验证」无关 |
| `UWorldLayerMapSubsystem` / `SCLCalendarDisplay` | 清单 B | **不纳入 F4** → 随 F4b 或更后 | 绑 DreamSession / PlayerAction |
| `DreamExitAdjudication` | 绑 DreamSession | **永久留业务**（非下沉对象） | 关口编排属内容域 |
| `SCLBPLibrary` | 永久留业务 | **不纳入 F4** | 聚合 3C/Presenter/Tactical API |

**结论：** F4 = **业务层验证收口 + 模块内文档**；清单 B 与 Bootstrap **整体另刀**，不在本 ARCH 扩 scope。

---

## 硬规则

1. 依赖方向永久：**SCL → SCLTactical → SCLCore → Engine**；发现 Core/Tactical 依赖 `SCL` → 停工。
2. **无双份真源：** `Source/SCL` 不得再出现 F2 清单 A 的 `.h/.cpp` 实现；仅允许经 `SCLCore` 模块 include。
3. **Presenter→ViewState 定版：** 唯一读出口不变；禁止 WBP/View 直读 Battle；禁止把 Presenter/3C 塞进 Core。
4. **清单 B / Bootstrap：** 本刀 **零搬迁**；仅可选 Bootstrap 头注释。
5. **UATBS* 更名：** 非 F4 DoD；不得借机改类型名/文件名。
6. 无本 ARCH「批准开工 F4 施工」→ 禁止改 `GAME_ROOT`；需越界 → 停工 → 主程改备忘。

---

## DoD（F4 施工刀）

| # | 项 |
|---|-----|
| 1 | 扫描确认：`Source/SCL` **无** F2 清单 A 双份实现或纯转发头 |
| 2 | `SCL.Build.cs` 依赖方向正确（Public SCLCore、Private SCLTactical）；**无**倒灌 |
| 3 | `SCLCore` / `SCLTactical` **不**依赖模块 `SCL` |
| 4 | 清单 A（必做）README / `SCL_SourceLayout.md` 已更新；旧 include 示例不再指向已删路径 |
| 5 | Presenter / ViewState / Bridge / 3C **零**逻辑/契约改动 |
| 6 | 清单 B / Bootstrap **未**搬迁或改实现语义 |
| 7 | `SCLEditor`：`SCL` + `SCLCore` + `SCLTactical` 编译 Succeeded |
| 8 | EXEC 写明「遵守 ARCH-F4」+ 扫描结论 + 编译证据 + 实际改动文件表 |

---

## 非目标

- 本定界刀改 `GAME_ROOT`（写 ARCH-F4 本身除外）
- 搬迁 DesignData 四子系统 / Bootstrap / WorldLayer / CalendarDisplay
- `UATBS*` → `USCLTactical*` 完整更名
- 改 Bridge/开战/EndTurn/Presenter 行为、D3 可达圆、HostileVision 脏改动
- 把 Presenter/3C 迁入 Core
- 大范围更新 `docs/design/**` 路径引用（可记债，非 F4 DoD）

---

## 主程签字

- **结论：批准开工 F4 施工**
- **否决项：** 无（F2/F3 PASS；现场无双份 Core 实现；依赖链已正确；本刀 scope 薄且可执行）
- **补充信息：** 不需要额外老板输入；清单 B/Bootstrap 已书面裁定另刀。
- 执行须严格落在「当刀文件清单 A + 可选 B」；交付 EXEC 对照 DoD。
- F4 完成后可进入 F5（组织 profile）；F4b（清单 B 下沉）须独立 ARCH。
