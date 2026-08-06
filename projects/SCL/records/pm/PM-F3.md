# PM 回馈主控 · F3

- **需求 ID：** F3（F3a 定界 + F3b 施工）
- **审核结论：** PASS（`records/review/REVIEW-F3.md`）
- **已登记（ORG）：** 本文件；主控同步 BACKLOG（F3b → **完成**）
- **阶段影响：** ATBS 插件/模块已迁 **SCLTactical**；依赖链 `SCL → SCLTactical → SCLCore → Engine` 定版；战旗生产入口（Bridge/EndTurn）未动；可进入 F4 闸门（须先 ARCH-F4）

## 自审对照

| 检查项 | 结果 |
|--------|------|
| 报告链齐全 | OK · ARCH-F3 + EXEC-F3 + REVIEW-F3=PASS + DONE-F3 |
| 定界遵守 | OK · REVIEW 越界检查 PASS；EXEC 声明遵守 ARCH-F3 阶段 A–E；`Source/SCL/Content/Tactical/` git diff 为零 |
| DoD | OK · ARCH-F3 八项 DoD 在 REVIEW 均有 PASS 结论（插件迁移、Build 依赖、编译、类型过渡、Demo 重定向、契约/公式未改、EXEC 证据齐全） |
| 风险披露 | OK · D1/D2 脏改动已声明基线 commit `779494e1` 并合入迁移；HostileVisionComponent / PlayerBotSmoke 脏文件未触；UATBS* 完整更名 deferred；编译 dll 现场未保留（gitea 提交前建议复编） |
| 下一项就绪 | OK · BACKLOG 下一项 **F4 业务依赖收口** 依赖 F2+F3 均已 PASS；F0 已写 F4 目标态与路径原则，**但 F0 硬规则要求 F4 开工前须独立 ARCH 锁当刀清单** |

## ARCH-F0 对 F4 可开性判断

- F0 已定版 F4：**业务层收口** — `SCL.Build.cs` 依赖方向正确；业务不承载已迁 Core 的重复实现；无 `#include`/模块倒灌；Presenter/3C 仍在业务。
- F0 明确：**F2–F4 细表由各刀 ARCH 再锁**；**不得仅凭 F0 大挪移**。
- F2 清单 B（DesignData 四子系统 / Bootstrap 下沉等）ARCH-F2 标为后续 F2b/F4 — 是否纳入 F4 由 **ARCH-F4** 书面锁清单，PM 不在此扩 scope。
- 故：**不可直接开 F4 施工**；须先派主程出 **ARCH-F4（业务依赖收口与允许删改路径）**。
- 风险是否升级老板：F3 面大（整插件迁移 + D1/D2 债合入）但 REVIEW 已验、契约未动、无 FAIL 反复 → **不升级**。

```text
## PM 自我审核裁决
- 结论：开下一项 F4（定界刀）
- 理由：F3 报告链 PASS、DoD 全绿、依赖链定版；F4 前置 F2+F3 已满足且 BACKLOG 已排队，但 F0 要求 F4 独立 ARCH 锁当刀删改清单，主控须先派 ARCH-F4 再施工
- 债（不挡）：UATBS*/ATBS*.h 完整类型更名须另开 ARCH；HostileVisionComponent 等工作区脏文件勿混入 F3 gitea commit；D3 可达圆（平面圆→真实可达集）仍排队；清单 B/Bootstrap 下沉待 F4 ARCH 裁定；D1/D2 已合入 SCLTactical 的人手坡测债；gitea 提交前建议复编留 dll 证据
```
