# SOURCE — nvidia-omniverse-usd-performance-tuning

- **原仓**: https://github.com/NVIDIA/skills
- **原路径**: `skills/omniverse-usd-performance-tuning/`
- **许可**: Apache-2.0 (SOURCE) / CC BY 4.0 (DOCS)
  - 本仓 SKILL.md 为基于上游公开版本（v0.1.0）撰写的可移植摘录；遵循原许可，使用前请到原仓核对 LICENSE
- **原版本**: 0.1.0
- **收录日期**: 2026-08-14（每日 cron 09:55+08:00 侦察）
- **触发词**: "USD performance" / "Optimize this USD stage" / "USD too slow" / "USD high memory" / "USD validation failed"

## 为什么收录

1. **NVIDIA 官方维护、Apache-2.0 + CC BY 4.0** — 双重许可，法律清晰度高
2. **与 `nvidia-omniverse-cad-to-simready` 同源互补** — 前者偏「产资产」（CAD → SimReady），本条目偏「优化已有资产」（USD 性能瓶颈诊断 + 修复）
3. **覆盖 UE/ArchViz/数字孪生通用痛点** — 大量 USD 场景导入 UE 后出现 draw-call 爆炸 / FPS 掉帧 / 显存爆炸，本条目提供上游修复链路
4. **活跃维护**：原仓今日 08-14 仍有 commit（孤儿技能清理 + 元数据索引刷新）
5. **状态机 + blocker codes**（`blocked_missing_usd_optimize` / `blocked_missing_usd_optimize_operation`）— 业内少见的明示错误形态，便于前端 / IDE 决策
6. **三个 scoped iterations** 的迭代节奏（baseline → after → compare）— 借鉴 Unreal Insights 的 frame-delta 思维，用户友好

## 关键工程细节

- **状态机字段**：`ready_to_plan`（默认）/ `approval_required`（gate 阻塞）/ `blocked`（运行时报错）；后续 gate 走 `gates_observed` 不入 `decision`
- **强制链式协议**：`omniverse-usd-performance-tuning` → `profile-stage:baseline` → `usd-structure-assessment` → `usd-validation-runner` → `restructure-decision` → `apply-restructure` → `usd-optimize-run-validators` → `usd-optimize-interpret-validators` → `usd-optimize-run-operations` → `profile-stage:after` → `compare-profiles` → `optimization-report`
- **条件必选里程碑**：`usd-hierarchy-dedupe-candidates`（自动 dedupe 候选收集） + `usd-edit-target-planner`（edit target 规划）
- **决策门**：bounded-loss ops（`decimateMeshes` / `fitPrimitives`）在 conservative band 内默认可执行；超过 band 或在 functional-precision 目标上变 inline-elicited

## 与本仓现有条目的互补

| 现有条目 | 与本条目的关系 |
|---|---|
| `nvidia-omniverse-cad-to-simready`（3D 仿真产出） | 互补：本条目优化已有 USD；cad-to-simready 产出新 SimReady USD |
| `dcc-mcp-blender`（3D 视觉） | 互补：本条目偏 USD 性能 + 优化链接；dcc-mcp-blender 偏 Blender 工具调用 |
| `blender-pro-workflow` / `blender-modeler` | 互补：本条目处理 USD / 大场景；本仓 Blender 条目偏单文件工作流 |
| `unreal-blueprints` / `unreal-cpp-gameplay`（UE 运行时） | 互补：本条目是 USD 上游优化；UE 条目处理运行时逻辑 |
| `level-design` / `level-design`（game-design 跨引擎） | 概念同源：本条目的 `profile-stage:baseline` → `compare-profiles` 与 UE Insights Frame Delta 同构 |

## 收录摘要

SKILL.md 重写为可移植的工作流抽象（decision 字段 + canonical plan contract + routing map +
deliverables + 与 UE 团队的 IDE 类比）。完整 references 链（`workflow.md` /
`runtime-artifact-token-budget.md` / `skill-map.md` / `troubleshooting.md` /
`upstreams/usd-optimize.md` 等）未复制，需要时请到原仓按需拉取。
