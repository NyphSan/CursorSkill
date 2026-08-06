# Lifecycle Benchmarks

Verified against primary sources 2026-08-04. These are descriptive industry data (Moderate evidence), not causal guarantees. Never quote a number not in this file; state the source and population when citing.

## Activation

| Metric | Value | Source / population |
|---|---:|---|
| Average activation rate | 34% | Lenny's Newsletter survey, 500+ products |
| Median activation rate | 25% | same |
| SaaS average / median | 36% / 30% | same, SaaS subset |
| Formula | users hitting activation milestone ÷ users completing signup | milestone = earliest onboarding point predictive of long-term retention |
| Quality check | activated users should retain ≥2× non-activated | Lenny guidance |
| Day-1 activation, 90th percentile | ~21% | Amplitude 2025 Product Benchmark Report (2,600+ companies) |
| Day-7 / Day-14 activation, 90th pct | ~12% / ~9% | same |
| "7% rule" | 7% of cohort returning D7 ≈ top 25% of products | Amplitude |
| Enterprise D7: top 10% / median | 12.4% / 2.1% | Amplitude |
| Early activation → 3-mo retention overlap | 69% of top D7 performers are top 3-mo performers | Amplitude |
| No value in 14 days | up to 91% drop off; >98% churn for half of products | Amplitude |

## Consumer social retention (a16z bands, bounded n-day)

| Band | D1 | D7 | D30 | DAU/MAU | Weekly L5+ | MoM growth (seed) |
|---|---:|---:|---:|---:|---:|---:|
| OK | 50% | 35% | 20% | 25% | 30% | 20% |
| Good | 60% | 40% | 25% | 40% | 40% | 35% |
| Great | 70% | 50% | 30% | 50%+ | 50%+ | 50% |

Weekly bands: OK W1 40% / W4 20% · Good 55% / 30% · Great 75% / 50%. Watch where the retention curve flattens (should plateau by ~D20).

## 6-month user retention & NRR (Lenny expert panel)

| Category | Good 6-mo | Great 6-mo |
|---|---:|---:|
| Consumer social | ~25% | ~45% |
| Consumer transactional | ~30% | ~50% |
| Consumer SaaS | ~40% | ~70% |
| SMB/mid-market SaaS | ~60% | ~80% |
| Enterprise SaaS | ~70–75% | ~90% |

12-mo net revenue retention: consumer SaaS good ~55% / great ~80%; bottom-up SaaS ~100% / ~120%; enterprise ~110% / ~130%.

## Subscription apps (RevenueCat State of Subscription Apps 2026; 115k+ apps, >$16B)

**Download → trial (D30 median):** Business 9.1% · Health & Fitness 6.9% · Education 6.5% · Gaming 4.4% · Media 4.0% · North America 7.1% · AI apps 8.5% vs non-AI 5.6%. Trial starts are heavily day-0 (78–90% by category).

**Trial → paid (median):** Travel 43.5% · Health & Fitness 37.7% · Gaming 25.0% · North America 34.2% · overall ~32.5% both stores. By trial length: 17–32 days **42.5%** · 10–16 days 35.4% · 5–9 days 37.4% · ≤4 days **25.5%**.

**Download → paid (D35 median):** Hard paywall **10.7%** (top quartile >20%) vs freemium **2.1%**. Health & Fitness 2.9% · Business 2.6% · Gaming 1.0%. App Store 2.6% vs Google Play 0.9%. Day-0 share of all paid conversions: 50.6%. Revenue per install D60: hard paywall $3.09 vs freemium $0.38 (~8×).

**Trial cancellation timing:** 3-day trials — 55.4% of cancellations on day 0 (84% by day 1); 7-day 39.8%; 14-day 35.7%; 30-day 31.1%. Day 0 must demonstrate value.

**Year-1 subscriber retention (median):** weekly plans 1–2% (near-total churn) · monthly ~6–14% · yearly ~20–40% (cohorts declining year over year) · low-priced yearly 36% vs high-priced 23%. First monthly renewal ~53–61%; 35% of annual cancellations happen in month 1. Google Play billing-error cancellations ~31% vs App Store ~14%.

## Broader product retention (Amplitude)

| Metric | Top/90th | Median |
|---|---:|---:|
| 3-month retention, all products | 18.5% | 3.8% |
| B2B tech 3-month | 15.6% | 2.5% |
| Travel & hospitality 3-mo | 25.6% | — |
| Financial services 3-mo | 19.5% | — |

## Web checkout (Baymard Institute)

| Metric | Value |
|---|---:|
| Global average cart abandonment (14-yr series) | ~70.19% |
| Average CR headroom from checkout UX fixes (large sites) | ~35% |
| Average checkout field count | 12.8 (achievable: 6–8 incl. payment) |
| Abandonment due to forced account creation | 18% of US adults |
| Sites without prominent guest checkout | 62% |
| Abandonment from too-long/complex flow | 18–26% |

## Usage rules

1. Match population before citing: subscription-app numbers ≠ SaaS ≠ social. 
2. These are medians/bands, not targets — a hard-paywall wellness app and a freemium social app live in different distributions.
3. Benchmarks are descriptive, not causal: "top quartile does X" does not mean "doing X makes you top quartile."
4. Industry reports update annually — figures verified 2026-08; re-verify before quoting in anything public.
