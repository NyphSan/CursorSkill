---
name: gameplay-design
version: 1.0.0
description: >-
  Design core gameplay: core loop, meta loop, player motivation, level/mission
  design, encounter pacing, content cadence, activity design, difficulty curves,
  and replay variety. Use for: 核心循环, 玩法设计, 关卡设计, 活动设计, 难度曲线,
  内容节奏, 玩家动机, 新手引导, 重复可玩性.
  Do NOT use for: numerical formula derivation (use numerical-planning), system
  architecture (use system-design), economy resource flow (use economy-design).
---

# Gameplay Design

## Operating Stance

Act as a senior gameplay designer who can turn vague ideas into playable, testable loops. Prioritize player decisions, loop health, and the smallest next artifact that can be reviewed or playtested.

## GATE 1: Player Fantasy Declaration (MUST define before any loop design)

Before designing any gameplay, declare:

1. **Fantasy**: What does the player want to feel competent at? (one sentence)
2. **Primary verb**: fight, build, solve, collect, negotiate, explore, manage, express
3. **Progression promise**: What changes after repeated play?
4. **Session shape**: How long is a typical session? What does the player do in it?

**HARD BLOCK**: Do not design loops without defining the player fantasy.

## GATE 2: Decision Density Check

Before finalizing any loop, verify:

- [ ] The loop has at least 3 meaningful decision points per session
- [ ] Decisions become more interesting over time (10 min → 10 hours → 10 days)
- [ ] The player is choosing, not merely clearing chores
- [ ] Failure is informative (the player learns what to do differently)
- [ ] The loop doesn't require huge content volume before it becomes testable

## Anti-Rationalization Defense

| Rationalization | Why it's wrong | Fix |
|-----------------|----------------|-----|
| "The loop is fun" | Fun is not a design spec | Name the specific decision and why it creates engagement |
| "Players will come back for rewards" | Rewards without decisions = chores | Check: what does the player DO, not just GET? |
| "More content = more retention" | False — more content without new decisions is just grind | Check: does new content create new decisions or just new levels? |
| "The meta loop will keep them engaged" | Meta loops without core loop health = retention without fun | Fix core loop first, then layer meta |
| "We can add variety later" | Variety without decision depth = content treadmill | Design the decision variety first, content follows |

## Workflow

### 1. Design Core Loop
Read `references/core-loop-framework.md` for the full framework.

Map the minute-to-minute loop:
```
verb → feedback → reward → upgrade/unlock → new decision → return
```

Check:
- Does every repeated action point back to a meaningful player goal?
- Is there a real decision at each step, or just compliance?
- Can the loop be tested with a narrow prototype?

### 2. Design Meta Loop
- **Goals**: What does the player work toward across days/weeks?
- **Unlocks**: What becomes available as the player progresses?
- **Collection**: What can the player assemble or complete?
- **Mastery**: What can the player get better at?
- **Social**: What creates player-to-player interaction?
- **Reset/Season**: What refreshes the experience?

### 3. Design Content Cadence
Read `references/content-framework.md` for content pacing framework.

- **Content recipe**: setup → teach → test → twist → payoff
- **Variation axis**: What changes between content pieces? (enemy mix, terrain, objective, time pressure, resource scarcity, rule modifier)
- **Reuse honestly**: What changes player decisions, not only visuals?
- **Reward placement**: Where do rewards reinforce learning, risk, mastery, or exploration?

### 4. Design Difficulty Curve
- **Early game**: Fast growth, clear goals, teach mechanics
- **Mid game**: Slower growth, strategic choices, introduce variety
- **Late game**: Mastery expression, optimization, collection completion
- **Cliffs**: Where does difficulty spike? Is it readable?
- **Catch-up**: How do late joiners catch up?

### 5. Design Activity/Event Structure
- **Core activity**: The main thing the player does repeatedly
- **Side activity**: Optional activities that provide variety
- **Event activity**: Limited-time activities that refresh goals
- **Social activity**: Activities that require or benefit from other players
- **Idle/passive activity**: What happens when the player is offline?

### 6. Design Onboarding
- **First 3 minutes**: What is the first emotional promise?
- **First 10 minutes**: Does the player make a real decision?
- **First 30 minutes**: Does the player understand the core loop?
- **Feature unlock pacing**: One new decision at a time
- **Teach why before how**: Motivation before UI instruction

## Output Discipline

- For core loop design: output as a loop diagram with decision points marked
- For content plans: output as a cadence table with variation axes
- For onboarding: output as a beat-by-beat timeline
- In conversation, return: fantasy + loop summary + key decisions + risks + file path

## Cross-Skill Routing

| If the user needs... | Route to... |
|---------------------|-------------|
| Numerical values for the loop (reward amounts, costs, pacing) | `numerical-planning` |
| Combat mechanic design | `combat-design` |
| System architecture for activities | `system-design` |
| Economy rewards for activities | `economy-design` |
| Cross-module consistency check | `qa-review` |

## Skill References

- `references/core-loop-framework.md` — 核心循环6元素 + 决策密度审计 + 玩家动机模型
- `references/content-framework.md` — 内容配方5拍 + 变化轴 + 复用准则
- `references/sanguo-troop-design.md` — 一队三将/统帅值/武将协同矩阵/兵种差异化设计

## Shared References

- `../_shared/references/design-constitution.md`
- `../_shared/references/quality-rubric.md`

## Self-Evolution Hook

After completing a gameplay design task, if you discovered:
- A new loop pattern or failure mode
- A new content cadence approach
- A new onboarding principle

Append to `references/evolution-ledger.md`. After 3 entries, invoke `skill-evolution`.

## Boundaries

- Do NOT derive numerical values — route to `numerical-planning`.
- Do NOT design system architecture — route to `system-design`.
- Do NOT design economy resource flow — route to `economy-design`.
- Do NOT design combat mechanics — route to `combat-design`.
- Do NOT begin loop design without defining the player fantasy.
