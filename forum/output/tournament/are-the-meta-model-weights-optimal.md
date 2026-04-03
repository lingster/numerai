---
title: "Are the Meta Model weights optimal?"
category: Tournament
url: https://forum.numer.ai/t/are-the-meta-model-weights-optimal/6378
created_at: 2023-05-19T08:01:54.476000+00:00
last_posted_at: 2023-08-06T11:45:38.724000+00:00
posts_count: 3
views: 1020
tags: []
---

# Are the Meta Model weights optimal?

---

### Post #1 — **thornam** | 2023-05-19 08:01 UTC

This might be a newbie question, so please enlighten me

What are the reasons for the Meta Model control to be based on the amount staked?

I get that using the staked amount for the MM control, the model self-corrects in terms of increasing/decreasing the weights on good/bad models. However, doesn’t it also introduce a bias towards models made from people with more money or models made from people who are willing to take on more risk.

Wouldn’t it be more optimal to base the MM control on the, say, 1-year tc score or in some other way on the ranking of models?

This would result in the MM to also self-correct by holding higher weights for good vs. bad models, but without having a bias towards models from people with higher risk willingness

---

### Post #2 — **wigglemuse** | 2023-05-19 15:02 UTC

Yes, that’s been discussed a lot. Short answer seems to be it works pretty well this way, and they haven’t found a better way. (So if you’re thinking “well that can’t work”, well … it does work.) So the question is what might work better without untenable drawbacks?

Any score-based metric kind of takes away our ability to switch/change models at will – remember they have no idea how our predictions are derived, and today’s model may not be the same as yesterday. Also anything with scores requires a long history. I suppose they could take historical (staked) performance of the person as evidentiary weight of their competence (which still requires history, but disregards changes to models). So long-participating participants could have some additional internal tweak to their weights, and newbies could be downgraded somewhat or something like that. But those adjustments would be minor – if you based everything on historical performance there would be several major problems with that (attack vector, metamodel cannot adjust quickly, etc). The main mitigation factor to possibly too much influence by a small number of stakers is simply to have as many participants as possible. Truth is there is no way to automatically derive optimal weights, but if you’ve got something that is working well (and it is), better to think twice before making major changes. Not that they’ve been afraid of making changes – they did add TC scoring (which was unproven and quite different) to simple corr scoring and made that more important – and now corr scoring has just changed also. So stakers are required to react to these changes.

So yeah, it is tempting to think there was got to be a better (and more complex!) way to do it, but once you try to figure out exactly how what that something would actually work, it becomes quite tricky and reveals its own problems or constraints (they don’t want to end up like every other hedge fund – that’d be missing the whole point). Something simple that works very well is hard to beat…

---

### Post #3 — **nmrdragon** | 2023-08-06 11:45 UTC

Idea: base the weighting on real time correlation with other predictions: give more weights to predictions that have a high correlation with the best models’ predictions and that also have a low correlation with the worst models’ predictions. The best models may be the models that were getting some good scores in recent rounds or models with the highest stakes in the current round. By using multiple models the effect of model changes or effect of different personal wealth or risk taking appetite is mitigated. Maybe this could be also a score for payouts so the staking and weighting would be more aligned. I know this is probably dumb and already thought about ![:grinning:](http://forum.numer.ai/images/emoji/twitter/grinning.png?v=12) but there’s always a small chance that it will lead to a good idea.
