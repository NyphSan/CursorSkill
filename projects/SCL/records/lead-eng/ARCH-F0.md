# ARCH_MEMO · 主程定界

- **Project：** SCL
- **需求 ID：** F0
- **主程：** lead-eng
- **栈适配器：** ue-framework
- **GAME_ROOT：** `E:\Project\Game\S_\SCL`
- **主题：** 框架改造总定界 — 业务 vs 核心、SCLCore、ATBS→战斗插件、迁移刀序

---

## 命名备忘（老板用语校正）

| 老板写法 | UE 规范名（本备忘定版） | 说明 |
|----------|-------------------------|------|
| SLCcore / SLCcore | **SCLCore** | 插件目录 / `.uplugin` Name / Runtime 模块名均为 `SCLCore` |
| （建议）SCLTactical 或 SCLCombat | **SCLTactical** | 见下文论证；禁止再用 `Plugins/SCL` 作插件名 |

---

## 现状核对（GAME_ROOT，定界依据）

| 点 | 现场 | 结论 |
|----|------|------|
| `Plugins/` | `ATBS`、`ALS-Refactored-4.16`、`VRM4U`、`BlockoutToolsPlugin` | **无** `Plugins/SCL` |
| `Source/SCL` | 游戏主模块；`SCL.uproject` Modules 仅 `"SCL"`；私有依赖 `"ATBS"` | **业务 + 大量可抽核心** 现仍混在游戏模块 |
| `Source/SCL` 分层 | `Rules/` · `Adjudication/` · `Content/` · `Infrastructure/` | 与 Design_00 一致；迁移按此切，不按「整仓搬家」 |
| ATBS | `Plugins/ATBS`；模块 `ATBS`；不依赖 SCL | 已是独立战旗核插件；需 SCL 化命名 + 依赖 Core |
| 名称易混 | `USCLCoreBootstrapSubsystem`（`Infrastructure/Bootstrap/`） | **类名**，不是插件；F2 迁 Core 时再处理，F1 不改其实现 |
| 战旗定版 | `docs/dev/SCL_Tactical_Architecture.md` | Presenter→ViewState 唯一读出口；本改造**不得推翻** |
| 3C | `Content/Control/`（InputRouter / Camera / Character） | 属业务操控通道；依赖战斗 API，不进 Core |

**命名冲突结论：** 当前**不存在** `Plugins/SCL` 与 `Source/SCL` 的插件级冲突。  
**策略（写死）：**

1. **禁止**新建 `Plugins/SCL`（与游戏模块名 `SCL` 在 UBT/模块空间冲突）。
2. 核心能力进 **`Plugins/SCLCore`**；战旗核演进为 **`Plugins/SCLTactical`**（由 ATBS 改名/替换）。
3. **`Source/SCL` 永久保留为业务游戏模块**（模式/关卡编排/3C/Presenter·View/内容）。
4. 若历史文档或口头称「Plugins/SCL」，一律理解为误称 → 对应 **SCLCore** 或业务模块，不落盘同名插件。

---

## 定层

- **层：** 工程框架 / 插件边界（组织级定界）；**本刀不搬代码、不改玩法数值**。
- **理由（ue-framework）：**
  1. 跨模式复用的系统与数据属 **插件化 Core**（Lyra GFP 思想：可依赖、不可倒灌），不是 GameMode/关卡内容。
  2. 回合/单位/格战真相属 **专用战斗插件**（现 ATBS），应对齐 SCL 战旗产品名并依赖 Core；不是 Character 堆属性，也不是 WBP。
  3. 业务模块只做 **编排与体验装配**（ASP/Dream/3C/Presenter），命令下行、ViewState 上行，禁止业务规则倒灌 Core。

---

## 业务开发 vs 核心功能开发（职责表）

| 维度 | **业务开发**（`Source/SCL` 为主） | **核心功能开发**（`SCLCore` + `SCLTactical`） |
|------|----------------------------------|-----------------------------------------------|
| 目标 | 可玩内容、模式编排、关卡/会话体验 | 可复用系统、数据管线、战旗规则核 |
| 典型归属 | GameMode/PC 组装、Dream/ASP/OpMode、3C、Presenter→ViewState→WBP、关卡脚本、内容配表行消费侧 | DesignData Catalog/Mount/Pipeline、Session/Manifest 基础设施、Framework Types/Guards、日历/世界层规则底座、战旗 L0（单位/回合/移动射击） |
| 允许依赖 | → SCLTactical → SCLCore → Engine | SCLCore → Engine；SCLTactical → SCLCore → Engine |
| 禁止 | 在业务里实现「第二套」战旗规则；WBP 直读 Battle | Core/战斗依赖 `SCL` 游戏模块；Core 依赖 SCLTactical |
| 组织含义 | 业务刀：模式/内容/3C/UI 契约 | 核心刀：插件 API、数据、战旗核；profile 按此分流（F5） |
| 验收重心 | 流程可玩、契约不破 | 模块可编、依赖单向、入口不断 |

**边界速判：**

- 「换一张图 / 进一场遭遇 / 切 IMC / 推 HUD」→ **业务**
- 「配表怎么挂、世界层铁律、回合队列怎么推进、单位怎么走格」→ **核心**（数据/规则进 Core；格战执行进 SCLTactical）

---

## 插件命名结论（论证）

### 1) 核心插件：**SCLCore**（定版）

- 对应老板 **SLCcore**；UE 惯例 PascalCase 插件/模块名。
- 承载：各系统与数据封装中**非战旗专属**、可被战斗与业务共用的部分。
- F1 只建空壳 + 公共 API 锚点；首批搬迁清单在 F2。

### 2) 战斗插件：**SCLTactical**（定版；不用 SCLCombat）

| 选项 | 评价 |
|------|------|
| **SCLTactical** ✅ | 与现有产品词一致：`TacticalGrid`、`SCLTactical*`、战旗定版文档、ATBS FriendlyName「Tactical Battle」；迁移时心智连续 |
| SCLCombat ❌ | 工程已有 `Content/Combat/`（HostileVision/Relation，**进战条件原料**，非回合核）；命名会与感知/关系模块撞车 |

**ATBS → SCLTactical 策略（F3 执行，F0 定界）：**

1. **目标态：** `Plugins/SCLTactical` + 模块 `SCLTactical`，`SCLTactical.uplugin` 启用；依赖 **SCLCore**。
2. **过渡：** 允许 F3 保留 `UATBS*` / `EATBS*` 类型名与头文件别名（减爆破面）；插件/模块对外名必须是 SCLTactical。完整类型更名另开刀，不塞进 F3 DoD。
3. **Demo：** `Plugins/ATBS/Content`（`AATBSGameMode` 等）保持 NON-PRODUCTION；SCL 生产入口仍是 `ASCLGameMode` / 业务侧 Bridge。
4. **禁止：** 新建第三套并行战旗核；禁止业务旁路直接复制 ATBS 规则。

### 3) 业务模块：**SCL**（`Source/SCL`，保留）

- 不插件化整仓；F4 只做依赖方向与职责收口。

---

## 目标插件地图与依赖方向

```text
┌─────────────────────────────────────────────────────────────┐
│ 业务 · Source/SCL（游戏模块）                                │
│  3C · ASP/Dream/Mode · Bridge/Flow · Presenter/ViewState/WBP │
│  Content 编排 · Adjudication 关口 · 关卡/GM 组装             │
└───────────────────────────┬─────────────────────────────────┘
                            │ 只依赖 ↓（禁止倒灌）
┌───────────────────────────▼─────────────────────────────────┐
│ 战斗 · Plugins/SCLTactical（由 ATBS 演进）                   │
│  L0：BattleSubsystem · UnitComponent · 移动/射击/回合真相    │
│  Settings / Types（战旗规则）；Demo Content 非生产            │
└───────────────────────────┬─────────────────────────────────┘
                            │ 只依赖 ↓
┌───────────────────────────▼─────────────────────────────────┐
│ 核心 · Plugins/SCLCore                                       │
│  数据管线 · Session/Manifest 底座 · Framework Types/Guards   │
│  日历/世界层等可复用系统（F2 清单为准）                        │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
                     Engine / UE 官方模块

旁路（第三方，不进主依赖链倒灌）：
  ALS / VRM4U / BlockoutTools — 业务或角色表现按需私有依赖；
  不得被 SCLCore / SCLTactical 反向依赖业务模块。
```

**硬依赖方向（写死）：**

```text
业务（SCL） → 战斗（SCLTactical） → 核心（SCLCore） → Engine
```

| 允许 | 禁止（倒灌） |
|------|----------------|
| SCL → SCLTactical、SCLCore | SCLCore → SCL / SCLTactical |
| SCLTactical → SCLCore | SCLTactical → SCL |
| 任一层 → Engine 官方模块 | 第三方插件依赖业务模块「回头」提供核心 API |

---

## 定版硬规则如何落入新图

既有战术 / 3C / ATBS 定版**继续有效**；框架改造只改**落盘位置与依赖**，不改契约语义。

| 定版要点 | 落入新图 |
|----------|----------|
| L0 战旗真相在 ATBS Unit/Battle | → **SCLTactical**；业务不得再实现第二套规则 |
| L1 Flow / Bridge / Environment | 默认仍在 **业务 `Source/SCL`**（会话编排属内容）；仅当证明「无 SCL 内容也能复用」时，F2+ 另备忘评估是否下沉（**默认不下沉**） |
| L2 唯一读出口 Presenter → `FSCLTacticalViewState` | **留在业务**；WBP 只吃 ViewState；禁止 View 直读 Battle |
| L3 3C（InputRouter / Camera / Command） | **留在业务** `Content/Control/`；Command 调 SCLTactical API |
| L4 WBP / WidgetComponent | **留在业务** Content/UI（或 Content）；禁止规则 |
| Character 薄 + `UATBSUnitComponent` 属性 | Pawn/Character 壳在业务；Unit 组件实现在 **SCLTactical** |
| DesignData / Infrastructure | **目标进 SCLCore**（F2 首批）；业务只消费 |
| Rules（世界层/Guards/日历） | **目标进 SCLCore**（可分批）；业务/流程受其约束 |
| D1/D2 已合入的 ATBS 高低差预算与 Tick 跟 Z | 随 ATBS 目录迁入 SCLTactical 时**行为不得回退**；F3 以编译+入口不断为底线，不借机改公式 |

---

## 迁移刀序 F1–F5 与每刀 DoD

| 刀 | 目标 | DoD（摘要） | 依赖 |
|----|------|-------------|------|
| **F0** | 本备忘定界 | 批准开工 F1；命名与依赖方向写清 | — |
| **F1** | 新建 **SCLCore** 插件壳 | 见下节「F1 允许路径」；`SCLEditor` 能编过；`Source/SCL` 可声明依赖 SCLCore（空 API 即可）；**不**搬业务/ATBS 代码 | F0 |
| **F2** | 划定迁入 Core 清单 + 首批搬迁 | 有书面清单（建议：DesignData\*、Session/Manifest 类型、FrameworkTypes/Guards 等）；仅搬清单内；依赖仍单向；业务编译通过；无业务倒灌 | F0+F1 |
| **F3** | ATBS → **SCLTactical** | 插件/模块名 SCLTactical；依赖 SCLCore；战旗生产入口（Bridge/开战/EndTurn 通道）不断；ATBS 旧名有迁移说明或别名；能编 | F0（建议 F1 完成后，可与 F2 部分并行但勿抢同一文件） |
| **F4** | 业务层收口 | `SCL.Build.cs` 依赖方向正确；业务不承载已迁 Core 的实现；无 `#include` / 模块依赖倒灌；Presenter/3C 仍在业务 | F2+F3 |
| **F5** | 组织 profile / 花名册 | `profiles/SCL` 与 PROJECT 区分业务岗 vs 核心岗；与本职责表对齐 | F0（可与工程刀并行，主控执行） |

**本刀（F0）非施工：** 不创建插件、不改 `GAME_ROOT` 代码。

---

## 允许改的路径

### 本刀 F0

- **仅组织仓文档：** `E:\dev\CursorTeam\projects\SCL\records\lead-eng\ARCH-F0.md`（本文件）
- **禁止**改 `GAME_ROOT` 任何文件

### F1 起（批准后；F1 专用允许路径）

相对 `GAME_ROOT`：

1. **新建** `Plugins/SCLCore/**`（`.uplugin`、`Source/SCLCore/*Build.cs`、模块进出点、空/锚点 Public API 头）
2. `SCL.uproject` — 启用插件 `SCLCore`
3. `Source/SCL/SCL.Build.cs` — **仅**增加对 `SCLCore` 的模块依赖（Public 或 Private 按 API 暴露需要；推荐业务侧 Private 直至有稳定 Public API）
4. （若 UBT 需要）`Source/SCL.Target.cs` / `SCLEditor.Target.cs` — 仅当启用插件所必需的最小改动

**F1 明确不做：** 搬迁 `Infrastructure/` / `Rules/`；不改 ATBS；不改 Presenter/ViewState/3C 实现。

### F2–F4 路径原则（细表由各刀 ARCH 再锁）

| 刀 | 允许方向 | 禁止 |
|----|----------|------|
| F2 | 清单内文件从 `Source/SCL` → `Plugins/SCLCore`；修 include/API 宏 | 改 SCLTactical/ATBS 规则；改 WBP 表现逻辑 |
| F3 | `Plugins/ATBS` → `Plugins/SCLTactical`（或等价替换）；`SCL.Build.cs`/uproject 依赖改名；最小调用点适配 | 推翻 ViewState 契约；大改移动/预算公式 |
| F4 | 业务侧删除已迁重复实现、整理依赖 | 把 Presenter/3C 塞进 Core「图省事」 |

---

## 禁止改的路径（越界红线）

**F0 本刀：** 全部 `GAME_ROOT` 代码与 Content。

**F1 起通用红线（除非后续 ARCH 明示放开）：**

- **倒灌：** SCLCore / SCLTactical 依赖游戏模块 `SCL`
- **新建 `Plugins/SCL`**
- **Presenter / ViewState 契约推翻：** 禁止 WBP/View 直读 Battle；禁止多 Presenter 真源
- **3C 规则化：** 禁止在 InputRouter/Camera 内实现回合/射程/移动预算
- **Character 堆战斗属性：** 属性与规则组件留在 SCLTactical Unit，不堆回 `ASCLCharacter`
- **借框架刀改玩法：** D3 可达圆、GAS 大扩、数值重做、无关 ALS/VRM4U 大改
- **第三方插件当 Core：** ALS/VRM4U/Blockout 不充当 SCLCore

---

## 硬规则

1. 无本 ARCH「批准开工」及后续各刀 ARCH → 禁止对应功能施工（组织铁律 `01_no_out_of_bounds`）。
2. 依赖方向永久：**业务 → 战斗 → Core → Engine**；发现倒灌 → 停工改备忘。
3. 插件命名定版：**SCLCore** + **SCLTactical**；老板 SLCcore ≡ SCLCore；不用 SCLCombat；不用 Plugins/SCL。
4. 战旗定版（Presenter→ViewState、双域、Command 上行）在迁移中**行为与契约保持**；只搬家不换架构。
5. F1 只允许空壳与依赖声明；大挪移必须 F2+ 且有清单。
6. `USCLCoreBootstrapSubsystem` 与插件 `SCLCore` 共存时：F1 不改该类；F2 迁入时避免模块 API 宏/类名混乱（可保留类名或改名，单独立项写进 F2 ARCH）。
7. 需越界 → 停工 → 主程改备忘 → 再干。

---

## 非目标

- 本刀搬代码、改数值、改可达圆（D3）、改 Presenter/WBP 视觉
- 一次到位重命名全部 `UATBS*` → `USCLTactical*`（可后续刀）
- 引入完整 Lyra Experience/GFP 栈
- 联机复制架构重做
- 合并或删除 ALS/VRM4U

---

## 主程签字

- **结论：批准开工 F1**
- **否决项：** 无（现场无 Plugins/SCL 冲突；命名与依赖可执行）
- 执行 F1 须严格落在上文「F1 允许路径」；交付 EXEC 写明「遵守定界」与编译证据。
- F2/F3/F4 开工前须各有独立 ARCH（可薄）锁当刀文件清单；不得仅凭 F0 大挪移。
