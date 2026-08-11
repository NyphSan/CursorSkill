---
name: qwen-mm-plugins-blender
description: >-
  Qwen-MM-Plugins Blender capability — 22 tools driving a running Blender
  instance through Python for 3D modeling, materials, lighting, and rendering.
  Part of Alibaba Qwen's multimodal plugin suite. Use when an AI agent needs
  to create or manipulate 3D content in Blender.
license: Apache-2.0
---

# Qwen-MM-Plugins — Blender Capability

## 用途

阿里 Qwen 团队多模态插件套件的 Blender 能力包。通过 Python 轻量客户端驱动运行中的 Blender 实例，提供 22 个工具覆盖建模、材质、灯光和渲染。

## 核心架构

```
Agent Skills (告诉模型工具存在) → MCP Server (执行实际工作) → uvx 按需启动
```

每个能力 = 一个 skill（模型感知）+ 一个可选 MCP server（工具实现）。依赖通过 `uvx` 按需隔离，不污染全局环境。

## Blender 工具（22 个）

| 领域 | 代表操作 |
|------|---------|
| 建模 | create_primitive, edit_mesh, boolean_ops |
| 材质 | create_material, set_color, assign_texture |
| 灯光 | create_light, set_intensity, setup_rig |
| 渲染 | render_scene, set_resolution, capture |

## 安装

```bash
# 引导安装
curl -fsSL https://raw.githubusercontent.com/QwenLM/Qwen-MM-Plugins/main/install.sh | bash

# 或按能力安装
qwen extensions install https://github.com/QwenLM/Qwen-MM-Plugins.git:qwen-mm-plugins-blender --consent
```

需要 `DASHSCOPE_API_KEY`（云端 VL/OCR/生成能力）和可选 `SERPER_API_KEY`（搜索）。

## 套件其他能力

| 能力 | 说明 |
|------|------|
| core | 图像/视频/文档/3D 模型读取 |
| api | 云端视觉/OCR/grounding/ASR/分割 |
| search | 网页搜索 + 反向图片搜索 |
| video-memory | 长视频分层图记忆 QA |
| video-edit | 视频/图像/音频生成编辑 |
| **blender** | **3D 建模/材质/灯光/渲染（本条）** |
| freecad | 参数化 CAD / STEP/STL / FEM |
| edu-agent | 数学/科学分步中文讲解视频 |

## 来源

- 仓库: https://github.com/QwenLM/Qwen-MM-Plugins
- 许可证: Apache-2.0 (Blender/FreeCAD 组件含 MIT 第三方代码)
- 发布: 2026-08-10
- Stars: ~1.6k (2026-08-11)
- 支持: Claude Code / Codex / Cursor / OpenClaw / Gemini CLI / Qwen Code / Qoder
