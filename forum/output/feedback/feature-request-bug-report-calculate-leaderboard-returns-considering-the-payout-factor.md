---
title: "Feature request/bug report: Calculate leaderboard returns considering the payout factor"
category: Feedback
url: https://forum.numer.ai/t/feature-request-bug-report-calculate-leaderboard-returns-considering-the-payout-factor/3317
created_at: 2021-05-16T10:51:16.411000+00:00
last_posted_at: 2024-03-28T02:24:17.907000+00:00
posts_count: 2
views: 859
tags: []
---

# Feature request/bug report: Calculate leaderboard returns considering the payout factor

---

### Post #1 — **ml_is_lyf** | 2021-05-16 10:51 UTC

I noticed that it doesn’t look like the returns on the leaderboard are taking into consideration the payout factor. I discovered this as I wrote a notebook to do the calculations for myself and noticed I get different numbers to the leaderboard unless I override the payout factor as 1 for all rounds. I’m assuming not including it was just an accident as the payout factor is pretty new, but I think it’s pretty important to include it in the calculations for the transparency of the tournament. More details here if you need them:

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/e56c9b/48.png)[Notebook to visualize historic model performance and see effect of different MMC multipliers and payout factors](<http://forum.numer.ai/t/notebook-to-visualize-historic-model-performance-and-see-effect-of-different-mmc-multipliers-and-payout-factors/3316/1>)

> Interestingly I noticed it looks like the 3 month and 1 year return on the leaderboard are not taking into consideration the roundPayoutFactor. I realized this as round 263 was my first round of seeing my 3 month returns on the leaderboard, and round 251 was my first staked round. But my 3 month return for ml_is_lyf on the leaderboard is 99.2%, and my performance for round 263 calculated above is 1.934420, which is a 93.4420% return. But you’ll notice if I set all the roundPayoutFactor to 1 (as if there was no payout factor) as I do below, then my calculated return is the same as on the leaderboard, with a performance of 1.991507, which is a 99.1507% 3-month return. I’ll make a separate feedback post about this issue.

---

### Post #2 — **ranzhang** | 2024-03-28 02:24 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/e56c9b/48.png)[Notebook to visualize historic model performance and see effect of different MMC multipliers and payout factors](<http://forum.numer.ai/t/notebook-to-visualize-historic-model-performance-and-see-effect-of-different-mmc-multipliers-and-payout-factors/3316/1>)

> Interestingly I noticed it looks like the 3 month and 1 year return on the leaderboard are not taking into consideration the roundPayoutFactor. I realized this as round 263 was my first round of seeing my 3 month returns on the leaderboard, and round 251 was my first staked round. But my 3 month return for ml_is_lyf on the leaderboard is 99.2%, and my performance for round 263 calculated above is 1.934420, which is a 93.4420% return. But you’ll notice if I set all the roundPayoutFactor to 1 (as if there was no payout factor) as I do below, then my calculated return is the same as on the leaderboard, with a performance of 1.991507, which is a 99.1507% 3-month return. I’ll make a separate feedback post about this issue.

yes! It’s quite strange
