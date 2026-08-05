# Web / Landing Page / Checkout Conversion Patterns

Sources: NN/g eyetracking research, Baymard Institute checkout/form research, CXL pricing experiments.

## Above-the-fold hierarchy (NN/g)

- Users spend ~80% of viewing time above the fold (eyetracking: 80.3% above / 19.7% below).
- Content above the fold is treated dramatically differently from content below (~84% difference in attention).
- Users scroll only when above-fold content promises value — design "information scent": cut content mid-element to invite scrolling, never a wall of text that looks complete.
- Responsive design has multiple folds — define mobile and desktop hero hierarchies separately.

**Above-fold checklist:** headline stating the job-to-be-done · subhead stating how · primary CTA · one proof element (logo bar or rating) · product visual. Minimize nav on conversion paths.

## Form design (Baymard)

| Practice | Detail |
|---|---|
| Single column | Avoid extensive multi-column layouts |
| Minimize fields | Target 6–8 for guest checkout including payment (site average is 12.8) |
| Mark required AND optional | 32% of users miss required fields when only optional ones are marked |
| Guest checkout prominent | 62% of sites fail this; forced account creation alone loses 18% |
| Gentle password rules | Overly complex rules + login friction → up to 19% abandonment among returning users |
| Inline validation, forgiving format | Accept flexible input (spaces in card numbers etc.), validate as-you-go |
| Address autocomplete | Cuts the highest-friction field cluster |

## Checkout friction reduction (priority order)

1. Guest checkout as the default path
2. 6–8 essential fields, single column
3. Transparent total early — late-revealed fees are the Hidden Costs dark pattern (refuse)
4. Multiple payment methods
5. Delivery **date** (not vague speed); 48% of sites fail this framing
6. Account creation offered after purchase, optional
7. Forgiving input + undo

## Pricing page patterns (CXL)

| Pattern | Use | Evidence note |
|---|---|---|
| Anchoring | Higher reference price first so the target feels reasonable | Strong classic effect; context matters |
| Decoy plan | Inferior third option steering to the preferred tier | Documented, not universal |
| Charm pricing | Prices ending in 9 | Practitioner + some experimental support |
| Currency-symbol removal | "24" vs "$24" | Context-specific finding; test it |
| Value-before-price | Outcomes explained before price appears | Practitioner CRO |
| Recommended-plan highlight | Visual emphasis on target tier (Von Restorff) | UI pattern |
| Annual default + monthly toggle | Default effect + discount framing | Strong mechanism — **must disclose clearly** |

**Guardrail:** anchoring/decoy sharpened to the point of preventing genuine comparison becomes Price Comparison Prevention / Interface Interference — dark patterns, refuse.

## Social proof placement

| Placement | Rationale |
|---|---|
| Adjacent to primary CTA | De-risks the decision at the decision moment |
| Near price | Peer validation softens price pain |
| Logo bar under hero | Fast authority scan above the fold |
| Review module mid-page | Feeds scroll scent through the consideration zone |
| Never fake live counters | FTC False Activity — refuse |
