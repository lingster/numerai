---
title: "What to do with the 'New Targets for the Tournament'"
category: Tournament
url: https://forum.numer.ai/t/what-to-do-with-the-new-targets-for-the-tournament/5845
created_at: 2022-11-13T12:36:12.150000+00:00
last_posted_at: 2022-11-15T22:57:55.563000+00:00
posts_count: 9
views: 1015
tags: []
---

# What to do with the "New Targets for the Tournament"

---

### Post #1 — **taori** | 2022-11-13 12:36 UTC

[New targets](<http://forum.numer.ai/t/new-targets-for-the-tournament/>) have been just released and I am now evaluating how to use them. I would be also curious to know what other users think.

I have already tested the targets, all of them, with my models and the results were that they are not good. What exactly means “they are not good”? From a user perspective “being good” means that you can make NRM out of them. We have only two ways to make money with them: corrrelation w.r.t. target_nomi_v4_20 or TC.

Unfortunately we still don’t have a way to test TC, so I cannot know how good these targets are on TC, unless I submit them and wait for live performance (this seems amateur hour compare to the high standards we have in ML for model evaluation). So we are left with only one option: use the new targets to stake on correlation w.r.t. target_nomi_v4_20. With my models the results are not that great.

Apparently I have no reason to use these new targets. Why don’t Numerai allows us to stake on the correlation with these targets If they believe they are good?

---

### Post #2 — **wigglemuse** | 2022-11-13 16:50 UTC

What is your opinion of the other 19 alternative targets we already had compared to the new ones we just got?

---

### Post #3 — **taori** | 2022-11-13 17:20 UTC

The performance of my models trained on these new targets looks better.However the performance are lower then what I get when training my models on target_nomi_v4_20. These alternative targets should be good for TC, but I cannot test it so I don’t know what to do with them.

---

### Post #4 — **kayeffnumeraitor** | 2022-11-13 19:12 UTC

“What means good?” is definitively a good question. Don’t know if you are already doing it but what might help is to measure the performance not in “mean corr” but to factor in the volatility of your model, so something like sharpe, which is somewhat related to FNC, and reevaluate.

In a quick training session with a simple lgb model the new target “ralph” didn’t perform well for me, though.

I guess in the end you’ll have to do the same as always: try it out and hope it works, see that it works, then stake on it and observe afterwards how you are burnt to hell ![:slightly_smiling_face:](http://forum.numer.ai/images/emoji/twitter/slightly_smiling_face.png?v=12)

---

### Post #5 — **kayeffnumeraitor** | 2022-11-13 20:13 UTC _(reply to #4)_

Reading the announcement post again I think one problem for evaluating the new target on our side is that we obviously cannot do any sort of risk analysis like Numerai can. However, the new targets might enhance the prediction quality of your model for those stocks that are more likely to survive the risk constraint optimization step (good for TC) as some of the new targets seem to be playing around with different risk factors. I imagine the new targets as playing around with “regularization”, so I assume more regularized targets may look worse during training.

So while for pure corr metrics the new targets might not be helpful on paper, the idea is that they give you some playground for improving on TC.

---

### Post #6 — **nyuton** | 2022-11-14 08:32 UTC

I appreciate the work the Numerai team is doing to improve data, targets, daily rounds etc. That’s what we need for the future success of Numerai. However we need help to fully unleash it’s potential [@pschork](</u/pschork>) [@slyfox](</u/slyfox>) [@richai](</u/richai>)

**What is needed in the order of priority:**

  1. MetaModel correlation metric in the diagnostic. This should be easy and MM correlation is correlated with TC
  2. TC in the diagnostics. Given that you have the metamodel from the past, it should be possible to come up with an estimation of TC. I understand the difficulties here, but an approximation with some limitations should be possible. That would be a hugh improvement.
  3. Lacking the above 2 points, we need MORE model slots, because that’s the only way to get an idea on model TC.
  4. Given the sheer number and size of models we submit daily, uploading and managing them is cloud with compute is troublesome in many ways and potentially expensive. I submit my staked model with compute from the cloud, but I submit the other 40+ locally. I’ve built my own scheduler for daily submission, but extending “compute” to this use case and make it easier for new joiners would be helpful.

---

### Post #7 — **joakim** | 2022-11-15 01:30 UTC _(reply to #6)_

A few more things that would be quite useful IMO:

  * Metamodel predictions for all resolved rounds
  * Post-optimised Metamodel rankings for all resolved rounds
  * Metamodel performance on the leaderboard fully backfilled
  * Benchmark models performance for all targets fully backfilled

---

### Post #8 — **robo_boi** | 2022-11-15 14:29 UTC

I’d like to use the new targets but I’m out of model slots

---

### Post #9 — **taori** | 2022-11-15 22:57 UTC

I agree, more slots and then also account level staking.
