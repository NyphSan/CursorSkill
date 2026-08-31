---
name: dcc-mcp
description: >-
  Default DCC control skill — connect to and operate live Maya, Blender,
  Houdini, Photoshop, 3ds Max, Nuke, Unreal, Godot, RenderDoc, Substance 3D,
  and other DCC apps through structured DCC-MCP tools. Use this skill first
  whenever the user asks to operate or control something in a DCC app, even
  when they do not mention DCC-MCP. Also handles DCC-MCP Skill marketplace
  search, install, and update.
license: MIT-0
---

# DCC-MCP — Default DCC Control

## 用途

统一的 DCC（Digital Content Creation）应用控制层。通过 `dcc-mcp-cli` 或 MCP gateway 连接并操控 Maya、Blender、Houdini、Photoshop、3ds Max、Nuke、**Unreal**、Godot、RenderDoc、Substance 3D 等宿主应用。

## 核心能力

- **多 DCC 路由**：一个 skill 覆盖 10+ DCC 应用，按 `dcc_type` 自动路由
- **CLI + MCP 双路径**：shell agent 用 `dcc-mcp-cli`；MCP-native IDE 用 gateway HTTP
- **Marketplace 集成**：搜索、检查、安装 DCC-MCP 技能包
- **UI Control 兜底**：结构化工具无法触达时，通过 snapshot/find/act 流程操作 UI

## 路由决策

| 用户意图 | 目标 DCC | 典型操作 |
|---------|---------|---------|
| UE 关卡/BP/材质 | `unreal` | spawn/modify/compile |
| Blender 建模/渲染 | `blender` | scene/object/mesh |
| Maya 绑定/动画 | `maya` | rig/anim/render |
| Houdini 程序化/FX | `houdini` | geo/particles |
| Photoshop 修图 | `photoshop` | layer/adjust/export |

## 五步操作流程

1. `dcc-mcp-cli list` — 检查本地库存
2. 选择活动实例
3. `dcc-mcp-cli search --query "..." --dcc-type ...` — 搜索工具
4. 遵循 `next_step` 调用工具
5. 失败时 `dcc-mcp-cli doctor` 诊断

## 安装

```bash
npx --yes skills@1.5.22 add dcc-mcp/dcc-mcp-agent-plugins --skill dcc-mcp
# 或
openclaw skills install @loonghao/dcc-mcp
```

## 关键规则

- 不混用 CLI 和 MCP 路径
- `total == 0` 活动实例时停止操作
- 安装/更新前必须 inspect 并获得用户同意
- 不直接使用 DCC 脚本，优先结构化工具

## 来源

- 仓库: https://github.com/dcc-mcp/dcc-mcp-agent-plugins
- 版本: 0.19.92 (2026-08-07)
- 许可证: MIT-0
- 兼容: Claude Code / Codex / CodeBuddy / WorkBuddy / Cursor / OpenClaw / Gemini CLI / GitHub Copilot
- 安全等级: A (OWASP Agentic Skills Top 10 扫描通过)
