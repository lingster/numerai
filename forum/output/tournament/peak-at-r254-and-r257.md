---
title: "Peak at R254 and R257"
category: Tournament
url: https://forum.numer.ai/t/peak-at-r254-and-r257/3620
created_at: 2021-06-18T13:14:17.972000+00:00
last_posted_at: 2021-06-28T14:20:41.067000+00:00
posts_count: 6
views: 956
tags: []
---

# Peak at R254 and R257

---

### Post #1 — **autratec** | 2021-06-18 13:14 UTC

I haved checked some top trader’s performance on leader board. And found most of them r doing well at round 254 and 257.

What does it mean?

Assume all the participants using different model to prediction the future, this kind of consistency should not be there.

Or in that two rounds market, perform the majority of prediction, which is 0.5. which makes us feel the prediction is meaningless. We might just put all the prediction at 0.5.

---

### Post #2 — **autratec** | 2021-06-18 13:22 UTC

and i feel the CORR line following certain trend. For example, the coming R268 and R269, i expect most of traders will go into negative zone. so, if we have choice, better pull your NVM back. and wait for R270 to gradually add in NVM and increase the multiple of MMC again to get better return.

Let me know whether you have similar observation.

---

### Post #3 — **swarm** | 2021-06-18 14:02 UTC

Although we all have different models, we’re all using the same training and validation data, so it’s hard not to have correlation between models.

And you’re free to use a different model to generate your predictions each week. If you truly feel that your current model may generate negative returns for the round, you could swap it out for a different model. Which makes you a manual decision tree I guess. You can also ensemble different models.

One idea that I just had is maybe you can try correlating your model or the metamodel’s live returns with other indices, like the S&P 500, or VIX (volatility). Although the data is encrypted and we don’t know what the targets actually mean, I imagine there must be some correlation to something in the real market.

A possible hypothesis could be that when VIX is high and the market is volatile, your model with feature neutralization works better, but during other times maybe your model that has a higher max feature exposure works better. This is a hypothesis, please don’t use it in real life.

---

### Post #4 — **ssh** | 2021-06-18 14:35 UTC

254 & 257 were “easy” rounds for the majority of participants  
<https://numer.ai/round/254>  
<https://numer.ai/round/257>

round 264, that has just resolved, was also a relatively easy one  
<https://numer.ai/round/264>

we have a lot of time period shocks both positive and negative and as they are spreading over 4 weeks we could see a serial correlation between rounds.

Don’t overestimate the significance of this correlation. I was not able to use it to improve my performance (trying to manipulate stakes based on AR(1) components across rounds). my rule of thumb - keep your model stable for a long time (10s of weeks) to see how it behave in different regimes.

---

### Post #5 — **sdimov101** | 2021-06-28 07:33 UTC _(reply to #3)_

> One idea that I just had is maybe you can try correlating your model or the metamodel’s live returns with other indices, like the S&P 500, or VIX (volatility).

That is a very good idea. I have a trello card about correlate SPY to numerai rounds but never got to it. It seems difficult to lay the rounds on top of each other in a way produces a monthly report that can be correlated to any other index since every week a new round start.

How would you approach that?

---

### Post #6 — **gammarat** | 2021-06-28 14:20 UTC _(reply to #3)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/9de053/48.png) swarm:

> I imagine there must be some correlation to something in the real market.

I never thought to check this before (I’m very slow at these things), but just did for the current round–the eraX_live Tournament era, and the live_universe file for Signals, are the same length, 5400 elements. It wouldn’t surprise me if they were also in the same order.
