---
title: "TL;DR scaling of tree ensemble size with training data size"
category: Data Science
url: https://forum.numer.ai/t/tl-dr-scaling-of-tree-ensemble-size-with-training-data-size/5698
created_at: 2022-09-18T19:38:58.914000+00:00
last_posted_at: 2022-09-26T12:54:57.778000+00:00
posts_count: 3
views: 944
tags: []
---

# TL;DR scaling of tree ensemble size with training data size

---

### Post #1 — **gbrecht** | 2022-09-18 19:38 UTC

I am struggling with one aspect of my training experiments that maybe somebody has an opinion on.

I run experiments exploring hyperparameter space and use optuna to do so. Normally I have ~10 hyper parameters and after ~1000 trials the visualization provided by optuna-dashboard gives me the feeling the search space has been processed. I do a 3-fold CV so one trial includes three train, predict, evaluate cycles.

With the size of our dataset, the time I am willing to give to one trial is ~0.25 hours:

1000 trials = 400 hours = close enough to two weeks of running my desktop 24/7

I train using xgboost/lgbm CPU. I have explored cloud GPU options and do not use them for two reasons:

  * The main part of the time is not the GPU number crunching, it is the evaluation code.
  * With the amount of RAM required to process our dataset, the options are too expensive to let them run for days



One trial with 2k trees (the example model size) and the whole dataset in a 3fold (50% train size) cv and some hyperparameters takes Xh to compute. X because I never let it finish. I expect X to be in the range of 8-12 hours. That is not too much for the final training run, but way too much for the experiment. So I have to downsize. I do that by sampling the dataset. At the moment I sample every 30th row like

`data = data[::30]`

That reduces the training time significantly, but leaves me with another question:

If my experiment yields e.g. 1500 trees as the optimum value.  
How can I be sure that that is the best value not for 1/30th of the data, but also for the whole data?

That argument does not stop with the number of trees but expands to every hyperparameter, in particular to: learning rate!

We all know that a low learning rate creates a little increment per tree and thus you should do more trees to prevent underfitting. If you have a too high training rate you will give too much weight to the data you look at first (aka overfit). So I have to take the learning rate into the equation. I am currently using the highly scientific furmula:

`trees = -2700 * learning_rate + 3003`

to get tree values between 300 and 3000 for learning rate values of `[0.001;1]`

Finally I arrive at my main question: **How do I scale back up to the full dataset?**

Do I multiply the number of trees by 30 (the reduction factor of the data)?  
Do I divide the learning rate by 30?  
Do I do both?  
Do I do neither, because it is a complete void assumption that there is such a trivial relation between training dataset size and learning_rate/trees?

---

### Post #2 — **nyuton** | 2022-09-26 10:17 UTC

1500 XGB boosting rounds are too much for hyperparameter search.

With learning rate 0.1, ~100 boosting rounds will do.  
If you add “eval_set” you will see that the validation metrics do not decrease beyond that.

When you want to scale, you just muptiply the tree by 10 and divide learning rate by 10. That should give better result, but it’s not necessary for hyperparameter turning.

The size of the dataset shouldn’t influence the hyperparameters.

---

### Post #3 — **gbrecht** | 2022-09-26 12:54 UTC

Thx for the insights.  
With 100 trees max the data size does not matter that much so … maybe I will be able to use eval_set again. At the moment it makes the whole process way too slow!
