---
module: fun-engines
status: "Claude-authored fill-in (2026-07-06) — replaceable by curated content"
sources: "MDA (Hunicke, LeBlanc & Zubek 2004); Koster, A Theory of Fun (2004); Csikszentmihalyi, Flow (1990); Ryan & Deci, Self-Determination Theory"
---

# Fun Engines — taxonomy for Step 5

A game usually runs 2–3 dominant engines, not one. For each engine present:
name it, cite its framework, and state what sustains and what kills it in
THIS game.

## How to use

1. Scan the eight MDA aesthetics below as a checklist; shortlist the ones the
   game plausibly serves.
2. For each shortlisted engine, find the mechanical evidence — which system
   produces it.
3. Rank engines by how much of the play time they explain.
4. Record each engine's sustain and kill conditions — these feed Step 6.

**Genre-fit check (do this before rating the Prediction loop):** decide whether
the game even *intends* a simultaneous opponent-read. If it is sequential +
spatial by genre (chess, tactics, RTS, 4X), it runs **Positional planning**,
not a broken Prediction loop — see both engines below. Absence of simultaneity
there is N/A by genre, not a defect.

## The eight MDA aesthetics (Hunicke, LeBlanc & Zubek, 2004)

MDA: Mechanics generate Dynamics generate Aesthetics; designers build M→A,
players experience A→M.

| Aesthetic | Game as... | Presence signals |
|-----------|------------|------------------|
| Challenge | obstacle course | win/loss states, skill ceilings, ranked play |
| Discovery | uncharted territory | maps, secrets, tech trees, unknown interactions |
| Fantasy | make-believe | roles, avatars, simulated professions |
| Narrative | drama | authored story, character arcs, dramatic pacing |
| Fellowship | social framework | co-op, guilds, trading, table talk |
| Expression | self-discovery | building, customization, style |
| Sensation | sense-pleasure | audiovisual juice, music sync, tactile feedback |
| Submission | pastime | low-stakes loops, grinding, idle systems |

## Engine: Prediction loop *(curated — interaction-structure.md §1)*

The challenge/competition branch: psychological friction of anticipating an
opponent inside a constrained, balanced, simultaneous system.

- **Sustains:** balanced intransitive network; small option pool; behavioral
  data accumulating across iterations; out-of-band manipulation (bluffing,
  rhetoric, tells).
- **Kills:** a dominant strategy (matrix solved); option-pool bloat past
  cognitive load (interaction-structure.md, Query 1); broken simultaneity
  (turn order leaks intent — interaction-structure.md §1.2).
- **Genre note — do not rate a sequential game's prediction loop "broken."**
  A game that is sequential + spatial *by genre* (chess, Fire Emblem, HoMM,
  Total War) is not a failed simultaneous game — it runs **Positional planning**
  (below) instead, and its lack of simultaneity is **N/A by genre, not a
  defect.** Rate this engine "broken" only when a game *intends* a simultaneous
  read and leaks it. Keep two questions apart: (1) is the simultaneous loop even
  the intended engine? — if not, it is N/A; (2) is the intended engine (often
  positional planning) starved by a shallow matrix? — that is the ratable
  problem.

## Engine: Positional planning *(curated — interaction-structure.md §2.3, §3.2)*

The sequential + spatial substitute for the simultaneous read: prediction
shifts from "what will they throw?" to "how will the board evolve over the next
several turns?" — terrain control, movement vectors, multi-unit synergy, long
planning trees. This is how an intransitive counter-web is enriched on a grid.

- **Sustains:** a matrix rich enough that positioning has real consequences;
  meaningful space (flanking, range, chokepoints); tempo / action-economy limits
  that make *reaching* the right matchup a live decision (interaction-structure.md
  §2.3).
- **Kills:** a matrix so shallow the board is solvable regardless of position
  (the planning tree collapses to one line); perfect information *combined with*
  a trivial matrix (nothing left to compute); positioning with no real
  consequence (space is cosmetic). Note: perfect information alone is **not** a
  kill — chess is fully observable and deep; depth comes from the planning tree.

## Engine: Pattern mastery *(Koster, A Theory of Fun, 2004)*

Fun is the brain consuming learnable patterns; mastery feels good; full
mastery is boredom.

- **Sustains:** fresh patterns at the edge of competence (new compositions,
  new tile shapes, new interactions); depth that reveals layers over time.
- **Kills:** solved patterns (stale meta — dovetails with the prediction
  loop's kill condition); patterns too noisy to learn (output randomness
  swamping skill signal).

## Engine: Flow *(Csikszentmihalyi, 1990)*

Sustained engagement needs challenge ≈ skill, clear goals, immediate
feedback.

- **Sustains:** difficulty that tracks skill growth; readable game state;
  short feedback loops.
- **Kills:** difficulty spikes (anxiety) or plateaus (boredom); muddy
  feedback; interruptions that break the loop.

## Engine: Self-determination *(Ryan & Deci)*

Autonomy (meaningful choice), competence (visible growth), relatedness
(mattering to others).

- **Sustains:** build variety with genuinely viable alternatives (autonomy);
  progression and skill expression (competence); co-op, guilds, social
  identity (relatedness).
- **Kills:** illusory choice — one true build (cross-ref: dominated nodes);
  pay-to-skip competence; dead multiplayer spaces.

## Reporting format (feeds report §4)

Per engine, one block:
**Engine — framework — evidence (mechanic) — sustains — kills — health**
(healthy / at risk / broken, one line why).
