---
title: "Model Diagnostics: Feature Exposure"
category: Data Science
url: https://forum.numer.ai/t/model-diagnostics-feature-exposure/899
created_at: 2020-09-03T13:46:43.125000+00:00
last_posted_at: 2023-09-16T03:45:06.536000+00:00
posts_count: 44
views: 32198
tags: []
---

# Model Diagnostics: Feature Exposure

---

### Post #1 — **jrb** | 2020-09-03 13:46 UTC

This post is about feature exposure. I’ll try explain the intuition behind feature exposure, and why it matters. I’ll also discuss ways to reduce feature exposure (regularization and feature neutralization).

#### Feature Exposure

The idea behind feature exposure is as follows: Any supervised ML model from a very high level perspective, is a function that takes an input feature vector (X) and outputs a prediction (y). At training time, the model learns a mapping between input features and the predictions. With the numerai data, the underlying process is non stationary. i.e features that have great predictive power in one era might not have any predictive power, or perhaps might even hurt the model’s performance in another era. A model that attributes too much importance to a small set of features might do well in the short run, but is unlikely to perform well in the long run. Feature exposure (more specifically, max feature exposure) is a measure of how well balanced a model’s exposure is to the features. Models with lower feature exposures tend to have more consistent performance over the long run.

For a real life example of this, I refer you to the massive burn in r223 on my [primary account](<https://numer.ai/jrb>). The model that I’d used for that round was performing rather well on live data under [another one of my accounts](<https://numer.ai/rbj>), before I decided to flip it over to my primary account. In hindsight that model was “overfit” on a limited set of features and when the regime changed, it began burning heavily. To conclude the anecdote, I switched back to a more conservative model from the next round onwards and everything was fine (at least for the next round). Bear in mind that it’s possible to train models with extremely low max feature exposure, which aren’t very useful in practice. There’s a trade off between feature exposure and correlation. Models with very low max feature exposure also tend to have low correlation. On the other hand, models with high max feature exposure will likely have higher corr, but are also more likely to burn in the long run.

The feature exposure metric has changed a bit since I last [posted](<http://forum.numer.ai/t/more-metrics-for-ya/636/19>) an implementation of it. We’ve gone from using [Pearson correlation coefficient](<https://en.wikipedia.org/wiki/Pearson_correlation_coefficient>) to using [Spearman’s rank correlation coefficient](<https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient>) (which is the same metric used for `CORR`). And instead of aggregating individual feature exposures with standard deviation, we’re now using [root mean square](<https://en.wikipedia.org/wiki/Root_mean_square>) as the aggregation function. Let’s start with a code snippet in Python to calculate maximum feature exposure, the new way. I know there are a lot of people here, who use R. I’d appreciate it if anyone proficient in R could post an R version of the snippet below in this thread.
    
    
    import numpy as np
    from scipy.stats import spearmanr
    
    TOURNAMENT_NAME = "kazutsugi"
    PREDICTION_NAME = f"prediction_{TOURNAMENT_NAME}"
    
    
    def feature_exposures(df):
        feature_names = [f for f in df.columns
                         if f.startswith("feature")]
        exposures = []
        for f in feature_names:
            fe = spearmanr(df[PREDICTION_NAME], df[f])[0]
            exposures.append(fe)
        return np.array(exposures)
    
    
    def max_feature_exposure(df):
        return np.max(np.abs(feature_exposures(df)))
    
    
    def feature_exposure(df):
        return np.sqrt(np.mean(np.square(feature_exposures(df))))
    

Given the aformentioned changes in the feature exposure metrics, all previous heuristics we had about good feature exposures are no longer valid. The example model has a validation max feature exposure of `0.2905`. That’s a reasonable benchmark to strive for, IMO. Although, it’s not difficult to do better than that (as we shall see in the section on feature neutralization below). ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15)

Now let’s look at two models which have very similar in sample (training) sharpe, but slightly different training max feature exposures. _NeuralNet8_ and _NeuralNet19_ are two NN models with very similar in-sample (training) correlations (0.0407) and sharpe (1.09). But, they have slightly different in-sample max feature exposures (`0.257` for _NeuralNet8_ and `0.325` for _NeuralNet19_ , respectively). Let’s see how this difference affects their out of sample (validation) scores.

[![NeuralNet8](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/b362371efd843be6c55d65b915b13f61b28775a5_2_690x274.png)NeuralNet81004×400 22.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/b362371efd843be6c55d65b915b13f61b28775a5.png> "NeuralNet8")

[![NeuralNet19](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/126cb1c1fe05c7e8a2e24d40bcdd4abed8aa29dc_2_690x273.png)NeuralNet191005×399 22.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/126cb1c1fe05c7e8a2e24d40bcdd4abed8aa29dc.png> "NeuralNet19")

The model with the lower in-sample max feature exposure (_NeuralNet8_) seems to do better on out of sample corr and sharpe. You might also notice that the worse model (_NeuralNet19_) paradoxically seems to have lower out of sample max feature exposure. It’s always a good idea to look at both in-sample and out of sample max feature exposures while evaluating models.

This inverse correlation between max feature exposure and out of sample performance seems to generally hold true for all kinds of models. To illustrate the point, here are two regression plots comparing out of sample (validation) and in-sample (training) max feature exposures with out of sample sharpe. This is drawn from 80 different Gradient Boosted Tree and Neural Network models (provided by the Numerai team). There’s also a linear model and the [example model](<https://github.com/numerai/example-scripts/blob/master/example_model.py>) thrown into the mix. The highest point (i.e the best performing model) in both plots unsurprisingly is the example model.

[![FeatureExposureRegressionPlots](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/078dbf2cf344b62e05caf55e16816cfb91c8fa91_2_690x228.png)FeatureExposureRegressionPlots1006×333 24 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/078dbf2cf344b62e05caf55e16816cfb91c8fa91.png> "FeatureExposureRegressionPlots")

#### Reducing Feature Exposure with Regularization

Let’s try training the [example model](<https://github.com/numerai/example-scripts/blob/master/example_model.py>) with [L1 regularization](<https://en.wikipedia.org/wiki/Lasso_\(statistics\)>) and see if it has any effect on the model’s feature exposure. If you’re following along at home, you’ll need to edit the line where `XGBRegressor` instance is created to add an extra parameter `alpha`. I’m setting it to `0.1`.

The specific line to change will go from this:
    
    
    model = XGBRegressor(max_depth=5, learning_rate=0.01, n_estimators=2000, n_jobs=-1, colsample_bytree=0.1)
    

To this:
    
    
    model = XGBRegressor(max_depth=5, learning_rate=0.01, n_estimators=2000, n_jobs=-1, colsample_bytree=0.1, alpha=0.1)
    

Let’s look at the validation results for the example model trained without the extra parameter.

[![ExampleModel](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/896147d2a7f1ef5d9fa911f25413585e9091512d_2_690x280.png)ExampleModel1007×409 22.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/896147d2a7f1ef5d9fa911f25413585e9091512d.png> "ExampleModel")

And now for the model trained with L1 regularization.

[![ExampleModelL1](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/b60ac8d2f144e02c13f010023103d74ccbf9e3cb_2_690x282.png)ExampleModelL11006×412 23.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/b60ac8d2f144e02c13f010023103d74ccbf9e3cb.png> "ExampleModelL1")

As you can see, the model is mostly the same, the validation correlation is down by a bit and so is the validation sharpe, but the max feature exposure is also slightly lower. I haven’t tried to search for the optimal value of the hyperparameter `alpha` here. Searching for it will almost certainly lead to better results.  
Also, there are many more regularization [parameters](<https://xgboost.readthedocs.io/en/latest/parameter.html#parameters-for-tree-booster>) that are worth exploring for XGBoost alone. And if you’re traing NNs, there’s a plethora of regularization parameters worth exploring.

#### Feature Neutralization

[![Numerai_Client](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e1d39e8f38ae51c1189ee85fd9578a2a555a3c06.jpeg)Numerai_Client646×431 60.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e1d39e8f38ae51c1189ee85fd9578a2a555a3c06.jpeg> "Numerai_Client")

Yet another, stronger way to reduce feature exposures is to use feature neutralization.  
Here’s a slightly simplified version of the neutralization code from the official [analysis and tips](<https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb>) notebook.
    
    
    def neutralize(df, target="prediction_kazutsugi", by=None, proportion=1.0):
        if by is None:
            by = [x for x in df.columns if x.startswith('feature')]
    
        scores = df[target]
        exposures = df[by].values
    
        # constant column to make sure the series is completely neutral to exposures
        exposures = np.hstack((exposures, np.array([np.mean(scores)] * len(exposures)).reshape(-1, 1)))
    
        scores -= proportion * (exposures @ (np.linalg.pinv(exposures) @ scores.values))
        return scores / scores.std()
    

There’s quite a lot going on in the little snippet of code. Let me try to explain the important bits. The function takes a pandas _DataFrame_ with features and predictions and returns a pandas _Series_ with neutralized predictions.

  * On line 9, we’re taking matrix with the features from the DataFrame and concatenating another column to it, which has a constant value (the mean of the prediction column). This is to remove bias from the linear model on the next line.
  * On line 11, we’re computing the [pseudo-inverse](<https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse>) of the feature matrix from the previous line and multiplying this pseudo inverse with the predictions. This returns the coefficients for an [OLS model](<https://en.wikipedia.org/wiki/Ordinary_least_squares>) fitted on the features.
  * On the same line, we then multiply the features with the coefficients, which returns the predictions of the linear model we just fitted.
  * We then multiply these linear predictions with a constant `proportion` (between `0` and `1`) and subtract them from the original predictions.
  * Subtracting the linear predictions (of the original predictions) from the original predictions results in predictions that are less linear (fully non-linear if the proportion is set to `1`) with respect to the features.
  * Finally we [divide the output by it’s standard deviation](<https://en.wikipedia.org/wiki/Standard_score>) to rescale it and return it.



If you read this far, you’re probably realized that feature neutralization is somehow related to feature exposures. And you’re right! Neutralizing the predictions with respect to the features reduces both feature exposure and max feature exposure. But they’re not exactly the same ([@mdo](</u/mdo>) has a [great post](<http://forum.numer.ai/t/mmc2-announcement/93/6>) explaining the difference). Let’s take the validation predictions from our old trusted example model and apply feature neutralization to it and see what happens. Sidenote: You might want to open this post in a second browser window and scroll one of them to the graphs from the unmodified example model above, to compare and contrast.

[![ExampleModelNeutralized](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/e604eeed6ae7e236b183209c2b80a81525d6eab4_2_690x282.png)ExampleModelNeutralized1000×410 24.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e604eeed6ae7e236b183209c2b80a81525d6eab4.png> "ExampleModelNeutralized")

As you can see, feature exposure and max feature values have dropped dramatically (`fe` from `0.0850` to `0.0061` and `max fe` from `0.2955` to `0.0153`). The validation correlation has dropped a bit (from `0.0291` to `0.0255`) but the validation sharpe has gone up (from `0.9608` to `1.2436`). The two burn eras `era205` and `era206` in the un-neutralized model have flipped and now have reasonable correlations. In the light of the improved sharpe ratio, it’s safe to conclude that neutralizing the predictions has made the model more consistent over the eras. Perhaps it’s also worthwhile trying to fine tune the proportion parameter. Another thing worth experimenting with is neutralizing predictions with respect to a subset of the feature groups instead of all the features. If you’d like to try this with your own models, the code to neutralize predictions is a one liner.
    
    
    df["prediction_kazutsugi"] = neutralize(df)
    

Now, what would happen if we feature neutralize a linear model? Intuitively, subtracting linear predictions from a linear model should lead to a very bad model. Let’s try doing that and see what happens.

Firstly, we need to train a linear model. And the easiest way to do that IMO, would be to swap out the default tree based booster in the example model with a [linear booster](<https://xgboost.readthedocs.io/en/latest/parameter.html#parameters-for-linear-booster-booster-gblinear>). It’s a really tiny change to the example model.
    
    
    model = XGBRegressor(max_depth=5, learning_rate=0.01, n_estimators=2000, n_jobs=-1, colsample_bytree=0.1, booster="gblinear")
    

[![LinearExampleModel](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/970667f2ec845da3a9fddc54bbeb92cd09a14dbe_2_690x282.png)LinearExampleModel1000×410 23.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/970667f2ec845da3a9fddc54bbeb92cd09a14dbe.png> "LinearExampleModel")

Unsurprisingly, the linear model is worse than the example model in every possible way. It’s performing a bit better than I’d expected it to on `val1` and much worse on `val2`. But, can we make it worse?

Sure we can!

[![NeutralizedLinearExampleModel](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/66a54c7be6dd0a12834fb8909af7be3f415aa9a8_2_690x282.png)NeutralizedLinearExampleModel1000×410 26.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/66a54c7be6dd0a12834fb8909af7be3f415aa9a8.png> "NeutralizedLinearExampleModel")

Now that’s what I’d call a truly bad model. I’ve got two takeaways from this little experiment.

  1. Linear models are mediocre performers on average, but do surprisingly well on some eras.
  2. Neutralizing linear models makes them worse.



Feature exposure and feature neutralization are fairly complex topics which I don’t fully understand, yet. Writing this post has certainly clarified these concepts to a great degree in my mind. I’m quite certain that I’ve left out some important aspects of both in this post, please feel free to post any questions you have on this thread and I’ll try to answer them. And if I cannot, I’m sure someone from the team will. The feature neutralization meme was stolen from [@Budbot](</u/budbot>)’s [post](<https://community.numer.ai/channel/memes?msg=r4pFJYhk2DBeTrRYj>) on [#memes](<https://community.numer.ai/channel/memes/>). Finally, I’d like to thank [@master_key](</u/master_key>) for all the ideas, encouragement and feedback while I was drafting this post. All errors remain mine.

Also, the code for drawing the (not so) pretty bar charts with validation corr and feature exposure is up on [this gist](<https://gist.github.com/jeethu/9039f5bdaa69692cff5cab839c048d67>).

---

### Post #2 — **budbot** | 2020-09-03 23:55 UTC

Great post. Happy to have my meme stolen ![:smile:](http://forum.numer.ai/images/emoji/twitter/smile.png?v=9). Never thought of neutralising to select features ![:thinking:](http://forum.numer.ai/images/emoji/twitter/thinking.png?v=9)

---

### Post #3 — **jrb** | 2020-09-04 12:57 UTC _(reply to #2)_

Perhaps it’s worth looking into neutralizing against only the top-k highest exposed features. ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #4 — **jeremy_berros** | 2020-09-07 18:21 UTC

Great post [@jrb](</u/jrb>). I tried your neutralization function in one of my codes and I got less exposure and SR boost on Val. However when trying to neutralize test set I run into memory issue. Any idea how to prevent that?

---

### Post #5 — **jrb** | 2020-09-07 20:58 UTC _(reply to #4)_

I’m glad you liked it, [@jeremy_berros](</u/jeremy_berros>). Inverting large matrices is very expensive (both, in terms of CPU and memory). And if you’re doing this for the whole tournament data, it’s going to be an extremely large matrix with ~1.6 million rows x 311 columns (310 features + the mean column).

Unfortunately, there’s no easy way to get around it. The bottleneck is the call to `numpy.linalg.pinv`. There’s `scipy.linalg.pinv` which is a drop-in replacement for the numpy function that uses a linear least squares based solver, but that’ll be even more memory hungry. There’s also `scipy.linalg.pinv2` which has similar performance characteristics to `numpy.linalg.pinv` (Both use SVD to compute the pseudo-inverse) but the performance difference between these two functions is negligible to non-existent.

I’d recommend using the python [`del`](<https://docs.python.org/3/reference/simple_stmts.html#grammar-token-del-stmt>) statement to delete as many unused data structures from your program memory as possible to free up memory before calling the `neutralize()` function. It might also be worth calling [`gc.collect()`](<https://docs.python.org/3/library/gc.html#gc.collect>) to reclaim whatever little memory it can.

Another option would be to compute the coefficients on a smaller set (perhaps the validation set as you’ve already mentioned) and then using those coefficients on the larger set. But that **wouldn’t be the same as feature neutralizing against the whole dataset**. If you’d like to try this out, you’ll need to compute the `(np.linalg.pinv(exposures) @ scores.values)` part from the snippet on the smaller set and then keep the 311 dimensional vector that it returns (the coefficients) and use them to neutralize the bigger set. Let me know if any of these options work for you.

---

### Post #6 — **jeremy_berros** | 2020-09-08 01:19 UTC _(reply to #5)_

Thanks [@jrb](</u/jrb>) for your quick reply. I already tried del / gc.collect() but my 16GB RAM is crashing anyway. I did some feature selection based on min correlation which gives me feature exposure on val set around 0.06. Neutralizing with proportion of 0.5 brings val feat_exp down to ~0.02 and boosted val SR ~1.7. I am going to try chunking the test set and see what happens. I will keep you posted. Thanks again.

---

### Post #7 — **jrb** | 2020-09-08 08:33 UTC _(reply to #6)_

I tried memory profiling a quick and dirty script to neutralize the example predictions on my laptop with Python 3.7. The laptop is running OSX Catalina and has 64 GB of RAM. My intuition about memory usage seems to have been roughly correct. With `numpy.linalg.pinv` the memory usage peaks at `19886 MB`, with `scipy.linalg.pinv2` it peaks at `19882.8 MB`, and with `scipy.linalg.pinv`, I had to manually kill the script after its RSS grew beyond 60 GiB.

Since the difference between the amount of physical memory you have and the peak observed memory usage isn’t too big, I’d recommend checking if you have swap enabled and adding a 8 GiB swap file, if you don’t have it already. This is very easy if you’re on Linux with `mkswap`, `swapon` and `swapoff`. IIRC, you should also be able to do this on Windows, where swap is called a `page file`.

---

### Post #8 — **voidcentury** | 2020-09-10 05:13 UTC

I think it also makes sense to do neutralization separately for each era as the feature correlations keep changing across eras. This way there would also be no memory issues.

---

### Post #9 — **wigglemuse** | 2020-09-10 13:15 UTC _(reply to #8)_

Yes, it doesn’t really make sense to me to neutralize EXCEPT on an era-by-era basis, which shouldn’t be a problem computationally.

---

### Post #10 — **jeremy_berros** | 2020-09-17 06:22 UTC

Thanks [@jrb](</u/jrb>) [@voidcentury](</u/voidcentury>) [@wigglemuse](</u/wigglemuse>). Era by era neutralization makes sense and I confirm that memory is not an issue anymore using a function greatly inspired by [analysis_and_tips.ipynb](<https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb>)
    
    
    def full_neutralization(df, feature_names, pred_name="prediction_kazutsugi"):
        df[pred_name] = df.groupby("era").apply(lambda x: normalize_and_neutralize(x, [pred_name], feature_names))
        scaled_preds = MinMaxScaler().fit_transform(df[[pred_name]])
        return scaled_preds
    

Now I need to spend some more time upstream on my feature engineering / selection ![:thinking:](http://forum.numer.ai/images/emoji/twitter/thinking.png?v=9)

---

### Post #11 — **wigglemuse** | 2020-09-20 23:46 UTC

Here’s that neutralization code for R:

> 
>     neutralize <- function(scores_v,exposures_m,proportion=1.0) {
>       scores_v <- scores_v - (proportion * (exposures_m %*% (MASS::ginv(exposures_m) %*% scores_v)))
>       return( scores_v/sd(scores_v) )
>     }
>     
>     normalize_vector <- function(v) {
>       qnorm( (rank(v)-0.5) / length(v) )
>     }
>     
>     normalize_matrix <- function(m) {
>       qnorm( (Rfast::colRanks(m)-0.5) / nrow(m) )
>     }
>     
>     normalize_and_neutralize <- function(scores_v,exposures_m,proportion=1.0) {
>       scores_v <- normalize_vector(scores_v)
>       exposures_m <- normalize_matrix(exposures_m)
>       return( neutralize(scores_v,exposures_m,proportion) )
>     }
>     

You’ll need “Rfast” package for colRanks function (note that there are other packages with same-named function). “MASS” should be included in any standard R installation. As I discussed with [@jrb](</u/jrb>), I recommend you call “normalize_and_neutralize” rather than just “neutralize” – your results will be different (unless your data is already normalized in the same way) and probably better. The function is expecting a numeric vector for scores and a matrix (not a data.frame) for the exposures. This has some slight differences from the python version given in the tips notebook – namely the ranking functions are using the “average” method instead of the “first” method for breaking ties which makes more sense to me for this application (as “first” essentially introduces randomness which might help, but might hurt – both functions have a parameter to can set to “first” if you want though). [Also, don’t have ties in your predictions.] And I don’t think the python version actually normalizes the exposures, only the scores. Which is fine if the exposures matrix is the raw data or is otherwise standardized/normalized, but sometimes I am neutralizing with respect to other types of transformations of the data and it is just safer.

---

### Post #12 — **mdo** | 2020-09-21 02:53 UTC

Here is a slightly different take on feature neutralization. Instead of finding a linear model of your predictions and subtracting a proportion of it off, we could instead find a linear model that when subtracted off reduces your feature exposure below a certain target. We could set a target and define a loss function such that when minimized all exposures will be less than or equal to the minimum of current exposure and the maximum desired exposure. So if some features have an exposure of 0.05, and you set a max exposure of 0.10, the features with the exposure of 0.05 won’t necessarily decrease as they would in the current neutralization code. This allows you to keep some of the smaller exposures that might be important, while reducing your largest risks. Test it out and let me know what you think! Be warned, it’s not especially fast…
    
    
    import torch
    from torch.nn import Linear
    from torch.nn import Sequential
    from torch.functional import F
    
    def exposures(x, y):
        x = x - x.mean(dim=0)
        x = x / x.norm(dim=0)
        y = y - y.mean(dim=0)
        y = y / y.norm(dim=0)
        return torch.matmul(x.T, y)
    
    def reduce_exposure(prediction, features, max_exp):
        # linear model of features that will be used to partially neutralize predictions
        lin = Linear(features.shape[1],  1, bias=False)
        lin.weight.data.fill_(0.)
        model = Sequential(lin)
        optimizer = torch.optim.Adamax(model.parameters(), lr=1e-4)
        feats = torch.tensor(np.float32(features)-.5)
        pred = torch.tensor(np.float32(prediction))
        start_exp = exposures(feats, pred[:,None])
        # set target exposure for each feature to be <= current exposure
        # if current exposure is less than max_exp, or <= max_exp if  
        # current exposure is > max_exp
        targ_exp = torch.clamp(start_exp, -max_exp, max_exp)
    
        for i in range(100000):
            optimizer.zero_grad()
            # calculate feature exposures of current linear neutralization
            exps = exposures(feats, pred[:,None]-model(feats))
            # loss is positive when any exposures exceed their target
            loss = (F.relu(F.relu(exps)-F.relu(targ_exp)) + F.relu(F.relu(-exps)-F.relu(-targ_exp))).sum()
            print(f'       loss: {loss:0.7f}', end='\r')
            if loss < 1e-7:
                neutralizer = [p.detach().numpy() for p in model.parameters()]
                neutralized_pred = pred[:,None]-model(feats)
                break
            loss.backward()
            optimizer.step()
        return neutralized_pred, neutralizer
    
    def reduce_all_exposures(df, column, neutralizers=[],
                                         normalize=True,
                                         gaussianize=True,
                                         era_col="era",
                                         max_exp=0.1):
        unique_eras = df[era_col].unique()
        computed = []
        for u in unique_eras:
            print(u, '\r')
            df_era = df[df[era_col] == u]
            scores = df_era[column].values
            exposure_values = df_era[neutralizers].values
            
            if normalize:
                scores2 = []
                for x in scores.T:
                    x = (scipy.stats.rankdata(x, method='ordinal') - .5) / len(x)
                    if gaussianize:
                        x = scipy.stats.norm.ppf(x)
                    scores2.append(x)
                scores = np.array(scores2)[0]
    
            scores, neut = reduce_exposure(scores, exposure_values, max_exp)
    
            scores /= scores.std()
    
            computed.append(scores.detach().numpy())
    
        return pd.DataFrame(np.concatenate(computed), columns=column, index=df.index)
    
    
    TOURNAMENT_NAME = "kazutsugi"
    PREDICTION_NAME = f"prediction_{TOURNAMENT_NAME}"
    
    ## Get output of your model
    # data[PREDICTION_NAME] = model.predict(data[feature_names])
    
    # reduce feature exposure in each era to max_exp
    data_rfe_10 = reduce_all_exposures(data,
                                       [PREDICTION_NAME],
                                       neutralizers=feature_names,
                                       era_col="era",
                                       max_exp=0.10)
    
    # replace prediction with reduced feature exposure prediction and rescale to [0,1]
    data[PREDICTION_NAME] = data_rfe_10[PREDICTION_NAME]
    data[PREDICTION_NAME] -= data[PREDICTION_NAME].min()
    data[PREDICTION_NAME] /= data[PREDICTION_NAME].max()

---

### Post #13 — **objectscience** | 2020-09-21 07:40 UTC _(reply to #12)_

Might not be a bad idea to have that officially replace the current code in the analysis and tips notebook.

---

### Post #14 — **wigglemuse** | 2020-09-21 12:19 UTC _(reply to #13)_

Have both. The former is more general and way faster. And you can do quick total neutralization as a point of comparison.

---

### Post #15 — **jrb** | 2020-10-10 14:03 UTC

Here’s a command line [feature neutralization script](<https://gist.github.com/jeethu/a586ab44a9b57af2ddf874d8c942e9a0>) that I [posted](<https://community.numer.ai/channel/datascience?msg=4tiGnv7jr8cTy8jJg>) on RocketChat. Since it’s a standalone script, it should work regardless of whether you’re using Python to build your models or something else. It takes the tournament data and predictions files as the inputs and outputs a neutralized csv file.

Example usage:
    
    
    # Fully neutralize predictions in example_predictions_target_kazutsugi.csv.xz wrt features in numerai_tournament_data.csv.xz
    python neutralize.py numerai_tournament_data.csv.xz example_predictions_target_kazutsugi.csv.xz
    

Another example:
    
    
    # Neutralize the top 10 highest exposed features by 50%
    python neutralize.py -t 10 -p 0.5 numerai_tournament_data.csv.xz example_predictions_target_kazutsugi.csv.xz

---

### Post #16 — **oxioxi** | 2020-12-13 11:51 UTC _(reply to #12)_

Any way possible to keep my Colab from crashing while doing this?

---

### Post #18 — **surajp** | 2020-12-15 17:10 UTC _(reply to #16)_

You can restart your runtime and then load saved predictions as float32. This will work under 10GB of colab memory.

---

### Post #20 — **wigglemuse** | 2021-01-08 15:57 UTC

It was pointed out to me that the R neutralization code I posted earlier in this thread ([Model Diagnostics: Feature Exposure](<http://forum.numer.ai/t/model-diagnostics-feature-exposure/899/11>)) doesn’t end up with values between [0,1]. That’s true – I left off that step at the end. So that’s normal, and you will need to do a minmax type rescaling to get the values into the proper ranger for submission. (The actual values you end up with in that range aren’t important as long as they remain in the same order.)

---

### Post #21 — **senadorancap** | 2021-01-09 14:42 UTC _(reply to #20)_

Here is my minmax scaler function for those interested:
    
    
    minmax <- function(x){(x-min(x))/(max(x)-min(x))}

---

### Post #22 — **kreator** | 2021-01-22 20:37 UTC _(reply to #11)_

I try to fully understand the approach. I understand that we don’t want a bias term, but it is a bit unfamiliar for me to transform the data to a standard normal. Why do we need this?

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> `(Rfast::colRanks(m)-0.5) / nrow(m)`

With this line of code you first transform the input data (in our appliction the features) to a uniform distribution. Then you apply the standard normal quantile and get realizations from a standard normal. As you say, this is not always needed. What you want to have is just zero expectation (thus no bias), right? With the -0,5 you avoid the borders of the [0,1] interval, correct?

In `normalize_vector` you basically do the same.

With `exposures_m %*% (MASS::ginv(exposures_m)` you calculate the \beta of the linear model: scores = \beta * features.

Then finally you calculate score_{neutral} = scores - proportion * \beta* features and rescale score_{neutral}.

Is this understanding correct?

---

### Post #23 — **wigglemuse** | 2021-01-22 21:17 UTC _(reply to #22)_

First of all, let me just say for the R code in particular that I was just translating the python code given by the team, so at first I was exactly replicating in R what they did in python so I could compare results of each version side-by-side to make sure I got it right. (This should have been trivial for a function of a few lines, but I don’t actually code in python so I had to do it one detail at a time. When I did it I didn’t quite understand the function myself because of mathematical deficiencies of my own – I didn’t even understand that the pseudo-inverse calculation was making an OLS model.) Anyway, I was just trying to get an exact translation at first, but then in the end I didn’t exactly replicate it as I noted – my version applies normalization on the “exposures” (features) as well as the scores (predictions) whereas theirs doesn’t, and I left out the min-max scaling at the end to get it back into the [0,1] range. (I do that part later in my own workflow.) So the reason I used qnorm and subtracted 0.5 from the ranks (to avoid 0 & 1 as you noted) is simply because that matches what they did in python and I’m not sure that is an important detail for this. (They use that same type of rank normalization in the scoring function so were probably just borrowing their own code.) If we just ranked and rescaled to [0,1] I bet results would be pretty much the same (but not identical). I probably tried that, can’t remember.

Also with the lack of the bias term – if you add one I don’t think it hurts, but results will be basically the same. (I definitely tested that.) And I don’t see why it is necessary to divide the result by the standard deviation (since that doesn’t change any rankings), but again that’s in the python version so there it is.

---

### Post #24 — **kreator** | 2021-01-22 21:49 UTC _(reply to #23)_

Thank you for your transparent comments and the efforts with the code!!

---

### Post #25 — **senadorancap** | 2021-01-24 10:35 UTC _(reply to #23)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> I didn’t even understand that the pseudo-inverse calculation was making an OLS model

That’s the matricial format of OLS algorithm without an intercept and how do i know that? Well let me say that is about the advantages of not taking a nap during the econometric classes ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=12)

I think i have one for Ridge:
    
    
      ridge_neutralize <- function(scores_v,exposures_m,proportion=1.0,ridge=1.0) {
      scores_v <- scores_v - (proportion * (exposures_m %*%
                                            (MASS::ginv((t(exposures_m) %*% exposures_m) +
                                            ridge*length(scores_v)*(diag(ncol(exposures_m)))) %*%
                                            (t(exposures_m) %*% scores_v))))
      return( scores_v/sd(scores_v) )
    }

---

### Post #29 — **lollocodes** | 2021-02-08 09:50 UTC

guys im having issues with the ram , how can i run the code ?

---

### Post #30 — **ieortools** | 2021-02-15 15:31 UTC _(reply to #29)_

[@lollocodes](</u/lollocodes>) depends on you system and language of choice. I use R and I’ve found that you need a decent memory size to perform this analysis. My machine has 16GB RAM. I would imagine this is simiar to using Python.

With using R I’ve also found using h2o.ai works rather well. h2o.ai allows to run in parallel and multiple clusters.

---

### Post #31 — **acassoni** | 2021-03-19 16:08 UTC

Hello! I am new to the competition…

Can someone explain to me the difference between applying feature neutralization to the features on the target, to get a set of features that contain as much original information as possible but decorrelate with the target VS neutralizing predictions by features?

Thanks.

---

### Post #32 — **gbrecht** | 2021-03-22 08:42 UTC

The difference is if you are trying to get the linear element out of your training/prediction result (neutralizing your predictions) or if you are trying the get the linear element out of your training data because you hope your model then is not focussing on that linear element at all (neutralizing the features to the target before training)

---

### Post #33 — **chelnak** | 2021-03-25 20:38 UTC _(reply to #12)_

Hey [@mdo](</u/mdo>) \- starting to think about using this but combining it with the idea of caching with joblib (as per the tensorflow example by [@jrb](</u/jrb>)). Before I go pen to paper - was wondering if you could advise on which metric i’d need to store alongside the era? I think the tensorflow example stores era and weights.

Cheers!

---

### Post #34 — **ml_is_lyf** | 2021-04-02 10:43 UTC _(reply to #12)_

Can anyone explain to me what the reasoning is for `pred[:,None]-model(feats)` the line below:

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> 
>             exps = exposures(feats, pred[:,None]-model(feats))
>     

If I understand correctly, this is the error between our original models predictions, and the predictions of the feature neutralization model. Why calculate the feature exposure of the error, rather than the feature exposure of the predictions of the feature neutralization model? Does this just ensure we don’t drift too far from the original predictions?

Thanks in advance.

---

### Post #35 — **mdo** | 2021-04-05 21:04 UTC _(reply to #34)_

Neutralization is finding a linear model `model(feats)` to subtract off from your predictions `predictions[:,None]`. That line is measuring how much exposure remains after that subtraction. The linear model is initialized at 0 and then learned until the exposures measured by that line fall below threshold. Make sense?

---

### Post #36 — **ml_is_lyf** | 2021-04-05 22:03 UTC _(reply to #35)_

Ahhhh that makes sense thank you. I missed that you mention in the post the model learns the amount to subtract from the original predictions to neutralize it, I thought it was learning a transformation that was feature neutral. Now I understand that it makes perfect sense. Thanks for the help

---

### Post #39 — **unsentient** | 2022-10-19 21:49 UTC

Does this neutralize function still work? I’ve played with it all day and seems to spit out all manner of numbers, positive, negative, greater than 1. I would have expected it to return an array of transformed predictions between 0 and 1.

Here is a self contained code block that I think shows this function doesn’t work.
    
    
    import numpy as np
    import pandas as pd
    
    def neutralize(df, target="predictions", by=None, proportion=1.0):
        if by is None:
            by = [x for x in df.columns if x.startswith('feature')]
    
        scores = df[target]
        exposures = df[by].values
    
        # constant column to make sure the series is completely neutral to exposures
        exposures = np.hstack((exposures, np.array([np.mean(scores)] * len(exposures)).reshape(-1, 1)))
    
        scores -= proportion * (exposures @ (np.linalg.pinv(exposures) @ scores.values))
        return scores / scores.std()
    
    
    data = {'feature_1': [0.00, 0.25, 0.50, 0.75, 1.00],
            'feature_2': [0.25, 0.75, 0.50, 0.75, 0.75],
            'feature_3': [1.00, 0.75, 0.00, 0.75, 0.75],
            'feature_4': [0.25, 0.50, 0.25, 0.00, 0.50],
            'predictions':  [0.52, 0.66, 0.71, 0.98, 0.33]}
    df = pd.DataFrame(data)
    
    neutralize(df)
    

Output:
    
    
    0   -1.953662
    1   -0.781465
    2   -1.172197
    3   -2.344394
    4    0.195366
    Name: predictions, dtype: float64

---

### Post #40 — **shatteredx** | 2022-10-19 22:08 UTC _(reply to #39)_

An updated neutralize function is located in the example scripts at [example-scripts/utils.py at master · numerai/example-scripts · GitHub](<https://github.com/numerai/example-scripts/blob/master/utils.py>)

---

### Post #41 — **wigglemuse** | 2022-10-20 01:47 UTC

I think that’s correct – it is just subtracting the linear model which is not bounded that would prevent the result from ending up with negative values, etc. You have to rescale it again to get it back to [0,1] if that’s what you want.

---

### Post #42 — **anthill** | 2022-10-20 04:36 UTC _(reply to #39)_

It might be more principled to pass the outputs of the neutralization through a sigmoid function, which will rescale it to [0, 1]. In that case you would effectively be subtracting out a logistic regression model rather than an OLS model.

---

### Post #43 — **unsentient** | 2022-10-20 04:57 UTC _(reply to #40)_

Okay so I tried that neutralize function and now I’m more confused. The neutralize function from the example script returns a DataFrame of transformed features. Is that the data I’m now meant to predict on? Does it not matter that some of it’s out side of the 0 to 1 range? Maybe that’s the point? The data is now scaled so the features are neutralized? I really thought a neutralize function would return transformed predictions.
    
    
    import pandas as pd
    import numpy as np
    import scipy as sp
    
    def neutralize(df,
                   columns,
                   neutralizers=None,
                   proportion=1.0,
                   normalize=True,
                   era_col="era"):
        if neutralizers is None:
            neutralizers = []
        unique_eras = df[era_col].unique()
        computed = []
        for u in unique_eras:
            df_era = df[df[era_col] == u]
            scores = df_era[columns].values
            if normalize:
                scores2 = []
                for x in scores.T:
                    x = (sp.stats.rankdata(x, method='ordinal') - .5) / len(x)
                    x = sp.stats.norm.ppf(x)
                    scores2.append(x)
                scores = np.array(scores2).T
            exposures = df_era[neutralizers].values
    
            scores -= proportion * exposures.dot(
                np.linalg.pinv(exposures.astype(np.float32), rcond=1e-6).dot(scores.astype(np.float32)))
    
            scores /= scores.std(ddof=0)
    
            computed.append(scores)
    
        return pd.DataFrame(np.concatenate(computed),
                            columns=columns,
                            index=df.index)
    
    data = {'era': [1,1,1,1,1],
            'feature_1': [0.00, 0.25, 0.50, 0.75, 1.00],
            'feature_2': [0.25, 0.75, 0.50, 0.75, 0.75],
            'feature_3': [1.00, 0.75, 0.00, 0.75, 0.75],
            'feature_4': [0.25, 0.50, 0.25, 0.00, 0.50],
            'predictions':  [0.52, 0.66, 0.71, 0.98, 0.33]}
    df = pd.DataFrame(data)
    df
    
    columns = [c for c in df.columns if c.startswith("feature")]
    neutralize(df,columns)
    

Output:
    
    
       feature_1  feature_2  feature_3  feature_4
    0  -1.463366  -1.463366   1.463366  -0.598798
    1  -0.598798   0.000000  -0.598798   0.598798
    2   0.000000  -0.598798  -1.463366   0.000000
    3   0.598798   0.598798   0.000000  -1.463366
    4   1.463366   1.463366   0.598798   1.463366

---

### Post #44 — **unsentient** | 2022-10-20 04:58 UTC _(reply to #42)_

Is that better? Or what other users do?

---

### Post #45 — **anthill** | 2022-10-20 15:50 UTC _(reply to #44)_

I’m not sure if it’s what other users do, but you could try it with one of your models to see if it improves things. Unfortunately the only way to make progress in ML is to just try things and see what works for you.

---

### Post #46 — **unsentient** | 2022-10-20 22:43 UTC _(reply to #45)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> subtract off from your predictions `predictions[:,None]`. That line is measuring how much exposure remains after that subtraction. The linear model is initialized at 0 and then learned until the exposures measured by that line fall below threshold. Make sense?

So I got my head around the rescaling. I tried min max scaling vs logistic scaling and there wasn’t really a difference. Although I think I’ve still got a problem with my neutralizer.

---

### Post #47 — **shatteredx** | 2022-10-22 15:25 UTC _(reply to #43)_

You’re getting neutralized features because you’re passing the feature columns to the columns argument. Whatever you pass to the columns argument is what gets neutralized. Pass your prediction column and you will get a neutralized prediction column as your output. You also should be passing names of features that will be used as “neutralizers” to the neutralizers argument.

Your observation that the output is not scaled from 0 to 1 is expected behavior. You will need to scale the output yourself.

Example
    
    
    tournament_data[f"preds_neutral"] = neutralize(
        df=tournament_data,
        columns=[PREDICTION_NAME],
        neutralizers=feature_cols,
        proportion=1.0,
        normalize=True,
        era_col=ERA_COL
    )
    tournament_data[PREDICTION_NAME] = tournament_data[f"preds_neutral"].rank(method='first',pct=True)

---

### Post #48 — **taori** | 2022-10-23 11:19 UTC

[@unsentient](</u/unsentient>) make sure to test your model out of samples when you use feature neutralization, because it doesn’t necessarily improve your performance. In my experience feature neutralization helps correlation of simple models, such as the numerai example script, but it hurts more advanced models. You might not be looking for improving the correlation metrics though, but still make sure to test if feature neutralization helps your model or not in the metrics you are interested in. Do not blindly trust feature neutralization.

---

### Post #49 — **esedx12** | 2023-06-26 16:45 UTC

Thanks for this post, it was an interesting read!

At the end, you mentioned that you tried neutralizing a linear model, which you fitted with OLS.  
I don’t really understand this. I’ll explain:

What a linear model does, when you apply OLS, is project the target of your training samples linearly onto the vector space spanned by your feature vectors, i.e. it finds the linear combination of the feature vectors that best approximates the target.

What the function neutralize does (as far as I can tell) is fit a linear model to the column ‘target’ and then subtract its prediction from this columng (and then normalize).

However, if the column ‘target’ was already obtained from a linear model fit on the same feature vectors, then ‘target’ is already a linear combination of the feature vectors. Thus, subtracting the predictions of the linear model should theoretically result in a zero vector.

…or did I miss something? I’d appreciate any feedback ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #50 — **wigglemuse** | 2023-06-26 17:18 UTC _(reply to #49)_

Neutralize is to the features->predictions, not to the original training target we are predicting. (So we can still do neutralization without the target on live predictions.) So we make a linear model using the features to predict the _predictions_ that our trained model is spitting out, and then subtract that, i.e. we are removing the linear relationships between the features and our predictions. Which is what we call “feature exposure” around here – the correlations between the features and our trained predictions. So fully neutralized set of predictions fully removes the portion of our original predictions that can be generated using a straight linear model (and the result if you do it 100% is predictions with zero correlation to any of the features).

So it still doesn’t make sense to neutralize a purely linear model that uses the original features for essentially the same reason – you’d just be zeroing it out. But the training target (which of course is not available for live eras) is not needed for that step.

---

### Post #51 — **reeboo** | 2023-09-16 03:45 UTC _(reply to #23)_

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/ea871cac08d3c0aebed77334ef1b248d84b79e90_2_690x371.png)image1648×888 74.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/ea871cac08d3c0aebed77334ef1b248d84b79e90.png> "image")
