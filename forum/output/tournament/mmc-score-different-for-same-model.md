---
title: "MMC score different for same model?"
category: Tournament
url: https://forum.numer.ai/t/mmc-score-different-for-same-model/84
created_at: 2020-03-26T18:05:31.351000+00:00
last_posted_at: 2020-04-19T21:11:32.630000+00:00
posts_count: 6
views: 1427
tags: []
---

# MMC score different for same model?

---

### Post #1 — **blockrocket** | 2020-03-26 18:05 UTC

Anyone have an idea why the same model submission gets the same Correlation, but slightly different MMC? Seems the first one submitted gets a slightly better score, is ‘first submitted’ used in MMC calculation?

---

### Post #2 — **bor3** | 2020-03-26 18:13 UTC

If you have many entries in the submission with exactly the same score, then there is some randomness in calculating a spearman correlation - the equal-score entries have to be put into an ordered rank somehow, and that would affect your score, even though you submit the same predictions.

Not sure if that is what is happening, but it might be.

---

### Post #3 — **quantnosticator** | 2020-03-26 18:15 UTC

If I understand it, there is a bagging process used (iterations of subsampling), which is random, so MMC is not 100% deterministic. It shouldn’t be a big variance though. (If there is, they need to increase the number of bagging trials.) It wouldn’t be from ties – those are handled consistently.

---

### Post #4 — **blockrocket** | 2020-03-26 18:17 UTC

thanks for the responses…i will keep an eye out but so far in every case (only a few) I observed that order submitted does slightly better.

---

### Post #5 — **quantnosticator** | 2020-03-26 18:22 UTC

If this is regarded as a problem, they could set a consistent random seed before each round of bagging so it would always turn out the exact same when the predictions are identical. But still as long as they do it using that procedure the MMC score itself will always have an element of randomness at the right-most decimal places…

---

### Post #6 — **master_key** | 2020-04-19 21:11 UTC

As [@quantnosticator](</u/quantnosticator>) has said, it is due to bagging. For compute efficiency, we do a smaller number of bags in the unresolved rounds (for daily updates), and then on round resolution we use a lot of bags to minimize the random factor. So until the round resolves you are likely to see more randomness, but when we actually calculate your final score (and eventually payouts) the random factor will be miniscule. We will increase the bag size even more when payouts are released too.
