---
title: "Feature request - portfolio stake"
category: Feedback
url: https://forum.numer.ai/t/feature-request-portfolio-stake/1235
created_at: 2020-11-28T12:40:56.002000+00:00
last_posted_at: 2020-12-16T22:22:43.728000+00:00
posts_count: 7
views: 1239
tags: []
---

# Feature request - portfolio stake

---

### Post #1 — **belzebot** | 2020-11-28 12:40 UTC

Hi,

I think it would be a very good improvement of stake management if we could balance easily our stake between our models. What I have in mind is something like a weight vector that would allow us to allocate % of our stake between our models. This would go together with an easy pull of the performance of all our models through time. This way we would be able to manage our different models like we would with a portfolio of strategies.

More specifically, we would still have our stake “frozen” account-wise but it would be freely re-allocatable between our models. (without having to first withraw and then re-stake on another model)  
Let me know what you think, I don’t see any drawback for Numerai.  
Cheers

---

### Post #2 — **lackofintelligence** | 2020-11-28 18:59 UTC

This idea has the potential to greatly increase metamodel performance.

---

### Post #3 — **dnos** | 2020-12-04 11:13 UTC

I think this feature would defeat the purpose of staking which is to express confidence in the portfolio you prioritize. If people moved their stake around when models failed or another of their models were doing especially well it would encourage a thought process of hedging bets rather than pursuing originality. Besides it’s less mentally taxing to divide your total stake into portions, match them to your models and switch where your different algorithms submit.

As LeBron says, “keep the number one thing the number one thing”

---

### Post #4 — **lackofintelligence** | 2020-12-13 18:26 UTC

The idea, the canonical financial technique, is to weight models proportionally to their probability to perform well. With the domination of MMC, performance is tightly coupled to originality, so this process also selects models that are more original. In my experience models that have characteristics that appear in Numer.ai discussions usually end up getting weighted less through this process. For example, presently none of my xgboost models would get exceptional weighting.

---

### Post #5 — **krizmanic** | 2020-12-14 04:57 UTC

Love the idea. I’ve been wrestling with this myself. I have several great models (probably more coming) and would love a way to not have to lose 4 weeks of staking, just to spread out the risk a little across models.

---

### Post #6 — **belzebot** | 2020-12-14 15:13 UTC

[@dnos](</u/dnos>), I think it would still help since we would be able to weight our stake with live/test performance and not only on validation performance, which given the non-stationary nature of the market is important. Further, most people ensemble multiple models, and thus kind of lose sight of each model’s performance. The fund would be better off if it could have access to each individual model to build the meta-model instead of ensembles. Thus, it would allow the users to submit their component models and then to balance their stake more dynamically while the fund could benefit from a greater variety of models.

---

### Post #7 — **dnos** | 2020-12-16 22:22 UTC _(reply to #6)_

I think I see your point now. By having an incentive to take a more active role in prediction performance, anyone would be able to ensure their best predictions are passed on to the meta model by altering their stake. It likely could and would lead to alpha in the short run but it’s equally likely (if not more likely) to lead to over-fitting and burns in the long run. Certainly participants would benefit from the extra capital and it would inflate NMR to sky high limits but it isn’t a sustainable solution to the burn of hard times. Participating in the tournament we’re guaranteed to lose and it wouldn’t express confidence to double back after the fact because then winning the game has nothing to do with our process and everything to do with manipulation.

We may be training algorithms but in truth we’re the ones being trained into what is designed to be a super intelligence. It’s like we’re all raising a child and everything that we think and do will impact their behavior. It’s not enough for the meta model to be a capable investor, it needs to be an omniscient one.
