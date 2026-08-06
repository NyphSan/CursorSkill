# 审核报告

- **需求 ID：** F3
- **审核员工：** `task-review`
- **依据：** [ARCH-F3.md](../lead-eng/ARCH-F3.md) + [EXEC-F3.md](../exec/EXEC-F3.md) + 定界铁律 `rules/01_no_out_of_bounds.md` + 模板 `templates/REVIEW_REPORT.md`
- **结论：** PASS

## 审核/测试做了什么

- 读 ARCH-F3（阶段 A–E、允许/禁止路径、类型过渡、DoD）、EXEC-F3、定界铁律。
- 静态抽查 `GAME_ROOT`（`E:\Project\Game\S_\SCL`）：
  - `Test-Path Plugins/ATBS` → **False**；`Plugins/SCLTactical/` + `SCLTactical.uplugin` 存在。
  - `SCL.uproject` 插件列表含 **SCLTactical**、**SCLCore**；**无** `"Name": "ATBS"`。
  - `SCL.Build.cs` Private 依赖 **`SCLTactical`**（非 ATBS）；Public 仍 **SCLCore**。
  - `SCLTactical.Build.cs` **Public** 含 **SCLCore**；**无** → `SCL` 模块依赖。
  - `SCLCore.Build.cs` **无** SCLTactical/ATBS 依赖。
  - `ATBSCompat.h` 提供 `#define ATBS_API SCLTACTICAL_API`；`ATBSModule.h` 已 include；Public 头均为 **SCLTACTICAL_API**；**UATBS*** / **EATBS*** 类型名保留。
  - `IMPLEMENT_MODULE(FATBSModule, SCLTactical)`；`FATBSModule` 类名保留。
  - `DefaultEngine.ini` 保留 `/Game/ATBS`→`/ATBS` 并 **追加** `/ATBS`→`/SCLTactical`；Enum/PropertyRedirects 与 HEAD 旧 ATBS Config **一致**（随插件迁移，非 F3 新扩）。
  - `git diff HEAD -- Source/SCL/Content/Tactical/` → **零改动**（Presenter/ViewState/Bridge 未触）。
  - D1/D2 脏改动：`ATBSTacticalSettings.h` 含 `MaxStepHeightDelta`；`ATBSUnitComponent.cpp` 含 `HorizontalPlusAbsZ` / Tick 跟 Z — 与 EXEC 披露一致。
- 编译：采信 EXEC 两条 `Build.bat … -Module=SCLTactical|SCL` **Succeeded**（2026-08-06 21:36–21:37）；现场 **未保留** `UnrealEditor-*.dll`（Binaries 未入库/已清理），未复跑 Build.bat。

## 越界检查

| 检查 | 结果 |
|------|------|
| 插件整树 ATBS→SCLTactical；无 `Plugins/ATBS/` 残留 | **PASS** — 磁盘无 ATBS 目录；git 显示 ATBS 树删除 + SCLTactical 新增 |
| 无双插件并存 | **PASS** — uproject 仅启用 SCLTactical |
| 未新建 `Plugins/SCL` | **PASS** |
| 依赖链 SCL→SCLTactical→SCLCore→Engine | **PASS** — Build.cs + uplugin 双处 SCLCore |
| 无倒灌 SCLTactical→SCL / SCLCore→SCLTactical | **PASS** |
| 未做 UATBS* 类型大更名 | **PASS** — 类名/文件名仍为 ATBS* 前缀 |
| Presenter→ViewState / Bridge / Flow 语义 | **PASS** — `Source/SCL/Content/Tactical/` git diff 为空 |
| 3C / Command 行为（F3 红线） | **PASS（本刀）** — F3 未改 Tactical；Control 另有 `SCLPlayerBotSmokeCommands.cpp` 脏改动属 EXEC 披露「非 F3 范围」，不记入本刀 FAIL |
| D1/D2 高低差/Tick 跟 Z | **PASS（纳入迁移）** — EXEC 已声明基线 commit `779494e1` + 具体文件；属 PM-F2 工程债合入，**非 F3 新 scope** |
| 完整类型更名 / 清单 B / SCLCore 搬迁 / docs sweep | **PASS（未做）** — 符合 ARCH 非目标 |

**越界检查结论：无越界（F3 施工落在 ARCH-F3 允许路径与阶段 A–E）。**

## 对照 DoD

| DoD 项 | 结果 | 证据 |
|--------|------|------|
| 1. 存在 `Plugins/SCLTactical/` + uplugin；无 ATBS 插件；uproject 仅 SCLTactical | PASS | 磁盘/uplugin/uproject 抽查 |
| 2. UBT 模块 SCLTactical 编译成功；Build.cs Public SCLCore；uplugin 声明 SCLCore | PASS | Build.cs/uplugin + EXEC Succeeded |
| 3. SCL 模块编译成功；SCL.Build.cs Private SCLTactical | PASS | Build.cs + EXEC Succeeded |
| 4. 无 SCLTactical→SCL；无 SCLCore→SCLTactical | PASS | 两 Build.cs 抽查 |
| 5. UATBS*/EATBS* 保留；ATBSCompat.h 提供 ATBS_API 别名 | PASS | 头文件 + compat 抽查 |
| 6. Demo Content 已迁移；DefaultEngine.ini 含 /ATBS→/SCLTactical 重定向 | PASS | Config 抽查 |
| 7. 未改 Presenter/ViewState、Bridge/Flow 语义、3C 公式（除披露 D1/D2） | PASS | Tactical 零 diff；D1/D2 见 EXEC |
| 8. EXEC 含定界声明 + 编译证据 + 改动表 + 脏改动基线 | PASS | `EXEC-F3.md` |

## 问题与退回意见（FAIL 必填）

- （无）

## 通过后移交 PM 的要点（PASS）

- 应登记的文档/Status 行：F3 审核 PASS；BOARD/BACKLOG 可标「ATBS→SCLTactical 插件/模块迁移」完成。
- 风险或债（不挡 PASS 的）：
  - 类型前缀仍为 **UATBS*** / **ATBS*.h**，完整更名须另开 ARCH。
  - D1/D2（MaxStepHeightDelta / HorizontalPlusAbsZ / Tick 跟 Z）已随迁移合入 SCLTactical，属披露工程债，非本刀新 scope。
  - GAME_ROOT 仍有 **HostileVisionComponent**、**SCLPlayerBotSmokeCommands** 等未提交脏文件（EXEC 声明 F3 未触）。
  - 编译 dll 现场未保留；gitea 提交前建议复编或保留 Binaries 证据。
