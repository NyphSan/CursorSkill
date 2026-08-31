---
name: leonxlnx-taste-skill
description: Use when designing, building or reviewing visual interfaces (web, mobile, design system) and the user wants non-generic, anti-slop output. Replaces boilerplate "AI landing page" layouts with high-end typography, motion, density, and spatial composition. Trigger on phrases like "build a landing page", "design a dashboard", "refactor this UI", "make it less generic", "give the agent taste", "stop making it look like every other AI page", "build a brand kit", or "imagegen for hero/mobile/brand reference board". Pairs with `nextlevelbuilder-ui-ux-pro-max` (this is for code output; nextlevelbuilder is for styles + palettes + fonts).
---

# Leonxlnx / taste-skill — anti-slop frontend Agent Skills

A curated pack of ~13 portable Agent Skills (~73.9k★ / ~5.06k forks as of 2026-08-13, MIT, copyright 2026 Leonxlnx). The headline claim is blunt: "give your AI good taste" — and **stops the AI from generating boring, generic slop**.

This is **code-output focused**. Unlike `nextlevelbuilder-ui-ux-pro-max` (which is retrieval-driven across 84 styles / 192 palettes / 74 font pairings), taste-skill ships as a family of smaller skill files that each do one job: redesign existing UIs, force minimalism, force brutalism, force high-end softness, stop half-finished output, generate image references for boards.

## When to use

Reach for taste-skill whenever the agent would otherwise produce an "AI landing page":

- **Brand landing pages** / marketing sites where layout, type, motion matter
- **Design systems / design tokens** for a new product
- **Refactoring an existing UI** away from default React / Next / Shadcn looks
- **Mobile app screens** (iOS / Android) — separate skill for mobile comps
- **Brand identity / kit boards** when the user wants logo directions, palettes, typography proposals
- **Image-first pipelines** — generate the reference board first, then implement

Skip when: the user wants an internal admin tool, a quick-and-dirty CRUD form, or backend work. taste-skill explicitly optimizes for **visual quality over speed**; for speed use plain `frontend-design`.

## Trigger examples

- "Build a SaaS landing page that doesn't look like every other AI page"
- "Refactor this UI to feel more premium / more brutalist / more minimal"
- "Generate a brand kit: 3 logo directions + palette + type pairing + 3 application samples"
- "Design mobile comps for an iOS app"
- "Stop leaving half-finished code or placeholder comments"
- "Pair ChatGPT Images for hero reference, then write the page"

## The 13 skills (one folder, one job)

Install everything with one command, or pick by install name:

```bash
# Whole pack
npx skills add https://github.com/Leonxlnx/taste-skill

# Single skill (note: --skill uses the frontmatter `name`, NOT the folder name)
npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend
```

| Folder | Install name | Job |
|---|---|---|
| `taste-skill` | `design-taste-frontend` | 🆕 **v2 (experimental)** — reads the brief, infers design language, tunes three dials (VARIANCE / MOTION / DENSITY), hard em-dash ban, canonical GSAP skeletons, redesign-audit protocol, strict pre-flight check |
| `taste-skill-v1` | `design-taste-frontend-v1` | Original v1, preserved for projects that depend on its exact behavior. Pin if v2 breaks a workflow |
| `gpt-tasteskill` | `gpt-taste` | Stricter variant for GPT / Codex: higher layout variance, stronger GSAP direction, aggressive anti-slop |
| `image-to-code-skill` | `image-to-code` | Image-first pipeline: generate site references → analyze → implement frontend to match |
| `redesign-skill` | `redesign-existing-projects` | Existing projects: audit the UI first, then fix layout, spacing, hierarchy, styling |
| `soft-skill` | `high-end-visual-design` | Polished, calm, expensive UI — softer contrast, whitespace, premium fonts, spring motion |
| `output-skill` | `full-output-enforcement` | When the model ships half-finished work: full output, no placeholders |
| `minimalist-skill` | `minimalist-ui` | Editorial product UI (Notion / Linear vibes), restrained palette, crisp structure |
| `brutalist-skill` | `industrial-brutalist-ui` | Hard mechanical language: Swiss type, sharp contrast, experimental layout |
| `stitch-skill` | `stitch-design-taste` | Google Stitch-compatible rules, with optional DESIGN.md export format |
| `imagegen-frontend-web` | `imagegen-frontend-web` | Image gen only (no code): website comps — hero, landing, multi-section, strong typography + anti-slop art direction |
| `imagegen-frontend-mobile` | `imagegen-frontend-mobile` | Image gen only: mobile screens and flows, iOS / Android / cross-platform mockups |
| `brandkit` | `brandkit` | Image gen only: brand-kit boards — logo directions, palettes, type, identity applications |

## How it differs from peers

| Skill | Approach | Best when |
|---|---|---|
| `taste-skill` (this) | Anti-slop opinionated rules, **code + image-gen family** | Brand pages, redesigns, premium aesthetic |
| `nextlevelbuilder-ui-ux-pro-max` | Retrieval-driven, **Python + CSV database** of styles / palettes / fonts | Consistent design systems across many surfaces, game-relevant 2D HUDs |
| `frontend-design` (Anthropic official) | Taste-driven prompt prose | When you want the host agent's own taste, web-only |
| `addyyosmani/agent-skills` | Engineering-discipline pack, has `frontend-ui-engineering` | Pipeline discipline for app engineering, not pure aesthetics |

The four are complementary. For a game-styled premium page: combine `taste-skill` (anti-slop rules) + `nextlevelbuilder-ui-ux-pro-max` (style lookup) + `addyyosmani/agent-skills/frontend-ui-engineering` (engineering discipline) + the host agent's native taste.

## The three dials that make v2 work

```
VARIANCE  = 1..10   layout asymmetry / boldness
MOTION    = 1..10   animation complexity
DENSITY   = 1..10   information density
```

v2 starts by inferring the design language from the brief, then tunes these three knobs before generating. Treat the knobs as the **specific observation point** when judging whether the skill actually changed model behavior versus just swapping a palette.

## What's NOT in the pack

- No general frontend engineering discipline (use `addyyosmani/agent-skills/frontend-ui-engineering` for that)
- No backend / testing / CI coverage
- No explicit game-engine coverage — but `industrial-brutalist-ui` and `high-end-visual-design` both ship game-relevant patterns
- v2 is **experimental / actively iterating** toward v2.0.0 stable; pin to `design-taste-frontend-v1` if v2 breaks a workflow

## Sharp edges

- **v2 is experimental**. README says "Actively iterating toward v2.0.0 stable" — expect frontmatter / body churn
- **Author-published disclaimer**: "Taste Skill has no official token, coin, or crypto project. Any token using my name, image, or project is unaffiliated and not endorsed by me." Do not install third-party projects claiming author endorsement
- **`--skill` argument uses the frontmatter `name` field, NOT the folder name**. `--skill taste-skill` will NOT match; you need `--skill design-taste-frontend`. This trips up first-time installers
- **`--skill` install only copies that one folder, not shared references**. The skill still works, but shared checklists between siblings are unavailable — install the whole pack if you want the family cross-references
- **`gsap` is canonical in code skeletons** — bundle size implication if you ship a marketing site with full GSAP; consider Motion One for lighter pages
- Last observed update: **2026-08-07** (v2 rewrite) — top commit visible to public events: 08-07 publish; frontmatter still iterating

## Install + use in one minute

```bash
# Pick a single taste skill by its install name
npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend

# Or the whole pack (one command, 13 skills)
npx skills add https://github.com/Leonxlnx/taste-skill

# In Cursor / Claude Code, ask:
"Build a SaaS landing page for a fintech dashboard. Use taste-skill. Variance 8, Motion 6, Density 7."
```

## Search coverage note

- New sighting **2026-08-13**. Today's star count ~73.9k / forks ~5.06k / today's delta ~+720 stars — the pack crossed the "1% of all GitHub" attention threshold this week. Likely to keep rising
- Pairs cleanly with `nextlevelbuilder-ui-ux-pro-max` (already in repo, 08-11) — that one supplies style / palette / font lookup; this one supplies anti-slop rules
- For game-adjacent UI (HUD / Sci-Fi FUI / Cyberpunk / Pixel-Art inventory / Vaporwave dashboards) both packs have direct coverage; pick `nextlevelbuilder` for the database, pick `taste-skill` for the opinionated constraints
