---
title: "Time ammount to solve tournament"
category: Tournament
url: https://forum.numer.ai/t/time-ammount-to-solve-tournament/3082
created_at: 2021-04-26T11:11:22.685000+00:00
last_posted_at: 2021-06-12T09:57:06.409000+00:00
posts_count: 6
views: 843
tags: []
---

# Time ammount to solve tournament

---

### Post #1 — **alexandruldaia** | 2021-04-26 11:11 UTC

Hello ,  
I need to know after new data is release how much time ammount do we have to solve tournament ?

---

### Post #2 — **ml_is_lyf** | 2021-04-26 11:29 UTC

The data for the next round is released at 6pm UTC on Saturday each week, and you have until 2:30pm UTC on Monday to make your submission. So we get about a 2-day window to make our submission. Importantly the training data rarely changes, so you don’t have to build a new model each week. Just build a model using the training data and you can reuse that model to make predictions each week.

---

### Post #3 — **alexandruldaia** | 2021-04-26 13:11 UTC

Tnks , helped me ,have a nice day !

---

### Post #4 — **autratec** | 2021-06-12 09:16 UTC _(reply to #2)_

> Importantly the training data rarely changes, so you don’t have to build a new model each week. Just build a model using the training data and you can reuse that model to make predictions each week.

quick question here: the tournament data set is huge. do i need to get whole file (2.5G) go through my model, or just pick LIVE category to generate the predication ?

---

### Post #5 — **ml_is_lyf** | 2021-06-12 09:29 UTC _(reply to #4)_

Yeah, it is big, depending on your model you can reduce the precision of the features and target to float16, which will significantly reduce the size. I think technically you’d still be fine to just submit predictions for the live rounds category. Maybe try it out with a model and see? Another technique is you can load the predictions for VALIDATION and TEST once, make predictions for those, save them, and then resubmit them each round. Although personally, I would re-predict VALIDATION each round as it’ll help you validate that nothing has gone wrong when making the predictions (assuming your models predictions for validation are always the same, which sometimes isn’t the case depending on if and how you apply feature neutralization for instance).

---

### Post #6 — **autratec** | 2021-06-12 09:57 UTC _(reply to #5)_

Thanks for the suggestion. I wil try to include both validation and test in next round.
