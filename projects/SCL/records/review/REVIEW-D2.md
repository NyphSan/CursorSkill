# 审核报告

- **需求 ID：** D2
- **审核员工：** `task-review`
- **依据：** [ARCH-D2.md](../lead-eng/ARCH-D2.md) + [EXEC-D2.md](../exec/EXEC-D2.md) + [DISPATCH-D2.md](../main/DISPATCH-D2.md) / BACKLOG DoD
- **结论：** PASS

## 审核/测试做了什么

- 读 ARCH / EXEC / 定界铁律，对照 BACKLOG D2 DoD（不再无脑压平 Target.Z；走坡与预览一致）。
- `git -C E:\Project\Game\S_\SCL`：工作区相对 HEAD 仍含 D1+D2 累计 diff；D2 增量落在 `TickComponent` ActivePath 推进。
- 静态对照 `UATBSUnitComponent::TickComponent`：无 `Target.Z=` / `FinalLocation.Z=` / `GetSafeNormal2D`；到达用 `FVector::Dist`；Character 用 `GetSafeNormal` + 同文件最小 Z `FInterpConstantTo`；终点 `ActivePathPoints.Last()` + sweep。
- 编译：采信 EXEC（`Build.bat SCLEditor Win64 Development -Module=ATBS` → Succeeded）；未复跑人手坡测。

## 越界检查

| 检查 | 结果 |
|------|------|
| D2 功能 diff 落点 | **PASS** — Tick ActivePath：FollowPathPointXYZ / Dist3D / 3D 方向+最小 Z 校正 / SnapToPathEndXYZ；均在 `ATBSUnitComponent.cpp` 允许范围内 |
| 工作区 Settings.h / 预算辅助 | **D1 遗留（已 REVIEW-D1 PASS）** — `MaxStepHeightDelta`、`GetPathLengthBudget` / `FindMoveStopIndex` 非本刀新增语义；D2 未改公式与默认值 |
| D1 预算/落差截断 | **未再改** — D2 未触碰 HorizontalPlusAbsZ / 截断逻辑 |
| 可达圆（D3） | **未改** — 无 Preview / `SetMoveRangeCircle` 行为 diff |
| Presenter / ViewState / WBP | **未改** — 无相关路径 diff |
| CMC / ALS / 新 Trace | **未引入** — 仍 `RequestDirectMove`；无 LineTrace/NavProject；无移动模式切换 |
| `.h` 扩 API | **未改** — 与 EXEC 一致 |

**越界检查结论：无越界。**

## 对照 DoD

| DoD 项 | 结果 | 证据 |
|--------|------|------|
| 不再无脑压平 Target.Z（中间） | PASS | 已删 `Target.Z = Current.Z`；`const FVector Target = ActivePathPoints[i]` |
| 终点不压成 Owner.Z | PASS | 已删 `FinalLocation.Z = Owner.Z`；用 `ActivePathPoints.Last()` |
| 到达判定含高度 | PASS | `FVector::Dist` ≤ `PathArrivalRadius`（20.f） |
| Character 方向含竖直 / 非 2D-only | PASS | `GetSafeNormal` + ARCH 允许的最小 Z 校正 |
| 非 Character 跟完整 Target | PASS | `VInterpConstantTo(Current, Target, …)` |
| 走坡与预览一致（执行消费路径 XYZ） | PASS | 执行层只消费已有 `ActivePathPoints`；预算/预览裁路未改（D1） |
| 编译通过 | PASS | EXEC：`SCLEditor` Win64 Development `-Module=ATBS` Succeeded |
| 有 EXEC 报告 | PASS | `records/exec/EXEC-D2.md`，遵守定界=是 |
| 遵守 ARCH 允许路径 / 未碰红线 | PASS | 见上「越界检查」 |
| 人手坡测 | 债（不挡） | ARCH 允许可选；EXEC 已标债 |

## 问题与退回意见（FAIL 必填）

- （无）

## 通过后移交 PM 的要点（PASS）

- 应登记的文档/Status 行：D2 审核 PASS；BOARD/BACKLOG 可标 D2 执行跟 Z 完成。
- 风险或债（不挡 PASS 的）：人手坡测未做；工作区仍为 D1+D2 未提交累计改动；D3（可达圆非纯盘）仍排队且 scope 更大。
