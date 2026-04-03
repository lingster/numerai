---
title: "TC, stake and payout: let's get some facts straight"
category: Tournament
url: https://forum.numer.ai/t/tc-stake-and-payout-lets-get-some-facts-straight/5730
created_at: 2022-09-27T19:51:57.914000+00:00
last_posted_at: 2022-09-29T16:40:15.601000+00:00
posts_count: 18
views: 1355
tags: []
---

# TC, stake and payout: let's get some facts straight

---

### Post #1 — **taori** | 2022-09-27 19:51 UTC

From [true contribution details](<http://forum.numer.ai/t/true-contribution-details/5128>) we learn that:

1 - “The goal of TC metric is to estimate how much a user’s signal improves or detracts from the returns of Numerai’s portfolio”

This is not correct. TC estimates how much a user’s stake should change so that the user’s signal (which is stake weighted) maximizes the returns of Numerai’s portfolio. In other words, to improve the returns of Numerai’s portfolio the weight (stake) of the user’s signal for that round should be stake+TC.

stake+TC is the signal contribution to that round, not TC alone. This mistake has important consequences if we use TC alone as payout.

By the way, this signal contribution doesn’t express how much a model is good in its predictions. It simply says how much of this signal is required so that combined with the others makes a good portfolio. Maybe the model is bad, but it combines well with the rest.

2 - “With TC as the payout metric, a user’s stake would increase if their model increased portfolio returns and decrease (burn) if the model reduced returns”

This is not correct. With TC as the payout metric, a user’s stake would increase or decrease so that the stake is adjusted until it reaches the optimal value that maximizes Numerai’s portfolio returns. At that point TC will become 0. And when TC is 0 the model contribution to the portfolio will be simply the stake. Interestingly enough, if the stake of a model is already at the optimal value and the user increases the stake ,the next round TC would be the negative value of the stake increase (assuming no other changes take place).

Is there a better payout scheme? Maybe the payout should be proportional to “stake + TC”, the actual signal contribution. If we compute “stake + TC” as percentage of the total tournament stake we have an estimate of a model importance in the portfolio. The payout could be something related to this value, but I have some doubts that would work. The problem is that “stake + TC” express how much the model is required by the portfolio but from the user perspective the stake is how much their want to invest in their model. If a user decides to double their stake what happens to the TC of all the other models?

[UPDATE]

A possible improvement to the current TC, stake and payout scheme is the following.

**TC** alone is responsible to define the contribution of a model to the Numerai’s portfolio. Stake is not used anymore in this context. However TC computation has to change: Numerai initially sets the TC of all models to 0 (or any value for that matter), then, at each round, it computes the optimal portfolio using TC as model initial weight. In the next step the gradient is computed and finally TC value is updated with this gradient. So TC at round end is TC of previous round + the gradient (TC[n+1] = TC[n] + gradient). This change in TC calculation makes it a full representation of a model contribution to the Numerai’s portfolio. TC expresses how much Numerai needs a model.

**Payout** can now be a function of TC, where TC is scaled with respect of the total amount of TCs in the tournament. Oversimplyfing, if Numerai is willing to pay A amount of NMR at each round, the payout could be computed as: Payout = (TC/TotalTournamentTCs) * A

**Stake** is just there for the user and it’s not part of the reward/punish mechanic. The stake earn/burn mechanic as a “the survive of the fittest” mechanic is interesting, but it is not required anymore: Numerai is already able to quantify what is the optimal model weight required to compute the best portfolio: it’s TC computed as I described above. If TC goes to 0 then a model gets 0 NMR reward, no need to burn NMR (at least not for this purpose, but I can see that a similar mechanic is still needed for the NMR ecosystem. I don’t have an answer for that yet).

---

### Post #2 — **restrading** | 2022-09-28 08:50 UTC

Below are just some of my opinions, not rigorous arguments.

  1. “The goal of TC metric is to estimate how much a user’s signal improves or detracts from the returns of Numerai’s portfolio”



TC is computed as the gradient of the portfolio return for that round wrt user stake, multiplied by some constant. If my understanding is correct, then this seems exactly what it estimates.

  2. “With TC as the payout metric, a user’s stake would increase if their model increased portfolio returns and decrease (burn) if the model reduced returns”



You seem to assume that there is a stationary point of optimal portfolio. But as the market evolves, the optimal point changes, there will always be positive and negative TCs to move the portfolio along to chase the optimal point.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/t/ebca7d/48.png) taori:

> **TC** alone is responsible to define the contribution of a model to the Numerai’s portfolio. Stake is not used anymore in this context

My understanding is TC is a measurement of the “would-be” delta of contribution of a model, not “the” contribution of a model. Stake doesn’t need to be used for defining the contribution because the stake will increase with payout which is what TC is supposed to do, rewarding more to “good” models so their stake becomes higher quicker than other models.

My concern with TC is more about the length of the feedback loop, especially if they move to 3-month resolution, but I think TC as a measurement is on-point.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/t/ebca7d/48.png) taori:

> **Payout** can now be a function of TC

TC as it currently stands is already a cumulative measure (within each round).

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/t/ebca7d/48.png) taori:

> **Stake** is just there for the user and it’s not part of the reward/punish mechanic

Stake is a expression of user confidence, without this information and using TC solely for deriving portfolio weights will be a problem because there’s no skin in the game. High TC at a certain moment or during some period of time doesn’t mean the model is good.

---

### Post #3 — **kayeffnumeraitor** | 2022-09-28 10:11 UTC _(reply to #2)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/restrading/48/2928_2.png) restrading:

> especially because they are moving to 3-month resolution

Where is this information from? I really wish there would be some informal Numerai blog

---

### Post #4 — **restrading** | 2022-09-28 10:52 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/kayeffnumeraitor/48/991_2.png) kayeffnumeraitor:

> Where is this information from? I really wish there would be some informal Numerai blog

It’s not confirmed, but I remember it being mentioned in RocketChat by Richard so I assume the daily tournaments will be on 60D targets with 3-month resolution.

---

### Post #5 — **kayeffnumeraitor** | 2022-09-28 14:20 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/t/ebca7d/48.png) taori:

> This is not correct. With TC as the payout metric, a user’s stake would increase or decrease so that the stake is adjusted until it reaches the optimal value that maximizes Numerai’s portfolio returns. At that point TC will become 0.

While you are technically correct, this is mostly a non issue since you would have to stake way more than even the largest stakers for that effect to play a significant role.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/t/ebca7d/48.png) taori:

> So TC at round end is TC of previous round + the gradient (TC[n+1] = TC[n] + gradient).

I guess this has the following drawback: once you achieved some rather high cumulative TC, you can upload garbage afterwards and still get reward for it.

In my opinion, TC is, from the perspective of a tournament participant, too noisy, for whatever reason that may be (stock market fluctuations, portfolio construction, etc.). Look at [one of my experimental models](<https://numer.ai/kayeff_random>), which uploads random numbers each round, so that i can estimate the statistical error of corr and TC. You can see that the statistical error for TC is rather huge, so to have a good TC model winning most of the time you need to have a mean TC of ~0.1, not accounting for systematic errors (model, training data). If your model has a mean TC lower than that, you will essentially suffer from the [volatitily tax](<https://en.wikipedia.org/wiki/Volatility_tax>) because of the volatility/noise of TC.

---

### Post #6 — **taori** | 2022-09-28 18:03 UTC

I am a little bit frustrated by my inability to clearly communicate my thoughts. Anyway, let’s try one more time.

The payout mechanic based on TC works great for optimizing the Numerai’s portfolio. It indeed maximizes the portfolio returns. That’s why Numerai is happy about it and all the tests they had performed confirmed the effectiveness of TC in optimizing their portfolio returns.

If payout based on TC mechanics works great for the fund, what is the problem? The problem is that a payout based on TC is not fair for the users, because TC doesn’t express a model contribution to the portfolio. To be optimal, the Numerai’s portfolio needs each model in “current stake + TC” amount. If a model stake is 10 and TC is -3, the model contribution to the fund is 7 not -3!!! TC expresses how much change in the model stake is required to improve the portfolio returns, but the portfolio needs “current stake + TC” amount of your model to get the maximum returns, not just TC! That’s why “stake + TC” is the real model contribution and that’s why the payout should be based on that.

However, as I explained already, a payout based on TC+stake would make the whole stake burning mechanics to go away and I have no solution for that. It’s a problem for the NMR ecosystem.

Note: If the market was not volatile, if the models wouldn’t change, if users wouldn’t change their stakes, then the current payout mechanics based on TC would make the model stakes converge to the optimal value that maximizes Numerai’s portfolio returns and would make TC go towards zero. In practice we will never be able to observe this convergence, because there are indeed models and stake changes and market volatility. The TCs computed at every round are more a compensation to that noise than a quantification of a model goodness, which again is given by stake value + TC.

---

### Post #7 — **taori** | 2022-09-28 18:07 UTC

Just one last fun comment: there is a very high probability that all my thoughts are wrong, since nobody agrees with me. However, why would I not take the opportunity of being dramatic and claiming that the current payout system is broken? The recent inactivity of the forum really pushed me to create some noise here ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #8 — **kayeffnumeraitor** | 2022-09-28 23:56 UTC _(reply to #6)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/t/ebca7d/48.png) taori:

> If a model stake is 10 and TC is -3, the model contribution to the fund is 7 not -3!!!

Now i get your point. This would be an interesting concept. So your version of TC would be < 0, if you actually hurt the portfolio with your staked predictions, i.e. you stake 10 but the TC is -13 or 3 for the same predictions inverted, it would be 0, if your predictions neither hurt nor help and it would be > 0, as soon as having some amount of stake on this prediction contributes to the numerai portfolio.

I wonder what kind of difference this makes.

---

### Post #9 — **taori** | 2022-09-29 06:59 UTC _(reply to #8)_

Exactly!

Also to make an even more extreme example on the current payout method, let’s say an extremely good model stake is 50% of the total tournament stake. Since this is an extremely good model the portfolio optimizer keeps its contribution ~50% at every round, thus TC will tend to be 0. This incredibly great model will be paid ~0 NMR every round although its actual contribution is 50%! Sometimes it will even get negative TC, due to the little stake adjustments required to keep all the stake weighted portfolio optimal.

See [here](<http://forum.numer.ai/t/question-on-tc-is-it-true-contribution-or-something-else/5134/>).

Being paid on TC doesn’t really make sense. TC is not a measure of the true contribution of a model, is a measure of how noisy the tournament is: more noise → more TC is required to keep the stake weighted portfolio optimal (with noise I mean market volatility, model changes, user stake changes)

---

### Post #10 — **restrading** | 2022-09-29 07:34 UTC _(reply to #9)_

How can a model consistently stay at the optimal point? The optimal portoflio will move around with the market so TC won’t always stay 0.

If a model is at its optimal point (optimal stake value for this model only such that it’s TC is 0, and optimal as in no matter if it increases or decreases in stake it will reduce the portfolio return), why should it be rewarded further if there are other models with positive TC that when their stake gets increased through payout it will improve the overall portfolio return?

---

### Post #11 — **taori** | 2022-09-29 08:25 UTC _(reply to #10)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/restrading/48/2928_2.png) restrading:

> How can a model consistently stay at the optimal point? The optimal portoflio will move around with the market so TC won’t always stay 0.

Correct. As I wrote “TC is a measure of how noisy the tournament is”, but why would users want to be paid on a noise rebalancing factor instead on their actual model contribution?

![](http://forum.numer.ai/user_avatar/forum.numer.ai/restrading/48/2928_2.png) restrading:

> If a model is at its optimal point (optimal stake value for this model only such that it’s TC is 0, and optimal as in no matter if it increases or decreases in stake it will reduce the portfolio return), why should it be rewarded further if there are other models with positive TC that when their stake gets increased through payout it will improve the overall portfolio return?

Because that “model at its optimal point” is required exactly at that stake level by Numerai. Without it the portfolio would decrease its returns!!! So the model must be paid because:  
1- its predictions are still required  
2- its stake is still required at that level (the user money are blocked in the stale)

---

### Post #12 — **taori** | 2022-09-29 09:29 UTC

Let’s see what happens to TC when a new model is introduced in the tournament first.

We have two options: the model is useful for the optimal stake weighted portfolio or it is detrimental to it. If it is detrimental, no matter what initial stake the model has, it will keep receiving negative TC until its stake is 0 and this behaviour is what users expect. If the model useful to the portfolio, then we have two options again: if the initial stake is below the optimal level, then the model will keep receiving positive TC until its stake becomes optimal, this behaviour is what users expect. If the initial stake is above the optimal level, then the model will keep receiving negative TC until its stake becomes optimal, this behaviour is NOT what users expect. In both cases, when the optimal stake is reached, the model will keep receiving random TC, just tournament noise adjustments, despite being a good model. This behaviour is NOT what users expect.

Now Let’s see what happens to TC of existing models when a new model is introduced in the tournament.

We have two options: the model is useful for the optimal stake weighted portfolio or it is detrimental to it. If it is detrimental, no matter what initial stake the model has, it will keep receiving negative TC until its stake is 0 and this behaviour is what users expect. What happens if the model is useful for the portfolio?

Every model can be seen as made up of two components: a unique contribution to the metamodel and a component correlated with other models. The component correlated with other models will influence the stake of the other models. This can have surprising effects. Let’s say a new model is introduced that is 100% correlated with another one (extreme example for the sake of argument). In this situation we have 2 models with identical submissions. The optimal stake weighted portfolio requires exactly X amount of that signal and this amount can be reached with any combination of stake between the two identical models. So what will TC do? Will TC make the stake flows from the model with higher value to the one with lower value until they balance out? Or what combination of stakes will it try to reach? If TC tries to balance out the stakes among models with similar predictions, then every user is encourage to split their models in multiple tournament entries so that each entry will have a smaller stake and those entries will drain the stakes of other users’ models with higher stake value and correlated predictions. On the other hand, if the evolution of TC doesn’t try to equalize the stake values among similar predictions, then we have another issue, that similar predictions are not evaluated and payed equally.

---

### Post #13 — **kayeffnumeraitor** | 2022-09-29 14:37 UTC _(reply to #12)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/t/ebca7d/48.png) taori:

> The optimal stake weighted portfolio requires exactly X amount of that signal and this amount can be reached with any combination of stake between the two identical models. So what will TC do?

As for how the tournament is right now, both models will receive basically the same TC score in each round. That is unless you are considering to stake more than 100k NMR in each model. In this case TC should be higher for the model with less stake of both of them, but both will probably receive fairly low TC for being whales in the tournament. Thats at least how I understood TC so I could be wrong…

---

### Post #14 — **wigglemuse** | 2022-09-29 14:52 UTC

Identical submissions get the same TC – it is the total stake among them that matters, doesn’t matter how it is broken up. (I believe they made sure of that by directly addressing that scenario.) An interesting question then is what happens with TC with _almost_ identical predictions, i.e. shuffle a few rows around, but only a few – can it lead to a noticeable difference in TC? I don’t know. (Probably would want to try that with shuffling some in the middle ranks but not at the extremes, and another experiment where you slightly shuffle the rows at the extremes.)

---

### Post #15 — **taori** | 2022-09-29 16:17 UTC

If account level staking was already a thing I would split one of my model in two tournament entries and stake one with 99% of the NMR it currently has and the other with the remaining 1% and I will monitor their TC to get some insights.

---

### Post #16 — **wigglemuse** | 2022-09-29 16:21 UTC

Same submission = same scores. This is a known fact already.

---

### Post #17 — **taori** | 2022-09-29 16:26 UTC _(reply to #16)_

Ah right, the 100 dropout thing…,I forgot about it.

---

### Post #18 — **degerhan** | 2022-09-29 16:40 UTC _(reply to #14)_

I switched two rows near the middle (0.48 with 0.52) and received [TC -0.159851](<https://numer.ai/degerhan_r2_16/submissions/312>) vs [TC -0.159858](<https://numer.ai/degerhan_ex_04/submissions/312>). Only a single data point but seems like tiny submission differences generate tiny changes in TC.
