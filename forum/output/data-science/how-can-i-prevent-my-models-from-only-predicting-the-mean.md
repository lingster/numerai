---
title: "How can I prevent my models from only predicting the mean"
category: Data Science
url: https://forum.numer.ai/t/how-can-i-prevent-my-models-from-only-predicting-the-mean/3535
created_at: 2021-06-06T09:31:54.495000+00:00
last_posted_at: 2021-06-06T16:45:04.803000+00:00
posts_count: 3
views: 1047
tags: []
---

# How can I prevent my models from only predicting the mean

---

### Post #1 — **by256** | 2021-06-06 09:31 UTC

I’m fairly new here and have recently had a great time participating in this competition.

One thing my models struggle with is predicting across the entire target distribution. I have experimented with a variety of model types and their predictive distributions are always fairly tightly centred around 0.5.

Does anyone have any tips to mitigate this problem?

---

### Post #2 — **ml_is_lyf** | 2021-06-06 09:57 UTC

I think we’d need some more information on your current model to give you advice. The reasoning can be quite different depending on what kind of model your using. I only use neural nets, and I found when I first started I saw a similar pattern. For me at least I think it was because I was using mean square error as the primary component of my loss function, and of course, if you’re trying to predict a dataset as complicated as this, the model can do a lot better sitting around the mean than making extreme guesses and getting large penalties. If you’re using boosted trees/neural nets you could try a different loss function. My model no longer has this behaviour, I’m pretty sure it’s because my loss function is now mostly calculated from the correlation of the predictions with the ground-truths for each era, which of course makes training less sensitive to individual predictions.

Also bear in mind that scale doesn’t affect correlation, so if you scaled your current predictions to be between 0 and 1, you’d have the same correlation, so it isn’t necessarily terrible having them all packed tightly on the mean. I guess unless it’s happening because your model is struggling to learn anything useful, then it’s a problem. So I’d be more concerned about your performance and risk metrics than how tightly centred it is on the mean.

This explains nicely why scale isn’t important for correlation:  
<http://rstudio-pubs-static.s3.amazonaws.com/318113_6581029a53064b988b700fc3eee55864.html>

---

### Post #3 — **gammarat** | 2021-06-06 16:45 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/by256/48/3317_2.png) by256:

> Does anyone have any tips to mitigate this problem?

This doesn’t matter as long as your upload file is done with high enough precision to separate individual results.

It used to bother me as well until [@wigglemuse](</u/wigglemuse>) and others straightened me out. And if you look at the tournament in terms of a stock model, expecting stocks to stay close to their relative return rank over a four week period is usually reasonable. (How’s that for a squishy statement,![:laughing:](https://emoji.discourse-cdn.com/twitter/laughing.png?v=14) )
