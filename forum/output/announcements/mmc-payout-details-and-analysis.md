---
title: "MMC - Payout Details and Analysis"
category: Announcements
url: https://forum.numer.ai/t/mmc-payout-details-and-analysis/220
created_at: 2020-04-21T19:43:20.051000+00:00
last_posted_at: 2020-04-21T19:43:20.164000+00:00
posts_count: 1
views: 4400
tags: []
---

# MMC - Payout Details and Analysis

---

### Post #1 — **master_key** | 2020-04-21 19:43 UTC

# MMC Payouts and Other Tweaks

Users today experience quite a lot of volatility in the tournament. Even the top, most consistent users can experience significant swings.

With MMC payouts, users will have access to a scoring system that improves the current tournament structure in three main ways:

  * More consistent payouts (less burn periods and less severe burns)
  * More efficient allocation of the payout pool towards top contributing users
  * Not easily exploitable



## How to Participate

Users will be able to opt-in or opt-out of MMC for each of their models by simply checking a box on their model page.

At the open of each round, if a model is checked for MMC, then their stake gets locked in for the MMC tournament for that round.

If they opt in for MMC, then they will get paid out ONLY ON MMC.

Otherwise, they will continue being paid on the normal tournament.

Users are allowed to play either tournament with any model for each week.

## The Structure

The MMC tournament has a similar payout curve to the primary tournament. Your payout/burn will be your stake-amount for the round multiplied by your MMC score for the round, multiplied by 2. It will be capped at ± 25% of stake just like the primary tournament.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/e6ec9313ffa7f3bdb043140cc594896225d06371_2_418x393.png)617×581 10.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e6ec9313ffa7f3bdb043140cc594896225d06371.png>)

Due to the increased stability (lower volatility/risk) of MMC, multiplying profits/losses by 2 brings the risk/reward in-line with the primary tournament for the average user. Users who benefit less from MMC would still prefer to play the primary tournament, and users who benefit more from MMC will have significantly more stable (and much higher) returns by playing MMC.

Note: MMC models and Regular models still contribute to the stake-weighted metamodel in the exact same way when calculating MMC scores. The only thing that changes is the payout basis.

# Benefits of MMC payouts

The very top users are far more profitable on MMC than in the Primary Tournament.

If we look at the payout structure for the main tournament, we can calculate a risk-adjusted return rate for some top users by dividing the mean of their round scores by the standard deviation of their round scores. I’ll refer to this metric as the sharpe. Since correlation and payout are perfectly correlated, we can roughly interchange correlation-score and payouts in our analysis.

(Although for the earnings calculations below I do consider compounding stake effects.)

However, if you look at mmc sharpe (the mean of a user’s mmc scores divided by the standard deviation of a user’s mmc scores), we can see that risk adjusted returns go up dramatically.

integration_test (rank ~30 main, rank ~60 MMC)

sharpe: 0.21 → 0.71

earnings: 26% → 65%

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a48dd72ff1ecba4c6c8319f0899e227d2bdf97a3.png)376×267 11.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a48dd72ff1ecba4c6c8319f0899e227d2bdf97a3.png>)

For integration_test, we see a correlation sharpe of 0.217.  
In fact, even the best users only have a correlation sharpe of less than 0.6.  
But integration_test mmc sharpe goes up more than 3x to 0.71.

And NMR earned on initial NMR investment goes up dramatically as well. By today, integration_test stake value would be at +65% vs +26% in the main tournament.

And other top mmc users see incredibly dramatic increases in profitability.

* * *

dataman_ai (rank ~100 main, rank ~20 MMC)

sharpe: 0.19 → 0.60

earnings: 16% → 101%

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/8b8f72d24c9e3057aa4ca9977a6700c204daa342.png)376×267 11.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/8b8f72d24c9e3057aa4ca9977a6700c204daa342.png>)

* * *

nasdaqjockey (rank ~10 main, rank ~14 MMC)

sharpe: 0.56 → 1.26 (!!!)

earnings: 62% → 185%

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/9909e9007bc65717e316e7642856eb7a2d3e1bd6.png)383×267 11.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/9909e9007bc65717e316e7642856eb7a2d3e1bd6.png>)

* * *

These users have unique models (low correlation with stake-weighted metamodel) which also perform very well on an absolute basis. These are the types of users that we especially want to reward with very consistent payouts. They improve the metamodel round after round, but so far have still been exposed to burns which may be caused more by the limitations of the data provided rather than the model itself.

With MMC though, if you consistently do better and more unique things with the data than everyone else, you will be consistently rewarded despite burn periods.

A few stats:

  * Out of the top 100 users currently on the main leaderboard, 84 of them would have higher returns on MMC than on the main tournament.

  * By contrast, ranks 200-300 would only have 37 users with higher payouts on MMC than on the main tournament.

  * Only 5 users in the top 100 would have worse drawdowns on MMC than on the main tournament.

  * For ranks 200-300, 31 users would have worse drawdowns on MMC.




(Note that I chose a cutoff of rank 300 to show here because that’s roughly the amount of users who have >= 0 reputation as of writing)

MMC better allocates the payout pool to the users who are contributing to the metamodel the most, without needing a leaderboard bonus add-on.

For top users, it increases both returns AND consistency.

## Leaderboard Bonus Removal

The leaderboard bonus will be phased out in the coming months.  
We know that this is a large portion of profitability for most users in the tournament today, but we do not see it as a fit for the long-term vision of Numerai.

We see MMC as a more stable replacement which still allows high returns.

Another downside to the leaderboard bonus is that we are already at the 250 NMR per day cap.

This means the “3% a day” payout is effectively 2.7% a day now. That number will continue to shrink as the tournament grows. 100 days from now, stakes will be nearly 4x what they are today. This means all of the leaderboard bonuses will be much much smaller relative to stake amounts.

There are a few reasons why we are opting not to keep the leaderboard bonus in place permanently. A primary reason is simply that it is susceptible to some certain attacks in which a bad-actor could game the tournament and guarantee high payouts for himself with minimal risk.

## Raising the Stake Limit

As of today, there is a 100k NMR stake limit. If total stakes exceed 100k, stakes are selected pro-rata. We are at >70k NMR staked today. As that number increases, payouts will be reduced even further in the tournament.

We will be increasing that stake limit to 200k NMR immediately.

With MMC starting, there may be an uptick in stakes, and we want to be sure that users can continue earning a high return on NMR for a long time into the future without throttling.

As MMC and the primary tournament have attack resistance as a core design goal, we can safely increase this limit without the same fear of exploitation that we would have for something like the leaderboard bonus.

## Continuous Staking Improvements

One of the top complaints is that earnings from each round get automatically rolled back into stake. While we’re changing stakes around, we want to give users this small but much requested change: an option to put profits directly into the wallet instead of into the stake.

# Timeline

  * MMC Payouts: May 31

  * Leaderboard Bonus Discontinued: Wednesday, September 9, 2020

  * Continuous Staking Improvements: soon (bother slyfox if you want it sooner)




* * *

* * *

* * *

### Payout Charts Appendix

One more set of charts to look at: Actual stake value per week for integration test for different leverages for each payout curve.  
The purpose of this is to show that MMC is not only better because of the leverage (tighter payout curve=2x leverage); Because of the improved consistency, users are actually able to benefit more from higher leverage on MMC than they would be able to benefit from higher leverage on the primary tournament.

I will also show dataman_ai as a great example of how different MMC can be for the right type of model.

Notice the consistency and the near absence of drawdowns as well, not just the final stake values.

Integration Test:

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/d57b172cc7bad3852a0deaf8487460b0b7d76ed2_2_265x186.png)764×520 50.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d57b172cc7bad3852a0deaf8487460b0b7d76ed2.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/9791637a013f6c48be78ef0374cda6596410181a_2_265x186.png)782×536 51.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/9791637a013f6c48be78ef0374cda6596410181a.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/20175309afcbbd486dddb0eb2317ed9cb46e8e4d_2_265x186.png)762×532 50 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/20175309afcbbd486dddb0eb2317ed9cb46e8e4d.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/1970daa798eab10a810cfe8ab4673f6f300f0299.png)376×267 11.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/1970daa798eab10a810cfe8ab4673f6f300f0299.png>)

Dataman_ai

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/9c1b40e32fedc5c4fea582aad41208a291221e8e.png)376×267 11.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/9c1b40e32fedc5c4fea582aad41208a291221e8e.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/b1db6e71c506dde6c4fde84c48fded661cc7dcef.png)376×267 11.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/b1db6e71c506dde6c4fde84c48fded661cc7dcef.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e7d88579002849ba45bd3e7cac3fb5195ae1bd55.png)376×267 12 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e7d88579002849ba45bd3e7cac3fb5195ae1bd55.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/23702076c0cec26817d2ed3198da430dd8784a26.png)376×267 11.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/23702076c0cec26817d2ed3198da430dd8784a26.png>)
