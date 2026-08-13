---
name: haxqer-godot-skill
description: Use when a coding agent (Claude Code, Codex, Cursor, Kiro) is asked to author, edit, debug, run, test, or export a Godot project. Covers Godot 4.7 (compatible with 4.x) — scene/script/resource inspection, batch scene transactions, TileSet / TileMapLayer / SpriteFrames / AnimationPlayer authoring, Theme/UI overrides, signal wiring, GridMap painting, 2D + 3D navigation mesh baking, CSG collision, glTF export, headless debugging, GUT / GdUnit4 test runners, deterministic scenario runs (input + assert + screenshot + perf threshold), and preset/environment-validated export (Android / iOS / Web / Win / Linux / macOS / dedicated server / visionOS). Auto-loads when the user mentions `.tscn` / `.tres` editing, autotiling, atlas slicing, scene refactor, GDScript or GDExtension validation, or "headless run / bake / paint / export".
---

# haxqer / godot-skill — portable Godot project automation

A portable Godot skill for Codex-style skill loaders (Claude Code / Codex CLI / Cursor / Kiro). Released under **MIT License on 2026-08-11**; substantial content updates landed 2026-07-14 (`feat: Add 3D/theme/navmesh authoring ops and inline-builder codec` — 9 test suites green against Godot 4.7) and 2026-08-11 (`Merge feat/godot-authoring-ops into main` → `b4d0e38`).

The skill payload itself lives at `skill/godot/` and **excludes `README.md` on purpose** so it can be copied into any skills directory without GitHub-specific files. There is a separate `scripts/package_skill.sh` that produces `dist/godot.zip` for release installs.

## When to use

Reach for godot-skill whenever the agent would otherwise hand-author or hand-edit Godot project files:

- **Transactional scene / resource / project editing** — node hierarchies, properties, signals, autoloads, InputMap, layer names, translations
- **Content authoring** — TileSet + TileMapLayer paint (including terrain autotiling), sprite-sheet slicing with per-frame durations, declarative AnimationPlayer clips, AudioBusLayout routing, shader globals
- **Headless validation + debugging** — Godot CLI runs with structured log parsing, deterministic input/assert/screenshot/perf scenarios, GUT / GdUnit4 test runners, static validation of GDScript / C# / GDExtension / plugin
- **2D + 3D baking** — mesh / CSG collision, sprite-outline collision, 2D + 3D NavigationMesh baking, glTF export
- **Export** — preset / environment preflight, Android / iOS / Web / Windows / Linux / macOS / dedicated server / visionOS

## Trigger examples

- "Open my Godot 4.7 project and paint this tileset onto the gridmap"
- "Slice this spritesheet into SpriteFrames with the durations from the readme"
- "Bake the navigation mesh for both 2D and 3D"
- "Run the project headless and turn runtime errors into structured diagnostics"
- "Wire this signal, refactor this node tree, swap this theme"
- "Set up export presets and export to Web + Windows"
- "Run GUT / GdUnit4 tests and report failures"
- "Validate every script, scene, shader, and resource before commit"

## What the skill actually does (4 surfaces)

### 1. Inspect — read unfamiliar projects without instantiating scenes

```text
inspect_project(<path>)
inspect_scene(<scene_path>)
inspect_resource(<res_path>)
```

Returns node trees, properties, signals, metadata, layer / group membership — without booting Godot. Lets the agent understand an unfamiliar codebase before mutating.

### 2. Edit — batch / transactional scene + resource + project mutations

`resource_batch` and `project_batch` are transactional:
- Properties, metadata, InputMap, autoloads, layer names, translations
- `call_method` action for builder-style APIs (`Gradient.add_point`, `Theme.set_color`, `TileSet.add_source`)
- `bake_navmesh` (2D NavigationPolygon + 3D NavigationMesh)
- `project_batch set_shader_global / clear_shader_global`
- `control` layout + theme overrides
- Script attachment, signal wiring, hierarchy refactors
- `build_sprite_frames` for AnimatedSprite2D frame animation

The dispatcher defers every operation through `await`, which makes autoload singletons register as global identifiers before scripts are loaded — fixing the false "Identifier not found" failures that bite projects with autoloads. `bake_csg` can await CSG frames.

### 3. Author — content-integration ops

- **`build_tileset`** — atlas sources, per-tile collision / custom data / terrains
- **`paint_tilemap`** — cells, fills, terrain autotiling on TileMapLayer
- **`build_sprite_frames`** — atlas mode (spritesheet slicing, per-frame duration, multiple animations)
- **`build_animation` / `build_animation_tree`** — keyframe clips and state machines via AnimationPlayer / AnimationLibrary / AnimationTree
- **`setup_audio_buses`** — AudioBusLayout routing
- **`set_import_options`** — patch `.import` params (e.g. audio loop mode)
- **`paint_gridmap`** — GridMap painting (3D)
- **`build_theme`** — programmatic Theme construction
- **`build_replication_config`** — for networking / Godot 4.x dedicated server setups

### 4. Validate / run / export

- `validate_project.py` — GDScript / C# / GDExtension / plugin checks (must-have)
- `audit_imports` + `import_project.py`
- `scenario_runner.gd` + `run_scenario.py` — deterministic input / assertion / screenshot / perf scenario
- `probe_environment.py` — detect installed Godot version, plugin status, etc.
- `run_tests.py` — headless GUT / GdUnit4 runner
- Export wrapper gains preflight checks + `pack` / `patch` modes; Android / iOS / Web / Windows / Linux / macOS / dedicated server / visionOS

Every dispatcher operation now exits non-zero on any logged error, so shell callers gate on exit codes instead of parsing stderr.

## Bundled reference docs (in `skill/godot/references/`)

| Doc | Why it matters |
|---|---|
| `automation_api.md` | Operation-by-operation schema + coding idioms |
| `authoring_recipes.md` | Recipes + editor-only non-goals |
| `vfx_2d.md` | 2D VFX / shader / particle recipes |
| `localization.md` | Translation setup, autoload, layer names |
| `ci.md` | GitHub Actions / headless CI recipes |
| `tween.md` | Tween + animation transition recipes |
| `asset_pipeline.md` | Sprite / texture / chroma-key cutout pipeline |
| `architecture_qframework_lite.md` / `architecture_templates.md` | QFramework-style architecture references for GDScript |
| `debugging.md` | Structured log parsing, runtime diagnostics |

## Install + use in one minute

```bash
# From source — copy skill/godot/ into any skills directory
git clone https://github.com/haxqer/godot-skill
cp -r godot-skill/skill/godot/ ~/.claude/skills/
# or .cursor/skills/ or .codex/skills/ etc.

# From release zip (auto-builds `dist/godot.zip`)
cd godot-skill
./scripts/package_skill.sh
# Unzip into your skills directory; the zip already contains the top-level `godot/` folder

# Requires the godot CLI on PATH (any 4.x; tested on 4.7)
which godot
```

## Quality signals

- **License**: MIT added 2026-08-11 (`chore: add MIT license` → `47ad12b`). Before 08-11 the project was license-less (wait-listed in 08-12 daily as "Yuki001 still no LICENSE"); the LICENSE addition cleared the gate
- **Tests**: 9 test suites green against Godot 4.7 (`tests/test_new_ops.py`). The CI matrix is small but real
- **Co-authorship trail**: every substantial feature commit has `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` / `Claude Sonnet 5` — explicit signal that the maintainer is iterating the skill with AI assistance, which is helpful context for how aggressively the frontmatter / op schema can change
- **Source quality**: per the 08-11 merge and the 07-14 ops dump, the skill ships real, locatable Godot 4.x APIs (NavigationPolygon, AnimationPlayer, TileMapLayer, AudioBusLayout, GridMap, CSG, glTF), not just prompts

## What it is NOT

- Not a Unity / Unreal skill — Godot only. For Unreal use `kevinpbuckley-unreal-engine-skills` (61 SKILL, broad) + `quodsoler-unreal-engine-skills` (27 SKILL, deep-audited C++) already in this repo
- Not a general-purpose design / art skill — no sprite authoring pipeline beyond chroma-key cutout + slice-to-atlas; bring `dcc-mcp-blender` or `qwen-mm-plugins-blender` for art generation
- Not a 3D-content library — it can edit / paint / run / export; for source 3D assets, see the 3D design directory

## Sharp edges

- **Dispatcher requires a local `godot` CLI** with shell access. Remote / sandboxed environments need `BLENDER_HOST`-style plumbing not in scope
- **Autoload-sensitive**. Operations now defer through `await` to handle the registration order, but very old Godot projects (< 4.x) may need careful audit
- **License added only on 2026-08-11**. Anything that pins a commit older than that needs a manual LICENSE audit
- **Skill payload intentionally excludes `README.md`**. If you need the README, read it from the repo before copying — but do NOT bundle it into the skills directory; that breaks downstream skill loaders
- **glTF export is a single op, not a full DCC pipeline**. Bring your own materials / animations before invoking `gltf_export`

## Search coverage note

- Picked up **2026-08-13** during a d7-window scan for Godot / Unity / 2D-pixel-art skill packages. The 08-11 LICENSE change plus the 08-11 merge of `feat/godot-authoring-ops` (3D / theme / navmesh authoring) is a clear "实质性更新" signal vs. star-only activity
- Sits in `skills/game-design/` because the dominant surface is game authoring (TileMap / SpriteFrames / AnimationPlayer / autotile), even though it also covers 3D authoring and headless engineering
- Pairs with `heycat-isometric-*` skills already in repo (`skills/2d/heycat-*`) — those handle iso pipeline; this one handles Godot-native scene + content ops
- Pairs with `gamedev-create-game-assets` (already in repo) for asset creation; pair with `dcc-mcp-blender` for art generation; pair with `game-design-document` / `game-world-design` / `gamedev-audio-design` for design-discipline framing
