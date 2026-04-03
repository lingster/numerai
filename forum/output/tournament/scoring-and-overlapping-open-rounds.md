---
title: "Scoring and overlapping open rounds"
category: Tournament
url: https://forum.numer.ai/t/scoring-and-overlapping-open-rounds/6014
created_at: 2023-01-07T17:59:59.771000+00:00
last_posted_at: 2023-01-07T18:51:07.875000+00:00
posts_count: 4
views: 528
tags: []
---

# Scoring and overlapping open rounds

---

### Post #1 — **m98008** | 2023-01-07 17:59 UTC

When I submit predictions for the weekly tournament (say round X), they will be scored after 4 weeks. In the meanwhile, I can see the scores of my predictions every day. What happens when I submit new predictions with the same model the subsequent week (say round X+1 - ignoring the daily rounds for now? Do the predictions for round X+1 override the ones I submitted for round X? Which scores do I see on the dashboard after one week - for scores for predictions X, predictions X+1, or some aggregate? (There is only one score per model per metric, e.g. TC or FNC, but up to 4 open rounds with submissions.)

---

### Post #2 — **wigglemuse** | 2023-01-07 18:23 UTC

Nothing overrides anything – each round is overlapping in time but is independent in terms of scoring. Round X+1 doesn’t even need to be the same model as last week, etc etc. So none of your scores for a submission are affected by any other future or past submission.

---

### Post #3 — **m98008** | 2023-01-07 18:30 UTC _(reply to #2)_

Thank you. So if I submit for model id M every week, what does FNC of 0.0435 on a given day after the X+1 submission mean? how is this calculated - using which submission/ prediction data?

---

### Post #4 — **wigglemuse** | 2023-01-07 18:51 UTC

You get a different set of numbers for each round. There are 4 overlapping live rounds going on all the time – so every scoring day you’ll get four updated CORR20 scores (one for each round), four updated FNC scores, four TC scores, etc. If you’re talking about the leaderboard numbers, that’s a weighted average over 20 rounds. But click on any of those models and you can see any score for any round (and even any day from that round).
