---
module: systemic-levers
status: "Claude-authored fill-in (2026-07-06) — replaceable by curated content"
sources: "Adams & Dormans, Game Mechanics: Advanced Game Design (Machinations); Engelstein & Shalev, Building Blocks of Tabletop Game Design; flow/difficulty literature"
---

# Systemic Levers — catalog for Steps 6–7

Format per lever: **what it does → when to pull it → failure modes.**
The seven interaction-core levers live in `interaction-structure.md` §2
(iteration, resource scarcity, spatial projection, asymmetry, 2-Paradox,
option-pool size, matrix density) — cross-reference them, never duplicate.

## Economy levers *(Machinations vocabulary — Adams & Dormans)*

- **Source (faucet):** injects a resource over time or on triggers. Pull when
  rewards feel scarce or progress stalls. Fails as inflation — abundant
  resources trivialize decisions.
- **Sink (drain):** removes resources (costs, decay, taxes). Pull when
  hoarding or inflation appears. Fails when it feels punitive and players
  stop experimenting.
- **Converter:** transforms resource A into B. Pull to add routing decisions.
  Fails when chains get so long that value becomes opaque.
- **Trader:** exchanges between players. Pull to feed fellowship/negotiation
  engines. Fails as kingmaking or market cornering.

**Diagnostics:** estimate a session's net faucet-minus-drain per resource —
monotonic growth means inflation; check whether late-game decisions still
spend anything meaningful.

## Feedback loops

- **Positive (snowball):** winning accelerates winning. Pull when games
  should end decisively and comebacks feel fake. Fails as runaway leader —
  everyone else is a spectator by mid-game.
- **Negative (rubber-band):** losing grants help. Pull in social/party games
  to keep the table tense. Fails when winning feels punished and sandbagging
  becomes optimal.

**Diagnostics:** from a small early lead, trace the loop — does the gap
self-amplify or self-correct? Is the optimal strategy to *look* like you're
losing?

## Randomness placement *(Engelstein)*

- **Input randomness** (randomize, then decide — card draw before your turn):
  creates fresh puzzles, preserves agency. Pull for pattern-mastery and flow
  engines.
- **Output randomness** (decide, then randomize — attack roll after
  commitment): creates drama and variance. Pull for tension spikes and
  underdog wins.

**Failure modes:** output randomness on high-stakes irreversible decisions
reads as unfair; zero randomness in symmetric games produces solved openings.

## Information structure

- **Hidden information** (fog of war, hands, secret roles): restores a
  prediction burden in sequential games — the sequential-play substitute for
  simultaneity (interaction-structure.md §1.2). Pull when a sequential game
  feels deterministic or solvable. Fails when so much is hidden that
  decisions feel like coin flips, or scouting becomes a mandatory chore.
- **Bluff bandwidth:** how much out-of-band signaling the rules permit. Pull
  when a prediction engine exists but starves. Fails when bluffing dominates
  system mastery entirely.

## Progression & difficulty

- **Curves and gates:** pace new mechanics and stats against expected skill.
  Pull at flow breaks (spikes, plateaus). Fails as time-gated walls
  (competence killed) or power creep flattening old content into a stat
  check (transitive collapse — interaction-structure.md §3.1).
- **Escalation scaling:** subset the interaction network act-by-act — one
  element → 3-node triangle → 7-node 2-Paradox
  (interaction-structure.md §2.5).

## Pacing

- **Decision density:** meaningful choices per minute. Pull when players
  report downtime. Fails as relentless density → fatigue.
- **Session shape:** opening/midgame/endgame arc. Classic failure: endgames
  that drag after the outcome is decided (cross-ref positive feedback).

## Choosing levers (Step 7 discipline)

1. Smallest lever that addresses the diagnosis.
2. State the predicted systemic effect — mirror the curated lever → effect
   format of interaction-structure.md §2.
3. State the cost: cognitive-load delta (standing rule 4), implementation
   scope, and which fun engine the lever might damage.
