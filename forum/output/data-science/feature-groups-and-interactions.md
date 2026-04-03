---
title: "Feature Groups and Interactions"
category: Data Science
url: https://forum.numer.ai/t/feature-groups-and-interactions/1324
created_at: 2020-12-17T12:34:10.739000+00:00
last_posted_at: 2020-12-23T09:01:06.636000+00:00
posts_count: 9
views: 1643
tags: []
---

# Feature Groups and Interactions

---

### Post #1 — **shonumerai123** | 2020-12-17 12:34 UTC

There are 6 groups of features in the dataset as everyone knows and I’ve been always thinking there should be some reasons behind that.  
Followings are the avenues I’ve tried to explore so far:

  1. Train models on a feature group (i.e. Dexterity only, Strength only etc), a combination of feature groups (i.e. Intelligence & Strength, Dexterity & Charisma & Constitution etc). There can be so many variations. Take subsets from each group and combine them, ensemble predictions etc etc.

  2. Generate some representative features from each feature group (e.g. PCAs, correlations, stds…) and use them for predictions.

  3. Limit interactions within a feature group and look at interactions with other feature groups only. (I’ve tried a XGBoost version below.)  
<https://xgboost.readthedocs.io/en/latest/tutorials/feature_interaction_constraint.html>




None of these attempts have led to any meaningful improvement in the metrics so far, unfortunately…

Has anyone tried something similar? Will be great if you could possibly share you 2 cents. Thanks!

---

### Post #2 — **arbitrage** | 2020-12-21 18:25 UTC

I tried the XGBoost feature interaction constraint and notice no discernable difference between using it and not using it. I have since abandoned the project. I do believe that the next frontier in model development will include some type of feature restriction, but so far, the frontier lies ahead…

---

### Post #3 — **restrading** | 2020-12-23 04:46 UTC _(reply to #2)_

My understanding is that the interaction constraints implemented by XGBoost is to allow only interactions within groups, not across groups. This is the opposite of what we want.

---

### Post #4 — **shonumerai123** | 2020-12-23 05:44 UTC _(reply to #3)_

Thanks for your reply.

Yes, you are right about the way XGB implemented that. So I defined 310 lists and gave them as constraints. [feature_dexterity1, all features EXCEPT other dexterity features], [feature_dexterity2, all features EXCEPT other dexterity features], etc etc…

---

### Post #5 — **restrading** | 2020-12-23 06:49 UTC _(reply to #4)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/e0b2c6/48.png) shonumerai123:

> all features EXCEPT …

So each constraint group has singled out one feature group into “quarantine”, but this still allows interactions among other feature groups.

Does having these many constraints affect training speed significantly?

---

### Post #6 — **shonumerai123** | 2020-12-23 07:23 UTC _(reply to #5)_

It wasn’t a problem but the result just wasn’t great unfortunately… I still don’t know how to make a good use of feature groups. The way I train my model at the moment is completely ignoring the groups so it’s no different even if they are given as feature1-feature310.

---

### Post #7 — **shonumerai123** | 2020-12-23 08:08 UTC _(reply to #4)_

Just realized this isn’t a proper way. Non-dex features can still interact within the group…

---

### Post #8 — **restrading** | 2020-12-23 08:08 UTC _(reply to #7)_

Yes, that’s what I was referring to

---

### Post #9 — **shonumerai123** | 2020-12-23 09:01 UTC _(reply to #8)_

Agreed. It’s impractical to define all possible allowed interactions…
