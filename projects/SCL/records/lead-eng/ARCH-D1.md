# ARCH_MEMO · 主程定界

- **Project：** SCL
- **需求 ID：** D1
- **主程：** lead-eng
- **栈适配器：** ue-framework
- **GAME_ROOT：** `E:\Project\Game\S_\SCL`
- **主题：** 战斗寻路高低差 — 路径预算含高度 + 邻点落差截断

## 现状核对（GAME_ROOT，定界依据）

| 点 | 位置 | 结论 |
|----|------|------|
| NavMesh 建路、点含 Z | `UATBSUnitComponent::BuildMovePath` → `FindPathSync` / `FNavPathPoint.Location` | 属实 |
| 预算/截断用 Dist2D | `ATBSUnitComponentPrivate::GetPathLength2D` / `FindMoveStopIndex` | 属实 |
| Tick 压平 Z | `TickComponent`：`Target.Z = Current.Z`；终点亦压当前 Z | 属实 → **D2**，本刀不改 |
| Preview Spline 吃 PathPoints | `UATBSTacticalPreviewComponent::ShowMovePathPoints` / `ShowActionMovePreview` | 属实；数据来自 Unit 的 `Compute*Preview` |
| 可达预览平面圆 | `UATBSBattleSubsystem::ShowReachablePreview` → `SetMoveRangeCircle` | 属实 → **D3**，本刀不改 |
| Presenter / ViewState | 战术 UI 契约层 | **本刀红线** |

## 定层

- **层：** ATBS 战术规则 / 单位移动组件（`UATBSUnitComponent` + 可选 `UATBSTacticalSettings` 配置旋钮）；预览仅消费既有 `FATBSMovePreviewData` / PathPoints，不改 Presenter→ViewState 契约。
- **理由（ue-framework）：**
  1. 路径代价与可走截断是**回合移动规则**，属 Pawn 上专用玩法组件（ATBS Unit），不是 PC / Character 堆属性，也不是 UI。
  2. 预览与真实开跑必须同一套截断/预算（数据同源在 Unit 的 `Compute*Preview` 与 `StartMoveAlongPath` / `FindMoveStopIndex` 链），Visualizer 只渲染已裁路径，故 D1 不必动 Preview 网格实现（除非编译/API 签名被迫同步，见允许路径）。
  3. Tick 跟路径 Z（D2）与可达圆（D3）是另一层表现/范围语义，拆刀避免一次改三义。

## 产品默认（本刀写死）

| 项 | 决策 | 说明 |
|----|------|------|
| 路径段代价 | **HorizontalPlusAbsZ**（写死推荐） | 段代价 = `Dist2D(A,B) + Abs(A.Z - B.Z)`。相对纯 ThreeD：显式「爬升/下落税」，更贴战旗高低差预算；ThreeD 在缓坡上近似 2D、陡坎上惩罚偏弱。执行勿再做成可切换枚举（除非后续 ARCH 改备忘）。 |
| 邻点截断 | **MaxStepHeightDelta** | 路径上相邻两点若 `Abs(ΔZ) > MaxStepHeightDelta`，在**前一点**截断（该段及之后不可用）；与预算截断取更短有效前缀。 |
| 建议默认值 | **90.f**（厘米） | 约 2× UE `CharacterMovement::MaxStepHeight`(45)；给 Recast 折线邻点留余量，仍截断悬崖级落差。可在 `UATBSTacticalSettings` 用 Config 暴露，默认 90；调参不改公式。 |
| 预览 ≡ 开跑 | 强制 | `ComputeMovePreview` / `ComputeAttackPreview`（及一切经 `FindMoveStopIndex` 的提交路径）与 `StartMoveAlongPath` 前预算核算**共用同一代价函数与落差规则**。 |

## 允许改的路径

相对 `GAME_ROOT`：

1. `Plugins/ATBS/Source/ATBS/Private/ATBSUnitComponent.cpp`  
   - 将 `GetPathLength2D` 升级/替换为含高度的段代价累加（命名可改为 `GetPathLengthBudget` 等，但调用点需一致）。  
   - `FindMoveStopIndex`：预算用新代价；并加入 `MaxStepHeightDelta` 邻点截断。  
   - `StartMoveAlongPath` / `ActivePathDistance` 及所有调用 `FindMoveStopIndex` / 路径长度的提交与预览路径（同文件内 Move/Attack/Throw 等）必须走同一实现。  
   - **不改** Tick 内 `Target.Z = Current.Z` 压平逻辑（D2）。
2. `Plugins/ATBS/Source/ATBS/Public/ATBSUnitComponent.h`  
   - 仅当需要声明/透出与 D1 直接相关的私有辅助或读取 Settings 的最小改动；禁止借机堆战斗属性。
3. `Plugins/ATBS/Source/ATBS/Public/ATBSTacticalSettings.h`（及对应 `.cpp` 若已有/需补 `Get()` 旁实现）  
   - 增加 `MaxStepHeightDelta`（默认 **90.f**）；**不要**做代价模式枚举热切换（本刀写死 HorizontalPlusAbsZ）。
4. （可选、最小）`Plugins/ATBS/Source/ATBS/Public/ATBSTypes.h`  
   - 仅当必须为预算/截断补极小类型或注释常量；禁止扩 ViewState/UI 结构。

**预览可视化：** 默认**不改** `ATBSTacticalPreviewComponent` / `ATBSBattleSubsystem::ShowReachablePreview`。Spline 已吃完整 `PathPoints`；Unit 侧截断后 Preview 自动变短即满足「预览与 StartMoveAlongPath 共用代价」。

## 禁止改的路径（越界红线）

- **Presenter / ViewState / WBP：** 任意 `*Presenter*`、`*ViewState*`、UMG/WBP、SCL 战术 UI 契约层。
- **SCL Character / Pawn 堆属性：** `SCL` 角色基类上叠加移动/战斗属性；D1 旋钮进 `UATBSTacticalSettings` 或 Unit 私有辅助，不进 Character。
- **Tick 跟随路径 Z / 取消压平：** `UATBSUnitComponent::TickComponent` 的 Z 压平与终点贴地策略 → **D2**。
- **可达圆算法：** `ShowReachablePreview` / `SetMoveRangeCircle` / 可达网格生成 → **D3**。
- **无关插件与系统：** ALS、GAS 扩展、NavMesh 重建工具链、非 ATBS 的移动组件、联机复制大改。
- **攻击/技能射程语义：** `IsWithinRange2D` 及「是否在射程」判定保持 **Dist2D**（本刀只改**移动路径预算与落差截断**）；除非截断点与射程共用循环时不得不调用同一 helper，射程公式本身不改为 3D。

## 硬规则

1. 无本 ARCH 签字「批准开工」→ 禁止功能施工（组织铁律）。
2. 路径段代价写死 **HorizontalPlusAbsZ**；预览裁路与 `StartMoveAlongPath` 消耗/截断必须数学一致（同一函数或同一私有实现）。
3. `MaxStepHeightDelta` 默认 **90.f** cm；邻点超限则在前一点截断，不得静默跳过落差段。
4. `BuildMovePath` 可继续用 NavMesh；本刀重点在**预算与截断**，不重写寻路后端、不改 Nav 投影魔法数 unless 编译/正确性必需且仍落在允许文件内。
5. 不扩 scope 至 D2/D3；不碰红线路径；需越界 → 停工 → 主程改备忘。
6. 验收以编译 + 静态对照 ARCH 为主；人手坡测可标债（见分发单）。

## 非目标

- D2：移动 Tick 跟随路径 Z / 取消平面插值压平。
- D3：可达范围由平面圆改为真实可达集/等高代价场。
- Presenter、ViewState、WBP、CommonUI 改版。
- GAS、技能管线、LOS 公式重做。
- Character/ALS 步高与 CMC 参数大改（仅可读对照；战术截断用 Settings 独立值）。

## 主程签字

- **结论：批准开工**
- 执行须严格落在「允许改的路径」；交付对照本备忘写 EXEC 报告「遵守定界」。
