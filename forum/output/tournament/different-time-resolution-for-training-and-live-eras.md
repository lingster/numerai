---
title: "Different time resolution for training and live eras"
category: Tournament
url: https://forum.numer.ai/t/different-time-resolution-for-training-and-live-eras/1203
created_at: 2020-11-19T13:59:02.477000+00:00
last_posted_at: 2020-11-19T16:52:48.263000+00:00
posts_count: 3
views: 854
tags: []
---

# Different time resolution for training and live eras

---

### Post #1 — **sirbradflies** | 2020-11-19 13:59 UTC

Hi,

As I understand the tournament, it is in everybody’s interest for the Training and Validation data to be representative of the patterns that our models will then need to predict for the Live data.

I am uneasy however at the idea of training our models on monthly eras and then apply them to weekly eras, where I believe it’s possible that regularities detected at a month level may vanish with a time horizon 4 times shorter (or the other way around). Has this issue been discussed before?

Were these possibilities considered (or even tested):

  * Training/Validating on weekly eras (thus increasing the dataset size)
  * Predicting on monthly eras (thus being able to trade only monthly)



I apologize if this has been discussed before or I’m missing a basic point!  
Thanks

---

### Post #2 — **wigglemuse** | 2020-11-19 16:22 UTC

All eras are monthly (specifically 4 weeks). It is just that they are overlapping in the live tournament, i.e. a new one starts each week, but each still takes 4 weeks to resolve. So there are not two levels.

---

### Post #3 — **sirbradflies** | 2020-11-19 16:52 UTC _(reply to #2)_

Thanks wigglemuse, I must have missed it in the documentation.  
That makes sense!
