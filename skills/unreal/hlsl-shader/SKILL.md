---
name: hlsl-shader
description: "Write, learn, and debug HLSL shader code (写着色器/材质节点/粒子/后期处理的 HLSL 代码): plain HLSL (types, built-ins, semantics, SM4/5/6), and Unreal Engine shaders — Material Custom node HLSL, full .usf/.ush files (GlobalShader/MaterialShader), Niagara GPU-simulation Custom HLSL, post-process / render-pass materials. Use whenever the user writes, reviews, fixes, or asks about shader code: HLSL, shader, 着色器, 材质节点, Custom node, pixel/vertex/compute shader, SV_Position/SV_Target, float4/half, .usf/.ush, MaterialTemplate, Niagara Custom HLSL, GPU particles, 粒子, SceneTexture, PostProcessInput, 后期处理, render target, or 'why does my shader not compile / show black / look wrong' (为什么变黑/报错). UE4 (SM5) + UE5 (SM5/SM6, Lumen/Nanite/VSM). DO NOT use for C++ side of materials or Niagara (spawning systems, setting parameters from code) — use ue-materials-rendering or ue-niagara-effects instead."
metadata:
  version: 1.0.0
---

# HLSL Shader Authoring

You write, teach, and debug HLSL shader code. Three contexts, handled very differently — **classify first, then read the matching reference**. Always lead with working code; explain "why" only when asked or when a subtle trap demands it.

## Step 1 — Classify the request

Ask one question: **where will this shader code run?**

| Signal in the prompt | Path | Read this reference |
|---|---|---|
| "Custom node", material graph, UV, `Parameters.Time`, a node-based effect the user wants in code | **A. UE Material Custom node** | `references/ue-material-shader.md` |
| `.usf` / `.ush` file, GlobalShader, MaterialShader, `IMPLEMENT_*_SHADER`, full shader class, plugin shader, custom render pass | **B. Full USF/USH file** | `references/ue-usf-ush-files.md` |
| Niagara, GPU particles, GPU simulation, particle attribute, `SimulationToParticle`, StageBool, "per-particle on GPU" | **C. Niagara Custom HLSL** | `references/ue-niagara-hlsl.md` |
| Post-process, SceneTexture, `PostProcessInput0`, bloom/tonemap/outline as full-screen effect, custom render pass output | **D. Post-process / render pass** | `references/ue-post-process.md` |
| None of the above — raw HLSL, learning, a snippet, syntax, "how do I … in HLSL", a compile error on plain shader code | **E. Plain HLSL** | `references/hlsl-core.md` |

If uncertain between A and D (both live in a Material), the deciding factor is **Material Domain**: Surface → A; Post Process → D.

**Read the chosen reference before writing code.** Each path has different available inputs, different restrictions, and different "invisible" injected code. Writing path-A code into a path-B file is the #1 cause of "works in Custom node, breaks as a file".

## Step 2 — Apply universal rules (all paths)

These traps recur on every path. Check the user's code against them before answering:

1. **Precision** — UE5 defaults to half (`half`/`float16`) in many material paths for performance. A `half` accidentally fed into a world-position calc silently loses precision. When in doubt in UE materials, use `float` for positions/UVs that need range; `half` is fine for colors.
2. **Matrix layout** — HLSL defaults to **column-major**, but UE's HLSL is compiled **row-major** (`mul(M, v)` = vector treated as row). `mul(v, M)` vs `mul(M, v)` flips meaning. Match the surrounding UE code's convention.
3. **`mul` argument order** — `mul(M, v)` transforms a column vector; `mul(v, M)` transforms a row vector. Wrong order = wrong transform or compile error on matrix dims.
4. **Semantics** — every shader stage input/output needs a semantic (`SV_Position`, `SV_Target`, `TEXCOORD0`…). Missing one = cryptic compile error. Custom node inputs don't need them (UE injects), full-file shaders do.
5. **Branching** — prefer `lerp`/`step` over `if` on divergent data; dynamic branches in pixel shaders can be fine on SM6 but costly. Avoid `if` inside Niagara GPU per-particle hot paths unless guarded.
6. **Black output** — almost always: sampling a texture that wasn't bound, dividing by zero, or a NaN from `normalize(zero)`. Check `length()`/`normalize()` inputs and unbound samplers first.

Full detail per path is in the references.

## Step 3 — UE version check

Before writing UE shader code, confirm the version if it affects the answer:
- **SM5** = both UE4 and UE5 (DX11-style, the common case).
- **SM6** = UE5 only, requires DXC, enables `WaveMath`/subgroup ops, half-precision intrinsics. Lumen and some UE5 features assume SM6.
- **Nanite** (UE5) restricts materials: no World Position Offset beyond a budget, limited shader complexity, no arbitrary Custom node freedom — flag this when the user targets Nanite-enabled meshes.

If the user doesn't specify, assume SM5 (works everywhere) unless they mention Lumen, Nanite, or SM6.

## Step 4 — How to answer

- **Code first.** Give a complete, runnable snippet for the chosen path with brief inline comments. No preamble.
- **Fix requests:** corrected code first, then one line stating the cause. Don't lecture.
- **"Why" questions:** the references end with a **Why** section per topic — draw on it to explain, but don't dump it unprompted.
- **Learning questions:** give a minimal runnable example + the one rule the user should remember. Offer to go deeper only if asked.

## Boundary — hand off, don't duplicate

This skill writes **shader code**. It does NOT do the C++ that drives materials/Niagara:

- "How do I set this material's scalar parameter from C++ / at runtime" → hand to **`ue-materials-rendering`**.
- "How do I spawn this Niagara system from code / bind a data interface" → hand to **`ue-niagara-effects`**.
- The seam: if the answer is *inside a `.usf`/`.ush`/Custom-node/HLSL box*, it's here. If it's *C++ calling the engine*, it's there.

## Locating UE shader source (when the user needs to read engine shaders)

UE ships readable shader source under `<UE>/Engine/Shaders/`. Key files:
- `Private/MaterialTemplate.ush` — the template every material compiles into; defines available inputs/outputs for Custom nodes.
- `Private/PostProcessMaterialShaders.usf` — post-process entry points and `PostProcessInput`/`SceneTexture` wiring.
- `Private/BasePassPixelShader.usf`, `Common.ush`, `Common.usf` — shared types and helpers.

Tell the user to grep these rather than guessing available symbols. They change between UE4 and UE5 — always read the version matching their engine.

## Quick lookup table (copy-paste starters)

When the user wants a fast start, the references contain ready templates: a UV-twist Custom node (A), a minimal GlobalShader `.ush/.usf` pair (B), a velocity-to-color Niagara snippet (C), and an outline/tonemap post-process (D). Point the user at the matching reference's template section instead of re-deriving.

## Step 5 — Use the recipe library for ready-made effects

For common effects (water, dissolve, fresnel, outlines, scanlines, curl-noise particles, ACES tonemap, procedural noise, triplanar, parallax…), read **`references/recipes.md`** before writing from scratch. It's organized by path (A/D/C/E) with inputs/outputs and a "why" per recipe. If the user describes an effect, scan recipes.md for a close match and adapt.

## Step 6 — Diagnose compile errors and visual bugs here

When the user pastes a compiler error or describes a broken result (black output, wrong transform, pink material, NaN, perf tank), open **`references/troubleshooting.md`**. It has lookup tables mapping raw error strings and visual symptoms → cause → fix, grouped by path. For raw compile errors, search the "Compile errors" table first; the first error line is usually the real cause.

## Step 7 — Use visual guides for teaching and pipeline confusion

When the user is learning, or confused about *where their code runs* (vertex vs pixel vs post-process vs compute, `SV_Position` semantics, row vs column major, dispatch indices), read **`references/visual-guides.md`**. It has ASCII diagrams of the pipeline, a material-node↔HLSL translation table, and the performance principles (warp divergence, coalesced access, register pressure, half/float, occupancy) that explain why one correct shader is faster than another. Reach for it when "why" questions go deep or when a shader is correct-but-slow.

## Step 8 — Topic-driven references (cross-path, read on demand)

These four references apply across multiple paths. Read the matching one when the user's question is about that topic, regardless of which path they're in:

- **`references/space-transforms.md`** — coordinate-space conversions (tangent↔world↔view↔clip↔screen) and **reconstructing world position from scene depth** (post-process, ray picking, water intersection, soft collision). Read when the user asks about spaces, transforms, TBN, reversed-Z, or "get world position from depth".
- **`references/sdf.md`** — signed distance fields: primitives, CSG ops (union/intersect/subtract), smooth blends, domain manipulation (repeat/mirror/rotate), AA fill with `fwidth`, ray marching, SDF text. Read when the user wants procedural shapes, soft outlines, antialiased edges, shape combining, or ray-marched implicit surfaces.
- **`references/blend-modes.md`** — Opaque/Masked/Translucent/Additive/AlphaComposite/Modulate: what each means for shader output, sorting, premultiplied alpha and the dark-halo bug, custom RT blend factors, the opaque>masked>translucent performance ordering. Read when the user asks about transparency, opacity, cutouts, glow compositing, or UI edge artifacts.
- **`references/mobile-and-fog.md`** — mobile/Metal/ES3 limits (sampler count, half-precision importance, instruction caps, feature gating) and volumetric fog interaction (what the engine's froxel fog does, why materials can't draw fog directly, how to fake localized fog via particles/decal/post-process). Read when the user targets iOS/Android, hits mobile compile failures, or asks about fog/mist/god-rays.
