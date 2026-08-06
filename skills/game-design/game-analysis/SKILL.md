---
name: game-analysis
description: Break down any game's design — typology, fun engines, balance
  diagnosis, improvement levers. Use when the user asks to analyze, break down,
  or audit a game or its mechanics/systems/balance; asks what makes a game fun,
  what type of game it is, or how to improve it. Works for published titles by
  name and for the user's own designs (GDD, rules text, prototype code).
---

# Game Systems Analysis

Break a game down into its systems, classify it, locate its fun engines,
diagnose weaknesses, and propose improvement levers. Follow the 8 steps in
order; read each reference file at the step that needs it, not before.

## Standing rules (apply to every step)

1. **Matrix before narrative.** Diagnose the pure interaction matrix first.
   Any claim that relies on space, tempo, or information dynamics must declare
   that layer explicitly ("at the spatial layer: ...").
2. **Attribute every framework claim** — cite the reference file section
   (curated methodology) or the named canonical source (fill-in modules).
3. **Assumptions are visible.** Uncertain facts about the game go in the
   report's Assumptions section — never silently resolved.
4. **Cognitive-load budget.** Lever proposals must state their option-pool
   impact; hyper-scaling destroys prediction loops
   (references/interaction-structure.md, Query 1).
5. **Scale depth to the ask.** Casual question → condensed report (~1 page)
   plus an offer to go deep. Explicit audit request or provided material →
   full template.

## Procedure

### Step 1 — Intake

Decide the path:

- **Path A — published title.** Enumerate the game's systems from your
  knowledge. Mark every fact you are not certain of. Verify uncertain,
  load-bearing facts (ask the user, or web-search if available); park the rest
  in Assumptions. If the title is obscure, ask for material or proceed with
  explicit low-confidence flags.
- **Path B — user material.** Read the provided GDD/rules text. For code:
  search for type charts, damage/effectiveness tables, unit/element enums,
  combat-resolution functions, and state machines. Reconstruct the node set
  and interaction rules from what you find. Ambiguities: ask, or list as
  assumptions.

Output of this step: a systems inventory — core loop candidates, entities,
resources, information structure.

### Step 2 — Decompose  *(read references/analysis-workflow.md, Phase 1)*

Isolate the core loop(s). Strip entities to base nodes — no stats, no health
bars, no secondary effects.

### Step 3 — Map  *(references/analysis-workflow.md, Phase 2)*

Where node-vs-node interactions exist, build the win/loss/neutral matrix (or
effectiveness multipliers). Also map economy flows (sources → converters →
sinks) and progression gates. If no interaction matrix exists, say so and
continue — Steps 5–7 carry the analysis.

### Step 4 — Classify  *(references/interaction-structure.md, §3)*

Place the game on the axes: transitive/intransitive · simultaneous/sequential
· symmetric/asymmetric · spatial/abstract · dense/sparse matrix. State the
genre framing this typology implies.

### Step 5 — Locate the fun engines  *(references/fun-engines.md)*

Identify which engagement engines the game runs (usually 2–3 dominant). For
each: what sustains it, what kills it. The prediction engine
(references/interaction-structure.md §1) is one branch.

### Step 6 — Diagnose  *(references/systemic-levers.md for pathology checklists)*

a. **Matrix layer:** if a matrix was extracted in Step 3, write it to a
   scratch JSON file (`{"nodes": [...], "matrix": [[...]]}`) and run:

   `python3 <skill-dir>/scripts/matrix_analysis.py matrix.json --max-stack 2`

   Encode weighted charts NON-NEGATIVELY (points scored, effectiveness
   multipliers — never a signed zero-sum differential): the script skips
   viability scores on negative-valued matrices, and signed encodings can
   invert what centrality means. Use its findings verbatim: dominated nodes,
   unbeatable pairs (doom-stacks), transitivity verdict, viability scores.
   Treat centrality as a raw-payoff heuristic, not play-rate — when exact
   strategy shares matter, derive the equilibrium mix separately.
b. **Declared layers:** re-examine matrix findings under spatial / tempo /
   information dynamics, labeling each layer explicitly.
c. **Non-matrix pathologies:** economy inflation, runaway feedback loops,
   difficulty spikes or flow breaks, cognitive overload, solved patterns.

Order findings by severity.

### Step 7 — Propose levers  *(references/systemic-levers.md; references/interaction-structure.md §2)*

For each diagnosis: lever → predicted systemic effect → risk/cost (including
cognitive-load impact). Prefer the smallest lever that fixes the diagnosis.

### Step 8 — Report  *(references/report-template.md)*

Render the report per the template — full or condensed per standing rule 5.
Mark inapplicable sections "N/A" with one line of reasoning; never silently
drop them.
