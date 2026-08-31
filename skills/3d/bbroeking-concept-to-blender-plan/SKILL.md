---
name: concept-to-blender-plan
description: "Convert a concept-art image into a structured Blender build plan — a markdown document that decomposes the character into proportions, palette, parts list (each part with primitive type, world position, dimensions, material, shading mode), animation contract, and a concept↔model alignment check. The plan goes straight into a Blender MCP authoring session: each part becomes one `add_box`/`add_sphere`/`add_cone`/`add_cylinder`/`add_metaball_blob` call with values lifted from the plan. Forces methodical analysis instead of eyeballing coordinates from a 2D image (the trap that produced multiple wrong-proportion rebuilds of Eldra). Pairs with `low-poly-character-modeling` (the cookbook of part recipes), `blender-stylized-game-assets` (the Python/MCP pipeline), and `art-style-blender-research` (the research router). Use this skill BEFORE writing any Blender code for a new character/enemy/prop, or when an existing model has drifted from its concept and you need to re-anchor."
metadata:
  tags: ["blender", "low-poly", "concept-art", "planning", "build-plan", "stylized", "game-art"]
  version: "1.0.0"
---

# Concept Art → Blender Build Plan

Take a concept-art image and produce a build plan that can be executed by Blender MCP without further interpretation. The plan IS the model — once it's complete, building it in Blender is a mechanical translation step.

## Why this skill exists

Eyeballing coordinates from a 2D concept image is error-prone. The Eldra rebuild burned through five iterations because each pass missed elements, got proportions wrong, mixed shading modes, or forgot to lock the palette. **The fix is forcing a structured analysis before any code is written.**

This skill produces a build plan that:
- Locks proportions FIRST (heightM, head fraction, key joint positions)
- Locks the palette FIRST (5-8 hex colors with role labels)
- Names every visible element from the concept (no missed elements)
- Decides primitive + position + dimensions + material + shading mode PER PART
- Defines the animation contract upfront (rig groups, hand-prop, lockArm)
- Includes an alignment check against the concept image

When you're done with the plan, building the model is **3-step**: open Blender via MCP → execute the plan as a series of helper calls → render and verify.

## When to use this skill

- Starting a new character, enemy, or distinct prop from concept art
- An existing model has drifted from its concept and you need to re-anchor
- You're about to write a Blender authoring script and want to do it right the first time

## When NOT to use

- Procedural set-dressing (rocks, fences, trees scattered by code) — primitives + randomness, no plan needed
- Pure environment kits (cottage, fence) where the concept is a kit, not a single character
- Tweaking a model that already has a build plan — edit the plan, don't redo the analysis

## How to invoke

User asks "build a plan for <character>" or "extract Eldra's concept into a build plan." If you have access to the concept image, read it via the Read tool (vision-capable image). If only a textual description exists, ask the user to point to an image file or paste a description.

Then walk through the **6 sections** below in order. Save the output to `docs/build-plans/<character_id>.md` (project-relative). Once written, the file is the canonical reference for building / iterating on the model.

## The build plan template

Produce a markdown document with these six sections, IN THIS ORDER:

### 1. Overall proportions

A short paragraph + a table of measurements. The table columns: name, value, notes.

```
heightM            — total height in meters (e.g. 1.55 for chibi adult)
head_fraction      — head height ÷ total height (chibi: 0.28-0.33; hero: 0.13-0.16)
shoulder_z         — height of shoulder joint above ground (m)
hip_z              — height of hip joint above ground (m)
knee_z             — height of knee joint above ground (m)
shoulder_width     — lateral distance between shoulder pivots (m)
torso_width        — front-back depth of torso (m)
limb_to_body_ratio — limb length ÷ body length (stubby chibi: 0.4-0.5; hero: 1.0+)
primary_shape      — circle / square / triangle (per `low-poly-character-modeling`)
secondary_shape    — circle / square / triangle (counter-note)
```

The numbers come from STUDYING the concept image: where do the joints sit relative to the total height? Use the head as a unit ("body is 3.5 heads tall" is a useful frame).

### 2. Palette

5-8 hex colors with role labels. ONE saturation peak (the most-saturated color) on the character-defining prop. Everything else ≤60% saturation.

Format as a table:

| role | hex | role description | use |
|---|---|---|---|
| skin | #f0c8a8 | peachy warm | face, hands, feet |
| hair | #f4f0e8 | off-white | hair, beard, eyebrows |
| ... | ... | ... | ... |
| saturation_peak | #ffd060 | warm gold + emissive | lantern flame |

Test: imagine the character at gameplay distance. Which one color does the eye lock onto? That's the saturation peak — it should land on the character-defining prop.

### 3. Silhouette mark + character-defining prop

Two-three sentences: what makes this character RECOGNIZABLE at 64×64 black-on-white?

- Primary silhouette feature (e.g., "voluminous windswept hair tufts going up-and-back")
- Character-defining prop (e.g., "wooden staff with two lanterns rising past her shoulder")
- Why these specifically (e.g., "the lantern is what tells you she's the lampwright at first glance — without it she's just an old man")

### 4. Parts list — organized by parent rig group

This is the bulk of the plan. List EVERY visible element. Group by which rig empty it'll be parented to:

```
Body (parent: rig group `Body`)
- Tunic_Body
  primitive    : box
  world_pos    : (0, 0, 0.78)
  dims         : (0.34, 0.28, 0.36)         # width, depth, height
  material     : tunic
  shading      : smooth
  notes        : cream undershirt, ~0.04 above the vest at the neckline

- Vest_Body
  primitive    : box
  world_pos    : (0, 0, 0.72)
  dims         : (0.38, 0.32, 0.34)
  material     : vest
  shading      : smooth
  notes        : ochre layer wrapped over tunic, slightly wider

[…]

Head (parent: rig group `Head`)
- Head_Mesh
  primitive    : sphere
  world_pos    : (0, 0, 1.12)
  radius       : 0.16
  scale        : (1.05, 1.0, 0.95)            # wider than tall
  material     : skin
  shading      : smooth
  notes        : —

- Beard
  primitive    : cone-cluster (per /low-poly beard recipe)
  parts        : Chin_Pad + 5 strands + 2 fork-tips + 2 mustache cones
  see          : low-poly-character-modeling.SKILL.md § Beard
  material     : hair
  shading      : flat
  notes        : substantial dwarf-wizard beard with forked tip

[…]
```

Constraints when filling out each entry:

- **Primitive**: pick the simplest one that captures the silhouette. Default order of preference: box → cylinder → sphere → cone → metaball. Use the `low-poly-character-modeling` recipes for each part type — don't default to "sphere" just because it's round.
- **World position**: AUTHORING-FRAME coordinates. The script's wrapper (per gj26 `feedback_glb_orientation_two_tier_root.md`) handles the +X→-Y rotation for engine convention.
- **Dimensions**: meters. Reference the proportions table — torso width should equal `shoulder_width` ± a small margin.
- **Material**: name from the palette (Section 2). Don't introduce new colors here.
- **Shading**: `flat` / `smooth` / `hybrid`. Decide per part — don't leave it accidental.
- **Notes**: one line max. Use it to flag non-obvious decisions (e.g., "scarf overlaps neck cylinder by 0.02u to hide the seam").

For each rig group, list parts in the order they should be created — typically from the largest / most-supporting (anchor) to the smallest / decorative.

### 5. Animation contract

The rig structure the engine expects, plus per-character overrides.

```
rig_groups        : Body / Head / Arm_L / Arm_R / Leg_L / Leg_R
optional_joints   : Knee_L / Knee_R / Elbow_L / Elbow_R   # if including secondary swing
hand_props
  - Arm_R         : Staff (with crook + 2 lanterns parented under it)
  - Arm_L         : —
locked_arms       : R           # arm holding the staff doesn't swing
cadence_mul       : 0.7         # slow elder
lean_mul          : 1.6         # stooped forward lean
```

This locks how the engine will drive the rig at runtime. Reference: `src/anim/knight.js` for the animator that consumes this contract.

### 6. Concept ↔ model alignment check

A checklist of major silhouette elements from the concept, with a tick for whether the parts-list captures each:

```
[x] Voluminous windswept hair tufts up-and-back        — 4 angular cones (Hair_Tuft_top, _L, _R, _back_L, _back_R)
[x] Substantial chin beard with forked tip             — cone-cluster (Beard)
[x] Layered cream tunic + ochre vest                   — Tunic_Body + Vest_Body
[x] Patterned teal scarf                               — Scarf_Front + Scarf_Tail (with embroidery stripe via material)
[x] Staff with 2 hanging lanterns                      — Staff_Pole_lo/mid/hi + Crook_a/b/c + Lantern_1/2 (each = body+cap+flame+base+hang)
[x] Backpack with herbs poking out                     — Backpack + 3 Backpack_Herb_a/b/c
[x] Olive trousers + bare feet                         — Trousers_L/R + Foot_L/R
[x] Belt with pouch                                    — Belt + Pouch_R
[ ] Sandal-strap detail                                — DEFERRED (small detail, low gameplay-distance read)
```

Three categories:
- `[x]` — captured in the parts list
- `[ ]` followed by DEFERRED — intentionally skipped (state why)
- `[ ]` followed by MISSING — gap to fix before building

If anything is MISSING, go back to Section 4 and add the part. The plan is not done until every silhouette element is either captured or explicitly deferred.

## Translating the plan into Blender MCP code

Once the plan is written, the build script is mechanical. For each part in Section 4:

```python
# Tunic_Body — copied straight from the plan
add_box('Tunic_Body', (0, 0, 0.78), (0.34, 0.28, 0.36), MAT_TUNIC, body_emp,
        bevel_width=0.020)
```

The helper signatures match the plan's per-part schema 1:1. If the plan calls for a recipe (e.g. "cone-cluster (per /low-poly beard recipe)"), look up that section in `low-poly-character-modeling` and copy the parameter pattern.

For new helpers needed (e.g., a multi-part composite that doesn't yet have a single function), define the helper FIRST in the script, then use it. Don't inline the same primitive cluster across multiple parts — extract a helper.

## What this skill does NOT do

- **Build the model.** That's `blender-stylized-game-assets` driving the MCP. This skill produces the plan; that skill executes it.
- **Pick the art style.** That's `stylized-art-direction`. By the time you reach this skill, the project's chunky-cozy / RuneScape-flavor / Wind-Waker-flavor / etc. is already locked.
- **Source the concept art.** Concept art is the input. If it doesn't exist yet, generate it first per `docs/concept-art-prompts-master.md` (gj26-specific) or via image-gen tools.
- **Improve a model that already matches its plan but looks wrong.** That's `low-poly-character-modeling` — the part-level cookbook of "this part looks dumb because…" diagnoses.

## Output convention

Save the plan to `docs/build-plans/<character_id>.md` in the active project. Include:

- Date the plan was authored (in the YAML frontmatter, e.g. `date: 2026-05-06`)
- Concept-art image path (`concept_art: docs/concept-art/<id>.png`)
- Linked plans for related characters if shared palette / shared rig template (`shared_with: [hod, quill]`)
- Version number — bump when you re-author after a major redesign

The plan is then a CHECKED-IN ARTIFACT that future build / iterate sessions reference. Updating the model = updating the plan first, then re-running the build.

## Failure modes specific to plan authoring

These are the patterns that produce bad plans (which produce bad models):

1. **"Just a parts list, no proportions / palette."** Skip Sections 1-2 and you're back to eyeballing. Always lock proportions and palette FIRST.
2. **"Proportions in vague language."** "Tall and skinny" is not a plan — give a heightM, a head_fraction, joint heights. Numbers force you to commit.
3. **"Mixed-shading-mode parts list."** Half the parts list says `shading: smooth` and the other half says `shading: flat` with no design intent behind the difference. Decide on a HOUSE STYLE for the character (e.g. "smooth body, flat hair") and apply consistently.
4. **"Missing alignment check."** Section 6 is the only thing that catches "I forgot the lanterns" before code gets written. Don't skip it.
5. **"Plan doesn't reference the rig contract."** A model that doesn't fit the engine's animator is broken on arrival. Section 5 prevents this.
6. **"Plan has 30 parts and no architecture."** A human-readable plan tops out around 25 parts. If you have more, extract repeated clusters (e.g. "lantern" with 5 sub-parts) into named composite recipes. Reference, don't list.

## Pairs with

- **`low-poly-character-modeling`** — the cookbook of part recipes. The plan references this for each part's primitive choice.
- **`blender-stylized-game-assets`** — the Python/MCP pipeline. Translates the plan into actual Blender code.
- **`art-style-blender-research`** — broader research router. Reach for it if the plan is stuck on a style/aesthetic decision rather than a part-level decision.

## Concrete example (header — full plan in `docs/build-plans/eldra.md`)

```yaml
---
character: eldra
character_role: village lampwright
date: 2026-05-06
concept_art: docs/concept-art/npc-eldra-lampwright.png
heightM: 1.55
primary_shape: circle
secondary_shape: triangle
saturation_peak: lantern_flame
rig: 6-empty biped, optional knees + elbows + feet
---

## 1. Overall proportions
[…]

## 2. Palette
[…]

## 3. Silhouette mark
[…]

## 4. Parts list
[…]

## 5. Animation contract
[…]

## 6. Concept ↔ model alignment check
[…]
```
