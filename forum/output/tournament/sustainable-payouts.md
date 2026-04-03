---
title: "Sustainable Payouts?"
category: Tournament
url: https://forum.numer.ai/t/sustainable-payouts/2561
created_at: 2021-03-27T21:38:03.077000+00:00
last_posted_at: 2021-03-27T21:47:46.973000+00:00
posts_count: 2
views: 1102
tags: []
---

# Sustainable Payouts?

---

### Post #1 — **joakim** | 2021-03-27 21:38 UTC

Are the current Numerai tournament payouts sustainable? In order to attempt to answer this question I’m making the following assumptions:

  * NMR price: $50/NMR (constant)

  * Staked amount: 300,000 NMR (constant)

  * Annual average return on stake: 200%

  * Current Numerai treasury: 5,000,000 NMR (??)

  * Fund fee structure: 2/20 (of which 10% of profits is for paying participants).

  * Fund leverage: 4x

  * Annual average fund return: 20% (reasonable, in order to attract investors money)

  * No further outside capital being raised.




With these assumptions Numerai pays out 600,000 NMR each year (more as payouts compound weekly, but I’m trying to keep it simple), so it will take 8.33 years until Numerai runs out of NMR in their treasury.

600,000 NMR = $30,000,000 USD

At this point the fund needs to generate $300,000,000 USD annually in profits in order to pay participants, assuming they allow 10% of profits to be returned to participants.

In order to generate $300,000,000 USD in annual profits at 20% of capital, that means $1.5 billion USD in total allocated capital. At 4x leverage that means $375 million in AUM.

Is having $375 million in AUM in 8 years possible? Definitely, but it won’t be because they’ve been successful at pitching the fund to investors as a fund powered by a global network of data scientists and AIs (I hope they don’t do this). That’s all nice and stuff but investors care about one thing only: Returns. Or risk adjusted unique returns to be specific.

I believe [@richardcraib](</u/richardcraib>) has presented previously that the backtest (test set) had a Sharpe Ratio of 2. Backtests are not the same as live performance of course but if they can show anywhere close to that on live performance, they won’t have any problems raising investors money. A Sharpe Ratio of 1 is probably enough, especially if their portfolio is somewhat unique.

Some of my assumptions might be completely off of course, but I tried to keep them somewhat reasonable. If they can achieve a live Sharpe Ratio of 2 investors will be begging them to take their money. I don’t think we’re quite there yet though.

Thoughts? Personally I would stop paying for common CORR, as this is not worth anything unless it contributes to the meta model’s performance. I would probably also limit round payouts to some pegged fiat amount.

---

### Post #2 — **richai** | 2021-03-27 21:47 UTC

We’ve been working on 10xing the data. A lot of what we decide on payouts has to depend on how much easier/harder the new data makes the tournament. We also have a lot of other ideas. I tend to agree that staking CORR on eg preds right now is very profitable for users but in an unsustainable / not that helpful way to Numerai vs other things. But we can’t change it before we get further with the new data.
