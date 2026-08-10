---
name: ue-mcp-niagara
description: Use when authoring, editing, or troubleshooting Unreal Engine Niagara VFX emitters and modules through the ue-mcp MCP server. Covers emitter vs system scope, module stack authoring, renderer settings, curve/color editing, and runtime driving from Blueprints or C++. Auto-loads when the user mentions Niagara, VFX, particles, emitters, or modules in a UE project using ue-mcp.
---

# ue-mcp niagara authoring

The `niagara` tool exposes emitter-level operations through ue-mcp's action-dispatch interface. Use it for **runtime-emitter reads and edits**, not for graph-level authoring (which goes through the C++ bridge or Epic's Toolset plugins where available).

## Authoring discipline

**Read → mutate → validate → save.** Never fire-and-forget. Niagara emitters carry module stacks, renderers, and per-emitter DI (Data Interface) configuration; getting any of them wrong tends to look fine in the editor but fail at runtime.

```text
niagara(action="list_emitters", systemPath=...)
niagara(action="read_emitter", emitterName=...)             # modules, curve tables, renderer set
niagara(action="add_module", emitterName=..., moduleType=..., stage=...)
niagara(action="set_module_property", emitterName=..., moduleName=..., property=..., value=...)
niagara(action="set_curve", emitterName=..., curveName=..., points=...)
niagara(action="compile", systemPath=...)
niagara(action="validate", systemPath=...)                  # dry-run safety net
niagara(action="save", systemPath=...)
```

## Module stack authoring

When you need a particular behavior — fire-and-forget, looping ambient, GPU sprite emitter, mesh emitter — choose the **module type first**, then place it at the right stage:

- **Emitter Update** group: spawn rate, emitter life cycle, looping, time-stepping
- **Particle Spawn** group: initial velocity, lifetime, size, color, mesh
- **Particle Update** group: forces, drag, color over life, size over life, sub-image animation
- **Render** group: Sprite / Mesh / Ribbon / GPU sprites

`add_module` takes a module **class path** (e.g. `NiagaraModule_ApplyForce`, custom project modules). For custom modules, register the module class in C++ first; refresh u-niagara reflection with `niagara(action="refresh_modules")` after registering.

## Renderer settings

Renderer changes — sprite alignment, sort mode, bounds calculation, GPU simulation toggle — go through `set_renderer_property`. Two sharp edges:

- **Bounds calculation** for GPU emitters is non-trivial; set explicit `Fixed Bounds` if the system is meant to live in a known region (UI, boss arena) and you cannot afford to over-allocate.
- **Sort mode** matters for transparency-heavy effects; pick by render order, not by which "looks nicer" in isolation.

## Driving Niagara at runtime

From BP / C++:

```cpp
UNiagaraComponent* NC = ...;
NC->SetAsset(NiagaraSystem);
NC->SetVariableFloat(FName("User.SpawnRate"), 100.f);
NC->SetVariableVec3(FName("User.EmitDirection"), Dir);
NC->Activate(true);
```

Set any variable exposed via `User.` namespace — those are the documented gameplay-side hooks. Don't poke internal emitter module parameters from C++; they will break on engine upgrades.

## Epic Toolset fallback

If on **UE 5.8+ with Epic toolset plugins enabled**, `epic(action="status")` may surface additional niagara operations. Prefer those when available; they go through Epic's official tool registry and tend to handle edge cases (preview meshes, transient assets) better than the native path.

See `ue-mcp-epic-routing` for the full native-vs-epic decision.

## Common pitfalls

- Module **spawn instant** = -1 will not behave like "infinite" in some 5.x versions — check engine version
- **GPU sim systems** cannot mix with CPU sim child emitters in the same system without explicit sync
- `Emitter.RecallFailed` errors usually mean a module parameter is bound to a missing curve / DI; read the warning list before mutating

## Cross-reference

- For Niagara **system / data** concepts (modules vs renderers vs DIs, design-time): pair with `skills/unreal/dcc-unreal-niagara/` and `skills/unreal/ue-niagara-authoring/`
- For Niagara runtime **Material + HLSL** work: pair with `skills/unreal/dcc-unreal-materials/` and `skills/unreal/hlsl-shader/`
- For Niagara JSON / preset pipelines: pair with `skills/unreal/niagara-json-generator/`
