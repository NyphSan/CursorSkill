---
name: nextlevelbuilder-ui-ux-pro-max
description: Use when designing, building, or reviewing UI/UX across web + mobile stacks — including game UI (HUDs, sci-fi FUI, pixel-art panels, cyberpunk surfaces, retro-futurism, spatial / VisionOS overlays) and 3D-flavored 2D screens (3D & Hyperrealism, 3D Product Preview). Provides a searchable database (84 styles, 192 color palettes, 74 font pairings, 192 product types, 98 UX guidelines) plus a Design System Generator that turns a product prompt into a complete design system in one shot. Auto-loads when the user asks for any visual design task: pages, components, palettes, typography, animation, accessibility, data viz.
---

# nextlevelbuilder / ui-ux-pro-max — design intelligence skill

A **search-driven** design intelligence skill (~115k★ GitHub as of 2026-08, MIT license). Unlike prompt-only "frontend-design" skills, **most of the SKILL is Python + CSV data**, not markdown prose. When a coding agent picks up a UI task, the skill tells it to run a search against a structured design database first, then apply the rules.

## When to use

Reach for this skill whenever the design surface is web, mobile, or web-shipping-game-screens — and the user wants **non-generic, professional** output:

- **Landing pages** for SaaS, fintech, healthcare, e-commerce, games, music, fashion, lifestyle
- **Dashboards / data apps** (BI, real-time monitoring, fintech dashboards, sales analytics)
- **Game UI surfaces** that ship as 2D overlays — HUDs, inventory grids, settings panels, achievement pop-ups, sci-fi FUI, cyberpunk surfaces, pixel-art game UI (it is explicit on Retro-Futurism, Pixel Art, HUD / Sci-Fi FUI, Cyberpunk UI, Vaporwave being game-relevant)
- **Spatial / 3D-flavored 2D** overlays (3D & Hyperrealism, 3D Product Preview, Spatial UI VisionOS)
- **Accessibility audits**, anti-pattern review, WCAG-aligned component recommendations

The skill is **prescriptive** by design — query returns a concrete pattern, style, palette, font pairing, effects stack, and anti-pattern list, rather than letting the model produce its own defaults.

## Trigger examples

- "Build a SaaS landing page"
- "Create a healthcare analytics dashboard"
- "Design a sci-fi HUD for a flight sim"
- "Build a pixel-art inventory panel for an indie game"
- "Refactor a generic purple-gradient hero into something with character"
- "Run an accessibility review on this UI"

## Tool surface (CLI: `uipro`)

```bash
npm install -g ui-ux-pro-max-cli
uipro init --ai claude --global     # global install into ~/.claude/skills/
uipro init --ai cursor             # project-local into .cursor/skills/
uipro update                       # pull latest skill data + scripts
uipro uninstall                    # removes the skill + manifest
```

Supported agents (20+): Claude Code, Cursor, Windsurf, GitHub Copilot, Kiro, Codex CLI, Gemini CLI, Trae, Qoder, Roo Code, Continue, CodeBuddy, Droid (Factory), KiloCode, Warp, Augment.

## The core operation: `--design-system`

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "fintech bank dashboard" \
  --design-system --persist
```

That's the headline v2.0 feature. It runs **five parallel multi-domain BM25 searches**:

| Domain | Queries |
|---|---|
| Pattern / structure | Landing pattern matching (Hero-Centric, Conversion-Optimized, Feature-Rich, Storytelling) |
| Style | One of 84 styles ranked by BM25 to query intent |
| Color | One of 192 palettes filtered by product type and dark/light mode |
| Typography | One of 74 font pairings personality-matched |
| Anti-patterns | Excluded clauses, e.g. "banks: no purple/pink AI gradients" |

Output is a complete design system: Pattern + Style + Color (hex codes) + Typography + Effects + Anti-patterns + Pre-delivery checklist. `--persist` writes to `design-system/MASTER.md` for cross-session reuse; per-page overrides live in `design-system/pages/`.

## Knobs

```bash
python3 .../search.py "X" --variance 1..10      # 1 = conservative centered, 10 = bold asymmetric
python3 .../search.py "X" --motion 1..10       # animation complexity
python3 .../search.py "X" --density 1..10      # information density
python3 .../search.py "X" --domain color       # single-domain query
python3 .../search.py "X" --stack next.js      # scope to one stack
```

## What's in the database (v2)

- **84 UI styles** — Glassmorphism, Neumorphism, Brutalism, Claymorphism, Bento Grid, Dark Mode, AI-Native UI, Cyberpunk, Vaporwave, Pixel Art, Spatial UI (VisionOS), Retro-Futurism, HUD / Sci-Fi FUI, 3D & Hyperrealism, 3D Product Preview, and more
- **192 product types** — SaaS, fintech, healthcare, e-commerce, creative agency, lifestyle, gaming, music, Web3, spatial computing, quantum, etc.
- **192 color palettes** — industry-appropriate, dark-mode-aware (mode-aware palette resolution added in PR #428)
- **74 font pairings** — Google Fonts based, personality-tagged
- **98 UX guidelines** — interaction, accessibility (WCAG AA contrast ratios, focus indicators), motion (150–300 ms hover sweet spot, `prefers-reduced-motion`), z-index management
- **25 chart types** — Chart.js / D3.js recommendations + accessibility notes
- **22 tech stacks** — React, Next.js, Vue, Nuxt, Svelte, Astro, SwiftUI, React Native, Flutter, Jetpack Compose, Angular, Laravel, Tailwind, shadcn/ui, Three.js + more

## How it differs from `frontend-design` (Anthropic official)

| Aspect | ui-ux-pro-max | frontend-design |
|---|---|---|
| Style | Retrieval-driven, prescriptive | Taste-driven, model-judgment |
| Format | Mostly Python + CSV + scripts | Mostly Markdown prose |
| Output | Concrete pattern + style + palette + fonts + anti-patterns | Aesthetic direction, typography, layout judgment |
| Persistence | `design-system/MASTER.md` per project | Per-conversation only |
| Cross-stack | 22 stacks, including Three.js / SwiftUI / Flutter | Web only |
| Best for | When you need consistent, non-generic output across a session and project | When you want the agent's taste |

They are complementary, not competing. `frontend-design` is in the watch list of this repo.

## Sharp edges

- **Requires Python 3.x** at runtime to call the search script — pure-frontend projects without Python need a one-line install first
- Prescriptive: outputs can look **too consistent** across very different products if you don't tune `--variance` and `--motion`
- The skill gives **design direction**, not finished UI code. The agent still has to implement; quality depends on the host agent's taste
- 115k★ reflects attention, not universal applicability — verify rules against your brand, users, and constraints
- Last numeric reflow at Aug 6, 2026 (v2.13.0); data size keeps growing

## Install + use in one minute

```bash
npm install -g ui-ux-pro-max-cli
cd /path/to/your/project
uipro init --ai claude
# Now any UI request inside Claude Code routes through the skill.
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "sci-fi game HUD" --design-system --persist
```

## Search coverage note

- New sighting at 2026-08-11 (skill data updated 08-06, repo continuously active). Tracks a meaningful design-intelligence gap: most UI skills are prompt-only, this one is **retrieval-driven**, which is precisely what gives non-generic output. Game UI style coverage (Cyberpunk, Pixel Art, HUD / Sci-Fi FUI, Vaporwave, Spatial UI, 3D & Hyperrealism) is directly applicable to game 2D HUDs even though it's a Web-oriented tool.
