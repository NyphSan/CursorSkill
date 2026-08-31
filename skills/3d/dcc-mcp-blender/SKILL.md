---
name: dcc-mcp-blender
description: >-
  Blender DCC-MCP adapter — 200+ pre-built tools across 29 categories for
  3D scene management, object manipulation, mesh editing, UV ops, rigging,
  materials, shader nodes, lighting, camera, rendering, physics, geometry
  nodes, animation, import/export, validation, and pipeline publishing.
  Embeds a Streamable HTTP MCP server directly in Blender 4.2+.
  Use when controlling Blender through AI agents.
license: MIT
---

# DCC-MCP Blender — 200+ Tool Blender MCP Adapter

## 用途

在 Blender 4.2+ 内部嵌入 Streamable HTTP MCP 服务器，让任何 MCP 兼容的 AI 客户端（Claude Desktop / Cursor / Claude Code 等）通过 200+ 预构建工具驱动完整 3D 工作流。

## 工具分类（29 类 / 200+ 工具）

| 类别 | 工具数 | 代表操作 |
|------|--------|---------|
| scene | 6 | new/open/save/list/get_info |
| objects | 17 | create/delete/move/rotate/parent/group |
| mesh-ops | 9 | triangulate/separate/combine/merge/mirror |
| uv-ops | 10 | create/copy/project/unwrap/pack |
| rigging | 9 | armature/bone/constraint/bind/retarget |
| shader-nodes | 15 | create/connect/disconnect/set_input |
| material-library | 10 | presets/texture/color_management |
| texture-bake | 5 | bake_ao/bake_lighting/transfer_maps |
| render | 4 | render_scene/set_settings/capture_viewport |
| render-farm | 8 | validate/submit/status/cancel |
| physics | 16 | rigid_body/cloth/collision/bake_sim |
| geometry-nodes | 5 | add/list/create/assign/evaluate |
| animation | 7 | keyframe/frame_range/bake |
| light-rig | 10 | three_point/softbox/hdri/aim |
| interchange | 8 | fbx/obj/usd/gltf/alembic/batch |
| validation | 6 | scene/mesh/material/animation/export |
| pipeline | 6 | metadata/tag/publish_manifest |
| dev | 13 | attach/reload/run_check/capture_ui |

## 安装

### Blender Extension（推荐手动）
1. 下载平台对应 ZIP（Win64/Linux/macOS）
2. Blender 4.2+ → Edit → Preferences → Extensions → Install from Disk
3. 启用 DCC MCP Blender

### pip
```bash
pip install dcc-mcp-blender
```

## 技能系统

- 内置 10 个技能类别，可扩展自定义技能
- `SKILLS_INDEX.md` 提供分阶段加载指南和任务-技能链路映射
- 环境变量 `DCC_MCP_BLENDER_SKILL_PATHS` 支持额外技能路径

## 来源

- 仓库: https://github.com/dcc-mcp/dcc-mcp-blender
- 版本: 0.1.43
- 许可证: MIT (源码) / GPL-3.0-or-later (Blender Extensions ZIP)
- Blender: 4.2+ (Extension 格式)
- 传输: Streamable HTTP (MCP 2025-03-26 兼容)
