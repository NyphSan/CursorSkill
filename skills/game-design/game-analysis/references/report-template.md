---
module: report-template
status: "Output contract for Step 8"
---

# Game Analysis Report — Template

Use the full template for audits and provided material; the condensed variant
for casual asks (standing rule 5). Mark inapplicable sections
**"N/A — <one line why>"**. Never drop a section silently.

## 1. Game snapshot
Title / working name · intake path (A recall-and-verify / B read-and-extract)
· material examined · 2–3 line confidence statement.

## 2. Typology
| Axis | Verdict | Evidence |
|------|---------|----------|
| Transitive / intransitive | | |
| Simultaneous / sequential | | |
| Symmetric / asymmetric | | |
| Spatial / abstract | | |
| Dense / sparse matrix | | |

Close with a one-line genre framing implied by the axes.

## 3. Systems map
Core loop (bullet chain) · node set · interaction matrix (table, or
"no matrix — <why>") · economy flows (sources → converters → sinks) ·
progression gates.

## 4. Fun engines
Ranked. Per engine: **Engine — framework — evidence — sustains — kills —
health** (healthy / at risk / broken + one line).

## 5. Diagnosis
Present findings **grouped by layer** in this fixed order (standing rule 1 —
matrix first), and **within each layer order by severity**, tagging every
finding with an explicit severity (Critical / High / Medium / Low). Layer tags:
- **[Matrix]** — computed by matrix_analysis.py; cite its output verbatim (or
  "N/A — no interaction matrix" and skip the script).
- **[Spatial] / [Tempo] / [Information]** — declared-layer findings.
- **[Systemic]** — economy, feedback loops, difficulty, cognitive load.

Keep **live issues** (things that actually hurt play) separate from
**structural notes** — observations that are true but inert (e.g. a doom-stack
that can never be fielded) or process/discipline cautions. Put structural notes
in a short tail; a structural note must never outrank a live issue. (Do not
label the section "severity-ordered" — it is layer-grouped, severity within.)

## 6. Improvement levers
Per finding: **lever → predicted systemic effect → risk/cost** (including
cognitive-load delta). Prefer the smallest sufficient lever.

## 7. Assumptions & open questions
Everything uncertain, unverified, or deliberately out of scope.

---

## Condensed variant (~1 page)
§1 in two lines · §2 table only · §4 top two engines · §5 top three findings
· §6 top three levers · close by offering the full audit.

---

## Worked micro-example (non-matrix game): Tetris

**1. Snapshot:** Tetris (1985+, falling-block puzzle). Path A. High
confidence — rules fully public.
**2. Typology:** no node-vs-node interaction matrix → transitivity N/A —
single-player vs. system; sequential (piece by piece); asymmetric
(player vs. generator); spatial (grid); matrix N/A. Framing: solo
spatial-arrangement puzzle under time pressure.
**3. Systems map:** loop = preview next piece → place piece → clear lines →
speed rises. No matrix — the only "opponent" is the piece generator.
Economy: board space is the scarce resource; line clears are the sink that
reclaims it. Progression gate: gravity speed per level.
**4. Fun engines:** Pattern mastery (Koster) — healthy: piece/stack patterns
deepen for years. Flow (Csikszentmihalyi) — healthy: speed curve tracks
skill; instant feedback. Challenge (MDA) — healthy: survival + score
ceilings.
**5. Diagnosis:** [Systemic] pre-7-bag randomizers could starve I-pieces —
output-flavored randomness injecting unfair droughts. [Systemic] fixed speed
curve eventually outruns human input — intentional ceiling, but kills flow
for elite players (kill-screen).
**6. Levers:** randomness placement → 7-bag input randomness (guaranteed
piece distribution per 14) — predicted effect: droughts bounded, planning
horizon restored; cost: none to cognitive load, slight drama loss. Difficulty
gate → marathon caps / infinite modes — predicted effect: flow preserved for
non-elite play; cost: none.
**7. Assumptions:** modern guideline Tetris (hold piece, 7-bag) unless the
user specifies a classic variant.
