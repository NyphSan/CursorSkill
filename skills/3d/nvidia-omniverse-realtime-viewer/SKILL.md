---
name: nvidia-omniverse-realtime-viewer
description: |
  Use as the top-level router for Omniverse Realtime Viewer USD app requests.
  Activate when the user asks to build, extend, or validate an interactive
  USD viewer: browser-streamed, local desktop, Tauri, Electron, ovui, or
  native C++ viewport. Forces ovrtx for all USD/3D rendering and prohibits
  browser-side WebGL/Three.js/Babylon fallbacks.
version: "0.1.0"
license: Apache-2.0
metadata:
  author: NVIDIA Omniverse
  source: https://github.com/NVIDIA/skills/tree/main/skills/omniverse-realtime-viewer
  tags:
    - omniverse
    - usd
    - viewer
    - ovrtx
    - 3d
    - workflow
---

# NVIDIA Omniverse Realtime Viewer

## Purpose

Top-level orchestrator for building interactive USD viewers on the Omniverse
stack. It classifies the requested delivery path, selects the minimal focused
reference set, and enforces architectural rules that must hold across every
generated viewer app.

## When to Use

- "Build a USD viewer"
- "Stream an Omniverse scene to a browser"
- "Add camera / picking / hierarchy panel to an ovrtx viewport"
- "Create a local workstation viewer for OpenUSD"
- "Wrap ovrtx in a Tauri / Electron / React frontend"

## Non-Negotiables

1. **All USD and 3D rendering must use `ovrtx`.**
2. Browser apps display an `ovstream` WebRTC video stream plus UI. The browser
   does **not** render USD geometry itself.
3. Do **not** substitute WebGL, Three.js, Babylon.js, PlayCanvas, A-Frame,
   model-viewer, react-three-fiber, glTF viewers, or any client-side 3D renderer.
4. If the local GPU/runtime is absent, scaffold the `ovrtx` path and document
   the runtime requirement. Do **not** add a browser-renderer fallback.
5. Keep user USD files unmodified. Viewer state (cameras, render products,
   render vars, settings, selection metadata) belongs in session/composite
   layers or app state.
6. Maintain one clear owner for `renderer.step()`, stage mutation, native
   picking, selection writes, and live attribute writes.

## Read Order

1. `references/routing.md` — choose the delivery path and focused references.
2. `references/conventions.md` — before camera, input, selection, viewport,
   streaming protocol, scene loading, or environment behavior.
3. `references/usd-viewer-app/README.md` — for broad viewer requests.
4. `references/streaming-vs-local/README.md` — if the delivery path is unclear.
5. `references/viewer-ux-workflow/README.md` — if the prompt includes layout,
   panels, controls, inspectors, status, or UX.
6. `references/viewer-input-routing/README.md` — before camera, picking, or
   selection references.
7. Read only the capability references required for the app.
8. `references/validation.md` — capture review evidence before handoff.

## Build Workflow

1. **Classify** the prompt by delivery path, target user, required capabilities,
   runtime environment, validation needs, and explicit constraints.
2. **Select a small reference set** — start with the recipe/routing reference,
   then add focused capabilities (camera, picking, hierarchy, properties,
   render settings, transform tools, cloud assets, deployment).
3. **Read selected references before writing app code.** Follow their build
   order, import order, data-channel contracts, and renderer ownership rules.
4. **Implement the core render path first**, then input routing and camera,
   then selection and data panels, then scene/settings features, then
   packaging/deployment.
5. **Capture validation evidence** before calling the viewer ready.

## Completion Checklist

- [ ] Selected references match the user's intent and delivery path.
- [ ] No code path uses a browser-side 3D renderer for USD.
- [ ] One clear owner exists for render stepping and stage mutation.
- [ ] User USD files remain untouched by viewer-owned session data.
- [ ] Camera, input, selection, scene loading, and stream behavior follow
      `references/conventions.md`.
- [ ] Setup/build/run results and visual interaction evidence are captured.

## Notes for UE/Game Teams

This skill is about building a standalone Omniverse viewer, not an Unreal
plugin. The architectural discipline is transferrable: single owner for render
step, separate viewer state from source USD, and validate with evidence before
handoff. If the end goal is to bring SimReady USD into UE 5.2+, pair this
with `nvidia-omniverse-cad-to-simready` and UE's Interchange USD importer.
