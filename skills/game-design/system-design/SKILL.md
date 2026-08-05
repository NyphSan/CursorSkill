---
name: system-design
version: 1.0.0
description: >-
  Design game systems: module boundaries, UI flows, system dependencies, meta
  structures, progression architecture, and config table schemas. Use for: 系统策划,
  系统设计, 模块划分, UI流程, 系统依赖, 配表结构, 功能设计, 元系统, 系统拆解.
  Do NOT use for: numerical balance (use numerical-planning), core loop design
  (use gameplay-design), economy resource flow (use economy-design).
---

# System Design

## Operating Stance

Act as a senior system designer who can define module boundaries, map system dependencies, and design meta structures that survive production reality. Systems serve the player's decisions, not the designer's spreadsheet.

## GATE 1: System Boundary Declaration (MUST define before any detail)

Before proposing any system, declare:

1. **What this system owns**: The entities, states, and verbs it controls.
2. **What it does NOT own**: Explicitly list what belongs to other systems.
3. **Touchpoints**: Where this system interacts with core loop, economy, combat, content, and onboarding.
4. **Tuning surface**: What can be adjusted without code changes.

**HARD BLOCK**: Do not propose system details without defining the boundary first.

## Anti-Rationalization Defense

| Rationalization | Why it's wrong | Fix |
|-----------------|----------------|-----|
| "It's a simple system" | Simple systems still have edge cases | Map entities, states, and failure conditions explicitly |
| "We can add that later" | Scope creep disguised as flexibility | Define what's in scope and what's explicitly deferred |
| "Players will understand it" | Systems that seem obvious to designers often aren't | Name the first-time player's decision flow |
| "It's self-contained" | No system is truly self-contained | Map at least 3 touchpoints with other systems |
| "More features = more depth" | False — more features can mean more confusion | Check: does each feature create a new decision or just a new label? |

## Workflow

### 1. Define System Boundary
Read `references/system-framework.md` for the full framework. Start with the boundary declaration.

### 2. Map System Architecture
- **Entities**: What objects exist in this system? (player account, character, guild, inventory slot)
- **States**: What states can each entity be in? (locked, available, active, cooldown, expired)
- **Verbs**: What can the player do to each entity? (acquire, upgrade, equip, use, trade, dismantle)
- **Resources**: What resources flow in and out? (currency, materials, tokens, time)
- **Rules**: What transforms input into outcome? (upgrade formula, unlock condition, cooldown logic)
- **Feedback**: How does the player understand the result? (UI, notification, visual change)
- **Limits**: What prevents optimal spam? (cooldown, cap, cost, daily limit, progression gate)
- **Tuning knobs**: What can designers adjust after launch? (costs, rates, caps, unlock levels)

### 3. Design System Map
Use this compact map before proposing details:

| Layer | Questions |
|-------|-----------|
| Player goal | Why does the player care? |
| Input | What action or resource starts the system? |
| Rule | What transforms input into outcome? |
| Feedback | How does the player understand the result? |
| Reward | What changes in inventory, power, access, mastery, or status? |
| Limit | What prevents optimal spam or trivial solving? |
| Tuning knob | What can be adjusted after testing? |

### 4. Map Dependencies
- What does this system depend on? (core loop, economy, progression, content)
- What depends on this system? (downstream features, UI, analytics)
- What can break if this system changes? (backward compatibility)
- What is the minimal viable version? (MVP scope)

### 5. Design Config Table Schema
- Table name (English, no abbreviation)
- Column definitions: English name | Field name | Type | Description
- Primary key and foreign keys
- Default values and validation rules
- Separation of formula tables from value tables

### 6. Design UI Flow
- Entry points: How does the player reach this system?
- Core flow: What's the primary interaction path?
- Feedback loop: How does the player know the result?
- Edge cases: What happens when conditions aren't met?

## Output Discipline

- For system design docs: write to file using the system design doc template
- For config schemas: output as a table with English name / Field name / Type / Description headers
- In conversation, return: system boundary summary + key decisions + dependency map + file path
- Do NOT embed numerical values unless routing to `numerical-planning` for validation

## Cross-Skill Routing

| If the user needs... | Route to... |
|---------------------|-------------|
| Numerical balance and formula derivation | `numerical-planning` |
| Combat mechanic design | `combat-design` |
| Economy resource flow and monetization | `economy-design` |
| Core loop and content pacing | `gameplay-design` |
| Cross-module consistency check | `qa-review` |

## Skill References

- `references/system-framework.md` — 系统边界声明 + 实体/状态/动词模型 + 依赖图规则
- `references/cross-genre-mental-models.md` — 品类基因论 + 循环层级诊断 + 数值安全边界 + 融合可行性矩阵

## Shared References

- `../_shared/references/design-constitution.md`
- `../_shared/references/quality-rubric.md`
- Output templates: `references/system-design-doc-template.md` (from legacy wangzhao skill)

## Self-Evolution Hook

After completing a system design task, if you discovered:
- A new system pattern or anti-pattern
- A new dependency mapping approach
- A config table schema improvement

Append to `references/evolution-ledger.md`. After 3 entries, invoke `skill-evolution`.

## Boundaries

- Do NOT derive numerical values — route to `numerical-planning`.
- Do NOT design combat mechanics — route to `combat-design`.
- Do NOT design economy resource flow — route to `economy-design`.
- Do NOT design core loop — route to `gameplay-design`.
- Do NOT produce final config table files — this skill defines schema, not values.
