---
name: unreal-motion-graphics-mcp
description: Guide for using Unreal Motion Graphics (UMG) via the UnrealMotionGraphicsMCP plugin and its bundled Skills. Use when building or editing UMG widgets with an agent that can call MCP tools against a running Unreal Editor.
---

# Unreal Motion Graphics MCP

面向 **UMG** 的 UE 插件 + Skills + MCP。适合用 Agent 驱动编辑器内 Widget 工作流，而不是纯 Web UI skill。

## When to use

- 做 HUD / 菜单 / UMG 控件树
- 已安装或准备安装 `UmgMcp` 插件，并且 Cursor/Agent 能连上对应 MCP

## Prerequisites

1. 从上游安装插件到引擎/项目（见原仓 `UmgMcp.uplugin`）
2. 配置 MCP，确认 tools/list 可见
3. 加载上游 `Skills/` 下配套 SKILL.md

## Workflow

1. 确认 Editor 在跑且 MCP 健康
2. 用配套 skill 描述目标 Widget/交互
3. 通过 MCP 查询/修改控件，再在 Editor 内目视验收
4. 变更记入工程记忆；不要改 `Plugins/AirSim/`

## Risks

- 需要额外插件与 MCP，非纯 Markdown skill
- 与个人 `ue-materials` / WP skill 正交；不要互相替代
