---
title: "Better neutralization?"
category: Data Science
url: https://forum.numer.ai/t/better-neutralization/4132
created_at: 2021-09-16T07:11:36.757000+00:00
last_posted_at: 2022-07-23T03:55:53.857000+00:00
posts_count: 7
views: 2421
tags: []
---

# Better neutralization?

---

### Post #1 — **nyuton** | 2021-09-16 07:11 UTC

Hi,

I’ve tested full neutralization on many of my models, but it never did the trick. Performance suffered.  
Which kind of makes sense. Removing linear dependency from all features should result in performance drop.

The new example model brings neutralization to the next level, by neutralizing only on risky features. With features, where the correlation with the target changes the most. This is a more reasonable approach, with hopefully better result. Still it removes linear dependencies from 50 features.

An improvement would be to neutralize only, if

  * a feature is in the “risky” group (changing correlation with the target thorugh eras)
  * the feature has exposure (high correlation with the target in the live era)



This method further cuts down on neutralization focusing only on cutting feature exposure, where it is necessary for long term performance.

An implementation of this method would look like this:
    
    
    all_feature_corrs = training_data.groupby('erano').apply( lambda d: d[features].corrwith(d['target']))
    riskiest_features = get_biggest_change_features(all_feature_corrs, 50)  
    
    feature_corrs = predict_data[predict_data.era=='eraX'].apply(lambda d: 
     [features].corrwith(d['prediction_sum'])).abs()
    feature_corrs_max = feature_corrs.max()
    feature_corrs_mean = feature_corrs.max().mean()
            
    to_neutralize = feature_corrs_max[riskiest_features].sort_values()
    to_neutralize = to_neutralize[to_neutralize>feature_corrs_mean].index.to_list()
            
    predict_data["prediction"] = neutralize(
                df=predict_data,
                columns=["prediction"],
                neutralizers=to_neutralize,
                proportion=0.5,
                normalize=True)["prediction"]
    

What’s you intuition on this?

---

### Post #2 — **lackofintelligence** | 2021-09-16 23:30 UTC

I think its a great idea.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nyuton/48/687_2.png) nyuton:

> An improvement would be to neutralize only, if
> 
>   * a feature is in the “risky” group (changing correlation with the target thorugh eras)
>   * the feature has exposure (high correlation with the target in the live era)
> 


How do you determine the 2nd point? You don’t have live correlations when estimating the exposure on live predictions. Also, could you elaborate on your function below? E.g., are you sorting by standard deviation of the correlations?

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nyuton/48/687_2.png) nyuton:

> 
>     riskiest_features = get_biggest_change_features(all_feature_corrs, 50)  
>     

OTOH, could it be that riskier features are those that historically show little variation in the historical data but then suddenly change orientation in the live data?

---

### Post #3 — **mdo** | 2021-09-17 03:58 UTC

There’s a similar idea near the end of: <https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb>

---

### Post #4 — **nyuton** | 2021-09-17 11:32 UTC _(reply to #2)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/lackofintelligence/48/774_2.png) lackofintelligence:

> How do you determine the 2nd point?

Sorry, I meant high correlation with the prediction in the live era.  
We don’t have targets obviously.

I guess it’s enough to neutralize on features, which has high effect (high correlation) on the predictions.  
I’m not 100% sure of this idea, but I’ll submit and see.

Feedback is welcome ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #5 — **nyuton** | 2021-09-17 11:33 UTC _(reply to #2)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/lackofintelligence/48/774_2.png) lackofintelligence:

> riskier features are those that historically show little variation in the historical data but then suddenly change orientation in the live data?

“get_biggest_change_features” here is the same function what you see in the advanced example script.

---

### Post #6 — **nyuton** | 2021-09-17 11:39 UTC _(reply to #4)_

Feature importance would be even better!

Neutralize to features, which

  * are risky (changing correlation with the target through eras)
  * have high feature importance in the model



If an unimportant feature changes correlation with the target, it won’t effect predictions much anyway.

I’m just trying to find ways to minimize the side effect of neutralization.  
Neutralization is a great tool, but neutralizing everything kills the model.

---

### Post #7 — **jmrichardson** | 2022-07-23 03:55 UTC _(reply to #6)_

Perhaps the intersection of:

  * Risky: Top quantile of STDev correlation
  * High Importance: Top quantile of mean correlation


    
    
    def get_biggest_change_features(corrs, n, q=.75):
        corrs_mean = corrs.mean().abs().sort_values(ascending=False)
        quantile = np.quantile(corrs_mean, q=q)
        corrs_mean_q = corrs_mean[corrs_mean >= quantile]
        corrs_std = corrs.std().sort_values(ascending=False)
        quantile = np.quantile(corrs_std, q=q)
        corrs_std_q = corrs_std[corrs_std >= quantile]
        worst_n = corrs_mean_q[corrs_mean_q.index.isin(corrs_std_q.index)].index.tolist()
        return worst_n
