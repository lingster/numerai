---
title: "Does Good Model Diagnostics Correlate with Tournament Performance?"
category: Data Science
url: https://forum.numer.ai/t/does-good-model-diagnostics-correlate-with-tournament-performance/1454
created_at: 2021-01-12T04:52:54.129000+00:00
last_posted_at: 2021-02-07T14:58:44.326000+00:00
posts_count: 14
views: 3050
tags: []
---

# Does Good Model Diagnostics Correlate with Tournament Performance?

---

### Post #1 — **nasdaqjockey** | 2021-01-12 04:52 UTC

Most of us are striving to create models that produce the best scores on the diagnostics, or at least that’s what we tell everyone else. But let’s be honest, we are actually trying to accumulate NMR as fast as we can, and the premise is that by training our models to optimize on the diagnostics we will earn more and burn less. So as any good data scientist would, I searched for models that maximized the diagnostic values, but when I looked at their performance, the models that earned the most were not the ones with the best diagnostics! So, what’s up? Maybe these metrics are good for NumerAI, but no so great for performance. Unfortunately, like everything else we do for NumerAI, my ground truth is limited since I just start feature neutralization in round 241, so I didn’t have a lot of performance data to use but I think the process I used is applicable to everyone.

What I set out to do is determine which diagnostics are correlated with performance and then select models that maximize those features. I also have another metric I use called validation_score, which is related to era consistency across the validation data (val1 and val2). So, in all, I used 10 metrics in my evaluation: validation_sharpe, validation_mean, feature_neutral_mean, validation_sd, feature_exposure, max_drawdown, corr_plus_mmc_sharpe, mmc_mean, corr_with_example_preds, and validation_score.

**Analysis**

The first thing I did was calculate the average performance of all my staked models since I started feature neutralization in round 241:

**rank** | **account** | **average CORR** | **average MMC**  
---|---|---|---  
1 | NASDAQJOCKEY9 | 0.018125 | 0.014125  
2 | NASDAQJOCKEY12 | 0.01545 | 0.0121  
3 | NASDAQJOCKEY3 | 0.011325 | 0.008875  
4 | NASDAQJOCKEY10 | 0.010125 | 0.007925  
5 | NASDAQJOCKEY1 | 0.010025 | 0.007875  
6 | NASDAQJOCKEY11 | 0.007275 | 0.0057  
7 | NASDAQJOCKEY7 | 0.00505 | 0.00405  
8 | NASDAQJOCKEY2 | 0.001875 | 0.00165  
9 | NASDAQJOCKEY5 | -0.00128 | -0.00093  
10 | EVOLVZ | -0.00273 | -0.00208  
11 | NASDAQJOCKEY4 | -0.004 | -0.00293  
12 | NASDAQJOCKEY6 | -0.00765 | -0.00588  
13 | NASDAQJOCKEY8 | -0.00943 | -0.0072  
14 | NASDAQJOCKEY | -0.01178 | -0.00903  
15 | ZBRAIN | -0.01253 | -0.00958  
  
I was originally thinking I would have to do three analyses for CORR, MMC, and CORR+MMC but interestingly enough, the rank order of CORR and MMC are the same (that may not be the case for your models so you may have to repeat the process). Then I calculated the diagnostics for all of the staked models (note that d0…d9 correspond to the diagnostic order above):

**account** | **d0** | **d1** | **d2** | **d3** | **d4** | **d5** | **d6** | **d7** | **d8** | **d9**  
---|---|---|---|---|---|---|---|---|---|---  
nasdaqjockey9 | 0.8768 | 0.0144 | 0.0127 | 0.0165 | 0.0402 | -0.0512 | 0.7368 | 0.0048 | 0.3085 | 20.4617  
nasdaqjockey12 | 1.5596 | 0.0168 | 0.0144 | 0.0108 | 0.0704 | -0.0120 | 1.3251 | 0.0036 | 0.4581 | 23.4258  
nasdaqjockey3 | 1.1774 | 0.0178 | 0.0150 | 0.0152 | 0.0630 | -0.0228 | 0.9790 | 0.0045 | 0.4438 | 22.6567  
nasdaqjockey1 | 0.9120 | 0.0162 | 0.0132 | 0.0178 | 0.0759 | -0.0689 | 0.7737 | 0.0026 | 0.4826 | 22.1604  
nasdaqjockey10 | 0.8047 | 0.0133 | 0.0108 | 0.0165 | 0.0575 | -0.0421 | 0.6416 | 0.0024 | 0.3810 | 21.9129  
nasdaqjockey11 | 1.1819 | 0.0200 | 0.0174 | 0.0169 | 0.0478 | -0.0258 | 1.0604 | 0.0076 | 0.3762 | 23.2207  
nasdaqjockey7 | 1.1313 | 0.0162 | 0.0142 | 0.0143 | 0.0619 | -0.0276 | 0.9313 | 0.0040 | 0.4126 | 22.7170  
nasdaqjockey2 | 0.9466 | 0.0154 | 0.0121 | 0.0163 | 0.0775 | -0.0353 | 0.7469 | 0.0017 | 0.4934 | 20.6683  
nasdaqjockey5 | 0.9405 | 0.0172 | 0.0151 | 0.0183 | 0.0529 | -0.0166 | 0.7627 | 0.0055 | 0.3759 | 19.5737  
evolvz | 1.3164 | 0.0198 | 0.0174 | 0.0150 | 0.0598 | -0.0172 | 1.1646 | 0.0067 | 0.4151 | 23.1187  
nasdaqjockey4 | 0.8864 | 0.0159 | 0.0135 | 0.0179 | 0.0607 | -0.0392 | 0.6765 | 0.0033 | 0.4338 | 21.4005  
nasdaqjockey6 | 0.8969 | 0.0142 | 0.0116 | 0.0159 | 0.0610 | -0.0330 | 0.7054 | 0.0019 | 0.4408 | 20.0621  
nasdaqjockey8 | 0.8548 | 0.0145 | 0.0121 | 0.0170 | 0.0545 | -0.0253 | 0.6166 | 0.0030 | 0.3928 | 21.0211  
nasdaqjockey | 1.1794 | 0.0158 | 0.0133 | 0.0134 | 0.0638 | -0.0094 | 0.8615 | 0.0036 | 0.4160 | 21.5069  
zbrain | 0.9751 | 0.0149 | 0.0130 | 0.0152 | 0.0625 | -0.0409 | 0.7851 | 0.0035 | 0.3856 | 19.7781  
  
Then I find the rank order of each model for each diagnostic:

**account** | **d0** | **d1** | **d2** | **d3** | **d4** | **d5** | **d6** | **d7** | **d8** | **d9** | **d0**  
---|---|---|---|---|---|---|---|---|---|---|---  
nasdaqjockey9 | 13 | 13 | 11 | 9 | 1 | 14 | 11 | 4 | 1 | 12 | 1  
nasdaqjockey12 | 1 | 5 | 5 | 1 | 13 | 2 | 1 | 8 | 13 | 1 | 2  
nasdaqjockey3 | 5 | 3 | 4 | 5 | 11 | 5 | 4 | 5 | 12 | 5 | 3  
nasdaqjockey1 | 10 | 6 | 9 | 13 | 14 | 15 | 8 | 12 | 14 | 6 | 5  
nasdaqjockey10 | 15 | 15 | 15 | 10 | 5 | 13 | 14 | 13 | 4 | 7 | 4  
nasdaqjockey11 | 3 | 1 | 1 | 11 | 2 | 7 | 3 | 1 | 3 | 2 | 6  
nasdaqjockey7 | 6 | 7 | 6 | 3 | 9 | 8 | 5 | 6 | 7 | 4 | 7  
nasdaqjockey2 | 8 | 10 | 12 | 8 | 15 | 10 | 10 | 15 | 15 | 11 | 8  
nasdaqjockey5 | 9 | 4 | 3 | 15 | 3 | 3 | 9 | 3 | 2 | 15 | 9  
evolvz | 2 | 2 | 2 | 4 | 6 | 4 | 2 | 2 | 8 | 3 | 10  
nasdaqjockey4 | 12 | 8 | 7 | 14 | 7 | 11 | 13 | 10 | 10 | 9 | 11  
nasdaqjockey6 | 11 | 14 | 14 | 7 | 8 | 9 | 12 | 14 | 11 | 13 | 12  
nasdaqjockey8 | 14 | 12 | 13 | 12 | 4 | 6 | 15 | 11 | 6 | 10 | 13  
nasdaqjockey | 4 | 9 | 8 | 2 | 12 | 1 | 6 | 7 | 9 | 8 | 14  
zbrain | 7 | 11 | 10 | 6 | 10 | 12 | 7 | 9 | 5 | 14 | 15  
  
Note that d0, d1, d2, d5, d6, d7, d9 are in descending order (higher values are better) and d3, d4, and d8 are in ascending order (lower values are better). Next, I find the correlation of each diagnostic rank with the performance rank:

validation sharpe | validation mean | feature neutral mean | validation sd | feature exposure | max drawdown | corr plus mmc sharpe | mmc mean | corr with example preds | validation score  
---|---|---|---|---|---|---|---|---|---  
0.061 | **0.232** | **0.182** | 0.021 | 0.021 | **-0.200** | **0.257** | **0.204** | -0.054 | **0.457**  
  
Now it become clear which diagnostics are most important when selecting a model to upload or determining stake amounts. You can draw some interesting conclusions from this. I was most surprised by the inverse correlation with max drawdown, that means models with high drawdowns when evaluated on the validation data perform better on live data! Also, consistency across eras is the most important metric (.457).

I had 51 trained models, so I created a normalized vector based on the above correlations and calculated a predicted score for each model and got the following results (sorted by score, lower is better):

**model** | **score** | **rank**  
---|---|---  
14 | 2.769437 | 1  
27 | 3.343164 | 2  
37 | 6.895442 | 3  
26 | 7.227882 | 4  
30 | 7.33244 | 5  
22 | 9.075067 | 6  
10 | 9.294906 | 7  
25 | 9.66756 | 8  
17 | 10.70777 | 9  
32 | 11.99196 | 10  
42 | 12.6059 | 11  
31 | 13.87131 | 12  
40 | 13.87131 | 13  
5 | 14.27078 | 14  
28 | 17.18231 | 15  
48 | 18.69437 | 16  
39 | 19.69705 | 17  
9 | 19.94638 | 18  
47 | 20.20107 | 19  
2 | 20.74799 | 20  
3 | 21.06971 | 21  
21 | 22.44504 | 22  
6 | 25.46649 | 23  
13 | 25.74799 | 24  
33 | 26.03485 | 25  
36 | 26.12601 | 26  
4 | 29.16086 | 27  
15 | 30.16354 | 28  
49 | 30.62466 | 29  
41 | 30.70509 | 30  
12 | 31.05898 | 31  
44 | 32.2252 | 32  
34 | 32.9008 | 33  
1 | 33.16622 | 34  
35 | 34.39678 | 35  
19 | 34.67828 | 36  
11 | 34.87936 | 37  
8 | 35.60054 | 38  
7 | 36.95174 | 39  
51 | 36.96515 | 40  
45 | 38.0992 | 41  
50 | 38.80697 | 42  
23 | 40.32708 | 43  
29 | 40.63539 | 44  
46 | 41.57909 | 45  
16 | 42.15818 | 46  
38 | 42.28686 | 47  
18 | 42.64611 | 48  
20 | 43.68901 | 49  
24 | 45.01072 | 50  
43 | 51 | 51  
  
I then selected the top 15 models to be uploaded and staked more on the models with a lower (better) predicted score.

**Summary**

If you are submitting multiple models and spreading your stake amongst them like me, this may be a good way to select models and stake them according to predicted performance and not just the diagnostics. Let me know if you have any ideas for improvement or if I made any errors. May your earns be strictly greater than your burns.

---

### Post #2 — **rsmillie94** | 2021-01-12 10:20 UTC

Very cool! You should keep this going, with a bigger sample of eras it would be very interesting to see what diagnostics are most important. A set of heavy burn eras would be good to look at.

---

### Post #3 — **restrading** | 2021-01-12 14:48 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nasdaqjockey/48/2933_2.png) nasdaqjockey:

> created a normalized vector based on the above correlations

Sorry for the dumb question, but would you elaborate on this? I am trying to understand it. Thanks!

---

### Post #4 — **nasdaqjockey** | 2021-01-12 23:41 UTC

I create the predicted score by weighting the correlation ranks for each model by a weight vector (aka normalized vector) and summing the results. The correlation values are (0.061, 0.232, 0.182, 0.021, 0.021, -0.200, 0.257, 0.204, -0.054, 0.457). You can convert this to a weight vector many different ways. The simplest is to sum the values and then divide each value by the sum. The sum of the values is 1.182 and the weight vector becomes (0.0514, 0.196, 0.154, 0.018, 0.018, -0.169, 0.218, 0.172, -0.045, 0.387). Since the predicted score is an arbitrary value I didn’t have to do this but it adds some interpretability to the score. The top model has a score of 2.769437 where a score of 1 is perfect (ranked #1 in all metrics). Without the normalization that goes away.

---

### Post #5 — **petervistar** | 2021-01-14 12:20 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nasdaqjockey/48/2933_2.png) nasdaqjockey:

> I use called validation_score, which is related to era consistency across the validation data (val1 and val2)

How did you calculate the validation_score?

---

### Post #6 — **nasdaqjockey** | 2021-01-14 19:14 UTC _(reply to #5)_

The validation_score is my secret weapon but I will tell you it is based on validation correlation. NumerAI used to report “consistency” and I extended that calculation. Consistency is calculated by counting the number of eras where your model’s achieves a correlation score greater than .002 and dividing by the number of eras.

---

### Post #7 — **petervistar** | 2021-01-15 19:01 UTC _(reply to #6)_

Ahh. I didn’t know NumerAI had a metric for consistency earlier.

---

### Post #8 — **succulent** | 2021-01-31 10:33 UTC

Would the max_drawdown correlation indicate that high risk is worth the reward in those eras, so to speak?

---

### Post #9 — **nasdaqjockey** | 2021-01-31 22:05 UTC _(reply to #8)_

Yes, but you have a higher chance of getting wiped out!

---

### Post #10 — **sirbradflies** | 2021-02-03 15:57 UTC

I have been playing around with this same question for a while and I wanted to share a simple script I am using to correlate validation metrics with live performance.

This script downloads the submissions of an account to chart both a correlation heatmap matrix and to save the raw data in a csv file for additional analysis.

The result for my submissions is quite interesting I believe:

[![submissions_correlations](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/6403f3e36634c5c23275f247a2ca9ea23139aff7_2_690x460.png)submissions_correlations1500×1000 163 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/6403f3e36634c5c23275f247a2ca9ea23139aff7.png> "submissions_correlations")

A few notes:

  * Live correlation is “Correlation”
  * I used the submissions starting from round 200 (I don’t remember exactly when Kazutsugi started)
  * Disregard the relationship between Round and Correlation (at least it shows I improved over time ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13) )



Below the script I have used.  
You can use it yourself by calling:  
`python script.py -i <NMR_PUBLICID> -k <NMR_SECRETKEY> [-m <MINIMUM_ROUND_NUMBER>]`

I’d be curious to see other people’s results!
    
    
    """
    Numerai tournament performance analyzer.
    Save submissions performance on CSV file and runs correlations
    with main diagnostic metrics.
    Use: python nmranalyzer.py -i <NMR_PUBLICID> -k <NMR_SECRETKEY> [-m <MINIMUM_ROUND_NUMBER>]
    """
    
    import argparse
    import pandas as pd
    import seaborn as sns
    from numerapi import NumerAPI
    import matplotlib.pyplot as plt
    from matplotlib import rcParams
    rcParams.update({"figure.autolayout": True})
    
    
    class NmrAnalyzer:
        def __init__(self, nmr_key=None, nmr_id=None):
            self.napi = NumerAPI(public_id=nmr_id, secret_key=nmr_key)
    
        def get_submissions_info(self, min_round=0):
            models = self.get_models().set_index("id")
            data = None
            for model_id in models.index:
                name = models.loc[model_id]["name"]
                submissions = self.get_model_sub(model_id)
                results = self.napi.daily_submissions_performances(name)
                results = pd.DataFrame(results).dropna().sort_values("date")
                results = results.groupby("roundNumber").nth(-1)  # Get final result from last day
                info = submissions.merge(results, left_on="round", right_index=True)
                data = info if data is None else data.append(info)
            data = data.merge(models, left_on="userId", right_index=True)
            return data[data["round"] >= min_round].set_index("id")
    
        def get_models(self):
            query = '''
            query {
                account {
                    models{
                        id
                        name
                    }
                }
            }
            '''
            data = self.napi.raw_query(query, authorization=True)['data']
            if data is None:
                return None
            else:
                return pd.DataFrame(data["account"]["models"])
    
        def get_model_sub(self, model_id):  # TODO: Extract also liveCorrelation when working
            query = '''
            query($modelId: String) {  
                user(modelId: $modelId) {
                    submissions{
                        id
                        userId
                        round {
                            number
                        }
                        filename
                        validationFeatureExposure
                        validationMaxDrawdown
                        validationCorrPlusMmcSharpeDiff
                        validationCorrPlusMmcMean
                        validationFeatureNeutralMean
                        validationMaxFeatureExposure
                        validationCorrelation
                        validationCorrPlusMmcSharpe
                        validationSharpe
                        validationStd
                        validationMmcMean
                        trainedOnVal
                        selected
                    }
                }
            }
            '''
            arguments = {'modelId': model_id}
            data = self.napi.raw_query(query, arguments,
                                       authorization=True)['data']
            if data is None:
                return None
            else:
                data = pd.DataFrame(data["user"]["submissions"])
                data["round"] = data["round"].apply(lambda x: x["number"])
                data = data[data["selected"] == True]  # Leave only submissions with live scores
                return data.drop("selected", axis="columns")
    
    
    def main():
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--nmrid", type=str, required=True,
                        help="NMR account id")
        ap.add_argument("-k", "--nmrkey", type=str, required=True,
                        help="NMR account secret key")
        ap.add_argument("-m", "--minround", type=str, required=False, default=0,
                        help="First round to consider in the analysis")
        args = vars(ap.parse_args())
        nmrizer = NmrAnalyzer(nmr_id=args["nmrid"],
                              nmr_key=args["nmrkey"])
        info = nmrizer.get_submissions_info(min_round=int(args["minround"]))
        info.to_csv("submissions_data.csv")
        plt.figure(figsize=(15, 10))
        sns.heatmap(info[info["trainedOnVal"] != True].corr(), annot=True)  # Excluding data trained on validation
        plt.savefig("submissions_correlations.png")
        plt.show()
    
    
    if __name__ == '__main__':
        main()

---

### Post #11 — **nasdaqjockey** | 2021-02-06 21:56 UTC _(reply to #10)_

Looks like we took different approaches but came to about the same results. The diagnostics that have the strongest correlation with profitable models are Validation Mean, Feature Neutral Mean, Corr + MMC Sharpe, and MMC Mean. And there is a string negative correlation with Max Drawdown. It will be interesting to see ifthese conclusions hold up over time.

---

### Post #12 — **succulent** | 2021-02-07 07:29 UTC _(reply to #11)_

This may be a silly question, but on getting some long-term data, would it make sense to train on epochs until n, and just use the n+1th epoch as the “live” data?

---

### Post #13 — **nasdaqjockey** | 2021-02-07 12:58 UTC

I’m not sure I understand your question. If by epoch you mean training epoch then n+1 will be very similar to your model predictions and not very useful as synthetic live data. Maybe you should post this question on rocket chat.

---

### Post #14 — **sirbradflies** | 2021-02-07 14:58 UTC _(reply to #11)_

Yes this is my experience so far. There are still some caveats in my analysis, firstly because I don’t remember exactly when Kazutsugi started and I picked tournament 200 as the starting point.

I hope somebody else will run my script and post the results so we can see if these patterns are “model-independent”.
