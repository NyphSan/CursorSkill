# CursorSkill

面向 **游戏设计 / 虚幻（UE）开发 / 3D·2D·UI 设计 / 研发工作流** 的 Agent Skills 精选库。

本仓不是全网镜像：只收录与方向相关、且能定位到 `SKILL.md` 的条目；每个技能保留原仓链接（见各目录 `SOURCE.md`）。

## 结构

```text
skills/
  game-design/   # 玩法、关卡、手感、叙事、小说转游戏…
  unreal/        # UE C++/蓝图/UMG/Niagara/MCP/Shader…
  ui-design/     # 游戏 UI 工作流、Figma、前端设计
  2d/            # 像素、角色、AI 游戏美术
  3d/            # Blender、Three.js、着色/VFX
  workflow/      # 研发工作流（精选）
DIGEST.md        # 每日侦察摘要（增量）
```

最新摘要见 [DIGEST.md](./DIGEST.md)（当前精选约 188 个 `SKILL.md`）。

## 安装（Cursor）

将需要的技能目录复制或软链到项目的技能路径，例如：

```bash
# 示例：引入游戏 UI 总控
mkdir -p .cursor/skills
cp -R skills/ui-design/game-ui-workflow .cursor/skills/
```

或按 Cursor / Agent Skills 文档指定的 skills 目录安装。**以原仓库安装说明为准**；本仓为精选摘录。

## 每日摘要

见 [DIGEST.md](./DIGEST.md)。

## 许可

各技能遵循其原仓库 LICENSE。使用前请核对 `SOURCE.md` 中的原仓链接。
