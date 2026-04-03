---
title: "Feature Request – Publish Metamodel Feature Exposures"
category: Tournament
url: https://forum.numer.ai/t/feature-request-publish-metamodel-feature-exposures/3523
created_at: 2021-06-04T04:10:30.276000+00:00
last_posted_at: 2021-06-10T10:04:15.009000+00:00
posts_count: 8
views: 1258
tags: []
---

# Feature Request – Publish Metamodel Feature Exposures

---

### Post #1 — **jacob_stahl** | 2021-06-04 04:10 UTC

MMC provides a strong incentive for users to create unique models that are orthogonal to the metamodel. More diverse predictions create a better ensemble which is good for the fund. Instead of relying on incentive structures alone to increase model diversity, Numerai should publish more information that users can use to make models more orthagonal to the metamodel.

I propose that Numerai publishes the feature exposures of the metamodel after every round. If a user knows what features the metamodel is likely to be exposed to in the next round, MMC would incentivize them to make a model that doesn’t have those same exposures. If enough staked models do this, the meta model would then be less exposed than it was in the previous round. Over time the feature exposure of the metamodel itself would fall considerably, and be less vulnerable to severe burns _cries in round 260_.

There is also a steep learning curve for this tournament and we should make it as easy as possible for new users start making good models. I think giving everyone more information that can easily be used to make better models can help with this.

I tried to think of ways this could be gamed to harm the tournament but I can’t think of any.

more on feature exposure: [jrb’s post on feature exposure](<http://forum.numer.ai/t/model-diagnostics-feature-exposure/899>)

  * Good idea
  * Perhaps
  * I see a problem



0 voters

---

### Post #2 — **mesozoicmetallurgist** | 2021-06-06 22:12 UTC

I like the idea of providing more data and information about the metamodel to users, but I believe that the proposed methods may have some drawbacks.

If each week we are provided the exposures of the meta-model from the previous round, then if people are trying to change their models accordingly, it may cause the meta-model to become more volatile, as each week people are trying to optimize on changes from the previous week, creating a constantly moving target.

This also makes the assumption that the meta-model’s feature exposure isn’t an integral part of its performance. We don’t have round performance for the meta-model, so we have no way of knowing whether it burned in round 260, or if linear exposure was the culprit. If we were provided a full model page for the meta-model, then we could compare its fnc to its corr to get a sense of whether a particular round’s feature exposures matter or not, but this wouldn’t solve the problem of a feedback moving target.

I think a better idea would be providing a snapshot of the meta-model predictions alongside training and validation data (not for test or live as it is a snapshot). This snapshot would not change over time, although potentially a new snapshot of it could be provided at a future point in time. This would provide us information on how the meta-model does in comparison to our models, as well as the opportunity to use it in the creation of our models. I imagine doing something like neutralizing the meta-model snapshot to the target, and then attempting to reduce correlation to the leftover component during training. Or, you could setup the problem as how do I build a model that always improves the meta-model when ensembled together with it.  
I think that since this would be provided for the model building process rather as a post-processing effect, it would incentivize people to create good long-term unique models that improve the meta-model, rather than short term adjustments chasing weekly changes in the meta-model.

---

### Post #3 — **jacob_stahl** | 2021-06-07 04:36 UTC _(reply to #2)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/mesozoicmetallurgist/48/2477_2.png) mesozoicmetallurgist:

> If each week we are provided the exposures of the meta-model from the previous round, then if people are trying to change their models accordingly, it may cause the meta-model to become more volatile, as each week people are trying to optimize on changes from the previous week, creating a constantly moving target.

I think this might cause some instability initially. If staked modelers only had a few rounds of feature exposures to go by, they would be playing a game of feature exposure whack-a-mole. But I suspect that this would reach an equilibrium eventually.  
Lets say the metamodel is exposed to feature A. Knowing this, many staked modelers would neutralize their predictions to feature A to increase MMC. Does that mean that the vast majority of these new predictions would then be exposed to a different feature B? Or would different types of models develop new exposures to a variety of features? If that’s the case then we should expect the new meta model exposures to get smaller over time. Over time this should keep the metamodel very feature neutral and reduce risk.

If additional dampening is needed maybe there could be a 2-3 round delay before exposures are released.

---

### Post #4 — **mesozoicmetallurgist** | 2021-06-07 18:30 UTC _(reply to #3)_

I think I misinterpreted how this would work initially. The way I understand neutralization to work, it wouldn’t really make sense that neutralizing against the meta-model’s exposure to increase any linear exposure. I still think there may be some whack-a-mole, but overall it would end up reducing the feature exposure of the meta-model if users used it for neutralization.

Although, users can already neutralize by the features to zero out feature exposure. Having the meta-model exposures for a given round would only help if we also knew the corr/mmc for those features for the round (such as [numer.ai/i3](<https://numer.ai/i3>) for each feature), as then we could ascertain whether it was good or not that the meta-model had exposure.  
I suppose they could also simply release the predictions of the meta-model each round, but I’m not sure that is such a good idea, and since releasing feature exposure is effectively releasing a linear model component of the meta-model it brings the same reservations.

To that effect, I still think a better move would be to release a meta-model snapshot with training/validation data. Releasing data on a weekly basis can lead to short-term bias. If the meta is exposed to some features one week, we can’t be sure that the same features will matter the next week, and if being feature neutral was the goal, then we can just neutralize to the features in the first place without observing the meta-model. It is also likely that some features that the meta are exposed to are actually good, and thus neutralizing out may hurt corr/mmc, and we would not know unless we also know the corr/mmc of the features.

To be clear I would love any sort of new data about the meta-model to integrate, and I would absolutely dive into trying to use meta exposures in my models, but I would prefer something that I build into my models from the get-go in training rather than a post-processing effect.

---

### Post #5 — **jacob_stahl** | 2021-06-07 23:05 UTC _(reply to #4)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/mesozoicmetallurgist/48/2477_2.png) mesozoicmetallurgist:

> To be clear I would love any sort of new data about the meta-model to integrate, and I would absolutely dive into trying to use meta exposures in my models, but I would prefer something that I build into my models from the get-go in training rather than a post-processing effect.

It doesn’t have to be a post processing effect. Suppose you had 20 rounds of meta exposures that tell you what features the metamodel is likely have a high OR low exposure too. This would be a powerful tool for feature selection as well.

---

### Post #6 — **chaotician** | 2021-06-09 23:37 UTC

This concept of feature neutralization for extracting uncorrelated alphas was already experimented with in another crowd sourcing site that folded last year. I know it failed for several reasons, 1) as meso mentioned this is a post processing scheme 2) it assumes the data is stationary, which it is not and 3) it invites gaming through optimization which leads to overfitting. I’d prefer the alphas to flow naturally with the chosen features and prediction models. And as it is a prediction model, consistency and accuracy in generalization are still the prime drivers, not ‘seemlingly sophisticated’ processes based on the wrong assumptions.

---

### Post #7 — **jacob_stahl** | 2021-06-10 04:17 UTC _(reply to #6)_

1. As I mentioned above, It can be used for post processing but it doesn’t have to be. Is there a specific reason why this is a bug?

  2. It is safe to assume that feature exposures would be roughly constant. the training and validation set don’t change. The live data is NOT however. this is why it is important to have feature neutral models that are less affected by this change.

  3. Knowledge of the meta model feature exposures allows users to make their models more orthogonal to the meta model. This is rewarded with MMC which they optimize for. Would ensambling many less correlated models result in overfitting or would it have a regularization effect?

---

### Post #8 — **chaotician** | 2021-06-10 10:04 UTC _(reply to #7)_

Not using it as a post processing scheme is IMO the proper way to utilize meta model feature exposures, just as a metric. The problem here is when you incorporate data from the past, in this case, meta model feature exposures into your model in an effort to try extract uniqueness of alpha vis a vis the meta model, you are introducing an additional constraint in your optimization process that limits your search parameters to focus on neutralizing feature exposures which muddles the natural churn of your model thus often leads to overfitting. You are also assuming meta model feature exposures will be persistant in the near future, it may or may not.
