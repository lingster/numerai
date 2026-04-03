---
title: "Revolutionizing Staking: Aligning Users and the Fund Through Unique Models"
category: Tournament
url: https://forum.numer.ai/t/revolutionizing-staking-aligning-users-and-the-fund-through-unique-models/7916
created_at: 2025-01-25T18:05:23.764000+00:00
last_posted_at: 2025-01-27T20:59:08.524000+00:00
posts_count: 5
views: 541
tags: []
---

# Revolutionizing Staking: Aligning Users and the Fund Through Unique Models

---

### Post #1 — **jefferythewind** | 2025-01-25 18:05 UTC

Hey everyone,

I’ve been thinking a lot about how we can improve the staking mechanism in Numerai to better align with the goals of both the fund and its users. The crux of my argument is this: **staking should always benefit both the user and the fund.**

This isn’t a radical idea. In the broader crypto world, staking ETH or other tokens often serves two purposes: it rewards the user for locking their assets, and it directly contributes to the functionality of the system. Staking in Numerai should work the same way—not just as a tool for data scientists (DSs), but as a mechanism that improves the Meta Model by encouraging broader participation.

* * *

### The Problem With Example Models

Right now, the system allows users to stake on example models, which creates a few issues:

  1. **No Unique Contribution** : When everyone stakes on the same example model, it provides little to no additional value to the fund.
  2. **No Real Incentive for Non-DS Stakers** : If staking example models neither benefits the Meta Model nor offers unique opportunities for users, it’s hard to justify staking for non-DS participants.



The result? A system that doesn’t take full advantage of staking’s potential to improve the Meta Model while engaging a wider audience.

* * *

### A Better Staking Paradigm: Randomized Grid Models

Here’s an alternative: **a system that generates unique, high-correlation models for every staker through a randomized grid search.** Here’s how it could work:

  * **Generic Staking:** Instead of staking on example models, users stake their NMR to generate a random, well-performing model on the validation set.
  * **Unique Contributions:** Each staker’s model would be unique, meaning every stake contributes a new signal to the Meta Model.
  * **Aligned Incentives:** The better the signal, the better the payout for the user. This directly aligns user rewards with the Meta Model’s performance.
  * **Risk and Opportunity:** Users could hedge their per-model risk by staking on a variety of randomized models, much like a diversified portfolio. This benefits the fund by delivering more unique signals and benefits users by increasing their chances of higher payouts.



* * *

### Staking as Signal Mining: The Pipeline for Randomized Models

I can provide the pipeline to implement this idea effectively, giving every staker a unique, randomized high-correlation model. Here’s the hyperparameter grid I typically use for generating models:

python

CopyEdit
    
    
    param_dict = {
        'colsample_bytree': list(np.linspace(0.001, 1, 100)), 
        'reg_lambda': list(np.linspace(0, 100_000, 10_000)),
        'learning_rate': list(np.linspace(.00001, 1.0, 1000)),
        'max_bin': list(np.linspace(2, 5, 4, dtype='int')),
        'max_depth': list(np.linspace(2, 12, 11, dtype='int')),
        'num_leaves': list(np.linspace(2, 24, 15, dtype='int')),
        'min_child_samples': list(np.linspace(1, 250, 250, dtype='int')),
        'n_estimators': list(np.linspace(100, 25_000, 24_000, dtype='int')),
        'target': targets,  # User-specified target values
    }
    

Using this grid, we can compute the total number of unique hyperparameter combinations:

  * **Total Combinations** = 100×10,000×1,000×4×11×15×250×24,000=39,600,000,000,000,000100 \times 10,000 \times 1,000 \times 4 \times 11 \times 15 \times 250 \times 24,000 = 39,600,000,000,000,000100×10,000×1,000×4×11×15×250×24,000=39,600,000,000,000,000  
Yes, you read that right: trillions of potential unique models! With this massive space, every staker could generate a completely unique model, even if we scale up participation dramatically.



* * *

### Why This Is Better

  1. **For the Fund** : Instead of everyone staking on the same model, the Meta Model gains from a diverse set of unique signals. This improves the overall performance and robustness of the Meta Model.
  2. **For the Users** : Generic stakers—who may not be data scientists—can now contribute meaningfully to the system and have a fair chance to earn rewards based on their contribution.
  3. **For the Ecosystem** : It incentivizes participation from a broader audience, fostering growth and sustainability for Numerai.



This system represents a huge improvement over the current example model setup, where staking on one shared model offers no real benefit to either the staker or the fund.

* * *

### Call for Feedback

I’d love to hear your thoughts on this idea. I can share code and examples to demonstrate how this system works, why scaling the number of random models consistently improves ensemble performance out-of-sample, and why models generated through this process are likely to maintain strong performance in the future.

How else can we maximize the potential of staking to benefit both users and the Meta Model? Let’s collaborate and unlock the full potential of staking for Numerai.

---

### Post #2 — **joakim** | 2025-01-26 06:04 UTC

I quite like the idea. However, I’m sceptical that random signals would add anything useful to the meta model. Unique doesn’t necessarily mean good (or additive) unfortunately. The most optimal combinations of these hyper parameters would already have been found I suspect and included in the SWMM, so any sub-optimal ones would either have 0 or negative MMC. Perhaps by luck, one could find a few models that would actually be additive, but most of them would not I fear, even if they have positive CORR. Unless the random search would continue until a model with consistently positive BMC/MMC on validation was found, then maybe… I still think most of those would already be included in the MM, though perhaps with less than optimal NMR staked, and anyone with existing similar models would then see their MMC get diluted. Not so good for existing (good) users.

---

### Post #3 — **foolish_observer** | 2025-01-26 18:49 UTC

Is this not what is supposed to be achieved through MMC?  
Also I assume most people would not like to stake on a random model? Besides, with this param_dict you are just performing grid search over xgboost parameters. Most of the resulting models will still be highly correlated also because they are subject to the same eras. So " trillions of potential unique models!" does not hold. Maybe i did not get what you are suggesting then I apologize.

---

### Post #4 — **jefferythewind** | 2025-01-27 14:36 UTC _(reply to #3)_

It is correct to be skeptical. You’ve also touched on additional ways to differentiate and add a larger pool to our model farm: dropping eras. Along with that is potentially dropping features. One thing to notice is that unique doesn’t mean orthogonal.

Yes this idea should play nicely with ideas behind MMC. The point is that a random staker now only has a known set of models to choose from (example models or numerbay), they don’t add any new signal at all by coming to this project and staking. So what I’m suggesting is that there may be a way to essentially give random stakers completely unique new models to stake on. This kinda gives a win-win to both the fund and the random stakers.

I hope also by open sourcing this idea it could lead some extensions and discoveries.

---

### Post #5 — **wigglemuse** | 2025-01-27 20:59 UTC

I very much doubt Numerai is going to pick up this idea anytime soon, which means what you’re really talking about is basically a more open Crowdcent where a pool is created for earning without model-making, and Numerai gets some more diversity (maybe). If we just created a protocol/script where people could contribute compute (“run a node”) or maybe just pay a fee and provide an API key then it would create these models and upload them automatically (bypassing a centralized investment entity like crowdcent through which funds would have to flow, which creates legal complications) and so everybody is staking their own slots but models provided. Like I mentioned in discord, I don’t think you can just randomly give some users better performance than others, so it would have to be a shared ensemble that kept getting bigger as users were added, or maybe it would still have individual models but would rotate them daily among users (if they ever add a churn requirement in the main tournament that won’t work) which would even out differences although I imagine luck would still play into it in the short-term (each user could also have several slots I guess which might even it out more).

I do have some skepticism that any automatic grid-searching thing still basically converges in aggregate to some form of “example predictions” even if it is submitted over many models over many slots in parallel – it will still just be xgboost. (Which is fine, but I think this idea is more useful for user’s ease of staking something than it would be for making a better metamodel.) Imagine that Numerai didn’t have any examples – somebody would just make one and it would be on github. There will always be some vanilla most easiest model to make and if more and more users use it than they “aren’t adding any new signal”. But still – we need that vanilla signal among many others, just depends how much is staked on it whether it is too much. And if we create a pool…again I think it distills to be much the same thing (maybe). I think there is a kernel of a good idea here, but so far I can’t quite work it out into something where I’m thinking “YES! We have got to do that!”
