---
title: "Time series CV & seperation to live data"
category: Data Science
url: https://forum.numer.ai/t/time-series-cv-seperation-to-live-data/5837
created_at: 2022-11-10T07:18:26.389000+00:00
last_posted_at: 2022-11-13T17:04:05.885000+00:00
posts_count: 6
views: 1034
tags: []
---

# Time series CV & seperation to live data

---

### Post #1 — **kayeffnumeraitor** | 2022-11-10 07:18 UTC

While training one of my models by expanding time series cross validation, a random thought popped into my head:

Lets say I train a model on the first 100 eras, and test/select it during training on eras 110-120 to prevent any leakage. In the next fold I will train on the first 120 eras, test on eras 130-140, and so on. The furthest that I can do this fold is right until `live era - 6`, meaning right now I would train on the first 1010 eras and test on 1020-1030.

However, if I use the model from the last fold to do the live predictions, the time seperation from the train set is not 10 eras but 30 + 6 eras. So the performance numbers from the test sets have a different seperation window than what I need for the live data. But obviously if I increase the time seperation on the test data during training, this will only add up to the seperation from the live data.

How can I go around this? Is this even an issue? Until now I always used the model from the last fold.

---

### Post #2 — **nyuton** | 2022-11-10 08:28 UTC

The data in the training set contains overlapping rounds!!!

When you train on the first 100 eras, you shouldn’t use eras 101-104 for testing, because in real life they are not available.

You should used purged time series cross validation.

---

### Post #3 — **sirbradflies** | 2022-11-10 08:42 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/kayeffnumeraitor/48/991_2.png) kayeffnumeraitor:

> eration from the live data.
> 
> How can I go around this? Is this even an issue? Until now I

Hi,  
You should see CV and Training as two separate steps. You may want to use CV (like through cross_val_score in sklearn) to get a sense of the model future performance (if you don’t use the CV data for model tuning) but then you can train the model on the full dataset so you don’t “waste” any data.

Hope it helps!

---

### Post #4 — **kayeffnumeraitor** | 2022-11-10 11:05 UTC _(reply to #2)_

Yes, that is why I said I train on first 100 eras, and will test on eras 110 - 120, so a 10 era gap between train and test to avoid leakage.

---

### Post #5 — **kayeffnumeraitor** | 2022-11-10 11:47 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/sirbradflies/48/2766_2.png) sirbradflies:

> You should see CV and Training as two separate steps

I guess my problem boils down to this misunderstanding, will read again on CV

---

### Post #6 — **jmrichardson** | 2022-11-13 17:04 UTC

You don’t have to use the last model of the fold. You can just train a new model on the latest data (obviously without a test set) which would match your CV expanding window strategy. One thing I have found helpful is to not just look at a short test window (in your example 10 eras) but rather all the available data as you walk forward. It gives you a better since for how the model performs as market regimes change over time. Expanding does appear to be better performing than fixed window. Here’s an example of a simple model I was testing where you see the mean and sharpe for the entire test data set but also the first 20 and last 20 as you walk forward:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e629a7c507815dd400c4a0f5e893598deed4dd3a_2_690x422.png)image1250×765 56.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e629a7c507815dd400c4a0f5e893598deed4dd3a.png> "image")
