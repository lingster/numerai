---
title: "Is it safe to train on validation set/use part of training set as validation set?"
category: Tournament
url: https://forum.numer.ai/t/is-it-safe-to-train-on-validation-set-use-part-of-training-set-as-validation-set/4323
created_at: 2021-10-12T06:53:46.786000+00:00
last_posted_at: 2021-10-12T06:53:46.860000+00:00
posts_count: 1
views: 541
tags: []
---

# Is it safe to train on validation set/use part of training set as validation set?

---

### Post #1 — **maxchu** | 2021-10-12 06:53 UTC

One concern here is that if a learning-based method like PCA is used for the dimensionality reduction on the dataset. If PCA is trained on the training set, then any cross-validation split that uses some portion of the training dataset will cause data leakage?
