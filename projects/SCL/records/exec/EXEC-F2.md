# 执行报告

- **需求 ID：** F2
- **执行员工：** exec（首批迁入 SCLCore）
- **结果：** DONE
- **遵守定界：** 是（严格落在 ARCH-F2 清单 A；未搬清单 B / Bootstrap / ATBS / Presenter / 3C / WorldLayer）

## 制作内容

### 迁入 `Plugins/SCLCore/Source/SCLCore/`（清单 A · 22 文件）

| # | 目标路径 | 说明 |
|---|----------|------|
| 1–6 | `Public/Framework/` · Types / Guards / GameplayTransitionReason / GameInstanceUtil / MapDefaults / WorldMapRegistryRow | World→Framework |
| 7–11 | `Public/Calendar/` + `Private/Calendar/` · EventData / CountdownTimer / DateSystem | 不含 CalendarDisplay |
| 12–18 | `Public/DesignData/` + `Private/DesignData/` · Types / PipelineTypes / Catalog / Manifest | 不含四子系统 |
| 19–21 | `Public/FeatureModule/` + `Private/FeatureModule/` · SessionManifest Types+Subsystem | 整组 |
| 22 | `Public/Adjudication/SCLAdjudicationTypes.h` | 仅 Types |

伴随：`SCL_API` → `SCLCORE_API`；跨 DLL 导出补 `SCLDataPipelineUtil` / `SCLDesignDataManifest` 函数 API。

### 业务适配（仅 include / 模块依赖）

| 文件 | 改动 |
|------|------|
| `Source/SCL/SCL.Build.cs` | `SCLCore` 升为 **Public** 依赖（自 Private 移出） |
| `Source/SCL/**` 约 40 处 | `#include "World/SCL…"` → `"Framework/SCL…"`；`SCLCalendarDisplay.h` 改吃 Core 的 `Calendar/EventData.h` |
| 清单 A 旧路径 | **已删除**（无双份实现、无转发头） |

### 可选锚点

| 文件 | 改动 |
|------|------|
| `Plugins/SCLCore/.../Public/SCLCore.h` | `PluginApiVersion = 2`；注释标明 F2 宿主范围 |

### 未改（红线）

- **未**搬 `USCLCoreBootstrapSubsystem`（仍在 `Infrastructure/Bootstrap/`，`SCL_API`）
- **未**搬 DesignData 四子系统 / WorldLayerMap / CalendarDisplay / DreamExit / BPLibrary
- **未**改 ATBS、Presenter/ViewState 契约、3C 实现逻辑（仅消费侧 include 路径）
- **未**新建 `Plugins/SCL`；**无** Core→SCL / ATBS 倒灌

## 解决方案

- 按 ARCH-F2 目录镜像迁入；Framework 自 `World/` 改名以免与留在业务的 WorldLayer 子系统混淆。
- 依赖方向保持：`SCL` → `SCLCore` → Engine；链接失败时仅补 Core 导出宏，不改玩法。

## 是否遇到问题

- **有（已解决）：** 首编 SCL 时 LNK2019 — `SCLDataPipelineUtil::*` / `SCLDesignDataManifest::*` 未导出。已加 `SCLCORE_API` 后重编通过。

## 编译证据

```text
Build.bat SCLEditor Win64 Development -Project=E:\Project\Game\S_\SCL\SCL.uproject -Module=SCLCore
→ Result: Succeeded（含迁入 cpp 与 Module.SCLCore；编出 UnrealEditor-SCLCore.dll）

Build.bat SCLEditor Win64 Development -Project=E:\Project\Game\S_\SCL\SCL.uproject -Module=SCL
→ Result: Succeeded（导出修复后；编出 UnrealEditor-SCL.dll）
```

引擎：`E:\Epic Games\UnrealEngine-5.6.1-release`

## 自检对照 DoD（ARCH-F2）

| DoD 项 | 自检 |
|--------|------|
| 清单 A 全部落入 SCLCore；Source/SCL 无双份 | 是 |
| SCLCore 不依赖 SCL/ATBS；SCL→SCLCore 方向不变 | 是 |
| Bootstrap 仍在业务模块；实现未借机大改 | 是 |
| 未改 ATBS、Presenter/ViewState、3C、清单 B | 是 |
| SCLEditor：SCLCore + SCL 模块 Succeeded | 是 |
| 遵守 ARCH-F2 定界 + 本 EXEC 文件表/编译证据 | 是 |

## 给审核的线索

- 静态：`Plugins/SCLCore/Source/SCLCore/Public/{Framework,Calendar,DesignData,FeatureModule,Adjudication}/`
- 搜红线：Bootstrap/四子系统/WorldLayer/CalendarDisplay/DreamExit 仍在 `Source/SCL`；ATBS 未触
- 搜倒灌：`SCLCore.Build.cs` 仅 Core/CoreUObject/Engine
- 编译：见上两条 Succeeded
