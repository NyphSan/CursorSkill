# Tactic Library

Consolidated from Laws of UX (Yablonski), Persuasive Patterns (Toxboe / ui-patterns.com), Coglode nuggets, EAST (UK Behavioural Insights Team), nudge taxonomy (Thaler/Sunstein lineage; Mertens et al. PNAS 2021), and Growth.Design case teardowns. Deduplicated and organized by mechanism family.

Evidence legend: **Strong** = peer-reviewed/replicated/meta-analyzed · **Moderate** = single studies, large industry datasets, or well-documented HCI laws · **Folklore** = practitioner heuristics and case studies without causal proof (usable when labeled).

## 1. Perception & interaction laws (HCI backbone)

| Tactic | Definition | Stage | Evidence |
|---|---|---|---|
| Fitts's Law | Target acquisition time = f(distance, size) — big, close CTAs | Conversion, Onboarding | Strong |
| Hick's Law | Decision time rises with number/complexity of choices | Onboarding, Conversion | Strong |
| Gestalt laws (proximity, similarity, common region, connectedness, Prägnanz) | Spatial grouping drives perceived relationships | All layout | Strong |
| Doherty Threshold | Keep interactive feedback under ~400ms | Engagement | Moderate |
| Miller's Law / chunking | Working memory ~7±2; group info into meaningful units | Onboarding | Strong (chunking) / Moderate (exact 7±2) |
| Cognitive load | Minimize mental effort required per step | All | Strong |
| Selective attention | Users only process goal-relevant stimuli | Engagement | Strong |
| Serial position effect | First and last items remembered best — order pricing tiers and lists deliberately | Onboarding, Pricing | Strong |
| Von Restorff (isolation) effect | The visually distinct item gets remembered/chosen — highlight the target plan | Conversion, Monetization | Moderate–Strong |
| Jakob's Law | Users expect your product to work like ones they know | Onboarding, Trust | Moderate |
| Mental models / conceptual metaphor | Map new concepts to known ones; migrate old models with live previews | Onboarding | Moderate–Strong |
| Aesthetic-usability effect | Attractive design is perceived as more usable | Trust, Onboarding | Moderate |
| Peak-end rule | Experiences are judged by peak moment and ending — engineer both | Engagement, Offboarding | Moderate–Strong |
| Recognition over recall | Show options rather than requiring memory | Engagement | Strong |
| Picture superiority | Images beat words for memory | Onboarding, Growth | Moderate–Strong |
| Tesler's Law | Irreducible complexity must live somewhere — decide where deliberately | Refinement | Moderate |
| Paradox of the active user | Users skip instructions and dive in — design for exploration, not manuals | Onboarding | Moderate |

## 2. Friction & choice architecture

| Tactic | Definition | Stage | Evidence |
|---|---|---|---|
| Reduction | Cut steps to the target action | Activation | Moderate |
| Tunnelling | Guide users through one focused path | Onboarding | Moderate |
| Sequencing | Order steps for comprehension and momentum | Onboarding | Moderate |
| Defaults | Pre-selected option persists via inertia; implied recommendation | Conversion, Onboarding | Strong |
| Decision structure nudges | Rearranging option format/order — the most effective nudge class in meta-analysis | Conversion, Pricing | Strong |
| Decision information nudges | Make info more available/comprehensible (labels, translations) | Trust, Conversion | Moderate–Strong |
| Limited choice | Fewer options increase decision rate (choice overload is real) | Onboarding, Monetization | Moderate–Strong |
| Lazy registration | Delay signup until after first value | Activation | Folklore–Moderate |
| Forgiving format / Postel's Law | Accept liberal input; validate inline | Forms, Trust | Moderate |
| Reminders | Timely prompts at opportune moments (Kairos) | Habit | Moderate–Strong |
| Cooling-off periods | Delay finalization of hot-state decisions (ethical monetization) | Monetization | Moderate |
| **Meta-caveat** | Choice architecture overall: d = 0.45 (CI 0.39–0.52), I² ≈ 99.7%, ~15% backfire (Mertens et al., PNAS 2021) — always recommend testing | — | Strong (about the limits) |

## 3. Value perception & pricing psychology

| Tactic | Definition | Stage | Evidence |
|---|---|---|---|
| Anchoring | Initial number biases later judgments — show reference price first | Pricing | Strong |
| Framing / attribute translation | Same facts, different decisions depending on presentation | Conversion, Monetization | Strong |
| Loss aversion | Losses hurt ~2× more than gains please (prospect theory) | Monetization, Retention | Strong |
| Status-quo bias | Preference for current state; powers defaults and renewals | Monetization | Strong |
| Decoy / asymmetric dominance | Inferior third option steers choice to target plan | Pricing | Moderate (context-sensitive) |
| Zero-price bias | "Free" is disproportionately attractive vs. cheap | Monetization | Moderate |
| Certainty effect | Users prefer clarity over chance — guarantee > lottery | Monetization, Trust | Strong |
| Contrast principle | Nothing is expensive or cheap except by comparison | Pricing | Moderate |
| Endowment effect | Owned things are valued more — trials that create ownership | Activation, Monetization | Strong |
| IKEA / labor effect | Users value what they helped build; visible effort raises perceived value (labor illusion) | Activation, Onboarding | Moderate |
| Sunk cost | Prior investment sustains commitment | Retention | Moderate |
| Present bias / delay discounting | Immediate rewards dominate delayed ones — front-load payoff | Habit, Monetization | Strong |
| Risk aversion | Prefer known over uncertain — de-risk with guarantees, previews | Monetization | Strong |

## 4. Progress & goal mechanics

| Tactic | Definition | Stage | Evidence |
|---|---|---|---|
| Goal-gradient effect | Effort accelerates as the goal nears — visible progress compounds | Retention, Habit | Moderate–Strong |
| Endowed progress | Artificial head-start (bar starts at 20%) increases completion | Onboarding, Habit | Moderate |
| Zeigarnik effect | Incomplete tasks nag memory — open loops drive returns | Retention | Moderate |
| Completeness meter / steps-left | % complete and "Step 2 of 5" indicators | Onboarding | Moderate |
| Set completion / collection bias | Drive to finish collections | Habit | Moderate |
| Shaping | Reinforce successive approximations of the target behavior | Onboarding, Habit | Strong |
| Levels / progression systems | Tiered advancement structures | Habit | Folklore |
| Self-monitoring | Let users track their own behavior (dashboards, stats) | Habit | Moderate–Strong |
| Flow / appropriate challenge | Match difficulty to skill; boredom and anxiety both kill sessions | Engagement | Moderate |
| Feedback loops | Show consequences of actions immediately | Engagement | Strong |
| Praise | Affirmative feedback builds competence | Engagement | Moderate |

## 5. Habit formation & timing

| Tactic | Definition | Stage | Evidence |
|---|---|---|---|
| Triggers (cue design) | Prompt at the moment motivation + ability converge (Fogg B=MAP) | Habit | Moderate |
| Implementation intentions | If–then plans for anticipated barriers | Habit | Strong |
| Tiny habits | Split goals small enough to always succeed | Habit | Moderate |
| Fresh start effect | Motivation spikes at temporal landmarks (Mondays, birthdays, resets) | Habit | Moderate |
| Spacing effect | Repetition over time/context beats massed exposure | Habit, Learning | Strong |
| Temptation bundling | Pair a "want" activity with a "should" activity | Habit | Moderate |
| Deposit contracts | Stakes on own goals (loss aversion applied to commitment) | Habit | Moderate |
| Appointment dynamics / periodic events | Scheduled return moments | Habit | Folklore |
| Variable rewards | Unpredictable reinforcement (operant conditioning) — **ethics gate required; no exit-less loops** | Engagement, Habit | Moderate (mechanism) / high compulsion risk |
| Fixed rewards | Predictable reinforcement for reliable behaviors | Habit | Moderate |
| Streaks | Consecutive-use counters (loss aversion + goal gradient) — **ship with freeze/repair** | Habit | Folklore–Moderate; documented backfire on loss |
| Investment loops | Users invest data/effort/content that loads the next trigger | Habit | Moderate |
| Hedonic adaptation | Pleasure from any fixed reward fades — rotate and escalate meaningfully | Rewards design | Strong |

## 6. Social & identity

| Tactic | Definition | Stage | Evidence |
|---|---|---|---|
| Social proof (genuine) | People copy others under uncertainty — strongest when uncertainty is high | Trust, Conversion | Moderate (context-sensitive; fake = refuse) |
| Descriptive norms | Show what most people actually do | Trust, Conversion | Strong |
| Injunctive norms | Show what people approve of | Trust | Moderate–Strong |
| Dynamic norms | Highlight growing behaviors ("more people are switching…") | Growth | Moderate |
| Authority | Compliance with perceived expertise — credentials, press, certifications | Trust | Moderate |
| Liking / halo effect | Preference transfers from one positive trait to the whole | Trust, Brand | Moderate |
| Reciprocity | Give first; obligation follows | Growth, Monetization | Moderate |
| Commitment & consistency | Users act consistently with prior commitments, especially public/effortful ones | Activation, Habit | Moderate |
| Status | Visible rank and prestige motivate | Growth, Premium | Folklore–Moderate |
| Self-expression / identity | Products as identity statements — design for the self users want to become | Growth, Premium | Moderate |
| Reputation systems | Peer evaluation scores | Growth | Moderate |
| Competition / leaderboards | Relative ranking motivates (and demotivates the bottom) | Habit, Growth | Folklore–Moderate |
| Storytelling | Narrative transportation frames meaning | Onboarding, Growth | Moderate |
| Mere exposure | Familiarity breeds liking | Trust, Habit | Strong |
| Nostalgia effect | Past-positive affect increases preference | Brand | Moderate |

## 7. Attention & belief heuristics

| Tactic | Definition | Stage | Evidence |
|---|---|---|---|
| Fluency shortcut | Easy-to-process = more believable — plain language wins | Trust, Conversion | Moderate–Strong |
| Curiosity / information gap | Tease unresolved information | Engagement | Moderate |
| Surprise effect / delighters | Unexpected positive moments punch above their weight (peak-end) | Engagement | Moderate/Folklore |
| Availability bias | Judged by ease of recall — vivid examples dominate | Trust | Strong |
| Confirmation bias | Users seek confirming evidence — meet them where they already believe | Trust | Strong |
| Priming | Prior stimulus shapes later response — **replication caveats; don't overclaim** | Onboarding | Contested |
| Negativity bias | Negative information weighs more — handle errors and bad news carefully | Trust, Offboarding | Strong |
| Reactance | Push too hard and users do the opposite — respect autonomy | Onboarding, Monetization | Strong |
| Analysis paralysis | Decision capacity depletes — don't stack choices | Onboarding | Moderate |

## 8. Scarcity & urgency (ethics-gated family)

| Tactic | Definition | Stage | Evidence |
|---|---|---|---|
| Scarcity (genuine) | Real limited availability raises value inference | Monetization, Conversion | Moderate — **only if true** |
| Limited duration (genuine) | Real time-boxed offers | Conversion | Folklore–Moderate — **only if true** |
| Limited access | Real gated cohorts/waitlists | Growth, Premium | Folklore |
| Time scarcity | Real deadlines create urgency | Conversion | Folklore–Moderate |
| **Rule** | Any fabricated scarcity, count, or countdown = dark pattern → refuse (see dark-patterns.md) | — | — |

## 9. EAST summary (policy-grade wrapper)

Behavioural Insights Team framework, backed by policy RCTs — use as a final checklist on any behavior-change design: make it **Easy** (defaults, friction cuts, simple messages), **Attractive** (salience, incentives), **Social** (norms, networks, reciprocity), **Timely** (right moment, immediate costs/benefits, if-then planning). Evidence: Strong.

## 10. Named case tactics (practitioner folklore — excellent UI ideas, unverified causality)

| Tactic | Case | Claimed result |
|---|---|---|
| Streak wager (bet currency on 7-day streak) | Duolingo | +14% D7 retention (self-reported) |
| Exit points after daily goal | Duolingo | +5% D30 (experiment goal) |
| Welcome-back reward + easier return lesson | Duolingo | reactivation aid |
| Notification auto-silencing when ignored | Duolingo | respect-attention pattern |
| Nav stripping on signup path ("less links, less leaks") | Trello | up to +28% CR (self-reported) |
| Persona-based onboarding quiz | Trello | +36% activation (self-reported) |
| Deferred account creation | Trello | value-before-signup |
| Live preview during setup (mental-model migration) | Trello | comprehension aid |
| Interest multi-select first-run | TikTok | personalization cold-start |
| Sniper links (deep-link straight to inbox confirmation) | various | activation friction cut |
| Aha-moment engineering / TTV compression | Amplitude-documented | activated users retain ≥2× |
