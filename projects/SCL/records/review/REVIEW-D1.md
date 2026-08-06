# 审核报告

- **需求 ID：** D1
- **审核员工：** `task-review`
- **依据：** [ARCH-D1.md](../lead-eng/ARCH-D1.md) + [EXEC-D1.md](../exec/EXEC-D1.md) + [DISPATCH-D1.md](../main/DISPATCH-D1.md) / BACKLOG DoD
- **结论：** PASS

## 审核/测试做了什么

- 读 ARCH / EXEC / 定界铁律，对照 BACKLOG D1 DoD。
- `git -C E:\Project\Game\S_\SCL`：工作区仅改 2 文件（见越界检查）。
- 静态对照 `ATBSUnitComponent.cpp` 私有辅助与 `TickComponent`、`StartMoveAlongPath`、Settings 旋钮。
- 编译：采信 EXEC 证据（`Build.bat SCLEditor Win64 Development -Module=ATBS` → Succeeded）；本刀以编译+静态为主，未复跑人手坡测。

## 越界检查

| 检查 | 结果 |
|------|------|
| diff 文件集 | **PASS** — 仅 `Plugins/ATBS/Source/ATBS/Private/ATBSUnitComponent.cpp`、`Plugins/ATBS/Source/ATBS/Public/ATBSTacticalSettings.h`（均在 ARCH 允许路径） |
| Tick Z 压平（D2） | **未改** — `Target.Z = Current.Z` / 终点贴当前 Z 仍在；diff 未触及 Tick |
| Presenter / ViewState / WBP | **未改** — 无相关路径 diff |
| 可达圆（D3） | **未改** — 无 `ShowReachablePreview` / Preview 组件 diff |
| 攻击射程 Dist2D | **保持** — `FindMoveStopIndex` 内射程与 `IsWithinRange2D` 仍 Dist2D |
| 代价模式枚举 | **未引入** — 写死 HorizontalPlusAbsZ |

**越界检查结论：无越界。**

## 对照 DoD

| DoD 项 | 结果 | 证据 |
|--------|------|------|
| 预览/开步共用 HorizontalPlusAbsZ（Dist2D+AbsΔZ） | PASS | `GetSegmentBudgetCost`；`GetPathLengthBudget` / `FindMoveStopIndex` 同源；`StartMoveAlongPath` 的 `ActivePathDistance` 走 Budget；预览链仍调 `FindMoveStopIndex` |
| 邻点超 MaxStepHeightDelta 在前一点截断；默认 90 | PASS | `FindMoveStopIndex` 超限 `break`（停在前一点）；`UATBSTacticalSettings::MaxStepHeightDelta = 90.f`；Settings 缺失时 helper 回落 90 |
| 编译通过 | PASS | EXEC：`SCLEditor` Win64 Development `-Module=ATBS` Succeeded |
| 有 EXEC 报告 | PASS | `records/exec/EXEC-D1.md`，遵守定界=是 |
| 遵守 ARCH 允许路径 / 未碰红线 | PASS | 见上「越界检查」 |
| 人手坡测 | 债（不挡） | 分发单允许可选；EXEC 已标债 |

## 问题与退回意见（FAIL 必填）

- （无）

## 通过后移交 PM 的要点（PASS）

- 应登记的文档/Status 行：D1 审核 PASS；BOARD/BACKLOG 可标 D1 规则核完成，进入 PM 登记 / 主控确认闸门。
- 风险或债（不挡 PASS 的）：人手陡坎/缓坡运行验收未做；D2（Tick 跟路径 Z）、D3（可达圆）仍排队。
