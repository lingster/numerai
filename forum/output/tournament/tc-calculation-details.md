---
title: "TC Calculation Details"
category: Tournament
url: https://forum.numer.ai/t/tc-calculation-details/5431
created_at: 2022-05-22T19:02:52.415000+00:00
last_posted_at: 2022-05-24T01:03:30.538000+00:00
posts_count: 3
views: 893
tags: []
---

# TC Calculation Details

---

### Post #1 — **dzheng1887** | 2022-05-22 19:02 UTC

Would anyone know exactly how TC is calculated? I have a general grasp of it as some gradient of the meta model return performance with respect to my stake size, if that is correct.

For example, I remember there was some illustration of how the meta model is combined from our predictions with our stakes. Could we view the detailed graph so we can analyze the back propagation? I don’t know what I’m looking for, or if I will uncover anything. I just want to understand TC better so I can think how to best optimize for it. The exact forward pass and backward derivative in math formulas would be ideal.

There have been discussions already to target FNCv3 or have low correlation with meta model. I think those are correct given the empirical evidence. I imagine they somehow target more obscure areas to provide the meta model with better balance. But I do not think it would be generally true all the time.

---

### Post #2 — **eleven_sigma** | 2022-05-23 08:25 UTC

The main problem with TC is it is calculated using only the portfolio.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png)

[Very, very strange TC behavior](<http://forum.numer.ai/t/very-very-strange-tc-behavior/5364/13>) [Tournament](</c/tournament/7>)

> Yeah markets are quite volatile at the moment and a metric based on portfolio returns (i.e. the returns of a subset of the stocks) is going to be much choppier than correlation to a normalized target across all stocks. With lots of stocks making double digit moves such things are to be expected. 

We optimize an universe of 5K instruments and then Numerai pick up 100 instruments (I don’t know exactly the number).  
The sampling (selection of instruments) is the key of the problem.  
If you have 5K instruments with correlation of 0.06 and sample 100 instruments, the distribution of correlations you will get has a high volatility.  
Only if you could get correlations in order of 0.8-0.9 the sampling would work.  
So the ploblem hasn’t solution. TC can be the perfect metric from a statistical point of view to the perspective of the challenge maker (average matters), but from individual perspective (variance matters) is horrid.

---

### Post #3 — **dzheng1887** | 2022-05-24 01:03 UTC _(reply to #2)_

But TC doesn’t depend on the sample of 100 does it? Like if you rank a stock as a buy that is not included in the 100 (because most others have it as a sell), and that stock does well, you still get TC from that correct? Because if you had increased your stake then that stock eventually makes it in the meta model and helps with returns.
