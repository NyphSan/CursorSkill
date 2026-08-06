# Tactic → UI Translation

Concrete component, layout, microcopy, and motion specs per tactic family. Sourced from documented teardowns (Growth.Design Duolingo/Trello/TikTok cases, UserOnboard patterns, NN/g, RevenueCat). A recommendation is not complete until it specifies all four layers.

## Streaks (Retention / Habit)

| Layer | Spec |
|---|---|
| Components | Streak counter badge (flame/calendar icon); daily-goal progress ring; streak-wager modal offered right after a reward peak; streak freeze/repair item |
| Layout | Streak state persistent near home header; incomplete daily goal framed as "one lesson away" |
| Microcopy | Commitment framing ("Bet 50 gems you'll keep a 7-day streak"); welcome-back grant on lapsed return |
| Motion | Progress fill toward daily goal; celebration on completion |
| Guardrail | Streak loss is a major quit trigger. Always ship freeze/repair. Never pair streak loss with shame copy. |

## Variable reward feeds (Engagement) — ethics-gated

| Layer | Spec |
|---|---|
| Components | Full-screen media viewport; swipe-next; algorithmically unpredictable next item; interest multi-select on first run (~15–20 options) |
| Layout | Immersive single-item view, chrome minimized |
| Motion | Instant swipe transition; auto-loop |
| Guardrail | **Required**: exit points and completion sense (session summaries, "you're all caught up"). Variable reward without exits is compulsion design — refuse for wellbeing products and minors. |

## Commitment devices (Activation / Habit)

| Layer | Spec |
|---|---|
| Components | Goal-setting screen; public-commitment toggle; stake/wager modal; reminder opt-in |
| Timing | Ask immediately after a reward peak, never before first value |
| Microcopy | User states the goal in their own terms; app mirrors it back later |

## Social proof (Trust / Conversion) — truth-gated

| Pattern | Component |
|---|---|
| User counts | "Join 2M+ learners" adjacent to CTA — real numbers only |
| Testimonials | Quote + full name + photo + role; disclose material connections |
| Ratings | Star aggregate + review count |
| Activity streams | "X booked today" — **only if literally true** (fake = FTC False Activity) |
| Authority badges | Press logos, certifications |
| Wisdom of friends | "Friends who use this" avatars |

Microcopy rules: specific > vague, attributable > anonymous, recent > stale.

## Progress mechanics (Onboarding / Habit)

| Layer | Spec |
|---|---|
| Components | Linear bar with %, step indicator ("Step 2 of 5"), checklist, endowed-progress bar starting >0% |
| Microcopy | Competence cues: "You're halfway there" |
| Motion | Smooth fill on step complete; confetti at 100% (once — hedonic adaptation) |

## Personalization / onboarding quizzes (Onboarding)

| Layer | Spec |
|---|---|
| Components | Multi-select use-case grid; dual path buttons ("Dive right in" / "Help me get started"); live preview of the product building itself from answers |
| Microcopy | Ask what the user wants to **accomplish**, not who they are |
| Guardrail | 2–4 questions max — quiz length is choice overload; every question must visibly change the outcome |

## Empty states (Onboarding)

| Pattern | Spec |
|---|---|
| Educative starter | Instructions + preview of power-user end state |
| Primary CTA in the empty container | "Create your first project" — one action, not a menu |
| Delight ratio | Two parts instruction, one part delight (illustration/mascot) |
| Pre-seeded content | Preload exactly one example item (one project, one note-as-tutorial, one sample file); gate the dashboard until first core action completes |

Related patterns: front-loaded user value, permission priming (explain before the OS prompt), sensible defaults, success states.

## Paywalls (Monetization)

| Pattern | Spec | Benchmark context |
|---|---|---|
| Hard paywall | Full-screen gate before core value; show value first via preview/demo | Median D35 download→paid 10.7% vs freemium 2.1% (RevenueCat 2026) |
| Freemium soft paywall | Feature locks, upgrade sheets, contextual banners | Lower conversion, similar Y1 yearly retention (~27–28%) |
| Trial UI | State duration clearly, show cancel path, deliver value on day 0 | 17–32-day trials convert 42.5% vs ≤4-day 25.5%; most cancellations happen day 0–1 |
| Plan cards | Monthly/annual cards, annual highlighted (Von Restorff) + default, restore-purchases link, visible legal | Disclose the default clearly — preselection against interest is a dark pattern |

## Onboarding path compression (Activation)

1. Strip nav on the signup path to Login + Signup only (Hick's Law).
2. Defer account creation / email confirmation until after first value.
3. Persona quiz → tailored first screen.
4. Offer experience segmentation: "Dive in" vs "Help me start".
5. Migrate mental models with a live preview (form input → visible product state).
6. One-tap shortcut to the core action for returning users; a focus overlay when many elements compete.

## Scarcity & urgency (truth-gated)

| Ethical | Refuse |
|---|---|
| Real inventory count, accurately refreshed | Fake "24 people viewing" |
| True sale end datetime | Ever-resetting countdown |
| Cohort access that actually closes | "Only 2 left" on digital goods |
