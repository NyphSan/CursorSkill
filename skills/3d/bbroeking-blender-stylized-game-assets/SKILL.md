---
name: blender-stylized-game-assets
description: "Build chunky low-poly stylized 3D assets (toon RPG, storybook, RuneScape/WoW/PMD vibe) in Blender via the official Blender Lab MCP and export to glTF for three.js. Covers reusable Python patterns, shingle/roof math, materials with image textures, GLB export, animation rigging via named-group hierarchies, and the pitfalls that kept biting during cow + cottage builds."
metadata:
  tags: ["blender", "3d", "gltf", "threejs", "low-poly", "stylized", "game-art", "mcp"]
  version: "1.1.0"
---

# Blender Stylized Game Assets

Build chunky low-poly stylized 3D assets in Blender via `mcp__blender__execute_blender_code` and ship them as `.glb` to a three.js game.

Use this skill when:
- Modeling a character, prop, or building from primitives in Blender
- Exporting to GLB for three.js / WebGL
- Setting up named-group hierarchies for procedural animation
- Applying tileable AI-generated textures (Midjourney `--tile`) to UV-unwrapped meshes
- Iterating quickly: write Python → render preview → compare to reference → tweak

## Mental model

You're scripting Blender from the outside via MCP. Every asset is built fresh by a Python script — never edit the .blend by hand, because state is invisible to future runs. All geometry, materials, lighting, camera, and exports are reproducible from code.

The script runs in Blender's `bpy` context. Operators (`bpy.ops.*`) act on the active object and selection — set both explicitly between steps. The data API (`bpy.data.*`) is for fine control without side effects.

## Project layout

```
project/
├── models/
│   ├── cow.glb
│   ├── cottage.glb
│   └── textures/<asset>/<file>.png   # MJ-generated tileable PNGs
├── docs/
│   ├── ART_BIBLE.md                  # locked style + master prompt
│   └── art-refs/inspiration/         # reference images
└── src/scene/characters.js           # GLTFLoader + clone(true) per spawn
```

For three.js loading, embed textures in the GLB (`export_image_format='AUTO'`). Self-contained binaries stay simple at the cost of repeating textures per asset; switch to shared `.ktx2` only if total budget exceeds ~50MB.

## What works

### 1. Build from primitives, join into named groups, parent to a root empty

```python
def add_box(name, sx, sy, sz, loc, mat, rot=(0,0,0), bevel=0.04, bevel_seg=2):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.active_object; o.name = name
    o.scale = (sx, sy, sz); o.rotation_euler = rot
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    o.data.materials.clear(); o.data.materials.append(mat)
    if bevel > 0:
        m = o.modifiers.new("Bevel", 'BEVEL')
        m.width = bevel; m.segments = bevel_seg
        m.limit_method = 'ANGLE'; m.angle_limit = math.radians(30)
        bpy.ops.object.select_all(action='DESELECT')
        o.select_set(True); bpy.context.view_layer.objects.active = o
        for mod in list(o.modifiers): bpy.ops.object.modifier_apply(modifier=mod.name)
    bpy.ops.object.shade_smooth()
    return o
```

Then join related parts and set the pivot via the 3D cursor:

```python
def join_to(name, parts, pivot_world):
    bpy.ops.object.select_all(action='DESELECT')
    for p in parts: p.select_set(True)
    bpy.context.view_layer.objects.active = parts[0]
    bpy.ops.object.join()
    j = bpy.context.active_object; j.name = name
    bpy.context.scene.cursor.location = pivot_world
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.context.scene.cursor.location = (0, 0, 0)
    return j
```

This is the foundation for procedural rigging: `Body`, `Head`, `Leg_FL` etc. each get a sensible pivot (legs at the hip, head at neck-base, tail at the body junction). Parent them all to a root empty:

```python
bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
root = bpy.context.active_object; root.name = "AssetRoot"
for m in groups:
    bpy.ops.object.select_all(action='DESELECT')
    m.select_set(True); root.select_set(True)
    bpy.context.view_layer.objects.active = root
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
```

In three.js, `inst.traverse(o => { if (wanted.has(o.name)) parts[o.name] = o; })` then drive `parts.Leg_FL.rotation.z = sin(phase) * swing` per frame.

### 2. Triangular prism roofs via bmesh

Two tilted slabs are hard to align at the ridge. A single cube with the top vertices collapsed to the centerline gives a clean prism:

```python
def make_prism_roof(name, base_w, depth, ridge_h, loc, mat):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.active_object; o.name = name
    o.scale = (base_w, depth, ridge_h)
    bpy.ops.object.transform_apply(scale=True)
    bpy.ops.object.mode_set(mode='EDIT')
    bm = bmesh.from_edit_mesh(o.data)
    for v in bm.verts:
        if v.co.z > 0: v.co.x = 0   # collapse top to ridge
    bmesh.update_edit_mesh(o.data)
    bpy.ops.object.mode_set(mode='OBJECT')
    o.data.materials.clear(); o.data.materials.append(mat)
    return o
```

### 3. Roof shingles laying flat on the slope

The rotation sign matters. For Y-up Blender with the ridge running along the Y axis:

```python
pitch     = math.atan2(ridge_h, half_w)         # angle from horizontal
slope_len = math.sqrt(ridge_h**2 + half_w**2)
sx, sz    = (side * half_w) / slope_len, -ridge_h / slope_len  # along-slope direction
nx, nz    = math.sin(pitch) * side, math.cos(pitch)            # outward normal

# Tile dimensions: ALONG-slope × ALONG-ridge × thickness
tile_l, tile_d, tile_th = 0.30, 0.44, 0.025
row_step = tile_l * 0.55                          # 45% overlap

for r in range(n_rows):
    d_center = (r + 1) * row_step - tile_l / 2
    cx = sx * d_center + nx * (tile_th/2 + 0.01)
    cz = (roof_base_z + ridge_h) + sz * d_center + nz * (tile_th/2 + 0.01)
    col_offset = (tile_d / 2) if r % 2 == 1 else 0.0   # brick stagger
    for c in range(n_cols):
        y = -roof_depth/2 + c * tile_d + col_offset
        add_box(f"Tile_{side}_{r}_{c}", tile_l, tile_d, tile_th, (cx, y, cz),
                mat, rot=(0, math.radians(pitch_deg * side), 0))   # POSITIVE pitch * side
```

**Critical:** rotation is `+pitch_deg * side`, not `-pitch_deg * side`. Negative makes tiles tilt the wrong way and read as edge-on rectangles.

### 4. Image-texture material setup

Tileable diffuse only — no PBR specular/metallic for this style.

```python
def attach_texture(mat_name, image_path, uv_scale=0.5):
    m = bpy.data.materials.get(mat_name)
    nt = m.node_tree
    bsdf = nt.nodes.get("Principled BSDF")
    # Always strip prior tex/coord/mapping nodes first
    for n in list(nt.nodes):
        if n.type in {'TEX_IMAGE','TEX_COORD','MAPPING'}: nt.nodes.remove(n)
    img = bpy.data.images.get(os.path.basename(image_path)) \
          or bpy.data.images.load(image_path, check_existing=True)
    img.colorspace_settings.name = 'sRGB'
    n_coord = nt.nodes.new("ShaderNodeTexCoord")
    n_map   = nt.nodes.new("ShaderNodeMapping")
    n_tex   = nt.nodes.new("ShaderNodeTexImage")
    n_tex.image = img
    n_tex.extension = 'REPEAT'
    n_map.inputs["Scale"].default_value = (uv_scale, uv_scale, uv_scale)
    nt.links.new(n_coord.outputs["UV"],   n_map.inputs["Vector"])
    nt.links.new(n_map.outputs["Vector"], n_tex.inputs["Vector"])
    nt.links.new(n_tex.outputs["Color"],  bsdf.inputs["Base Color"])
    bsdf.inputs["Roughness"].default_value = 0.85
```

UV scale rule: `< 1.0` makes the pattern appear LARGER (less tiling). Bigger painterly spots → use 0.4-0.7. Tight repeats → 1.5-2.0.

After joining a group of meshes, re-run Smart UV Project on the joined object before applying textures:

```python
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.uv.smart_project(angle_limit=1.15, island_margin=0.02)
bpy.ops.object.mode_set(mode='OBJECT')
```

### 5. GLB export for three.js

```python
bpy.ops.export_scene.gltf(
    filepath=out_path,
    export_format='GLB',
    use_selection=True,
    export_yup=True,            # Blender Z-up → glTF Y-up
    export_apply=False,         # KEEP transforms — origins matter for animation
    export_normals=True,
    export_materials='EXPORT',
    export_animations=False,
    export_image_format='AUTO', # embed PNGs into the GLB
)
```

Three.js side, with a per-asset cache:

```js
const _glb = { cottage: null, cottagePromise: null };
export function loadCottageGLB(url = 'models/cottage.glb') {
  if (_glb.cottage) return Promise.resolve(_glb.cottage);
  if (_glb.cottagePromise) return _glb.cottagePromise;
  const loader = new GLTFLoader();
  _glb.cottagePromise = loader.loadAsync(url).then(g => {
    _glb.cottage = g.scene;
    g.scene.traverse(o => { if (o.isMesh) { o.castShadow = o.receiveShadow = true; } });
    return g.scene;
  });
  return _glb.cottagePromise;
}
```

Always `clone(true)` per spawn so each instance has independent transforms.

### 6. Procedural detail via random loops

For "stone block foundations", "brick chimneys", "shingles", "grass tufts", "flowers" — let Python place them:

```python
import random; random.seed(42)   # deterministic — same scene on every rerun

for r in range(rows):
    for c in range(cols):
        x = -fnd_w/2 + (c + 0.5) * block_w + random.uniform(-0.04, 0.04)
        mat = random.choice([mat_stone, mat_stoneL, mat_stoneM])
        add_box(f"Stone_{r}_{c}", w, 0.05, h, (x, face_y, z), mat)
```

Three or four mid-tone material variants in the random pick is enough to break uniformity; more makes it noisy.

### 7. Iteration loop

1. Write/edit a focused Blender Python script — one targeted change per pass.
2. `mcp__blender__render_viewport_to_path` → returns a temp path.
3. `cp` the file to `/tmp/<project>-debug/<asset>_vN.png` and `Read` it.
4. Compare to reference, identify the largest gap, repeat.

Keep one camera + sun setup at the top of every script so renders stay framed:

```python
cam = bpy.data.objects["PreviewCam"]
target = mathutils.Vector((0, 0, 1.7))
cam.location = (5.5, -5.5, 3.0)
cam.rotation_euler = (target - mathutils.Vector(cam.location))\
                       .to_track_quat('-Z', 'Y').to_euler()
sun = bpy.data.objects.get("PreviewSun")
sun.data.energy = 4.0
sun.rotation_euler = (math.radians(50), math.radians(-15), math.radians(40))
scene.world.node_tree.nodes["Background"].inputs[1].default_value = 0.4
```

### 8. Preview render settings that don't wash colors out

```python
scene.view_settings.view_transform = 'Standard'   # NOT 'Filmic' for stylized colors
scene.view_settings.look = 'None'
scene.world.node_tree.nodes["Background"].inputs[1].default_value = 0.35  # 0.3-0.5
sun.data.energy = 4.0–5.0  # higher to compensate for low ambient
```

Filmic tone-mapping pulls saturation out and crushes highlights — fine for photoreal, terrible for toon-painted.

## Pitfalls (every one of these bit during the cow + cottage builds)

### Materials keep their old image-texture nodes when you "switch" them back to solid color
Setting `bsdf.inputs["Base Color"].default_value` does NOT detach an existing TEX_IMAGE that's wired into Base Color. The texture wins. Fix:

```python
for n in list(nt.nodes):
    if n.type in {'TEX_IMAGE','TEX_COORD','MAPPING'}: nt.nodes.remove(n)
for link in list(nt.links):
    if link.to_node == bsdf and link.to_socket.name == "Base Color":
        nt.links.remove(link)
```

Symptom: "I set the horn material to cream but it still renders wood-grain."

### Blender 5.1 dropped `mesh.use_auto_smooth`
Old patterns like `o.data.use_auto_smooth = True; o.data.auto_smooth_angle = math.radians(35)` raise `AttributeError`. Replace with a Smooth-by-Angle modifier or just rely on `bpy.ops.object.shade_smooth()` plus enough geometry to look smooth.

### Roof tile rotation sign flip
`rot=(0, -pitch_deg * side, 0)` makes the tile's +Z axis point INTO the roof, so the tile sticks out edge-on. Use `+pitch_deg * side`. Verifiable by computing the rotated +Z axis: should equal the slope's outward normal `(sin(pitch)*side, 0, cos(pitch))`.

### Animation overrides rest position
`parts.Body.position.y = bob` clobbers the GLB's rest position (e.g. 0.55 in local space). Use a delta:

```js
e._cowBodyRestY ??= parts.Body.position.y;
parts.Body.position.y = e._cowBodyRestY + bob;
```

### Joining loses pivot, joining loses UVs
After `bpy.ops.object.join()`:
- The joined mesh inherits the leader's origin → set explicitly via cursor + `origin_set('ORIGIN_CURSOR')`.
- All parts share UV space → run Smart UV Project on the joined mesh before texturing.

### Two-slab roofs misalign at the ridge
The math for tilted slabs that meet exactly at the peak is tedious. Use a single triangular prism (cube with top vertices collapsed via bmesh) instead.

### `transform_apply(rotation=True)` only applies what you say
If you scale and rotate but only apply rotation, the scale stays as a transform. For predictable export, apply scale and rotation but NOT location (location IS the pivot).

```python
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
```

### Browser ESM cache makes you doubt your edits
After re-exporting `cottage.glb` or editing `src/main.js`, the running browser may still execute the cached prior version. Either:
- Run the local server with `Cache-Control: no-store, must-revalidate` headers.
- Close the tab fully and open a fresh one (in-tab reload doesn't always bust nested module caches).
- Cmd+Shift+R for a true hard reload.

### Headless Chrome can't render WebGL
Puppeteer with swiftshader fails to create a WebGL context. Don't use it to verify the visual state of a three.js scene — use a real Chrome via `claude-in-chrome` MCP, with the tab in the foreground (background tabs throttle RAF).

### Background MCP tab → animations frozen
`document.hidden === true` → Chrome pauses requestAnimationFrame entirely (since Chrome 88). Symptoms: scene rendered correctly once, but no per-frame state change. Visit the tab manually to see the animation actually run.

### `--tile` is the only seamless flag MJ honors
"seamless tileable" in the prompt isn't enough; some outputs still have visible seams. Add `--tile` flag every time. Even then, generate 3-4 variants and pick the cleanest one — MJ occasionally fails on the pattern (e.g. a "horn" prompt comes back as wood grain).

## Sample asset workflow (copy-paste)

```python
# Skeleton: cow with 7 named groups, painted textures, exported to GLB.
import bpy, math, mathutils, bmesh, os, random
random.seed(42)

# 1. Wipe (idempotent — script can be re-run without leftover state)
for o in list(bpy.data.objects):
    if o.name.startswith(('CowPart','Cow','Body','Head','Leg_','Tail')):
        bpy.data.objects.remove(o, do_unlink=True)

# 2. Materials (textured + solid color helpers omitted — see attach_texture above)
mat_white = make_textured("Cow_White", "models/textures/cow/cowhide_body.png", uv_scale=0.55)
mat_horn  = make_color("Cow_Horn", (0.94, 0.88, 0.70), 0.55)
# ... etc

# 3. Build sub-parts (each is a primitive with bevel + smooth)
body  = add_box("CowPart_Body", 1.10, 0.60, 0.55, (0,0,0.55), mat_white, bevel=0.14)
# ...

# 4. Group into 7 named meshes, each with its own pivot
m_body = join_to("Body",   [body, chest, neck, ...], pivot_world=(0,0,0.55))
m_head = join_to("Head",   [head, jowl, snout, ...], pivot_world=(0.85,0,0.66))
# ...

# 5. UV unwrap each joined group
for o in [m_body, m_head, m_FL, m_FR, m_BL, m_BR, m_tail]:
    bpy.ops.object.select_all(action='DESELECT')
    o.select_set(True); bpy.context.view_layer.objects.active = o
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.uv.smart_project(angle_limit=1.15, island_margin=0.02)
    bpy.ops.object.mode_set(mode='OBJECT')

# 6. Parent everything to a root empty
bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0,0,0))
root = bpy.context.active_object; root.name = "CowRoot"
for m in [m_body, m_head, m_FL, m_FR, m_BL, m_BR, m_tail]:
    bpy.ops.object.select_all(action='DESELECT')
    m.select_set(True); root.select_set(True)
    bpy.context.view_layer.objects.active = root
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

# 7. Export
bpy.ops.object.select_all(action='DESELECT')
for o in [root] + groups: o.select_set(True)
bpy.context.view_layer.objects.active = root
bpy.ops.export_scene.gltf(
    filepath="models/cow.glb", export_format='GLB',
    use_selection=True, export_yup=True, export_apply=False,
    export_normals=True, export_materials='EXPORT',
    export_image_format='AUTO', export_animations=False,
)
```

## Procedural creature recipe — empties as rig pivots, separate meshes per part

Alternative to the join-into-named-groups approach above. Use this when each
sub-part wants its own material (cream body / brown spots / pink snout / brass
bell), or when iteration speed matters more than mesh count.

### The mental shift

- **Rig pivots are EMPTIES**, not joined meshes. Create one `EMPTY` per
  animatable joint at the joint's world position (hip top, neck base, body
  centre, tail base).
- **Each visual part is a SEPARATE mesh**, parented to whichever empty it
  should follow. `Eye_L` → `Head` empty. `LegFL_Hoof` → `Leg_FL` empty.
- The three.js side reads `inst.userData.parts.Head` (the empty) and rotates
  IT — every mesh under it follows automatically.

### The single most important rule: place geometry at WORLD positions before parenting

```python
# RIGHT
bpy.ops.mesh.primitive_cube_add(size=2, location=(0.33, 0, 0.54))   # head, in world space
o.scale = (0.16, 0.17, 0.16); apply scale
o.parent = head_empty   # Blender writes the correct parent_inverse to keep
                        # mesh.world unchanged. Mesh.local naturally becomes
                        # the offset relative to head_empty's world position.
```

```python
# WRONG — the bug that bit the v2 archetype meshes + first cow rebuild
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))     # head at origin
o.parent = head_empty   # Blender writes parent_inverse = -head_empty.world
                        # to KEEP the head at world (0,0,0). Result: animation
                        # rotating head_empty does nothing visible — the
                        # parent_inverse cancels out the rig motion.
```

The parent_inverse itself isn't the enemy. Authoring meshes at `(0, 0, 0)` and
relying on the rig to "carry them" later is the enemy. Place each mesh at its
intended world position FIRST, then parent — Blender's default `keep_transform`
behaviour writes the right inverse and the rig drives the mesh correctly.

### Cube size gotcha

`bpy.ops.mesh.primitive_cube_add(size=N)` creates a cube with **side length N**
(vertices at ±N/2). If you scale by `(sx/2, sy/2, sz/2)` expecting dimensions
`(sx, sy, sz)`, you get half — because `size=1` gives a 1-unit cube and `0.5`
scaling halves it to 0.5 units.

Two equivalent fixes:
- `primitive_cube_add(size=2)` then `o.scale = (sx/2, sy/2, sz/2)` → final
  dimension `sx/sy/sz`. Verbose but reads naturally.
- `primitive_cube_add(size=1)` then `o.scale = (sx, sy, sz)` → same final
  dimension. Compact.

**Verify with a render and a world-bbox dump** — eyeballing coordinates is
unreliable. Pick one mesh, list its world bbox span, confirm it matches
intent. If it's half, you hit this trap.

### Push surface details OUTSIDE the parent's face

Eyes, spots, ear-inner panels — anything that should sit on a parent's surface
needs to be at `parent_face_position + 0.005u` outside the parent. If you
position them at the parent's centre or anywhere inside the parent's bbox,
they're hidden geometry. Visible only by accident if the camera looks through
a thin parent wall.

```python
# Head bbox: x 0.17..0.49, y -0.17..0.17. Eyes need to be on the front face.
add_sphere('Eye_L', (0.495, -0.13, 0.58), 0.035, ...)   # X = 0.495 = front face + 0.005
# NOT x = 0.42 (centre of head — eye is invisible inside)
```

Same trap for spots on a body's side: position at `body_y_max + 0.005`
(not `body_y_centre`).

### "Touching" needs a small overlap, not an exact junction

Two meshes whose faces meet at exactly the same plane Z-fight. Two meshes whose
faces are 0.001u apart show a hairline gap. Aim for a 0.005-0.02u **overlap**:

- Head back at `x = 0.17`, body front at `x = 0.165` → 0.005u overlap, no gap
- Hoof top at `z = 0.05`, leg shaft bottom at `z = 0.04` → 0.01u overlap
- Spot at `y = body_max_y + 0.005` → spot inflated 0.005u outside body face,
  visually attached, no Z-fighting because the planes are 0.005u apart

### Iteration discipline: render between every meaningful change

1. Make ONE change (move head down, resize body, push eyes forward).
2. Render. Read the PNG. Compare to concept art / previous render.
3. Either keep going or revert. Don't stack 5 changes before rendering — when
   the result looks wrong you won't know which change caused it.

The `mcp__blender__render_viewport_to_path` → `Read` loop is fast enough to
do 20+ times per asset. Use it.

### Verify with bbox dumps when renders are ambiguous

When a render shows "something looks floating" but you can't tell which part:

```python
out = []
for o in bpy.context.scene.objects:
    if o.type == 'MESH' and o.data.vertices:
        coords = [o.matrix_world @ v.co for v in o.data.vertices]
        out.append({
            "name": o.name,
            "world_xc": round(sum(c.x for c in coords)/len(coords), 2),
            "world_yc": round(sum(c.y for c in coords)/len(coords), 2),
            "world_zc": round(sum(c.z for c in coords)/len(coords), 2),
            "size": [round(max(c.x for c in coords)-min(c.x for c in coords), 2),
                     round(max(c.y for c in coords)-min(c.y for c in coords), 2),
                     round(max(c.z for c in coords)-min(c.z for c in coords), 2)],
        })
```

Sort by Z-centre or by parent name; an outlier — a part whose world centre
is far from where its parent sits — is the floater.

### Skeleton recipe (cow, ~32 meshes, 7 rig empties, ~10 minutes)

```python
def add_box(name, world_center, size, mat, parent, bevel_width=0.025):
    cx, cy, cz = world_center
    sx, sy, sz = size
    bpy.ops.mesh.primitive_cube_add(size=2, location=(cx, cy, cz))   # size=2!
    o = bpy.context.active_object; o.name = name
    o.scale = (sx/2, sy/2, sz/2)                                     # halves to dim
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    o.data.materials.append(mat)
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles(threshold=0.0001)
    bpy.ops.object.mode_set(mode='OBJECT')
    mod = o.modifiers.new('Bevel', 'BEVEL')
    mod.width = min(bevel_width, min(size) * 0.08)
    mod.segments = 2; mod.limit_method = 'ANGLE'; mod.angle_limit = math.radians(30)
    # Parent — keep_transform=True is the default and the right thing here
    # because we placed the cube at its proper world position above.
    bpy.ops.object.select_all(action='DESELECT')
    o.select_set(True); parent.select_set(True)
    bpy.context.view_layer.objects.active = parent
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
    return o

def add_empty(name, location, parent=None):
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=location)
    o = bpy.context.active_object; o.name = name
    if parent:
        bpy.ops.object.select_all(action='DESELECT')
        o.select_set(True); parent.select_set(True)
        bpy.context.view_layer.objects.active = parent
        bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
    return o

# Layout: cow facing +X, Z up, ~0.9m long × 0.7m tall.
root = add_empty('CowRoot', (0, 0, 0))
body_emp = add_empty('Body',   (-0.10, 0, 0.42), parent=root)
head_emp = add_empty('Head',   (0.20,  0, 0.50), parent=root)  # neck-base, where animation pivots
tail_emp = add_empty('Tail',   (-0.42, 0, 0.50), parent=root)
leg_fl   = add_empty('Leg_FL', (0.10, -0.18, 0.30), parent=root)  # hip top
leg_fr   = add_empty('Leg_FR', (0.10,  0.18, 0.30), parent=root)
leg_bl   = add_empty('Leg_BL', (-0.30, -0.18, 0.30), parent=root)
leg_br   = add_empty('Leg_BR', (-0.30,  0.18, 0.30), parent=root)

# Body + spots + tail + head + snout + eyes + horns + ears + collar + bell + 4 legs.
add_box('Body_Mesh', (-0.10, 0, 0.42), (0.55, 0.42, 0.40), MAT_BODY, body_emp, bevel_width=0.06)
# spots inflated 0.005u outside body Y faces:
add_box('Spot_0', (-0.20, -0.215, 0.50), (0.16, 0.04, 0.13), MAT_SPOT, body_emp, bevel_width=0.005)
# eyes pushed onto front face of head (head front X = 0.49):
add_sphere('Eye_L', (0.49, -0.13, 0.58), 0.035, MAT_EYE, head_emp, segments=10, rings=8)
# ... etc — every part placed at its WORLD position before parenting.
```

The result exports cleanly to glTF (`yup=True, apply=True, animations=False,
skins=False`) and the named empties (`Body, Head, Tail, Leg_FL, Leg_FR, Leg_BL,
Leg_BR`) hook directly into the project's procedural animation in
`src/anim/cow.js` without code changes.

## Quick reference

| Need                                     | Pattern                                                     |
| ---------------------------------------- | ----------------------------------------------------------- |
| Chunky soft cube                         | Bevel modifier `0.04 / 2 segs / 30°` + shade_smooth         |
| Pillow-shaped form                       | Above + Subdivision Surface level 1                         |
| Triangular roof                          | Cube + bmesh: pinch verts where `co.z > 0` to `co.x = 0`    |
| Pivot at hip / neck / base               | Empty at the pivot world position; mesh parented at world   |
| Avoid parent_inverse trap                | Place mesh at world pos BEFORE parenting; never at (0,0,0)  |
| Cube of dimension D                      | `primitive_cube_add(size=2)` + `scale=(D/2, D/2, D/2)`      |
| Surface details visible                  | Position at `parent_face + 0.005u`, not parent centre       |
| Joints touch without Z-fighting          | 0.005-0.02u overlap, never zero-gap or tiny-gap             |
| Tileable AI texture                      | TexCoord → Mapping (scale 0.4-0.7) → ImageTex → Base Color  |
| Three.js procedural rig                  | Named empties as pivots, `inst.traverse` to grab refs       |
| Stop washed-out colors                   | view_transform='Standard', bg strength 0.35-0.45, sun 4-5   |
| Fresh browser modules                    | `Cache-Control: no-store` + close-and-reopen tab            |
| Diagnose floating bits                   | Dump world bbox per mesh, sort by Z, find the outlier       |
