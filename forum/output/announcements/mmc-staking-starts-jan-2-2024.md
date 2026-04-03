---
title: "MMC staking starts Jan 2, 2024"
category: Announcements
url: https://forum.numer.ai/t/mmc-staking-starts-jan-2-2024/6827
created_at: 2023-11-28T21:12:31.948000+00:00
last_posted_at: 2024-02-15T09:58:37.069000+00:00
posts_count: 25
views: 4041
tags: []
---

# MMC staking starts Jan 2, 2024

---

### Post #1 — **ark** | 2023-11-28 21:12 UTC

We are reviving Meta Model Contribution (MMC) to replace True Contribution (TC). For rounds starting on or after January 2nd, 2024 staking and payouts will transition to the fixed multipliers 0.5xCORR + 2xMMC. Furthermore, the 2024 Grandmasters season will be determined on CORR and MMC.

We are doing this for a few reasons:

  * MMC is more stable than TC
  * MMC is locally calculable while TC is not
  * We realized our most stable performance when paying MMC



# What is MMC (and BMC)?

From our [docs](<https://docs.numer.ai/numerai-tournament/scoring/meta-model-contribution-mmc-and-bmc>):

> MMC is the covariance of a model with the target, after its predictions have been neutralized to the Meta Model. Similarly, Benchmark Model Contribution (BMC) is the covariance of a model with the target, after its predictions have been neutralized to the stake-weighted[ Benchmark Models](<https://numer.ai/~benchmark_models>).

The idea to revive MMC started with a simple question from our founder, Richard Craib:

> “Given a model, how much does the Meta Model’s correlation with the target change if we increase the model’s stake by some small amount?”

He asked this because we know that the Meta Model’s correlation with our target is a directly monetizable metric for which we could optimize. This produced a simple formula for calculating MMC that I call “Richard’s MMC”:

![Screenshot 2023-11-28 at 1.05.08 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/26544c024f589ff1f497518033ee256cb8cb8333_2_345x25.png)

Where y is the target, m is the Meta Model, and p are a model’s predictions.

Using a derivative with respect to the 0.001 as it goes to 0, we reach the following formula that I call “Murky’s MMC” (big thanks to our user Murky for this derivation):

![Screenshot 2023-11-28 at 1.05.14 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/ab129ea1ce012f4473aaa822c4b1b06a8bc0d270.png)

Assuming that p and m are both centered, normalized column vectors (using the tie_kept_rank and gaussian functions from our [open-source scoring tools package](<https://github.com/numerai/numerai-tools>)) both formulas reach results that are 100% correlated with each other.

Finally, to sanity check these methods of calculating MMC, I revived the old method for calculating MMC, removed the bagging and uniform transformation to yield a third formula that i dub “Mike’s MMC”:

![Screenshot 2023-11-28 at 1.05.23 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/52f0e302db458c8563a31ba045273bc62a5f6034.png)

It took some time to convince myself of the mathematical equivalence of Murky’s and Mike’s.  
Here are some thoughts:

  * tie_kept_rank and gaussian functions makes both predictions and meta model centered and normalized
  * mean = 0 and std = 1 allows the following relationships:  
![Screenshot 2023-11-28 at 1.05.37 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/513ca8607924585477b165f230322150a9a4c84b_2_517x33.png)
  * when mean = 0:  
![Screenshot 2023-11-28 at 1.05.51 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/380fef290c0936ce603f91bf302c44dc5fc830a2.png)
  * The inverse of a vector can be defined as:  
![Screenshot 2023-11-28 at 1.05.57 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c0d79d86120572c6e366578db44bc3d36961488b.png)
  * using the above we can convert between Murky’s MMC and Mike’s MMC:  


[![Screenshot 2023-11-28 at 1.06.08 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b01aaefb0cbf016426acc4938e2a1e2b782be6d8_2_517x106.png)Screenshot 2023-11-28 at 1.06.08 PM1020×210 12.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b01aaefb0cbf016426acc4938e2a1e2b782be6d8.png> "Screenshot 2023-11-28 at 1.06.08 PM")




Murky’s version is the fastest and simplest to compute, so we are using it to calculate MMC:
    
    
    def contribution(
    predictions: pd.DataFrame,
    meta_model: pd.Series,
    live_targets: pd.Series,
    ) -> pd.Series:
    
    """Calculate the contribution of the given predictions
    to the given meta model.
    
    Then calculate contribution by:
    1. tie-kept ranking each prediction and the meta model
    2. gaussianizing each prediction and the meta model
    3. orthogonalizing each prediction wrt the meta model
    4. multiplying the orthogonalized predictions and the targets
    
    Arguments:
    predictions: pd.DataFrame - the predictions to evaluate
    meta_model: pd.Series - the meta model to evaluate agains
    live_targets: pd.Series - the live targets to evaluate against
    
    Returns:
    pd.Series - the resulting contributive correlation
    scores for each column in predictions
    
    """
    # filter and sort preds, mm, and targets wrt each other
    meta_model, predictions = filter_sort_index(meta_model, predictions)
    live_targets, predictions = filter_sort_index(live_targets, predictions)
    live_targets, meta_model = filter_sort_index(live_targets, meta_model)
    
    # rank and normalize meta model and predictions so mean=0 and std=1
    p = gaussian(tie_kept_rank(predictions)).values
    m = gaussian(tie_kept_rank(meta_model.to_frame()))[meta_model.name].values
    
    # orthogonalize predictions wrt meta model
    neutral_preds = orthogonalize(p, m)
    
    
    # center the target
    live_targets -= live_targets.mean()
    
    # multiply target and neutralized predictions
    # this is equivalent to covariance b/c mean = 0
    mmc = (live_targets @ neutral_preds) / len(live_targets)
    return pd.Series(mmc, index=predictions.columns)
    

We divide by the length of the target to bring the final values inside the range of something like CORR20v2.

Your BMC is basically MMC, but using just the stake-weighted benchmark models instead of the Meta Model. This is helpful to tell us how well your model ensembles with just our internal Benchmark Models. A high score in both would indicate a truly unique and contributive signal.

# Why MMC?

The fact that we can calculate MMC 3 different ways and they are all 100% correlated means that this is an easily explainable metric regardless of how you intuit the linear algebra and can be calculated locally (unlike TC).

Furthermore, MMC is much more stable than TC. Take a look at the following charts showing the distribution of each score over time:

[![Screenshot 2023-11-28 at 1.02.31 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/82f5123da1274c155c0cbd14525b95e77a852c50_2_690x186.png)Screenshot 2023-11-28 at 1.02.31 PM1492×404 251 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/82f5123da1274c155c0cbd14525b95e77a852c50.png> "Screenshot 2023-11-28 at 1.02.31 PM")

Clearly MMC is much closer to the distribution of CORR than TC ever was or will be. This stability in the score is significant when we consider how users need to optimize their models for MMC and CORR.

---

### Post #2 — **taori** | 2023-11-29 21:08 UTC

Out of curiosity, why is that the grandmaster raking is caldendar year based and not rolling year window based?

Also, will you ever consider removing the test daily rounds from the computation of leaderboard and grandmaster scores? There was no stake allowed on those testing daily rounds so they should not be part of the ranking computation.

---

### Post #3 — **ark** | 2023-11-29 22:17 UTC _(reply to #2)_

1. There must be some cutoff date to award titles and we want to highlight long-term performance. Yearly seasons are the most reasonable to achieve this.

  2. The test daily rounds are now starting to phase out and will finish phasing out by 2024-06-02. This is partially by design b/c those that switched over right away clearly worked harder to stay up-to-date with tournament functions and thus deserve a higher rank.

---

### Post #4 — **taori** | 2023-11-30 10:04 UTC

@numerank

You initially convinced me that it is ok to reward fast-adapting/hard-workings users more by including the test daily rounds in the ranking computation, but then this choice makes very hard to compare models. Forget about prestige, I would just like to compare my models with benchmark models, for example. It’s a pity that I cannot properly use this functionality due to the inclusion of test daily rounds in the statistics and ranking.

Wouldn’t be more useful to keep the test daily rounds out of the leaderboard and use them only for the grandmaster ranking, which is prestige focused?

---

### Post #5 — **nasdaqjockey** | 2023-12-10 05:01 UTC

I’ve seen some posts about changing the multipliers. On Jan 2, 2024 will the multipliers be 0.5 x CORR + 2 x MMC?

Or something else?

---

### Post #6 — **wigglemuse** | 2023-12-10 05:19 UTC _(reply to #5)_

The latest announcement is 0.5 Corr + 3x MMC, although I’m not sure you should bank on that either. (And MMC was corrected on the website earlier in the week from an erroneous version that was previously displayed. So if you had looked at your models a week ago thinking about MMC, check again.)

---

### Post #7 — **nasdaqjockey** | 2023-12-10 12:41 UTC

Thanks [@wigglemuse](</u/wigglemuse>), yes I’m aware of the new MMC calculation. It’s hard to follow all the threads.

That really puts a lot of emphasis on MMC. I hope it correlates with fund performance, I’m not sure we can survive another drawdown like we recently experienced.

---

### Post #8 — **eleven_sigma** | 2023-12-11 19:49 UTC _(reply to #6)_

Where is described the bug and the correct way to compute MMC?  
Is Murky’s version correct as said before?  
Is there a R implementation of the function to do it?

---

### Post #9 — **wigglemuse** | 2023-12-11 20:21 UTC _(reply to #8)_

The code released is correct, but the website displayed version (before sometime last week) was still using the old Nomi target (leftover from original MMC), not the Cyrus target as it should have been. (Seems like if that was the case, the code was probably wrong too, but whatever – supposedly it is all correct now. I leave it to others to verify that as it seems like many are recreating locally. Do it all match up now people?)

---

### Post #10 — **numerologist** | 2023-12-13 15:33 UTC _(reply to #8)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/e/8797f3/48.png) eleven_sigma:

> Where is described the bug and the correct way to compute MMC?

The most up-to-date function is always located here: [numerai-tools/numerai_tools/scoring.py at master · numerai/numerai-tools · GitHub](<https://github.com/numerai/numerai-tools/blob/master/numerai_tools/scoring.py>)

You can check what has been fixed in the commits history: [History for numerai_tools/scoring.py - numerai/numerai-tools · GitHub](<https://github.com/numerai/numerai-tools/commits/master/numerai_tools/scoring.py>)

As you can see, the latest fixes were pushed 6 hours ago. ![:slightly_smiling_face:](http://forum.numer.ai/images/emoji/twitter/slightly_smiling_face.png?v=12)  
So it might be a good idea to subscribe to repo changes.

---

### Post #11 — **sirbradflies** | 2023-12-16 14:41 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/ark/48/3156_2.png) ark:

> `predictions`

Thanks for sharing this. I have some (probably basic) questions about how the MMC and the payout is calculated.

  1. Why in the [correlation_contribution](<https://github.com/numerai/numerai-tools/blob/master/numerai_tools/scoring.py#L191>) function we don’t raise the gaussian to the 1.5 power as in the [numerai_corr](<https://github.com/numerai/numerai-tools/blob/master/numerai_tools/scoring.py#L349>)?
  2. Am I oversimplifying if I see the payout (excluding clipping and payout factor) as 0.5xCORR(P, T) + 3xCORR(P⊥M, T)?  
Where:  
CORR → Correlation (as calculated in [numerai_corr](<https://github.com/numerai/numerai-tools/blob/master/numerai_tools/scoring.py#L349>))  
P → User predictions  
M → Meta Model predictions  
T → Cyrus target  
P⊥M → The user predictions component independent of (orthogonal to) the meta model predictions



Thank you in advance

---

### Post #12 — **andralienware** | 2023-12-16 16:31 UTC _(reply to #11)_

There’s also the Gaussianization step for both the meta model and the user predictions that happens before 1.5 power and corr (for corr) and neutralization (for mmc).

---

### Post #13 — **sirbradflies** | 2023-12-16 16:41 UTC _(reply to #12)_

Thanks [@andralienware](</u/andralienware>), yes this is what I meant with “as calculated in [numerai_corr](<https://github.com/numerai/numerai-tools/blob/master/numerai_tools/scoring.py#L349>)”.  
It just surprised me that the steps to calculate CORR (the score) seem to be different from those needed to calculate MMC and not just the neutralization but also the 1.5 power.  
I was trying to find a simple way to tie together CORR and MMC like in 0.5xCORR(P, T)+3xCORR(P⊥M, T) but it doesn’t match the code I see in the repository so I guess there is no easy way to represent it.

---

### Post #14 — **ark** | 2023-12-18 19:15 UTC

CORR and MMC are fundamentally different metrics and thus cannot be calculated the same way. They are different both mathematically but also different in their intent. We wanted CORR to capture performance in the tails of your prediction distribution (hence the pow 1.5) whereas MMC cares about how your predictions improve the entire Meta Model (hence no accentuation of the tails with a pow 1.5). As others have stated, we do similar pre-processing in both CORR and MMC, so they aren’t completely dissimilar.

---

### Post #15 — **andralienware** | 2023-12-19 04:13 UTC _(reply to #14)_

Isn’t the reason that pow 1.5 is employed to capture the leptokurtosis of real returns? It seems that if there are issues in the tail of the meta model (which is probably what drives most trading losses and gains), and a model’s predictions correct them, there should be a payout increase corresponding to that. I understand the idea of getting rid of predictions’ components made up of each’s projection onto the meta model, but that does not preclude the idea of using Gaussian-ized and then pow 1.5’ed predictions from being projected. I agree that Spearman correlation does not make sense, but I agree with sirbradflies’s idea that the 1.5 pow makes sense. We all know market returns are not actually Gaussian, and if the pow 1.5 pre-processing step makes sense for CORR for its effects on tails, then it should make sense as something to do before neutralization. Run it by [@murkyautomata](</u/murkyautomata>), and I’m sure you’ll get agreement that pow 1.5 (or whichever transformation you think matches the tails) would be a good idea in MMC.

---

### Post #16 — **taori** | 2023-12-29 08:06 UTC

[@ark](</u/ark>)

![](http://forum.numer.ai/user_avatar/forum.numer.ai/ark/48/3156_2.png) ark:

> MMC is the covariance of a model with the target, after its predictions have been neutralized to the Meta Model.

Shouldn’t the Meta Model be deprived of the model contribution before we can use it to compute MMC?

Firstly using a model to compute the Meta Model and asking in a second step how much a model can still improve the Meta Model (MMC), means that MMC disregards the contribution that a model gave in building the Meta Model in the first place.

---

### Post #17 — **eleven_sigma** | 2024-01-12 13:01 UTC _(reply to #16)_

I’m very interested too in this topic. Computing MMC as taori says have a big computational cost (a MM should be computed with a LOO strategy).  
Is there other way to adjust the ‘size’ efect of a model in the MMC?  
Perhaps computing MM with LOO only for big staked predictions, those that the difference in MMC computed as now and with LOO have a significant difference. I would like Numerai Team does some test with top 100 stacked models and check the impact in MMC with/without LOO MM build.

---

### Post #18 — **taori** | 2024-01-15 15:08 UTC

Thanks to @PTR for clarifying my question on [discord](<https://discord.com/channels/894652647515226152/1089609932518731827/1195689296842199100>). You are totally right.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/9ce8b8a1762978ba9eea72d3525883099fe04b20.png)image909×267 43.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/9ce8b8a1762978ba9eea72d3525883099fe04b20.png> "image")

I forgot that this is also how TC worked. Both MMC and TC try to estimate how much more (or less) of a model is needed in the Meta Model to improve its performance.

So MMC serves to optimize the weights of the models within the SWMM.

From the hedge fund that seems reasonable, but from the user perspective it is totally unfair. The users would like to be paid on how much their models contributed to the performance of the SWMM. That part is the 0.5xCORR, but I believe that is too low for the [risk](<http://forum.numer.ai/t/numeraire-worst-part-of-numerai-time-to-change>) associated with NMR.

Using the stake, and hence payout, as a mechanism to optimize the MM is in conflict with how the users see the stake and the payout and I hope this part of the tournament changes in the future.

---

### Post #19 — **ark** | 2024-01-15 20:47 UTC _(reply to #18)_

A models CORR is not how much it contributed to the MM - this is just a measure of how predictive of the target it is. MMC is the models contribution to the MMs CORR. Here are some facts about MMC that you may be missing:

  * If you have positive CORR but 0 MMC then you are providing no uniquely additive signal - you just have a model that we (and other data scientists) already know about.

  * We orthogonalize predictions wrt the MM and most predictions have very small stake so there is virtually no difference between raw MMC and bagged (LOO) MMC.

  * Calculating MMC in a bagged/LOO formulation makes the calculation more opaque to data scientists because you all don’t have access to other models’ raw predictions, thus you can’t optimize for it locally. Local optimization is a key characteristic.

---

### Post #20 — **taori** | 2024-01-16 00:52 UTC

If the MM was so good that it can perfectly predict the target, then all models would have MMC 0 and not rewarded.

However MM doesn’t come for free, so you should also reward the models that created the MM in the first place and the risk the users take in staking those models. Currently this part is rewarded 0.5xCORR, which is too low.

> if you have positive CORR but 0 MMC then you are providing no uniquely additive signal - you just have a model that we (and other data scientists) already know about.

This is where I disagree with you. You believe you don’t have to pay for the MM, but it has a cost for the users and I am saying you need to reward that

---

### Post #21 — **thinkdevdo** | 2024-01-16 03:14 UTC _(reply to #20)_

Hello, thanks for your posts I’ve been enjoying thinking about what you are saying.

Just to play devils advocate on this point, and help myself understand a little bit, is it unreasonable to say they have already paid for the MM with historical payouts? If MMC is 0, doesn’t that mean the is no reason to incorporate the user’s signal into the next version of the MM and the MM would remain unchanged if this were the only contributed signal?

Don’t get me wrong, I’m devastated that Corr multiplier is 0.5, and that MMC is 4x higher, it might be the death of my participation, as I was just getting my Classic models to produce some stable signals, and don’t want to “start over”. But, I don’t see the fundamental problem with the team having “bought” the current state of the meta-model with the payouts that have run the tournament over the past years, and now consider this model the bare minimum to be able to improve upon be able to continue in the tournament.

I don’t think it’s a user-friendly way to move forward, and in fact I hate it; it says to me “we’re using your predictions only for as long as we need you,” which is something I feared before I started participating. Just trying to understand if there’s something I’m missing with respect to fairness towards us.

Best,  
TDD

---

### Post #22 — **taori** | 2024-01-16 10:29 UTC

> is it unreasonable to say they have already paid for the MM with historical payouts?

I believe it is unreasonable. The MM has to be built at every round, so Numerai continuously needs the users’ models. But without reward the users would stop submitting.

Just to be clear, I like the current tournament and MMC is much better than TC. I don’t even want the models to be rewarded for predictions that are either useless or detrimental to the hedge fund (if the fund doesn’t go well, everybody lose).

My only concern is that MMC and TC do not take into consideration the effort and [risk](<http://forum.numer.ai/t/numeraire-worst-part-of-numerai-time-to-change>) (!) of building the MM and Numerai doesn’t seem to care much about that. Numerai even considered going for 0 CORR multiplier. That is what worries me.

---

### Post #23 — **numerologist** | 2024-01-20 20:53 UTC

> the switch to MMC will cause an outflow of bad performers which will significantly increase the payout factor

But _**decrease**_ the payout.

What Numerai neglects to acknowledge is that when the outflow of ([likely good](<http://forum.numer.ai/t/how-many-high-mmc-models-have-recently-been-unstaked/6951/3>)) performers happens, they cash out. When they cash out, they sell the crypto and as such, influence the market.

In other words, if you extract a benchmark (e.g. short top cryptos or just ETH and buy NMR), you’ll be at a loss. Because the monetary payout “factor” **has decreased, not increased** due to the NMR impact on payouts.

---

### Post #24 — **autratec** | 2024-02-09 02:44 UTC

After carefully observing both MMC and CORA20V2 results, it seems that they are closely aligned. If this observation holds true, it prompts the question: why maintain two separate indicators for scoring? A similar pattern is also evident in the signals.

---

### Post #25 — **taori** | 2024-02-15 09:58 UTC

I have been thinking about it for a while and I believe BMC is a better metric to base the payout on.

[@ark](</u/ark>) have you (the numerai team) considered to base the payout on BMC instead of MMC? Would you share the pros and cons that you come up with?
