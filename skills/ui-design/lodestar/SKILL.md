---
name: lodestar
description: Evidence-graded behavioral design for generating and critiquing apps, websites, and funnels. Use when designing or reviewing onboarding, activation, retention, engagement loops, habit/streak mechanics, gamification, paywalls, pricing pages, landing pages, checkout, or conversion flows — or when asked to make a product "sticky", improve retention/activation metrics, or apply psychology to UI. Includes lifecycle benchmarks, tactic→UI translation, and a dark-pattern refusal policy.
---

# Lodestar — Evidence-Graded Behavioral Design for Apps & Web

Design products around what users *feel* and *return for*, not just what they complete — using named, citable mechanisms instead of copied screenshots, with honest evidence grading and hard ethical limits.

## Core workflow (every generation or critique)

1. **Diagnose before designing.** Identify the lifecycle bottleneck stage first (see router below). Never optimize a screen without naming which stage metric it serves.
2. **Pick tactics from the library** — [references/tactic-library.md](references/tactic-library.md). Name each tactic, its mechanism, and its evidence grade. Never invent unnamed "psychology".
3. **Translate to concrete UI** — [references/ui-translation.md](references/ui-translation.md): components, layout, microcopy, motion. A tactic without a UI spec is not a deliverable.
4. **Attach a benchmark expectation** when making any performance claim — [references/benchmarks.md](references/benchmarks.md). Never quote a number that isn't there.
5. **Run the SDT check** — [references/motivation-science.md](references/motivation-science.md): does this support autonomy, competence, relatedness — or thwart them? Prefer intrinsic-motivation language ("support competence") over pop framing ("hack dopamine").
6. **Run the dark-pattern refusal table** — [references/dark-patterns.md](references/dark-patterns.md). Refuse or hard-flag anything on it.
7. **Label evidence strength** on every tactic you recommend: **Strong** (replicated/meta-analyzed), **Moderate** (single studies, large industry data, HCI laws), **Folklore** (practitioner heuristics — usable, but say so).

## Stage router

| Bottleneck symptom | Stage | Primary tactic families | Key benchmark anchor |
|---|---|---|---|
| Users sign up but never reach value | **Onboarding** | Reduction, tunnelling, chunking, defaults, personalization quiz, empty states, lazy registration | Avg activation 34% / median 25% (Lenny) |
| Users try it once, no "aha" | **Activation** | Time-to-value compression, endowed progress, IKEA effect, deferred signup, aha-moment design | D7 return ≥7% ≈ top quartile (Amplitude) |
| Users don't come back | **Retention & Habit** | Triggers, streaks (with repair), implementation intentions, variable reward (ethics-gated), investment loops, fresh start effect | Social: D1/D7/D30 60/40/25 = good (a16z) |
| Sessions are shallow | **Engagement** | Flow/appropriate challenge, feedback loops, curiosity gaps, peak-end design, delighters | DAU/MAU 40% = good (a16z) |
| Free users never pay | **Monetization** | Paywall placement, trial design, anchoring, decoy, loss framing, zero-price bias | Hard paywall 10.7% vs freemium 2.1% D35 download→paid (RevenueCat) |
| No organic growth | **Growth / Referral** | Social proof (true), reciprocity, status, self-expression, dynamic norms | MoM growth 35% = good at seed (a16z) |
| Visitors don't trust or convert | **Trust & Web Conversion** | Authority, testimonials (true), aesthetic-usability, above-fold hierarchy, form reduction | ~70% cart abandonment; ~35% CR headroom (Baymard) |

For web/landing/checkout specifics use [references/web-cro.md](references/web-cro.md).

## Output format for recommendations

Emit each recommendation as a tactic card:

```
TACTIC: <name from library>
MECHANISM: <psychological mechanism> [Evidence: Strong|Moderate|Folklore]
STAGE: <lifecycle stage> — targets <metric>
UI SPEC: <component / layout / microcopy / motion>
ADAPT: <how to fit this product's users and context>
PAIRS WITH: <related tactics>
GUARDRAIL: <backfire risk + ethical check result>
```

## Hard rules

- **Never fabricate** scarcity, urgency, activity counts, testimonials, or reviews — real numbers only, or don't use the tactic.
- **Refusal list is binding**: roach motel, forced continuity, hidden costs, confirmshaming, fake social proof, sneak-into-basket, preselection against user interest, disguised ads, cost-obscuring token currencies, variable-reward loops without exit points. See [references/dark-patterns.md](references/dark-patterns.md).
- **Nudges are not guaranteed wins**: choice architecture averages d≈0.45 with ~15% of interventions backfiring (Mertens et al., PNAS 2021). Recommend A/B validation for any high-stakes change.
- **Streaks and loss mechanics** must ship with repair/freeze paths — streak loss is a documented churn trigger, not just a motivator.
- **Octalysis drives 6–8** (scarcity, unpredictability, loss) require an explicit ethics note whenever used; default to drives 1–5.
- When the product's mission is wellbeing (health, mindfulness, kids), bias strongly toward SDT-supportive mechanics and against compulsion loops entirely.
