# 执行报告

- **需求 ID：** D2
- **执行员工：** ATBS 战旗核（执行岗）
- **结果：** DONE
- **遵守定界：** 是

## 制作内容

- `Plugins/ATBS/Source/ATBS/Private/ATBSUnitComponent.cpp`（仅 `TickComponent` ActivePath 推进）
  - 取消中间航点 `Target.Z = Current.Z` → **FollowPathPointXYZ**（完整 `ActivePathPoints[i]`）
  - 到达判定 `Dist2D` → **`FVector::Dist`（Dist3D）≤ PathArrivalRadius**
  - Character：`GetSafeNormal2D` → **`GetSafeNormal`** + `RequestDirectMove`；同文件最小 Z `FInterpConstantTo` 校正（CMC Walk 吃竖直分量）
  - 非 Character：保持 `VInterpConstantTo` 到完整 Target（已含 Z）
  - 取消终点 `FinalLocation.Z = Owner.Z` → **SnapToPathEndXYZ**（`ActivePathPoints.Last()` + `SetActorLocation(..., true)`）
- **未改：** `.h`、预算/`FindMoveStopIndex`/`MaxStepHeightDelta`/`BuildMovePath`、`IsWithinRange2D`、Preview/可达圆、Presenter/ViewState、Settings、CMC/ALS

## 解决方案

- 执行层只消费已有 `ActivePathPoints` 的 XYZ；贴地权威为 Nav 路径点 Z，不新增 Trace。
- Character 仍走 CMC `RequestDirectMove`，用 3D 方向 + 最小 Z 校正补齐 Walk 丢竖直分量的缺口，不换移动模式。

## 是否遇到问题

- **无**（编译通过；未遇编辑器锁）

## 自检对照 DoD

| DoD 项 | 自检 |
|--------|------|
| Tick 中间/终点无 Z 压平 | 是（已删 `Target.Z=Current.Z` / `FinalLocation.Z=Owner.Z`） |
| 到达判定含高度（Dist3D） | 是（`FVector::Dist` ≤ `PathArrivalRadius` 20.f） |
| Character 方向含竖直 / 非 2D-only | 是（`GetSafeNormal` + 最小 Z 校正） |
| 非 Character 跟完整 Target | 是（`VInterpConstantTo`） |
| 编译通过 | 是（`SCLEditor` Win64 Development，`-Module=ATBS` Succeeded） |
| 有 EXEC 报告 | 是（本文件） |
| 遵守 ARCH 允许路径 / 未碰红线 | 是 |
| 人手坡测 | 无法自证（标债：ARCH 允许运行测可选） |

## 给审核的线索

- 静态对照：`UATBSUnitComponent::TickComponent` ActivePath 循环与收尾；搜 `Target.Z` / `FinalLocation.Z` / `GetSafeNormal2D` 应无命中
- 编译：`Build.bat SCLEditor Win64 Development -Project=E:\Project\Game\S_\SCL\SCL.uproject -Module=ATBS` → Succeeded（约 20s）
- 人手坡测债：有高差路径应跟点爬升/下降，终点 Z 落在路径末点而非平面压平
- 未改文件：`ATBSTacticalPreviewComponent`、`ATBSBattleSubsystem`、Settings、Presenter/ViewState、`GetPathLengthBudget` / `FindMoveStopIndex`
