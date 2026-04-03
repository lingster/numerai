---
title: "The Un-Meta Model"
category: Tournament
url: https://forum.numer.ai/t/the-un-meta-model/4412
created_at: 2021-10-27T11:36:57.078000+00:00
last_posted_at: 2022-08-30T10:34:38.463000+00:00
posts_count: 8
views: 1553
tags: []
---

# The Un-Meta Model

---

### Post #1 — **rlh** | 2021-10-27 11:36 UTC

Numerai’s payout ratio is declining, as the amount staked doubles every 6-9 months. This means yields will rapidly converge below those of basically every DeFi/yield-farming protocol.

Is it worth staking a model where your 0.03 corr now pays 3% every two months (a year from now), instead of 3% per week like it used to be? Is it worth staking for 12% annualized while taking on Numerai price risk, then hoping the coin holds its value as yields halve again every couple quarters?

---

### Post #2 — **rlh** | 2021-10-27 11:44 UTC

In theory, a protocol like Numerai would figure out an intelligent way to incent top performers–thousands compete on Kaggle for a small chance at large payouts, but no one is going to put forward their own money to make 3%, which is 1% more than a naive public model.

The current argument about Sybil resistance doesn’t really fly–somehow every other machine learning platform has figured this out, and the best models win.

How hard would it actually be to, e.g. give out prizes within each tier of NMR staked (top model with more than 1 NMR staked, 10 NMR staked, 100 NMR staked, etc.). Why not reward actual Sharpe ratio or Sharpe * Corr–much harder to fake by taking on huge exposures–rather than Corr. It would seem any basic combination of these, requiring _some_ stake, using a volatility-adjusted return, or even longer-window prizes, solves this problem.

Absent that, it’s hard to see why any serious data scientist would have any interest as yields collapse. (And Numerai can expect the quality of the ‘signal’ to degrade accordingly.)

---

### Post #3 — **gammarat** | 2021-10-27 15:06 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/r/9de053/48.png) rlh:

> Is it worth staking a model where your 0.03 corr now pays 3% every two months (a year from now),

I’m fine with it; to a large extent I think the value of Tournament and Signals depends on how you use whatever you learn while participating here. Personally, and broadly speaking, I’ve had a long term interest in advanced signal processing (going back to the 80s) and have enjoyed using those techniques in financial markets (going back to the 90s). Numerai provides a great test bed to try out different approaches My own plan–and I started here in March–is to test the abstracted algorithms on Tournament, adapt them to real data via Signals (which pays better), and apply what I learn to my own portfolio (which pays best). I would ballpark my progress at being at about the halfway mark.

As for 3% per every two months, that’s still a decent rate of return.

---

### Post #4 — **eleven_sigma** | 2021-10-29 12:32 UTC _(reply to #3)_

Some insights:  
Doesn’t make sense to pay for predictions with lower corr than example prediction.  
Payment should begins at the level the benchmark reaches.  
In future, when the payment factor drops close to 0.2 the MMC multiplier perhaps will go to x3 or x4, so Numerai will pay unicity not naive correlation.  
As the hedge fund performance it is the first priority for Numerai, they should begin to use in the metamodel other criteria for weighting different than stacking. Performance track or performance in a blind test set. Otherwise the hedge fund will trade the predictions of 20 models with high stacking, that not necesary are the best models. This is a loss of efficiency.  
A mixed weighting based in stacking and performance is the way.

Finally, we know there are 3M of NMR blocked until 2028  
<https://medium.com/numerai/numerais-new-token-supply-7c34636929c>  
so treasury up to 2027 is aprox 2M?  
How Numerai will pay the tournments during 2022-2027 with only this amount available?

---

### Post #5 — **gammarat** | 2021-10-29 15:46 UTC _(reply to #4)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/e/8797f3/48.png) eleven_sigma:

> Doesn’t make sense to pay for predictions with lower corr than example prediction.

That’s actually more of a business decision than anything else, I would think. Allowing everybody to win at least a little something helps bring in new modelers. Some will get hooked, and some will create new and better models. People who don’t find they’re winning much in exchange for their effort will leave. The end result is a source of steadily improving models. At least I think that’s the plan ![:laughing:](http://forum.numer.ai/images/emoji/twitter/laughing.png?v=12)

Looking at model distribution might give some sense of what I’m talking about. There’s approximately 11000 models listed, of which 6,400 participated in the most recent round (287), and of those only 3,400 were staked. Using the payouts from the most recently completed tournament (283), only about 80 of those models would be earning a reasonable full time income from the Tournament. The whole thing is pretty Darwin ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

As for the MMC payouts, my _instinct_ (I still haven’t worked through the issue) is to run the meta-model once for each model, with the users’ stake weighted model removed. The difference between that result, and the full result, should be used to estimate the users contribution to the meta-model. Define a fixed total payout on the MMC aspect, and then divide that total payout up proportionally among those whose contributions were positive. Use those results to also burn the staked NMR of models with a negative contribution.

That approach though is probably full of holes, I haven’t thought too much about it.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/e/8797f3/48.png) eleven_sigma:

> so treasury up to 2027 is aprox 2M?  
>  How Numerai will pay the tournments during 2022-2027 with only this amount available?

By averaging less than ~8K NMR in payouts per week. I wouldn’t worry about that.

---

### Post #6 — **eleven_sigma** | 2021-10-29 17:13 UTC _(reply to #5)_

How do you work the statistics about models, earnings…? Where is available?

---

### Post #7 — **gammarat** | 2021-10-29 17:27 UTC _(reply to #6)_

The models in general I just take from the front page of the Tournament, the number of over all models is at the bottom.  
For numbers w/r to specific rounds, go to the “Account” tab, select “Models”, and that brings up the list of all your models. Below that you will see a box labelled “Recent Rounds” with four or five rounds listed in the first column. Click on one of those, that takes you to the results of that specific round. The number of submissions is again at the bottom.

If you go to specific round, the address bar will look something like this:  
https: [//numer.ai/round/286](<//numer.ai/round/286>)  
(but without the space between “https:” and the “[//numer.ai/round/286](<//numer.ai/round/286>)”.

changing to 286 to 287 will give you the most current round today…But you can poke around and look at other previous rounds as well, by changing the round number.

I suppose there’s ways of doing this via the API, but I’m pretty old school ![:older_man:](//forum.numer.ai/images/emoji/twitter/older_man.png?v=9)

---

### Post #8 — **lcrmorin** | 2022-08-30 10:34 UTC

It makes sense to pay for predictions with lower corr than example if they are uncorrelated.
