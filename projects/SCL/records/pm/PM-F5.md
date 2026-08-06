# PM 回馈主控 · F5

- **需求 ID：** F5（组织 profile / 花名册收口）
- **审核结论：** PASS（待 `records/review/REVIEW-F5.md` 落盘；BOARD 审核子任务运行中；PM 已对照 EXEC + 现场抽查）
- **已登记（ORG）：** 本文件；BACKLOG 同步 F5 → **完成**、F0–F5 迁移批闭合
- **阶段影响：** ARCH-F0 定义的 F1–F5 迁移刀序（SCLCore 壳 → 首批 Core 叶 → SCLTactical → 业务收口 → 组织花名册）**工程面 + 组织面均已闭合**；`profiles/SCL.md` 业务岗/核心岗与 SCLTactical/SCLCore 路径对齐 F0 职责表；清单 B / Bootstrap 下沉 **未动**，仍排队 **F4c**

## 自审对照

| 检查项 | 结果 |
|--------|------|
| 报告链齐全 | **条件 OK** · ARCH-F0（含 F5 DoD）+ EXEC-F5=DONE；REVIEW-F5 运行中，PM 已按 EXEC 自检表 + `profiles/SCL.md` / `PROJECT.md` 抽查替代预审 |
| 定界遵守 | OK · EXEC 声明仅改组织仓 `profiles/SCL.md` + 轻量 `PROJECT.md`；**未改 GAME_ROOT**；未大改 `docs/design`；git 范围与改动表一致（2 文件） |
| DoD | OK · ARCH-F0 · F5 五项 DoD 均满足（见下表） |
| 风险披露 | OK · 零工程代码变更；F4c / UATBS* 更名 / D3 / 脏文件债均未在本刀扩大；组织仓提交由 Gitea 子任务负责 |
| 下一项就绪 | OK · BACKLOG 下一项 **F4c** 须 **ARCH-F4c** 定界，前置 F4 PASS 已满足，但 GI/Consumer 接口未锁，**不宜在本批末抢开** |

### ARCH-F0 · F5 DoD 对照（PM 抽查）

| DoD 项 | 结论 |
|--------|------|
| `profiles/SCL` 区分业务岗 vs 核心岗 | ✅ 「业务岗」「核心岗」分节 + 边界速判 |
| 与 ARCH-F0 职责表对齐 | ✅ 模块分层、依赖方向、禁止项一致 |
| SCLTactical / SCLCore 路径正确 | ✅ `Plugins/SCLTactical/**`、`Plugins/SCLCore/**`；无 `Plugins/ATBS` 路径残留 |
| PROJECT 可选模块分层说明 | ✅ `PROJECT.md` 已增模块分层节 |
| EXEC 含定界声明 + 改动表 | ✅ EXEC-F5 齐全 |

## ARCH-F0 对 F0–F5 批末判断

- F0 迁移刀序 **F1–F5** 在 ARCH-F0 §「迁移刀序」中写死；**F5 为末刀**（组织 profile），不隐含 F4c。
- F4c（清单 B / Bootstrap 下沉）ARCH-F4 已裁定 **整体另刀**、须独立 ARCH-F4c；BACKLOG 记为排队，**不属于 F0–F5 批内必达项**。
- F0–F5 批目标态已达成：插件地图 SCLCore + SCLTactical + 业务 SCL；依赖链单向；组织花名册与工程分层同步。
- 开 F4c：前置 F4 PASS ✅，但接口/GI 设计未锁 → **本批末不开**；待老板/主控另起批或单独立项时先 ARCH-F4c。
- 升级老板：F1–F4 均 PASS、F5 薄刀无越界、无 FAIL 反复、无产品口径变更、无组织红线 → **不升级**。

```text
## PM 自我审核裁决
- 结论：结束本批（F0–F5 框架迁移批）
- 理由：ARCH-F0 定义的 F1–F5 刀序已全部 PASS/DONE；F5 组织花名册与职责表对齐，闭合迁移批最后一项；F4c 为清单 B 独立 ARCH 项，排队不抢本批末；无阻塞升级的 FAIL/契约缺口
- 债（不挡）：F4c（DesignData 四子系统 + Bootstrap cpp 下沉）排队待 ARCH-F4c；UATBS*/ATBS*.h 完整更名另开 ARCH；D3 可达圆；HostileVision / PlayerBotSmoke 脏文件；GAME_ROOT 历史 commit 与 gitea 分仓提交债；docs/design/** 路径债
```

## 主控后续（批末）

1. 跑 `workflow/BATCH_CLOSEOUT.md`（retro / BOARD / 不私自开 F4c 施工）。
2. 待 REVIEW-F5 落盘 PASS 后补链；若 FAIL → 撤回本裁决、不开批末。
3. F4c 下一动作：**派主程 ARCH-F4c**（非本批续刀）；老板可另批立项。
