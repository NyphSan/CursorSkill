---
name: nvidia-omniverse-usd-performance-tuning
description: >
  Top-level NVIDIA Omniverse USD performance-diagnosis and optimization workflow. Run when an
  Omniverse / USD scene exhibits slow loading, low FPS, high memory, GPU device-lost, or
  broad "optimize this stage" requests. Authored by NVIDIA Omniverse (v0.1.0); orchestrates
  usd-structure-assessment, usd-validation-runner, usd-optimize-run-{validators,operations},
  profile-stage:{baseline,after}, compare-profiles, optimization-report. Delegates auth and
  runtime setup to Phase 0 owners.
---

# NVIDIA Omniverse — USD Performance Tuning

End-to-end orchestrator for USD performance diagnosis and optimization, authored by NVIDIA
Omniverse. Treats slow loading, low FPS / interactivity, high GPU / system memory, GPU crash
or device-lost, validation failures, and CAD / conversion-quality triage as one routing
problem. Adapted excerpt of `NVIDIA/skills` v0.1.0 for the 3D-performance direction.

## When to use

- Slow USD scene loading, low FPS / interactivity, high GPU or system memory, GPU device-lost.
- Validation failures or CAD / conversion-quality issues.
- Broad "optimize this stage" / "profile this USD scene" / "shrink memory" requests.

**When *not* to use:**

- Pure visual / non-USD scenes — see `dcc-mcp-blender` or `unreal-blueprints` workflows.
- Single-shot `decimateMeshes` with explicit `mm_tolerance` already given — the narrow
  `usd-optimize-run-operations` reference is enough; do NOT enter the broad workflow.

## Mandatory session-start gate

Before any tuning output **except** a static classification-only answer, follow
`references/setup-usd-performance-tuning/references/runtime-context-header.md`. That reference
owns `output_path`, `setup-preflight.json`, Format A / Format B, and forbids silent ad hoc
probing.

Behavior:

- **Missing / unreadable preflight** → invoke `setup-usd-performance-tuning`.
- **Present preflight** → print Format A and wait for Continue / Change Kit / Switch to
  standalone / Re-run probe.
- **Runtime already confirmed this session** → use compact Format B:
  `[Kit: {runtime_context.kit.application} {runtime_context.kit.version} | SO: {runtime_context.usdOptimize.version} | AV: {runtime_context.assetValidator.version}]`
- **`omniverse://` assets** → route through `omniverse-authentication` before setup, triage,
  or first open.
- **Standalone / usd-optimize packages** → runtime evidence must include package / sentinel
  checks **plus** shared-library or import / load verification, not just the Python executable
  / version.

## Entry-skill and decision rules

- **Name `omniverse-usd-performance-tuning` as the entry** whenever any runtime path is
  verified (Kit, standalone, or partial stack such as usd-validation-nvidia only). If the
  requested tool / operation is missing, return the specific blocker code such as
  `blocked_missing_usd_optimize` or `blocked_missing_usd_optimize_operation` — **do NOT
  substitute a different workflow**.
- **Name `setup-usd-performance-tuning` as entry** only when no runtime path is verified and
  runtime choice / setup is the first unresolved problem.
- This is **ownership, not phase order**: auth, setup, and triage still run in their normal
  order.

## Canonical plan contract

Broad optimization must:

- Start milestone lists with `omniverse-usd-performance-tuning`; include
  `setup-usd-performance-tuning` only as Phase 0 context when relevant.
- Set top-level `decision` to `ready_to_plan` for generic optimization.
- Include the chain through `optimization-report` in both `committed_milestones` and
  `planned_phases`.
- Use exact profile labels `profile-stage:baseline` and `profile-stage:after`; never emit
  bare `profile-stage`.
- Preserve this exact subsequence (optional analysis only where it does NOT reorder):

  `omniverse-usd-performance-tuning` → `profile-stage:baseline` → `usd-structure-assessment`
  → `usd-validation-runner` → `restructure-decision` → `apply-restructure` →
  `usd-optimize-run-validators` → `usd-optimize-interpret-validators` →
  `usd-optimize-run-operations` → `profile-stage:after` → `compare-profiles` →
  `optimization-report`

**Conditionally required milestones** — only when their trigger holds:

- `usd-hierarchy-dedupe-candidates` → after `usd-structure-assessment`, before
  `restructure-decision`, whenever the stage shows repeated copied hierarchy, high mesh
  count with little or no instancing, or a monolithic root. Do NOT conclude
  `hierarchy_dedupe.recommended: false` without it.
- `usd-edit-target-planner` → after `apply-restructure`, before the Usd Optimize
  validator / operations chain, whenever the stage is composed (references or payloads).

Default to **three scoped iterations** unless the user opts out, asks for a quick pass, or
stop criteria apply. Each iteration writes an interim report; later passes reuse prior
evidence instead of restarting the full workflow.

## Decision fields (`decision`)

- `ready_to_plan` — default for generic optimization. Nothing in this response awaits the
  user; `committed_milestones` equals `planned_phases`. Includes a proactive
  `auto-within-tolerance` bounded-loss pass.
- `approval_required` — this response halts at a gate it is surfacing now; `committed_milestones`
  is a strict prefix of `planned_phases`, and `approval_required_reason` names the gate.
  Triggered by an unresolved decision, NOT by destructive-intent — bounded-loss ops above
  the conservative band or on functional-precision targets become **inline-elicited**.
- `blocked` — a `blocked_code` applies.
- Future gates that genuinely fire later belong in `gates_observed`, never in `decision`.

## Mutation / operation rules

Invariants (prototypes first → per-asset validation → stage-level operations last):

- Always run composition audit before mutation.
- Validate before and after processor execution.
- Optimize prototypes before per-asset validation.
- Check hierarchy-level reuse before whole-stage mesh dedupe on very large CAD scenes.
- Base recommendations on bottleneck evidence — do NOT recommend fixed stacks without findings.
- Do NOT authorize mutation when writes are not allowed.

**Usd Optimize curation:**

- Prefer `canonical` operations from `references/operations/operations.json`.
- Vertex welding → prefer canonical `meshCleanup` with explicit flags over standalone
  `mergeVertices`; follow upstream mechanics and local approval policy.
- Hierarchy dedupe → prefer `usd-hierarchy-dedupe-candidates` + `apply-restructure` (owns the
  manifest / identity contract); standalone approved-chain dedup drives `deduplicateHierarchies`
  per frontier region (`paths` + per-region `maxDepth`).
- Per-mesh dedupe → prefer canonical `deduplicateGeometry`; `findCoincidingGeometry` is
  analysis-only.
- Do NOT agent-initiate `documentary` ops (`boxClip`, `deletePrims`, `removeAttributes`,
  `removeUntypedPrims`, broad `merge`) except its narrow non-instanced case, unless
  explicitly requested.
- `specialty` operations are OK when validator evidence wires them into the interpret step or
  downstream context requires them (`sparseMeshes`, `optimizePrimvars`, `primitivesToMeshes`,
  `utilityFunction`, `pythonScript` recipes).

## Routing map

| Concern | Route to |
|---|---|
| Composition / structure / layer health / instancing readiness | `usd-structure-assessment` |
| Validation / content issues | `usd-validation-runner` → `validate-*` or Usd Optimize validators |
| Edit target, variant, payload, output decisions | `usd-edit-target-planner` |
| Repeated copied hierarchy / high mesh count no instancing | `usd-hierarchy-dedupe-candidates` |
| Monolithic stage / asset-boundary materialization | `restructure-decision` → `apply-restructure` |
| CAD converter settings | `references/cad-conversion/README.md` |
| Usd Optimize execution | `usd-optimize-run-validators` / `...-interpret-validators` / `...-run-operations` |
| Full Kit runtime profiling (FPS, frame time, Hydra/RTX) | external NVIDIA / omniperf skills |

## Deliverables

End-to-end optimization produces an **optimized USD stage** when mutation runs and an
`optimization-report`. Diagnosis-only work ends with a report or summary stating no
optimized stage was written.

- Structured JSON must conform to `optimization-report`'s
  `scripts/optimization-report.schema.json`.
- Save the generated Markdown summary.
- Render HTML from `references/report-templates/optimization-report.html.template` via
  `render_preview.py`; never hand-write HTML.

Final runtime response must explicitly name:

- Selected entry skill + selected runtime / preflight state, including standalone package
  sentinel / load evidence.
- Optimized USD output path when written, or "no mutation ran".
- Source-not-overwritten / in-place mutation status.
- Exact operation chain executed, especially safe / lossless chains.
- Before / after validation and profile metrics from evidence.
- Validated report JSON, generated Markdown, rendered HTML, schema verdict, score (if any),
  and `workflow_mode`.

If preflight is missing, validation / rendering failed, or no mutation ran — say so plainly;
do NOT replace missing artifacts with a chat-only recap.

## Why this matters for game / UE pipelines

- **UE 5.2+ USD import** in production projects (e.g. automotive configurators, arch-viz,
  factory simulation, large-scale sandbox games) often pulls in USD assemblies that balloon
  in size once instancing collapses. The Usd Optimize validation + decimation chain is the
  upstream fix that imports a smaller, valid USD into UE — saving downstream frame stalls and
  draw-call explosion.
- The **prototype-first → per-asset → stage-level** ordering maps directly onto UE's own
  guidelines (whitebox prototype → per-mesh asset polish → lighting / VFX pass). Frame the
  automation in matching terms when handing off.
- **`profile-stage:baseline` → `profile-stage:after` → `compare-profiles`** mirrors Unreal
  Insights' `Trace` + frame delta workflow — engineers familiar with Insights grasp the
  profile model instantly.
- `blocked_*` codes (e.g. `blocked_missing_usd_optimize`) are first-class error shapes — use
  them to surface missing-runtime risk to the user before spending GPU time.

## Limitations

- Does NOT install runtimes, replace downstream reference instructions, authenticate remote
  assets itself, approve unrequested destructive writes, or guarantee performance gains
  without evidence.
- If runtime status is unclear → return to the setup gate.
- If mutation appears before evidence → return to baseline profiling + composition audit.

## Detailed references (read on demand)

- `references/workflow.md` — Phase 0-7 flow, Kit / standalone branches, validator routing,
  operation ordering, termination criteria, default three-pass pattern.
- `references/runtime-artifact-token-budget.md` — bounded metadata for Kit logs, validation
  CSVs, Tracy CSVs.
- `references/skill-map.md` — full routing graph.
- `references/usd-structure-assessment/references/optimization-tradeoffs.md` — per-pipeline
  phase tradeoffs.
- `references/usd-structure-assessment/references/factory-level-structuring.md` — factory
  structuring.
- `references/usd-structure-assessment/references/composition-audit.md`.
- `references/usd-validation-runner/README.md`.
- `references/optimization-report/references/optimization-report-template.md`.
- `references/upstreams/usd-optimize.md`.
