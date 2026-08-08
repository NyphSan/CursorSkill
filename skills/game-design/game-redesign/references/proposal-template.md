---
module: proposal-template
status: "Output contract for Step 6"
---

# Game Redesign Proposal — Template

Follow the section order exactly; mark inapplicable parts
**"N/A — <one line why>"**. The document header carries the label:
**theory-consistent, not play-tested.**

## 1. Design brief (echo)
Identity pillars (from audit §2 + §4) · targets (findings + engines) ·
directive as parsed (quote the user's words, then your parse of boldness
and direction) · cognitive-load posture. If this section is wrong,
everything after it is aimed wrong — the user should be able to correct it
at a glance before reading a single proposal.

## 2. Portfolio
| # | Proposal | Move (design-moves entry) | Targets | Boldness |
|---|----------|---------------------------|---------|----------|

One row per proposal. Boldness ∈ identity-preserving ·
bent (directive-authorized) · **[Wildcard — identity-stretching]** ·
pivot (directive-authorized).

## 3. Proposals (one subsection each)
Per proposal, in this order:
- **Mechanic spec** — implementable rules text: what a designer would
  build, precise enough to prototype from.
- **Rationale** — the audit finding(s) and/or engine(s) addressed, cited
  by name (standing rule 1), and the design-moves entry used.
- **Theory-test evidence** — script output verbatim (with a before/after
  delta table when the audit has a current matrix) and/or the layer-move
  theory anchor (standing rule 4).
- **Engine deltas** — per affected engine: sustains added/removed, kills
  added/removed, predicted health change.
- **Costs** — cognitive-load delta (option counts before → after, Query 1
  verdict) · engines this proposal could damage · implementation scope
  (S/M/L).
- **Identity check** — per pillar: preserved / bent / broken + one line.

## 4. Recommendation & sequencing
Which proposal to pursue first and why. Which proposals compound. Which
conflict — never recommend two that fight over the same engine.

## 5. Re-audit handoff (Path-B spec)
The recommended proposal rendered as a self-contained design spec an
auditor can read cold: node set and full interaction chart (if any), rules
text, economy touches, information structure. Close with, verbatim:

> To validate independently, run the game-analysis skill against this
> section in a fresh session, and compare its findings with the audit that
> seeded this redesign.

## 6. Assumptions & open questions
Uncertainties, directive interpretations you chose, and anything only a
playtest can answer — name what the playtest would measure.
