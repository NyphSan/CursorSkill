# SOURCE — qwen-mm-plugins-blender

- **原仓**: https://github.com/QwenLM/Qwen-MM-Plugins
- **能力路径**: `src/capabilities/blender/`
- **NOTICE**: `src/capabilities/blender/NOTICE.md` (MIT 第三方代码归属)
- **许可证**: Apache-2.0
- **发布日期**: 2026-08-10
- **Stars**: ~1.6k (2026-08-11)
- **最近 commit**: 2026-08-11 (Merge PR #9)

## 收录说明

本 SKILL.md 为摘录索引，保留了 Blender 能力的核心架构、工具概要和安装方式。完整 cookbook (`cookbooks/blender/usage.md`) 和 MCP server 代码未复制。

## 为什么收录

1. **2026-08-10 刚发布** — 本轮搜索窗口内最新
2. **Apache-2.0** — 宽松许可，商用友好
3. **22 个 Blender 工具** — 建模/材质/灯光/渲染全覆盖
4. **多 agent 兼容** — 支持 Claude Code / Codex / Cursor / OpenClaw / Gemini CLI 等 9 个平台
5. **uvx 按需启动** — 依赖隔离，不污染全局环境
6. **套件协同** — core 能力可读取 3D 模型，blender 能力可创建，video-edit 可渲染输出

## 注意

- 需要 `DASHSCOPE_API_KEY`（阿里云 DashScope API）
- 推荐 Linux 或 WSL2 环境（原生 Windows 未验证）
- 与 `dcc-mcp-blender` 互补：Qwen 版轻量（22 工具），dcc-mcp 版重量级（200+ 工具）
