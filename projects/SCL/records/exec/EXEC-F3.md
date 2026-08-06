# 执行报告

- **需求 ID：** F3
- **执行员工：** exec（ATBS → SCLTactical 插件/模块迁移）
- **结果：** DONE
- **遵守定界：** 是（严格落在 ARCH-F3 阶段 A–E；未改 Presenter/ViewState/Bridge/3C 行为；未做 UATBS* 类型大更名）

## 制作内容

### 插件/模块迁移（ARCH 阶段 A–B）

| 动作 | 结果 |
|------|------|
| `Plugins/ATBS/` → `Plugins/SCLTactical/` | 整树迁移（Content/Config/Source/README）；**无** `Plugins/ATBS/` 残留 |
| `ATBS.uplugin` → `SCLTactical.uplugin` | Name=`SCLTactical`；FriendlyName=`SCL Tactical Battle`；Modules[0]=`SCLTactical` |
| `.uplugin` 插件依赖 | 保留 `EnhancedInput`；**追加** `SCLCore` |
| `Source/ATBS/` → `Source/SCLTactical/` | 模块目录重命名 |
| `ATBS.Build.cs` → `SCLTactical.Build.cs` | 类名 `SCLTactical`；**Public** 依赖 **SCLCore** |
| `IMPLEMENT_MODULE(FATBSModule, ATBS)` → `SCLTactical` | `FATBSModule` 类名保留 |
| 全部 Public `.h` | `ATBS_API` → **`SCLTACTICAL_API`**（20 个头文件） |
| 新建 `Public/ATBSCompat.h` | `#define ATBS_API SCLTACTICAL_API` 兼容别名 |
| `ATBSModule.h` | `#include "ATBSCompat.h"` |
| **保留** | `UATBS*` / `EATBS*` / `FATBS*` 类型名；`ATBS*.h/.cpp` 文件名；业务 `#include "ATBS*.h"` **零改动** |

### 项目与业务 Build（ARCH 阶段 C）

| 文件 | 改动 |
|------|------|
| `SCL.uproject` | 插件 `ATBS` → **`SCLTactical`**（仅一项 Enabled，无双插件） |
| `Source/SCL/SCL.Build.cs` | Private `"ATBS"` → **`"SCLTactical"`** |
| `Source/SCL/**` 业务 C++ | **未改** include/类型/Bridge/Presenter/3C 逻辑 |

### Demo Content 与 Config（ARCH 阶段 D）

| 文件 | 改动 |
|------|------|
| `Plugins/SCLTactical/Content/**` | 原样随插件迁移 |
| `Plugins/SCLTactical/Config/DefaultEngine.ini` | 保留 `/Game/ATBS`→`/ATBS`；**追加** `/ATBS`→`/SCLTactical`（MatchSubstring） |
| `Plugins/SCLTactical/Config/DefaultGame.ini` | 注释路径更新为 `/SCLTactical/` |
| `Plugins/SCLTactical/README.md` | 插件名/挂载点/启用说明更新；Demo 仍 NON-PRODUCTION |

### ATBS 脏改动基线（PM-F2 披露 · 纳入本迁移）

- **基线 commit：** `779494e1` feat(sclcore): migrate first-batch framework and data types into SCLCore
- **迁入 SCLTactical 的未提交改动（D1/D2 高低差）：**
  - `ATBSTacticalSettings.h`：新增 `MaxStepHeightDelta`（默认 90cm）
  - `ATBSUnitComponent.cpp`：`HorizontalPlusAbsZ` 预算、`MaxStepHeightDelta` 截断、Tick 跟 Z（Dist3D 到达、Z 校正、终点 Snap XYZ）
- **说明：** 属 ARCH 允许的 D1/D2 工程债合入；**非** F3 新扩 scope

### 工作区其他脏文件（非 F3 范围 · 未触）

- `Source/SCL/Content/Combat/HostileVisionComponent.{h,cpp}` — 工作区另有未提交改动；**本刀未改**

### 未改（红线）

- **未**改 `FSCLTacticalViewState` / Presenter→ViewState 契约
- **未**改 Bridge/Flow/EndTurn 语义、3C/Command 行为
- **未**批量 `UATBS*`→`USCLTactical*` 类型更名
- **未**新建 `Plugins/SCL`；**无** SCLTactical→SCL / SCLCore→SCLTactical 倒灌
- **无** ATBS 与 SCLTactical 双插件并存

## 依赖链验证

```text
SCL ──Private──► SCLTactical ──Public──► SCLCore ──► Engine
SCL ──Public──► SCLCore
```

| 检查项 | 结果 |
|--------|------|
| `SCLTactical.Build.cs` Public 含 SCLCore | 是 |
| `SCLTactical.uplugin` Plugins 含 SCLCore | 是 |
| `SCLCore.Build.cs` 无 SCLTactical/ATBS | 是 |
| `SCLTactical` 无 → `SCL` 依赖 | 是 |

## 编译证据

```text
Build.bat SCLEditor Win64 Development -Project=E:\Project\Game\S_\SCL\SCL.uproject -Module=SCLTactical
→ Result: Succeeded（约 29s；编出 UnrealEditor-SCLTactical.dll · 2026-08-06 21:36:55）

Build.bat SCLEditor Win64 Development -Project=E:\Project\Game\S_\SCL\SCL.uproject -Module=SCL
→ Result: Succeeded（约 22s；编出 UnrealEditor-SCL.dll · 2026-08-06 21:37:21）
```

引擎：`E:\Epic Games\UnrealEngine-5.6.1-release`

UHT：SCLTactical 模块 55 个头反射写入；SCL 模块 5 个头更新（插件名变更触发）。

## 类型过渡说明

插件/UBT 模块对外名定版 **SCLTactical**；`UATBS*` / `EATBS*` / `ATBS*.h` 为历史别名，完整类型更名 **不在本刀 DoD**，须另开 ARCH。

## 自检对照 DoD（ARCH-F3）

| DoD 项 | 自检 |
|--------|------|
| 存在 `Plugins/SCLTactical/` + `SCLTactical.uplugin`；无 `Plugins/ATBS/`；uproject 仅 SCLTactical | 是 |
| UBT 模块 SCLTactical 编译成功；Build.cs Public 依赖 SCLCore；uplugin 声明 SCLCore | 是 |
| SCL 模块编译成功；SCL.Build.cs Private 依赖 SCLTactical | 是 |
| 无 SCLTactical→SCL；无 SCLCore→SCLTactical | 是 |
| UATBS*/EATBS* 保留；ATBSCompat.h 提供 ATBS_API 别名 | 是 |
| Demo Content 已迁移；DefaultEngine.ini 含 /ATBS→/SCLTactical 重定向 | 是 |
| 未改 Presenter/ViewState、Bridge/Flow 语义、3C、移动/射击公式（除已纳入的 D1/D2 脏改动） | 是 |
| EXEC 含定界声明 + 编译证据 + 改动表 + ATBS 脏改动基线 | 是 |

## 给审核的线索

- 静态：`Plugins/SCLTactical/SCLTactical.uplugin`、`Source/SCLTactical/SCLTactical.Build.cs`、`Public/ATBSCompat.h`
- 搜残留：`Plugins/ATBS` 应不存在；`SCL.uproject` 无 `"Name": "ATBS"`
- 搜倒灌：`SCLCore.Build.cs` 仅 Core/CoreUObject/Engine
- 搜双插件：uproject Plugins 数组仅一条 SCLTactical
- 编译：见上两条 Succeeded + dll 时间戳
