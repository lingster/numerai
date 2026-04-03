---
title: "More metrics for ya"
category: Data Science
url: https://forum.numer.ai/t/more-metrics-for-ya/636
created_at: 2020-07-08T21:52:47.243000+00:00
last_posted_at: 2021-04-04T19:31:49.168000+00:00
posts_count: 24
views: 7249
tags: []
---

# More metrics for ya

---

### Post #1 — **arbitrage** | 2020-07-08 21:52 UTC

import matplotlib.pyplot as plt
    from sklearn.preprocessing import minmax_scale
    
    def ar1(x):
        return np.corrcoef(x[:-1], x[1:])[0,1]
    
    def autocorr_penalty(x):
        n = len(x)
        p = np.abs(ar1(x))
        return np.sqrt(1 + 2*np.sum([((n - i)/n)*p**i for i in range(1,n)]))
    
    def smart_sharpe(x):
        return (np.mean(x)/(np.std(x, ddof=1) * autocorr_penalty(x)) * np.sqrt(12))
    
    def numerai_sharpe(x):
        return ((np.mean(x) - 0.010415154) / np.std(x)) * np.sqrt(12)
    
    def spearmanr(target, pred):
        return np.corrcoef(
            target,
            pred.rank(pct=True, method="first")
        )[0, 1]
    
    
    era_col = df_val['era']
    new_df = df_val.copy()
    new_df['target'] = new_df['target_kazutsugi']
    new_df['era'] = era_col
    preds = boost_model.predict(df_val[features])
    preds = minmax_scale(preds)
    #new_df['pred'] = new_df['prediction_kazutsugi']
    new_df["pred"] = preds
    era_scores = pd.Series(index=new_df['era'].unique())
    print("getting per era scores")
    for era in new_df['era'].unique():
        era_df = new_df[new_df['era'] == era]
        era_scores[era] = spearmanr(era_df['pred'], era_df['target'])
    era_scores.sort_values(inplace=True)
    era_scores.sort_index(inplace=True)
    era_scores.plot(kind="bar")
    print("performance over time")
    plt.show()
    
    print("Maximum Drawdown (Minimum Score)")
    print(np.min(era_scores))
    print("Average Correlation")
    print(np.mean(era_scores))
    print("Median Correlation")
    print(np.median(era_scores))
    print("Variance")
    print(np.var(era_scores))
    print("Std. Dev.")
    print(np.std(era_scores))
    print("Autocorrelation")
    print(ar1(era_scores))
    print("Sharpe")
    print(np.mean(era_scores)/np.std(era_scores) * np.sqrt(12))
    print("Smart Sharpe")
    print(smart_sharpe(era_scores))
    print("Numerai Sharpe")
    print(numerai_sharpe(era_scores))
    import scipy
    from scipy.stats import skew, kurtosis, sem, gmean
    
    print("Skewness")
    print(skew(era_scores))
    print("Excess Kurtosis")
    print(kurtosis(era_scores))
    print("Standard Error of the Mean")
    print(sem(era_scores))
    
    
    def annual_sharpe(x):
        return ((np.mean(x) -0.010415154) /np.std(x)) * np.sqrt(12)
    
    print("Annualized Sharpe")
    print(annual_sharpe(era_scores))
    def adj_sharpe(x):
        return annual_sharpe(x) * (1 + ((skew(x) / 6) * annual_sharpe(x)) - ((kurtosis(x) - 3) / 24) * (annual_sharpe(x) ** 2))
    print("Adjusted Sharpe")
    print(adj_sharpe(era_scores))
    
    def VaR(x):
        return -np.mean(x) - np.sqrt(np.var(x)) * np.percentile(x, 10)
    print("Value at Risk (VaR) with 10% probability of occurring")
    print(VaR(era_scores))
    def smart_sortino_ratio(x, target=0.010415154):
        xt = x - target
        return np.mean(xt)/(((np.sum(np.minimum(0, xt)**2)/(len(xt)-1))**.5)*autocorr_penalty(x))
    print("Smart Sortino Ratio")
    print(smart_sortino_ratio(era_scores))
    def sortino_ratio(x, target=0.010415154):
        xt = x - target
        return np.mean(xt) / (np.sum(np.minimum(0, xt)**2)/(len(xt)-1))**.5
    print("Sortino Ratio")
    print(sortino_ratio(era_scores))

---

### Post #2 — **richai** | 2020-07-08 22:13 UTC

[@master_key](</u/master_key>) we might want these in the new Numerai metrics

---

### Post #3 — **arbitrage** | 2020-07-08 22:13 UTC

CAVEAT EMPTOR on all these; most are copied directly from Michael Oliver’s era boosting notebook and I added a few more myself.

---

### Post #4 — **blockrocket** | 2020-07-09 12:17 UTC _(reply to #3)_

is his notebook available on github?

---

### Post #5 — **arbitrage** | 2020-07-09 14:34 UTC _(reply to #4)_

yes, in <https://github.com/numerai/example-scripts/blob/master/era_boosting_example.ipynb>

---

### Post #6 — **lackofintelligence** | 2020-07-13 08:30 UTC

An equivalent integral version of [@wigglemuse](</u/wigglemuse>)’s geometric Sharpe ratio:
    
    
     w  = \exp\left\{\log\left[ e^{\int_{-1}^{1}P(C\mid \alpha)\ \log(1+C)\ dC}-1 \right] - \log\left[\int_{-1}^{0} P(C\mid \alpha)\ C \ dC\right] \right\}
    

where I have used instead of the maximum drawdown, the expectation of the drawdown. You can use this if you think you understand the distribution, P, of correlations, C, as a function of the model/distribution parameters, alpha. For clarity here is an image of the equation.

![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/f8d3d3d282d9e1f6b9e48023217dbacbd1c44c51.png)

---

### Post #7 — **wigglemuse** | 2020-07-13 19:38 UTC _(reply to #6)_

code didn’t really work out there

---

### Post #8 — **lackofintelligence** | 2020-07-13 22:09 UTC _(reply to #7)_

I thought we were supposed to be submitting code here. You think latex is too slow? I already submitted a request on support quite a while ago and there were several community members who voted it up. [@slyfox](</u/slyfox>) even suggested an install.

---

### Post #9 — **wigglemuse** | 2020-07-13 22:19 UTC

Sure we should submit code, but as it is now latex is unreadable.

---

### Post #10 — **of_s** | 2020-07-16 15:12 UTC

Related post / paper on left-tail persistence

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/adb4cee0c46f2b20e6c5de64d8c46a8a2ed44a58.png) [Alpha Architect – 14 Jul 20](<https://alphaarchitect.com/left-tail-risk-and-left-tail-momentum/> "11:30AM - 14 July 2020") ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c13c76bf7dd27725bb898307e02a27b55e723ac1_2_500x500.png)

### [Left Tail Risk and Left Tail Momentum](<https://alphaarchitect.com/left-tail-risk-and-left-tail-momentum/>)

The positive trade-off between risk and expected return is the most fundamental concept in financial economics. Most investors are risk-averse. In order to hold

---

### Post #11 — **mdo** | 2020-07-17 08:18 UTC

[@arbitrage](</u/arbitrage>) There is a small mistake in the adj_sharpe function. The version of kurtosis used by default in scipy already has the 3 subtracted, so the formula you have is subtracting that 3 again and will give spurious results.

---

### Post #12 — **player1** | 2020-07-24 02:42 UTC

Thanks for these [@arbitrage](</u/arbitrage>)! You (or anyone) wouldn’t happen to have the python code for calculating feature exposure available? Both the way [@bor1](</u/bor1>) described it ([here](<http://forum.numer.ai/t/model-evaluation-metrics/337/2>)) and max feature exposure that [@richai](</u/richai>) talked about in today’s OHwA?

---

### Post #13 — **themicon** | 2020-07-24 06:24 UTC _(reply to #12)_

[@player1](</u/player1>) I’ve got something that might help, not sure if it’s exactly what they use on the Numerai tournament, but it’s helped me with the feature exposure evaluations. It does require the scipy.stats module.
    
    
    from scipy import stats
    import numpy as np
    
    ...
    
    predictors = train.columns.values.tolist()
    feature_pearson = []
    feature_spearman = []
    for i in range(len(predictors)):
    	feature_pearson.append(stats.pearsonr(preds_valid, valid[predictors[i]])[0])
    	feature_spearman.append(stats.spearmanr(preds_valid, valid[predictors[i]])[0])
    
    print("*******")
    print("Pearson:")
    print("Feat. Max: \t", np.max(feature_pearson))
    print("Feat. Exp: \t", np.std(feature_pearson))
    print("Spearman:")
    print("Feat. Max: \t", np.max(feature_spearman))
    print("Feat. Exp: \t", np.std(feature_spearman))
    

So this is after you’ve got a list of your predictions that you can compare to the real target values in your validation set.

---

### Post #14 — **player1** | 2020-07-24 06:53 UTC _(reply to #13)_

Brilliant, thank you! Here’s what I got with one of my models (IceShark).
    
    
    *******
    Pearson:
    Feat. Max: 	 0.2025210097078443
    Feat. Exp: 	 0.06394568577456082
    Spearman:
    Feat. Max: 	 0.19976677632974976
    Feat. Exp: 	 0.0634932164568535
    

Max feature correlation of 0.2 seems quite high (too high), would you agree?

---

### Post #15 — **themicon** | 2020-07-24 06:57 UTC _(reply to #14)_

I’ve got very similar results for the maximum as that. I’ve not really concentrated on the max value. The mean was more important for me, but since [@richai](</u/richai>) mentioned the max value yesterday I might start looking into it.

---

### Post #16 — **wigglemuse** | 2020-07-24 14:05 UTC

It can be tough to get the max down to less than .15 or so, but as usual depends on what you are doing. To throw a wrinkle into it, a summary stat of feature exposure is useful but not necessarily accurate (AS “exposure”) because it just means your predictions are correlated to some feature over the time period you are measuring (or averaged over eras or whatever). But that does not necessarily mean you are over-relying on that feature (although it might and probably does actually). And if you look at the same stat for a different validation period, you might get a similar max but that doesn’t mean it is the same features that are reaching that max.

You are also trying to be correlated to the real targets after all, and if a feature happens to also be correlated to the targets during that period, then being correlated with such a feature is not a bad thing (for that period). In other words, if that feature stops being correlated to the targets, but your model goes happily along remaining correlated to the targets but not that feature, then that’s a good model and your correlation to that feature wasn’t a main causative factor. So if you really want to dive deep on feature exposure, you’d look at each feature in isolation and compare correlations between predictions and targets vs partial correlation between predictions and targets with the feature as control variable (effect removed in partial correlation) and then you’ll get a better idea what effect it is really having on your model. And you need to do that over different periods where that feature was both more and less correlated with the targets. Then you can see _which_ features are relatively highly correlated with your predictions, and if it is the same features that remain so over time.

---

### Post #17 — **jrb** | 2020-07-27 12:10 UTC _(reply to #16)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> It can be tough to get the max down to less than .15 or so, but as usual depends on what you are doing.

Feature exposure and max feature exposure (computed with pearson’s correlation coefficient on validation data) for example predictions: `0.0796` and `0.1013`. Another data point from one of my [models](<https://numer.ai/ethr>): (fe: `0.0582`, max fe: `0.0793`).

---

### Post #18 — **joakim_arvidsson** | 2020-07-27 16:08 UTC _(reply to #17)_

I got like 0.23 max FE for the example model using the above code. That’s with training on both Train and Val. Would Max FE go up by that much just by including Val in training? Or am I more likely doing it wrong?

---

### Post #19 — **jrb** | 2020-07-27 17:04 UTC _(reply to #18)_

The numbers I got for the example model were computed from the `example_predictions.csv` file that is a part of the weekly data download. Running the python example script also gives similar numbers (albeit slightly different, because of different random seeds) for me. I’d recommed trying to reproduce it without training on val.

I’ve attached a snipped version of the code that I use, abridged to reproduce my results for example predictions, below. Just run it in the directory with the unzipped contents of the weekly zip file and you’ll get the same results for example predictions as what I’d posted above.
    
    
    import csv
    import numpy as np
    import pandas as pd
    
    TOURNAMENT_NAME = "kazutsugi"
    PREDICTION_NAME = f"prediction_{TOURNAMENT_NAME}"
    
    
    def feature_exposure(df):
        df = df[df.data_type == 'validation']
        feature_columns = [x for x in df.columns if x.startswith('feature_')]
        pred = df[PREDICTION_NAME]
        correlations = []
        for col in feature_columns:
            correlations.append(np.corrcoef(pred, df[col])[0, 1])
        return np.std(correlations)
    
    
    def max_feature_exposure(df):
        df = df[df.data_type == 'validation']
        feature_columns = [x for x in df.columns if x.startswith('feature_')]
        fe = {}
        for era in df.era.unique():
            era_df = df[df.era == era]
            pred = era_df[PREDICTION_NAME]
            correlations = []
            for col in feature_columns:
                correlations.append(np.corrcoef(pred, era_df[col])[0, 1])
            fe[era] = np.std(correlations)
        return max(fe.values())
    
    
    def read_csv(file_path):
        with open(file_path, 'r') as f:
            column_names = next(csv.reader(f))
    
        dtypes = {x: np.float16 for x in column_names if
                  x.startswith(('feature', 'target'))}
        df = pd.read_csv(file_path, dtype=dtypes, index_col=0)
    
        return df
    
    
    if __name__ == '__main__':
        tournament_data = read_csv(
            "numerai_tournament_data.csv")
        example_predictions = read_csv(
            "example_predictions_target_kazutsugi.csv")
        merged = pd.merge(tournament_data, example_predictions,
                          left_index=True, right_index=True)
        fe = feature_exposure(merged)
        max_fe = max_feature_exposure(merged)
        print(f"Feature exposure: {fe:.4f} "
              f"Max feature exposure: {max_fe:.4f}")
    

PS: iPad + Blink + mosh + Wireguard VPN + wakeonlan = fun. ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

---

### Post #20 — **joakim_arvidsson** | 2020-07-27 20:17 UTC _(reply to #19)_

Awesome, thanks [@jrb](</u/jrb>), will try this.

---

### Post #21 — **koerrie** | 2020-08-06 16:54 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/arbitrage/48/2538_2.png) arbitrage:

> 0.010415154

Where does this magic number come from?  
Is this the correlation from some basic estimator?

---

### Post #22 — **arbitrage** | 2020-08-07 16:18 UTC _(reply to #21)_

richard said that this number approximated their average trading costs

---

### Post #23 — **jrb** | 2020-08-28 16:49 UTC _(reply to #19)_

I just realized that the `max_feature_exposure` implementation in my previous post is incorrect (it’s computing the max of each era’s feature correlation, instead of the max of each feature’s correlation with the predictions). Here’s the same code block with the correct implementation.
    
    
    import csv
    import numpy as np
    import pandas as pd
    
    TOURNAMENT_NAME = "kazutsugi"
    PREDICTION_NAME = f"prediction_{TOURNAMENT_NAME}"
    
    
    def feature_exposures(df):
        df = df[df.data_type == 'validation']
        feature_columns = [x for x in df.columns if x.startswith('feature_')]
        pred = df[PREDICTION_NAME]
        correlations = []
        for col in feature_columns:
            correlations.append(np.corrcoef(pred, df[col])[0, 1])
        return np.array(correlations)
    
    
    def feature_exposure(df):
        return np.std(feature_exposures(df))
    
    
    def max_feature_exposure(df):
        return np.max(feature_exposures(df))
    
    
    def read_csv(file_path):
        with open(file_path, 'r') as f:
            column_names = next(csv.reader(f))
    
        dtypes = {x: np.float16 for x in column_names if
                  x.startswith(('feature', 'target'))}
        df = pd.read_csv(file_path, dtype=dtypes, index_col=0)
    
        return df
    
    
    if __name__ == '__main__':
        tournament_data = read_csv(
            "numerai_tournament_data.csv")
        example_predictions = read_csv(
            "example_predictions_target_kazutsugi.csv")
        merged = pd.merge(tournament_data, example_predictions,
                          left_index=True, right_index=True)
        fe = feature_exposure(merged)
        max_fe = max_feature_exposure(merged)
        print(f"Feature exposure: {fe:.4f} "
              f"Max feature exposure: {max_fe:.4f}")
    

Update 3rd September, 2020: The feature exposure metrics have **changed slightly** since I posted this. I’m leaving the code in this post intact, as I’d posted it earlier. Please refer to [this post](<http://forum.numer.ai/t/model-diagnostics-feature-exposure/899>) to find out more about the new feature exposure and max feature exposure metrics.

---

### Post #24 — **kecol** | 2021-04-04 19:31 UTC _(reply to #21)_

I am new here and I am trying to understand the whole Numerai project yet, but for me it looks like a possible Risk Free interest rate. At least it makes sense to me. The idea would be to avoid considering profits that can be obtained without risk in the market. For instance, this helps to make your own sharpe ratios comparable over time when the risk free rate change.
