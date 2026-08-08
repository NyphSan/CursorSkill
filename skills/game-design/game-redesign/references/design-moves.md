---
module: design-moves
status: "Claude-authored fill-in (2026-07-07) — replaceable by curated content"
sources: "Matrix/layer moves derive from the curated interaction-structure.md §2 and systemic-levers.md (read from the installed game-analysis skill); engine amplifiers cite MDA (Hunicke, LeBlanc & Zubek 2004), Koster (2004), Csikszentmihalyi (1990), Ryan & Deci; wildcard patterns are Claude-authored."
---

# Design Moves — catalog for Steps 3–5

Entry format: **what it does → when to reach for it → how to theory-test it
→ cost & failure mode.** Cite the entry you use in each proposal's
rationale. Family 3 entries use **Moves / Test / Failure mode** — their
"when to reach for it" is the engine being amplified. Moves compose — say
so when a proposal uses two. Theory
references live in the installed game-analysis skill
(`~/.claude/skills/game-analysis/references/`).

## Family 1 — Matrix moves

### Add node
Introduces a new option wired into the interaction chart.
- **When:** doom-stacks with no counter; stale or solved matchup space; a
  role the roster cannot express.
- **Test:** before/after script runs; the new chart must add no dominated
  nodes; state the doom-stack delta explicitly.
- **Cost:** +1 option pool (Query 1 check mandatory). Failure mode:
  mis-wired edges create new doom-stacks — the script, not intuition,
  decides.

### Rewire edges
Changes who-beats-whom without growing the roster.
- **When:** a dominated node exists; a doom-stack is fixable by flipping or
  adding one edge; centrality spread is too wide (one node's viability
  dwarfs the rest).
- **Test:** before/after script runs; no new dominated nodes; the targeted
  pathology must be gone in the after-run.
- **Cost:** zero option-pool growth. Failure mode: breaks learned matchups
  (mastery churn), and an edge with no thematic justification reads as
  arbitrary.

### Densify neutrals
Converts neutral matchups into win/loss edges, moving toward a tournament.
- **When:** neutral matchups let players opt out of the mind-game by locking
  into no-counterplay engagements.
- **Test:** script confirms `Tournament: yes`, cycle structure retained
  (still INTRANSITIVE), no dominated nodes introduced.
- **Cost:** more edges to learn. Failure mode: some neutrals are deliberate
  safe-engagement valves or mercy states — check intent before removing.

### Sparsify / add ties
Deliberately introduces neutral matchups or tie outcomes.
- **When:** every engagement is lethal and play is exhausting; the design
  needs tempo breathers or mercy states.
- **Test:** script run on the sparser chart; confirm no node becomes
  dominant because its bad matchups turned neutral.
- **Cost:** each neutral removes a prediction stake. Failure mode: too many
  neutrals collapse the prediction burden entirely.

### 2-Paradox expansion
Grows the roster to ≥ 7 nodes wired so every two-node subset has a counter
(interaction-structure.md §2.5; Query 4: 7 nodes is the proven minimum).
- **When:** pair-based doom-stacks are the core pathology and roster growth
  is acceptable.
- **Test:** the script MUST print
  `size 2: none — the 2-Paradox property holds.`
  and `Dominated nodes: none`. No exceptions.
- **Cost:** option pool → 7+, near the cognitive-load ceiling (Query 1).
  Failure mode: shipping the expansion all at once — mitigate with Subset
  rotation or act-based escalation (§2.5).

### Subset rotation
Rotates which nodes are legal (seasons, acts, ban phases) over a larger
designed pool.
- **When:** the meta is solved but there is no budget for new content; the
  load ceiling is reached but freshness is needed.
- **Test:** run the script on EACH rotated subset — a subset of a healthy
  chart can contain dominance or doom-stacks the full chart lacks.
- **Cost:** invalidates some mastery each rotation. Failure mode: rotation
  cadence faster than players re-learn.

## Family 2 — Layer moves

### Iteration
Multi-round structure: best-of-N, sets, carry-over stakes
(interaction-structure.md §2.1).
- **When:** single-shot outcomes feel like coin flips; no behavioral data
  accumulates for reads.
- **Test:** theory anchor §2.1 (chance → pattern recognition); engine delta
  must show Prediction loop / Pattern mastery strengthened.
- **Cost:** session length. Failure mode: early-round results dominating
  (front-loaded variance).

### Resource scarcity
Limited hand or limited uses per node (interaction-structure.md §2.2).
- **When:** choices feel weightless; no state persists between rounds.
- **Test:** theory anchor §2.2 (state-dependent economic weighting); note
  the shift from stateless to tracked-state play.
- **Cost:** memory/bookkeeping load. Failure mode: the last forced move
  ("only Rock left") removing the decision entirely.

### Spatial projection
Projects the interaction web onto a grid or board
(interaction-structure.md §2.3).
- **When:** the game resolves instantly and feels flat; the design wants a
  Positional-planning engine.
- **Test:** theory anchor §2.3 (prediction horizon shifts to positioning);
  engine table gains Positional planning with its sustain conditions met
  (consequential space, tempo limits).
- **Cost:** large scope (board, movement, range rules) and real load
  growth. Failure mode: cosmetic space — positioning that changes nothing;
  identity bend large enough that this is often wildcard-adjacent.

### Information structure
Hides or reveals state: fog of war, hidden picks, simultaneous commitment,
bluff windows (systemic-levers.md "Information structure";
interaction-structure.md §1.2).
- **When:** a sequential game is solved by calculation; bluff bandwidth is
  starved; per fun-engines.md's genre-fit check, only when the game intends
  a read at all.
- **Test:** theory anchor (hidden info as the sequential-play substitute for
  simultaneity); engine delta on Prediction loop.
- **Cost:** trust in randomness drops when outcomes hide too long. Failure
  mode: over-hiding → decisions feel like coin flips; mandatory scouting
  chores.

### Tempo / action economy
Limits actions, movement, or time: AP budgets, movement points, timers
(systemic-levers.md "Pacing"; interaction-structure.md §2.2 spirit).
- **When:** the right answer is always reachable, so sequencing is never a
  decision.
- **Test:** theory anchor; engine delta on Positional planning (reaching
  the matchup becomes a live decision).
- **Cost:** rules overhead. Failure mode: budgets so tight play becomes
  fiddly micro-optimization.

## Family 3 — Engine amplifiers

### Amplify: Prediction loop
(fun-engines.md "Prediction loop"; interaction-structure.md §1)
- **Moves:** widen bluff bandwidth (table talk, feints, declared partial
  information); iterated stakes (carry-over between rounds so reads
  compound); mixed-value outcomes (some wins worth more — skews frequency
  bias and deepens reads).
- **Test:** sustain/kill delta table; the loop's pillars (simultaneity or
  hidden info, balanced web, small pool) must remain intact.
- **Failure mode:** bluffing drowns system mastery; stakes so high that
  losses read as unfair.

### Amplify: Positional planning
(fun-engines.md "Positional planning"; interaction-structure.md §2.3, §3.2)
- **Moves:** terrain asymmetry (chokepoints, high ground, cover); objective
  placement that forces rotations; vision/tempo interplay (what you can see
  vs how fast you can react).
- **Test:** sustain/kill delta; verify the matrix is deep enough that
  position matters (a shallow matrix voids this engine — check the audit's
  matrix findings first).
- **Failure mode:** solvable maps; positioning with no consequence.

### Amplify: Pattern mastery
(fun-engines.md "Pattern mastery"; Koster 2004)
- **Moves:** layered reveals (new interactions unlock as mastery grows);
  content rotation; composition depth (few pieces, many combinations).
- **Test:** sustain/kill delta; confirm output randomness stays low enough
  that the skill signal survives.
- **Failure mode:** noise swamping the pattern; option bloat past Query 1.

### Amplify: Flow
(fun-engines.md "Flow"; Csikszentmihalyi 1990)
- **Moves:** difficulty that tracks skill (dynamic ramps tied to
  performance, not time); tighter feedback loops (instant resolution,
  juice); state readability passes.
- **Test:** sustain/kill delta; the challenge≈skill channel must hold at
  both ends (novice and expert).
- **Failure mode:** spikes/plateaus; dynamic difficulty perceived as
  cheating when visible.

### Amplify: Self-determination
(fun-engines.md "Self-determination"; Ryan & Deci)
- **Moves:** build variety with ENFORCED viability — when a matrix exists,
  check centrality spread via the script (near-uniform = healthy autonomy;
  a dominant build is the math smell of illusory choice); visible growth
  ladders; expressive optional techniques.
- **Test:** sustain/kill delta + script centrality section when applicable.
- **Failure mode:** illusory choice (one true build); pay-to-skip
  competence.

### Amplify: Fellowship
(MDA aesthetics table in fun-engines.md; Hunicke, LeBlanc & Zubek 2004)
- **Moves:** role interdependence (asymmetric abilities that must combine);
  shared stakes and rituals (team wagers, the countdown); communication
  channels as mechanics (restricted signaling, table talk windows).
- **Test:** sustain/kill delta; check the interdependence is mechanical,
  not just thematic. Derive Fellowship's per-game sustains/kills from the
  MDA row (fun-engines.md defines no engine section for it).
- **Failure mode:** forced socialization; kingmaking (systemic-levers.md
  "Trader" warning).

## Family 4 — Wildcard patterns

Identity-stretching by definition: each bends a pillar (who decides, when
resolution happens, what is hidden, or whether an interaction core exists).
Wildcards obey every standing rule, including theory-test.

### Resolution-timing bend
Flips sequential ↔ simultaneous (e.g., simultaneous programmed turns in a
turn-based tactics game).
- **When:** the audit shows calculation has replaced prediction, and
  information moves alone are too weak.
- **Test:** engine deltas (Prediction loop gains its simultaneity pillar;
  Positional planning shifts from reactive to committed). If the change
  alters effective matchups (initiative removal), re-run the script on the
  effective chart.
- **Cost:** deep identity bend; execution/UI complexity (plan-then-reveal).

### Information bend
Changes WHAT is hidden: hidden win conditions, secret roles, revealed
hands, delayed reveals.
- **When:** the read is stale — everyone knows what everyone wants.
- **Test:** anchor to the Information structure move + engine deltas;
  state what new question the hidden thing makes players ask.
- **Cost:** trust and kingmaking dynamics; new-player confusion.

### Agency bend
Changes WHO decides: draft your opponent's options, bid for turn order,
program moves in advance, vote on rules.
- **When:** choices are solitary and opponents are scenery; the audit
  flags dead interactivity.
- **Test:** engine deltas (Fellowship/Prediction); if it changes effective
  matchup frequencies (e.g., opponents assemble your hand), run the script
  on the effective chart.
- **Cost:** the deepest identity bend; analysis burden shifts onto players.

### Introduce-a-matrix
Adds an interaction core to a matrix-less game (e.g., piece-vs-piece
interactions in a puzzle game; typed attacks in a racer).
- **When:** the audit marks the matrix N/A AND an engine gap exists that
  counterplay would fill (usually Prediction or Positional planning).
- **Test:** the NEW chart must be script-run: intransitive by design, no
  dominated nodes; state the doom-stack profile honestly (small charts
  fail 2-Paradox by construction — say so and justify the node count).
- **Cost:** changes the game's §2 typology row by row — the biggest scope
  in this catalog. Failure mode: the new core strangles the engines that
  already worked (run the cross-engine damage line with extra care).
