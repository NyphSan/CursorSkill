---
name: nvidia-simready-foundation-conform-fet-000-core
description: |
  Repair an existing USD asset so it passes the SimReady Foundation FET000_CORE
  feature contract: naming, asset layout, unresolved paths, and undefined prim
  failures. Stages a repaired copy without silently mutating the source asset.
version: "2026.06.0"
license: Apache-2.0
metadata:
  author: Shaad Boochoon (NVIDIA)
  source: https://github.com/nvidia/simready-foundation/tree/main/skills/simready-foundation-conform-fet-000-core
  tags:
    - simready
    - usd
    - conformance
    - core
    - 3d
    - workflow
---

# NVIDIA SimReady Foundation — Conform FET-000 Core

## Purpose

Bring an existing USD-family asset into conformance with the SimReady Core
feature contract, then hand the repaired copy back to profile validation.

This skill does **not** act as the final validator and must not silently mutate
source assets. It stages a repaired asset under the requested output directory,
applies deterministic fixes only where safe, and stops when a validation gate
still fails or a manual decision is required.

## When to Use

- "Fix SimReady Core failures on this USD asset"
- "Repair naming/path/metadata issues so the asset passes FET000_CORE"
- "Stage a conformant copy of a CAD/DCC-converted USD asset"
- "Clean up unresolved references and undefined prims before packaging"

## Inputs

| Input | Requirement |
|---|---|
| `usd_asset` | Required `.usd`, `.usda`, `.usdc`, or unpacked USD-family asset. |
| `output_root` | Required or inferred folder for staged assets and reports. |
| `simready_profile` | Profile being validated, e.g. `prop-robotics-neutral`. |
| `profile_version` | Profile version, if supplied. |
| `validation_report` | Preferred JSON/markdown report from the failing gate. |
| `source_asset` | Original CAD, DCC, URDF, MJCF, or conversion input path. |
| `asset_name` / `asset_type` | Explicit user values, or infer conservative defaults. |

## Source of Truth

Before editing, load the selected FET000_CORE manifest:

- `nv_core/sr_specs/docs/features/FET_000_base_neutral-0.1.0-core.json`
- `nv_core/sr_specs/docs/features/FET_000-base_neutral-0.1.0-core.md`

Treat the JSON requirement list as authoritative when markdown and JSON
disagree.

## Repair Checklist

1. Confirm the input asset exists and record the original path.
2. Parse the validation report when available; otherwise run the narrowest
   available FET000_CORE validation gate first.
3. Filter to FET000_CORE failures and requirement IDs only.
4. Create a staged output folder under `output_root` with safe lowercase paths.
5. Copy/export the input asset into the staged folder. Do not overwrite source.
6. Apply fixes in order:
   - Path and layout fixes for `NP.002`, `NP.003`, `NP.004`, `NP.005`.
   - Metadata fixes for `NP.006` and `SR.001` (prefer
     `apply-simready-foundation-metadata` when available).
   - Composition and asset path fixes for `NP.007`, `NP.008`.
   - Undefined prim cleanup for `HI.010` only when the over can be safely
     resolved or removed.
7. Rerun the same validation gate.
8. Summarize as `passed`, `failed`, `skipped`, or `blocked`.

## Mechanical Repairs Allowed

- Rename copied files/folders to satisfy Core naming rules.
- Place the main USD file at `asset_root/<intermediate>/<asset_file>.usd*`.
- Author `customLayerData['SimReady_Metadata']` with `asset_name`,
  `asset_type`, `source_file`, and `usd_date_generated`.
- Rewrite absolute asset paths to relative paths only when the referenced file
  exists inside the staged asset root or can be safely copied there.

## Block and Report Instead of Guessing

- Required dependency cannot be found.
- Path points outside the asset package and copying would change ownership or
  licensing assumptions.
- Undefined prim might be a legitimate composition override.
- Metadata values would require domain knowledge the user did not provide.
- Repairing one requirement would invalidate a higher-priority profile
  requirement.

## Summary Format

| Field | Meaning |
|---|---|
| `input_usd_path` | Original USD path. |
| `output_usd_path` | Latest staged/repaired USD path. |
| `profile` / `profile_version` | Validation target. |
| `requirements_repaired` | Requirement IDs changed by this skill. |
| `requirements_blocked` | Requirement IDs that need user or upstream data. |
| `validation_report` | Path to the rerun validation report. |
| `next_step` | Usually rerun the full selected profile validation. |

## Notes for UE/Game Teams

SimReady Core conformance is an upstream cleanup step before USD enters a game
engine. Use this skill after CAD → USD conversion and before UE 5.2+ Interchange
USD import to avoid broken references, naming conflicts, and missing metadata in
engine. It is not an engine-specific skill; it standardizes the USD payload.
