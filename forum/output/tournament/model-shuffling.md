---
title: "Model shuffling"
category: Tournament
url: https://forum.numer.ai/t/model-shuffling/1223
created_at: 2020-11-24T01:49:22.838000+00:00
last_posted_at: 2021-05-24T16:57:05.720000+00:00
posts_count: 7
views: 1318
tags: []
---

# Model shuffling

---

### Post #1 — **liz** | 2020-11-24 01:49 UTC

are there any obvious advantages or disadvantages to model shuffling? what i mean is some variant of :

  * suppose i have 10 good models
  * instead of posting weekly predictions from model A to numerai model account a, B : b, etc…, models {A,B,C,D,E,F,G,H,I,J} predictions are shuffled before being posted to numerai, so they may end up A : c, B : e, etc.



i keep wondering if this might accomplish masking some signal, and if masking signal would enable the user to achieve more sustained MMC. these are my intuition but this is super-not-my-field.

---

### Post #2 — **lackofintelligence** | 2020-11-24 02:28 UTC

I do that all of the time. I try to keep them constant, but sometimes I have to rotate them. One reason to rotate them is if I need a boost to my earnings and the best model does not correspond to the higher staked models. Its much easier to do that then to pull a stake and restake it on another model. Zero tax consequences too. Have not seen anything bad other than ranks getting shifted a bit. It will not have any effect on MMC, it will only cause interested parties to wonder what is going on there. It has no negative effects to the Hedge Fund either since they look at the test set scores and stake to determine the model weight for the MM at the outset of every round.

I think it actually helps the Hedge Fund if you rotate models the way I have outlined.

---

### Post #3 — **liz** | 2020-11-24 02:50 UTC

that makes sense, thanks!

i think my thoughts about MMC stem from assuming that the Hedge Fund can use predictions submitted to them to improve their own models. and that somehow, faithful model submissions would improve that for them, compared to shuffled model submissions.

---

### Post #4 — **wigglemuse** | 2020-11-24 15:22 UTC

Shuffling makes no difference to the fund – there is no past at all as far as the fund is concerned. Each week is brand new and they create a whole new metamodel. The idea that if users submitted the same models persistently (and in the same slots) it is better for the fund somehow is a common misconception about the tournament.

From the user side, the only major reason it would matter is to stake differently on a model week-to-week, i.e. moving a model that has a current stake on it of 10 NMR to another slot that also has a current stake of 10 NMR is mathematically pointless staking-wise, but if you have different stakes on different slots than you might move them around for quick staking changes without having to actually add or remove overall stakes.

---

### Post #5 — **crownholder** | 2021-05-24 09:29 UTC _(reply to #4)_

Is this true and is there solid proof? Because my analysis seems to indicate there is a benefit to persistent use of the same model once a high performing model is created.

---

### Post #6 — **wigglemuse** | 2021-05-24 14:51 UTC _(reply to #5)_

Is what true exactly? My comment above was strictly about whether Numerai cares [from a technical standpoint] if you submit the same model in the same slot each week. (They don’t.) There is sometimes a misconception that Numerai is tracking your model over weeks or months to tune the metamodel better or something, but like I said they recreate the metamodel each week from scratch with the predictions submitted only for that round, and anything submitted for previous rounds or previous performance of your model (or your ranking on the leaderboard) is not factored in at all. Only your stake amount for that round is a factor in how your model is weighted in the metamodel. [However, the implementation of this actually wasn’t 100% right for the last so many months because for a while they had the stake-change deadline in the middle of the week, but now it has been moved back to be the same as the submission deadline where it should be so they can be sure to have accurate staking amounts when they do their real life trades.]

But anyway, it sounds like you are saying there is benefit TO YOU in sticking with the same model for a while (not worrying about every down round, etc) and not changing up all the time. And that is probably true, at least as long as it is a decent model. And yes, what’s good for you is good for Numerai if you make wise decisions about which models to submit and how much to stake on them. But that wasn’t what I was addressing at all.

---

### Post #7 — **mindyoself** | 2021-05-24 16:57 UTC _(reply to #6)_

It would be reasonable to try it at least to build a solid background and track record for each.
