---
name: ui-design-brain
description: Generate production-grade UI using real component patterns and best practices from 60+ documented interface components. Use when building web interfaces, pages, dashboards, forms, navigation, or any UI — SaaS-quality output grounded in design-system conventions rather than generic AI patterns.
---

# UI Design Brain

Curated knowledge of 60+ UI component patterns (from component.gallery) with best practices, layouts, and anti-patterns. Prefer this over guessing when generating web/SaaS UI.

## When to use

- Web pages, landing pages, dashboards, settings
- Forms, tables, navigation, modals/drawers
- React / HTML/CSS / Tailwind UI

## Core principles

1. Restraint over decoration; white space is a feature
2. Typography carries hierarchy
3. One strong color moment on a neutral base
4. 8px spacing grid
5. Accessibility non-negotiable (WCAG AA, focus, semantic HTML)
6. Avoid generic AI looks (purple gradients, Inter defaults, equal card grids)

## Workflow

1. Identify components needed (Header, Form, Table, Modal, Toast, Empty state, …)
2. Apply per-component best practices (see upstream `components.md`)
3. Pick a direction: Modern SaaS / Minimal / Enterprise / Creative / Dashboard
4. Generate production-ready code with hover/focus/disabled and mobile-first responsive

## Upstream

Full component reference lives in the source repo `components.md`. If missing locally, fetch from origin before coding complex UI.
