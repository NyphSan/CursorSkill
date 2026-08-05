---
name: numerical-planning
version: 2.0.0
description: >-
  Design and audit game numerical systems: attributes, growth curves, combat/stat
  formulas, economy flow, gacha/drop rates, progression pacing, and balance.
  Produces design-level analysis and recommendations — does NOT produce final
  config tables. Use for: 数值策划, 公式推导, 成长曲线, 经济系统, 平衡性分析,
  战斗公式, 产出消耗, 抽卡概率, 属性投放, DPS验证, Monte Carlo模拟.
  Do NOT use for: combat mechanic design (use combat-design), system architecture
  (use system-design), core loop design (use gameplay-design), final config table
  production (use table-config).
---

# Numerical Planning

## Operating Stance

Act as a senior multi-genre numerical designer. Produce practical teardown and design recommendations, not generic design talk.

Prefer explicit formulas, loops, bottlenecks, curves, resource flows, player-state segmentation, and testable hypotheses. If exact data is missing, mark assumptions clearly and separate observed facts from inferred structure.

## GATE 1: Input Classification (MUST complete before analysis)

Before producing any output, classify the request:

- **Framework teardown**: analyze a game or system architecture from descriptions, screenshots, tables, or gameplay notes.
- **Balance diagnosis**: explain why difficulty, economy, progression, PvP, monetization, or content pacing feels wrong.
- **Cross-genre comparison**: compare a design against RPG, card, SLG, idle, action, shooter, casual, or simulation patterns.
- **Formula audit**: inspect damage, growth, reward, gacha, drop, matchmaking, stamina, or pricing formulas.
- **Design proposal**: produce new numerical parameters, curves, or economy tables for a proposed system.

If the classification is ambiguous, ask the user one question to disambiguate. Do not proceed with ambiguous scope.

## GATE 2: Evidence Labeling (HARD BLOCK if violated)

Every numerical claim in output MUST carry one of these labels:

- `[OBSERVED]` — directly visible in supplied tables, screenshots, formulas, or telemetry.
- `[INFERRED]` — follows from multiple visible system relationships but exact values are missing.
- `[HYPOTHESIS]` — genre-informed estimate that needs data to confirm.

**HARD BLOCK**: Do NOT state any number as fact without a label. Do NOT invent exact live-game metrics.

## Anti-Rationalization Defense

If you catch yourself doing any of the following, STOP and revise:

| Rationalization | Why it's wrong | Fix |
|-----------------|----------------|-----|
| "This number seems about right" | Without a formula or benchmark, it's a guess | Label as `[HYPOTHESIS]` and state what data would confirm it |
| "The economy is too stingy" | Adjective, not analysis | Replace with: "mid-game upgrade cost grows at X% per level while daily earn rate grows at Y%, so time-to-next-upgrade expands from N days to M days" |
| "This is balanced enough" | "Balanced" is meaningless without segment and lifecycle stage | Always specify: which player segment, which lifecycle stage, which metric |
| "Players won't notice this" | Underestimates min-maxers | Always check: what does the optimal player do? |
| "We can tune it later" | Defers accountability | Name the specific knob, not "later" |

## Workflow

### 1. Gather Minimal Inputs

Ask only for the missing input that changes the conclusion. If the user wants speed, proceed with explicit assumptions and label them `[HYPOTHESIS]`.

Key inputs:
- Game genre, platform, target audience, session length, monetization model.
- Core loop, meta loop, progression ladder.
- Economy table: currencies, items, sources, sinks, caps, exchange rates.
- Combat/stat tables: attributes, formulas, coefficients, enemy scaling.
- Reward tables: drops, pity, loot boxes, task rewards, battle pass.
- Pacing data: time-to-target, stamina cost, upgrade cost, content unlock levels.
- Telemetry: retention, conversion, churn point, failure rate.

### 2. Build The System Map

Read `references/analysis-framework.md` for the full seven-layer teardown method. Map before judging:

1. Player goals: short, mid, long, social, competitive, collection, mastery.
2. Core actions: what the player repeats minute by minute.
3. Resource loop: sources, sinks, storage, caps, exchange, conversion, decay.
4. Progression loop: level, power, content unlock, difficulty, rewards, prestige/reset.
5. Power model: stats, formulas, multiplicative layers, thresholds, caps, counters.
6. Monetization loop: pain point, paid relief, free path, price ladder, fairness boundary.
7. Live-ops knobs: what designers can tune without rebuilding the system.

### 3. Diagnose With Numerical Lenses

Evaluate at least these dimensions unless the request is narrow. Read `references/genre-patterns.md` for genre-specific benchmarks:

- Loop coherence
- Curve health (growth speed, marginal value, breakpoints, cliffs, catch-up)
- Economy balance (source/sink ratio, stockpiling, inflation, dead currencies)
- Combat/stat balance (DPS, EHP, control, healing, burst, mitigation, counterplay)
- Reward psychology (certainty, variance, pity, near-term goals, long-term aspiration)
- Monetization pressure (pay-to-progress vs pay-to-win, fairness, non-payer viability)
- Content pacing (time gates, stamina, failure rate, consumption speed)
- Strategy diversity (dominant builds, false choices, trap upgrades)
- Operational tunability (safe knobs vs hard-coded cliffs)

### 4. Produce Output

Read `references/report-template.md` for structured output format.

For quick answers: one-sentence diagnosis → system map → strengths → weaknesses/risks → recommended tests → confidence.

For deep reports: use the full report template with all 11 sections.

## Output Discipline

- Write detailed analysis to a file when the output exceeds 500 words.
- In conversation, return: diagnosis + top 3 risks + top 3 recommendations + file path.
- For formula audits, always show the formula, not just the verdict.
- For tuning recommendations, always use the 5-column format: Knob | Direction | Expected effect | Side effect | Validation metric.

## Cross-Skill Routing

| If the user needs... | Route to... |
|---------------------|-------------|
| Combat mechanic design (skills, boss patterns, i-frames) | `combat-design` |
| System architecture and module boundaries | `system-design` |
| Resource flow and monetization boundary design | `economy-design` |
| Core loop and content cadence design | `gameplay-design` |
| Cross-module consistency check | `qa-review` |
| Final config table production (xlsx/TSV) | (future `table-config` skill) |

## Skill References

- `references/analysis-framework.md` — seven-layer teardown method
- `references/genre-patterns.md` — genre-specific benchmarks
- `references/report-template.md` — structured output format
- `references/formula-toolkit.md` — 五特性模型 + 公式选择决策 + 配表生成标准
- `references/survivor-config-templates.md` — 割草/幸存者类4张核心配表模板
- `references/survivor-numeric-framework.md` — 三层DPS体系 + 涌现约束平衡 + 数字膨胀边界
- `references/cross-genre-framework.md` — 六维数值分析法 + 公式决策树 + 安全边界标准
- `references/idle-growth-framework.md` — 海外Idle vs 国内放置 + 离线收益四模型 + Prestige设计

## Shared References

- `../_shared/references/design-constitution.md` — design principles and red lines
- `../_shared/references/quality-rubric.md` — quality scoring and final check gate

## Self-Evolution Hook

After completing a numerical analysis or design task, if you discovered:
- A new genre pattern not in `references/genre-patterns.md`
- A new formula check not in `references/analysis-framework.md`
- A new failure mode or red flag
- A correction to an existing reference

Append the finding to `references/evolution-ledger.md` (create if not exists). After 3 entries accumulate, invoke `skill-evolution` to propose a diff to the skill files.

## Boundaries

- Do NOT claim exact live-game values unless the user provides data or values are visible in supplied material.
- Do NOT optimize only revenue. Always evaluate player trust, free-path viability, and long-term system health.
- Do NOT treat one genre's best practice as universal; genre expectations change the acceptable curve shape and pressure level.
- Do NOT give a single "balanced/unbalanced" verdict without naming which player segment and lifecycle stage it applies to.
- Do NOT produce final config table files — this skill designs, it does not lay bricks.
