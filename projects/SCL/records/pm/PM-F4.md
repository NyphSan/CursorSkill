# PM 回馈主控 · F4

- **需求 ID：** F4（F4a 定界 + F4b 施工 · 业务层收口）
- **审核结论：** PASS（`records/review/REVIEW-F4.md`）
- **已登记（ORG）：** 本文件；主控同步 BACKLOG（F4a/F4b → **完成**；F4c/F5 保持排队）
- **阶段影响：** 业务层依赖方向 `SCL → SCLTactical → SCLCore → Engine` 已验证；模块内 README / `SCL_SourceLayout.md` 对齐 Core 路径；清单 B / Bootstrap **未动**；Presenter/3C/Bridge 零改动；F0 迁移刀序 F1–F4 工程面闭合

## 自审对照

| 检查项 | 结果 |
|--------|------|
| 报告链齐全 | OK · ARCH-F4 + EXEC-F4 + REVIEW-F4=PASS + DONE-F4 |
| 定界遵守 | OK · REVIEW 越界检查 PASS；EXEC 声明遵守 ARCH-F4 清单 A + 可选 B；git diff 7 文件与改动表 1:1；Content/Tactical\|Control\|UI 与 Plugins diff 为零 |
| DoD | OK · ARCH-F4 八项 DoD 在 REVIEW 均有 PASS 结论（无双份/无倒灌/Build.cs/文档/README/红线未触/三模块编译/EXEC 证据齐全） |
| 风险披露 | OK · 清单 B（四子系统/WorldLayer/CalendarDisplay）与 Bootstrap cpp 下沉 deferred 至 F4c；UATBS* 完整更名 deferred；GAME_ROOT 7 文件 **未 stage**（gitea 须仅 add 本刀）；HostileVision / PlayerBotSmoke 脏文件未触；编译 dll REVIEW 未复跑 |
| 下一项就绪 | OK · BACKLOG 下一项 **F5 组织 profile** 仅依赖 F0（ARCH-F4 书面推荐 F4 后进入 F5）；F4c 清单 B 下沉须独立 ARCH，前置 F4 已 PASS 但接口/GI 设计未锁，不宜与 F5 抢序 |

## ARCH-F0 对下一项可开性判断

- F0 刀序 F1–F4 工程迁移目标（SCLCore 壳 → 首批叶节点 → SCLTactical → 业务收口）**均已 PASS**。
- F0 定义 **F5**：`profiles/SCL` 区分业务岗 vs 核心岗，与本职责表对齐；依赖 F0，**可与工程刀并行、主控执行**。
- ARCH-F4 裁定：清单 B / Bootstrap **整体另刀**（BACKLOG 记 **F4c**）；F4 完成后 **可进入 F5**；不得在本刀扩 scope 下沉四子系统。
- `profiles/SCL.md` 仍写「战旗核 ATBS / Plugins/ATBS/**」— 与 F3 SCLTactical、F4 模块分层 **不同步**，F5 正当其时。
- F4c 开性：F4 PASS 解除「业务收口未验证」阻塞，但下沉需 GI/Consumer 接口化（ARCH-F2/F4 均已书面说明），**须先 ARCH-F4c 定界**，不可直接施工。
- 风险是否升级老板：F4 薄刀 PASS、无 FAIL 反复、无产品口径变更、无组织红线 → **不升级**。

```text
## PM 自我审核裁决
- 结论：开下一项 F5（组织 profile）
- 理由：F4 报告链 PASS、DoD 全绿，F0 迁移刀序 F1–F4 工程面已闭合；ARCH-F4 与 REVIEW 均推荐 F4 后进入 F5；F5 仅依赖 F0、改组织仓 profile/花名册、风险低于 F4c；F4c 清单 B/Bootstrap 下沉须独立 ARCH 锁 GI 接口，排队不抢 F5
- 债（不挡）：F4c（清单 B + Bootstrap cpp 下沉）排队待 ARCH-F4c；UATBS*/ATBS*.h 完整更名另开 ARCH；GAME_ROOT 7 文件 gitea 提交前仅 stage 本刀、建议复编留 dll；HostileVision / PlayerBotSmoke 勿混入 F4 commit；docs/design/** 路径债；D3 可达圆仍 BACKLOG 外债
```
