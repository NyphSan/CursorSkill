---
name: kevinpbuckley-unreal-engine-skills
description: Use when writing UE 5.8 C++, designing gameplay systems, or making Blueprint / asset / content decisions. Provides pure UE domain knowledge (correct classes, real API signatures, idiomatic patterns, sharp edges, engine source references) — NOT an MCP automation tutorial. Auto-loads for any Unreal Engine task in a 5.8 project.
---

# kevinpbuckley/unreal-engine-skills — UE 5.8 domain knowledge pack

A **pure-knowledge** skill pack (not an MCP layer, not a button-clicker) covering 61 UE skills in **8 categories**, all retargeted to **Unreal Engine 5.8** as of 2026-08-04. The pack ships with mandatory `references/`, optional `scripts/`, optional `assets/` per skill — conforming to the Agent Skills format.

These skills are **what to do**, not **how to click**. They cover correct class names, real API signatures, idiomatic patterns, sharp edges, and engine-source references. MCP bridges to the live editor are a separate concern (e.g. `ue-mcp-*` skills in this repo).

## When to use

Pull this pack in when the user is **authoring or reviewing** UE code or design, especially:

- Writing or editing **Unreal C++** (game classes, modules, build files)
- Choosing between **Blueprint vs C++** for a system
- Composing **assets, content, animation, Sequencer, materials, Niagara, audio**
- Working with **Gameplay Framework**: GameMode/State, Actor/Component, Pawn/Character, Enhanced Input, Subsystems, GAS, replication, save games
- **World building**: level streaming, World Partition, landscape + foliage, lighting + Lumen, Nanite + rendering pipelines
- Doing the **tooling work**: editor scripting (Python/C++), plugins, automation tests, profiling, packaging, debug workflows
- Cross-cutting: engine source navigation, coding standards

## Categories at a glance (61 skills, 216 markdown files)

| Category | # skills | Highlights |
|---|---:|---|
| Cross-cutting / meta | 2 | Engine source navigation, coding standards |
| C++ foundations | 7 | UObject reflection, modules/build, memory/GC, core types, delegates, logging |
| Gameplay framework | 8 | GameMode, Actor/Component, Character movement, Enhanced Input, Subsystems, GAS |
| Blueprints | 2 | BP basics, C++ ↔ Blueprint integration |
| Content & assets | 5 | Asset mgmt, content import, mesh, materials, data-driven design |
| Animation | 3 | Animation system, Control Rig / IK, Sequencer / cinematics |
| World building | 4 | Levels / World Partition, landscape + foliage, lighting / Lumen, Nanite / rendering |
| VFX & audio | 2 | Niagara VFX, Audio / MetaSounds |
| UI | 1 | UMG / Slate / CommonUI |
| Systems | 4 | Networking / replication, physics / Chaos, AI / navigation, save / load |
| Tooling, pipeline, quality | 7 | Editor scripting (Python), plugins, automation tests, profiling, packaging, debug |
| Marketplace asset pack skills | 14 | Ultra Dynamic Sky (10), Ultra Dynamic Weather (4) |

## How it fits this repo

- This skill is **complementary** to the MCP-layer skills already in `skills/unreal/` (e.g. `ue-mcp-blueprint`, `ue-mcp-workflow`, `vibeue-blueprints`, `epic-unreal-mcp`). MCP skills drive the editor; this pack tells the model **what is correct in UE itself**.
- Cross-references:
  - For BP graph writing: pair with `skills/unreal/ue-mcp-blueprint/` (DSL vs node)
  - For Niagara: pair with `skills/unreal/dcc-unreal-niagara/` and `skills/unreal/niagara-json-generator/`
  - For GAS: pair with `skills/unreal/unrealsharp-operations/` and `skills/unreal/ue-gameplay-ability-system/`
  - For UMG: pair with `skills/unreal/ue5-ui-umg-slate/` and `skills/unreal/unreal-motion-graphics-mcp/`

## Install modes

The upstream ships skills under `skills/<category>/<skill-name>/SKILL.md`. Any of the 61 can be installed:

- **Whole pack**: copy the entire `skills/` directory into the consuming agent's skill path (`.claude/skills/`, `.cursor/skills/`, etc.)
- **Per skill**: copy only the relevant leaf directory — recommended for projects not needing the whole surface area
- **As references**: keep on disk as `references/` for the model to consult on-demand without loading into context

## Sharp edges

- License field was not visible on the upstream repo README at scout time — verify the upstream LICENSE file before redistributing; do not assume MIT without confirmation.
- Pack is **authored against UE 5.8 only**. For 5.4 / 5.6 / 5.7 projects some patterns (e.g. Epic Toolset Registry, UEFN properties) may not map cleanly.
- The 14 Marketplace-pack skills depend on **specific Marketplace assets** (Ultra Dynamic Sky, Ultra Dynamic Weather). Pull those **only** when those assets are present in the consuming project.

## Search coverage note

This entry was promoted from the **2026-08-06 watch list** after the upstream repo underwent a complete audit and retargeted all 61 skills to UE 5.8 on 2026-08-04.
