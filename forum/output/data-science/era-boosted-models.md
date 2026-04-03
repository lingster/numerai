---
title: "Era Boosted Models"
category: Data Science
url: https://forum.numer.ai/t/era-boosted-models/189
created_at: 2020-04-19T22:31:01.733000+00:00
last_posted_at: 2021-10-10T13:13:03.393000+00:00
posts_count: 22
views: 15519
tags: []
---

# Era Boosted Models

---

### Post #1 — **richai** | 2020-04-19 22:31 UTC

I want to share a new model that we have studied internally at Numerai. We think it is a big improvement over the current example predictions model and the simple idea behind it could be helpful to many Numerai data scientists. So we want to share it.

Our current example predictions have performed well over the last few months and currently place 27th in the tournament. The example predictions are built from a simple XGBoost model but with some important tweaks such as setting colsample_bytree=0.1 to reduce overfitting to specific features.

Let’s look at the in sample performance of the example predictions as we train that model on the training data.

**After 10 trees**  
`era_scores.plot(kind="bar")`  
`plt.show()`  


[![10 trees](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/4de5f4bf34751fc080ff39bbf9e3a44d42d4e418.png)10 trees390×274 9.02 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/4de5f4bf34751fc080ff39bbf9e3a44d42d4e418.png> "10 trees")

As you can see even after 10 trees the model is has learned to get positive correlation in most eras. However, there are still many eras with very weak or even negative correlations. (The x-axis here is eras in order - apologies for the image.)

**After 200 trees**  
`era_scores.plot(kind="bar")`  
`plt.show()`

[![performance through time](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/ae83da708819dd76d73571191a34286c4c0cc0bb.png)performance through time390×274 9.27 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/ae83da708819dd76d73571191a34286c4c0cc0bb.png> "performance through time")

After 200 trees, there are fewer negative eras and of course the mean correlation is a lot higher however performance of the model is very inconsistent even in sample. Because of the large standard deviation between eras, the Sharpe of this model is only 2.28 in sample after 100 trees. We can see the problem here is that the XGBoost model is really just trying to maximize it’s mean performance over the training data it is not also trying to minimize the standard deviation of returns across eras or produce a stationary model through time (see post on [Performance Stationarity](<http://forum.numer.ai/t/performance-stationarity/151/3>)).

So can we improve the XGBoost model we use in example predictions so that it cares about improving Sharpe over time not just mean correlation? It is possible that there are fancy neural network architectures and cost functions that can do this directly in the learning. But there’s another way; borrowing ideas from boosting we can simply upweight the eras we want to improve not just the training examples. We call this Era Boosting.

**The Era Boosting algorithm**  
Build 10 trees on all eras in the training data  
Predict with your model over the training data and see which eras are in the worst half of performance vs the other eras  
Then build 10 new trees but only on the worst half of eras  
Predict with all your trees over the training data and see which eras are in the worst half of performance vs the other eras  
Then build 10 new trees but only on the worst half of eras… repeat

**Era Boosting in action**  
The first 10 trees are the same as example predictions - they are built with all eras  


[![10 trees era boost](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/bb330ccbf5e413d1fcccc328f7c052f71fb82965.png)10 trees era boost396×274 10.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/bb330ccbf5e413d1fcccc328f7c052f71fb82965.png> "10 trees era boost")

But after 200 trees where every 10 trees we told the model to only build trees for the eras where it was underperforming the results change dramatically.  


[![200 trees](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/96650ce3078acb1c647807f00cb89216a94e5702.png)200 trees381×274 9.43 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/96650ce3078acb1c647807f00cb89216a94e5702.png> "200 trees")

With the same number of trees as before, we now have no negative eras and the eras have consistent and similar performance with low standard deviation among era performance. The in sample Sharpe here is now 21.99.

By building trees on only the worst performing eras, we are in a sense asking the model to learn something that gives equal performance across all eras and minimizes the performance difference between a good era and a bad era. We are asking the model to learn something more stationary and consistent and so it does.

Btw the era boosted models also have lower autocorrelation and higher Smart Sharpe in sample than regular models (see again [Performance Stationarity](<http://forum.numer.ai/t/performance-stationarity/151/3>)).

Michael wrote up some simple code to do era boosting which I have shared below. I think we’ll integrate the idea into example scripts soon and perhaps use the idea for a new version of example predictions.

**Open questions:**  
I didn’t talk about out of sample performance in this post - Sharpe of 22 is absolutely an overfit so how can one use this idea without overfitting so quickly? Does it need slower learning rate?  
Does era boosting really perform better than example predictions if you did cross validation by holding out groups of eras?  
We equal weight all the worst performing eras but perhaps they should have weights that grow in some exponential way like AdaBoost does.  
Can bagging on eras help for example choosing a random sample of 67% of eras before selecting the worst half of eras? This would let the model see a more diverse distribution of eras.  
Do the era boosted models automatically feature neutralize themselves in some sense or do they also take on high feature exposures? Is their feature exposure lower than eg preds?
    
    
    def ar1(x):
        return np.corrcoef(x[:-1], x[1:])[0,1]
    
    def autocorr_penalty(x):
        n = len(x)
        p = ar1(x)
        return np.sqrt(1 + 2*np.sum([((n - i)/n)*p**i for i in range(1,n)]))
    
    def smart_sharpe(x):
        return np.mean(x)/(np.std(x, ddof=1)*autocorr_penalty(x))
    
    import matplotlib.pyplot as plt
    def era_boost_train(X, y, era_col, proportion=0.5, trees_per_step=10, num_iters=200):
        model = GradientBoostingRegressor(max_depth=5, learning_rate=0.01, max_features="sqrt", subsample=0.5, n_estimators=trees_per_step, warm_start=(num_iters>1))
        features = X.columns
        model.fit(X, y)
        new_df = X.copy()
        new_df["target"] = y
        new_df["era"] = era_col
        for i in range(num_iters-1):
            print(f"iteration {i}")
            # score each era
            print("predicting on train")
            preds = model.predict(X)
            new_df["pred"] = preds
            era_scores = pd.Series(index=new_df["era"].unique())
            print("getting per era scores")
            for era in new_df["era"].unique():
                era_df = new_df[new_df["era"] == era]
                era_scores[era] = spearmanr(era_df["pred"], era_df["target"])[0]
            era_scores.sort_values(inplace=True)
            worst_eras = era_scores[era_scores <= era_scores.quantile(proportion)].index
            print(list(worst_eras))
            worst_df = new_df[new_df["era"].isin(worst_eras)]
            era_scores.sort_index(inplace=True)
            era_scores.plot(kind="bar")
            print("performance over time")
            plt.show()
            print("autocorrelation")
            print(ar1(era_scores))
            print("mean correlation")
            print(np.mean(era_scores))
            print("sharpe")
            print(np.mean(era_scores)/np.std(era_scores))
            print("smart sharpe")
            print(smart_sharpe(era_scores))
            model.n_estimators += trees_per_step
            print("fitting on worst eras")
            model.fit(worst_df[features], worst_df["target"])
        return model
    
    boost_model = era_boost_train(train_features, train_targets["target_kazutsugi"], era_col=train_targets["era"], proportion=0.5, trees_per_step=10, num_iters=20)

---

### Post #2 — **benben11** | 2020-04-20 16:08 UTC

That is a pretty interesting topic. Just adding my 2 cents here.  
If we refer to the previous discussions about performance stationarity, this seems like the perfect solution.  
I have not looked at the model myself but does it generalizes at all? What are the results on the validation period?  
I assume it is not too complex to achieve this result with trees. Just fit each era independently and ensemble the trees for example should give something probably 90% of the way there I imagine ( do not quote me on this ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13) ).  
This brings me to the important point that I think Numerai meant by performance stationarity, and it is instead model stationarity. If the model is fitted and behaving differently across eras of the training set, I do not believe this model has much chance of generalizing well as we have a limited set of eras. This is the typical bias/variance trade off.

---

### Post #3 — **mdo** | 2020-04-20 19:41 UTC

Era boosting with XGBoost.
    
    
    from xgboost import XGBRegressor
    
    def spearmanr(target, pred):
        return np.corrcoef(
            target,
            pred.rank(pct=True, method="first")
        )[0, 1]
    
    def era_boost_train(X, y, era_col, proportion=0.5, trees_per_step=10, num_iters=200):
        model = XGBRegressor(max_depth=5, learning_rate=0.01, n_estimators=trees_per_step, n_jobs=-1, colsample_bytree=0.1)
        features = X.columns
        model.fit(X, y)
        new_df = X.copy()
        new_df["target"] = y
        new_df["era"] = era_col
        for i in range(num_iters-1):
            print(f"iteration {i}")
            # score each era
            print("predicting on train")
            preds = model.predict(X)
            new_df["pred"] = preds
            era_scores = pd.Series(index=new_df["era"].unique())
            print("getting per era scores")
            for era in new_df["era"].unique():
                era_df = new_df[new_df["era"] == era]
                era_scores[era] = spearmanr(era_df["pred"], era_df["target"])
            era_scores.sort_values(inplace=True)
            worst_eras = era_scores[era_scores <= era_scores.quantile(proportion)].index
            print(list(worst_eras))
            worst_df = new_df[new_df["era"].isin(worst_eras)]
            era_scores.sort_index(inplace=True)
            era_scores.plot(kind="bar")
            print("performance over time")
            plt.show()
            print("autocorrelation")
            print(ar1(era_scores))
            print("mean correlation")
            print(np.mean(era_scores))
            print("sharpe")
            print(np.mean(era_scores)/np.std(era_scores))
            print("smart sharpe")
            print(smart_sharpe(era_scores))
            model.n_estimators += trees_per_step
            booster = model.get_booster()
            print("fitting on worst eras")
            model.fit(worst_df[features], worst_df["target"], xgb_model=booster)
        return model
    
    boost_model = era_boost_train(train_features, train_targets["target_kazutsugi"], era_col=train_targets["era"], proportion=0.5, trees_per_step=10, num_iters=20)

---

### Post #4 — **lackofintelligence** | 2020-04-21 02:50 UTC

Xgboost is still problematic run this way. Let’s modify [@mdo](</u/mdo>) 's code a bit:
    
    
    def era_boost_train(X, y, era_col, proportion=0.5, trees_per_step=10, num_iters=200, one_shot=False, tree_method='gpu_hist', test_model=None, note=None):
        print(f"\n#### Era boost train with proportion {proportion:0.3f} ####\n")
        if note is not None:
            print(note)
        if one_shot:
            trees_per_step = trees_per_step * num_iters
            num_iters=1
    
        if test_model is None:
            print(f"Train {num_iters} iterations")
            print(f"Train {trees_per_step} rounds per iteration")
        else:
            print("Testing model performance")
        features = X.columns
        new_df = X.copy()
        new_df["target"] = y
        new_df["era"] = era_col
        for i in range(num_iters):
            print(f"\nIteration {i+1}:\n")
            if test_model is None:
                if i==0:
                    model = XGBRegressor(max_depth=5, learning_rate=0.01, n_estimators=trees_per_step, n_jobs=-1, colsample_bytree=0.1, tree_method=tree_method)
                    model.fit(X, y)
                else:
                    model.n_estimators += trees_per_step
                    booster = model.get_booster()
                    print("fitting on worst eras")
                    model.fit(worst_df[features], worst_df["target"], xgb_model=booster)
            else:
                model = test_model
            # score each era
            print("predicting on train")
            preds = model.predict(X)
            new_df["pred"] = preds
            era_scores = pd.Series(index=new_df["era"].unique())
            print("getting per era scores")
            for era in new_df["era"].unique():
                era_df = new_df[new_df["era"] == era]
                era_scores[era] = spearmanr(era_df["pred"], era_df["target"])
            era_scores.sort_values(inplace=True)
            worst_eras = era_scores[era_scores <= era_scores.quantile(proportion)].index
            print(list(worst_eras))
            worst_df = new_df[new_df["era"].isin(worst_eras)]
            era_scores.sort_index(inplace=True)
            era_scores.plot(kind="bar")
            print("performance over time")
            plt.show()
            plt.savefig(outdir+f"fig_{i}.png")
            print("autocorrelation")
            print(ar1(era_scores))
            print("mean correlation")
            print(np.mean(era_scores))
            print("sharpe")
            print(np.mean(era_scores)/np.std(era_scores))
            print("smart sharpe")
            print(smart_sharpe(era_scores))
        return model
    
    

Now we run it setting the proportion equal to one. The idea is that we should get the same results either training incrementally or training all at once for that particular proportion. Let’s look at in sample and out of sample results.
    
    
    ifile = idir+"numerai_training_data.csv"
    print(f"Read Numerai training data from {ifile}...")
    df = pd.read_csv(ifile)
    features = [c for c in df if c.startswith("feature")]
    X = df[features]
    
    note = "First create era boosted model."
    boost_model_1 = era_boost_train(X, df["target_kazutsugi"], era_col=df["era"], proportion=1.0, trees_per_step=trees_per_step, num_iters=num_iters, note=note)
    note = "Now create a regular model."
    boost_model_2 = era_boost_train(X, df["target_kazutsugi"], era_col=df["era"], proportion=1.0, trees_per_step=trees_per_step, num_iters=num_iters, one_shot=True, note=note)
    
    print("\nRead Numerai Tournament data...\n")
    tfile = idir+"numerai_tournament_data.csv"
    tdf = pd.read_csv(tfile).set_index("id")
    tdf = tdf.loc[tdf['data_type'] == 'validation',].copy()
    X = tdf[features]
    note = "Look at out of sample for era-boosted model:"
    era_boost_train(X, tdf["target_kazutsugi"], era_col=tdf["era"], proportion=1.0, trees_per_step=trees_per_step, num_iters=num_iters, one_shot=True, test_model=boost_model_1, note=note)
    note = "Look at out of sample for regular model:"
    era_boost_train(X, tdf["target_kazutsugi"], era_col=tdf["era"], proportion=1.0, trees_per_step=trees_per_step, num_iters=num_iters, one_shot=True, test_model=boost_model_2, note=note)
    

Now the results:
    
    
    Read Numerai training data from ../input/ds_0208/numerai_training_data.csv...
    
    #### Era boost train with proportion 1.000 ####
    
    First create era boosted model.
    Train 3 iterations
    Train 10 rounds per iteration
    
    Iteration 1:
    
    predicting on train
    getting per era scores
    ['era68', 'era103', 'era58', 'era91', 'era104', 'era60', 'era69', 'era41', 'era9', 'era42', 'era107', 'era110', 'era106', 'era19', 'era113', 'era119', 'era101', 'era73', 'era49', 'era66', 'era27', 'era85', 'era50', 'era74', 'era67', 'era89', 'era75', 'era57', 'era116', 'era70', 'era112', 'era21', 'era26', 'era46', 'era7', 'era18', 'era33', 'era40', 'era100', 'era59', 'era82', 'era32', 'era102', 'era79', 'era65', 'era31', 'era87', 'era118', 'era17', 'era84', 'era11', 'era62', 'era97', 'era80', 'era35', 'era28', 'era2', 'era55', 'era14', 'era3', 'era15', 'era114', 'era54', 'era34', 'era117', 'era43', 'era81', 'era88', 'era56', 'era44', 'era39', 'era111', 'era72', 'era24', 'era13', 'era37', 'era99', 'era45', 'era77', 'era98', 'era93', 'era25', 'era10', 'era71', 'era29', 'era61', 'era96', 'era51', 'era53', 'era78', 'era86', 'era38', 'era20', 'era63', 'era8', 'era5', 'era6', 'era95', 'era47', 'era94', 'era23', 'era52', 'era1', 'era4', 'era64', 'era30', 'era12', 'era108', 'era120', 'era92', 'era36', 'era48', 'era115', 'era90', 'era76', 'era22', 'era109', 'era83', 'era105', 'era16']
    performance over time
    autocorrelation
    0.09222123754537882
    mean correlation
    0.06679633035407485
    sharpe
    2.1846286077155144
    smart sharpe
    1.9848699585634093
    
    Iteration 2:
    
    fitting on worst eras
    predicting on train
    getting per era scores
    ['era68', 'era103', 'era58', 'era91', 'era104', 'era60', 'era41', 'era69', 'era107', 'era66', 'era9', 'era42', 'era19', 'era106', 'era27', 'era49', 'era110', 'era85', 'era74', 'era101', 'era73', 'era113', 'era119', 'era67', 'era89', 'era75', 'era31', 'era7', 'era70', 'era40', 'era33', 'era50', 'era18', 'era79', 'era112', 'era100', 'era26', 'era57', 'era46', 'era116', 'era21', 'era59', 'era65', 'era82', 'era84', 'era55', 'era87', 'era32', 'era80', 'era118', 'era34', 'era2', 'era62', 'era114', 'era54', 'era17', 'era3', 'era35', 'era102', 'era111', 'era117', 'era11', 'era14', 'era15', 'era71', 'era25', 'era88', 'era81', 'era28', 'era37', 'era44', 'era97', 'era56', 'era98', 'era13', 'era24', 'era72', 'era51', 'era99', 'era43', 'era10', 'era45', 'era63', 'era78', 'era77', 'era39', 'era86', 'era29', 'era47', 'era93', 'era8', 'era61', 'era52', 'era6', 'era53', 'era20', 'era1', 'era38', 'era5', 'era94', 'era12', 'era96', 'era108', 'era23', 'era64', 'era90', 'era48', 'era120', 'era30', 'era95', 'era36', 'era115', 'era76', 'era92', 'era4', 'era22', 'era109', 'era16', 'era83', 'era105']
    performance over time
    autocorrelation
    0.10810158200051456
    mean correlation
    0.07308286520688552
    sharpe
    2.2883751249083386
    smart sharpe
    2.046323092280946
    
    Iteration 3:
    
    fitting on worst eras
    predicting on train
    getting per era scores
    ['era68', 'era103', 'era58', 'era91', 'era104', 'era60', 'era41', 'era69', 'era107', 'era66', 'era9', 'era106', 'era49', 'era27', 'era19', 'era42', 'era113', 'era85', 'era110', 'era89', 'era119', 'era101', 'era73', 'era31', 'era7', 'era67', 'era18', 'era33', 'era40', 'era100', 'era70', 'era46', 'era112', 'era26', 'era75', 'era74', 'era57', 'era84', 'era50', 'era116', 'era65', 'era21', 'era59', 'era79', 'era32', 'era80', 'era82', 'era34', 'era87', 'era55', 'era118', 'era25', 'era111', 'era62', 'era2', 'era114', 'era54', 'era35', 'era117', 'era3', 'era17', 'era15', 'era71', 'era88', 'era102', 'era81', 'era14', 'era11', 'era28', 'era97', 'era56', 'era37', 'era98', 'era44', 'era24', 'era1', 'era51', 'era13', 'era93', 'era43', 'era99', 'era29', 'era78', 'era47', 'era52', 'era72', 'era45', 'era10', 'era53', 'era39', 'era86', 'era77', 'era63', 'era8', 'era12', 'era61', 'era20', 'era94', 'era5', 'era6', 'era38', 'era90', 'era96', 'era23', 'era64', 'era48', 'era108', 'era36', 'era30', 'era115', 'era120', 'era22', 'era76', 'era92', 'era95', 'era109', 'era16', 'era4', 'era83', 'era105']
    performance over time
    autocorrelation
    0.10116833027108213
    mean correlation
    0.0782261415611412
    sharpe
    2.3853342448740174
    smart sharpe
    2.147903025024261
    
    #### Era boost train with proportion 1.000 ####
    
    Now create a regular model.
    Train 1 iterations
    Train 30 rounds per iteration
    
    Iteration 1:
    
    predicting on train
    getting per era scores
    ['era68', 'era103', 'era91', 'era58', 'era41', 'era69', 'era104', 'era60', 'era66', 'era107', 'era49', 'era106', 'era27', 'era19', 'era9', 'era42', 'era113', 'era85', 'era119', 'era101', 'era110', 'era31', 'era73', 'era112', 'era67', 'era7', 'era26', 'era40', 'era84', 'era89', 'era50', 'era100', 'era46', 'era116', 'era65', 'era18', 'era33', 'era75', 'era32', 'era79', 'era21', 'era74', 'era70', 'era57', 'era59', 'era34', 'era25', 'era80', 'era87', 'era82', 'era118', 'era55', 'era111', 'era35', 'era71', 'era17', 'era62', 'era114', 'era117', 'era3', 'era14', 'era54', 'era2', 'era88', 'era15', 'era1', 'era37', 'era102', 'era28', 'era98', 'era97', 'era51', 'era24', 'era93', 'era81', 'era56', 'era47', 'era29', 'era78', 'era10', 'era44', 'era99', 'era11', 'era52', 'era12', 'era43', 'era20', 'era13', 'era77', 'era39', 'era45', 'era53', 'era94', 'era86', 'era72', 'era6', 'era61', 'era38', 'era63', 'era8', 'era96', 'era90', 'era5', 'era36', 'era115', 'era64', 'era23', 'era48', 'era22', 'era108', 'era30', 'era76', 'era120', 'era92', 'era95', 'era16', 'era109', 'era83', 'era4', 'era105']
    performance over time
    autocorrelation
    0.08129248445845112
    mean correlation
    0.07639378884006609
    sharpe
    2.2663449766142603
    smart sharpe
    2.0817198544863738
    
    Read Numerai Tournament data...
    
    
    #### Era boost train with proportion 1.000 ####
    
    Look at out of sample for era-boosted model:
    Testing model performance
    
    Iteration 1:
    
    predicting on train
    getting per era scores
    ['era127', 'era131', 'era121', 'era125', 'era126', 'era129', 'era130', 'era122', 'era124', 'era123', 'era128', 'era132']
    performance over time
    autocorrelation
    -0.1550246653070757
    mean correlation
    0.03738069280208456
    sharpe
    1.4334015707235843
    smart sharpe
    1.583701400030438
    
    #### Era boost train with proportion 1.000 ####
    
    Look at out of sample for regular model:
    Testing model performance
    
    Iteration 1:
    
    predicting on train
    getting per era scores
    ['era127', 'era121', 'era126', 'era131', 'era125', 'era129', 'era122', 'era130', 'era123', 'era124', 'era128', 'era132']
    performance over time
    autocorrelation
    -0.19234565338406373
    mean correlation
    0.03568585451261579
    sharpe
    1.4905205172696703
    smart sharpe
    1.7057722745747308
    

So you see: In sample, trained incrementally, with exactly the same data, xgboost generates extra sharpe (no cheese). Out of sample the regularly trained xgboost performs better. One should be really careful using xgboost this way.

---

### Post #5 — **mdo** | 2020-04-21 06:39 UTC _(reply to #4)_

Hmmm, interesting, but those differences aren’t big enough to convince me that this isn’t just differences in how random seeds are used to select variables for the trees when training incrementally vs all in one go. When restarting training 3 times vs only once I could see how things could easily come out a bit different depending on exactly how things are implemented. I actually find your test a bit reassuring that things aren’t completely broken when training like this with xgboost.

---

### Post #6 — **smokh** | 2020-04-22 04:44 UTC

I am able to achieve similar results using neural networks with a custom loss function which adds to the mean squared error the squared standard deviation of absolute feature correlation coefficient with predictions

y_pred=[…]  
y_true=[…]  
corr_coefs=[…] #310 correlation coefficients with y_pred

mse= mean(square(y_pred - y_true)  
correlation_penalty= square(std(abs(corr_coefs)))  
loss= mse + correlation_penalty

in sample results  


[![insampleeras](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/e42e2fe056e909b0e63f3b39f562e2b4c5be20ce_2_690x231.png)insampleeras1711×575 14.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e42e2fe056e909b0e63f3b39f562e2b4c5be20ce.png> "insampleeras")

numerai_score_mean_across_eras~0.397  
sharpe~19.221

---

### Post #7 — **quantverse** | 2020-04-22 08:19 UTC

I made few tests with catboost but it seems after sufficient amount of trees it will end up with high sharpe ratio on training data anyway, even without messing with train data in between the training process.

---

### Post #8 — **jrdi** | 2020-04-24 11:03 UTC

After playing a bit with validation 2 dataset and realizing how bad are my models (it’s already shown by the live data but I was refusing to accept the reality), I’ve been trying different approaches, one of them focused on decreasing meta-model correlation and another one trying to improve correlation across eras while reducing feature exposure.

**Base model**

Train avg 0.09118565453972223, sharpe 2.61238059500593  
Val1 avg 0.08252843111050458, sharpe 3.173499533551588  
Val2 avg 0.008812162895404011, sharpe 0.28613703839300464

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e303b6c580f709023ebbca26b5e40f52ab8f41b3.png)image1167×452 3.33 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e303b6c580f709023ebbca26b5e40f52ab8f41b3.png> "image")

Feature exposure 0.08264085332303439

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/36289c7ec4693fdb0f1ad7106eb0bae6bff5cf40.png)image1159×466 4.79 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/36289c7ec4693fdb0f1ad7106eb0bae6bff5cf40.png> "image")

While validation 2 average correlation across eras was still positive, the sharpe ratio was a disaster, that’s why I’ve been trying to improve it using a different approach to the shown here but with quite similar results. Also, there is a group of features highly correlated with the predictions!

**Improved model**

After trying to reduce the correlation between features and predictions I ended with a model that looks better.

Train avg 0.17071569939420486, sharpe 7.353940587005201  
Val1 avg 0.16559936247951454, sharpe 8.009380660205698  
Val2 avg 0.011188128720098198, sharpe 0.6254681270125086

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/20e4a9331bd36ab3ef40735ed17974cad9951f5b.png)image1159×452 3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/20e4a9331bd36ab3ef40735ed17974cad9951f5b.png> "image")

Feature exposure 0.060100944750934554

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/fa49f3d7bc6d5b47c87ad3eac220c10436d61ccf.png)image1159×466 5.26 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/fa49f3d7bc6d5b47c87ad3eac220c10436d61ccf.png> "image")

The next step will be trying to include neutralization but I’m doubting between prediction neutralization and label neutralization, which do you think would be a better approach?

---

### Post #9 — **correlator** | 2020-05-30 09:23 UTC _(reply to #3)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> model.n_estimators += trees_per_step

Is this step necessary? This will result in increased number of tress as the iterations increase. Do we actually want that?  
Also please help me understand how .fit() works incrementally. In each iteration, we fit a new set of boosters by passing the earlier model, we also pass new (X, y) but will it also consider the weights of instances from previous model or the instance weights will start afresh again?

---

### Post #10 — **richai** | 2020-05-31 00:17 UTC _(reply to #9)_

Because warm_start is True the model will build “trees_per_step” new trees per step and add them to the existing trees. The new trees built will only look at the data in (X,y) and will therefore be different and help to fit those eras.

Because of warm_start I think the weights are being stored and improved upon but could be that the old weights on examples are ignored for the new trees because (X,y) is different.

---

### Post #11 — **surajp** | 2020-06-07 05:28 UTC _(reply to #8)_

By label Neutralization, you mean first Neutralize ‘target_kazutsugi’ and train unlike the one in example scripts which neutralizes the predictions?

---

### Post #12 — **bot42** | 2020-07-15 19:29 UTC

I’ve been trying the era boosting for a bit, but I can’t really seem to get meaningful out of sample performance. While score on the training data goes up almost linearly (as far as I’ve seen) the validation correlation doesn’t seem to improve much if at all. I’m admittedly not an expert and just playing around, but it really seems to me that it’s just overfitting. These are my current results after ~20 rounds, the “time” in the right plot is just the number of boosting iterations and the score is the average of the pearson correlation.

[![index](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/003fc34c7ab5986c1b17e21d84ecdcba97414af9_2_690x280.png)index758×308 17.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/003fc34c7ab5986c1b17e21d84ecdcba97414af9.png> "index")

[Edit] I just finished running it for 50 rounds, and the results seem to be the same:

[![index_50](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/17127c494d50d184173073ff806efd3d63934079_2_690x282.png)index_50751×308 18.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/17127c494d50d184173073ff806efd3d63934079.png> "index_50")

---

### Post #13 — **richai** | 2020-07-16 21:05 UTC _(reply to #12)_

0.025 correlation on validation is meaningful ![:slightly_smiling_face:](https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=13)

My experience with era boosting is that you tend to have more consistency (more good eras out of sample). From your results here, it looks like that’s true in your 20 round run only a few eras with negative performance? I think that’s better than the example predictions which doesn’t use era boosting isn’t it?

---

### Post #15 — **lingzhou125** | 2021-04-08 01:00 UTC _(reply to #13)_

I’m new to numerai and to datascience in general but a few questions came up as I saw this notebook in the example scripts folder.

My intuition tells me that era boosting will create the same problem as a heavily weighted feature. the problem is risk metrics used by numerai look for over-exposed features but I don’t think they’ll pick up on over-exposed eras, so maybe that’s why your corr is going up without an proportional increase in risk. Interested in what others think.

---

### Post #16 — **krizmanic** | 2021-04-12 22:06 UTC

To me, era boosting looks like a way to follow a specific method of overfitting. This problem has a host of answers, and to the extent that people use the same methodology to arrive at their answer, their answers are probably similar. People have contended that this is the best way, I’ve personally never used it, and don’t really see the need to. I like at least some originality ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=9)

---

### Post #17 — **evanhennis** | 2021-04-15 21:55 UTC _(reply to #6)_

I have so many questions…

I am going at this project by creating a NN with TensorFlow. My first model is just a simple NN across the data without anything special. My second model I want to use the eras as a guiding light. My original thought was to find the X closes eras to the live era and then train a smaller NN on those. But, I feel like I am assuming that my model expects history to repeat itself in the market and I am not sure that is how I want to go.

Anyway, for your model (if you want to give a beginner help), can you explain how you are able to get the eras to train on their own? I thought about doing a version of transfer learning where I would train on the eras closes to live but then also add back in the other eras and give them a few epochs.

---

### Post #18 — **gammarat** | 2021-04-15 23:30 UTC _(reply to #17)_

Try training on the broad data, like the simple NN model you mention, and then see which eras give a high Spearman correlation to your NN, and which don’t. Divide the eras into high scoring ones and low scoring ones, and then train different nets on each, as well as a discrimination function that can accurately (somewhat) assign an arbitrary era to its proper pile. Rinse and repeat until you have a few different subnets each trained in their own subgroups (which may overlap a bit) along with the associated discrimination functions. Just be careful not to overfit (too many subnets=inability to generalize).

That general approach seems to be giving me the best results, I’m new myself (My first submitted model just completed its first round, rather but not completely abysmally, so I’m feeling ![:+1:](http://forum.numer.ai/images/emoji/twitter/+1.png?v=9)).

FWIW, I don’t do NNs, just plain old math and stats, so my vocabulary may be a bit awkward.

---

### Post #19 — **olivepossum** | 2021-04-18 11:06 UTC _(reply to #18)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gammarat/48/3281_2.png) gammarat:

> Divide the eras into high scoring ones and low scoring ones, and then train different nets on each, as well as a discrimination function that can accurately (somewhat) assign an arbitrary era to its proper pile.

Regarding the discrimination function that can assign an arbitrary era to its proper pile, I’ve been struggling trying to find similarities among eras. So far I’ve tried this technique [[numerai] metric learning and 'live' era | Kaggle](<https://www.kaggle.com/code1110/numerai-metric-learning-and-live-era>) and also a simple per era PCA reduction to 2 components and average all rows for each era (last one was specially not successful).

Bor also shared info to cluster eras a while ago [Office Hours with Arbitrage #5. Bor shares his analysis of Numerai data… | by Anthony Mandelli | Numerai | Medium](<https://medium.com/numerai/office-hours-with-arbitrage-5-421ea23f4eec>)

Any other interesting approaches?

---

### Post #20 — **gammarat** | 2021-04-18 14:16 UTC _(reply to #19)_

Right now I’m using the sine of the principal angle between subspaces based on somewhere between 3 and 9 PCA coefficients. I’ve got a search running right now on that, as well as several other parameters, so I won’t know until later today (I put it in last night, and it still has a couple of hours to go. ![:crossed_fingers:](http://forum.numer.ai/images/emoji/twitter/crossed_fingers.png?v=9) there’s no power failures).

I put a [brief thread up on Rocket Chat](<https://community.numer.ai/channel/newusers?msg=gRW5fZZfdvbtHLQz2>) about how I’m approaching this, and if I get something useful I’ll write it up. But basically I use Gaussian mixture models based on those subspaces to separate different era regimes.

I did try various methods using PCA to invert the era data directly to targets, usually keeping ~90-95% of the variance, which means around 100+ coefficients. In the forward problem (calculating weights) it takes a while, but for the inverse problem (using weights to estimate targets) it’s very quick. And as those weights don’t change (they come from the training data, which doesn’t change usually from round to round), carrying out the predictions is pretty fast. I think it actually takes longer to write out the csv file than it does to do the inversions ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

ETA: re the principle angles:

[en.wikipedia.org](<https://en.wikipedia.org/wiki/Angles_between_flats>)

### [Angles between flats](<https://en.wikipedia.org/wiki/Angles_between_flats>)

The concept of angles between lines in the plane and between pairs of two lines, two planes or a line and a plane in space can be generalized to arbitrary dimension. This generalization was first discussed by Jordan. For any pair of flats in a Euclidean space of arbitrary dimension one can define a set of mutual angles which are invariant under isometric transformation of the Euclidean space. If the flats do not intersect, their shortest distance is one more invariant. These angles are call Let ...

It’s the kind of thing I like; it was invented in 1875. But I don’t do the calculations myself, I use MatLab’s “subspace” routine.

---

### Post #21 — **gammarat** | 2021-04-19 01:46 UTC _(reply to #19)_

On the PCA front – I did get something unexpected w/r to how many coefficients to use for the subspace weighting; it looks like I should have extended my search out further. I had set it to use from 3 to 9 coefficients, expecting it to fall off quickly as that part of the system became over determined. But it looks like I may have been wrong. The plot below shows the distribution of the number of coefficients used to determine the principle angle among the top quarter (42) of the (168) model results.

[![PcaSubspaceCoeffs](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/924afa531c886d3b842287f415c1ec0455ce82a3.jpeg)PcaSubspaceCoeffs560×420 10.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/924afa531c886d3b842287f415c1ec0455ce82a3.jpeg> "PcaSubspaceCoeffs")

Certainly 4 and five turned out to be popular, but from 7 to 9 things look to be making a good run of it. Will 10, 11, 12 (or higher) finish in the money? Stay tuned ![:tv:](https://emoji.discourse-cdn.com/twitter/tv.png?v=13)

Personally, I think that the result is probably due to using soft class membership rather than hard; I had to pick the top twelve models to replace the poorly performing ones I put in last month, and they all used soft membership.

---

### Post #22 — **murenoha** | 2021-07-16 00:34 UTC _(reply to #3)_

Thank you for sharing era boost idea and implementation.

The first argument of `spearmanr` defined in this script is `target`.  
but this function is used with `pred` specified as the first argument.

Pull Request

[github.com/numerai/example-scripts](<https://github.com/numerai/example-scripts/pull/82>)

####  [Fix to rank predictions instead of ranking targets](<https://github.com/numerai/example-scripts/pull/82>)

`master` ← `murenoha:fix-order-of-arguments-in-spearmanr`

opened 09:30AM - 10 Jul 21 UTC

[ ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b39175e97400b35509b5140fe1c1881297bfc7bb.png) murenoha ](<https://github.com/murenoha>)

[ +1 -1 ](<https://github.com/numerai/example-scripts/pull/82/files>)

Thank you for sharing era boost idea and implementation. # Summary Current[…](<https://github.com/numerai/example-scripts/pull/82>) code ranks targets. I fixed incorrect order of arguments in `spearmanr`. # Details The first argument of `spearmanr` defined in this script is `target`. ```python def spearmanr(target, pred): return np.corrcoef( target, pred.rank(pct=True, method="first") )[0, 1] ``` but this function is used with `pred` specified as the first argument. Therefore, this code ranks targets. ```python era_scores[era] = spearmanr(era_df["pred"], era_df["target"]) ``` I fixed to rank predictions.

I fixed incorrect order of arguments in `spearmanr`.

---

### Post #23 — **nickkon** | 2021-10-10 13:13 UTC _(reply to #10)_

At least for LGBM, I do not think that this is true. I believe (but am not sure anymore) that I also checked that behaviour with xgboost.  
I tried to use model.n_estimators += trees_per_step at first and noticed: Each iteration takes longer and longer to train which lead me to investigate that issue. I was using something like 100 trees per step and 10 iterations. I then did some tests with model.n_estimators += trees_per_step and without it.

Example with trees_per_step=5 and num_iters=10:

Without model.n_estimators += trees_per_step:  
model.n_estimators prints 5 which is logical since it got initialized with 5 trees.  
models.booster_.num_trees() prints 50 which is trees_per_step*num_iters. So 50 trees have been build with 5 per iterations, as expected. The elapsed time for each iteration is about equals since it always trains the same number of trees (5).

With model.n_estimators += trees_per_step:  
model.n_estimators prints 50. The parameter n_estimators is a cumulative sum of trees_per_step for each iteration, thus the final value is trees_per_step*num_iters. Seems correct.

But: models.booster_.num_trees() prints 275 which means that 275 trees have been build. This seems weird at first. But since each iterations has an increasing number of n_estimators, it means that more and more trees are build per iterations: The first iteration builds 5 trees, the next one 10, the one after it 15, 20, 25 up until the last iteration which builds trees_per_step*num_iters trees. The final number of trees is the sum of trees for each iteration: sum((i+1)*trees_per_step for i in range(num_iters)) = 275.  
Since ever iteration is building trees_per_step more trees, the training time keeps increasing from each iteration to each iteration.

Using model.n_estimators += trees_per_step or not does give different results. I added “commulative_trees: bool=False” as a parameter to decide whether I want n_estimators to keep increasing or not. The intuition behind using it might be something like:  
Fit 5 trees on the easy eras, calculate the worst performing eras and use more and more trees to fit them since they are ‘harder’ to predict.
