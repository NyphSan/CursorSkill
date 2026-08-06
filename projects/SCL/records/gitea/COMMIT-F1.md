# Git 提交说明（仓库管理员填写）

- **仓：** 项目 SCL（`http://192.168.3.23:3000/SCLG/SCL.git`）
- **分支：** `autoAISkill`
- **关联刀：** F1
- **hash：** `a60cb80af6aa12913b0b56039d6ef32a07065cfa`
- **push：** 成功（`46c8eb12..a60cb80a  autoAISkill -> autoAISkill`）
- **GAME_ROOT：** `E:\Project\Game\S_\SCL`
- **时间：** 2026-08-06

## Subject（一行）

```text
feat(sclcore): add SCLCore plugin shell and wire game module dependency
```

## Body

```text
为什么改 / 改了什么要点：
- F1：落地 Plugins/SCLCore 标准空壳（uplugin + Build.cs + Module + Public API 锚点）
- SCL.uproject 启用 SCLCore
- Source/SCL/SCL.Build.cs PrivateDependencyModuleNames 增加 SCLCore
- 未混入 ATBS 或其他业务改动（工作区 ATBS 改动保持 unstaged）

风险与债：
- 首次 push 因远程超前被拒；stash ATBS 无关改动后 rebase 到 origin/autoAISkill 再推送成功
- rebase 后 hash 由 f490651e 变为 a60cb80a（以 push 后 hash 为准）
```

## 自检

- [x] 未混入无关文件（仅 SCLCore 源 + uproject + SCL.Build.cs；Binaries/Intermediate 被 gitignore）
- [x] 无密钥
- [x] 与 EXEC/DONE-F1 一致
- [x] push 成功（非 BLOCKED_PUSH）

## 提交文件清单

| 路径 | 操作 |
|------|------|
| `Plugins/SCLCore/SCLCore.uplugin` | A |
| `Plugins/SCLCore/Source/SCLCore/SCLCore.Build.cs` | A |
| `Plugins/SCLCore/Source/SCLCore/Private/SCLCoreModule.cpp` | A |
| `Plugins/SCLCore/Source/SCLCore/Public/SCLCore.h` | A |
| `Plugins/SCLCore/Source/SCLCore/Public/SCLCoreModule.h` | A |
| `SCL.uproject` | M（启用 SCLCore） |
| `Source/SCL/SCL.Build.cs` | M（Private 依赖 SCLCore） |

## 依据

- 主控派工 / 主程通知：`records/lead-eng/DONE-F1.md`
- EXEC：`records/exec/EXEC-F1.md`
- 规则：`rules/06_gitea_repo_admin.md`
