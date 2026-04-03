---
title: "What is a good sharpe ratio and validation correlation?"
category: Tournament
url: https://forum.numer.ai/t/what-is-a-good-sharpe-ratio-and-validation-correlation/419
created_at: 2020-05-16T22:37:41.906000+00:00
last_posted_at: 2020-05-18T15:22:06.916000+00:00
posts_count: 5
views: 3481
tags: []
---

# What is a good sharpe ratio and validation correlation?

---

### Post #1 — **mendrinos** | 2020-05-16 22:37 UTC

Hi, first of all I’m just getting started on this so I’m still learning.

I just wanted to know what good values for the sharpe ratio and validation correlation are. I understand that the higher the better for both of these values but what is a realistic value? For example my current model has a validation correlation of 0.0717 and a validation sharpe of 2.4858. Are these values good, bad, or average? (I have another model that I’m sure cannot be right, which had a validation correlation of 0.8 and a sharpe of 54, is this overfit? both models trained on the same data however the max depth in the XGBRegressor was changed from 3 to 10)

Thanks in advance for any help

---

### Post #2 — **joakim_arvidsson** | 2020-05-17 02:55 UTC

If you have held out a test set and got similar Sharpe and correlation on that, then I’d say those are excellent. In the end, all that matters is live performance and if you can get positive Sharpe and mean correlation consistently, I’d say that’s good too. Ideally different from the meta model and what others have already discovered.

---

### Post #3 — **mendrinos** | 2020-05-17 08:46 UTC _(reply to #2)_

I’m using the train_test_split method to create a training set and a testing set from both the training data and the tournament validation data using a test size of 0.3 so hopefully that means my numbers are alright?

thanks for your help

---

### Post #4 — **arbitrage** | 2020-05-18 14:59 UTC _(reply to #3)_

instead of treating all the rows as the same dataset, you should instead split based on era. Each era is a single time period of a month, so if you mix and match rows from different eras, then you may receive bad inference. Check out the example notebooks in the github repo: <https://github.com/numerai/example-scripts>

---

### Post #5 — **mendrinos** | 2020-05-18 15:22 UTC _(reply to #4)_

I didnt realise that, thanks for the heads up!
