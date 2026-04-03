---
title: "Learning to Rank"
category: Data Science
url: https://forum.numer.ai/t/learning-to-rank/454
created_at: 2020-05-22T10:36:21.558000+00:00
last_posted_at: 2023-03-21T13:30:37.761000+00:00
posts_count: 30
views: 19777
tags: []
---

# Learning to Rank

---

### Post #1 — **jrb** | 2020-05-22 10:36 UTC

I’d mentioned this on OHWA #12 yesterday, and [@arbitrage](</u/arbitrage>) suggested that I post the idea here. The idea is as follows: It is perhaps worth taking a step back and rethinking the tournament as a [learning to rank](<https://en.wikipedia.org/wiki/Learning_to_rank>) problem rather than a regression problem.

The metric we’re trying to optimize for is a ranking metric which is scale invariant, and the only constraint is that the predicted targets are within the interval `[0, 1]`. With that in mind, we don’t need to optimize for squared error, absolute error or something in between the two. The only requirement is that the predicted targets are co-monotonic with the labels. This in my opinion, opens up the design space for loss functions and learning algorithms in general.

Also, I’ve empirically found that although a regression based loss function helps with performance initially. But once the learner converges sufficiently, a regression based loss actively hurts the learner’s performance. I think it’s because memorization (which the regression metric optimizes for) is good, until it isn’t. This also explains why it’s so easy to overfit the data. We try to alleviate this with regularization, but perhaps we could do better than just that.

Traditionally, in learning to rank literature, the problem is usually expressed in 3 ways.

  1. Pointwise ranking
  2. Pairwise ranking
  3. Listwise ranking



Treating the problem as a pointwise ranking problem is essentially treating it as a classification/regression problem. In LTR benchmarks, pairwise ranking almost always beats pointwise ranking. The intuition behind this is that comparing a pair of datapoints is easier than evaluating a single data point. Also, the learner has access to two sets of features to learn from, rather than just one.

The `XGBoost` Python API comes with a simple wrapper around its ranking functionality called `XGBRanker`, which uses a pairwise ranking objective. `catboost` and `lightgbm` also come with ranking learners. I’ve added the relevant snippet from a slightly modified example model to replace `XGBRegressor` with `XGBRanker`. This model does almost as well as the example model on the usual battery of metrics. Tuning hyperparameters to make it better than the example model is left as an exercise to the reader. Listwise ranking could probably be the topic for a future discussion.

Can anyone think of a way to get this to beat the example model? Perhaps combine this with the other recent ideas of era-boosting and feature neutralization.
    
    
        model = XGBRanker(max_depth=5, learning_rate=0.01, n_estimators=2000, n_jobs=-1, colsample_bytree=0.1)
        cdf = training_data.groupby('era').agg(['count'])
        group = cdf[cdf.columns[0]].values
        del cdf
        model.fit(training_data[feature_names], training_data[TARGET_NAME], group=group)
    

Edits: Fixed a typo: s/Treating the problem as a _**pairwise ranking**_ problem …/Treating the problem as a _**pointwise ranking**_ problem is essentially treating it as a classification/regression problem/

---

### Post #2 — **wigglemuse** | 2020-05-22 13:35 UTC

I have done some experiments with what I call head-to-head models (pairwise comparisons) and while it worked, so far I haven’t gotten it to work quite as well as…not doing that. I do use decision trees, but none of the typical boosting libraries so they may implement it in a more clever way than I do, and I do have a few ideas for next time I try it.

---

### Post #3 — **jrb** | 2020-05-22 13:45 UTC _(reply to #2)_

[@wigglemuse](</u/wigglemuse>) When you say head-to-head models, do you mean [Siamese nets](<https://en.wikipedia.org/wiki/Siamese_neural_network>)?

And yes, metric learning (with contrastive loss) and pairwise ranking are very closely related.

---

### Post #4 — **wigglemuse** | 2020-05-22 14:26 UTC

I’m using decision trees, so they aren’t NNs, and if there is a special name for them I don’t know. I just mean instead of taking a bunch of rows of the data as given (more or less) and predicting that, I make a dataset where each row contains two original rows appended together (so 620 features instead of 310) or maybe one row subtracted from another. And then the target is 1/0 and you are predicting which row is greater than the other (you’d only compare rows that did not have equal targets originally). I used to do this with literal horse racing models, i.e. instead of “who is going to win the race?” I’d break it down into “is this horse going to beat that one?” and then it becomes a one-on-one comparison / sorting problem.

---

### Post #5 — **jrb** | 2020-05-23 11:48 UTC _(reply to #4)_

That’s quite neat! Your predictor will likely do much better if its output is expressed as a [trichotomy](<https://en.wikipedia.org/wiki/Trichotomy_\(mathematics\)>). Quite like how [comparator functions](<https://www.cplusplus.com/reference/cstdlib/qsort/>) work in sorting algorithms.

---

### Post #6 — **wigglemuse** | 2020-05-23 19:45 UTC _(reply to #5)_

Adding the equality comparison just seemed to increase the training burden with no benefit, but I haven’t really taken a deep dive into the method as it looked like it would need some improvements just to get even performance-wise with the more usual methods.

---

### Post #7 — **quantverse** | 2020-05-24 08:20 UTC

CatBoost GPU example code:
    
    
    params = {
        'loss_function': 'PairLogit:max_pairs=100000',
        'task_type': 'GPU',
        'devices': '0'
    }
    m = CatBoost(params)
    # traind = numerox Data object for training
    m.fit(traind.x, traind.y['kazutsugi'], group_id=traind.era_float.astype(int))
    

I was torturing my `1080Ti` for the whole night but I am not really able to find any models significantly better than I’ve already got using RMSE loss (yet). Exploring both normal & target neutralized possibilities.

One thing is clear though - pairwise mode requires **much more** GPU power (I limit amount of pairs to 100k per era, but still) than pointwise mode.

Maybe I will try listwise mode as well but it seems to run even slower.

---

### Post #8 — **wigglemuse** | 2020-05-24 12:16 UTC

Yeah, you get into the problem where theoretically you’d want to compare every row with every other row in your dataset, and so that becomes infeasible and you have to subsample from all those possibilities but in a way that you can still get a reliable ranking for each original row.

---

### Post #9 — **correlator** | 2020-06-19 18:47 UTC

LTR is often used in information retrieval. There’s a query and multiple documents and the documents need to be ranked. The ‘Y’ is the labelled relevance score assigned to a feature vector (constructed using q and d). I’m having a hard time relating this to the numerai dataset.  
In the code you’ve grouped by eras that means era==query, features are being ranked according to target scores (not relevance scores). None of this matches with the earlier context.  
I may have misunderstood some details, could you elaborate on this further.

---

### Post #10 — **bcb** | 2020-06-20 11:25 UTC _(reply to #8)_

i am currently looking at locality sensitive hashing as a kind of nearest neighbour in high dimension in a scalable way (<https://towardsdatascience.com/understanding-locality-sensitive-hashing-49f6d1f6134>)…

Not yet sure if it really helps though…

---

### Post #11 — **surajp** | 2020-08-14 15:47 UTC _(reply to #7)_

For the very first time, Using default parameters I felt like beating example_predictions (experimenting with round 224 data)  
Really excited for applying new methods with this

[![Screenshot_2020-08-14 Google Colaboratory](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a0745685cae09f9a4395fa3ed791efc33b4419d9.png)Screenshot_2020-08-14 Google Colaboratory439×509 6.38 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a0745685cae09f9a4395fa3ed791efc33b4419d9.png> "Screenshot_2020-08-14 Google Colaboratory")

---

### Post #12 — **nrichers** | 2020-09-24 14:46 UTC

Can someone perform cross validation through scikit-learn on XGBRanker?  
Extending [@jrb](</u/jrb>) code, and passing `group` parameter as `**fit_params`, it returns my `error_score=123`. I guess `group` param got lost once you split the data.
    
    
    from sklearn.metrics import mean_squared_error
    from xgboost import XGBRanker
    from sklearn.model_selection import GridSearchCV
    
    xgb_param_grid = {'n_estimators' : [10,20,30]}
    fit_params = {'group': group}
    scorer=make_scorer(mean_squared_error)
    
    grid_search = GridSearchCV(XGBRanker(), xgb_param_grid, scoring=scorer, cv=3, error_score=123)
    grid_search.fit(training_data[feature_names], training_data[TARGET_NAME], **fit_params)
    
    grid_search.cv_results_
    

I found several attempts to fix it on google, including a [xgb extension](<https://github.com/bigdong89/xgboostExtension>) lib, but it looks outdated to any `XGB version >= 0.90`. However snooping their [code](<https://github.com/bigdong89/xgboostExtension/blob/master/xgboostextension/xgbranker.py>), it seems to create a new `group` variable to every split. It is possible because you have to pass the `group` column (`era in our case`) , attached as first column to your X matrix.

An idea could be perform the splits in advance, to store all your `group` lists (related to your splits), and use it as an [iterator](<https://www.w3schools.com/python/ref_func_next.asp>).
    
    
    group_splitted = iter([group_split1, group_split2, ....])
    fit_params = {'group': next(group_splitted)}
    

But no clue if it gonna work… Any idea?

---

### Post #13 — **jrb** | 2020-10-07 15:02 UTC _(reply to #12)_

Hey [@nrichers](</u/nrichers>)! I wish I’d seen your post earlier. Perhaps you’ve solved the problem by now. If not, here’s one way to go about solving it.

Btw, this reminds me of the old CS adage: “All problems in computer science can be solved by another level of indirection … except for the problem of too many layers of indirection”.

This problem can simply be solved by adding a layer of indirection. You could subclass `XGBRanker` and override the `fit()` method to take both era and the features in the `x` argument, and seperates them before calling the superclass’s `fit()` method. Of course, you’ll also need to override `predict()` on your subclass to account for this change.
    
    
    class MyXGBRanker(XGBRanker):
        def fit(self, x, y):
            cdf = x.groupby('era').agg(['count'])
            group = cdf[cdf.columns[0]].values
            return super().fit(x[feature_colums], y, group=group)
    
        def predict(self, x):
            return super().predict(x[feature_colums])
    

Now, you can call `gridsearch.fit()` from your snippet like this:
    
    
    grid_search = GridSearchCV(MyXGBRanker(), xgb_param_grid, scoring=scorer, cv=3, error_score=123)
    grid_search.fit(training_data[['era'] + feature_names], training_data[TARGET_NAME])
    

Bear in mind that I haven’t tried to run it and it’s quite likely that the hastily typed code above has some typos/errors. But this should be enough to unblock you, IMO. Let us know if it works for you.

---

### Post #14 — **jrai** | 2021-09-21 19:56 UTC

I’ve been revisiting ranking with the new dataset and have had good results so far in validation.

If you are using LTR, I’d suggest neutralizing targets before training. With even a very slight neutralization proportion, the targets become far less discrete and can provide a lot more information when generating pairs or lists for the ranking task. I ran an optuna optimization to check whether I should train on the given nomi target or a neutralized version of it (along with some other hyperparameters to tune) and overwhelmingly pre-training target neutralized models had better performance and it was the most important hyperparameter:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c7b592671e270a115a162fb58234acf1478b7f41_2_690x228.png)image1687×559 22.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c7b592671e270a115a162fb58234acf1478b7f41.png> "image")

We can also search over different degrees of neutralization to train on. The objective value here I was trying to optimize was mean correlation of all eras across all folds. If you look at the “target” column, you can see the contour plot of different hyperparameter trials and their scores–and they all roll down (in a good way) towards target neutral:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8dd66a25e7041c658aca4c57e04e27c716e3a1ef_2_690x320.jpeg)image1242×576 131 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8dd66a25e7041c658aca4c57e04e27c716e3a1ef.jpeg> "image")

---

### Post #15 — **eleven_sigma** | 2021-09-22 12:45 UTC _(reply to #14)_

Interesting… these objective values are using validation dataset too? and how many folds? Is very useful for having a reference.  
Thanks.

---

### Post #16 — **jrai** | 2021-09-22 16:06 UTC _(reply to #15)_

This was 3 folds with the folds being era-wise groupings with a purge of eras between the end of train and the start of test indices. The objective value is measured as the mean correlation on the val set across those folds. Only using the training data for generating the val set in each fold. Optuna also has multi-objective optimization so you can search for hyper parameters that maximize both mean correlation and sharpe across the folds.

---

### Post #17 — **galskari** | 2022-01-07 06:53 UTC _(reply to #16)_

Can you show a snippet of how you provide the optuna optimizer those 3 unique folds?

I’ve been trying this but it doesn’t really work. y is simply a rank of 1…n of the documents
    
    
    model = xg.XGBRanker(
        objective='rank:ndcg',
        random_state=42,
        subsample=0.75,
        min_child_weight=0.06
        )
    
    param_dist = {'n_estimators': [20,50,100],
                  'learning_rate': [0.01,0.2, 0.59],
                  'max_depth': [3, 4, 5],
                  }
    scorer = sklearn.metrics.make_scorer(sklearn.metrics.ndcg_score, greater_is_better=True)
    gkf = GroupKFold(n_splits=5)
    groups = train_data[era_column_name]
    cv = gkf.split(x_train, y_train, groups=groups)
    cv_group = gkf.split(x_train, groups=groups)
    # generator produces `group` argument for LGBMRanker for each fold
    def group_gen(flatted_group, cv):
        for train, _ in cv:
            yield np.unique(flatted_group.iloc[train], return_counts=True)[1]
    gen = group_gen(groups, cv_group)
    # separate CV generator for manual splitting groups
    
    
    clf = sklearn.model_selection.GridSearchCV(model,
                                               param_grid=param_dist,
                                               cv=cv,
                                               scoring=scorer,
                                               verbose=10,
                                               n_jobs=1)
    
    clf.fit(X=x_train, y=y_train, group=next(gen))
    

I get the following error
    
    
    ValueError: Only ('multilabel-indicator', 'continuous-multioutput', 'multiclass-multioutput') formats are supported. Got multiclass instead
    

[@jrai](</u/jrai>) [@jrb](</u/jrb>)

---

### Post #18 — **chintanjoshi** | 2022-04-01 11:00 UTC _(reply to #17)_

I think the issue is XGB/LGBM rate groups in a different way then the groups in the sklearn CV function. IF you have 100 eras/dates for 100 stocks then the length of array for grouping for XGB/LGBM is 100 (100 repeated 100 times) while for CV this has to be length 10000 (1…100 repeated 100 time), as an example. I am not quite sure how to resolve this issue. Any thoughts?

---

### Post #19 — **jmrichardson** | 2022-12-14 20:50 UTC

Has anyone had any luck using LGBMRanker? Unfortunately, LGBMRanker results are much worse than XGBRanker. Here is the code for both:
    
    
    params = {
            'max_depth': 5,
            'learning_rate': .01,
            'n_estimators': 2000,
            'colsample_bytree': 0.1,
            # 'label_gain': [0, 1, 2, 3, 4],
        }
    
        group = train.groupby("era")["era"].count().to_numpy()
    
        model = lgbrank(**params)
        model = model.fit(train.drop(columns=['era', 'label']), train.label, group=group)
    
        model = XGBRanker(**params)
        model = model.fit(train.drop(columns=['era', 'label']), train.label, group=group)
    

XGBRanker mean correlation: .025  
LGBMRanker mean correlation: .0067

Thanks for any help

---

### Post #20 — **taori** | 2022-12-15 09:18 UTC _(reply to #19)_

I wonder what is the default objective for `LGBMRanker`. `XGBRanker` defaults to `objective='rank:pairwise'`. That could be the reason of the different results

---

### Post #21 — **jmrichardson** | 2022-12-15 15:59 UTC _(reply to #20)_

The default for lgbmranker is lambdarank which I believe is also pairwise. I tried changing the objective to rank_xendcg and got a little better results of .017. However, it is still significantly worse than xgbranker.

---

### Post #22 — **taori** | 2022-12-15 16:51 UTC _(reply to #21)_

The algorithms behind `LGBMRanker` and `XGBRanker` are similar but still different. So there is no guarantee that using the same hyperparameters results in the same predictions from both rankers. I wouldn’t be too suspicious about that difference in the results. You might try several sets of hyperparameters and find that a particular set gives better results on `LGBMRanker` than `XGBRanker`

---

### Post #23 — **jmrichardson** | 2022-12-15 17:11 UTC _(reply to #22)_

I did try optuna but never got correlation close to xgbranker. The only thing I didn’t try was changing the number of estimators because I usually try to keep them constant until evaluation as a secondary step. Thank you for letting me know that the algos are similar and perhaps it is just a case of not having the right parameters (will keep trying).

---

### Post #24 — **sneaky** | 2022-12-16 23:41 UTC _(reply to #19)_

I am using LGBM with custom objective functions. I tried LGBMRanker but it wasn’t flexible enough.  
This one is mean group rank correlation:
    
    
    def fobj_mean_group_corr(ypred,ytruex):
        groups = ytruex.get_group()
        ytrue = ytruex.get_label()
        return mean_group_corr(ypred,ytrue,groups)
    
    def mean_group_corr(ypred,ytrue,groups):
        # convert to pytorch tensors
        ypred_th = torch.tensor(ypred, requires_grad=True).float()
        # adding some noise
        ypred_th = ypred_th + torch.normal(0,0.0001,ypred_th.size())
        ytrue_th = torch.tensor(ytrue).float()
    
        all_corrs = []
    
        pivot = 0
        result = 0
        for g in groups:
            idxes = list(range(pivot,pivot+g))
            #print(ytrue_th[idxes].detach())
    
            pred = torch.flatten(
                torchsort.soft_rank(
                    torch.reshape(ypred_th[idxes],(1,g)),
                    regularization="l2",
                    regularization_strength=1,
                )
            )/torch.tensor(g)
            corr_res = torch.sqrt(- torch_corr(pred,ytrue_th[idxes]) +  torch.tensor(1))
            all_corrs.append(corr_res)
            pivot += g
    
        all_corrs = torch.stack(all_corrs)
    
        # calculate mean
        loss = all_corrs.mean()
        print(f'MGC Current loss:{loss}')
    
        # calculate gradient and convert to numpy
        loss_grads = grad(loss, ypred_th, create_graph=True)[0]
        loss_grads = loss_grads.detach().numpy()
        print(loss_grads)
    
        # return gradient and ones instead of Hessian diagonal
        return loss_grads, np.ones(loss_grads.shape)

---

### Post #25 — **gbrecht** | 2023-03-19 09:03 UTC _(reply to #24)_

Thank you very much for sharing this idea.  
Is there any reason you are adding noise to the predictions? Is it needed to get a unique sorting?

---

### Post #26 — **sneaky** | 2023-03-20 08:21 UTC _(reply to #25)_

If I remember it correctly, if predictions are all zeros/ones/… then soft_rank returns also one number everywhere, and the autograd returns nans. So this was my hack fix. It is not pretty but it works.

---

### Post #27 — **gbrecht** | 2023-03-20 08:23 UTC _(reply to #26)_

I had this issue as well. I think the reason is that the custom objective does not work from the start.

With your method you are introducing (a very small) randomness all the time. I had success with the following two hacks:

  * completely randomize the predictions in the first round
  * boost one tree with a normal objective



Both of these only affect the start

---

### Post #28 — **sneaky** | 2023-03-20 08:28 UTC _(reply to #27)_

The randomness should not matter in the end right? But it is better to get rid of it, because it is an unnecessary step that the model calculates all the time for nothing.

---

### Post #29 — **gbrecht** | 2023-03-20 08:40 UTC _(reply to #28)_

yes, you are right.  
A post has to be at least 20 characters

---

### Post #30 — **sneaky** | 2023-03-21 13:30 UTC _(reply to #29)_

Tried your solution and the results were sadly underwhelming. Maybe I did something wrong. 1 epoch wasn’t enough and often even with 100 epochs pretrained the models were failing to learn. I measured the time that the function saves by dumping the noise line and it is like 0.001 seconds. So with 30000 epochs its is like half a second. So I am gonna stick to my implementation for now. But thank you for the input!
