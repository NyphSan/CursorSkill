---
name: design-game-ui
description: "Design, implement, polish, or audit UI inside playable games: HUDs, menus, inventory, maps, dialogs, reticles, touch controls, gamepad navigation, visual assets, component states, motion, audio or haptic feedback, responsive layouts, input ownership, and screenshot QA. Use for browser, desktop, mobile, 2D, or 3D game projects when the task concerns in-game interface quality or interaction feel. Also use when replacing placeholder icons or frames, defining UI art direction, generating production UI assets, or fixing hover, focus, pressed, selected, disabled, loading, pointer-lock, and modal behavior. Do not use for game marketing sites, store pages, community portals, analytics or admin dashboards, or gameplay systems unrelated to UI."
---

# Design Game UI

## Mission

Create game-native interfaces that improve player decisions, control, feedback, and immersion. Treat the playable scene, player verbs, and input model as the primary design constraints. Do not disguise generic website or SaaS patterns with gradients, glow, or decorative borders.

## Operating Principles

1. Establish game context before styling.
2. Build one coherent visual language before generating assets.
3. Treat interaction states as a system, not isolated CSS effects.
4. Keep gameplay, rendering, input mapping, and presentation ownership explicit.
5. Validate in the running game at representative states and viewports.
6. Use reference cases to extract transferable patterns, never to clone protected assets, exact trade dress, or branded composition.
7. Do not claim an asset, screenshot, input test, or visual check was completed unless it was actually produced or run.

## Classify the Task

Classify the request as one or more of:

- `design`: create a new UI direction or surface architecture
- `implement`: build or connect UI in an existing game
- `polish`: replace placeholders and improve hierarchy, assets, states, motion, sound, or feel
- `audit`: inspect an existing implementation and report or fix defects
- `case-update`: add or revise a reference case for future work

Keep the scope narrow when the user asks for one component. Use the full workflow for multi-surface redesigns, asset generation, or production-readiness claims.

## Core Workflow

### 1. Inspect the Project

Inspect the repository before proposing a design. Determine:

- game genre, fantasy, core loop, camera, and primary player verbs
- target platforms, viewports, input methods, and accessibility requirements
- renderer or engine and the boundary between playfield and UI
- existing game state, input action map, UI framework, theme tokens, fonts, icons, and art assets
- current surfaces, information priority, safe zones, pointer-lock or camera-control behavior
- existing test, screenshot, browser automation, and asset-generation capabilities

Reuse stable architecture and assets when they fit. Do not rebuild the UI stack merely to apply a visual treatment.

### 2. Record a Decision Snapshot

For a small change, state the decisions briefly in the work log. For a multi-surface or asset-heavy task, copy and complete:

- `assets/templates/visual-direction-lock.json`
- `assets/templates/ui-surface-inventory.json`
- `assets/templates/asset-manifest.json` when generated or replaced assets are involved

Place project-specific copies under `docs/game-ui/` unless the repository already has an equivalent location. Do not add planning files for a trivial one-component fix.

### 3. Select the Right Knowledge

Read only the references needed for the task:

- visual system and quality: `references/visual-direction.md`
- generated or replacement assets: `references/asset-pipeline.md`
- hover, focus, pressed, selected, disabled, loading, motion, sound, and haptics: `references/interaction-feedback.md`
- component-specific behavior: `references/component-recipes.md`
- genre and camera defaults: `references/genre-archetypes.md`
- playfield, modal, pointer-lock, focus, and input ownership: `references/playfield-and-input.md`
- scoring and critical failures: `references/qa-rubric.md`
- case selection and case updates: `references/reference-case-workflow.md` and `references/case-library.json`

Use one to three relevant reference cases. Explain internally which transferable patterns apply and which branded details must not be copied. Do not mix unrelated case aesthetics merely to increase visual complexity.

### 4. Define Surface and Input State

Classify each surface as:

1. persistent gameplay HUD
2. contextual or transient gameplay UI
3. blocking overlay
4. pause or meta UI

For every surface define:

- visibility condition and information priority
- input owner and supported devices
- whether simulation pauses
- camera, drag-look, or pointer-lock behavior
- initial focus, focus order, confirm, cancel, and close behavior
- stacking, dismissal, loading, error, and interrupted-transition behavior

Never allow gameplay actions or camera input to leak through a blocking UI unless the design deliberately requires a hybrid mode and the allowed actions are enumerated.

### 5. Lock the Visual Direction

Define one coherent direction before styling or generating assets:

- game fantasy and UI metaphor
- material and shape language
- typography and number treatment
- palette and semantic colors
- icon and illustration language
- spacing, depth, edge, shadow, and glow hierarchy
- motion tone, audio tone, and effects budget

Expose reusable values as design tokens. Reserve strong glow, particles, bounce, shake, and long transitions for meaningful events. Do not give every component equal visual weight.

### 6. Run the Asset Pass

Audit placeholder and mismatched assets. Classify each replacement as:

- CSS-rendered geometry or material
- SVG or tintable icon
- generated raster asset
- generated nine-slice frame
- sprite or state atlas
- existing project asset

Prefer DOM, CSS, or SVG for dynamic text, localization, values, scalable geometry, and accessibility-sensitive controls. Use generated art for thematic silhouettes, ornaments, textures, badges, illustrations, icon families, and frames that genuinely require art direction.

When an image-generation capability is available:

1. generate one style anchor first
2. approve or inspect it at final in-game scale
3. generate related assets as one family from the same anchor
4. preserve transparency, padding, silhouette, and protected nine-slice regions
5. integrate the files and inspect them in the running game

Never bake dynamic or localized text into generated images. Never generate related states independently when geometry must remain stable. When no image-generation capability is available, produce the manifest and prompts with `scripts/build_asset_prompts.py`; report the missing generation step explicitly instead of pretending it happened.

Validate PNG or SVG outputs with `scripts/inspect_ui_assets.py` when a manifest is available.

### 7. Run the Interaction Pass

Every interactive component must implement all applicable states:

- idle
- hover
- focus-visible or gamepad focus
- pressed
- selected
- disabled
- loading
- success
- error
- attention

Keep hover, focus, pressed, and selected visually distinguishable. Do not rely on hover on touch devices. Do not rely on color alone for critical state.

Use coordinated feedback channels:

- color or brightness
- edge, depth, and shadow
- small translation or scale
- icon or label treatment
- motion
- audio
- haptics where supported

Pressed controls should usually show physical engagement through a small downshift, scale reduction, or depth compression. Avoid layout shift: animate transform and opacity where possible, and do not change border width, content size, or surrounding flow during state changes.

Use shared motion tokens. Functional feedback must be faster than decorative transitions. Respect reduced-motion preferences.

### 8. Implement in Four Passes

1. `functional`: data, actions, state ownership, input mapping, and error handling work
2. `visual-language`: typography, hierarchy, tokens, iconography, materials, and assets are coherent
3. `interaction-feel`: pointer, keyboard, gamepad, touch, motion, audio, and haptic feedback are complete
4. `in-engine-qa`: representative states are exercised and visually inspected over the real playfield

Do not report completion after only the functional pass or a successful compile.

### 9. Validate

Run the most relevant checks:

```bash
python3 scripts/validate_skill.py .
node scripts/audit_ui_polish.mjs /path/to/game-ui --strict
node scripts/capture_ui_states.mjs --config /path/to/ui-capture.config.json
python3 scripts/inspect_ui_assets.py --manifest /path/to/asset-manifest.json --asset-root /path/to/game
```

Use existing repository test commands as well. For Canvas or WebGL games, screenshots are mandatory because DOM assertions cannot judge scene obstruction, depth competition, material mismatch, or readability over motion.

Capture representative evidence for applicable states:

- normal gameplay
- contextual prompt
- hover and pointer press
- keyboard focus and gamepad focus
- selected and disabled
- loading, error, success, or danger
- blocking overlay and pause
- desktop and mobile or touch viewport
- reduced-motion mode when motion is substantial

Revise and recapture when critical issues remain.

## Non-Negotiable Quality Rules

- Do not use generic admin-dashboard composition for live gameplay.
- Protect the central and lower-middle playfield during action gameplay.
- Prefer contextual disclosure over permanently expanded instructions, lore, objectives, and controls.
- Use DOM for text-heavy HUD, menus, settings, and accessible controls by default; use Canvas or WebGL when world-space placement, reticles, shaders, or renderer coupling justify it.
- Do not leave emoji, arbitrary Unicode glyphs, inconsistent icon families, default form controls, temporary gray boxes, or unthemed focus states as production UI without a documented reason.
- Do not apply the same glow, scale, bounce, or sound to every component.
- Do not make disabled controls appear actionable.
- Do not confuse selected state with current navigation focus.
- Do not let a modal open without a deterministic cancel or close path.
- Do not copy proprietary fonts, logos, illustrations, icons, exact layouts, or branded motifs from reference games.

## Definition of Done

A production-ready claim requires:

- coherent visual-direction lock
- complete surface and input-state model
- production-appropriate assets or an explicitly incomplete asset step
- complete applicable interaction states
- keyboard, pointer, gamepad, and touch support required by the project
- responsive behavior at supported viewports
- in-engine screenshots or equivalent visual evidence
- no critical failure in `references/qa-rubric.md`
- a concise QA report with assumptions, exceptions, unresolved non-critical issues, and evidence paths

## Final Report

Lead with what changed and what was verified. Include:

1. surfaces and files changed
2. visual direction and reference patterns used
3. generated or replaced assets and their validation status
4. interaction and input states implemented
5. tests, viewports, and screenshots exercised
6. critical issues resolved
7. remaining limitations and deliberate exceptions
