---
title: "Era-wise Time-series Cross Validation"
category: Data Science
url: https://forum.numer.ai/t/era-wise-time-series-cross-validation/791
created_at: 2020-08-18T23:55:56.489000+00:00
last_posted_at: 2021-11-05T14:05:02.001000+00:00
posts_count: 25
views: 11886
tags: []
---

# Era-wise Time-series Cross Validation

---

### Post #1 — **mdo** | 2020-08-18 23:55 UTC

In case you’re not aware, the time-series cross-validation code in sklearn takes a groups argument, but doesn’t actually use it! I like using time-series cross-validation since it prevents you from using any future information to predict out of sample, since your out of sample test set is always in the future. I wrote a sklearn compatible cross validation splitter that can use eras as groups so your splits are always erawise. Below is example code for doing a hyperparameter grid search with XGBoost and era-wise time-series cross validation. My models [Niam](<https://numer.ai/niam>), [NMRO](<https://numer.ai/nmro>), and [MDO](<https://numer.ai/mdo>) were trained in exactly this way (but with different parameter ranges than are used below). MDO also drops some of the worst and best features (according to feature importance) with the exact choices of what to drop determined by this cross validation strategy. See, nothing fancy needed to get a top 3 model ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=9) Now take this information and make even better models!
    
    
    from sklearn.model_selection._split import _BaseKFold, indexable, _num_samples
    from sklearn import model_selection, metrics 
    import pandas as pd
    import numpy as np
    from xgboost import XGBRegressor
    import csv
    from scipy.stats import spearmanr 
    
    
    with open('numerai_training_data.csv', 'r') as f:
        column_names = next(csv.reader(f))
        dtypes = {x: np.float32 for x in column_names if
                  x.startswith(('feature', 'target'))}
    data = pd.read_csv('numerai_training_data.csv', dtype=dtypes, header=0, index_col=0)
    
    
    features = [f for f in data.columns if f.startswith("feature")]
    target = "target_kazutsugi"
    data["erano"] = data.era.str.slice(3).astype(int)
    eras = data.erano
    
    class TimeSeriesSplitGroups(_BaseKFold):
        def __init__(self, n_splits=5):
            super().__init__(n_splits, shuffle=False, random_state=None)
    
        def split(self, X, y=None, groups=None):
            X, y, groups = indexable(X, y, groups)
            n_samples = _num_samples(X)
            n_splits = self.n_splits
            n_folds = n_splits + 1
            group_list = np.unique(groups)
            n_groups = len(group_list)
            if n_folds > n_groups:
                raise ValueError(
                    ("Cannot have number of folds ={0} greater"
                     " than the number of samples: {1}.").format(n_folds,
                                                                 n_groups))
            indices = np.arange(n_samples)
            test_size = (n_groups // n_folds)
            test_starts = range(test_size + n_groups % n_folds,
                                n_groups, test_size)
            test_starts = list(test_starts)[::-1]
            for test_start in test_starts:
                
                yield (indices[groups.isin(group_list[:test_start])],
                       indices[groups.isin(group_list[test_start:test_start + test_size])])
    
    
    def spearman(y_true, y_pred): 
        return spearmanr(y_pred, y_true).correlation 
    
    
    cv_score = []
    models = []
    for lr in [0.006, 0.008, 0.01, 0.012, 0.014]:
        for cs in [0.06, 0.08, 0.1, 0.12, 0.14]:
            for md in [4, 5, 6]:
                models.append(XGBRegressor(colsample_bytree=cs, learning_rate=lr, n_estimators=2000, max_depth=md, nthread=8))
    
    
    
    for model in models:
        score = np.mean(model_selection.cross_val_score(
                    model,
                    data[features],
                    data[target],
                    cv=TimeSeriesSplitGroups(5),
                    n_jobs=1,
                    groups=eras,
                    scoring=metrics.make_scorer(spearman, greater_is_better=True)))
        cv_score.append(score)
        print(cv_score)

---

### Post #2 — **zempe** | 2020-08-22 17:43 UTC

Hi,  
thanks for sharing again (also said that in the chat).  
The results are like that:  
[0.04468379562495979]  
[0.04468379562495979, 0.04466911064704264]  
[0.04468379562495979, 0.04466911064704264, 0.044610228323998906]

How can I read it?  
Since it is nested for loop, does that mean that the first line is lr=0.006 + cs = 0.06 + md = 4 and then the third line is: lr=0.006 + cs = 0.06 + md = 6

Any help, super appreciated!

---

### Post #3 — **jorijnsmit** | 2020-08-22 19:07 UTC _(reply to #2)_

I believe the `print(cv_score)` should be outside the for loop.

To answer your question [@zempe](</u/zempe>); try verifying your assumptions by printing those arguments in the for loop, e.g. `print(model.learning_rate, score)`.

---

### Post #4 — **jorijnsmit** | 2020-08-22 19:18 UTC

[@mdo](</u/mdo>) can you elaborate on how your custom class differs from [`GroupKFold`](<https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html>)?

---

### Post #5 — **koerrie** | 2020-08-25 10:57 UTC _(reply to #1)_

Thank you for sharing this code snippet!  
It got me thinking about how to do proper cross validation on this dataset.

However I might have found a bug in your code.  
Since eras are strings in the Pandas Dataframe taking unique values with Numpy produces for the following group_list variable:  
[‘era1’ ‘era10’ ‘era100’ ‘era101’ ‘era102’ … ‘era96’ ‘era97’ ‘era98’ ‘era99’]

The eras are not properly ordered.  
This can be fixed by changing the definition of the eras to only take the integer part in account:  
eras = pd.Series([int(era[3:]) for era in data.era])

---

### Post #6 — **mdo** | 2020-08-25 23:42 UTC _(reply to #5)_

Thanks [@koerrie](</u/koerrie>) good catch! It’s fixed now. I actually had it right like it is now in my original code, but I guess that’s what I get for trying to simplify code I haven’t looked at in while ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=9)

---

### Post #7 — **mdo** | 2020-08-26 00:13 UTC _(reply to #2)_

You can just look at the corresponding object in the models list to find the parameters that go with any of the scores

---

### Post #8 — **mdo** | 2020-08-26 00:18 UTC _(reply to #4)_

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/344ff0d5688fa29bdb8cfdc4d37093b8771ce52f.png)image600×300 11.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/344ff0d5688fa29bdb8cfdc4d37093b8771ce52f.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/94faaf266e082873a5b3965134502364f29634fd.png)image600×300 12 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/94faaf266e082873a5b3965134502364f29634fd.png> "image")

  
This is like the latter but splits are only between consecutive eras/groups which is not true for the sklearn version.

---

### Post #9 — **rgsw** | 2020-09-01 00:30 UTC

I’m fairly new to this so sorry if this is a dumb question. Once you find the optimal set of parameters, and you’re ready to fit the model, is there a way to incorporate the era groups? Or would you just use fit() as normal?

---

### Post #10 — **jrdi** | 2020-09-01 07:25 UTC _(reply to #8)_

[@mdo](</u/mdo>) thanks for the original post and for the plot, really illustrative. I’ve been participating in Numerai for a while but also been working as a data scientist in time series problems. I’ve always used the TimeSeriesSplit approach to force testing on “future” data but always tried to keep using the same amount of training data in each fold.

I mean, if you are using 4 eras for training and 2 for testing in iteration 0, I’d prefer to use 4+2 also in iteration 1 and so on, but seems you’re using 8+2. I don’t have a strong opinion here, and since you are using the same approach for all models it should be ok. In my mind, it resonates as the average error metric won’t be accurate since I’d expect iteration 3 to be better (or worse if your model gets easily overfitted) than iteration 0 because it’s using more training data.

Edit: I’ve found an illustrative image for both approaches.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/46b341edd56e7753f17390af3f6b2ec2984120d2_2_690x182.png)696×184 25.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/46b341edd56e7753f17390af3f6b2ec2984120d2.png>)

Is there some reasoning to use “Expanding window” over “sliding window”?

---

### Post #11 — **lackofintelligence** | 2020-09-07 02:03 UTC _(reply to #10)_

Many of my base models use time-series CV. Until [@mdo](</u/mdo>) made that post I did not think anybody else used it. For the models that I have using time-series-CV, I also used an expanding window. My reasoning is that I want the fold size to approach the size of the final training data set because if you use a fixed size which is much smaller than the final training data set size then you might train models that are too greedy and so there is a much greater chance of over-fitting. When we were only allowed 3 models I weighted those ensembles much more to the time-series CVed models and they reached the top 100 very quickly.

---

### Post #12 — **objectscience** | 2020-09-19 23:00 UTC _(reply to #6)_

Edit: I clearly fail at reading and in-line responses. Zempe was already given an answer to the posed question.

---

### Post #13 — **jeremy_berros** | 2020-10-06 00:06 UTC

Hi [@mdo](</u/mdo>). In Advances in Financial Machine Learning Marcos Lopez de Prado addresses the failures of CV for financial time series mostly because of false assumptions of observations drawn from an IID process and the leakage / overlap that results from it. As a solution Marcos suggests "purging " and “embargoing” data between training and test sets with a “Purged/Embargoed K-Fold CV”. Now in the case of applying your Era-wise Time-series CV on Numerai training data (especially Nomi) and considering that the eras provided are in chronological order would it make sense to apply such purging / embargoing? To illustrate here is a slide from Marcos’ lecture at Cornell University available online:

[![Capture](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/c0bb383c7f6279c4c6b4114c5043763e0cf6a1f1_2_690x395.jpeg)Capture1509×864 109 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c0bb383c7f6279c4c6b4114c5043763e0cf6a1f1.jpeg> "Capture")

---

### Post #14 — **mdo** | 2020-10-08 17:31 UTC _(reply to #13)_

There really shouldn’t be a problem with overlap that purging is designed to fix, but you could always try it for added safety. I had considered adding it, but didn’t seem worth it so haven’t explored at all so ymmv. Should be pretty easy to modify my code (or sklearn’s group k-fold) to add the option.

---

### Post #15 — **jeremy_berros** | 2020-10-08 20:36 UTC

So there is no overlap/leakage in the provided dataset. That answers my main question. Thank you [@mdo](</u/mdo>)

---

### Post #16 — **jrai** | 2020-12-21 19:03 UTC _(reply to #15)_

<https://www.kaggle.com/marketneutral/purged-time-series-cv-xgboost-optuna>

---

### Post #17 — **shatteredx** | 2021-01-18 02:50 UTC

Using scipy.stats.spearmanr.correlation to score my model gives the following validation mean: 0.0250.

However, the numerai website calculates this same model having validation mean: 0.0254.

Is this small difference expected? The model is the example model: XGBRegressor(max_depth=5, learning_rate=0.01, n_estimators=2000, n_jobs=-1, colsample_bytree=0.1)

Sorry if this is a dumb question. I am a data science noob.

---

### Post #20 — **shonumerai123** | 2021-01-18 19:08 UTC _(reply to #17)_

Did you calculate the mean of era-wise correlations?  
If you just calculated the correlation ignoring the eras, that could have been the cause of the small difference?

---

### Post #21 — **shatteredx** | 2021-01-18 23:02 UTC _(reply to #20)_

[@shonumerai123](</u/shonumerai123>) You’re right, I just calculated the correlation ignoring the eras. My mistake, thank you for pointing this out.

So, I just went back to my code and calculated the mean of the era-wise correlations using spearmanr.correlation, here are the results:

numer.ai era-wise validation correlation: 0.0254  
spearmanr era-wise validation correlation: 0.0255

So, there appears to still be a small difference!

Code snippet:
    
    
    from scipy.stats import spearmanr 
    import numpy as np
    
    # Numerai correlation functions
    def correlation(targets, predictions):
        ranked_preds = predictions.rank(pct=True, method="first")
        return np.corrcoef(ranked_preds, targets)[0, 1]
    def score(df):
        return correlation(df[TARGET_NAME], df[PREDICTION_NAME])
    
    #Spearman scoring
    def spearmandf(df):
        return spearmanr(df[PREDICTION_NAME], df[TARGET_NAME]).correlation
    
    #read data
    training_data = pd.read_csv("https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_training_data.csv.xz")
    tournament_data = pd.read_csv("https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_tournament_data.csv.xz")
    validation_data = tournament_data[tournament_data.data_type == "validation"].copy()
    
    #features and eras
    feature_names = [
        f for f in training_data.columns if f.startswith("feature")
    ]
    training_data["erano"] = training_data.era.str.slice(3).astype(int)
    eras = training_data.erano
    target = "target"
    
    #model
    model = XGBRegressor(max_depth=5, learning_rate=0.01, n_estimators=2000, n_jobs=-1, colsample_bytree=0.1)
    model.fit(training_data[feature_names], training_data[TARGET_NAME])
    
    #predictions
    valpredictions = model.predict(validation_data[feature_names])
    validation_data[PREDICTION_NAME] = valpredictions.copy()
    
    #numerai score
    validation_correlations = validation_data.groupby("era").apply(score)
    print(validation_correlations.mean())
    
    #spearman score
    validation_correlations = validation_data.groupby("era").apply(spearmandf)
    print(validation_correlations.mean())

---

### Post #22 — **mdo** | 2021-01-18 23:57 UTC

Yes you should use the numeral correlation function, instead of `spearmanr` as that is the correct scoring function. I sometimes just use `spearmanr` because it’s convenient and, as you found, gives virtually identical answers. The difference is `spearmanr` ranks both inputs (rather than just predictions) before calling the Pearson correlation function.

---

### Post #24 — **sirbradflies** | 2021-08-20 04:23 UTC _(reply to #14)_

Here’s a slightly modified version introducing also the purging. In my understanding the embargo makes sense only for KFold CV so simply purging the periods between the Train and Test sets should be enough to avoid leakages in case of time series CV.  
I haven’t had the chance to test it yet but I’ll post an update when I have run the tests.
    
    
    import numpy as np
    from sklearn.model_selection._split import _BaseKFold, indexable, _num_samples
    
    
    class PurgedTimeSeriesSplitGroups(_BaseKFold):
        def __init__(self, n_splits=5, purge_groups=0):
            super().__init__(n_splits, shuffle=False, random_state=None)
            self.purge_groups = purge_groups
    
        def split(self, X, y=None, groups=None):
            X, y, groups = indexable(X, y, groups)
            n_samples = _num_samples(X)
            n_folds = self.n_splits + 1
            group_list = np.unique(groups)
            n_groups = len(group_list)
            if n_folds + self.purge_groups > n_groups:
                raise ValueError((f"Cannot have number of folds plus purged groups "
                                  f"={n_folds+self.purge_groups} greater than the "
                                  f"number of groups: {n_groups}."))
            indices = np.arange(n_samples)
            test_size = ((n_groups-self.purge_groups) // n_folds)
            test_starts = [n_groups-test_size*c for c in range(n_folds-1, 0, -1)]
            for test_start in test_starts:
                yield (indices[groups.isin(group_list[:test_start-self.purge_groups])],
                       indices[groups.isin(group_list[test_start:test_start + test_size])])

---

### Post #25 — **profricecake** | 2021-09-28 15:38 UTC

Hi [@mdo](</u/mdo>) and others -

This is a cool way to ensure that eras/groups aren’t split across the train/test border, but I don’t see it say anywhere in the `cross_val_score()` docs that group info is taken into account for scoring. If it’s not, then that means the scorer is doing a spearman on the whole test set instead of averaging it over the eras. Seeing as we score on single eras in the tourney, then to get a more tournament-accurate score from `cross_val_score()` we need it to return the mean spearman over the various testing eras. Does anyone know how to accomplish this with sklearn’s routines?

Thanks

---

### Post #26 — **neosbrother** | 2021-10-08 16:08 UTC

Even after removing eras on the border, I’m receiving significantly better results on all subsequent folds (0.05ish) vs the base fold where train=train and validation=validation (0.025ish). Is this a sign of a bug in my code, or is there something about the training vs validation set that makes the training data easier to predict in general?

---

### Post #27 — **sneaky** | 2021-10-09 10:12 UTC _(reply to #26)_

I would guess, the training and validation data are selected based on their properties. For example the validation data seems to be harder than real data. Atleast in the old dataset it is the case.

---

### Post #28 — **neosbrother** | 2021-11-05 14:05 UTC

For those using both neutralization and cross-validation, do you apply neutralization to the predictions of each of your folds, or only at the end after averaging the fold predictions? I think it works out to the same in the end, but this does impact the cross validation score that we use to tune hyperparameters and I don’t have a strong intuition on whether this would be desirable or not.
