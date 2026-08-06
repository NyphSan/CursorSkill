---
name: game-redesign
description: Turn a game-analysis audit into bold, theory-tested redesign
  proposals — new mechanics, matrix changes, fun-engine amplification. Use when
  the user asks to redesign, evolve, or reimagine a game, wants new mechanic
  ideas beyond minimal fixes ("make it more fun", "propose a new mechanic",
  "what should I do about this audit"), or points at a game-analysis report
  and asks to act on it. Requires the game-analysis skill installed.
---

# Game Redesign

Turn a completed game-analysis audit into a portfolio of bold, theory-tested
redesign proposals, then hand the result back for an independent re-audit.
You are the designer counterpart to the game-analysis auditor: the auditor
proposes the smallest sufficient lever; you propose mechanic-level changes —
kept honest by mandatory theory-testing and the fresh-eyes audit loop.

## Step 0 — Dependency check

Verify `~/.claude/skills/game-analysis/` contains `SKILL.md`,
`references/interaction-structure.md`, `references/fun-engines.md`,
`references/systemic-levers.md`, and `scripts/matrix_analysis.py`.
If anything is missing, STOP and tell the user: "This skill requires the
game-analysis skill installed at ~/.claude/skills/game-analysis."
Read theory from those files at the step that needs them; never copy them.

## Standing rules (apply to every step)

1. **Grounded.** Every proposal cites the specific audit finding and/or fun
   engine it addresses. No untargeted ideas.
2. **Identity default + one wildcard.** Unless the user's directive says
   otherwise, proposals preserve the game's identity pillars, plus exactly
   one clearly-labeled **[Wildcard — identity-stretching]** proposal. When
   the directive lifts the cap, still REPORT the identity check per proposal.
3. **Beyond the audit.** Never repropose the audit's §6 levers. If the audit
   already names the idea, go materially beyond it (the audit gestured at
   "expand to 7 nodes" → you deliver the wired 7-node chart, verified) or
   drop it.
4. **Theory-test mandatory.** Matrix claims are verified by actually running
   the dependency script and quoting its output verbatim; engine claims by
   sustain/kill delta tables. A proposal that fails or cannot be tested is
   revised or cut — never shipped untested.
5. **Cost everything.** Every proposal states its cognitive-load delta
   (option-pool before/after; interaction-structure.md, Query 1) and which
   fun engine it might damage.
6. **Attribute every framework claim** — curated reference sections, named
   canonical sources, or design-moves entries.
7. **Never self-certify.** Your output is theory-consistent, not verified
   fun. End with the fresh-session re-audit handoff; never claim the
   redesign is proven to work.

## Directive grammar (parse the user's brief before designing)

Two independent axes; both optional:

- **Boldness:** silence → default (2 identity-preserving + 1 wildcard).
  "go bigger" → up to 2 wildcards and pillar-bends allowed outside the
  wildcard slot (total count stays 3 unless a count is also requested;
  allowed range 2–5).
  "pivots allowed" / "full redesign" → identity cap removed entirely
  (identity checks still reported per proposal).
- **Direction:** silence → audit's top live findings + weakest engine.
  An engine name ("maximize Fellowship") → the portfolio must serve that
  engine. A finding ("fix the snowball") → the portfolio must address it.
  A mechanic ("add a 6th node") → at least one proposal implements it,
  theory-tested.

Contradictory directives ("keep it identical but revolutionize it") →
surface the tension and ask. Never silently resolve.

## Procedure

### Step 1 — Locate the audit

Priority: explicit path in the request → newest `*analysis*.md` or
`*audit*.md` in the working directory (confirm with the user it is the
intended audit) → none: run the game-analysis skill's procedure first
(condensed is acceptable), then continue here. If the user declines an
audit, decline to freestyle — the audit is your ground truth.

### Step 2 — Extract the design brief

From the audit:
- **Identity pillars** — the genre framing (audit §2) plus the top-ranked
  healthy engine(s) (audit §4 #1, and any engine the audit calls defining).
- **Targets** — audit §5 live findings at Critical/High severity (add
  Medium only if fewer than 2), plus engines rated at risk or broken.
- **Cognitive-load posture** — option-pool/load notes in audit §2/§5.

If the audit is condensed (no severity tags), use its top findings as-is
and note the reduced grounding in Assumptions.

From the user: the directive (grammar above). Echo the complete brief as §1
of your output so a mis-read brief is visible before any proposal is read.

### Step 3 — Select moves  *(read references/design-moves.md)*

Shortlist moves whose "when to reach for it" matches the targets. Note each
move's theory-test hook. Moves compose — say so when a proposal uses two.

### Step 4 — Generate the portfolio

Default exactly 3 proposals: 2 identity-preserving + 1 wildcard. Every
proposal is **mechanic-level** — a rule/system change a designer could
implement from your spec — and obeys standing rule 3. Matrix moves apply
only where the audit found an interaction core; for a matrix-less game,
matrix content is allowed only via the Introduce-a-matrix wildcard.

### Step 5 — Theory-test every proposal

- **Matrix moves:** write the proposed chart to a scratch JSON
  (`{"nodes": [...], "matrix": [[...]]}`) and run
  `python3 ~/.claude/skills/game-analysis/scripts/matrix_analysis.py chart.json --max-stack 2`.
  Encode weighted charts NON-NEGATIVELY (points scored, effectiveness
  multipliers — never a signed zero-sum differential): the script skips
  viability on negative-valued matrices. Quote verbatim: structure verdict,
  dominated nodes, doom-stacks, centrality. If the audit contains a current matrix, run BOTH charts and
  present a before/after delta table. Universal pass bar: **no new
  dominated nodes**. A 2-Paradox claim passes only when the script prints
  `size 2: none — the 2-Paradox property holds.`
- **Layer moves:** map the claimed effect to the documented systemic effect
  it cites (interaction-structure.md §2 / systemic-levers.md entry). A
  claim with no theory anchor fails.
- **Engine moves:** sustain/kill delta table per affected engine
  (fun-engines.md definitions) + a mandatory cross-engine damage line.
- **Every proposal:** cognitive-load delta (option counts before → after,
  Query 1 verdict) and a per-pillar identity check (preserved / bent /
  broken + one line).

### Step 6 — Write the redesign doc  *(references/proposal-template.md)*

Follow the template exactly; mark inapplicable parts "N/A — <one line why>".

### Step 7 — Hand off

Render the recommended proposal as a Path-B-ready spec (rules text an
auditor can read cold). End with the template §5 closing instruction,
verbatim. Label the whole document **theory-consistent, not play-tested**.
