# Gitea 提交记录 · F3

- **需求：** F3 ATBS → SCLTactical 插件迁移
- **依据：** EXEC-F3、REVIEW-F3 PASS、DONE-F3
- **GAME_ROOT：** `E:\Project\Game\S_\SCL`
- **分支：** autoAISkill
- **hash：** `a7b58498f0814971baf85ba80bce5ae784d670e8`（短：`a7b58498`）
- **Subject：** `feat(scltactical): migrate ATBS plugin to SCLTactical with SCLCore dependency`
- **Push：** 成功（`origin/autoAISkill` 与本地 HEAD 一致）

## 提交范围

- 删除 `Plugins/ATBS/` 整树
- 新增 `Plugins/SCLTactical/` 整树（含 Content/Source/uplugin/README 等）
- `SCL.uproject`（插件引用 ATBS → SCLTactical）
- `Source/SCL/SCL.Build.cs`（模块依赖）

**统计：** 238 files changed, 223 insertions(+), 157 deletions(-)

## 刻意未纳入本次 commit（工作区仍保留修改）

| 路径 | 原因 |
|------|------|
| `Source/SCL/Content/Combat/HostileVisionComponent.cpp` | 主控派工排除（非 F3 刀范围） |
| `Source/SCL/Content/Combat/HostileVisionComponent.h` | 同上 |
| `Source/SCL/Content/Control/Controller/SCLPlayerBotSmokeCommands.cpp` | 同上 |

## Push 备注

- 首次 `git push` 报 `unable to rewind rpc post data`（大体积插件/Content 重命名）；在本仓临时增大 `http.postBuffer` 后重试，远程已为 `a7b58498`（`Everything up-to-date`）。

## 前序

- F2：`779494e1` — feat(sclcore): migrate first-batch framework and data types into SCLCore
