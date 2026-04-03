---
title: "I am bored therefore I write"
category: Tournament
url: https://forum.numer.ai/t/i-am-bored-therefore-i-write/6667
created_at: 2023-09-14T13:18:08.194000+00:00
last_posted_at: 2023-09-14T13:18:08.290000+00:00
posts_count: 1
views: 627
tags: []
---

# I am bored therefore I write

---

### Post #1 — **taori** | 2023-09-14 13:18 UTC

From yesterday on discord (I don’t like discord, I prefer the forum so I write here):

![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/2210acec22c58235fd81c150b92eb38bd1d97c29_2_690x46.png)

> anyone like removing “degenerate” TC payouts? if your TC is positive in a round but your Corr v2 is negative, you cannot earn on TC staking. If your TC is negative but your Corr v2 is positive, you can’t burn on TC? this would make TC like a bonus only when it corresponds to your Corr not when it noisily happens not to?

which translates to:
    
    
             Prediction                   Payout
    Positve  CorrV2 & Postive  TC  =  1xCorr + 3xTC
    Postive  CorrV2 & Negative TC  =  1xCorr
    Negative CorrV2 & Postive  TC  = -1xCorr
    Negative CorrV2 & Negative TC  = -1xCorr - 3xTC
    

This seems an interesting idea that requires a thorough analysis before being implemented, but still interesting.

But then the venerable wigglemuse has always the best comment:

![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c5ab4ae75203299cdc42a1580dd74fe887998f33_2_690x46.png)

> Sounds interesting. Not necessarily good. But geez … all these multipliers and weird rules – this is a big load of nonsense to a new user. Any reset of the scoring should also entail a radical simplification of the whole thing, should it not? It has got one hack after another piled on…get back to basics.

How can wigglemuse be so on point every time they say something? Kudos.

However that’s not what I wanted to discuss.

I would like to remind that TC is a change in contribution. TC should be called “CTC=change in true contribution”: If the fund requires a model at X stake amount, than the model TC will be positive/negative at each round depending on how much its stake deviates from X. This is the source of the noise. If the payout was based on X (instead of the gradient) then we wouldn’t have so much noise and it would also be a fair payout. A payout based on TC is wrong on a [theoretical level](<http://forum.numer.ai/t/true-contribution-for-dummies>).

While I cannot accept a payout based on TC, it might be that TC is an important tool for the fund. I can see the theoretical reasons for that, but I am still waiting for Numerai to share some serious analysis that shows that TC works in practice and maybe reassure us that the recent fund bad performance have nothing to do with TC.

Regardless of whether we stick to TC (Lord please spare us) or not, there is a clever way to make the payout more fair (fairer?) and help the fund at the same time… plus a caveat.

Currently the payout is based on the performance of the model predictions on the latest round only. Making the payout dependents on the last X rounds (the history of a model) would introduce so many issues (I hope these are obvious and I don’t need to explain them) that it is not feasible. However an important improvement would be to ask the users to provide, at every round, the predictions for the live data plus a selection of X random old eras and make the payout based on the average prediction performance of these X rounds. This not only would promote models that work consistently good and hence are more useful to the fund, but it would also produce less noisy payouts.

The caveat is that the results of the X old eras are known, so there is no way to prevent the users from cheating. To avoid that the X old eras should be replaced by synthetically generated data, which might not be easy to do, because the synthetically generated era data would have to be consistent with real market data to make them useful to the Numerai’s fund.
