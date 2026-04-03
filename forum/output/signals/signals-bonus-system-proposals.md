---
title: "Signals' Bonus System proposals"
category: Signals
url: https://forum.numer.ai/t/signals-bonus-system-proposals/3583
created_at: 2021-06-11T00:08:43.351000+00:00
last_posted_at: 2021-06-12T17:12:55.018000+00:00
posts_count: 13
views: 828
tags: []
---

# Signals' Bonus System proposals

---

### Post #1 — **joakim** | 2021-06-11 00:08 UTC

Just moving this thread from RC to the forum…

Apparently there might be a “**big bounty for anyone who can come up with a bonus scheme that is actually sybil resistant and aligns perfectly with [Numerai’s] incentives / safety requirements.** ” ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

[@slyfox](</u/slyfox>), any other requirements we should be aware of?

Suggestions so far:

  * Joakim (me): Pay bonuses to top k live CORR models (after n rounds) that stay within their Bayesian probability ‘cone’, based on priors from the model’s validation set predictions. This model would NOT be getting a bonus (flipped the chart to hopefully make it more clear).  


[![Bayseian chart flipped 3](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/1c0cc1aa343e157da3d1b38a43181ffff27cbabb.png)Bayseian chart flipped 3469×306 70.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/1c0cc1aa343e157da3d1b38a43181ffff27cbabb.png> "Bayseian chart flipped 3")

  * [@swish](</u/swish>) : Apply erasure to the top performance bonuses, any taker can be griefed by CoE if an attack was exposed by somebody, who would be rewarded in return for that.

---

### Post #2 — **gammarat** | 2021-06-11 02:46 UTC

Why would you think a model should ‘stay in its lane’ so to speak? Especially if that lane depends on performance on the validation sets, which in turn would seem to require those sets to be broadly representative of future eras. Are they?

---

### Post #3 — **joakim** | 2021-06-11 03:21 UTC _(reply to #2)_

Well no, they aren’t necessarily. Stock market time series is indeed non-stationary, and there’s recency bias, etc. It’s difficult to predict the future without making use of historical data however.

If a model stays within it’s predicted Bayesian probability cone, then at least it’s a good and ‘useful’ model for that time period, and might deserve a ‘bonus’ payout (in addition to 2xCorr + MMC) for as long as it does stay within this probability cone.

---

### Post #4 — **gammarat** | 2021-06-11 04:09 UTC _(reply to #3)_

That makes sense. Alas the Tournament is set up in a somewhat time independent manner, so it would be difficult to calculate the spread of the cone over 4 weeks, I would think. I’m curious though if you can get it to work. But something like that could be especially interesting in Signals.

FWIW, the next step in the tech aspect of building a Signals model is bringing in a Kalman filter analysis).

---

### Post #5 — **gbrecht** | 2021-06-11 06:11 UTC

My proposal:

  * The bonus system is a seperate game besides week-for-week staking, so that remains unchanged
  * numerai sets up their dedicated compute environment for entries towards bonus
  * a user who wants to participate submits a container (basically a predict.py) to that compute env
  * a user has one container slot to upload
  * an entry has to be unchanged for x (e.g. 4) weeks before it is eligible for a payout
  * the scoring of the predictions is done on how good and unique it is. I am very bad at designing this in a formula, first idea could be` corr / (1-abs(corr-mmc))` but basically I am aiming for the true contribution to the metamodel
  * you reupload your container, your trial period begins anew

---

### Post #6 — **jackerparker** | 2021-06-11 07:53 UTC

My proposal (actually can be applied to both Classic and Signals):

  1. Allow people to stake on user models (kind of community portfolio managers). Limit the stakes to the Z * number of NMR earned from the MMC part on its own models for the last N rounds (Only successful and useful (for metamodel) participants can stake on others users. That will reduce the effect of “investors” who only want to stake on someone). Pay bonuses as X% of profit accumulated in X months (for example, 12) to the model owner. Add extra information for the models like: optional (only if user wants it) link between Signals and Classic models (idea here is that high-variance models for (p, 1-p) attack have low chances to be good at both Tournaments); info about verified users. Verification is optional, users can send some docs to the Numerai team, for the rest of users only the date of verification will be available (just to check if modelers were verified before or after the (p, 1-p) model became successful ). Pay bonuses in fiat with some contract to be sure that only people from verified documents can get the payment (It will be so hard for (p, 1-p) attackers to find a lot of people which they can use both for verification now and for payout 1 year later).
  2. All the same, but portfolio managers are the Numerai team. Allow some part of the team to stake some limited NMR from Numerai treasure on the user models, pay Y% of profit for the team member and X% of profit to the model owner. And the rest of the things from #1.



(p, 1-p) attacks will take a lot of resources and result in small chances to get profit. I believe that people/team will stake on the “known” users rather than unknown models from the top of the leaderboard. Thus, bonus will also reward modelers useful for the community.

Regards,  
Mark

---

### Post #7 — **mugamma** | 2021-06-11 18:12 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/joakim/48/3442_2.png) joakim:

> Pay bonuses to top k live CORR models (after n rounds) that stay within their Bayesian probability ‘cone’, based on priors from the model’s validation set predictions.

This still sounds vulnerable to p/1-p. Top k by itself introduces the asymmetry, and I assume finagling the cone is not terribly hard. Particularly for signals since you can get the historical data.

---

### Post #8 — **filipstefano** | 2021-06-11 20:47 UTC

We can use another reasoning.

Instead of ‘bonus’ payout, maximum burn limit can be changed to some value between **-10% to -15%** (instead of -25%).  
This would also motivate new users to start submitting on signals , and it would help achieving positive effect without much effort.

---

### Post #9 — **joakim** | 2021-06-11 21:17 UTC _(reply to #7)_

How is it vulnerable to p | 1-p? If you have a model with positive performance on validation, the 1-p of that model would have negative performance on validation, so would have a negative sloping probability cone. Even if the latter model has positive performance on live, it would deviate outside of the probability cone and hence not be eligible for a bonus. The first model obviously wouldn’t get a bonus either as it would have negative live performance in this scenario.

Creating a model that performs similarly on live (after say 20 rounds) as it does on historical data is far from easy. If you can do that however, it’s less likely due to just luck and IMO would deserve a bonus. In short, I don’t see how it’s gamable as only models with positive performance on both validation AND live would get a bonus.

---

### Post #10 — **mugamma** | 2021-06-11 21:39 UTC

Validation is trivial to fake since you know the right answers.

---

### Post #11 — **joakim** | 2021-06-11 22:39 UTC _(reply to #10)_

Ah yes, you’re right, thanks! You could just create many different models with the same (positive) validation predictions, but different live predictions. The model that performs within the spoofed probability cone would get a bonus merely because of luck. ![:frowning:](http://forum.numer.ai/images/emoji/twitter/frowning.png?v=9) Oh well, I tried.

---

### Post #12 — **liz** | 2021-06-11 23:12 UTC

discretionary bonus might be the way to go

---

### Post #13 — **ssh** | 2021-06-12 17:12 UTC

I suggest to keep it simple and profitable for the users - just like the very same bonus as it were for main NMR tournament: with a few top tiers and percentage of staked amount (N weeks before). It has flaws and vulnerabilities but it worked mirracle to main tournament as it was a huge insentive to upper you stake in a hope of generous bonuses. All these leads to more participants and more submissions. The same approach could be applied to MMC or CORR20.
