---
title: "Deep metric learning to find a close era to live"
category: Data Science
url: https://forum.numer.ai/t/deep-metric-learning-to-find-a-close-era-to-live/1268
created_at: 2020-12-06T05:05:36.578000+00:00
last_posted_at: 2021-03-12T23:06:24.845000+00:00
posts_count: 3
views: 1855
tags: []
---

# Deep metric learning to find a close era to live

---

### Post #1 — **katsu1110** | 2020-12-06 05:05 UTC

It would be great if we could know which training or validation era is ‘close’ to the live era to enhance our model performance in the tournament. This knowledge may help us avoid a burning era by focusing our modeling on improving its validation performance on that ‘close’ era.

Here I use a simple deep metric learning approach to do that in the following kaggle notebook.

[metric learning and live era](<https://www.kaggle.com/code1110/numerai-metric-learning-and-live-era/notebook>)

Feel free to comment and upvote if you like:)

---

### Post #2 — **oxioxi** | 2020-12-06 12:27 UTC

This is pretty cool. All of these explanatory style posts / notebooks are awesome for beginners like myself. Thank you.

One of those final plots looks eerily like some meteorological image ![:leaves:](http://forum.numer.ai/images/emoji/twitter/leaves.png?v=9).

---

### Post #3 — **alexweefs** | 2021-03-12 23:06 UTC

Siamese Networks are mainly used in combination with a **Contrastive Loss function aka Pairwise ranking Loss.** The loss function is mainly used to learn embeddings (feature vectors) in a way that the metric distance between two examples from the same class is small and that between different classes is large in a metric space.  
Triplet network is also a Symmetric neural network architecture but consists of three identical subnetworks that share the same sets of parameters.

* * *

[Dean’s Tank Inc.](<http://www.deanstank.net/>)
