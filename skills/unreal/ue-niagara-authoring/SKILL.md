---
name: ue-niagara-authoring
description: "Use this skill when authoring Niagara particle/VFX systems IN THE NIAGARA EDITOR: emitter setup, module stack (Spawn/Update/Initial/Event/Constraint modules), parameter namespaces (User/Particle/Emitter/Engine), renderer choice (Sprite/Ribbon/Mesh/Light/Decal), Simulation Stages, Data Interfaces in the editor (Grid3D/Neighbor/DistanceField/SkeletalMesh), GPU vs CPU simulation target, LOD/scalability, sim cache. Covers building emitter stacks, exposing User parameters, wiring renderers to particle attributes, and Niagara editor workflow. For C++ runtime control (spawning systems, setting parameters from code, pooling), see ue-niagara-effects. For GPU Custom HLSL sim script code, see hlsl-shader. For particle materials, see ue-materials-rendering."
metadata:
  version: 1.0.0
---

# UE Niagara Authoring

You are an expert in authoring Unreal Engine Niagara VFX systems in the **Niagara editor**. You provide accurate guidance on emitter properties, the module stack, parameter namespaces, renderer selection, Simulation Stages, Data Interfaces, and GPU-vs-CPU simulation trade-offs. This skill covers building the emitter stack itself — not driving it from C++ (see `ue-niagara-effects`), not the inline HLSL sim script (see `hlsl-shader`), not the particle material (see `ue-materials-rendering`).

## Context Check

Read `.agents/ue-project-context.md` before proceeding. Confirm:

- The `Niagara` plugin is enabled (`Plugins/FX/Niagara`).
- UE version: **UE5** unlocks full Simulation Stages, Grid3D, Neighbor, Mesh Renderer maturity, per-instance dynamic parameters; **UE4** has a smaller GPU-sim surface and several renderer features are absent or limited. State the version gap when it changes the answer.
- Sim target in scope: CPU, GPU, or both (mobile may force CPU).
- Whether **Niagara Mesh emitters** or **Skeletal Mesh DI** are needed (they pull mesh dependencies).

## Information Gathering

Before advising on an emitter stack, clarify:

1. **Effect shape** — what does it look like? (spray, burst, ribbon trail, mesh swarm, volume, decal)
2. **Sim target** — CPU (simple, flexible, deterministic) or GPU (massive counts, limited modules)? Mobile?
3. **Particle count budget** — orders of magnitude decide GPU vs CPU.
4. **Does it need cross-particle interaction?** (neighbor lookup, grid, collision between particles → GPU Stages + Neighbor/Grid3D)
5. **Does gameplay need to drive it?** → which `User.*` parameters to expose (then hand off to `ue-niagara-effects` for the C++ side).
6. **Renderer type** — what draws the particles? (sprite, ribbon, mesh, light, decal)

---

## System Structure (UE Concept Map)

```
 UNiagaraSystem  (asset — what you place/spawn in the world)
   │
   ├── Parameters (System-level User/Engine params, exposed to C++/Blueprint)
   │
   └── Emitters[]  (UNiagaraEmitter — one per "layer" of the effect)
         │
         ├── Emitter Properties (Sim Target, Lifecycle, Bounds, Determinism, LOD)
         │
         ├── Scripts  (each emitter has 3 script groups)
         │     ├── Emitter Spawn   (runs once when emitter starts)
         │     ├── Emitter Update  (runs every tick, emitter-scoped)
         │     ├── Particle Spawn  (runs once per particle at birth)
         │     └── Particle Update (runs every tick per particle)   ← most modules live here
         │
         ├── Module Stack  (ordered list of modules; top→bottom = execution order)
         │     Each module reads/writes the Parameter Map.
         │
         ├── Renderers[]  (how particles are DRAWN — sprite/ribbon/mesh/light/decal)
         │     A renderer reads particle attributes; no sim here.
         │
         └── Simulation Stages (UE5, GPU only) — split Particle Update into phases
               (e.g. "integrate", "neighbor solve", "render prep")

 DATA FLOW:  Modules WRITE particle attributes (Position, Color, Age…)
             ─────────►  Parameter Map (per-particle state)
             Renderers READ particle attributes ─────────► draw

 The Parameter Map is the spine: modules never talk to each other directly;
 they communicate by reading/writing named attributes on the map.
```

**Key insight**: a Niagara emitter is a **data pipeline**, not a script. Modules are ordered transforms on the parameter map; the renderer is a pure reader. Getting this model right prevents 90% of "my module doesn't take effect" bugs (cause: it's below the module that reads the attribute, or writes to the wrong namespace).

---

## The Parameter Namespace System (the most important concept)

Every value in Niagara lives in a **namespace**, which determines its scope and visibility:

| Namespace | Scope | Set by | Example |
|---|---|---|---|
| `User.*` | System, runtime-settable from C++/BP | Game code (the ONLY runtime-writable namespace) | `User.Color`, `User.SpawnRate` |
| `Engine.*` | System, engine-provided | Engine (time, delta time, view) | `Engine.Time`, `Engine.RealTime` |
| `Emitter.*` | One emitter, shared by all its particles | Emitter Spawn/Update modules | `Emitter.Age`, `Emitter.LoopCount` |
| `Particle.*` | Per-particle (the bulk of sim state) | Particle Spawn/Update modules | `Particle.Position`, `Particle.Velocity` |

**Rules:**
- To expose a parameter to gameplay code, create it in the **`User`** namespace in the System's parameter panel. Only `User.*` is settable at runtime. (C++ side: see `ue-niagara-effects`.)
- `Particle.*` attributes are the per-particle state modules read/write. A module that needs persistent per-particle data must write a `Particle.*` attribute; a local variable in a module does not survive the tick.
- `Emitter.*` is shared across all particles of one emitter — use for counts, ages, loop state.
- Module order matters: a module can only read a `Particle.*` value if a module **above** it wrote it (or it's a built-in like Position).

**Common bug**: "I set a parameter but C++ can't find it." → It's not in the `User` namespace, or it's on the Emitter not the System. See Common Mistakes.

---

## The Module Stack — how modules execute

Each script group (Emitter Spawn/Update, Particle Spawn/Update) holds an **ordered list of modules**. They execute **top to bottom** within the group, every tick.

```
 Particle Update (runs per particle, per tick):
   ┌─────────────────────────────────────┐
   │ 1. Gravity Force        (reads Mass, │
   │    writes Velocity)                  │
   │ 2. Drag                (writes       │  ← execution order
   │    Velocity)                          │
   │ 3. Curl Noise Force    (writes       │
   │    Velocity)                          │
   │ 4. Solve Velocity &    (reads        │
   │    Position  → writes Position)       │  ← Position committed here
   │ 5. Color by Speed      (reads        │
   │    Velocity → writes Color)           │  ← renderer sees this Color
   └─────────────────────────────────────┘
   Renderer (Sprite) reads Particle.Position + Particle.Color → draws
```

**Why order matters**: Force modules accumulate into `Velocity`; a single "Solve Velocity and Position" module commits Velocity into Position. If Solve is above a force, that force is ignored this frame. If two modules both write (not add) the same attribute, the lower one wins.

**Module categories** (full table in `references/emitter-and-modules.md`):
- **Spawn** modules (in Particle Spawn) — initialize birth state (Initial Position/Velocity/Size/Color, Spawn Burst/Rate).
- **Update** modules (in Particle Update) — per-tick behavior (Gravity, Drag, Curl Noise, Color, Lifetime, Forces).
- **Constraint** modules — post-solve corrections (e.g. keep above floor).
- **Event** modules — emit/consume gameplay events (collision, death, generation).
- **Renderer** — listed separately (see below), not in the update stack.

When the user needs a behavior, identify the module category, then the specific module. For behavior no built-in module covers, the **Custom / Scratch Pad / HLSL** module slots in (HLSL code itself → see `hlsl-shader`; *which module type to pick and where in the stack* is here).

---

## Renderer Selection — the draw decision

The Renderer is what turns particle attributes into visible pixels. An emitter can have **multiple renderers** (e.g. a sprite + a ribbon on the same particles). The renderer does **no simulation** — it only reads attributes.

| Renderer | Draws | Needs (key Particle attrs) | Use when |
|---|---|---|---|
| **Sprite Renderer** | Camera-facing quads | Position, (Size), (Color/UVs from material) | Default smoke/spark/dust |
| **Ribbon Renderer** | Connected strips following particles | Position, + ribbon-specific (age order, links) | Trails, laser beams, streaks |
| **Mesh Renderer** | Static/Skeletal mesh per particle | Position, (Rotation/Scale) | Debris, swarms, flocking, instanced props |
| **Light Renderer** | Actual dynamic lights (CPU/GPU) | Position, (Color/Radius/Intensity) | Particle that lights the scene |
| **Decal Renderer** | Projected decals | Position, (Orientation/Size) | Scorch marks, splats |
| **Camera Renderer** | Camera-facing helpers | Position | Debug, rare |
| **Noise Renderer** | Procedural noise field | (grid) | Wind/turbulence visualization |

**Decision flow**: Does it face the camera? → Sprite. Is it a connected trail? → Ribbon. Is it a real 3D object? → Mesh. Must it light the world? → Light. Stays on a surface? → Decal.

Full per-renderer config, required attributes, and UE4↔UE5 availability: `references/renderers.md`.

**Why renderer choice is a sim decision**: a Ribbon renderer needs particles ordered by age and a "linked" attribute set; a Mesh renderer needs Orientation/Scale attributes you must populate in the update stack. Choosing the renderer first, then building the module stack to feed it, avoids "renderer shows nothing/garbage" bugs.

---

## GPU vs CPU Simulation Target

Set per-emitter: **Emitter Properties → Sim Target = CPU | GPU | CPU and GPU**.

| | CPU Sim | GPU Sim |
|---|---|---|
| Particle count | Thousands | Hundreds of thousands+ |
| Module availability | All built-in modules | Subset (GPU-compatible only) |
| Data Interfaces | All | Subset (Grid3D, Neighbor, DistanceField, Mesh DI — GPU-enabled ones) |
| Simulation Stages | ❌ | ✅ (UE5) |
| Determinism | Easier (fixed seed) | Harder (vendor variance) |
| Mobile | ✅ | Limited/often disabled |
| Debugging | Easier (Scratch Pad, attributes visible) | Harder (GPU buffers) |

**Rule**: start on CPU while building/iterating (full module set, easy debug), switch to GPU when you need the count or GPU-only features (Stages, neighbor grids). Not all modules port — the editor warns about incompatible modules on switch; resolve each. Deep table + mobile/mobile-forcings in `references/performance-and-lod.md`.

---

## Simulation Stages (UE5, GPU only)

A Simulation Stage splits the Particle Update into **named phases**, each a separate GPU dispatch. This enables cross-particle work that a single per-particle update can't do:

- **Iteration stages** — run the whole particle set N times (relaxation, smoothing).
- **Data-instance stages** — iterate over a Data Interface (e.g. per Grid3D cell).
- **Neighbor stages** — read other particles via a neighbor grid (flocking, SPH-like fluids).

When the user asks "how do particles interact with each other / with a grid / find neighbors", they need Simulation Stages + a Neighbor/Grid3D Data Interface. Full mechanism + authoring: `references/data-interfaces-and-stages.md`.

This is the most advanced Niagara feature and the main UE4↔UE5 capability gap — UE4 lacks it.

---

## Data Interfaces in the Editor

A **Data Interface (DI)** is a module/parameter that lets the sim sample external data (mesh, curve, texture, grid, distance field, audio, spline…) or do cross-particle queries (neighbor grid). In the editor you **add** a DI as a User parameter, then **bind** it in modules that accept DI inputs.

Common DIs (editor usage — for the C++ binding side see `ue-niagara-effects`):
- **Skeletal Mesh / Static Mesh DI** — sample vertex/triangle data (spawn on mesh surface).
- **Curve DI** — sample a UCurve in-sim.
- **Array DI** — typed arrays (Vector/Float) the sim reads/writes.
- **Grid3D DI** — a 3D voxel grid for fields (velocity, density) — pairs with Simulation Stages.
- **Neighbor Grid3D DI** — spatial hashing for neighbor queries (flocking, fluids).
- **Distance Field DI** — sample the mesh/global distance field (collision, avoidance).
- **Scene Depth DI** — read the depth buffer (GPU collision against world).

**When to reach for a DI**: cross-particle or world-interaction needs. A pure per-particle effect (gravity, noise, simple sprites) needs none. See `references/data-interfaces-and-stages.md` for which DI to pick and how to wire it in the editor.

---

## LOD and Scalability

Niagara supports per-emitter **LOD** (Level of Detail) — different module stacks / settings at distance — and **scalability settings** (quality tiers per platform). Author these as **data in the editor**, not code.

- **LOD**: define distance thresholds; each LOD level has its own enabled modules/spawn rates. Far away → fewer modules, fewer particles.
- **Scalability**: in System properties, set quality tiers; mobile/low gets a cheaper stack.
- **Sim Cache**: (UE5) bake a simulation to a cache asset for fixed, repeatable, cheap-to-play effects (cutscenes, deterministic VFX).

Full budgeting, LOD setup, sim cache, and UE4↔UE5 differences: `references/performance-and-lod.md`.

---

## Common Mistakes and Anti-Patterns

| Mistake | Why it fails | Fix |
|---|---|---|
| Module below the attribute's writer | Reads stale/zero value | Move the reading module below the writer in the stack |
| Two modules both `write` (not add) Velocity | Lower one silently overwrites | Use `Add` for forces, reserve `Set` for initial values |
| Exposed param on Emitter, not System | C++ can't set it at runtime | Create `User.*` params at System level |
| GPU sim with CPU-only module | Module silently dropped → behavior missing | Resolve the editor's incompatible-module warnings; find a GPU replacement |
| Ribbon shows scattered quads, not a strip | Missing linked/age-order attributes | Configure Ribbon renderer binding + ensure age-ordering |
| Effect huge on GPU, invisible on mobile | Mobile forced CPU sim, incompatible modules | Build a CPU fallback stack or a low-quality LOD |
| Determinism off; replay flickers | Random module not seeded by particle index | Enable Determinism; use index-seeded RNG |
| Renderer reads attribute nothing writes | Particles draw at origin / black | Trace the attribute to the module that should write it |

---

## Related Skills

- **`ue-niagara-effects`** — C++ runtime control: spawning systems, setting `User.*` parameters from code, binding Data Interfaces, pooling (`ENCPoolMethod`), `OnSystemFinished` callbacks, scalability from code. The C++ complement to this skill.
- **`hlsl-shader`** (reference `ue-niagara-hlsl.md`) — the GPU Custom HLSL sim script: per-particle HLSL semantics, available symbols, what you can't do, when to use the Custom module. This skill tells you *when/where* to drop a Custom module; that one tells you *what to write in it*.
- **`ue-materials-rendering`** — particle materials (Sprite/Ribbon/Mesh material setup, dynamic material instances, per-particle color/UV from Niagara). The renderer draws; the material shades.
- **`ue-editor-tools`** — asset editor extensions, custom editor workflows (for tooling around Niagara authoring).
