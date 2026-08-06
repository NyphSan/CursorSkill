# ARCH_MEMO · 主程定界

- **Project：** SCL
- **需求 ID：** D2
- **主程：** lead-eng
- **栈适配器：** ue-framework
- **GAME_ROOT：** `E:\Project\Game\S_\SCL`
- **主题：** 移动执行跟随路径点 Z — 取消 Tick 无脑压平

## 现状核对（GAME_ROOT，定界依据）

| 点 | 位置 | 结论 |
|----|------|------|
| Tick 中间航点压平 Z | `UATBSUnitComponent::TickComponent`：`Target.Z = Current.Z` | 属实 → **本刀目标** |
| 到达判定纯平面 | 同函数：`FVector::Dist2D(Current, Target)` | 属实；跟 Z 后须改为含高度到达 |
| Character 驱动 2D | `RequestDirectMove(Direction * MoveSpeed)` 且 `GetSafeNormal2D()` | 属实；仅取消压平不够，方向须含竖直分量或等价 Z 校正 |
| 非 Character 插值 | `VInterpConstantTo(Current, Target, …)` | 属实；Target 恢复完整 XYZ 后即可带高差插值 |
| 终点再压平 | `FinalLocation.Z = Owner->GetActorLocation().Z` 后 `SetActorLocation` | 属实 → **本刀取消** |
| 路径点含 Nav Z | `BuildMovePath` → `FNavPathPoint.Location`（含 Z） | 属实；D1 预算已吃高度，执行层此前丢弃 |
| D1 预算/落差截断 | `GetPathLengthBudget` / `FindMoveStopIndex` / `MaxStepHeightDelta` | 属实 → **非目标**，本刀不改公式 |
| 可达预览平面圆 | `ShowReachablePreview` / `SetMoveRangeCircle` | 属实 → **D3** |
| Presenter / ViewState | 战术 UI 契约层 | **本刀红线** |

## 定层

- **层：** ATBS 单位移动**执行**（`UATBSUnitComponent::TickComponent` 及同文件内与 ActivePath 推进直接相关的最小辅助）；不改寻路后端、不改路径预算、不改 UI。
- **理由（ue-framework）：**
  1. 「沿已裁路径走完」是 Pawn 上 ATBS Unit 玩法组件的运行时职责，不是 PC / Presenter / Character 堆属性。
  2. D1 已让预算与预览承认高度；D2 只补齐执行层与路径点 Z 一致，避免「算得爬、走得平」。
  3. 可达圆（D3）与 Presenter 契约另刀，避免一次改执行+范围语义+UI。

## 产品默认（本刀写死）

| 项 | 决策 | 说明 |
|----|------|------|
| 中间航点 Z | **FollowPathPointXYZ** | 删除 `Target.Z = Current.Z`；`Target = ActivePathPoints[ActivePathIndex]` 完整 XYZ。 |
| 终点 Z | **SnapToPathEndXYZ** | 删除 `FinalLocation.Z = Owner->GetActorLocation().Z`；终点用 `ActivePathPoints.Last()` 完整 XYZ，`SetActorLocation(..., true)`（保留 sweep）。 |
| 到达判定 | **Dist3D ≤ PathArrivalRadius** | 写死用三维距离（或等价：`Dist2D` 与 `Abs(ΔZ)` **均** ≤ 同一 `PathArrivalRadius`）。禁止继续只靠 Dist2D 切航点（XY 到了高度没到会跳段）。既有 `PathArrivalRadius`（20.f）可复用，本刀不强制改数值。 |
| Character 驱动 | **3D 方向 + 仍走 CMC** | `RequestDirectMove` 的方向改为 `(Target - Current).GetSafeNormal()`（**禁止**再 `GetSafeNormal2D`）。不切换飞天/自定义移动模式；不重写 CharacterMovement。若 Walk 下竖直分量被引擎吃掉导致明显不跟坡，允许**同文件内**对 Owner 做最小 Z（或整点）校正以贴当前航点，不得引入新组件/新移动系统。 |
| 非 Character | 保持 `VInterpConstantTo` 到完整 Target | Target 已含 Z 即满足。 |
| 额外贴地 Trace | **不做** | 本刀不新增 LineTrace/NavProject 终点贴地；Nav 路径点 Z 即权威。若 Capsule 中心与 Nav 点语义偏差导致陷入/悬空，仅允许在 Tick/收尾处加**有注释的**最小 HalfHeight 常量校正，且须仍落在允许文件内；不得借机大改 Capsule/CMC。 |

## 允许改的路径

相对 `GAME_ROOT`：

1. `Plugins/ATBS/Source/ATBS/Private/ATBSUnitComponent.cpp`  
   - **必改：** `TickComponent` 内 ActivePath 推进：取消中间/终点 Z 压平；到达判定含高度；Character 分支方向改为 3D（及上表允许的最小 Z 校正）。  
   - **可改（最小）：** 同文件 `ATBSUnitComponentPrivate` 内与到达半径/跟点辅助直接相关的常量或极小 helper（若抽函数仅为 Tick 可读性）。  
   - **不改：** `GetPathLengthBudget` / `FindMoveStopIndex` / `MaxStepHeightDelta` / `BuildMovePath` 预算与截断语义（D1）；`IsWithinRange2D` 射程公式。
2. `Plugins/ATBS/Source/ATBS/Public/ATBSUnitComponent.h`  
   - 仅当 Tick 跟 Z 需要声明极小私有 helper 时的最小改动；禁止借机堆战斗属性或扩公开 API。

**默认不改：** `ATBSTacticalPreviewComponent`、`ATBSBattleSubsystem`、Settings（D2 无新旋钮）、Types/ViewState。

## 禁止改的路径（越界红线）

- **路径预算 / 落差截断（D1）：** `GetPathLengthBudget`、`FindMoveStopIndex`、`MaxStepHeightDelta`、HorizontalPlusAbsZ 公式与默认值。
- **可达圆（D3）：** `ShowReachablePreview` / `SetMoveRangeCircle` / 可达网格生成。
- **Presenter / ViewState / WBP：** 任意 `*Presenter*`、`*ViewState*`、UMG/WBP、SCL 战术 UI 契约层。
- **SCL Character / Pawn 堆属性；CMC/ALS 大改：** 不改 `MaxStepHeight`、不换移动模式、不引入 ALS/根运动大修。
- **寻路后端：** 不重写 `BuildMovePath` / NavMesh 工具链（除非编译/链接被迫且仍无行为语义变化——本刀预期不需要）。
- **无关系统：** GAS、技能管线、LOS、联机复制。

## 硬规则

1. 无本 ARCH 签字「批准开工」→ 禁止功能施工（组织铁律）。
2. **禁止**在 Tick 中间航点或终点再次把路径 Z 压成 `Current.Z` / `Owner.Z`（本刀核心）。
3. 跟路径策略写死：**FollowPathPointXYZ**（中间）+ **SnapToPathEndXYZ**（终点）；贴地权威是路径点 Z，不做额外地面 Trace。
4. 到达判定必须含高度（Dist3D 或 Dist2D∧AbsΔZ）；Character 不得继续 `GetSafeNormal2D` 作为唯一推进方向。
5. 预览/预算与 D1 一致即可；本刀不改裁路数学。执行层只消费已有 `ActivePathPoints`。
6. 不扩 scope 至 D1 返工或 D3；不碰红线路径；需越界 → 停工 → 主程改备忘。
7. 验收以编译 + 静态对照 ARCH（Tick 无 Z 压平、到达含高、方向/插值跟点 Z）为主；坡地人手测可标债。

## 非目标

- D1 返工：路径预算公式、邻点落差截断、Settings 默认值。
- D3：可达范围由平面圆改为真实可达集/等高代价场。
- Presenter、ViewState、WBP、CommonUI。
- 额外 LineTrace/NavProject 贴地系统、物理下落模拟重做。
- CharacterMovement / ALS / GAS / LOS 大改。
- 攻击/技能射程（`IsWithinRange2D`）改为 3D。

## 主程签字

- **结论：批准开工**
- 执行须严格落在「允许改的路径」；交付对照本备忘写 EXEC 报告「遵守定界」。
