# 执行报告

- **需求 ID：** D1
- **执行员工：** ATBS 战旗核（执行岗）
- **结果：** DONE
- **遵守定界：** 是

## 制作内容

- `Plugins/ATBS/Source/ATBS/Private/ATBSUnitComponent.cpp`
  - `GetPathLength2D` → `GetPathLengthBudget`（HorizontalPlusAbsZ：`Dist2D + Abs(ΔZ)`）
  - 新增 `GetSegmentBudgetCost` / `GetMaxStepHeightDelta`（读 Settings）
  - `FindMoveStopIndex`：预算改用新代价；邻点 `Abs(ΔZ) > MaxStepHeightDelta` 时在前一点截断；射程仍 Dist2D
  - `StartMoveAlongPath` 的 `ActivePathDistance` 改走 `GetPathLengthBudget`
  - 预览/开跑（`ComputeMovePreview` / `ComputeAttackPreview` / `TryMoveToLocation` / Approach*）仍共用 `FindMoveStopIndex`，未改 Tick Z 压平
- `Plugins/ATBS/Source/ATBS/Public/ATBSTacticalSettings.h`
  - 增加 Config `MaxStepHeightDelta = 90.f`（Category Movement）
- **未改：** Presenter / ViewState / WBP / Character、`TickComponent` Z 压平、可达圆、`ATBSUnitComponent.h`、Preview 组件

## 解决方案

- 路径段代价写死 HorizontalPlusAbsZ；预算累加与落差截断集中在私有 `FindMoveStopIndex` / `GetPathLengthBudget`，预览裁路与 `StartMoveAlongPath` 消耗同源。
- 落差阈值进 `UATBSTacticalSettings`，默认 90cm，不引入代价模式枚举。

## 是否遇到问题

- **无**（编译通过；未遇编辑器锁）

## 自检对照 DoD

| DoD 项 | 自检 |
|--------|------|
| 预览/开步共用 HorizontalPlusAbsZ（2D+ΔZ）代价 | 是（`FindMoveStopIndex` + `GetPathLengthBudget` 同源） |
| 邻点超 MaxStepHeightDelta 在前一点截断 | 是（默认 90，Settings 可配） |
| 编译通过 | 是（`SCLEditor` Win64 Development，`-Module=ATBS` Succeeded） |
| 有 EXEC 报告 | 是（本文件） |
| 遵守 ARCH 允许路径 / 未碰红线 | 是 |
| 人手坡测 | 无法自证（标债：分发单允许运行测可选） |

## 给审核的线索

- 静态对照：`ATBSUnitComponentPrivate::GetSegmentBudgetCost` / `FindMoveStopIndex` / `StartMoveAlongPath` ActivePathDistance；Settings `MaxStepHeightDelta`
- 编译：`Build.bat SCLEditor Win64 Development -Project=E:\Project\Game\S_\SCL\SCL.uproject -Module=ATBS` → Succeeded（约 25s）
- 人手坡测债：陡坎路径应在落差点前截断；缓坡预算应高于纯 Dist2D
- 未改文件：`ATBSTacticalPreviewComponent`、`ATBSBattleSubsystem::ShowReachablePreview`、Presenter/ViewState
