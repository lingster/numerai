---
title: "New target in Q4"
category: Tournament
url: https://forum.numer.ai/t/new-target-in-q4/4389
created_at: 2021-10-24T13:52:27.930000+00:00
last_posted_at: 2021-10-27T20:50:30.837000+00:00
posts_count: 5
views: 983
tags: []
---

# New target in Q4

---

### Post #1 — **eleven_sigma** | 2021-10-24 13:52 UTC

In the last Announcements we can read:  
“For Q4 2021, we want to continue unification of Signals and Tournament by starting to score Tournament submissions against a 20D2L target (20 days long w/ a 2-day lag). This is a small, but important, change from the 1-day lagged target we currently use for scoring. This change will likely take place sometime in November, so **be ready** for the new scoring process”

If I understand the change, the performance will be compute as (close_20 - close_2) / close_2 instead of (close_20 - close_1) / close_1. Right?  
This will require the training of models with a new target (correlated with target_nomi_20, but different). We don’t know how the change in target will affect to feature selection of parameter tuning until we have the new target, so I don’t know what exactly means “be ready”.

I hope you release the new target a few weeks before the change so we can check how it affects to the models.

---

### Post #2 — **rlh** | 2021-10-25 10:24 UTC

Generally fixed-threshold return targets are relatively poor indicators. A 5% move on the 20th day makes a 5% difference versus one on the 21st day, which makes no real sense.

Any trader with scale (and a desire to improve sharpe) tends to scale in; even a simple 5-day average for position entry, and 5-day average for position exit, would be a much better target.

That said, wholly agree that some notice would be optimal to tune models, as the fixed cutoffs lead to major artifacts.

---

### Post #3 — **richai** | 2021-10-25 23:13 UTC

Yeah that’s confusing language. The new target discussed is the current target in the new data. So you don’t have to do anything or be ready. [@ark](</u/ark>) can you change the post so it’s clear.

---

### Post #4 — **ark** | 2021-10-27 15:46 UTC _(reply to #3)_

Sorry for that confusion, it was meant to read like “get ready for a potential change in performance” in the case that there were legacy models still using the old target. In any case, I’ve updated the post to be much more clear and concise.

---

### Post #5 — **rehoboam** | 2021-10-27 20:50 UTC _(reply to #4)_

How it would affect legacy models still using the old target?
