# Profile · SCL

| 键 | 值 |
|----|-----|
| ProjectId | `SCL` |
| ORG_ROOT | `E:\dev\CursorTeam` |
| **项目文件夹** | `E:\dev\CursorTeam\projects\SCL\` |
| **GAME_ROOT** | `E:\Project\Game\S_\SCL` |
| **记录根** | `E:\dev\CursorTeam\projects\SCL\records\` |
| 项目说明 | `E:\dev\CursorTeam\projects\SCL\PROJECT.md` |
| 栈适配器 | `ue-framework` |
| 运行测 | `ue-pie-validate` |
| PM 委托 | `scl-pm`（可选写 GAME_ROOT/`docs/pm`）；**岗位记录必写记录根** |
| 写仓库 docs | 是（PASS 后，额外） |

## 岗位记录路径（强制）

| 岗位 | 写入 |
|------|------|
| 主控 | `projects/SCL/records/main/` |
| 主程 | `projects/SCL/records/lead-eng/` |
| 执行 | `projects/SCL/records/exec/` |
| 审核 | `projects/SCL/records/review/` |
| PM | `projects/SCL/records/pm/` |
| Gitea | `projects/SCL/records/gitea/` |

项目远程：`http://192.168.3.23:3000/SCLG/SCL.git`  
禁止写入已废弃的 `runs/SCL/`。

## 模块分层（派工锚点）

```text
业务 · Source/SCL  →  战斗 · Plugins/SCLTactical  →  核心 · Plugins/SCLCore  →  Engine
```

依赖方向写死：**业务 → 战斗 → Core → Engine**；禁止 Core/战斗依赖游戏模块 `SCL`。  
定界依据：`projects/SCL/records/lead-eng/ARCH-F0.md` 职责表。

## 执行花名册

### 业务岗（`Source/SCL` 为主）

目标：可玩内容、模式编排、3C、Presenter→ViewState→WBP、关卡/会话体验。

| 细分岗 | Skill | 路径锚点（相对 GAME_ROOT） |
|--------|--------|---------------------------|
| 3C | `ue-scl-3c` | `Content/Control/` · `Source/SCL/` 操控通道 |
| 角色/属性 | `ue-character` | Character/Pawn 壳；**不**堆战旗 Unit 规则 |
| AI/ST | `ue-ai-state-tree` | 业务侧 StateTree / PlayerBot |
| 渲染 | `ue-rendering` | 渲染管线 / 着色器（按需） |
| uasset | `ue-uasset-type-identify` | Content 资产类型识别 |
| Solo | `second-self` | 端到端交付（仍遵守分层） |

**业务岗禁止：** 在 `Source/SCL` 实现第二套战旗规则；WBP/View 直读 Battle；把 Core 实现塞回业务模块。

### 核心岗（`SCLCore` + `SCLTactical`）

目标：可复用系统与数据管线、战旗 L0 规则核。

| 细分岗 | Skill | 路径锚点（相对 GAME_ROOT） |
|--------|--------|---------------------------|
| 核心插件 **SCLCore** | 执行子代理 + 主程定界 | `Plugins/SCLCore/**` |
| 战旗核 **SCLTactical** | 执行子代理 + 主程定界 | `Plugins/SCLTactical/**`（由 ATBS 演进；类型可暂留 `UATBS*` 别名） |

**核心岗禁止：** Core/战斗模块依赖 `SCL` 游戏模块；Core 依赖 SCLTactical；新建 `Plugins/SCL`。

### 边界速判

| 任务特征 | 归岗 |
|----------|------|
| 换图 / 遭遇 / 切 IMC / 推 HUD / Presenter·ViewState | **业务岗** |
| 配表挂载 / 世界层铁律 / 回合队列 / 走格射击 / DesignData 叶节点 | **核心岗**（数据→SCLCore；格战执行→SCLTactical） |
