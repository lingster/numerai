---
title: "Will early stopping in cross validation introduce overfitting?"
category: Data Science
url: https://forum.numer.ai/t/will-early-stopping-in-cross-validation-introduce-overfitting/4643
created_at: 2021-12-18T04:01:19.230000+00:00
last_posted_at: 2022-01-01T17:29:40.716000+00:00
posts_count: 8
views: 1733
tags: []
---

# Will early stopping in cross validation introduce overfitting?

---

### Post #1 — **maxchu** | 2021-12-18 04:01 UTC

Anyone has done experiments on early stopping and cross-validation? Does it give a better result using only cross-validation alone?

Also, how do you determine what n_estimator / num_of_epoch of your final model?

---

### Post #2 — **jacob_stahl** | 2021-12-18 18:00 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/dec6dc/48.png) maxchu:

> Also, how do you determine what n_estimator / num_of_epoch of your final model?

Check out [Optuna - A hyperparameter optimization framework](<https://optuna.org/#code_examples>). It makes picking hyper parameters a lot more efficient, and generally gives good results after ~30 trials.

---

### Post #3 — **maxchu** | 2021-12-20 23:29 UTC _(reply to #2)_

Thanks for the sugguestion!

---

### Post #4 — **neosbrother** | 2021-12-22 02:51 UTC

I’m mostly working with neural nets and so early stopping is very important. I am using ES + CV and while I don’t have enough live data to feel confident, I think it’s a principled approach that should at least allow me to evaluate a model with some degree of confidence.

---

### Post #5 — **maxchu** | 2021-12-22 04:53 UTC _(reply to #4)_

Is your final model trained on train+valid dataset?

---

### Post #6 — **neosbrother** | 2021-12-22 13:47 UTC _(reply to #5)_

I don’t have a final model. I use the models trained during CV as an ensemble.

---

### Post #7 — **maxchu** | 2022-01-01 10:02 UTC _(reply to #6)_

So you just average the predictions of the same model trained on different CV?

---

### Post #8 — **neosbrother** | 2022-01-01 17:29 UTC _(reply to #7)_

Yes, average the predictions of each of the models.
