---
title: "MMC Calculation 'Punishes' Originality During Meta-Model Burns"
category: Feedback
url: https://forum.numer.ai/t/mmc-calculation-punishes-originality-during-meta-model-burns/738
created_at: 2020-07-31T07:56:08.048000+00:00
last_posted_at: 2021-09-06T17:39:11.875000+00:00
posts_count: 33
views: 4498
tags: []
---

# MMC Calculation "Punishes" Originality During Meta-Model Burns

---

### Post #1 — **sdmlm** | 2020-07-31 07:56 UTC

As the title indicates, when the meta-model has a negative score, MMC “punishes” originality. I’ve included a toy example code and an alternative mmc formula for negative periods.

Basically, when the meta-model has negative stock market corr, the more meta-model exposure/corr a model has, the higher the MMC, which I believe shouldn’t be the case.

I might be completely wrong/off in my calculations/formula for MMC. But if I’m not, seems like something that should be addressed.

The intuition for the current problem is something like this: user model has 0.99 corr with meta-model, user model has 1% corr on stock market, meta-model has -1% corr on stock market, mmc will be something like 2% (1% user corr - 0.99 * (-1% meta-model raw corr). If the user model had 0 corr with meta-model, then mmc will be something like 1% (1% - 0 * (-1%)). Which seems to go against the incentive plan of rewarding originality. When the meta model is positive, this doesn’t hold obviously.  
The code uses the actual mmc formula/proper computations.

Basically, during negative periods, the lower the meta-model corr a model has, the lower mmc score, assuming equal raw corr on the stock market.

I’ve proposed an alternative payment scheme for negative periods in the code.  
Basically, when meta_model is negative, neutralize with proportion = - 1 (note the minus!), then do some “manual” cleaning to the mmc score, so that if the user model has 0.99 corr with meta-model but much higher raw corr on the stock market, it still gets a good mmc score, but lower than a model with 0 corr with meta-model. Obviously this needs to be further checked by the numerai team so that there are no cases where it falls apart.
    
    
    import numpy as np
    import pandas
    import scipy.stats
    
    def spearmanr(target, pred):
        return np.corrcoef(
            target,
            pred.rank(pct=True, method="first")
        )[0, 1]
    
    def neutralize_series(series, by, proportion=1.0):
       scores = series.values.reshape(-1, 1)
       exposures = by.values.reshape(-1, 1)
    
       # this line makes series neutral to a constant column so that it's centered and for sure gets corr 0 with exposures
       exposures = np.hstack(
           (exposures, np.array([np.mean(series)] * len(exposures)).reshape(-1, 1)))
    
       correction = proportion * (exposures.dot(
           np.linalg.lstsq(exposures, scores)[0]))
       corrected_scores = scores - correction
       neutralized = pandas.Series(corrected_scores.ravel(), index=series.index)
       return neutralized
    
    def _normalize_unif(df):
        X = (df.rank(method="first") - 0.5) / len(df)
        return scipy.stats.uniform.ppf(X)
    
    target = pandas.Series([0, 0, 0, 0,
              0.25, 0.25, 0.25, 0.25,
              0.5, 0.5, 0.5, 0.5,
              0.75, 0.75, 0.75, 0.75,
              1, 1, 1, 1])
    
    meta_model = pandas.Series([1, 0, 0.25,
                  1, 0.5, 0.75,
                  0.5, 0.5, 1,
                  0.75, 0.75, 0,
                  0, 0.25, 0.25,
                  1, 0, 0.25, 0.5, 0.75])
         
    high_meta_corr_model = pandas.Series([1, 0, 0.25,
                  1, 0.25, 0.75,
                  0.5, 0.5, 1,
                  0.75, 0.75, 0,
                  0, 0.25, 0.25,
                  1, 0, 0.5, 0.5, 0.75])
    
    low_meta_corr_model = pandas.Series([1, 1, 0.75,
                  0, 0.5, 0.25,
                  0.5, 0.25, 0,
                  0.5, 0.25, 1,
                  1, 0.75, 0.75,
                  0, 0, 0.75, 0.5, 0.25])
       
    # Meta model has raw corr with target of -5.5% (burning period)
    meta_model_raw_perf = spearmanr(target, meta_model)
    print(f"Meta_model performance: {meta_model_raw_perf}")
    
    # Model highly correlated with meta model (i.e. non-original model)
    # 95% meta-model correlation
    # 2.45% raw corr with target
    # Overall a good model, but not very original
    
    high_meta_corr_raw_perf = spearmanr(target, high_meta_corr_model)
    high_meta_corr = spearmanr(meta_model, high_meta_corr_model)
    
    print(f"High_meta_corr model cross-corr: {spearmanr(meta_model, high_meta_corr_model)}")
    print(f"High_meta_corr model performance: {high_meta_corr_raw_perf}")
    
    
    # Model uncorrelated with meta model (i.e. original model)
    # -63% meta-model correlation
    # 2.45% raw corr with target
    # Overall a good model and also very original
    low_meta_corr_raw_perf = spearmanr(target, low_meta_corr_model)
    low_meta_corr = spearmanr(meta_model, low_meta_corr_model)
    
    print(f"Low_meta_corr model cross-corr: {spearmanr(meta_model, low_meta_corr_model)}")
    print(f"Low_meta_corr model performance: {low_meta_corr_raw_perf}")
    
    # MMC Computation
    # All series are already uniform
    
    # Neutralize (using forum post code for neutralization)
    neutralized_high_corr = neutralize_series(high_meta_corr_model, meta_model, proportion=1.0)
    neutralized_low_corr = neutralize_series(low_meta_corr_model, meta_model, proportion=1.0)
    
    
    # Compute MMC
    mmc_high_corr = np.cov(target, 
                                neutralized_high_corr)[0,1]/(0.29**2)
    
    mmc_low_corr = np.cov(target, 
                                neutralized_low_corr)[0,1]/(0.29**2)
    
    print(f"MMC for non-original model: {mmc_high_corr}")
    print(f"MMC for original model: {mmc_low_corr}")
    
    # I assume there is some clipping in order to not actually give negative mmc to the original model in reality
    # Still 0.108 MMC for meta-model copy (non-original model) vs -0.43 MMC for completely different model seems bad
    # CORR+MMC performance is 0.0245 + 0.108 for non-original model vs 0.0245 - 0.43 for original model
    # Most likely this will hold in any burning period, and the more original a model is, the more punishing MMC will be in a burning period!
    
    # Counter proposals:
    # Keep same MMC in good periods
    # In burn periods (i.e. meta-model is negative), make proportion = -1.0 in neutralize_series, and then use manual clipping techniques
    # E.g. proposal
    
    # Neutralize (using forum post code for neutralization) with -1
    neutralized_high_corr = neutralize_series(high_meta_corr_model, meta_model, proportion=-1)
    neutralized_low_corr = neutralize_series(low_meta_corr_model, meta_model, proportion=-1)
    
    
    # Compute MMC
    mmc_high_corr = np.cov(target, 
                                _normalize_unif(neutralized_high_corr))[0,1]/(0.29**2)
    
    mmc_low_corr = np.cov(target, 
                                _normalize_unif(neutralized_low_corr))[0,1]/(0.29**2)
    
    print(f"New MMC before clipping for non-original model: {mmc_high_corr}")
    print(f"New MMC before clipping for original model: {mmc_low_corr}")
    
    # Now mmc_high_corr is negative
    # Clipping
    
    new_mmc_high_corr = max([(1 - high_meta_corr) * (high_meta_corr_raw_perf - meta_model_raw_perf), mmc_high_corr, high_meta_corr_raw_perf])
    new_mmc_low_corr = max([(1 - low_meta_corr) * (low_meta_corr_raw_perf - meta_model_raw_perf), mmc_low_corr, low_meta_corr_raw_perf])
    
    print(f"New MMC for high correlation is still positive but quite low as the model is a copy of the meta model: {new_mmc_high_corr}")
    print(f"New MMC for low correlation is very high as the model is almost opposite to the meta model: {new_mmc_low_corr}")

---

### Post #2 — **jackerparker** | 2020-07-31 08:33 UTC

Indeed, you have shown an example of very unique and useful model. If you have 0.99 correlation with MM, but your CORR is 1% vs -1%, that would mean that you found 1% of stocks which significantly changes the output of model. In my opinion, that model is even better than model with 0 correlation with MM and 1% CORR.  
I can be also completely wrong here, but that is my intuition.

---

### Post #3 — **sdmlm** | 2020-07-31 08:40 UTC _(reply to #2)_

If what you are saying is true, then what is the point of originality/MMC? It also goes against how MMC behaves during good periods. In good periods (which fortunately are probably the majority of periods) MMC rewards originality properly. In my example, if I switch the meta-model raw corr performance to some positive number, then it’s all good, the low meta-model corr model is rewarded properly vs the high meta-model corr model. Only during burn periods there is this weird “inversed” behavior, where basically you are rewarded for being as close to the meta-model as possible.

Also, if I were to make the user model performances -1%, then the MMC for the meta-model clone would be 0 (fair enough as it’s equal to the meta-model), but the MMC for the original model would be -1% which is very bad…in reality maybe they do some manual clipping/modification in order to avoid this situation, but still seems to be against the spirit of MMC and rewarding originality.

---

### Post #4 — **jackerparker** | 2020-07-31 09:53 UTC _(reply to #3)_

Could you please describe your example in more details? I don’t understand your main point which is “the MMC for the original model would be -1%”. MMC will be negative only if combination of MM and your original (0 corr with MM, right?) model provides a lower COR than MM itself (so, it should be something less <-0.01). MMC will be positive, if combination of MM and your model provides a higher COR than -0.01. That has nothing in common with MM COR, it can be both positive and negative.

But in general, you must get negative MMC if your model makes MM worse and it doesn’t matter if you doing it in unique or non-unique way. Lets think about it from MM point of view. Just imagine, in near future payout will be a percentage of fund MM profit multiplied to your contribution to the MM. And someone add his own model to MM, which make a negative impact on MM (Increases loses when MM has negative COR and reduces profit when MM has positive COR). Do you think that you will be happy that this user is participating here and getting any positive payout?)

P.S. I’m not a native speaker and hope that there is nothing offensive in my style.

Regards,  
Mark

---

### Post #5 — **sdmlm** | 2020-07-31 10:16 UTC _(reply to #4)_

I’m using the actual formula for MMC calculation. Basically, in the MMC formula, you do the following steps:

  1. Transform all predictions to standard uniform
  2. Neutralize against the meta-model
  3. Transform neutralized predictions to standard uniform
  4. Compute MMC as the covariance between neutralized predictions and the target, divided by 0.29^2 (variance of standard uniform) to get to correlation space



This is the formula from [MMC2 Announcement](<http://forum.numer.ai/t/mmc2-announcement/93/24>)

The MMC is not influenced in any way by how the meta model performs in combination with specific user predictions. It is influenced by the overall meta model performance and the user’s exposure (correlation) to the meta model, as seen in the above steps.

Now, using the above formula when the meta model raw corr is -1% with two user models:  
Model A: raw corr -1%, meta model corr 0.99 (so a meta model clone)  
Model B: raw corr -1%, meta model corr 0 (same performance, but completely uncorrelated)

You would get roughly MMC model A score of 0, MMC model B score of -1%.  
So originality gets ‘punished’, as you get much lower MMC with the uncorrelated model.

Again, this only happens when the meta model has negative correlation with the target.

You could think about it like this: model A has 0.99 exposure to the meta model, which this round is a negative feature/predictor. By removing the meta model from model A, the MMC for model A is increased just because we remove a negative corr exposure. But model B is not correlated to the meta model, so neutralization doesn’t change anything. It doesn’t “benefit” from the negative performance of the meta model.

In good periods, model B really benefits from MMC. Using the above MMC formula when the meta model raw corr is 1% with two user models:  
Model A: raw corr 1%, meta model corr 0.99 (so a meta model clone)  
Model B: raw corr 1%, meta model corr 0 (same performance, but completely uncorrelated)

You would roughly get scores of around 0% MMC for model A, but around 1% MMC for model B.  
So total CORR+MMC scores are 1% for model A (basically no originality = 0 MMC) and 2% for model B (originality makes MMC=CORR leading to twice the payout of just CORR).

---

### Post #6 — **alfa137** | 2020-07-31 11:21 UTC _(reply to #5)_

**Regarding Model A** , I totally agree:  
It is almost a MM clone, it does not add anything to MM, so 0% MMC. OK

**Regarding Model B:**  
You say it is completely uncorrelated with MM, but you give numbers that shows perfect correlation:  
MM CORR = -1% ==> Model B CORR = -1%  
MM CORR = 1% ==> Model B CORR = 1%  
If you use this numbers:  
MM CORR = -1% ==> Model B CORR = -1%  
MM CORR = 1% ==> Model B CORR = -1%  
you get MMC = -1%, as it should be, because its contribution is negative to the MM performance.

**Regarding originality:**  
You can do something very original and very bad, or something very original and very good. In your example, B is an original and bad model. Originality should pays if it contributes in the right direction.

---

### Post #7 — **sdmlm** | 2020-07-31 11:37 UTC _(reply to #6)_

Sorry, maybe I wasn’t clear.  
Model B has stock market correlation of -1%  
Meta model has stock market correlation of -1%  
Model B has correlation with meta model of 0%.  
These 3 things are completely separate numbers/notions.

You could get a model with the same corr on the stock market as the meta model, but around 0% correlation with the meta model itself. Please do no confuse the 3 correlation types.

I’m not saying that originality should be rewarded when it’s bad.  
I’m saying that it gets punished “more” than a meta model clone. Which shouldn’t be the case as this overall diminishes the incentives of MMC, by basically saying that during meta model burns, meta model clones are “safer”.

Perhaps the problem is more like MMC punishes meta model clones less during meta-model burns, than original models.

I have seen actual models during this round that have higher positive corr on target, lower meta-model correlation, but lower MMC than models with lower corr (even negative) on target, but higher meta-model correlation.  
As stated, these models would probably have higher MMC during good periods, but why should they have lower MMC during bad periods?

**If you run my example code, the two models have the same positive corr on target (around 2.4%) on target, but because the meta model has around - 5% (so really negative) corr on target, the MMC for the original model is negative while the MMC for the 95% meta model correlation model is very high and positive.**

Basically, we remove the very bad signal (the meta model in this case) from the meta model clone and we end up with a huge MMC. For the -63% meta model correlation model (so a completely original, even opposite model to the meta model), we get really negative MMC. Why? Because we are basically adding the meta model to the original model (negative times negative equal plus), as per the neutralize_series code from the official forum post.

---

### Post #8 — **alfa137** | 2020-07-31 12:18 UTC _(reply to #7)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/sdmlm/48/1152_2.png) sdmlm:

> You could get a model with the same corr on the stock market as the meta model, but around 0% correlation with the meta model itself. Please do no confuse the 3 correlation types.

I am not confusing them, I agree that case is possible. So, if you say: “Model B has correlation with meta model of 0%”, your example should have numbers according to that hypothesis. If B and MM are uncorrelated, good periods for MM should not perfectly overlap with good periods for B.  
Translating this to your example: even if the two scenarios that you describe were posible, and you got those outcomes, they are not representative of the average outcome in the long run. Maybe you get that contradictory results in 1 or two rounds, but not on average.  
I am not sure but maybe the problem is that the numbers you have included in your simulation are not satisfying all the hypothesis you have made.

---

### Post #9 — **sdmlm** | 2020-07-31 12:42 UTC _(reply to #8)_

The toy code example was just for illustrative purposes, but it’s a miniature of a possible real world  
scenario.

If you look at and understand the way the neutralization function works, you do not need actual numbers.

---

### Post #10 — **wigglemuse** | 2020-07-31 12:50 UTC _(reply to #5)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/sdmlm/48/1152_2.png) sdmlm:

> The MMC is not influenced in any way by how the meta model performs in combination with specific user predictions. It is influenced by the overall meta model performance and the user’s exposure (correlation) to the meta model, as seen in the above steps.

Aren’t you glossing over the part where your predictions are neutralized with the metamodel and so then the residuals are compared to the targets? You make it sound as if _only_ your single-number correlation score matters to this process and not the actual interactions of your specific predictions and the metamodel and targets. (i.e. not everybody with the same overall correlation to the targets and also the same correlation to the metamodel will end up with the same MMC, right? The actual predictions do matter.)

Anyway, here’s an interesting case. For round 218 I submitted a couple of unstaked (1-p) models to my normal models to see if the MMC results would be exactly symmetrical. (They are.) But the effect was interesting with one of them. (218 was probably a metamodel burn, right?)

The result for “wigglemuse” (one of my normal models) was a burn:

CORR_TARGETS: -0.0151  
CORR_META: +0.6902  
MMC: +0.0027

So I’ve got a slight positive MMC for a model that is relatively correlated with metamodel (but nothing close to a clone) but did slightly better than the metamodel (judging by my rank and scores by integration_test,etc) but still negative to targets. So that’s fine.

And so the (1-p) model (“smoghovian”) ended up with the exact opposites:  
CORR_TARGETS: +0.0151  
CORR_META: -0.6902  
MMC: -0.0027

So the opposite – at least if you looked at it in isolation and weren’t thinking about it flipped – might leave you scratching your head. Here I was highly negatively correlated with the metamodel, did WAY better on correlation to the targets, and yet have a slight negative MMC. But of course it is completely symmetrical with the other opposite model ( as expected) although some disagree that any positive corr should get a negative MMC.

I think the disconnect comes as many want to be additionally rewarded/punished for essentially the same thing as CORR is measuring if they do it better or worse than others. (In which case we’d just make MMC = percentile corr rank) But MMC is actually on a totally different axis (or can be) than your CORR scores, and is its own number. Which doesn’t necessarily make it a good or useful number (it doesn’t necessarily not either), but we’ve seen lots of attempts to judge it by its correlation to other things rather than just what it is actually trying to measure.

---

### Post #11 — **sdmlm** | 2020-07-31 13:08 UTC _(reply to #10)_

Thank you for proving my point!

Your two models are a perfect example of what I’m trying to explain.

Indeed 218 was most likely a meta model burn round.

The intuitive explanation (not following the actual formula!) is something like this: your wigglemuse model had negative corr, but mmc is approximately (again not actual official formula) something like wigglemuse_corr - wigglemuse_exposure*mm_corr = -0.0151 - (0.6902) * (-0.0307 integration test) = 0.0061 (which is not super far from 0.0027). If I use mm score of -0.026 I get 0.0028 MMC (which is more realistic as MM should beat integration test)

The same can be applied to smoghovian: MMC = +0.0151 - (-0.6902) * (-0.0307) = -0.0061, or -0.0028 if I use again -0.026.

Now the question is do we want this sort of scenario?

If wigglemuse had CORR_META of 1 and smoghovian CORR_META of -1, the difference in MMC would be even more extreme, in favor of wigglemuse. However, wigglemuse had a really negative raw corr while smoghovian had a really good positive corr, so why are we rewarding wigglemuse? Negative corr and kinda correlated to the meta model…  
While an opposite, original model with highly positive corr gets negative (?!) mmc?

And again it would be even more extreme if the corrs with the meta model were 1 and -1.

Regarding the neutralization, I was merely offering a simple explanation. In my example code I used the exact formula and steps for MMC and the official neutralization function from the official forum post.

The whole scenario comes from the neutralization function…

---

### Post #12 — **wigglemuse** | 2020-07-31 13:32 UTC _(reply to #11)_

I don’t have a strong feeling about it one way or another at this time. As far as why are we rewarding wigglemuse in this case, well I say would we are not! Especially since now we get CORR or CORR+MMC but never just MMC, I’d actually much rather have wigglemuse’s burn be somewhat offset by a positive MMC than get rid of the slight ding to smoghovian’s overall positive score. wigglemuse is still negative and smoghovian still positive as far as payouts go.

I am suspicious of the appropriateness of the neutralization function as it is and certainly am not opposed to further improvements to the MMC calculation. But I just don’t have the mathematical grounding to really make a good argument on that front so I’ll have to leave that to others. But most arguments seem to want to converge MMC towards CORR, but if they are too alike then we don’t need them both. I have no problem for instance with MMC being negative at times that CORR is positive and vice-versa, etc etc. I think what you are pointing out is interesting but I’m not yet convinced it is a travesty of justice. And I tend not to like “fiddly” solutions that single out special cases and try to adjust them to “better” outcomes – if that is needed we need to get to the root cause of the problem and come up with a total elegant solution that doesn’t rely on exceptions and special adjustments. At least that’s the ideal. If we are going to tear it down, let’s tear it all the way down and then build it up again a better way.

---

### Post #13 — **sdmlm** | 2020-07-31 13:59 UTC

It’s not a special case. This sort of scenario will always happen during burn periods due to the way the neutralization function is set up.

wigglemuse is technically rewarded with mmc. When I was mentioning rewards etc, I was 100% referring to numerai’s rewards for originality. From my point of view, corr is not a reward per-se as that is simply raw performance on the target for which anybody can earn a decent number with the example_predictions. MMC on the other hand is numerai’s incentive to be original. To deviate as much as possible from the example predictions (and meta model).

From a payout perspective sure it’s less important, but I’m seeing this as a problem for numerai’s plan of rewarding originality.

I certainly do no want for MMC to converge towards CORR.  
I am merely stating the fact that MMC “fails” as an incentive to be original when the meta model is negative. As stated before, a simple, basic explanation of the neutralization is that it “removes” the meta model. However, what happens when you remove a negative stock market corr feature from a model that had a positive exposure to that feature?

I am also 100% ok with MMC to be negative even with positive CORR and vice-versa, but only when it should.

E.g. positive corr but highly correlated with example predictions and maybe corr is even less than the example predictions corr -> negative MMC.

Or negative corr, but low correlation to example predictions and maybe even beating the example predictions -> positive MMC.

However, as your models proved, you can have positive CORR, negative exposure to the meta model, significantly outperforming the example predictions (and meta model too probably) and have negative MMC. This I can’t really see as an acceptable scenario…

And the problem is only on the rounds with negative meta model, otherwise I believe MMC is really well constructed. On positive rounds, it removes the meta model performance (proportionately to the user’s exposure) and computes the corr again (with covariance), very elegant and straightforward…

It would only need a bit of a fix for negative rounds…

---

### Post #14 — **wigglemuse** | 2020-07-31 14:12 UTC _(reply to #13)_

It is of course MMC – MetaModel Contribution, not Originality Score (for which we could use simple uncorrelatedness to metamodel).

So we can see how the wigglemuse model deserved a slightly positive MMC for helping the metamodel to be less bad during a burn period. But smoghovian should have also done that even more, right? (Both wigglemuse and its opposite smoghovian were superior to the metamodel corr-wise as far as we can reasonably guess.) So the question for the team is how is it possible (or the better question: how is it reasonable and acceptable) for the smoghovian model with its way better target corr and negative mm corr to actually be hurting the metamodel? Is it really, or it is a mathematical quirk of the neutralization process and negative metamodel performance that round? I guess I’d like to hear from the defense at this point…

---

### Post #15 — **sdmlm** | 2020-07-31 14:34 UTC _(reply to #14)_

It’s the way the neutralization function is set-up.

My understanding is this: the neutralization function is actually just a slightly modified linear regression model.

user_predictions = a x mean_of_user_predictions + b x meta_model_predictions

  1. a and b are the coefficients:



Code: np.linalg.lstsq(exposures, scores)  
exposures are the meta_model_predictions concatenated with the mean_of_user_predictions  
scores are the user_predictions

  2. mean_of_user_predictions is just a vector filled with the mean of the users predictions, basically instead of using 1 we use the mean of the user predictions as the intercept column
  3. meta_model_predictions are the meta model



after estimating this model:

neutralized_user_predictions = user_predictions - (a x mean_of_user_predictions + b x meta_model_predictions)

Code: corrected_scores = scores - correction

So the neutralized user predictions are just the residuals from this linear model.

Perhaps this makes it clearer…  
For a MM clone, b is going to be large and positive (near 1), leading to something like this:  
user_predictions (e.g. 1% raw corr) - b * meta_model_predictions (some negative corr, e.g. -3%) =  
neutralized_user_predictions -> higher corr, probably something like 4% (1 - - 3%) if b around 1

For an original model, b is going to be small, e.g. 0 for 0% correlation to meta model  
user_predictions (e.g. 1% raw corr) - b * meta_model_predictions (some negative corr, e.g. -3%) =  
neutralized_user_predictions -> 1% raw corr as b = 0

---

### Post #16 — **lackofintelligence** | 2020-08-02 07:24 UTC

I think [@sdmlm](</u/sdmlm>) has done a very good job of identifying one the problems with MMC. It seems so clear to me I was compelled to write something, which I will just paste here.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/390ddf5bdd43366863f6ea44e417638eee6a840f_2_575x500.png)image894×777 75.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/390ddf5bdd43366863f6ea44e417638eee6a840f.png> "image")

---

### Post #17 — **sdmlm** | 2020-08-02 07:56 UTC _(reply to #16)_

Hi [@lackofintelligence](</u/lackofintelligence>), thanks a lot for this! Indeed this is a very nice mathematical presentation of the problem. The discussion also evolved further on the feedback channel on the chat. Hopefully they’ll address it soon, especially if meta model burns will become more frequent.

For example, if somehow the meta model had overall 0% corr on target across rounds and 50% rounds would be burns, then mmc overall doesn’t reward (nor punish) originality in any way on average. That is why I believe this sort of behaviour is detrimental to the incentive plan of rewarding originality (combined with performace of course)…

---

### Post #18 — **wigglemuse** | 2020-08-02 13:29 UTC

How about make a sort of confusion matrix with all the basic negative/positive possibilities of a model relatively closely related to the metamodel and one with much lower mm correlation, and what same situations would look like under proposed solution?

---

### Post #19 — **lackofintelligence** | 2020-08-02 15:28 UTC _(reply to #17)_

That is easy to see by taking the average of the derived formula for MMC. The average MMC:

`<MMC>` = `<CORR>` \- `<U, M>` x `<M, T>`

When the average correlation of the meta model to the truth is zero, `<M, T>` is zero, the 2nd term in the equation is zero so `<MMC>` = `<CORR>`; originality, which can be represented by the inverse of `<U, M>`, has no impact on the score in that case.

---

### Post #20 — **sdmlm** | 2020-08-02 19:38 UTC

Yes that is exactly the case. And once the correlation of the meta model to the truth becomes negative, then negative times negative = plus, so the more correlated with the meta model, the higher the score.

Regarding an alternative to the current MMC, as a first step, there needs to be some consensus on what characteristics MMC should have.

My opinion:

  1. Transparency: no black box approach as I believe the community should understand how they are scored and have the opportunity to perform their own analysis like this forum post. The current MMC mostly satisfies this.

  2. All other things being equal, MMC should always increase with a decrease in corr to the meta model. E.g. two models, same exact corr on target, the model with a lower corr with the meta model should always have higher MMC. The current MMC formula does not satisfy this during negative meta model rounds as less corr with meta model decreases MMC.

  3. Simplicity: the MMC should not have an overly complicated methodology, in order to have as many people properly understand how their being scored. If users understand how they’re being scored for originality (and relative performance), they’ll have an easier time actually working towards that goal. The current MMC only somewhat satisfies (or doesn’t satisfy) this as I got the impression most people have a hard time understanding the neutralization function and the underlying mathematics behind it. This is probably also one of the reasons why the main problem with the current MMC hadn’t been identified until now.

  4. (Similar to 2) MMC should always be a monotone increasing function of: originality and relative performance to the meta model. By originality I mean correlation to the meta model (original model = low correlation to the meta model). By relative performance I mean how much better or worse is the user’s model vs the meta model. MMC should of course increase with lower correlation with the meta model, but it should also decrease when the user’s predictions underperform the meta model. An original model shouldn’t be rewarded if it has very very bad relative performance. The current MMC does not satisfy this as during negative meta model rounds it punishes originality, i.e. it is not monotonically increasing in originality.

---

### Post #21 — **master_key** | 2020-08-02 20:41 UTC _(reply to #20)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/sdmlm/48/1152_2.png) sdmlm:

> All other things being equal, MMC should always increase with a decrease in corr to the meta model. E.g. two models, same exact corr on target, the model with a lower corr with the meta model should always have higher MMC. The current MMC formula does not satisfy this during negative meta model rounds as less corr with meta model decreases MMC.

So this is not really what we want. Take a case where the metamodel is in a burn period, scoring -0.05. Model A submits random noise, and scores -0.01. Model B submits a model that is **strictly better than the metamodel** , but very similar to the metamodel, scoring -0.04.

What you’re saying is we should reward this model A random noise because it looks unique and it did better than the metamodel. But it gave 100% unique information, and the result was negative. It should be punished. It made the metamodel strictly worse than it was before. Model B however made the metamodel strictly better, so it should be rewarded.

Looking only at correlation_score and correlation_w_metamodel can be very misleading in this way. The current MMC approach corrects this though, and only rewards for real added unique information.

The reason we see some models with low correlation get hurt worse in burn rounds is because they are actually not helpful signals in most cases ![:frowning:](http://forum.numer.ai/images/emoji/twitter/frowning.png?v=12)

MMC is very difficult… you don’t play it just because you can submit a unique signal. Anyone can do that. You play it because you have something valuable that is currently either absent or underrepresented in the metamodel.

Still, your code example highlights a different part of MMC design. It seems like this is really a case of it being a 1-P model, and that information gets removed by neutralization, just as submitting the metamodel itself would. You could also form a similar example where you submit exactly a negative version of the metamodel, and boom you have something SUPER ORIGINAL (-1 corr with metamodel), and also scored +0.05 instead of -0.05! In your encoded example, that unique model was actually worse than simply submitting a negative metamodel in its entirety. But that’s not really original, it’s just market timing with a signal we already have. I can see some argument for rewarding that, but it’s not what we wanted to accomplish with MMC. Corr will already reward that timing ability proportionally to its value.

---

### Post #22 — **sdmlm** | 2020-08-02 20:54 UTC _(reply to #21)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png) master_key:

> What you’re saying is we should reward this model A random noise because it looks unique and it did better than the metamodel. But it gave 100% unique information, and the result was negative. It should be punished. It made the metamodel strictly worse than it was before. Model B however made the metamodel strictly better, so it should be rewarded.

I am a bit confused by this. How did model B make the metamodel strictly better? The current MMC formula doesn’t implement about how the metamodel is affected by the user’s predictions. Also, why are you saying model A is random noise? How would you know that? Based on this premise, then we should punish model A even when the meta model is positive, but then why even care about originality? Also, this is an extreme example/case, realistically most models are within 0.3 to 0.95 corr with the meta model, so they are def not random noise. Yet in negative meta model rounds, the more you go towards 0.3 corr with the meta model, the lower your MMC scores becomes.

---

### Post #23 — **sdmlm** | 2020-08-02 20:58 UTC _(reply to #21)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png) master_key:

> Looking only at correlation_score and correlation_w_metamodel can be very misleading in this way. The current MMC approach corrects this though, and only rewards for real added unique information.

This is also confusing. The current MMC does not say anything about how the meta model behaves in relation to a user’s model. It only cares about how a user’s model behaves in relation to the meta model (very different things). Again, when the meta model is negative, the more unique you are the lower your MMC score. It doesn’t have to be 0 or negative corr with the meta model.

---

### Post #24 — **sdmlm** | 2020-08-02 21:02 UTC _(reply to #21)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png) master_key:

> Still, your code example highlights a different part of MMC design. It seems like this is really a case of it being a 1-P model, and that information gets removed by neutralization, just as submitting the metamodel itself would. You could also form a similar example where you submit exactly a negative version of the metamodel, and boom you have something SUPER ORIGINAL (-1 corr with metamodel), and also scored +0.05 instead of -0.05! In your encoded example, that unique model was actually worse than simply submitting a negative metamodel in its entirety. But that’s not really original, it’s just market timing with a signal we already have. I can see some argument for rewarding that, but it’s not what we wanted to accomplish with MMC. Corr will already reward that timing ability proportionally to its value.

My code example was just to illustrate the MMC formula and it’s behavior under negative meta model rounds. There are plenty of real model examples (not 1-p etc) on this forum and the chat where simply having lower (not negative just a bit lower) corr with the meta model but higher corr on target leads to a lower MMC score during meta model negative rounds.

---

### Post #25 — **lackofintelligence** | 2020-08-02 21:50 UTC _(reply to #21)_

> What you’re saying is we should reward this model A random noise because it looks unique and it did better than the metamodel. But it gave 100% unique information, and the result was negative. It should be punished. It made the metamodel strictly worse than it was before. Model B however made the metamodel strictly better, so it should be rewarded.

The only metric that you have for determining whether one model is strictly superior to another model is the correlation to the resolved scores. So if someone bets their bank on random noise, then it is because they believe that a strategy of random noise will be superior to any other strategy, especially in the context where we only report orderings and not magnitudes for our predictions, i.e., submitting random noise is the analogy of reducing the amplitude of predictions in the correlation to outcome context.

---

### Post #26 — **master_key** | 2020-08-02 22:01 UTC _(reply to #22)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/sdmlm/48/1152_2.png) sdmlm:

> Yet in negative meta model rounds, the more you go towards 0.3 corr with the meta model, the lower your MMC scores becomes.

This just isn’t necessarily true. For examples where you can find users who have lower corr_w_metamodel and lower MMC, you can also find users with lower corr_w_metamodel and higher MMC. It just depends on which way that independent vector faces with respect to the target.

If a model is very unique, but it’s still burning at the same time as the metamodel, why would we reward that model? A key point of MMC for us is finding signals which burn at different times. If your model is uncorrelated but burns at the same time as the metamodel, then it means that all of your uniqueness was for nothing ![:frowning:](https://emoji.discourse-cdn.com/twitter/frowning.png?v=13) . You just found a unique way to burn that no one else found. Not very helpful for us.

The problem with your analysis is you’re looking at the universe of users where  
They are unique  
AND there’s a burn period for the metamodel  
AND the user still burned at the same time too.

The truth is that if you are unique, in general, you are more likely to be OK in a burn period. If you are burning at the same time while being unique, then it means you may have just managed to isolate a part of the metamodel responsible for the burning, and the rest of your signal didn’t save you.

Take this data for round 218 showing users who have roughly 30% corr with metamodel.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/3fc9574d168309880c2213ddf828d56e2f22c7fa_2_332x250.png)image1012×760 55.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/3fc9574d168309880c2213ddf828d56e2f22c7fa.png> "image")

Then look at the data for round 218 showing users who have high corr with metamodel. Which group has better scores on average? Which group has higher MMC on average?  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/558bd6fe5c4a94b0a125e523b555f5f69fd78470_2_330x374.png)image1026×1164 86.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/558bd6fe5c4a94b0a125e523b555f5f69fd78470.png> "image")

It should be clear that in this burn round, it was not necessarily better or worse to be unique. It only matters what type of uniqueness you have, whether it’s good uniqueness or bad uniqueness.

Being more unique definitely allows for higher magnitudes of MMC, in either direction. But your direction is still influenced by the quality of your signal with respect to the target.

---

### Post #27 — **sdmlm** | 2020-08-03 06:47 UTC _(reply to #26)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png) master_key:

> This just isn’t necessarily true. For examples where you can find users who have lower corr_w_metamodel and lower MMC, you can also find users with lower corr_w_metamodel and higher MMC. It just depends on which way that independent vector faces with respect to the target.

This is not the problem here. The problem is that, during meta model burns, 2 models with the _**same**_ corr on target, one with lower corr_w_metamodel and one with higher corr_w_metamodel, the one with lower corr_w_metamodel will have lower MMC.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png) master_key:

> If a model is very unique, but it’s still burning at the same time as the metamodel, why would we reward that model? A key point of MMC for us is finding signals which burn at different times. If your model is uncorrelated but burns at the same time as the metamodel, then it means that all of your uniqueness was for nothing ![:frowning:](https://emoji.discourse-cdn.com/twitter/frowning.png?v=15) . You just found a unique way to burn that no one else found. Not very helpful for us.

There are numerous examples of models with **positive** corr on target and **negative** MMC during negative meta model rounds.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png) master_key:

> The problem with your analysis is you’re looking at the universe of users where  
>  They are unique  
>  AND there’s a burn period for the metamodel  
>  AND the user still burned at the same time too.

Again the user doesn’t have to burn for this to happen and they also don’t have to be unique, the problem is that MMC is an increasing function of corr with the meta model during negative meta model rounds.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png) master_key:

> The truth is that if you are unique, in general, you are more likely to be OK in a burn period. If you are burning at the same time while being unique, then it means you may have just managed to isolate a part of the metamodel responsible for the burning, and the rest of your signal didn’t save you.
> 
> Take this data for round 218 showing users who have roughly 30% corr with metamodel.
> 
> [![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/3fc9574d168309880c2213ddf828d56e2f22c7fa.png)image1012×760 55.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/3fc9574d168309880c2213ddf828d56e2f22c7fa.png> "image")
> 
> Then look at the data for round 218 showing users who have high corr with metamodel. Which group has better scores on average? Which group has higher MMC on average?
> 
> [![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/558bd6fe5c4a94b0a125e523b555f5f69fd78470_2_440x499.png)image1026×1164 86.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/558bd6fe5c4a94b0a125e523b555f5f69fd78470.png> "image")

The data you posted actually proves my point.

As shown by previous forum posts and by [@lackofintelligence](</u/lackofintelligence>) mathematical note, MMC = CORR_user - CORR_WITH_METAMODEL * CORR_META_MODEL_ON_TARGET. Looking at this it is clear that MMC will increase with CORR_user , but decrease with CORR_WITH_METAMODEL .

**From the data you posted for round 218:**  
**user sunkay: -1% corr_target, 91% corr with meta model, 1.59% MMC**  
**user souryuu: 0.25% corr_target, 31% corr with meta model, 1.33% MMC**

As you can see, we gave user sunkay a larger MMC even though user souryuu has much **better, positive corr on target.**

Again, it is mathematically proven that ****MMC = CORR_user - CORR_WITH_METAMODEL * CORR_META_MODEL_ON_TARGET**. Meaning that the users with low CORR_WITH_METAMODEL from your example data got MMC due to higher CORR_user, which offset the loss from CORR_WITH_METAMODEL * CORR_META_MODEL_ON_TARGET.**

In any case, I think I’ve basically exhausted all possible arguments/examples I could give.

In the end it is what it is.

I really enjoy this tournament and have really tried my absolute best to improve it by trying my hardest to identify and explain this problem and ways to fix it.

If other users want to contribute to this please feel free, but I don’t think there’s anything else I could say on the matter.

---

### Post #28 — **lackofintelligence** | 2020-08-03 08:20 UTC

For this data, what you should be looking at is the differences between MMC and CORR in relation to the correlation with the meta model. Let’s pick two points and compare. For purple who has the most unique model shown, the difference between MMC and CORR = 0.057 - 0.042 = 0.015. For the least unique model shown, rehoboam, the difference is -0.00555 - -0.02777 = 0.02222. So rehoboam is rewarded much more solely for being more like the meta model, which makes no sense as usual, especially since purple has a much better model in this round. All of this data seems to follow this trend except for a couple of outliers that suggest some other kind of oddities in this data.

---

### Post #29 — **jackerparker** | 2020-08-03 09:45 UTC _(reply to #28)_

There is almost no sense to compare correlation with the meta model between users. You can split your predictions into two parts - most confident and least confident, reverse the latter one and as the result - significant drop in correlation with meta model and almost the same correlation with real target. And the MMC right now exactly represents a “useful uniqueness” your model have.

Another example for the situation discussed in the beginning of this post: Users 1-5 have unique models with -0.01 Corr and 0 corr with MM. MM is based on these 5 predictions and results in -0.05 Corr.  
User 6 has a model which is staked models from User 1-4 with -0.04 Corr and 80% corr with MM.  
In the current MMC calculation system, Users 1-5 will get negative MMC values and User 6 will get high positive MMC. And all of that just sounds right.

---

### Post #30 — **jackerparker** | 2020-08-04 09:10 UTC

There was feedback in the private messages which forced me to clarify my statements.

I believe that we cannot use any live data results as any justification of the theory discussed above. My point is that correlation with MetaModel is a completely wrong metric for model uniqueness. There are 4 example models in the attached code (based on the sdmlm’s code). First one is MM with -0.055 CORR performance . Second one is a true unique model with -0.036 CORR performance, 41% corr with MM, -0.066 MMC and -0.03 MMC-CORR value. The third one is a noisy “unique” model with -0.03 CORR performance, 43% corr with MM, -0.15 MMC and -0.12 MMC-CORR value. By the term noisy model I mean here that correlation was reduced mostly using part of predictions which does not correlate with target values. And the last, fourth model is highly correlated which is basically a noisy “unique” model with less artificial shuffles of predictions which does not correlate with target values. It has the same -0.03 CORR, 65% corr with MM, -0.075 MMC and -0.044 MMC-CORR value. So, truly unique model have the highest MMC and MMC-CORR metrics despite the worst raw CORR performance. Highest correlation model has better MMC and MMC-CORR metrics than noisy unique model. Both results provide me with the feeling that current MMC implementation is totally fine. And this “So rehoboam is rewarded much more solely for being more like the meta model, which makes no sense as usual, especially since purple has a much better model in this round. All of this data seems to follow this trend except for a couple of outliers that suggest some other kind of oddities in this data.” can be just explained by most of “unique” models in live data are fulfilled with a noise except “the couple of outliers” which are truly unique and useful models.

The only thing which makes me feel slightly less confident in my example is using 0.3 value in low_meta_corr_model array. So, any comments about that are appreciated.

Regards,  
Mark
    
    
    import numpy as np
    import pandas
    import scipy.stats
    
    def spearmanr(target, pred):
        return np.corrcoef(
            target,
            pred.rank(pct=True, method="first")
        )[0, 1]
    
    def neutralize_series(series, by, proportion=1.0):
       scores = series.values.reshape(-1, 1)
       exposures = by.values.reshape(-1, 1)
    
       # this line makes series neutral to a constant column so that it's centered and for sure gets corr 0 with exposures
       exposures = np.hstack(
           (exposures, np.array([np.mean(series)] * len(exposures)).reshape(-1, 1)))
    
       correction = proportion * (exposures.dot(
           np.linalg.lstsq(exposures, scores)[0]))
       corrected_scores = scores - correction
       neutralized = pandas.Series(corrected_scores.ravel(), index=series.index)
       return neutralized
    
    def _normalize_unif(df):
        X = (df.rank(method="first") - 0.5) / len(df)
        return scipy.stats.uniform.ppf(X)
    
    target = pandas.Series([0, 0, 0, 0,
              0.25, 0.25, 0.25, 0.25,
              0.5, 0.5, 0.5, 0.5,
              0.75, 0.75, 0.75, 0.75,
              1, 1, 1, 1])
    
    meta_model = pandas.Series([1, 0, 0.25,
                  1, 0.5, 0.75,
                  0.5, 0.5, 1,
                  0.75, 0.75, 0,
                  0, 0.25, 0.25,
                  1, 0, 0.25, 0.5, 0.75])
         
    high_meta_corr_model = pandas.Series([1, 0, 0.25,
                  1, 0.75, 0.5,
                  0.5, 0.5, 0.75,
                  0.75, 1, 0,
                  0, 0.25, 0.25,
                  0.75, 0.5, 1.0, 0.0, 0.25])
    
    low_meta_corr_model = pandas.Series([0.3, 0.5, 0.75,
                  1, 0.5, 0.75,
                  0, 0, 1,
                  0.75, 0.75, 0,
                  0.25, 0.25, 0.5,
                  1, 1, 0, 0.25, 0.25])
    
    low_meta_corr_model_noise = pandas.Series([0.25, 0, 1,
                  1, 0.75, 0.5,
                  0.5, 0.5, 0.75,
                  0.75, 1, 0,
                  0, 0.25, 0.25,
                  0.75, 0.5, 1.0, 0.0, 0.25])
       
    # Meta model has raw corr with target of -5.5% (burning period)
    meta_model_raw_perf = spearmanr(target, meta_model)
    print(f"Meta_model performance: {meta_model_raw_perf}")
    
    high_meta_corr_raw_perf = spearmanr(target, high_meta_corr_model)
    high_meta_corr = spearmanr(meta_model, high_meta_corr_model)
    
    print(f"High_meta_corr model cross-corr: {spearmanr(meta_model, high_meta_corr_model)}")
    print(f"High_meta_corr model performance: {high_meta_corr_raw_perf}")
    
    
    low_meta_corr_raw_perf = spearmanr(target, low_meta_corr_model)
    low_meta_corr = spearmanr(meta_model, low_meta_corr_model)
    
    print(f"Low_meta_corr model cross-corr: {spearmanr(meta_model, low_meta_corr_model)}")
    print(f"Low_meta_corr model performance: {low_meta_corr_raw_perf}")
    
    
    low_meta_corr_raw_perf_noise = spearmanr(target, low_meta_corr_model_noise)
    low_meta_corr_noise = spearmanr(meta_model, low_meta_corr_model_noise)
    
    print(f"Low_meta_corr_noise model cross-corr: {spearmanr(meta_model, low_meta_corr_model_noise)}")
    print(f"Low_meta_corr_noise model performance: {low_meta_corr_raw_perf_noise}")
    
    
    # MMC Computation
    # All series are already uniform
    
    # Neutralize (using forum post code for neutralization)
    neutralized_high_corr = neutralize_series(high_meta_corr_model, meta_model, proportion=1.0)
    neutralized_low_corr = neutralize_series(low_meta_corr_model, meta_model, proportion=1.0)
    neutralized_low_corr_noise = neutralize_series(low_meta_corr_model_noise, meta_model, proportion=1.0)
    
    
    # Compute MMC
    mmc_high_corr = np.cov(target, 
                                neutralized_high_corr)[0,1]/(0.29**2)
    
    mmc_low_corr = np.cov(target, 
                                neutralized_low_corr)[0,1]/(0.29**2)
    
    mmc_low_corr_noise = np.cov(target, 
                                neutralized_low_corr_noise)[0,1]/(0.29**2)
    
    print(f"MMC for non-original model: {mmc_high_corr}")
    print(f"MMC for original model: {mmc_low_corr}")
    print(f"MMC for original noise model: {mmc_low_corr_noise}")
    
    
    print(f"MMC-CORR for non-original model: {mmc_high_corr-high_meta_corr_raw_perf}")
    print(f"MMC-CORR for original model: {mmc_low_corr-low_meta_corr_raw_perf}")
    print(f"MMC-CORR for original noise model: {mmc_low_corr_noise-low_meta_corr_raw_perf_noise}")
    
    Meta_model performance: -0.05518254055364692
    High_meta_corr model cross-corr: 0.6560590932489134
    High_meta_corr model performance: -0.030656966974248294
    Low_meta_corr model cross-corr: 0.4169347508497767
    Low_meta_corr model performance: -0.03678836036909795
    Low_meta_corr_noise model cross-corr: 0.4353289310343258
    Low_meta_corr_noise model performance: -0.030656966974248308
    MMC for non-original model: -0.07529413605357009
    MMC for original model: -0.06688466111771676
    MMC for original noise model: -0.15449965579823513
    MMC-CORR for non-original model: -0.044637169079321797
    MMC-CORR for original model: -0.030096300748618812
    MMC-CORR for original noise model: -0.12384268882398683

---

### Post #31 — **sdmlm** | 2020-08-04 09:55 UTC _(reply to #30)_

[@jackerparker](</u/jackerparker>) you didn’t transform the predictions to standard uniform (my original example were at least discretely uniform). By making them standard uniform at the start of the code, you get vastly different results.  
Basically just add this right after creating your predictions:

target = pandas.Series(_normalize_unif(target))  
meta_model = pandas.Series(_normalize_unif(meta_model))  
high_meta_corr_model = pandas.Series(_normalize_unif(high_meta_corr_model))  
low_meta_corr_model = pandas.Series(_normalize_unif(low_meta_corr_model))  
low_meta_corr_model_noise = pandas.Series(_normalize_unif(low_meta_corr_model_noise))

MMC-CORR for non-original model is the highest MMC-CORR…
    
    
    import numpy as np
    import pandas
    import scipy.stats
    
    def spearmanr(target, pred):
    return np.corrcoef(
        target,
        pred.rank(pct=True, method="first")
    )[0, 1]
    
    def neutralize_series(series, by, proportion=1.0):
       scores = series.values.reshape(-1, 1)
       exposures = by.values.reshape(-1, 1)
    
       # this line makes series neutral to a constant column so that it's centered and for sure gets corr 0 with exposures
       exposures = np.hstack(
       (exposures, np.array([np.mean(series)] * len(exposures)).reshape(-1, 1)))
    
       correction = proportion * (exposures.dot(
       np.linalg.lstsq(exposures, scores)[0]))
       corrected_scores = scores - correction
       neutralized = pandas.Series(corrected_scores.ravel(), index=series.index)
       return neutralized
    
    def _normalize_unif(df):
    X = (df.rank(method="first") - 0.5) / len(df)
    return scipy.stats.uniform.ppf(X)
    
    target = pandas.Series([0, 0, 0, 0,
          0.25, 0.25, 0.25, 0.25,
          0.5, 0.5, 0.5, 0.5,
          0.75, 0.75, 0.75, 0.75,
          1, 1, 1, 1])
    
    meta_model = pandas.Series([1, 0, 0.25,
              1, 0.5, 0.75,
              0.5, 0.5, 1,
              0.75, 0.75, 0,
              0, 0.25, 0.25,
              1, 0, 0.25, 0.5, 0.75])
     
    high_meta_corr_model = pandas.Series([1, 0, 0.25,
              1, 0.75, 0.5,
              0.5, 0.5, 0.75,
              0.75, 1, 0,
              0, 0.25, 0.25,
              0.75, 0.5, 1.0, 0.0, 0.25])
    
    low_meta_corr_model = pandas.Series([0.3, 0.5, 0.75,
              1, 0.5, 0.75,
              0, 0, 1,
              0.75, 0.75, 0,
              0.25, 0.25, 0.5,
              1, 1, 0, 0.25, 0.25])
    
    low_meta_corr_model_noise = pandas.Series([0.25, 0, 1,
              1, 0.75, 0.5,
              0.5, 0.5, 0.75,
              0.75, 1, 0,
              0, 0.25, 0.25,
              0.75, 0.5, 1.0, 0.0, 0.25])
    
    
    # Make uniform
    target = pandas.Series(_normalize_unif(target))
    meta_model = pandas.Series(_normalize_unif(meta_model))
    high_meta_corr_model = pandas.Series(_normalize_unif(high_meta_corr_model))
    low_meta_corr_model = pandas.Series(_normalize_unif(low_meta_corr_model))
    low_meta_corr_model_noise = pandas.Series(_normalize_unif(low_meta_corr_model_noise))
    
       
    # Meta model has raw corr with target of -1.5% (burning period)
    meta_model_raw_perf = spearmanr(target, meta_model)
    print(f"Meta_model performance: {meta_model_raw_perf}")
    
    high_meta_corr_raw_perf = spearmanr(target, high_meta_corr_model)
    high_meta_corr = spearmanr(meta_model, high_meta_corr_model)
    
    print(f"High_meta_corr model cross-corr: {spearmanr(meta_model, high_meta_corr_model)}")
    print(f"High_meta_corr model performance: {high_meta_corr_raw_perf}")
    
    
    low_meta_corr_raw_perf = spearmanr(target, low_meta_corr_model)
    low_meta_corr = spearmanr(meta_model, low_meta_corr_model)
    
    print(f"Low_meta_corr model cross-corr: {spearmanr(meta_model, low_meta_corr_model)}")
    print(f"Low_meta_corr model performance: {low_meta_corr_raw_perf}")
    
    
    low_meta_corr_raw_perf_noise = spearmanr(target, low_meta_corr_model_noise)
    low_meta_corr_noise = spearmanr(meta_model, low_meta_corr_model_noise)
    
    print(f"Low_meta_corr_noise model cross-corr: {spearmanr(meta_model, low_meta_corr_model_noise)}")
    print(f"Low_meta_corr_noise model performance: {low_meta_corr_raw_perf_noise}")
    
    
    # MMC Computation
    # All series are already uniform
    
    # Neutralize (using forum post code for neutralization)
    neutralized_high_corr = pandas.Series(neutralize_series(high_meta_corr_model, meta_model, proportion=1.0))
    neutralized_low_corr = pandas.Series(neutralize_series(low_meta_corr_model, meta_model, proportion=1.0))
    neutralized_low_corr_noise = pandas.Series(neutralize_series(low_meta_corr_model_noise, meta_model, proportion=1.0))
    
    
    # Compute MMC
    mmc_high_corr = np.cov(target, 
                            neutralized_high_corr)[0,1]/(0.29**2)
    
    mmc_low_corr = np.cov(target, 
                            neutralized_low_corr)[0,1]/(0.29**2)
    
    mmc_low_corr_noise = np.cov(target, 
                            neutralized_low_corr_noise)[0,1]/(0.29**2)
    
    print(f"MMC for non-original model: {mmc_high_corr}")
    print(f"MMC for original model: {mmc_low_corr}")
    print(f"MMC for original noise model: {mmc_low_corr_noise}")
    
    
    print(f"MMC-CORR for non-original model: {mmc_high_corr-high_meta_corr_raw_perf}")
    print(f"MMC-CORR for original model: {mmc_low_corr-low_meta_corr_raw_perf}")
    print(f"MMC-CORR for original noise model: {mmc_low_corr_noise-low_meta_corr_raw_perf_noise}")
    
    
    Meta_model performance: -0.01503759398496236
    High_meta_corr model cross-corr: 0.6796992481203005
    High_meta_corr model performance: -0.04360902255639097
    Low_meta_corr model cross-corr: 0.4195488721804511
    Low_meta_corr model performance: -0.06766917293233085
    Low_meta_corr_noise model cross-corr: 0.463157894736842
    Low_meta_corr_noise model performance: -0.007518796992481184
    MMC for non-original model: -0.034737792600909013
    MMC for original model: -0.06384083997464719
    MMC for original noise model: -0.0005764144386876333
    MMC-CORR for non-original model: 0.008871229955481959
    MMC-CORR for original model: 0.0038283329576836583
    MMC-CORR for original noise model: 0.006942382553793551

---

### Post #32 — **of_s** | 2021-08-22 20:03 UTC

Where, how and more importantly why was it simply assumed that a unique model is random noise?

---

### Post #33 — **of_s** | 2021-09-06 17:39 UTC _(reply to #32)_

Related new discussion on RC:

![](https://community.numer.ai/channel/random/assets/favicon_16.png) [community.numer.ai](<https://community.numer.ai/channel/random?msg=YYHvRHhEsJWbSZQCd>) ![](https://community.numer.ai/channel/random/assets/favicon_512.png)

### [Numerai Community](<https://community.numer.ai/channel/random?msg=YYHvRHhEsJWbSZQCd>)
