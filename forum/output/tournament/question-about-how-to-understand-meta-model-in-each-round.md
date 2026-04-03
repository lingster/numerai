---
title: "Question about how to understand Meta Model in Each Round"
category: Tournament
url: https://forum.numer.ai/t/question-about-how-to-understand-meta-model-in-each-round/3242
created_at: 2021-05-06T21:53:00.160000+00:00
last_posted_at: 2021-05-07T18:03:47.209000+00:00
posts_count: 8
views: 784
tags: []
---

# Question about how to understand Meta Model in Each Round

---

### Post #1 — **pwang24** | 2021-05-06 21:53 UTC

Hi,

I am wondering how should I understand the numerical value of the correlation score for each updates. For instance, for each day, we will get the updates for the numerical correlation value for each rounds. As my model is still developing, my model for each rounds is always different…

As we usually have 4 values (one for each rounds) for every day updates, I am wondering, so, is the correlation is dealing with same Meta-Model? Or different one?

For instance, my round 1 have a lower correlation but higher MMC, my round 2 have a higher correlation but lower MMC. I am thinking to ensemble them together by assigning some weights, but are they dealing with same model or not when taking about the correlation?

Thank you.

---

### Post #2 — **wigglemuse** | 2021-05-06 23:01 UTC

You will notice that your “corr w/ metamodel” for each round never changes – the metamodel is the ensemble made of all staked models, and weighted by those stakes. So once each round is started and stakes are in, that’s the metamodel for that round, it doesn’t change. What does change every day is the real stock market, and the therefore the ground truth of the targets we are predicting, i.e. the “answers” to the question we are asked change everyday, but only the final day of each round actually counts for our score that round – all the other days were just for fun looking at. So think of it like you are predicting the spread of an in-progress basketball game – each update tells you what your final score would be _IF_ the game ended right now. But only the actual real end of the game and your final result actually count.

---

### Post #3 — **pwang24** | 2021-05-07 03:12 UTC _(reply to #2)_

[@wigglemuse](</u/wigglemuse>) Thank you for sharing the thoughts. It looks Meta model will be different between different rounds based on stakes. Yeah, I understand the final result based on the resolved date. But I think try to understand whether there are positive correlation between the stock market vs the daily return I can get. For instance, recently the market is kind of volatile, it helps to understand if for certain rounds, there are positive correlation and certain rounds, it is negative correlation.

---

### Post #4 — **wigglemuse** | 2021-05-07 15:10 UTC

Any correlation you notice between the real market and your performance or the general performance of everybody is mostly spurious.

---

### Post #5 — **pwang24** | 2021-05-07 15:21 UTC _(reply to #4)_

[@wigglemuse](</u/wigglemuse>) I am trying to understand whether I can observe any real market performance and the performance of my models. For instance, I have a ensembled NN models as a basis line, which accounts for 90-95% of the weight for my submission. And starts to blend in different models like XGboost or some random models for different weight. Then, for my round 261, suddenly the correlation and MMC get a 92 percentile rank yesterday. while my round 262 is around 80 and 78 rank. Because the difference between 2 rounds is 5% weight for XGBoost. In addition, my round 261 is not performing last week, and gradually increasing this week. So, I am start to think, whether there are certain models more suitable for volatile market and certain models are suitable for increasing market. Yeah, I also try to see my performance with the overall performance as well. But looks like if the weight for the Mega Model is based on the staked NMR, the correlation between different rounds more like for reference looks like.

Because overall speaking, due to the stimulus, kind of expecting the market is increasing for sure in the long term.

---

### Post #6 — **wigglemuse** | 2021-05-07 15:36 UTC

The fund is market neutral, and so the tournament is designed to be as well. Trying to predict how our models are going to do based on what the market is doing…hasn’t worked out for anybody. Sometimes you’ll think you see a pattern, then it will stop being a pattern.

---

### Post #7 — **pwang24** | 2021-05-07 15:46 UTC _(reply to #6)_

[@wigglemuse](</u/wigglemuse>) Thank you for sharing. Out of curious, hmm, the market neutral here means regardless of the price movement? For instance, it seems hard for me to understand.

For instance, from a portfolio perspective, market neutral usually refers to delta neutral. If the model is market neutral and the meta-model is based on all the staked model, it does not seems so, as the overall performance is dropping a lot recently.

But yeah, for sure, no pattern works for long…I think it is like the model performance is decreasing if submit the same model for different rounds…

---

### Post #8 — **gammarat** | 2021-05-07 18:03 UTC _(reply to #6)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> The fund is market neutral,

Well, it’s _designed_ to be market neutral, but as Robbie Burns put it:

> But Mousie, thou art no thy-lane,  
>  In proving foresight may be vain:  
>  The best laid schemes o’ Mice an’ Men  
>  Gang aft agley,  
>  An’ lea’e us nought but grief an’ pain,  
>  For promis’d joy!

![:thinking:](http://forum.numer.ai/images/emoji/twitter/thinking.png?v=12)

But seriously, has anyone looked at this in any depth? I’d be curious if there’s a financial equivalent to the [Reynolds Number](<https://en.wikipedia.org/wiki/Reynolds_number>) in fluid dynamics that could be used to separate orderly from more chaotic market periods, and whether that could be applied to the Tournament.

Added: Actually, there do seem to be researchers working on such with the markets, judging by the hits returned by Googling “Reynolds number for stock markets”. But they seem (to me) at first glance to be heavily involved in mirroring the specifics of the underlying physical theory.
