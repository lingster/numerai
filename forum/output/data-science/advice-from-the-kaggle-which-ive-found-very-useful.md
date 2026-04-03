---
title: "Advice from the Kaggle which I've found very useful"
category: Data Science
url: https://forum.numer.ai/t/advice-from-the-kaggle-which-ive-found-very-useful/300
created_at: 2020-05-01T10:11:57.969000+00:00
last_posted_at: 2021-06-14T00:45:45.153000+00:00
posts_count: 3
views: 2809
tags: []
---

# Advice from the Kaggle which I've found very useful

---

### Post #1 — **jackerparker** | 2020-05-01 10:11 UTC

Hi everyone!

I’ve found nice advice from the Kaggle’s grandmaster which can be easy fitted into the Numerai competition. Original version can be found here: <https://www.kaggle.com/c/home-credit-default-risk/discussion/58332>. And here is my adaption for Numerai:

  1. Since we’re provided historic data, this is partly a time-series problem. This means that recent data is more relevant than old data.
  2. There’s a lot of different regimes between the eras, which means that there’s a lot of variance between folds. Try different K-fold sets to see if your model is stable, and interpret the validation score as just one more fold. It could be an outlier, so TRUST YOUR LOCAL CV!!!
  3. Many of the features we’re given and that we generate are not relevant to the target and just confuse the model. LGB and XGB have a rich toolset to remove noisy features and regularize your models. Two of the most important for this competition are featurefraction and reglambda.
  4.      *   5. As in all Kaggle competitions (and all machine learning problems, for that matter), the most important first step is to get a validation set-up that matches the test set. There’s no point in spending time on feature-engineering before your validation system is trustworthy.
  6.      *   7. Have fun!



Regards,  
Mark

---

### Post #2 — **chelnak** | 2021-05-19 20:10 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jackerparker/48/1580_2.png) jackerparker:

>   * As in all Kaggle competitions (and all machine learning problems, for that matter), the most important first step is to get a validation set-up that matches the test set. There’s no point in spending time on feature-engineering before your validation system is trustworthy.
> 


[@jackerparker](</u/jackerparker>) what do you mean here by “get a validation set-up that matches the test set” ?

---

### Post #4 — **autratec** | 2021-06-14 00:45 UTC

“Two of the most important for this competition are featurefraction and reglambda” - good suggestion. Especially the first one.
