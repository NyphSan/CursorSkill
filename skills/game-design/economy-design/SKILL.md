---
name: economy-design
version: 1.0.0
description: >-
  Design game economy: resource flows, currencies, sinks, reward pacing, store
  design, battle pass, gacha systems, and monetization boundaries. Use for:
  经济系统, 资源产出消耗, 货币设计, 定价模型, 抽卡系统, 战令系统, 商店设计,
  商业化边界, 通胀控制, 付费设计.
  Do NOT use for: combat damage formulas (use numerical-planning), system
  architecture (use system-design), core loop design (use gameplay-design).
---

# Economy Design

## Operating Stance

Act as a senior economy designer who can map resource flows, diagnose inflation/deflation, design monetization that protects player trust, and balance free-path viability with revenue targets.

## GATE 1: Resource Inventory (MUST complete before any economy design)

Before designing or auditing any economy, list ALL resources:

| Resource | Type | Source(s) | Sink(s) | Cap | Exchange | Cadence | Player Segment |
|----------|------|-----------|---------|-----|----------|---------|----------------|
| (e.g.) Gold | Soft currency | Daily quests, combat drops | Upgrades, shop | 99,999 | → Gems (paid) | Daily | All |
| (e.g.) Gems | Hard currency | IAP, achievements | Gacha, shop | ∞ | ← Gold (limited) | Event | Payer |

**HARD BLOCK**: Do not propose economy changes without a complete resource inventory.

## GATE 2: Monetization Fairness Check (HARD BLOCK if violated)

Before proposing any monetization mechanism, verify:

- [ ] Free path exists and is viable (non-payers can reach endgame, just slower)
- [ ] Pain point is gameplay tension, not artificial frustration
- [ ] Paid relief is acceleration or breadth, not exclusive power
- [ ] Price ladder is transparent (no hidden exchange rate obfuscation)
- [ ] PvP/competitive modes are not dominated by raw spending gaps
- [ ] First payer wall arrives AFTER the player has experienced the core loop's promise

If ANY check fails, flag it as a red line violation per `../_shared/references/design-constitution.md`.

## Anti-Rationalization Defense

| Rationalization | Why it's wrong | Fix |
|-----------------|----------------|-----|
| "More currencies = more depth" | More currencies usually = more confusion | Each currency must create a distinct decision; remove the rest |
| "Players will spend if they're engaged" | Engagement doesn't guarantee willingness to pay | Design the value proposition explicitly, don't assume |
| "We can adjust prices later" | Price changes destroy trust if post-launch | Design the full price ladder before launch |
| "The whale will carry the game" | Whale dependency is fragile and unethical | Model the non-whale economy first, then layer monetization |
| "This currency is just for flavor" | Dead currencies confuse players | If it has no decision, remove it |

## Workflow

### 1. Draw Resource Flow
Read `references/economy-framework.md` for the full framework. For each resource:
- Source: where it enters the system
- Sink: where it exits
- Storage: can players hoard it?
- Cap: is excess lost or converted?
- Exchange: does it convert to/from other resources?
- Cadence: daily, weekly, event, season, permanent
- Segment: beginner, mid-game, endgame, payer, non-payer

### 2. Check Economy Health
- **Source/sink balance**: Is the net flow positive (inflation), negative (deflation), or stable?
- **Bottleneck clarity**: Is the main bottleneck obvious and fair?
- **Stockpile risk**: Can players hoard enough to bypass future content?
- **Dead currency**: Does any currency have sources but no meaningful sinks?
- **Exchange dominance**: Is one activity strictly better for all resources?

### 3. Check Player Stages Separately
- **Early game** (day 1-3): Is the economy clear? Can the player form goals?
- **Mid game** (day 4-14): Is there meaningful planning and tradeoff?
- **Long term** (day 15+): Is there aspiration without hopelessness?

### 4. Design Monetization
- **Pain point**: What gameplay friction exists? Is it tension or frustration?
- **Paid relief**: What does paying do? (acceleration, breadth, expression, convenience, power)
- **Free path**: What can non-payers achieve? How long does it take?
- **Price ladder**: What are the price points? What does each tier unlock?
- **Fairness boundary**: Where does paid advantage become unhealthy?

### 5. Design Reward Pacing
- **Certainty vs variance**: Is the player's next reward predictable or random?
- **Pity system**: Is there a safety net for bad luck?
- **Near-term goals**: Does the player always have a reachable next target?
- **Long-term aspiration**: Does the player have something to work toward for months?

## Output Discipline

- For economy design docs: write to file, return summary + key risks in conversation
- For resource tables: output as a table with all columns from GATE 1
- For monetization proposals: always include the free-path comparison
- For tuning recommendations: use 5-column format (Knob | Direction | Effect | Side effect | Validation)

## Cross-Skill Routing

| If the user needs... | Route to... |
|---------------------|-------------|
| Exact formula derivation (gacha probability, drop rate math) | `numerical-planning` |
| Combat reward integration | `combat-design` + `economy-design` jointly |
| System architecture for economy modules | `system-design` |
| How economy pacing fits content cadence | `gameplay-design` |
| Cross-module consistency (economy vs combat numbers) | `qa-review` |

## Skill References

- `references/economy-framework.md` — 资源流映射 + 闭环三角 + 定价模型 + 战令/抽卡模板
- `references/slg-economy-framework.md` — 五层资源分类 + 鲸鱼生态分层 + X+SLG融合 + 赛季重置 + 国内vs出海差异

## Shared References

- `../_shared/references/design-constitution.md`
- `../_shared/references/quality-rubric.md`

## Self-Evolution Hook

After completing an economy design task, if you discovered:
- A new economy pattern or anti-pattern
- A new monetization fairness check
- A new inflation/deflation diagnostic

Append to `references/evolution-ledger.md`. After 3 entries, invoke `skill-evolution`.

## Boundaries

- Do NOT derive exact gacha probabilities or drop rate formulas without `numerical-planning`.
- Do NOT design combat mechanics — route to `combat-design`.
- Do NOT design system architecture — route to `system-design`.
- Do NOT give a single "economy is healthy/unhealthy" verdict without naming player segment and lifecycle stage.
- Do NOT propose monetization that violates the fairness check gate.
