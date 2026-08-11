---
name: quodsoler-unreal-engine-skills
description: >-
  27 Unreal Engine 5 C++ skills for AI coding agents. Source-audited against
  UE engine source with 160+ inaccuracies corrected. Covers core C++,
  gameplay systems, rendering/VFX, world & data, AI & logic, UI & input,
  build & tools. Use when writing production UE5 C++ code with AI agents.
license: MIT
---

# quodsoler/unreal-engine-skills — 27 UE5 C++ Skills

## 用途

为 AI 编码代理（Claude Code / Cursor / Windsurf 等）设计的 UE5 C++ 技能集。每个技能经过 UE 引擎源码验证，修正了 160+ 处不准确内容（错误函数签名、不存在的方法、已弃用 API 等），确保 AI 生成的代码无幻觉 API。

## 27 个技能分类

| 分类 | 技能数 | 技能列表 |
|------|--------|---------|
| Core C++ | 3 | ue-cpp-foundations, ue-actor-component-architecture, ue-module-build-system |
| Gameplay Systems | 6 | ue-gameplay-framework, ue-gameplay-abilities, ue-animation-system, ue-character-movement, ue-game-features, ue-networking-replication |
| Rendering & VFX | 4 | ue-materials-rendering, ue-niagara-effects, ue-audio-system, ue-sequencer-cinematics |
| World & Data | 5 | ue-world-level-streaming, ue-procedural-generation, ue-physics-collision, ue-serialization-savegames, ue-data-assets-tables |
| AI & Logic | 3 | ue-ai-navigation, ue-state-trees, ue-mass-entity |
| UI & Input | 2 | ue-ui-umg-slate, ue-input-system |
| Build & Tools | 3 | ue-editor-tools, ue-testing-debugging, ue-async-threading |
| Project Setup | 1 | ue-project-context（基础技能，被所有其他技能首先读取） |

## 关键特性

- **源码审计**：每条 API 均对照 UE5 引擎头文件验证
- **无幻觉 API**：修正 160+ 处不准确（函数签名/不存在方法/已弃用 API）
- **跨引用机制**：`ue-project-context` 是基础技能，所有其他技能首先读取它
- **SKILL.md < 500 行**：超长内容移至 `references/` 目录

## 安装

```bash
# CLI 安装
npx --yes skills@latest add quodsoler/unreal-engine-skills

# 或 Clone 复制
git clone https://github.com/quodsoler/unreal-engine-skills.git
cp -r unreal-engine-skills/skills/* ~/.claude/skills/
```

## 使用示例

```
"Add a replicated health attribute with GAS"
→ 自动使用 ue-gameplay-abilities 技能

"Set up World Partition streaming for my open world"
→ 自动使用 ue-world-level-streaming 技能
```

## 来源

- 仓库: https://github.com/quodsoler/unreal-engine-skills
- 许可证: MIT
- 初始发布: 2026-03-02
- 技能数: 27
- 作者: quodsoler
