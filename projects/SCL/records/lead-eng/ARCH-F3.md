# ARCH_MEMO · 主程定界

- **Project：** SCL
- **需求 ID：** F3
- **主程：** lead-eng
- **栈适配器：** ue-framework
- **GAME_ROOT：** `E:\Project\Game\S_\SCL`
- **主题：** ATBS → **SCLTactical** 插件/模块迁移步骤、依赖 SCLCore、过渡策略
- **依据：** ARCH-F0 · DISPATCH-F3a · PM-F2 · DONE-F2（F2 PASS）

---

## 定层

- **层：** 工程框架 / 战斗插件边界（插件与 UBT 模块改名 + 依赖收口；**不改战旗规则语义**）。
- **理由（ue-framework + F0）：**
  1. 现 `Plugins/ATBS` 已是独立 L0 内核，但对外名与 SCL 产品词（Tactical）不一致，且 **未** 声明对 `SCLCore` 的依赖，与目标依赖链不符。
  2. F3 只做 **落盘位置与模块名** 对齐；`UATBSBattleSubsystem` / Bridge / Presenter→ViewState 契约 **行为不变**。
  3. 完整 `UATBS*`→`USCLTactical*` 类型更名爆破面过大，**本刀明确不做**（F0 非目标）。

---

## 现状核对（GAME_ROOT，定界依据）

| 点 | 现场 | 结论 |
|----|------|------|
| 插件目录 | `Plugins/ATBS/`（`.uplugin` Name=`ATBS`） | F3 整树迁至 `Plugins/SCLTactical/` |
| 模块 | `Source/ATBS/ATBS.Build.cs`；`IMPLEMENT_MODULE(FATBSModule, ATBS)` | 模块名改为 `SCLTactical`；**不**改 `FATBSModule` 类名 |
| 模块依赖 | ATBS → Engine 官方模块；**无** SCLCore | F3 必须加 `SCLCore`（即使 C++ 暂未 `#include` Core 头） |
| 业务依赖 | `SCL.Build.cs` Private `"ATBS"`；`SCL.uproject` 启用 `ATBS` | 改为 `SCLTactical` |
| 业务 include | ~35 个 `.h/.cpp` 含 `#include "ATBS*.h"`、`UATBS*` 类型 | **F3 不改** include 路径与类型名（过渡期） |
| API 宏 | 头文件 `ATBS_API` | 模块改为 `SCLTACTICAL_API` + **兼容别名**（见专节） |
| C++ 源文件 | `Source/ATBS/` 下 40 个 `.h/.cpp`，文件名均 `ATBS*` | **F3 不改文件名** |
| Demo Content | `Plugins/ATBS/Content/`；挂载 `/ATBS/`；`Config/DefaultEngine.ini` 含 `/Game/ATBS`→`/ATBS` 重定向 | 随插件迁移；加 `/ATBS`→`/SCLTactical` 重定向；**仍 NON-PRODUCTION** |
| SCLCore | F2 PASS；`SCL` Public 依赖 `SCLCore` | 不变；SCLTactical **新增** 对 SCLCore 依赖 |
| 生产入口 | `ASCLGameMode` / `BP_GM_SCL` + `USCLTacticalBattleBridge` / Flow / Presenter | F3 **不得**改 Bridge/开战/EndTurn 语义 |
| 工程债 | PM-F2 披露 ATBS 工作区曾有未提交脏改动 | F3 EXEC 须声明基线 commit + 实际 diff 范围 |

---

## 插件 / 模块重命名步骤（F3 施工 · 写死顺序）

路径均相对 `GAME_ROOT`。建议 **单 commit 原子完成**；施工前后 **删** `Plugins/ATBS`（禁止双插件并存）。

### 阶段 A · 目录与描述符

| # | 动作 | 细节 |
|---|------|------|
| A1 | 重命名插件根目录 | `Plugins/ATBS/` → `Plugins/SCLTactical/`（含 `Content/`、`Config/`、`Source/`、`README.md`） |
| A2 | 重命名 `.uplugin` | `ATBS.uplugin` → `SCLTactical.uplugin` |
| A3 | 更新 `.uplugin` 字段 | `"Name": "SCLTactical"`；`FriendlyName` 建议 **「SCL Tactical Battle」**；`Description` 注明由 ATBS 演进；`Modules[0].Name`: **`SCLTactical`** |
| A4 | 声明插件依赖 | `.uplugin` → `"Plugins"` 数组 **追加** `{ "Name": "SCLCore", "Enabled": true }`（保留现有 `EnhancedInput`） |
| A5 | 禁用旧插件名 | `SCL.uproject`：`"Name": "ATBS"` 条目 **替换** 为 `"Name": "SCLTactical", "Enabled": true`（不得 ATBS 与 SCLTactical 同时 Enabled） |

### 阶段 B · UBT 模块

| # | 动作 | 细节 |
|---|------|------|
| B1 | 重命名模块目录 | `Source/ATBS/` → `Source/SCLTactical/` |
| B2 | 重命名 Build 规则 | `ATBS.Build.cs` → `SCLTactical.Build.cs`；类名 `ATBS` → **`SCLTactical`** |
| B3 | 模块实现宏 | `ATBSModule.cpp`：`IMPLEMENT_MODULE(FATBSModule, ATBS)` → **`IMPLEMENT_MODULE(FATBSModule, SCLTactical)`**（`FATBSModule` 类名 **保留**） |
| B4 | API 宏替换 | 全部 `.h` 中 **`ATBS_API` → `SCLTACTICAL_API`**（UHT/导出一致） |
| B5 | 兼容头（必须） | 新建 `Public/ATBSCompat.h`（或并入 `ATBSModule.h` 末尾）：`#ifndef ATBS_API` / `#define ATBS_API SCLTACTICAL_API` / `#endif`；**所有 Public 头**在 `#include` 链上保证业务仍可编译若遗漏个别宏（施工自检） |
| B6 | 清理构建产物 | 删除旧 `Plugins/ATBS/{Binaries,Intermediate}`（新路径同理清一次后全量编） |

### 阶段 C · 项目与业务模块

| # | 动作 | 细节 |
|---|------|------|
| C1 | `SCL.Build.cs` | `PrivateDependencyModuleNames`：`"ATBS"` → **`"SCLTactical"`** |
| C2 | 业务 C++ | **默认零改动** `#include "ATBS*.h"` 与 `UATBS*` 符号；若 UBT 报模块 API 仅因宏，修 compat 头，**禁止**借机改 Bridge/Presenter/3C 逻辑 |
| C3 | 生成工程文件 | 改 `.uproject`/插件后 Regenerate VS 工程（EXEC 记录命令） |

### 阶段 D · Demo Content 与 Config

| # | 动作 | 细节 |
|---|------|------|
| D1 | 随插件迁移 | `Content/**` 原样迁入 `Plugins/SCLTactical/Content/`（**不**改 uasset 内类引用；类名仍为 `AATBSGameMode` 等） |
| D2 | 挂载点变化 | 插件改名后 UE 默认挂载 **`/SCLTactical/`**（原 `/ATBS/`） |
| D3 | 重定向（必须） | 在 `Plugins/SCLTactical/Config/DefaultEngine.ini` **保留**现有 `/Game/ATBS`→`/ATBS` 行，**追加**：`+PackageRedirects=(OldName="/ATBS",NewName="/SCLTactical",MatchSubstring=true)`；若仍有个别 `/Game/ATBS` 硬引用，可追加 `(OldName="/Game/ATBS",NewName="/SCLTactical",MatchSubstring=true)` **或** 保留旧链由 `/ATBS` 二次重定向（二选一，EXEC 注明实测路径） |
| D4 | 编辑器步骤 | 改 Config 后 **重启编辑器**；可选 Fix Up Redirectors on `Plugins/SCLTactical/Content`（**非** F3 DoD 硬门槛；编译+生产入口不断为硬门槛） |
| D5 | README | 更新 `Plugins/SCLTactical/README.md` 路径与插件名；**保留** Demo NON-PRODUCTION 与 `ASCLGameMode` 正式入口说明 |

### 阶段 E · 验证

| # | 动作 |
|---|------|
| E1 | `SCLEditor` 目标：`SCLCore` + `SCLTactical` + `SCL` 编译 **Succeeded** |
| E2 | 确认 **无** 模块 `SCLTactical` → `SCL` 依赖 |
| E3 | EXEC 列出：uproject 插件列表、Build.cs 依赖、是否仍存在 `Plugins/ATBS` |

---

## SCLTactical.Build.cs · 依赖 SCLCore（写死）

在 **`SCLTactical.Build.cs`**（原 ATBS.Build.cs）中：

```csharp
PublicDependencyModuleNames.AddRange(new string[]
{
    // … 保留现有 Core / Engine / EnhancedInput / NavigationSystem / AIModule / UMG / Slate / DeveloperSettings …
    "SCLCore",   // F3 新增 · 硬要求
});
```

| 项 | 定版 |
|----|------|
| 依赖方向 | **SCLTactical → SCLCore → Engine**；禁止 SCLTactical → `SCL` 游戏模块 |
| Public vs Private | **`PublicDependencyModuleNames`** 声明 `SCLCore`（与 F0「战斗依赖 Core」一致；便于后续战旗类型引用 Framework/DesignData 叶节点） |
| F3 是否必须 `#include` Core | **否**；允许零引用先编过；但 Build.cs + `.uplugin` 插件依赖 **必须** 存在 |
| SCLCore 倒灌 | SCLCore **仍不得** 依赖 `SCLTactical` / `ATBS`（F2 已锁） |

`.uplugin` 与 Build.cs **两处** 均声明 SCLCore，避免仅模块链而插件加载顺序异常。

---

## SCL 业务模块 · 依赖如何改（写死）

| 文件 | F3 允许改动 | 定版 |
|------|-------------|------|
| `Source/SCL/SCL.Build.cs` | `PrivateDependencyModuleNames`：`ATBS` → **`SCLTactical`** | **必改** |
| `SCL.uproject` | 插件 `ATBS` → **`SCLTactical`** | **必改** |
| `Source/SCL/**/*.h/cpp` | 仅当 **纯编译** 需要（如误写模块名字符串） | **默认不改**；禁止改 Bridge/Flow/Presenter/3C **行为** |
| `Source/SCL.Target.cs` / `SCLEditor.Target.cs` | 通常 **不改**（无硬编码 ATBS 时） | 若存在 `"ATBS"` 字符串则改为 `SCLTactical` |

**依赖链目标态（F3 后）：**

```text
SCL（业务） ──Private──► SCLTactical ──Public──► SCLCore ──► Engine
         ──Public──► SCLCore
```

业务仍 **Private** 依赖战斗模块（Presenter/Bridge 实现细节不暴露给下游 Target）；与 F0 一致。

---

## UATBS* / EATBS* / FATBS* 类型别名过渡期（写死）

| 维度 | F3 策略 |
|------|---------|
| **UCLASS/USTRUCT/UENUM 名** | **全部保留** `UATBS*`、`AATBS*`、`EATBS*`、`FATBS*`（含 Blueprint 可见名） |
| **头/源文件名** | **保留** `ATBS*.h` / `ATBS*.cpp` |
| **模块对外名** | **必须是** `SCLTactical`（插件 + UBT 模块 + `.uproject`） |
| **API 宏** | 导出改为 **`SCLTACTICAL_API`**；提供 **`#define ATBS_API SCLTACTICAL_API`** 兼容（`ATBSCompat.h`） |
| **模块类** | `FATBSModule` **可保留**；仅 `IMPLEMENT_MODULE` 第二参数改为 `SCLTactical` |
| **UHT Category / ClassGroup** | 可保留 `Category="ATBS|…"`、`ClassGroup=(ATBS)`；**非** F3 必改项 |
| **完整更名** | `USCLTacticalBattleSubsystem` 等 → **另开刀**（F0 非目标）；**不得** 塞进 F3 DoD |
| **文档** | EXEC/README 写一句：「插件名 SCLTactical；类型前缀 ATBS 为历史别名，后续刀更名」 |

**理由：** 业务 ~35 文件、`FSCLTacticalViewState` 已嵌 `EATBSBattlePhase` 等；F3 改类型名会牵动 UHT、蓝图、存档，与「编译+入口不断」底线冲突。

---

## Demo Content 处理（写死）

| 项 | 定版 |
|----|------|
| 定位 | `AATBSGameMode`、`/SCLTactical/Map/DemoMap`（经重定向）等 **永久 NON-PRODUCTION**；AwS 正式仍 **`ASCLGameMode` / `BP_GM_SCL` + Bridge** |
| 物理位置 | 随 `Plugins/SCLTactical/Content/**` 迁移；**F3 不删 Demo** |
| 挂载 / 路径 | 接受 UE 新挂载 `/SCLTactical/`；用 **PackageRedirects** 兼容旧 `/ATBS/` 与 `/Game/ATBS/`（见阶段 D3） |
| WBP 命名 | `WBP_ATBS_TacticalHUD` 等业务资产 **F3 不改名**（属业务 Content，本刀允许路径零触） |
| 禁止 | 用 Demo `ATBSGameMode` 替换正式关；运行 `Scripts/FixATBSAssetPaths.py`（README 已警告毁 uasset） |
| 可选验收 | EXEC 可记：Editor 能加载 DemoMap（**软**）；**硬** DoD 为编译 + 无 ATBS 插件残留 |

---

## 允许改的路径（F3 施工刀）

相对 `GAME_ROOT`：

1. **整树迁移：** `Plugins/ATBS/**` → `Plugins/SCLTactical/**`（含 `Content/`、`Config/`、`Source/`、`README.md`）；完成后 **无** `Plugins/ATBS/`
2. **模块规则：** `Plugins/SCLTactical/Source/SCLTactical/SCLTactical.Build.cs`（含 SCLCore 依赖）
3. **插件描述符：** `Plugins/SCLTactical/SCLTactical.uplugin`
4. **插件 Config：** `Plugins/SCLTactical/Config/DefaultEngine.ini`（PackageRedirects 增补）
5. **项目：** `SCL.uproject`（插件名）
6. **业务 Build：** `Source/SCL/SCL.Build.cs`（模块依赖名）
7. **业务源码：** `Source/SCL/**` — **仅** UBT 编译必需的最小 diff（默认应为 0 行逻辑变更）
8. **构建清理：** 删除旧 ATBS 与新路径下 stale `Intermediate/`/`Binaries/`（本地）

**本定界刀（写 ARCH-F3）：** 仅组织仓本文件；禁止改 `GAME_ROOT`。

---

## 禁止改的路径（越界红线）

- **倒灌：** `SCLTactical` / `SCLCore` 依赖游戏模块 **`SCL`**；`SCLCore` 依赖 `SCLTactical`
- **双插件：** 同时启用 `ATBS` 与 `SCLTactical`；或保留 `Plugins/ATBS/` 与 `Plugins/SCLTactical/` 并行
- **新建 `Plugins/SCL`**
- **类型大_rename：** 批量 `UATBS*`→`USCLTactical*`、改 Blueprint 资产类名（**非 F3**）
- **契约：** 改 `FSCLTacticalViewState` 字段语义；WBP 直读 Battle；多 Presenter 真源
- **业务战旗逻辑：** `Content/Tactical/**` Bridge/Flow/Presenter **实现**；`Content/Control/**` 3C/Command **行为**
- **公式 / 数值：** D1/D2 高低差预算、Tick 跟 Z、可达圆、伤害/移动公式（F0 红线）
- **SCLCore 搬迁：** F2 清单 B、Bootstrap、DesignData 四子系统（属 F2b/F4 ARCH）
- **第三方：** ALS/VRM4U/Blockout 大改
- **借刀改 docs 口径：** `docs/**` 大规模 ATBS→SCLTactical 文档 sweep **非 F3 必做**（可另开文档刀）

---

## 硬规则

1. 无本 ARCH「**批准开工 F3 施工**」→ 禁止 `GAME_ROOT` 改名迁移（组织铁律 `01_no_out_of_bounds`）。
2. 依赖方向：**SCL → SCLTactical → SCLCore → Engine**；发现倒灌 → 停工改备忘。
3. 插件/模块对外名定版：**SCLTactical**；老板口头 ATBS 插件 → 指 **SCLTactical**（类型前缀除外）。
4. 战旗定版（Presenter→ViewState、Command 上行、双域）**行为不变**；只改落盘与 UBT 名。
5. F3 DoD **不包含** 完整类型更名；compat 别名必须有书面说明。
6. Demo **不得** 升格为生产入口；`USCLTacticalBattleBridge` 开战/EndTurn 通道 **不得** 回退。
7. 需越界 → 停工 → 主程改备忘 → 再干。

---

## DoD（F3 施工刀）

| # | 项 |
|---|-----|
| 1 | 存在 **`Plugins/SCLTactical/`** + `SCLTactical.uplugin`；**不存在** `Plugins/ATBS/`；`SCL.uproject` 仅启用 **SCLTactical** |
| 2 | UBT 模块 **`SCLTactical`** 编译成功；`SCLTactical.Build.cs` **Public** 依赖 **`SCLCore`**；`.uplugin` 声明 **SCLCore** 插件依赖 |
| 3 | **`SCL`** 模块编译成功；`SCL.Build.cs` Private 依赖 **`SCLTactical`**（非 ATBS） |
| 4 | **无** `SCLTactical`→`SCL` 模块依赖；**无** `SCLCore`→`SCLTactical` 模块依赖 |
| 5 | **`UATBS*` / `EATBS*` 类型名保留**；`ATBSCompat.h`（或等价）提供 **`ATBS_API`** 别名；EXEC 说明完整类型更名不在本刀 |
| 6 | Demo Content 已随插件迁移；`Config/DefaultEngine.ini` 含 **`/ATBS`→`/SCLTactical`**（及/或 `/Game/ATBS`）重定向说明 |
| 7 | **未改** Presenter→ViewState 契约、Bridge/Flow **语义**、3C 规则、移动/射击/预算 **公式** |
| 8 | EXEC 写明「遵守 ARCH-F3 定界」+ 编译证据 + 实际改动文件表 + ATBS 脏改动基线说明 |

---

## 非目标

- 本定界刀改 `GAME_ROOT` 代码
- 完整 `UATBS*`→`USCLTactical*` 与蓝图资产重绑
- SCLCore 清单 B / Bootstrap 下沉 / DesignData 四子系统
- F4 业务层依赖收口与删重复实现
- 改玩法数值、Presenter UI、3C、ALS/VRM4U
- 文档全仓 ATBS 字样替换

---

## 迁移步骤摘要（给主控 / 施工 · ≤5 条）

1. **`Plugins/ATBS` → `Plugins/SCLTactical`**：`.uplugin`/模块目录/`SCL.uproject` 插件名一律 **SCLTactical**；删旧 ATBS 插件条目与目录。
2. **`SCLTactical.Build.cs`**：模块类名 `SCLTactical`；**Public** 加 **`SCLCore`**；`.uplugin` 同步依赖 SCLCore。
3. **`SCL.Build.cs`**：Private **`ATBS` → `SCLTactical`**；业务 `#include "ATBS*.h"` **默认不动**。
4. **类型过渡**：**保留** `UATBS*`/`EATBS*` 与 `ATBS*.h` 文件名；`ATBS_API`→`SCLTACTICAL_API` + **`#define ATBS_API SCLTACTICAL_API`**。
5. **Demo Content**：随插件迁；Config 加 **`/ATBS`→`/SCLTactical`** 重定向；Demo 仍 NON-PRODUCTION，正式入口仍 Bridge/`ASCLGameMode`。

---

## 主程签字

- **结论：批准开工 F3 施工**
- **否决项：** 无（F0/F2 策略可执行；F2 PASS；SCLCore 已就绪；ATBS 源树清晰、业务仅 Private 模块依赖，可按上文步骤原子迁移）
- 执行须严格落在「允许改的路径」与阶段 A–E；交付 EXEC 对照 DoD。
- **完整 `UATBS*` 类型更名、清单 B 子系统下沉、F4 业务收口** 须各开 ARCH，不得凭本备忘扩 scope。
