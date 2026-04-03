---
title: "Hyperparameters optimization for 'small' LGBM models"
category: Data Science
url: https://forum.numer.ai/t/hyperparameters-optimization-for-small-lgbm-models/6693
created_at: 2023-09-29T18:40:25.301000+00:00
last_posted_at: 2023-10-09T17:31:02.204000+00:00
posts_count: 8
views: 2727
tags: []
---

# Hyperparameters optimization for "small" LGBM models

---

### Post #1 — **svendaj** | 2023-09-29 18:40 UTC

Majority of [Numerai example models](<https://github.com/numerai/example-scripts>) are using following hyperparameters with certain comments on “better” values:
    
    
    model = lgb.LGBMRegressor(
        n_estimators=2000,  # If you want to use a larger model we've found 20_000 trees to be better
        learning_rate=0.01, # and a learning rate of 0.001
        max_depth=5, # and max_depth=6
        num_leaves=2**5-1, # and num_leaves of 2**6-1
        colsample_bytree=0.1
    )
    

[Super Massive LGBM Grid Search](<http://forum.numer.ai/t/super-massive-lgbm-grid-search/6463/1>) was done with v4.1 data and some Numerai data wonks (like me) were asking for hyperparameters optimization with smaller number of estimators. So I have decided to do perform “Tiny Little LGBM Bayesian Search” on my own in Kaggle.

I am using Optuna on following optimization space:

  * `n_estimators` in int iterval <1_000;10_000>
  * `learning_rate` in real interval <0.001;0.9> originally sampled from logaritmic space later from linear
  * `max_depth` in int iterval <2;10> later limited to <4;7> due to large impact on run time without promising results (`num_leaves` is set as 2^{num\\_leaves})
  * `colsample_bytree` in real interval <0.05;1.0>



Notebook is public on Kaggle - [Numerai LightGBM Hyperparameter Search with Optuna | Kaggle](<https://www.kaggle.com/code/svendaj/numerai-lightgbm-hyperparameter-search-with-optuna/>) and saves optimization study, so that you can fork it and continue in the study (Optuna will take previous results into account when suggesting next trial). Eventually you can modify objective function (search space) and run it on your favourite subspace. It would be really nice if you would then make your notebook public, so that we all can see your results and possibly continue your search. We could then make it **Super Massive Distributed Hyperparameter Search** for numerai models. ![:exploding_head:](http://forum.numer.ai/images/emoji/twitter/exploding_head.png?v=12)

Next week when my Kaggle GPU quota (30 hours of runtime) will be renewed, I am planning to do fork for XGBoost. I will keep you posted.

---

### Post #2 — **svendaj** | 2023-10-02 11:58 UTC

So XGBoost optimization is public as well: [Numerai XGBoost Hyperparameter Search with Optuna | Kaggle](<https://www.kaggle.com/code/svendaj/numerai-xgboost-hyperparameter-search-with-optuna>). It is not fully comparable to [Numerai LightGBM Hyperparameter Search with Optuna | Kaggle](<https://www.kaggle.com/code/svendaj/numerai-lightgbm-hyperparameter-search-with-optuna>) because `learning_rate` is sampled from log distribution, but some interesting observations can be made:

  * better general performance than LGBM (although `learning_rate` sampling might play a role
  * needs more trees
  * `colsample_bytree` higher than with LGBM which is higher than recommended 0.1 (might be influenced by number of features - we play on Kaggle with medium feature set)



Both LGBM and XGB could not use T4 x 2 GPU Kaggle accelerator (or precisely was using only 1 GPU core for calculations) and CatBooost is using both cores (should be faster) next week, when my Kaggle GPU quota will be replenished, I will do fork for CatBoost.

---

### Post #3 — **neverfall** | 2023-10-04 19:25 UTC

Hi, i like the idea of distributing the Hyperparameter Search, but from my perspective it comes with a bit of a Problem.  
As you already stated, one could modify the objective function, but if you do so, or maybe use the data in another way, the resulting trials and their scores can’t be compared to everything else.  
So distributing it would definitly make sense, if we would all (the participants) agree about what we are looking for.  
If you are intrested, i would share some thoughts (either in kaggle where the code is, or via pm?), as i have done some optuna research on numerai myself.

---

### Post #4 — **svendaj** | 2023-10-05 20:27 UTC _(reply to #3)_

Thanks for your comments and congratulations on your first post on Forum!

Yes I am aware that modification of search space is basically definition of new study, but if there would be group of researchers forking the notebook with their own study and making it public, other researchers might continue with for them interesting study (increasing number of trials) so we could explore much larger space of hyperparameters.

I am interested in your remarks and best, I believe, would be to discuss where the code is. In kaggle each notebook have section Comments, so your thoughts will be welcome there: [Comments on Numerai LightGBM Hyperparameter Search with Optuna | Kaggle](<https://www.kaggle.com/code/svendaj/numerai-lightgbm-hyperparameter-search-with-optuna/comments>)

BTW kind of unexpected result (at least for me) was identification of fairly small LGBM model which was in top 5 % results. This model significantly reduced training time (and size of model) without sacrificing CORRV2 performance (0.024682):
    
    
    params = {
            "n_estimators": 1_885,
            "learning_rate": 0.019,
            "max_depth": 5,
            "colsample_bytree": 0.13,
            # LGBM 4.0.0 params on Kaggle
            "verbosity": -1, # reduce logging output
            "num_threads": 4   # number of CPUs on Kaggle
        }
    params["num_leaves"] = 2 ** params["max_depth"]
    ​model = LGBMRegressor(**params)

---

### Post #5 — **neverfall** | 2023-10-08 14:43 UTC _(reply to #4)_

Thanks for sharing. How big (filesize) is the model?  
I had some good results in my crossvalidation with building one model per era (hyperparams would very likely be different) and letting each of them predict the live data and take the average of those predictions. It was better on corr and sharpe than doing the same with one big(ger) model.  
In the end in had like ~250 (every 4th era) models with ~300MB each which makes it impossible to use with compute.

---

### Post #6 — **svendaj** | 2023-10-08 19:39 UTC _(reply to #5)_

That small model (1_885 trees) trained only on train data had pickled about 6.4 MB. Which would be two orders smaller than yours, but still too much for model upload environment, I guess.

This is one of the reasons I actually like very much the “limited” Kaggle environment. It keeps you within limits of 4 CPUs (or 2CPUs&GPU), 30 GB RAM and 20GB of persistent storage (output folder). If you can make it there, it will be good enough to run in Numerai upload images (although my bigger ensembles were also too big for model upload - 2.2GB - and I am launching them in Kaggle and submitting predictions from there the old way).

And finally, because “necessity is mother of invention”, Kaggle constrains could spark new solution which will be still good enough but more efficient on resources. So here is another optimization task: what would be the minimum number of ensembled per era trained minimodels to maintain solid CORR and Sharpe? Also containing interesting sub-problem how to subsample those minimodels.

Thanks on your comments on Kaggle, I will react but just now I am doing CatBoost optimization fork and so I will react later.

---

### Post #7 — **svendaj** | 2023-10-09 15:27 UTC

And [Numerai CatBoost Hyperparameter Search with Optuna | Kaggle](<https://www.kaggle.com/code/svendaj/numerai-catboost-hyperparameter-search-with-optuna>) has been published as well.

No major surprise in first review of results, which supports my hypothesis that you can choose whatever GB trees method and you will not gain any significant edge coming from method (due to high noise in the data):

  * Best results: `{'n_estimators': 6685, 'learning_rate': 0.02659796127076718, 'max_depth': 5} with best CORRV2: 0.02549098149390841`
  * Although CatBoost used both cores of 2xT4 GPU accelerator, it was not much faster, also because CatBoost was performing better with larger number of trees, which prolonged computation.
  * `learning_rate` was larger than the other two methods. Average C (`learning_rate * n_estimators`) of top 5% trials is 149 (XGB was 18 and LGBM was 59)

---

### Post #8 — **neverfall** | 2023-10-09 17:31 UTC _(reply to #7)_

If they gain similar corr but the predictions itself are not too correlated to each other, they might ensemble well. Maybe worth to test that…

btw. ~6.5MB should be small enough to work… maybe I’ll give it a shot, as soon as I find the time
