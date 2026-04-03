---
title: "Independence and Sharpe"
category: Data Science
url: https://forum.numer.ai/t/independence-and-sharpe/2560
created_at: 2021-03-27T21:03:02.060000+00:00
last_posted_at: 2022-01-13T21:40:34.515000+00:00
posts_count: 21
views: 4052
tags: []
---

# Independence and Sharpe

---

### Post #1 — **richai** | 2021-03-27 21:03 UTC

The more independent bets in a portfolio the better.

A casino in Las Vegas doesn’t need many Roulette wheels to almost never have a losing month because each wheel spin is independent and has an edge that favors the house. But often quant funds all go down in the same month. Clearly the bets of the quant funds are not nearly as independent as the casinos but independence is a very good goal because there is a relationship between your information coefficient (your correlation with the target), the number of independent bets you take and your Sharpe ratio.

[![Screen Shot 2021-03-27 at 1.32.07 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/43c2e0cae672dea91330ec07383f52002ae48090_2_690x250.png)Screen Shot 2021-03-27 at 1.32.07 PM1490×540 59.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/43c2e0cae672dea91330ec07383f52002ae48090.png> "Screen Shot 2021-03-27 at 1.32.07 PM")

Given this relationship, I think broadly people might be too focussed on improving their information coefficient instead of improving the degree of independence in their bets.

How do you measure whether your model trained on Numerai’s data is producing independent bets?

I was thinking about this last year and wrote this note that I wanted to share:

*What I mean by independence is that if you knew the outcome of 99 of the top 100 predictions of your model, would you be able able to say something more about the 100th stock? For example, if you had a predicted score of 0.7 and this was your highest prediction, and you knew that your 99 other scores did very well that era, would you want to bump up your prediction of 0.7 to say 0.75 or would knowing the targets not change your original prediction at all? If you wouldn’t want to change your 0.7 prediction at all then your predictions are independent.

I was thinking about ways to formalize this and came up with:

We call the error vector of a prediction set: (targets - prediction)**2

Richard’s Dependence = cor(1-error, era_score)

If you think of your performance on a prediction as 1-error, then Richard’s Dependence says the more correlation your era_score has to your prediction performance, the more dependent each prediction is on the outcome of your other predictions that month.*

I’ve found this simple measure of independence to be quite useful. For example, it can be used to determine when to stop training a model (when dependence is minimized). It also seems to be a better measure of the riskiness of a model that the standard deviation of correlation scores. By targeting independence when training a model, the model will tend to learn to reduce feature exposure automatically (big feature exposure typically means not a lot of independence). Just like the formula from Grinold & Kahn above, high independence tends to lead to higher Sharpe.

Nevertheless, I’m sure there are better, more statistical approaches to calculate the independence of model predictions. Can anyone propose something better than this with a more statistical basis? Perhaps we can formulate an independence measure we can include in diagnostics on Numerai and Numerai Signals.

Here’s a code sample that prints the dependence of example predictions to the validation targets
    
    
    sub = pd.read_csv("s3://numerai-public-datasets/latest_numerai_example_predictions_data.csv.xz", index_col=0)
    val_data = pd.read_csv("s3://numerai-public-datasets/latest_numerai_validation_data.csv.xz", index_col=0)
    
    val_targets = val_data[['era', 'target']]
    df = val_targets.join(sub)
    
    def richards_dependence(df, target_col, era_col, prediction_col):    
        scores_by_era = df.groupby(era_col).apply(
            lambda d: d[[prediction_col, target_col]].corr()[target_col][0]
        )
    
        # these need to be ranked within era so "error" makes sense
        df[prediction_col] = df.groupby(era_col)[prediction_col].rank(pct=True)
        df[target_col] = df.groupby(era_col)[target_col].rank(pct=True)
    
        df["era_score"] = df[era_col].map(scores_by_era)
    
        df["error"] = (df[target_col] - df[prediction_col]) ** 2
        df["1-error"] = 1 - df["error"]
    
        # Returns the correlation of the 1-error with the era_score
        # i.e. how dependent/correlated each prediction is with its era_score
        return df[["1-error", "era_score"]].corr()["era_score"][0]
    
    print(richards_dependence(df, 'target', 'era', 'prediction'))
    # 0.022152739462416336

---

### Post #2 — **joakim** | 2021-03-27 22:13 UTC

In short, if I have a tiny edge I’d like to place as many independent bets as possible.

Grinold & Kahn last year released a supplemental version to their classic: <https://www.amazon.com/Advances-Active-Portfolio-Management-Econometrics/dp/1260453715>

I’m still going through it…

---

### Post #3 — **gbrecht** | 2021-03-27 22:54 UTC

quick question to the code, specifically the `'DATE'` and `mm` keys in the input DataFrame and era scores:  
Does `mm` stand for metamodel?  
Does the `'DATE'` refer to predictions done in the rounds before or the month `scores_by_era[i]`?

---

### Post #4 — **richai** | 2021-03-27 23:46 UTC _(reply to #3)_

good question – edited the code to say “era”. this is from some internal code where we used “DATE” instead and “mm” maybe did mean a meta model I was testing… I think you could replace that with `prediction_col` and it should work so I made that edit now too. [@_liamhz](</u/_liamhz>) says he’ll make a cleaner version if that helps.

---

### Post #5 — **_liamhz** | 2021-03-28 00:38 UTC _(reply to #3)_

I’ve edited Richard’s post with a more clear standalone code sample

---

### Post #6 — **_liamhz** | 2021-03-28 03:52 UTC

Here’s the source of the Sharpe ratio image

[faculty.fuqua.duke.edu](<https://faculty.fuqua.duke.edu/~charvey/Teaching/BA453_2004/Muller_Proprietary_trading.pdf>) [](<https://faculty.fuqua.duke.edu/~charvey/Teaching/BA453_2004/Muller_Proprietary_trading.pdf>)

### [Muller_Proprietary_trading.pdf](<https://faculty.fuqua.duke.edu/~charvey/Teaching/BA453_2004/Muller_Proprietary_trading.pdf>)

928.05 KB

---

### Post #7 — **jorijnsmit** | 2021-03-28 08:52 UTC

You write:

> We call the error vector of a prediction set: (targets - prediction)*2

You code:
    
    
    df["error"] = (df[target_col] - df[prediction_col])
    df["error"] = df["error"] * df["error"]
    

I believe the *2 should be **2? Are you squaring the error to get rid of signage? What effect would square rooting the error afterwards have (basically implementing RMSE)? Or are you doing this on purpose to punish bigger errors stronger?

---

### Post #8 — **gbrecht** | 2021-03-28 09:19 UTC _(reply to #6)_

Thank you very much.  
As a “scholar of [@arbitrage](</u/arbitrage>)” (regTM) I find the part about digging deep vs. searching wide interesting, because of its translation to our classic tournament efforts: It means that it is better to look for one good learner than to ensemble weak learners. The reasons is that the correlation may not be as low as we think. Ensembles work very well in the classic tournament. Does that mean  
a) [@mdo](</u/mdo>) put together such a good target that it is easy for us to find uncorrelated assets?  
b) the bets of the fund are so long term and wide that the correlation transports well?  
c) there is a mismatch between live corr and fund performance (hopefully not!)?

---

### Post #9 — **gbrecht** | 2021-03-28 10:17 UTC _(reply to #7)_

You mean instead of:

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jorijnsmit/48/2305_2.png) jorijnsmit:

> `df["error"] = df["error"] * df["error"]`

it should read:  
`df["error"] = df["error"] ** df["error"]`

that would translate error^2 to error^(error)

---

### Post #10 — **jorijnsmit** | 2021-03-28 12:01 UTC _(reply to #9)_

No I believe the code is correct, it’s just that in the initial quote it is written as

> (targets - prediction)*2

Anyway that I believe is just a typo.

My real question is why not square root the error afterwards again?

---

### Post #11 — **orbitalteapot** | 2021-03-28 14:08 UTC

> lambda d: d[[prediction_col, target_col]].corr(method=‘spearman’)[target_col][0]

In this line, need to add method=‘spearman’ to recreate Richard’s results.

If the function is applied several times on the same df, it doesn’t matter due to the mutation to ranks later on in the function.

---

### Post #12 — **gbrecht** | 2021-03-28 14:40 UTC _(reply to #10)_

With other metrics like MSE and RMSE for regression, the difference is that without rooting outliers are penalized harder.

---

### Post #13 — **richai** | 2021-03-28 18:23 UTC _(reply to #8)_

yes when thinking about targets we do look at how much dependence there is. if you remember our old target “Bernie”, it had much higher dependence and models didn’t generalize nearly as well on live data because of that.

---

### Post #14 — **richai** | 2021-03-28 18:38 UTC

@MikeP was talking to me last night about giving an example of a model which has low Standard Deviation of correlations on the validation set (SD) but actually has high Dependence — such an example would show how this really is a different measure of risk. I think there is probably some feature that if you submit the feature as your prediction it has a good Sharpe (low standard deviation) but has very high dependence, which is a nice warning sign that even if it has high Sharpe on validation it’s probably not likely to work well out of sample because of it’s high dependence. Would be nice if someone could find such a feature and post the result here ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #15 — **jorijnsmit** | 2021-03-31 08:33 UTC _(reply to #11)_

Just to deepen my understanding, why does adding `method='spearman'` matter? We already ranked `prediction_col` and `target_col` in order to calculate `error` properly, so it shouldn’t matter right? I do still get a very small difference (maybe just rounding?):
    
    
    0.021525909978845296
    0.021525909978845223
    

Oh and I found one more typo, `df.era.map(scores_by_era)` should be `df['era_col'].map(scores_by_era)`.

---

### Post #16 — **profricecake** | 2021-04-01 07:34 UTC _(reply to #14)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/richai/48/2493_2.png) richai:

> I think there is probably some feature that if you submit the feature as your prediction it has a good Sharpe (low standard deviation) but has very high dependence, which is a nice warning sign that even if it has high Sharpe on validation it’s probably not likely to work well out of sample because of it’s high dependence. Would be nice if someone could find such a feature and post the result here ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

I ran through the full feature list but didn’t find any that I’d think of as having a particularly high Sharpe.

For reference, the best I found was `feature_charisma74` with a validation Sharpe of `.47`.

I tried inverting the features too, just for kicks. The best performer was `1.0 - feature_constitution100` with a validation Sharpe of `.52`.

Do you consider either of those high enough to be representative of what you were discussing, [@richai](</u/richai>) ?

---

### Post #17 — **orbitalteapot** | 2021-04-02 14:08 UTC _(reply to #15)_

The ranking takes place after the score_by_era calculation.

In order to recreate the result (0.022152739462416336) in OP, ranking needs to be performed before the score_by_era calculation or spearman needs to be used.

When performing the richards_dependence function twice, you’d get the OP’s result the second time. The results I get on two consecutive runs.
    
    
    0.021851763462089693
    0.022152739462416336
    

The reason behind this is because pandas is pass-by-reference and not pass-by-value. Thus these two lines overwrite the original values of prediction_col and target_col.
    
    
    df[prediction_col] = df.groupby(era_col)[prediction_col].rank(pct=True)
    df[target_col] = df.groupby(era_col)[target_col].rank(pct=True)

---

### Post #18 — **richai** | 2021-04-05 22:01 UTC _(reply to #16)_

Definitely high enough. And did you try calculate their dependence?

---

### Post #19 — **profricecake** | 2021-04-06 03:08 UTC _(reply to #18)_

[@richai](</u/richai>) Here are the validation Sharpes and “Richard’s dependence” values for both features:
    
    
    feature_charisma74                  vsharpe: 0.47   rdep: 0.0158
    1.0 - feature_constitution100       vsharpe: 0.52   rdep: 0.0100

---

### Post #20 — **thekizoch** | 2021-11-22 07:02 UTC

What was the end result of this discussion? Does a finalized form of measuring independence get returned in the validation_metrics() function in the (basic) example script or is this still up to the data scientist to code Richard’s dependence into his/her code?

Thanks in advance

---

### Post #21 — **baslaa** | 2022-01-13 21:40 UTC

Hi [@richai](</u/richai>) ,

After reading this post I starting reading a bit about this fundamental law of active management to understand more about it, and I found this interesting paper that I wanted to share on why it might not be completely reliable. Not sure what I think of it yet, but it is interesting.  
<https://newfrontieradvisors.com/media/1333/fund-law-april-2017.pdf>
