# Source Attribution — nvidia-simready-foundation-conform-fet-000-core

- **Upstream repository**: https://github.com/nvidia/simready-foundation
- **Upstream path**: `skills/simready-foundation-conform-fet-000-core/`
- **Upstream release**: `2026.06.0` (commit `0ed0dfb`, 2026-08-04)
- **License**: Apache-2.0
- **Author**: Shaad Boochoon (NVIDIA)

## What Was Extracted

This local `SKILL.md` is a condensed excerpt of the upstream skill. It keeps:

- The conformance purpose and staged-output policy.
- Required inputs and the source-of-truth manifest paths.
- The ordered repair checklist tied to FET000_CORE requirement IDs.
- Mechanical vs. blocked repair policies.
- The summary format for handoff to downstream profile validation.

The upstream `assets/scripts/`, `references/`, and `nv_core/sr_specs/`
requirement documents are **not mirrored** here. For full conformance tooling
and validator entrypoints, clone the upstream repository or install the skill
with:

```bash
npx skills add nvidia/simready-foundation --skill simready-foundation-conform-fet-000-core
```

## Why Included in CursorSkill

- Discovered during the 2026-08-15 scan as a new standalone NVIDIA repository
  for SimReady USD conformance (previously only `NVIDIA/skills/omniverse-*`
  were tracked).
- Fills the gap between "produce USD" and "import USD into UE/engine": a
  deterministic cleanup step for naming, paths, metadata, and prim hygiene.
- Apache-2.0 license allows redistribution; the skill itself is a workflow
  contract rather than a code dependency.

## Direction Tags

`3d` / `dev-workflow`
