---
name: ue-material-authoring
description: "Use this skill when authoring materials IN THE UNREAL MATERIAL EDITOR: material graph (nodes), PBR inputs (Base Color, Roughness, Metallic, Specular, Normal, Emissive, AO, Opacity), Shading Models (Default Lit, Subsurface, Clear Coat, Thin Translucent, Hair, Eye, Cloth, Unlit), Blend Mode (Opaque, Masked, Translucent, Additive, Modulate, AlphaComposite), Material Domain (Surface, Post Process, UI, Decal, Volume), Material Functions, Material Layers, static Material Instances, parameter exposure, tessellation, world position offset, two-sided. Covers building the graph, choosing shading/blend/domain, organizing reusable logic, material performance, and Nanite material constraints. For runtime material control (Dynamic Material Instances, Parameter Collections from C++, render targets), see ue-materials-rendering. For inline HLSL in a Custom node, see hlsl-shader. For particle materials, see ue-niagara-authoring."
metadata:
  version: 1.0.0
---

# UE Material Authoring

You are an expert in authoring Unreal Engine materials in the **Material Editor**. You provide accurate guidance on the material graph, PBR inputs, Shading Models, Blend Modes, Material Domains, Material Functions/Layers, static Material Instances, parameter exposure, and material performance. This skill covers building the material asset itself — not driving it from C++ at runtime (see `ue-materials-rendering`), not writing HLSL inside a Custom node (see `hlsl-shader`), not particle-system authoring (see `ue-niagara-authoring`).

## Context Check

Read `.agents/ue-project-context.md` before proceeding. Confirm:

- **Engine version** — UE5 unlocks Material Layers, `From Material Expression` shading model, thin-translucent blend, advanced material functions; UE4 has a smaller feature surface. State the gap when it changes the answer.
- **Rendering path** — Deferred (desktop default) vs Forward (mobile/VR): Forward limits dynamic lights, restricts some material features, and changes how translucency works. Forward shaders are less feature-rich.
- **Nanite / Lumen status** — Nanite constrains material complexity (translucent, Pixel Depth Offset, heavy WPO); Lumen affects emissive/GI interaction. Flag material choices that break these.
- **Target platforms** — Mobile has hard sampler-count caps (5–8 on ES3.1), strict instruction budgets, and missing features. A material fine on PC can fail or fall back on mobile.

## Information Gathering

Before advising on a material, clarify:

1. **Surface type** — what physical material? (metal, dielectric, skin, glass, cloth, foliage, glowing, stylized) Drives PBR values and Shading Model.
2. **Blend Mode** — opaque solid, masked cutout, translucent see-through, additive glow, modulate tint?
3. **Material Domain** — surface, post-process, UI, decal, volume?
4. **Reuse** — one-off, or a family of variants? (Material Instance / Material Function / Material Layer)
5. **Runtime driving** — will gameplay set parameters? (expose as parameters; the C++ side is `ue-materials-rendering`)
6. **Performance budget** — target platform + shader-complexity tolerance.

---

## Material Structure (UE Concept Map)

```
 UMaterial (asset — the authored material graph)
   │
   ├── Material Inputs (the result pins on the MAIN node)
   │     ├── PBR: Base Color, Metallic, Specular, Roughness,
   │     │         Normal, Emissive Color, Ambient Occlusion, Tangent
   │     ├── Opacity / Opacity Mask / Refraction
   │     ├── Pixel Depth Offset, World Position Offset (WPO)
   │     ├── Subsurface / Tessellation / etc. (Shading-Model dependent)
   │     └── (Domain-specific: e.g. PostProcessInput for post-process)
   │
   ├── Material Properties (Details panel — the BIG decision panel)
   │     ├── Material Domain      (Surface / PostProcess / UI / Decal / Volume)
   │     ├── Blend Mode           (Opaque / Masked / Translucent / Additive / Modulate / AlphaComposite)
   │     ├── Shading Model        (Default Lit / Subsurface / ClearCoat / Thin Translucent / Hair / Eye / Cloth / FromMatExpr)
   │     ├── Two-Sided / Dithered / Tessellation
   │     ├── Usage (Nanite, Skeletal, Particle, UI, ...)
   │     └── Translucency settings (Lighting Mode, sort priority)
   │
   └── Material Graph (nodes wired INTO the inputs above)
         ├── Sample nodes (Texture, Particle, Time, Camera, Fresnel, ...)
         ├── Math nodes (Add/Mul/Lerp/Pow/Dot/Cross/Saturate/Smoothstep)
         ├── Parameter nodes (Scalar/Vector/Texture/Static Switch/Font) ← exposed to instances/C++
         ├── Function Call nodes (invoke a Material Function asset)
         └── Custom node (HLSL → see hlsl-shader)

 VARIANTS (authoring reuse):
   UMaterialInstance (Constant / Dynamic) → override parent's parameters
   UMaterialFunction (asset) → reusable node sub-graph
   UMaterialLayersFunction (UE5) → layered material composition
```

**Key model**: a material is a **node graph that fills result pins**. The Main material node's inputs are the output; everything else computes what feeds them. The Details panel (Domain/Blend/Shading) decides *what those inputs mean* and *how the GPU runs the result*. Getting Domain/Blend/Shading right first prevents "my graph is correct but the material looks wrong" bugs.

---

## The Three Big Settings (decide FIRST, before building the graph)

The combination of **Material Domain × Blend Mode × Shading Model** defines what the material IS. Setting these after authoring often invalidates the graph (inputs change meaning). Decide first.

### Material Domain
| Domain | Use | Reads/writes |
|---|---|---|
| **Surface** | Meshes in the world (default) | PBR inputs |
| **Deferred Decal** | Projected decals on surfaces | DBufer / decal inputs |
| **Post Process** | Fullscreen post-process pass | PostProcessInput, SceneTexture |
| **User Interface** | UMG/Slate UI | UI-specific, unlit |
| **Volume** | Volumetric (Heterogeneous Volumes, UE5) | Density, albedo, emission |
| **Light Function** | Project a texture from a light | Light function input |

### Blend Mode
| Mode | Use | Sorts? | Notes |
|---|---|---|---|
| **Opaque** | Default solids | No (depth-tested, early-z) | Cheapest |
| **Masked** | Cutouts (foliage, fence) | No | Opacity Mask 0/1, hard edge |
| **Translucent** | Glass, water, UI, particles | Yes | Opacity 0..1, true alpha blend |
| **Additive** | Glow, sparks, fire, lasers | Yes | Black=invisible; adds to bg |
| **Modulate** | Tints, projector mattes | Yes | Multiplies against bg |
| **AlphaComposite** | Premultiplied UI | Yes | Correct UI compositing |

Deep rules (sorting, premultiplied alpha, masked vs translucent perf): see `references/instances-domains-layers.md`.

### Shading Model
| Model | Use | Extra inputs it activates |
|---|---|---|
| **Unlit** | Emissive-only (glow, UI) | Emissive Color |
| **Default Lit** | Standard PBR | BaseColor/Metallic/Specular/Roughness/Normal/AO/Emissive |
| **Subsurface** | Skin, wax, marble | Subsurface Color, Opacity |
| **Subsurface Profile** | Cinematic skin (profile asset) | Profile asset + scattering |
| **Clear Coat** | Car paint, lacquer over base | ClearCoat, ClearCoatRoughness |
| **Thin Translucent** (UE5) | Thin glass, soap bubble | Transmittance |
| **Hair** | Hair strands | (UE5 Groom system) |
| **Eye** | Realistic eye (cornea/reflection) | (UE5) |
| **Cloth** | Fabric (sheen + fuzz) | Cloth, FuzzColor, RoughnessTint |
| **From Material Expression** (UE5) | Custom per-material shading model | Your own via SetShadingModel |

PBR value guidance + per-model details: `references/pbr-and-shading-models.md`.

**Rule**: pick Shading Model from the physical material. Default Lit covers 80% of cases; reach for Subsurface on skin/wax, ClearCoat on lacquered surfaces, etc.

---

## PBR Inputs — what each pin means (summary)

| Input | Meaning | Typical source |
|---|---|---|
| **Base Color** | Albedo (non-metal) / specular color (metal) | Texture / Vector param |
| **Metallic** | 0=dielectric, 1=metal, blend | Constant 0/1 or mask texture |
| **Specular** | Dielectric reflectance at normal incidence (~0.5) | Usually leave default |
| **Roughness** | Microsurface roughness (smooth↔matte) | Texture (R channel common) |
| **Normal** | Surface micro-detail bump | Normal map (tangent space) |
| **Emissive Color** | Self-emission (glow; Lumen light source) | Texture / add for bloom |
| **Ambient Occlusion** | Cavity/contact occlusion | AO texture (R channel) |
| **Opacity** (Translucent) | See-through factor | Alpha / param |
| **Opacity Mask** (Masked) | Binary cutout | alpha clip |
| **Pixel Depth Offset** | Push pixel in depth (silhouette fix) | advanced |
| **World Position Offset** (WPO) | Move vertices (wind, morph) | expensive, breaks Nanite budget |

Values & common mistakes: `references/pbr-and-shading-models.md`.

---

## Parameters — exposing material values for instances / C++

A **Parameter node** (Scalar/Vector/Texture/Static Switch/Font) makes a value overridable. Plug it anywhere in the graph; it appears in Material Instances and is settable from C++ (`ue-materials-rendering`).

- **Scalar Parameter** — single float (Roughness, Intensity, Time multiplier).
- **Vector Parameter** — 4-channel (color, RGBA, or XYZW).
- **Texture Parameter** / **Texture Object Parameter** — swappable textures.
- **Static Switch Parameter** — compile-time branch (cheap; makes variants; bloats permutations).
- **Font Sample Parameter** — font for UI materials.
- **Channel Parameter** (UE5) — pick which channel of a texture to sample.

**Parameter hygiene**: name consistently (case-sensitive!), group them (Group property), use tooltips. Bad names are the #1 silent failure in C++/instance binding. Static switches multiply compiled shader permutations — use sparingly.

---

## Reuse: Material Functions, Instances, Layers (summary)

Three reuse mechanisms (full detail in `references/instances-domains-layers.md`):

| Mechanism | What it reuses | When |
|---|---|---|
| **Material Instance** (Constant/Dynamic) | A *parent material's graph*, overriding parameters only | A family of variants (10 rock materials from 1 master) |
| **Material Function** (asset) | A *node sub-graph* callable across materials | Shared math/logic (blend normals, triplanar, fresnel) |
| **Material Layers** (UE5) | *Composable layers* stacked into one material | Complex multi-layer surfaces (base + grime + damage + wet) |

---

## Common Mistakes and Anti-Patterns

| Mistake | Why it fails | Fix |
|---|---|---|
| Wrong Shading Model for the surface | Subsurface inputs ignored on Default Lit | Match Shading Model to physical material |
| Masked material with Translucent-style Opacity | Masked reads Opacity Mask (binary), not Opacity | Use the right input |
| Translucent with lit shading but slow | Lit translucency is expensive | Use Unlit where possible; limit sort/overlap |
| Parameter name case mismatch | C++/instance can't find it | Exact case-sensitive match |
| Static switch explosion | Each combo = a compiled shader | Minimize switch combos |
| Nanite + translucent | Reverts to non-Nanite (perf loss) | Split translucent to separate mesh |
| Heavy WPO on Nanite | Exceeds Nanite budget | Simplify WPO or disable Nanite on that mesh |
| Normal map not set as "Normal" compression | Wrong lighting | Set texture compression = Normal; sRGB off |
| Many overlapping translucent particles | Fill-rate death (overdraw) | Fewer, larger, higher-opacity sprites |

---

## Related Skills

- **`ue-materials-rendering`** — C++ runtime control: Dynamic Material Instances (set params per-frame), Material Parameter Collections, post-process volumes, render targets, decals, Nanite/Lumen runtime API. The C++ complement; this skill authors the asset, that one drives it.
- **`hlsl-shader`** (reference `ue-material-shader.md`) — inline HLSL in a Custom node: available symbols (`Parameters.*`), texture sampling, when to use Custom vs nodes. This skill tells you *whether* to drop a Custom node; that one tells you *what to write in it*.
- **`ue-niagara-authoring`** — particle material setup (Sprite/Ribbon/Mesh materials reading ParticleColor/UVs), shared parameter binding.
- **`ue-editor-tools`** — material asset editor extensions (custom material workflows, property customizations).
