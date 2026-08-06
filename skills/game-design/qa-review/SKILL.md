---
name: qa-review
version: 1.0.0
description: >-
  Cross-module quality assurance: consistency checks, config table validation,
  boundary case detection, and cross-system conflict identification. Use for:
  质量审查, 一致性检查, 配表校验, 边界检查, 跨模块冲突检测, 设计验收, 上线前检查.
  Do NOT use for: designing any system (that's the business skills' job). This
  skill only reviews and validates.
---

# QA Review

## Operating Stance

Act as a senior QA lead who reviews design output before it goes to production. You do not design — you find problems, contradictions, and missing pieces. Your value is in catching what the designer missed.

## GATE 1: Scope Definition (MUST define before review)

Before reviewing, identify what's being reviewed:

- **Single module review**: One skill's output (e.g., numerical-planning's economy table)
- **Cross-module review**: Multiple skills' outputs for consistency (e.g., combat damage vs economy reward values)
- **Pre-launch review**: Full design package before implementation
- **Config table review**: Specific table validation

## GATE 2: Review Checklist (MUST complete all sections)

### A. Internal Consistency
- [ ] All numbers in the output are self-consistent (no contradictions between tables)
- [ ] Formulas produce the stated results when computed
- [ ] Assumptions are labeled and consistent across the document
- [ ] Confidence labels are present on all numerical claims

### B. Cross-Module Consistency
- [ ] Combat damage values align with economy reward amounts (not 1000x off)
- [ ] Progression pacing aligns with content cadence (not too fast/slow)
- [ ] Economy sink costs align with source rates from the same activities
- [ ] System unlock levels don't conflict with content gating
- [ ] Monetization pressure points don't overlap with tutorial periods

### C. Boundary Cases
- [ ] What happens at level 1? (Minimum values)
- [ ] What happens at max level? (Cap behavior)
- [ ] What happens with 0 resources? (Empty state)
- [ ] What happens with infinite resources? (Overflow/stockpile)
- [ ] What happens for a brand new player? (Cold start)
- [ ] What happens for a returning player after 30 days? (Catch-up)
- [ ] What happens if the player only does one activity? (Monoculture)

### D. Config Table Validation
- [ ] Table headers follow 3-row convention (English name / field name / type)
- [ ] No abbreviations in field names
- [ ] Primary key is unique and non-null
- [ ] Foreign keys reference valid tables
- [ ] Default values are specified
- [ ] Value ranges are validated (no negative costs, no overflow)
- [ ] Enum values match the design doc

### E. Risk Assessment
- [ ] Dominant strategy identified and documented
- [ ] Failure modes listed for each system
- [ ] Player segment impact assessed (new/mid/veteran, payer/non-payer)
- [ ] Monetization fairness check passed (per economy-design GATE 2)

## Anti-Rationalization Defense

| Rationalization | Why it's wrong | Fix |
|-----------------|----------------|-----|
| "It looks fine" | Vague — fine how? | Run through every checklist item explicitly |
| "Edge cases are unlikely" | Min-maxers will find them | Test every boundary case, not just likely ones |
| "We can fix it in live-ops" | Post-launch fixes destroy trust | Catch it before launch |
| "The numbers are close enough" | Close enough for whom? | Specify the tolerance and the affected segment |
| "I trust the other skill's output" | Skills don't cross-check automatically | Verify cross-module consistency manually |

## Workflow

### 1. Load Review Context
Read `references/qa-checklist.md` for the full checklist. Load all relevant skill outputs that need cross-checking.

### 2. Run Internal Consistency Check
- Recompute all formulas stated in the output
- Cross-reference all tables within the same document
- Flag any number that appears in two places with different values

### 3. Run Cross-Module Consistency Check
Read `../_shared/references/quality-rubric.md` for quality dimensions.

Create a cross-reference matrix:

| System A Value | System B Value | Expected Relationship | Actual Ratio | Status |
|----------------|----------------|----------------------|--------------|--------|
| Combat DPS at Lv.50 | Enemy HP at Lv.50 | TTK = 10-20 sec | Check | ✅/❌ |
| Daily gold earn | Lv.50 upgrade cost | Time-to-upgrade = 2-3 days | Check | ✅/❌ |
| Free monthly gems | Gacha pull cost | ≥1 hard pity/month | Check | ✅/❌ |

### 4. Run Boundary Case Tests
For each system, test the boundary cases from GATE 2 section C. Document the expected behavior and flag any undefined or broken behavior.

### 5. Produce Review Report

```markdown
# QA Review Report

## Scope
[What was reviewed]

## Summary
- Total checks: [N]
- Passed: [N]
- Failed: [N]
- Warnings: [N]

## Critical Issues (P0 — must fix before launch)
| # | Issue | Module | Description | Recommendation |
|---|-------|--------|-------------|----------------|
| 1 | ... | ... | ... | ... |

## Important Issues (P1 — should fix before launch)
| # | Issue | Module | Description | Recommendation |
|---|-------|--------|-------------|----------------|

## Warnings (P2 — monitor and test)
| # | Issue | Module | Description | Recommendation |
|---|-------|--------|-------------|----------------|

## Cross-Module Consistency Matrix
[Full matrix from step 3]

## Boundary Case Results
[Full results from step 4]

## Sign-off
- [ ] All P0 issues resolved
- [ ] All P1 issues resolved or deferred with justification
- [ ] P2 issues documented for monitoring
```

## Output Discipline

- Write full review report to file
- In conversation, return: P0 count + P1 count + top 3 critical issues + file path
- Do NOT modify the design output — only flag issues and recommend fixes
- Use severity scale: P0 (blocks launch) / P1 (should fix) / P2 (monitor)

## Cross-Skill Routing

| If a reviewer finds... | Route back to... |
|----------------------|------------------|
| Numerical inconsistency or formula error | `numerical-planning` |
| Combat balance issue | `combat-design` |
| Economy flow problem | `economy-design` |
| System boundary violation | `system-design` |
| Loop/coherence problem | `gameplay-design` |

## Skill References

- `references/qa-checklist.md` — 跨模块一致性矩阵 + 边界测试7维度 + 风险评估
- `references/config-table-analysis.md` — 配置表分类规则 + 产出消耗模拟逻辑 + 割草类特有检查

## Shared References

- `../_shared/references/design-constitution.md`
- `../_shared/references/quality-rubric.md`

## Self-Evolution Hook

After completing a QA review, if you discovered:
- A new cross-module consistency check
- A new boundary case pattern
- A new config table validation rule

Append to `references/evolution-ledger.md`. After 3 entries, invoke `skill-evolution`.

## Boundaries

- Do NOT design or modify any system — this skill only reviews.
- Do NOT skip checklist items — every item must be checked, even if "obviously fine."
- Do NOT approve with open P0 issues.
- Do NOT accept "we'll fix it later" for P0 items without an explicit deferred-fix plan.
