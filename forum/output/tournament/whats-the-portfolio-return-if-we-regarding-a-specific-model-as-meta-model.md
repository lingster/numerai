---
title: "What's the portfolio return if we regarding a specific model as meta model?"
category: Tournament
url: https://forum.numer.ai/t/whats-the-portfolio-return-if-we-regarding-a-specific-model-as-meta-model/5599
created_at: 2022-07-24T22:50:18.548000+00:00
last_posted_at: 2022-07-27T23:57:36.909000+00:00
posts_count: 3
views: 697
tags: []
---

# What's the portfolio return if we regarding a specific model as meta model?

---

### Post #1 — **sunkay** | 2022-07-24 22:50 UTC

Model developers concern about whether their model is good and how good it is.

Have you ever thought about what is the best metric to use to judge whether a model is good or bad? At present, Numerai uses TC as the main evaluation metric and the leaderboard is sorted by TC by default. But TC is not an metric to evaluate the quality of the model itself, it reflects whether a model can improve the overall return when it working with other models. This is what Numerai concern about.

But developers concern about the model itself. If we want to evaluate a specific model in terms of portfolio returns, our question should be: What’s the portfolio return for treating my model as the meta model? True Return of a specific model is what developers concern about.

Numerai doesn’t provide this metric right now, but I’m sure it’s something developers would love to know. Even if a model does not improve the overall return when it working with other models, it may be a very good model on its own.

And this metric doesn’t depend on other models, so enabling everyone to get their own True Return in history rounds in local validation time is possible.

---

### Post #2 — **autratec** | 2022-07-26 05:50 UTC

TC is unstable and non-predictable. i believe more participants will move their staking strategy focusing on CORR only.

---

### Post #3 — **sunkay** | 2022-07-27 23:57 UTC

At present, it’s still hard to tell which model is good with leaderboard metrics, so I think finding more good metrics to evaluate the model is far more important than finding more data to train the model.
