---
name: nvidia-omniverse-cad-to-simready
description: >
  Coordinate the end-to-end NVIDIA Omniverse CAD-to-SimReady pipeline: take a source CAD or mesh
  asset, convert to USD, assign Content Agents materials/physics/texture, run SimReady profile
  conformance, validate, render with OVRTX, and (optionally) assemble a SimReady package. Use
  when the request names "CAD to SimReady", "source asset to simulation-ready USD", "SimReady
  package", "SimReady conformance", or wants to feed a digital-twin / robot / autonomous-sim
  pipeline. Targets Linux/macOS hosts with Docker + NVIDIA Container Toolkit + a GPU.
---

# NVIDIA Omniverse — CAD to SimReady

End-to-end orchestrator that turns a source CAD or mesh asset into a SimReady USD (and optional
package) suitable for physics simulation, robotics training, and digital-twin runtimes. Comes
from `NVIDIA/skills` and coordinates existing NVIDIA stage references; it does NOT replace them
with one monolithic runner. Adapted excerpt for the gamedev / 3D-pipeline direction.

## When to use

- Broad "CAD to SimReady" / "source asset to SimReady USD" / "SimReady package" requests.
- Pipelines that feed USD into UE 5.2+ (UE imports USD natively) or NVIDIA Isaac Sim / Omniverse.
- When material / physics / sensor properties must be authored on the asset, not just visual.

**When *not* to use:**

- Conversion-only, validation-only, or packaging-only — use the matching stage reference
  directly (`convert-to-usd`, `validate-usd-minimum`, `assemble-package-source`).
- Just visual USD (no physics / no SimReady conformance) — use `dcc-mcp-blender` or
  `unreal-blueprints` import workflow instead.

## Prerequisites

- Python 3.12 + `uv` (per upstream `README.md`).
- Docker, NVIDIA Container Toolkit, NVIDIA GPU for Content Agents + OVRTX stages.
- A Content Agents model-provider key matching the selected backend
  (`NVIDIA_API_KEY` / `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` / `GOOGLE_API_KEY` / `GEMINI_API_KEY`)
  **OR** explicit endpoint + usage-token env vars for already-running endpoints.
- Local upstream checkouts under
  `${OMNIVERSE_CAD_TO_SIMREADY_UPSTREAM_ROOT:-$HOME/.omniverse-cad-to-simready/upstreams}`
  when a stage needs upstream scripts or specs.

## Default intent (always ask before overriding)

- `property_assignment_intent=run` — the default for any broad end-to-end request. Deploys
  Content Agents (Material → Physics → optional Texture), then conformance.
- `property_assignment_intent=skip` — only for **conversion-only** or **validation-only**;
  do not deploy Content Agents; just run `convert-to-usd` and (if conversion succeeded)
  `validate-usd-minimum`.

## Hard rules (excerpt from upstream)

1. **Run `preflight` first.** Writes `cad-to-simready-preflight.json` and exports
   `PHYSICAL_AI_PREFLIGHT_MANIFEST` + `PHYSICAL_AI_REQUIRE_PREFLIGHT=1`. Treat as dependency
   bootstrap, not workflow routing. Use `--skip-content-agents` for conversion-only /
   validation-only requests.
2. **Content Agents gate.** When `property_assignment_intent=run`, verify or deploy Content
   Agents services **before** any asset-context inspection, conversion, validation,
   conformance, rendering, packaging, or upstream source build. Block on missing auth or
   unhealthy services — never continue past it. Treat explicitly provided healthy endpoints
   as user-owned; otherwise `deploy-content-agents` runs the OVRTX renderer first, then
   Material / Physics / optional Texture services in order.
3. **Validation policy.** Only `validate-usd-minimum` is allowed **before** Content Agents
   (it is a basic USD viability check). Never run `simready-conform-profile`, `simready-validate`,
   or any FET helper before Content Agents when property assignment will run.
4. **Stage references only.** No single `omniverse-cad-to-simready` runner. Invoke each
   stage reference's installed script directly.
5. **Source conversion** delegates to `convert-to-usd`; do not substitute another converter
   for CAD or mesh formats.
6. **Property assignment** runs Content Agents references as **separate atomic steps**:
   material first, then physics, then texture only when requested.
7. **Stop at the first failing** deployment / conversion / property-assignment / conformance
   gate unless the user explicitly asks for best-effort continuation. After a meaningful
   artifact exists, do not stop at validation findings — continue the remaining diagnostic
   gates and mark the result `needs_rerun`.
8. **`GSP.001` profile failure is never the end.** Route it to
   `simready-foundation-conform-fet-005-simulate-grasp-physics`; if the agent cannot inspect
   renders or no explicit grasp points are available, report a blocked FET005 repair with
   the visual evidence path or missing-input reason.

## Workflow (14-step summary)

1. Confirm source asset path exists, resolve `output_root`, classify request as end-to-end,
   conversion-only, validation-only, or packaging.
2. Resolve `property_assignment_intent` (default `run`).
3. Run `preflight` for the selected workflow targets, source the env file, treat as setup only.
4. **If `property_assignment_intent=run`** → verify or deploy Content Agents first.
5. Read `references/workflow.md` + `references/commands.md`, then run only the stage references
   the current request actually needs.
6. `identify-asset-context` on the original source (when web search is available, or property
   assignment will run).
7. Route the source through `convert-to-usd`. Skip for existing USD input.
8. `validate-usd-minimum` as a viability gate only — record `metersPerUnit != 1.0` etc., do
   not run profile / FET repairs yet.
9. Content Agents material → physics → optional texture assignment (when `property_assignment_intent=run`).
10. `simready-conform-profile` on the latest simulation USD path after property assignment;
    preserve every selected FET repair report.
11. Run validation gates in order: `omni-asset-validate` → `omni-asset-validate-geometry` →
    `omni-asset-validate-physics` → `simready-validate`.
12. If `simready-validate` reports a repairable requirement, rerun `simready-conform-profile`,
    then rerun profile validation on the newest authored USD.
13. `ovrtx-render-service` when preview / thumbnail / inspection images are requested. For
    package outputs, run `assemble-package-source` (creates the clean `deliverable/` package
    source from final USD + thumbnail), then `nv-core-package-sample` +
    `nv-core-package-sample-validation` on the deliverable folder only.
14. Emit a consolidated workflow report (status = `passed` / `blocked` / `failed` / `needs_rerun`).
    See `references/workflow.md` for the required Markdown and JSON report fields.

## Output

Markdown consolidated report **plus** JSON when the workflow writes structured artifacts.
Always include:

- Final USD path.
- All stage reports.
- Validation findings + rerun reasons.
- `next_steps` for unfinished work.

## Detailed references (read on demand)

- `references/preflight/README.md` — deterministic local setup, manifest / env contract.
- `references/workflow.md` — inputs, source routing, validation policy, output report fields.
- `references/commands.md` — portable script command patterns.
- `references/assemble-package-source/README.md` — two-zone package source assembly.
- `references/troubleshooting.md` — symptom / cause / fix table plus FET (`GSP.001` / `RB.MB.001`)
  repair-routing detail.
- `references/publishing-layout.md` — frontmatter compatibility-field notes for this skill's
  own file tree.

## Why this matters for game / UE pipelines

- **UE 5.2+ imports USD natively** (`Datasmith USD` / `Interchange USD`). A SimReady USD can
  be dropped straight into a UE project as a simulation-ready prop with material / physics /
  collision already assigned — saving the manual `UPhysicalMaterial` / `UStaticMesh` collider
  authoring pass.
- Content Agents material + physics assignment uses LLM-driven property inference from the
  asset's part naming, so props get believable density / friction / restitution without a
  human in the loop.
- OVRTX preview lets you visually verify the SimReady output before committing to a UE import
  pass — catches wrong scale / wrong up-axis early.
- The validation gate chain (`omni-asset-validate*` → `simready-validate`) is the same shape
  UE-side users would build by hand with `UAutomationTest`; importing a pre-validated SimReady
  asset shifts that work upstream.

## Limitations

- Linux / macOS only.
- Requires a GPU + Docker + Content Agents runtime (NVIDIA_API_KEY or compatible).
- This workflow **coordinates** existing conversion, property assignment, conformance,
  validation, rendering, and packaging skills; it does **not** replace them with a single
  monolithic runner command.
