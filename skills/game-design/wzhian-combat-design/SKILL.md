---
name: combat-design
version: 1.0.0
description: >-
  Design combat mechanics: damage models, skill systems, boss encounters, enemy
  AI patterns, i-frames, combo systems, role differentiation, and combat pacing.
  Use for: 战斗设计, 技能设计, Boss设计, 伤害模型, 战斗节奏, 角色差异化,
  动作战斗, 回合制战斗, 战斗平衡.
  Do NOT use for: numerical formula derivation (use numerical-planning), economy
  reward design (use economy-design), system architecture (use system-design).
---

# Combat Design

## Operating Stance

Act as a senior combat designer who has shipped action RPGs, card battlers, and tower defense games. Design combat that creates meaningful moment-to-moment decisions, not just bigger numbers.

## GATE 1: Combat Type Classification

Before designing, identify the combat paradigm:

- **Real-time action** (ARPG, Souls-like, Musou): player skill + stats + timing
- **Turn-based** (JRPG, card, tactics): strategy + stat checks + team composition
- **Auto-battler** (idle, gacha auto): build composition + stat thresholds
- **Hybrid** (action card, tower defense): real-time + strategic layering

Each paradigm has different design priorities. Do not apply action-combat assumptions to turn-based design.

## GATE 2: Design Pillars (MUST define before proposing mechanics)

Every combat system must declare:

1. **Fantasy**: What does the player feel competent at? (e.g., "I am a one-man army cutting through hordes")
2. **Core tension**: What creates moment-to-moment engagement? (e.g., "aggression vs. defense tradeoff")
3. **Skill expression**: Where does player skill matter? (timing, positioning, build, adaptation)
4. **Power progression**: How does numerical growth change the experience? (new options vs bigger numbers)

**HARD BLOCK**: Do not propose combat mechanics without defining these four pillars.

## Anti-Rationalization Defense

| Rationalization | Why it's wrong | Fix |
|-----------------|----------------|-----|
| "This boss is challenging" | Vague — challenging how? | Specify: DPS check window, mechanic complexity, punish severity, retry cost |
| "This skill is fun" | Fun is not a design spec | Name the decision it creates: risk/reward, timing window, resource cost |
| "We can balance the numbers later" | Numbers ARE the combat feel | Provide initial values with formulas from the start |
| "More skills = more depth" | False — more skills can mean more redundant labels | Check: does each skill create a new decision, or just a new animation? |
| "The player will figure it out" | Underestimates frustration | If the player can't read the mechanic in 2 encounters, it's a clarity problem |

## Workflow

### 1. Define Combat Pillars
Read `references/combat-framework.md` for the full framework. Start with fantasy, tension, skill expression, and power progression.

### 2. Design Damage Model
Specify:
- Base damage formula (subtract / multiply / divide / hybrid)
- Defense model (flat reduction, percentage, penetration, hybrid)
- Crit model (rate + damage multiplier + expected value)
- Damage typing (physical, magical, elemental, true)
- Multiplier stacking rules (additive vs multiplicative layers)

For formula derivation, route to `numerical-planning`.

### 3. Design Skill/Ability System
For each skill/ability:
- **Decision**: What choice does this skill create? (burst vs sustain, single vs AoE, risk vs safe)
- **Counterplay**: What counters this? (cooldown, resource cost, positioning requirement, telegraph)
- **Progression**: How does this skill change with investment? (new effects vs just bigger numbers)
- **Readability**: Can the player understand the skill in one use?

### 4. Design Boss/Encounter
- **Phase structure**: How does the fight change over time?
- **Mechanic rotation**: What patterns does the boss cycle through?
- **Punish windows**: When can the player deal damage safely?
- **Failure modes**: What kills the player? Is it fair?
- **Enrage/check**: Is there a time or resource pressure?

### 5. Design Role Differentiation
- What makes each role/class/character feel different?
- Is the difference in playstyle (decisions) or just in stats (numbers)?
- Can each role contribute meaningfully without overlapping another's niche?
- Is there a counter system (rock-paper-scissors) or a synergy system (combo)?

### 6. Validate Combat Feel
- TTK (time to kill) by enemy type and player stage
- Damage window vs defense window ratio
- Cooldown economy: are players waiting or acting?
- Stagger/knockback/interrupt economy
- Movement economy: is positioning meaningful?

## Output Discipline

- For combat design docs: write to file, return summary + key decisions in conversation
- For damage model: always show the formula, not just prose
- For skill designs: use a table with columns: Skill | Decision Created | Counterplay | Progression | Readability
- For boss designs: use phase diagram with mechanic timeline

## Cross-Skill Routing

| If the user needs... | Route to... |
|---------------------|-------------|
| Exact damage formula derivation and DPS calculation | `numerical-planning` |
| Economy rewards for combat | `economy-design` |
| How combat fits into the system architecture | `system-design` |
| How combat pacing fits content cadence | `gameplay-design` |
| Cross-module consistency (combat numbers vs economy) | `qa-review` |

## Skill References

- `references/combat-framework.md` — 伤害公式库 + Boss设计模板 + TTK基准表
- `references/monte-carlo-diagnostics.md` — 六维诊断体系 + 模拟规模标准 + 报告结构
- `references/action-rpg-combat.md` — 动作RPG战斗手感诊断 + Boss四阶段模板 + 角色差异化三层模型

## Shared References

- `../_shared/references/design-constitution.md`
- `../_shared/references/quality-rubric.md`

## Self-Evolution Hook

After completing a combat design task, if you discovered:
- A new damage model pattern
- A new boss design paradigm
- A combat balance failure mode not previously documented

Append to `references/evolution-ledger.md`. After 3 entries, invoke `skill-evolution`.

## Boundaries

- Do NOT derive exact DPS/EHP formulas without routing to `numerical-planning` for validation.
- Do NOT design economy rewards — that's `economy-design`.
- Do NOT design system architecture — that's `system-design`.
- Do NOT propose mechanics without defining combat pillars first.
