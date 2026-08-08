# Dark-Pattern Refusal Taxonomy

Sources: FTC "Bringing Dark Patterns to Light" (2022), Brignull / deceptive.design, Gray et al. CHI 2018 (+ 2024 ACM ontology), OECD dark commercial patterns report.

Definition (FTC): design practices that "trick or manipulate users into making choices they would not otherwise have made and that may cause harm." Dark patterns stack: one FTC-cited study found they roughly **doubled** signups to a dubious service, with stronger effects when combined.

## Gray et al. five strategies (ontology backbone)

| Strategy | Definition |
|---|---|
| Nagging | Persistent interrupts redirecting from the user's task |
| Obstruction | Making a process needlessly hard to dissuade an action (sludge) |
| Sneaking | Hiding, disguising, or delaying relevant information |
| Interface Interference | UI manipulation privileging certain actions deceptively |
| Forced Action | Requiring an unwanted action to reach desired functionality |

## Refusal / flag table

Generate **none** of these. If asked directly, refuse and offer the fair alternative.

| Pattern | Definition | Category |
|---|---|---|
| False activity messages | Fake "24 people viewing now" | Deceptive social proof (FTC) |
| Deceptive testimonials | Fabricated or undisclosed-paid endorsements | Endorsements (FTC) |
| Fake scarcity | False limited supply ("only 2 left" on digital goods) | Manufactured urgency |
| Fake urgency / resetting countdowns | False or ever-resetting time limits | Manufactured urgency |
| Roach motel / hard to cancel | Easy signup, obstructed cancellation | Obstruction |
| Forced continuity | Trial silently converts; cancellation buried | Negative option abuse |
| Hidden costs | Fees revealed at the last step | Sneaking |
| Sneak into basket | Items added via opt-out | Sneaking |
| Bait and switch | User intends A, receives B | Deception |
| Trick questions | Wording that asks the opposite of what it appears to | Interface interference |
| Confirmshaming | Guilt-tripping decline copy ("No thanks, I hate saving money") | Emotional manipulation |
| Nagging | Repeated interrupts to force an action | Nagging |
| Obstruction / sludge | Deliberate process friction against the user | Obstruction |
| Hidden information | Material terms in fine print / low contrast | Sneaking |
| Preselection | Defaults set against user interest without affirmative consent | Interface interference |
| False hierarchy | Visual design implying one option is the only/best when choices are parallel | Interface interference |
| Disguised ads | Ads styled as content or UI controls | Deception |
| Forced action | Must do unwanted X (share contacts, subscribe) to get Y | Forced action |
| Privacy Zuckering | Tricking users into oversharing data | Privacy harm |
| Friend spam | Contact import under false pretenses, then spam | Social graph abuse |
| Price comparison prevention | Bundles/formats designed to defeat comparison | Obstruction |
| Intermediate currency | Tokens/gems primarily to obscure real spend | Cost obfuscation |
| Misdirection | Attention steered away from material facts | Interface interference |
| Attention capture / compulsion loops | Exploiting vulnerability for excessive use (exit-less variable reward) | Wellbeing harm |
| Asymmetric choice | Accept path one tap; refuse path a maze | Autonomy violation (FTC) |
| Coerced action | Forced bundles/enrollment | Coercion (FTC) |

## Operational refusal policy

Refuse or hard-flag any request that:

1. Falsifies scarcity, urgency, social activity, testimonials, or reviews
2. Hides price, recurring billing, or material terms
3. Makes cancellation materially harder than signup
4. Uses confirmshaming or emotional punishment
5. Preselects consent against user interest without clear affirmative action
6. Disguises ads as product UI
7. Uses intermediate currency primarily to obscure real spend
8. Builds variable-reward loops without exit points, or targets them at minors/vulnerable users

## Fair-pattern alternatives (offer these instead)

- Labeled, explained defaults instead of buried preselection
- Equal-visual-weight accept/decline paths
- True inventory, true deadlines, or no scarcity claim at all
- One-click (or legally compliant) cancellation; cancel path as short as signup
- Real testimonials with disclosure; real usage counts
- Prices in real currency at first mention; totals early
- Session-complete signals and exit points in feeds
- SDT-supportive feedback (competence, autonomy) instead of loss-punishment
