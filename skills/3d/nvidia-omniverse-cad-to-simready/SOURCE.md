# SOURCE — nvidia-omniverse-cad-to-simready

- **原仓**: https://github.com/NVIDIA/skills
- **原路径**: `skills/omniverse-cad-to-simready/`
- **许可**: Apache-2.0 (SOURCE) / CC BY 4.0 (DOCS)
  - 本仓 SKILL.md 为基于上游公开版本（v0.2.0）撰写的可移植摘录；遵循原许可，使用前请到原仓核对 LICENSE
- **原版本**: 0.2.0
- **收录日期**: 2026-08-14（每日 cron 09:55+08:00 侦察）
- **触发词**: "CAD to SimReady" / "source asset to SimReady" / "SimReady package" / "SimReady conformance" / "USD to UE"

## 为什么收录

1. **NVIDIA 官方维护、Apache-2.0 + CC BY 4.0 双重许可** — 与 Anthropic / Adobe 官方仓一致的法律清晰度
2. **本仓 3D 主向首个 SimReady / USD 物理仿真类条目** — 补齐 `dcc-mcp-blender`（视觉）、`qwen-mm-plugins-blender`（多模态）之外的「仿真就绪」第三象限
3. **UE 5.2+ 原生支持 USD 导入**（`Datasmith USD` / `Interchange USD`），产出的 SimReady USD 可直接落到 UE 项目，跳过手工 `UPhysicalMaterial` / 碰撞体配置
4. **活跃维护**：原仓今日 08-14 仍有 commit（孤儿技能清理 + 元数据索引刷新）
5. **OMS 签名 + 技能卡片 + 评估数据集** — 业界少见的端到端技能治理流水线
6. **内容创作 → 仿真 → UE 数字孪生** 的全链路单点入口（CAD → USD → SimReady → UE/Isaac Sim）

## 关键工程细节

- **运行环境**：Linux/macOS + Docker + NVIDIA Container Toolkit + GPU + Python 3.12
- **API 密钥**：默认 `property_assignment_intent=run` 需 Content Agents（`NVIDIA_API_KEY` 或 OpenAI / Anthropic / Google / Gemini 任一兼容 backend）
- **状态机**：`passed` / `blocked` / `failed` / `needs_rerun`（无 `complete` —— 任何残留工作都进 `needs_rerun`）
- **阶段门**：preflight → Content Agents 部署 → 转换 → 最小验证 → 属性分配 → profile → 全验证 → 渲染 → 打包 → 报告

## 与本仓现有条目的互补

| 现有条目 | 与本条目的关系 |
|---|---|
| `dcc-mcp-blender`（3D 视觉） | 互补：本条目偏「物理仿真就绪 + UE 导入」；dcc-mcp-blender 偏「Blender 视觉资产 + 200+ 工具」 |
| `qwen-mm-plugins-blender`（3D 多模态） | 互补：本条目是 NVIDIA 官方物理仿真链；Qwen 是多模态套件 |
| `unreal-blueprints` / `unreal-cpp-gameplay`（UE） | 互补：本条目产出 SimReady USD 后，UE 侧用 unreal-blueprints / unreal-cpp-gameplay 处理导入与运行时逻辑 |
| `dcc-mcp`（workflow 路由） | 互补：本条目是单产品深链；dcc-mcp 是 10+ DCC 统一路由层 |

## 收录摘要

SKILL.md 重写为可移植的 14 步工作流 + 8 条硬规则（preflight / Content Agents gate / 验证策略 /
阶段引用原则 / 停止条件 / GSP.001 路由）。完整 14 references 链未复制（`workflow.md` /
`commands.md` / `troubleshooting.md` / `assemble-package-source/README.md` 等），需要时请到原仓按需拉取。
