---
name: quodsoler-unreal-engine-skills
description: Router/catalog for 27 Unreal Engine C++ Agent Skills (gameplay, rendering, networking, animation, GAS, modules). Use when writing UE5 C++ and you need production-oriented skill packs beyond local AirSimUE skills.
---

# Quodsoler Unreal Engine Skills（目录 skill）

上游合集：**27** 个 UE C++ Agent Skills（MIT），覆盖 Actor/Component、动画、GAS、Gameplay Framework、Networking/Replication、模块/插件等。

## When to use

- 需要 UE5 C++ 正确写法与领域知识时
- 本仓已有 `ue-*` 个人 skill 未覆盖的子系统（GAS、复制、动画图等）

## How to use

1. 打开上游仓库索引，按任务选具体 skill 目录
2. 将对应 `SKILL.md`（及 `references/`）拷入本机 `~/.cursor/skills/` 或本仓 `skills/unreal/<name>/`
3. 不要一次装全 27 个，避免上下文噪声

## Suggested first pulls

- ue-actor-component-architecture
- ue-gameplay-framework
- ue-gameplay-abilities（若用 GAS）
- ue-networking-replication（若做联机）

## Notes for AirSimUE

- 工程禁改 `Plugins/AirSim/`
- C++ 约定仍以工程 `unreal-cpp` 规则为准；本目录 skill 为补充知识
