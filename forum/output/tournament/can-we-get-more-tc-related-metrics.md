---
title: "Can we get more TC related metrics?"
category: Tournament
url: https://forum.numer.ai/t/can-we-get-more-tc-related-metrics/5664
created_at: 2022-08-23T15:18:54.604000+00:00
last_posted_at: 2022-08-27T19:21:26.401000+00:00
posts_count: 5
views: 1086
tags: []
---

# Can we get more TC related metrics?

---

### Post #1 — **kayeffnumeraitor** | 2022-08-23 15:18 UTC

They way it is right now when my model has low TC in a round, I don’t know whether

  * i got unlucky because TC is noisy
  * others started to stake high amounts on similar predictions
  * my model is bad



Can we get metrics that solves these issues? Here are my suggestions:

  * TC pre-portfolio selection or mean TC over lets say 100 toy portfolios to reduce noise
  * TC if my model would be the only model in the meta model



The first could actually be very closely related to FNC / FNCv3 and the latter to MMC, however I cannot verify that.

---

### Post #2 — **mdo** | 2022-08-24 20:17 UTC

I hear you and we will revisit related metrics at some point.  
But to address your points, TC is in fact not a noisy estimate. TC is calculated by dropping out 1/2 of the stakes 100 times to create 100 portfolios and then calculating the gradient of returns with respect to stakes for all 100 portfolios and then averaging those 100 gradients. Repeating this with a different random seed gives results over 99% correlated.

What _is_ noisy is stock returns. Their heavy tails effect real life stock returns (and therefore TC) much more than you might guess from the ranked correlation of predictions and stock returns.

Also, it would require pretty substantial stake moves by others to really effect your TC. It’s not something I’d worry about or try to attribute on a round to round basis. But if your TC is low for a while you might want to do something more original.

It’s basically impossible to evaluate a model based on one round. My advice is to trust your CV and let it ride. I was definitely guilty of lots of switching up models round to round, but that was before there were lots of model slots. So use them!

TC as currently calculated doesn’t make sense for only one stake, but we could show your portfolio return for the portfolio created if you were the only one in the metamodel. We experimented with this originally, but iirc it wasn’t that helpful for predicting TC as it doesn’t capture at all the interaction with everyone else. But I will definitely reevaluate when I revisit TC.

---

### Post #3 — **kayeffnumeraitor** | 2022-08-25 09:23 UTC _(reply to #2)_

Thanks for the reply.

In hindsight I should have read your [initial post about TC](<http://forum.numer.ai/t/true-contribution-details/5128>) more carefully.

I think I was under the wrong assumption that your optimizer would be selecting the stocks for the final portfolio prior to looking at the meta model predictions and then apply the calculations based on the reduced set of stocks. In this scenario it made intuitively sense to me that being correlated to the target under as many viewpoints as possible (high FNC), would lead to a high TC, provided the prediction is unique enough.

However, it seems to me that a high exposure to a particular feature can lead to the optimizer systematically dropping out those predictions you were correlated to begin with, leaving basically some uncorrelated or even systematically anti correlated predictions. Which seems to be the better reason for the importance of FNC.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> What _is_ noisy is stock returns. Their heavy tails effect real life stock returns (and therefore TC) much more than you might guess from the ranked correlation of predictions and stock returns.

The real reason I was under the assumption TC is noisy is because [one of my models](<https://numer.ai/kayeff_random>) submits random numbers and has a wide range of TC results. While the averaged TC is actually negative, I was not expecting it to provide any “contribution” in any round.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> But if your TC is low for a while you might want to do something more original.

Is there a timeframe defining “a while”? I have other models that seem to have rather inconsistent TC results, like having 9 rounds of positive TC and then a long streak of negative TC, eating up the cumulative TC from the previous 9 rounds.

I really like the essence of TC, and obviously I am still experimenting, but somehow it feels a little bit like driving with no dials and a muddy windscreen, having only the rearview mirror available.

---

### Post #4 — **dd_dd** | 2022-08-25 10:06 UTC

Regarding more diagnostics,  
wouldn’t backfilling TB200 or other (trainable) diagnostics from [@mdo](</u/mdo>) 's post be simple and super useful to everyone?

---

### Post #5 — **sunkay** | 2022-08-27 19:21 UTC _(reply to #2)_

Is is possible to calculate historical portfolio return for if my model were the only model in the meta model in cross validation period?
