# Source Attribution — nvidia-omniverse-realtime-viewer

- **Upstream repository**: https://github.com/NVIDIA/skills
- **Upstream path**: `skills/omniverse-realtime-viewer/`
- **Upstream version**: `0.1.0`
- **License**: Apache-2.0
- **Author**: NVIDIA Omniverse
- **Last upstream commit reviewed**: 2026-05-29 (`6c6fc09` — manually staged into catalog)

## What Was Extracted

This local `SKILL.md` is a condensed, opinionated excerpt of the upstream
`SKILL.md`. It preserves:

- The top-level router purpose and frontmatter.
- The architectural non-negotiables (ovrtx-only rendering, no browser-side 3D
  renderer fallbacks, viewer-state separation from source USD, single owner for
  render stepping and stage mutation).
- The canonical read order and build workflow.
- The completion checklist.

The upstream `references/` directory (routing, conventions, streaming/local
recipes, viewer UX, input, camera, selection, render settings, deployment,
validation, etc.) is **not mirrored** here. Users who need the full reference
family should clone the upstream repository or install the skill with:

```bash
npx skills add NVIDIA/skills --skill omniverse-realtime-viewer
```

## Why Included in CursorSkill

- Complements the already-indexed `nvidia-omniverse-cad-to-simready` and
  `nvidia-omniverse-usd-performance-tuning` skills as the third leg of the
  NVIDIA Physical AI / Omniverse USD workflow: **produce → optimize → view**.
- Provides a strong, vendor-enforced boundary against the common anti-pattern
  of falling back to browser WebGL/Three.js when a GPU runtime is missing.
- Useful for teams building USD-based review tools, digital-twin viewers, or
  synthetic-data inspection UIs that eventually feed assets into UE 5.2+ via
  Interchange USD.

## Direction Tags

`3d` / `dev-workflow`
