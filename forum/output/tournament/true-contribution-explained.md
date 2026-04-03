---
title: "True Contribution explained"
category: Tournament
url: https://forum.numer.ai/t/true-contribution-explained/4808
created_at: 2022-01-17T12:59:31.252000+00:00
last_posted_at: 2022-01-19T03:06:32.613000+00:00
posts_count: 14
views: 1873
tags: []
---

# True Contribution explained

---

### Post #1 — **nyuton** | 2022-01-17 12:59 UTC

What is TC and how is it calculated? Can someone shed some light on it? I can’t find any documentation on this topic.

Thanks

---

### Post #2 — **jay1100** | 2022-01-17 15:53 UTC

They did some explanation in the latest fireside chat:  


And more documentation will come in the future.

Basically TC is looking at the performance of the stake weighted meta model with and without your model (your model gets a fixed weight of 1% in the meta model. So it does not depend how much you staked on it for the TC calculation)

So you can not really calculate it locally on your validation data / cross-validation. Doing proper data science will be difficult. It seems the only thing you can do is to look at the live data. This of course has super high turn around times because you need to have your model running for several month before you have enough rounds for proper evaluation.

I think from the perspective of numerai TC makes perfect sense. But from the perspective of a data scientist it seems to make it impossible to run any experiments with reasonable turnaround times.

---

### Post #3 — **wigglemuse** | 2022-01-17 21:15 UTC

They could make a tool using real past rounds with the real metamodel from those rounds to help evaluate TC. Seems like they also need to come up with a more stable version of TC itself.

---

### Post #4 — **jay1100** | 2022-01-18 08:46 UTC _(reply to #3)_

I think building such a tool is not easily possible: They were saying that calculating TC is very computationally expensive because they run the meta model optimizer for each submission (For each submission they calculate a “new” meta model and compare if it is better or worse than their real meta model).

---

### Post #5 — **eleven_sigma** | 2022-01-18 12:27 UTC

First impressions are that new metric is extremely volatile and sometimes uncorrelated with CORR (this could be reasonable) but with MMC too (that is a major problem).  
If I understood well, TC is computed doing bootstrapping, computing a metamodel, computing its performance, and repeating this process several times. Then the TC is the mean of performance in the runs in which a model is vs the runs in which is not (something like this, I think).  
The accuracy of this metric depends of the variance of the result of each run of bootstrapping.  
I hope Numerai computes the confidence interval of TC using the sd of each estimation (run of bootstrapping) and checks the wide of the interval is small. Othervise they will need other approach or increase the number of runs.

---

### Post #6 — **mic** | 2022-01-18 13:18 UTC _(reply to #5)_

[@eleven_sigma](</u/eleven_sigma>) why would TC being uncorrelated with MMC be a major problem?

---

### Post #7 — **eleven_sigma** | 2022-01-18 14:37 UTC _(reply to #6)_

If TC is highly uncorrelated with MMC how do you test your models are good?  
Imagine in future the payment is based only in TC…

---

### Post #8 — **rigrog** | 2022-01-18 14:54 UTC _(reply to #2)_

“TC is looking at the performance of the stake weighted meta model with and without your model”

That sounds to me, just like the explanation of MMC, absent some details. From the ancient scrolls:

# 

Calculation

To calculate a user’s (U) `mmc` for a given round we

  * select a random 67% of all staking users (with replacement)

  * calculate the stake weighted predictions of these users

  * transform both the stake weighted predictions, and U’s model to be uniformly distributed

  * neutralize U’s model with respect to the uniform stake weighted predictions

  * calculate the covariance between U’s model and the targets

  * divide this value by 0.0841 (this step is to bring the expected score up to the same magnitude as correlation)

  * the resultant value is an MMC score

  * repeat this whole process 20 times and keep the average MMC score

---

### Post #9 — **wigglemuse** | 2022-01-18 16:19 UTC _(reply to #4)_

If they can compute it every day for all models, they can certainly compute it on demand for a few rounds when you submit some test predictions (even if it isn’t instant). Another idea is for those previous live rounds is to not only release the targets, but the blended metamodel predictions. Then we could estimate TC ourselves. (Releasing the metamodel predictions might be controversial.)

---

### Post #10 — **wigglemuse** | 2022-01-18 16:19 UTC _(reply to #8)_

That was the original version of MMC (the current version uses residuals), and yes it does sound very much like that.

---

### Post #11 — **of_s** | 2022-01-18 21:08 UTC _(reply to #8)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/r/dec6dc/48.png) rigrog:

> “TC is looking at the performance of the stake weighted meta model with and without your model”

How is performance defined and evaluated…Sharpe, average returns, something else?

---

### Post #12 — **rigrog** | 2022-01-18 22:06 UTC _(reply to #11)_

Not sure… I think it’s Spearman correlation.

---

### Post #13 — **wigglemuse** | 2022-01-18 22:14 UTC

It is going through the optimizer and is scored in basis points, so evaluated like real trades not a proxy metric sounds like.

---

### Post #14 — **aventurine** | 2022-01-19 03:06 UTC

It would be interesting to see once TC calculation bugs are squashed what the distribution of TC to Stake sizes looks like over time. That would be more interesting to than TC vs CORR or even TC vs FNC
