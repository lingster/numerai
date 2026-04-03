---
title: "Request for TC of perfect predictions"
category: Tournament
url: https://forum.numer.ai/t/request-for-tc-of-perfect-predictions/6060
created_at: 2023-01-22T23:43:20.203000+00:00
last_posted_at: 2023-01-24T04:14:03.346000+00:00
posts_count: 3
views: 1218
tags: []
---

# Request for TC of perfect predictions

---

### Post #1 — **profricecake** | 2023-01-22 23:43 UTC

Hi Numerai -

As I continue to wrap my head around what TC is and how to train for it, I would be very curious to see the historical TC scores for the actual resolved final target values in each round. In other words, can you please share the TC score of what would have been a 100% perfect prediction set for already-completed rounds?

In the world of corr, a perfect corr of 1.0 is theoretically possible if you predict the exact sort order for the samples. But what does that translate to in the TC world? Does a perfect set of predictions lead to a high TC? Or even a positive one? I would hope so, since the target values are all that we have to train on. But given the mysterious impact of the optimizer, who knows for sure?

I’d also be interested in how many user-submitted predictions each round (if any) beat out the perfect predictions in terms of TC.

---

### Post #2 — **nyuton** | 2023-01-23 09:27 UTC

The perfect prediction is, if you hit the exact right ranking! It must have a good TC ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

But here is a good (?) description on how to estimate TC:

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nyuton/48/687_2.png) [How to estimate TC with the numerai meta model data](<http://forum.numer.ai/t/how-to-estimate-tc-with-the-numerai-meta-model-data/6032>) [Data Science](</c/data-science/5>)

> Hi, TC is a metric that shows, how much your model improves the meta model. That means that ensembling the predictions of my model with the metamodel should improve the meta model metrics like corr and sharpe. The fund also picks trades from the stocks, where the metamodel has the most confidence (top/bottom 200). With that in mind, we can estimate the (past) TC of a model with the following script: validation[‘my_prediction’] = my_model.predict(validation[features]) mm = pd.read_parquet(‘…

---

### Post #3 — **profricecake** | 2023-01-24 04:14 UTC _(reply to #2)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nyuton/48/687_2.png) nyuton:

> The perfect prediction is, if you hit the exact right ranking! It must have a good TC ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

I would like to know just how good a TC one gets from perfect predictions.

Given the various pieces of state in the optimizer that we cannot know nor estimate, such as how much of this or that security is already being held, the balance across sectors, the balance across geographical regions, and so forth, it might be that imperfect predictions actually score a higher TC than perfect ones.
