---
title: "Era Purging to minimize data leakage between train/val/test"
category: Data Science
url: https://forum.numer.ai/t/era-purging-to-minimize-data-leakage-between-train-val-test/704
created_at: 2020-07-24T06:13:22.115000+00:00
last_posted_at: 2020-07-27T20:16:34.683000+00:00
posts_count: 5
views: 1864
tags: []
---

# Era Purging to minimize data leakage between train/val/test

---

### Post #1 — **player1** | 2020-07-24 06:13 UTC

Adding this to the forum as I think it’s an important topic. Here I’ll focus mainly on the potential ‘data leakage’ issue, rather than on the more general problem of over-fitting, which could be due to many different reasons.

In short, eras are one month long, chronological, and non-overlapping in time. However, assuming some features are based on company financials, and since financials are usually reported quarterly, each era could potentially include information from the previous 1-2 eras. To me this seems like it could be a concern, as good validation and test performances could be mainly due to data leakage, and those optimized models wouldn’t necessarily perform as well on live data.

Marcos Lopez de Prado (MLdP) proposes in chapter 7 of his book Advances in Financial Machine Learning to ‘purge’ some time series after each train and test set, to overcome this problem. He also suggests to ‘embargo’ some additional time series after the test set, if purging only is not sufficient.

[@richai](</u/richai>) mentioned in today’s OHw [@arbitrage](</u/arbitrage>) that models (and features?) with high auto-correlation could potentially be impacted by data leakage between eras, as well as some shorter term features (shorter window length?)? ← Please correct me if I’m misrepresenting anything here.

My main questions are:

  1. Is data leakage between eras a concern with the Numerai dataset?
  2. If it is, how many eras should one purge? Purging 2 eras after each train and val/test set seems like it should be sufficient.
  3. Other than comparing live performances, is there a way to check if a model optimized on a purged dataset performs better than one that’s been optimized on a non-purged dataset?
  4. If Numerai provided an additional grouping, e.g. 3 eras = 1 epoch, that is less likely to have data leakages between epochs, would that help?
  5. Perhaps I’m overthinking this way too much and it’s not really a concern at all? ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

---

### Post #2 — **master_key** | 2020-07-25 06:39 UTC

I think you could test this yourself by training models on many different subsets of eras, and then seeing if they perform way way better on their direct neighbors than they do on slightly less distant neighbors. If the difference here is large then maybe you’ll want to embargo the data yourself, but if negligible then it means no need to worry ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

---

### Post #3 — **player1** | 2020-07-25 07:09 UTC _(reply to #2)_

True, but variance in performance between near and far eras could also be due to radical differences in market regimes, and not necessarily due to leakage. How would we measure how much variance is due to leakage and how much is due to regime changes?

I understand Numerai doesn’t want to disclose too much about the dataset, but I think it would be useful for us to know if the dataset has already been structured in such a way to minimize data leakage.

---

### Post #4 — **lackofintelligence** | 2020-07-27 16:51 UTC

Let me try to simplify things a little for you. Ask a sorcerer or anybody off the street for parameters for your model. Don’t worry about data leakage when you do that. Now that you have a model you can do two calculations. 1) A leave-one-era-out CV calculation of your model’s performance. 2) A leave-one-era-out N-embargoed CV calculation of your model’s performance. If the results of those two CV calculations are somewhat different, go with the more conservative estimate. If they are really really so different that you are concerned, pick a different sorcerer, or, i.e., think about a more rational way to pick candidate models.

---

### Post #5 — **joakim_arvidsson** | 2020-07-27 20:16 UTC _(reply to #4)_

That does help, thank you! Now I just have to figure out how to do this in code.
