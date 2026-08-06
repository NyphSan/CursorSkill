# QA Checklist

Full checklist for cross-module quality assurance.

## 1. Internal Consistency Checks

### Formula Verification
For each formula stated in design output:
- [ ] Substitute sample values and compute the result
- [ ] Verify the result matches the stated expected value
- [ ] Check unit consistency (gold + gold, not gold + gems)
- [ ] Verify coefficient ranges are reasonable (not 0.001 or 10000 without justification)

### Table Cross-Reference
- [ ] Same value appears identically in all tables that reference it
- [ ] No orphaned foreign keys (references to non-existent rows)
- [ ] No duplicate primary keys
- [ ] Sorting/ordering is correct (levels in sequence, costs monotonically increasing)

### Assumption Consistency
- [ ] All assumptions are labeled [HYPOTHESIS] / [INFERRED] / [OBSERVED]
- [ ] No assumption contradicts another assumption in the same document
- [ ] Assumptions carried over from another skill's output are re-labeled

## 2. Cross-Module Consistency Matrix

### Combat ↔ Economy
| Check | Expected Relationship |
|-------|----------------------|
| Combat DPS vs Enemy HP | TTK within genre benchmark (see combat-design/references) |
| Combat reward amount vs Economy sink cost | Reward covers 1-3 days of sink activity |
| Combat difficulty vs Player power growth | Difficulty grows at similar rate to player power |
| Combat session length vs Reward cadence | One session = at least one meaningful reward |

### Economy ↔ Progression
| Check | Expected Relationship |
|-------|----------------------|
| Daily earn rate vs Upgrade cost at each level | Time-to-upgrade = 1-3 days (early), 3-7 days (mid), 7-14 days (late) |
| Free currency vs Paid currency ratio | Free path reaches endgame within 3-6 months |
| Event reward vs Permanent income | Event reward ≤ 2x normal monthly income |
| Stockpile cap vs Next content cost | Can't stockpile enough to skip more than 1 content tier |

### Progression ↔ Content
| Check | Expected Relationship |
|-------|----------------------|
| Player level unlock vs Content unlock | Content unlocks at levels the player actually reaches |
| Power growth vs Difficulty growth | Power grows at similar or slightly slower rate than difficulty |
| Content cadence vs Player consumption speed | Content lasts longer than consumption speed |
| Catch-up speed vs Veteran investment | Catch-up ≤ 50% of veteran time investment |

### System ↔ Onboarding
| Check | Expected Relationship |
|-------|----------------------|
| Feature unlock order vs Learning dependency | Each unlock builds on a previously taught mechanic |
| Tutorial complexity vs First session length | Tutorial fits within first 10 minutes |
| System count at launch vs New player cognitive load | Max 3 systems active in first session |

## 3. Boundary Case Test Matrix

### Numerical Boundaries
| Case | What to Check | Expected Behavior |
|------|--------------|-------------------|
| Level 1 (minimum) | All formulas produce valid results | No division by zero, no negative values |
| Max level (cap) | Growth curve behavior at cap | Plateau or prestige, not overflow |
| 0 resources | What can the player still do? | Core loop still accessible |
| Max resources (stockpile) | What happens at cap? | Convert, overflow, or hard stop — not undefined |
| Critical hit on min damage | Does crit formula handle edge? | Damage ≥ 1 (or stated floor) |
| Defense ≥ Attack (subtract formula) | Does damage floor at 1? | No negative damage |
| Defense = 0 | Full damage passes through? | Damage = attack * coefficient |

### Player Journey Boundaries
| Case | What to Check | Expected Behavior |
|------|--------------|-------------------|
| Brand new player | Cold start economy | Can engage with core loop within 5 minutes |
| Returning after 30 days | Catch-up mechanics | Can re-engage without feeling permanently behind |
| Player who only does PvP | Economy viability | Can progress through PvP-only path (if design promises it) |
| Player who only does PvE | Economy viability | Can progress without PvP (if design promises it) |
| F2P player at 6 months | Endgame access | Can reach endgame content (slower than payer) |
| Whale at day 1 | Pay-to-win check | Cannot trivially bypass all content |

### Config Table Boundaries
| Case | What to Check | Expected Behavior |
|------|--------------|-------------------|
| Empty table | What happens with no rows? | Graceful fallback, not crash |
| Duplicate IDs | Validation catches it? | Error on duplicate primary key |
| NULL in required field | Validation catches it? | Error on NULL in required field |
| Value out of range (negative cost) | Validation catches it? | Error on negative cost |
| Foreign key to deleted row | Referential integrity? | Error or cascade per design |

## 4. Severity Scale

| Level | Definition | Action |
|-------|-----------|--------|
| P0 | Breaks core loop, fairness, retention, or economy health | MUST fix before launch |
| P1 | Meaningfully harms one lifecycle stage or player segment | SHOULD fix before launch |
| P2 | Local issue, polish problem, or future risk | Monitor and test |

## 5. Sign-off Criteria

- [ ] All P0 issues resolved or explicitly deferred with owner and timeline
- [ ] All P1 issues resolved or documented with mitigation plan
- [ ] P2 issues logged for monitoring
- [ ] Cross-module consistency matrix has no ❌ items
- [ ] All boundary cases have defined behavior (no "undefined")
- [ ] Config tables pass validation (3-row header, no abbreviations, PK/FK integrity)
