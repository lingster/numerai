---
title: "Announcing new payouts system mini-release"
category: Announcements
url: https://forum.numer.ai/t/announcing-new-payouts-system-mini-release/2469
created_at: 2021-03-20T22:44:03.627000+00:00
last_posted_at: 2021-03-20T22:44:03.966000+00:00
posts_count: 1
views: 2653
tags: []
---

# Announcing new payouts system mini-release

---

### Post #1 — **pschork** | 2021-03-20 22:44 UTC

> New (& OG) Users: If you are not familiar with the staking threshold and how it impacts payouts, please take a look our recently updated [Payouts documentation](<https://docs.numer.ai/tournament/learn#payouts>).

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/60aadaef96f82d9f735e60e99246ecc89f3a8601.png)image636×260 13.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/60aadaef96f82d9f735e60e99246ecc89f3a8601.png> "image")

With the Numerai tournament approaching 300,000NMR at stake, we are rolling out a redesigned payouts subsystem that provides more transparency and flexibility for tuning.

> Note: There are no actual payouts configuration changes in this release - we are just releasing a new payouts subsystem and surfacing it’s features in the frontend. Any future payout configuration changes will be announced separately and will typically coincide with new data release or other major releases.

The tournament has always had a staking threshold, and our payout system has always supported pro-rata payouts, but the staking threshold was never hit because we would always increase it to maintain a payout factor of 1 and avoid triggering pro-rata payouts for users. But Numerai can’t continue doing that forever because of this thing called [exponential growth](<https://makeameme.org/meme/exponential-growth-boy>).

This time around, there are no plans to increase the staking threshold. When the total NMR at stake breaches the staking threshold (300k Classic, 100k Signals), a payout factor will be calculated and applied per round to both payouts & burns

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/2d4e9a28efaf5113d04463cec955d955e7c97021_2_690x280.png)image1604×652 66.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2d4e9a28efaf5113d04463cec955d955e7c97021.png> "image")

While the legacy payout system calculated a valid payout factor, it was opaque and not propagated. Additionally our payout multiplier types (CORR, MMC) were tightly coupled and not easily changed or expanded.

The new payouts system now exposes all of these values and configurations parameters per round. New rounds will have a `null` payoutFactor until round `scoreTime` when payout factor is determined after all pending stake changes are confirmed.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/c3a7424dfa68086521194b11e9d22f6a319f0fdf_2_690x412.png)image1900×1136 205 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c3a7424dfa68086521194b11e9d22f6a319f0fdf.png> "image")

You can track the round payout factor on the model submissions performance page

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/679608add539ee646f0d80ace7c05a991037fbd7_2_690x425.png)image1940×1196 218 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/679608add539ee646f0d80ace7c05a991037fbd7.png> "image")

The staking modal also has a payout factor calculator showing projected payout factor based on the proposed stake change.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/aeb281d181bb43737c10c8646f6acb7ae3885655_2_361x500.png)image1220×1688 169 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/aeb281d181bb43737c10c8646f6acb7ae3885655.png> "image")

**FAQ**

**What changes are you planning to make to payouts?**  
Expect major adjustments of staking threshold and payout multipliers in the near future as the tournament continues to evolve (new data, new scores, new tournaments).

**Why are you doing this?**  
We think Signals should be more profitable than Numerai, and that MMC should be significantly more profitable than CORR (especially as the tournament grows). Expect changes to MMC multipliers and stake thresholds to shepherd these outcomes.

**When should we expect payout configuration changes?**  
Soon. Changes to payouts configuration will be announced separately with as much advance notice as possible. As before, we will never change payouts to ongoing or past rounds.
