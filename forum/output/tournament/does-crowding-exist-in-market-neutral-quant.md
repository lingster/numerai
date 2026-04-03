---
title: "Does crowding exist in market-neutral quant?"
category: Tournament
url: https://forum.numer.ai/t/does-crowding-exist-in-market-neutral-quant/8267
created_at: 2026-03-28T15:03:33.180000+00:00
last_posted_at: 2026-03-31T20:27:07.566000+00:00
posts_count: 3
views: 69
tags: []
---

# Does crowding exist in market-neutral quant?

---

### Post #1 — **greyone** | 2026-03-28 15:03 UTC

The below is an early effort to evaluate risk regimes within Numerai.

Every quantitative strategy shares a structural vulnerability: when a strategy works, participants converge on it. This convergence is rational at the individual level — you train on the target that pays, using the features that predict — but collectively it creates a crowded trade that eventually undermines itself.

In traditional equity markets, crowded factor trades unwind suddenly and violently. The August 2007 quant quake, momentum crashes, and carry trade reversals all follow the same pattern. Capital accumulates gradually on one side of a trade over months, then exits in days when the underlying factor relationships break. The buildup is slow; the unwind is fast.

Numerai’s tournament has the same dynamics but with a specific mechanism. The majority of modelers (as well as other quant strategy trading systems) optimize against a single target — Ender20 — using overlapping feature sets. When those features work well, CORR rises for everyone, new capital enters, and the stake-weighted meta-model becomes increasingly saturated with Ender20-like predictions. The benchmarks still predict accurately (high CORR), but their unique contribution shrinks (low MMC) because the crowd is expressing the same signal. This is the crowding building.

The correction comes when the crowded feature exposures stop working. Too much capital on the same factors causes those factors to mean-revert or lose effectiveness. CORR collapses — not just for the crowded models, but for all models, because the factor environment itself has shifted. Short-term optimizers, who chased the features precisely because they were working, are the most exposed. They entered late, sized up at the peak, and their positions are the most correlated with each other. When they exit, they exit together.

The research below attempts to detect where we are in this cycle using publicly available benchmark performance data. The core insight is that the relationship between CORR and MMC across Numerai’s 8 benchmark models reveals the crowding state. When non-Ender benchmarks earn significantly more MMC than Ender20 at the same CORR level, the crowd has piled into Ender20-like features. When both CORR and MMC trends weaken simultaneously, the unwind may be beginning.

This is not a predictive model — the dataset is too short and the independent observations too few to claim statistical significance. It is a risk management framework: a structured way to think about when to be fully invested and when to protect capital, based on the crowding cycle that is inherent to any tournament where participants can observe and imitate each other’s success.

**

The system below classifies the benchmark regime into four phases using two trend signals:** the 5-round moving average minus the 15-round moving average of both CORR20 and MMC20 across all 8 Numerai benchmarks.

**Phase is determined by which trends are positive.** Both up = Phase 1 (early regime, full stake). CORR up but MMC down = Phase 2 (crowd catching up, reduce). Both down = Phase 3 (drawdown, minimum). CORR down but MMC up = Phase 4 (washout ending, moderate).

**Stake tapers with duration.** The longer you stay in Phase 1, the more you reduce — from 1,500 down to 500 as the run exceeds its historical median of 7 rounds. In Phase 3, you do the opposite — start at 250 and scale up as the drawdown extends past its median of 12 rounds, positioning for recovery.

**One reset trigger.** If CORR makes a new 20-round high while in Phase 1, the duration clock resets and stake goes back to 1,500. The regime has genuinely renewed.

**One veto.** Unresolved round data from the maturity-filtered crossover (days 7-13 vs days 14-19) can block the reset. If the leading signal is weakening relative to the confirmed signal, the breakout may be stale — don’t size up.

**Result over 318 rounds:** 20% better capital efficiency than flat staking, worst single round cut in half, same Sharpe ratio at 56% of the average stake. When vol-matched to the same risk budget as flat 1,500, the system produces approximately 1,149 NMR versus 959 flat — 20% more return for the same risk.

**Current reading:** Phase 1, day 13, 1.7x median duration. Breakout trigger is firing (CORR at new highs) but the live data veto is active (unresolved crossover weakening). Recommended stake: 500 NMR.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b22af9e4455659671a185be183564a80a92d0204_2_624x323.jpeg)image780×404 61.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b22af9e4455659671a185be183564a80a92d0204.jpeg> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8df4d72a73249e4e435704f2fe34887502df594c_2_624x323.jpeg)image780×404 73.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8df4d72a73249e4e435704f2fe34887502df594c.jpeg> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/95fbc1c3254daef19e4a4375629eaec640fe3fbe_2_624x273.png)image780×341 53.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/95fbc1c3254daef19e4a4375629eaec640fe3fbe.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/cc8b68554ffcd9b4adceaadc0ae4d3f71ba0770c_2_624x226.png)image780×282 73.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cc8b68554ffcd9b4adceaadc0ae4d3f71ba0770c.png> "image")

---

### Post #2 — **greyone** | 2026-03-31 19:59 UTC

**Using MMC as a crowding risk indicator — a novel application of benchmark divergence**

I’ve been experimenting with a new way to look at MMC — not as a model scoring metric, but as a market structure indicator.

The idea is simple: compare Ender20 benchmark CORR20 and MMC against the average of the other 7 benchmarks. When Ender20’s relative CORR20 is rising (its factor exposures are winning) but its relative MMC is falling (its contributions are becoming redundant), that divergence may indicate the crowd is converging onto the same factor exposures — i.e., crowding.

**The smoothing method:**

Since live rounds take 20 days to resolve, I built a composite indicator that blends the latest 8 days of available live data. Each day-window looks back at a different number of recent rounds (day 1 averages 10 rounds, day 2 averages 9, down to day 8 averaging 3), with each window starting from the most recent round that has data for that day. Early-day readings are noisy but current; later-day readings are more mature but older. Averaging across all 8 windows produces a smoothed estimate that balances freshness with stability — essentially a near-real-time series built from overlapping live round data rather than waiting for full resolution.

The two charts below show Ender20 vs the average of the other 7 Numerai benchmarks. Chart 1 is Composite CORR20, Chart 2 is Composite MMC.

**What stands out:**

The pre-round-1170 peak shows Ender20 MMC leading (green shading in Chart 2 — independent alpha), followed by CORR convergence, then a sharp drawdown for everyone. In the current cycle, we see a similar early pattern of Ender20 MMC leadership after rounds 1210 and 1217, but the resolution so far looks different — a gradual rollover rather than a cliff.

At round 1231, Ender20’s CORR has just crossed above the other 7 while its MMC remains below — the first divergence in the dataset. Whether that’s meaningful or noise is TBD.

**Caveats:** This is entirely preliminary. 69 rounds of data, one benchmark comparison, and one divergence event is not a validated signal. I’m sharing it because I think using MMC as a structural risk indicator — separate from its role in payout scoring — is an unexplored direction that the community might find worth thinking about. The core logic (CORR measures accuracy, MMC measures independence, divergence between them reveals crowding) seems sound in principle even if the specific implementation needs much more work.

Interested to hear if anyone else has looked at MMC this way or sees flaws in the reasoning.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d02ca4d7b185086c10feb1c57b9e26e39d94ce39_2_690x253.png)image1297×476 76.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d02ca4d7b185086c10feb1c57b9e26e39d94ce39.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/9fce4e0c5d706c3d6bbd3cbe9ecc5e247c364ce6_2_689x265.png)image1292×498 85.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/9fce4e0c5d706c3d6bbd3cbe9ecc5e247c364ce6.png> "image")

---

### Post #3 — **greyone** | 2026-03-31 20:27 UTC

I think percentile view can offer unique insights as well.

Below is Phymirus’s Corr and MMC live 8 round percentile series (calculated as above)  
Phymirus slot is currently the history of ensemble of 8 Numerai’s benchmarks.  
(model development cycle has been rapid).

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2f0ee259c1ea71191e7035ab4bcad43a29c64065.png)image598×480 15 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2f0ee259c1ea71191e7035ab4bcad43a29c64065.png> "image")
