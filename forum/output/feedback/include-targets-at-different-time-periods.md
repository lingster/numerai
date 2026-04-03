---
title: "Include targets at different time periods"
category: Feedback
url: https://forum.numer.ai/t/include-targets-at-different-time-periods/1297
created_at: 2020-12-13T11:41:45.046000+00:00
last_posted_at: 2020-12-15T11:51:37.460000+00:00
posts_count: 15
views: 1113
tags: []
---

# Include targets at different time periods

---

### Post #1 — **tchaye59** | 2020-12-13 11:41 UTC

Hi, everyone! I’m new to numerai and preparing for my first tournament.  
The dataset contains only one **target** column and all my models easily overfit it.  
Could numerai include targets at different time periods? Preferably, when the trade is executed to the main target period. I think this will help a lot to regularize our models.

---

### Post #2 — **wigglemuse** | 2020-12-13 15:51 UTC

Yes, so the target for each round is 20 trading days out from when we get the data, i.e. we are predicting 20 trading days into the future. (As far as we know, we are just predicting a future snapshot of a particular day and only the state of things on that single future day matter to our final score. But we don’t actually know that for sure, I keep meaning to ask about that and see if they will confirm.) So what are you asking for then is for targets to be included for some of the intermediate days also?

---

### Post #3 — **tchaye59** | 2020-12-13 17:51 UTC _(reply to #2)_

This is exactly what I mean. If the main target is after 20 days I think they could at least include the target at day 5,10,15.

---

### Post #4 — **wigglemuse** | 2020-12-13 22:29 UTC _(reply to #3)_

Interesting. I think there is basically zero chance of them doing that, but it is an interesting idea nevertheless.

---

### Post #5 — **lackofintelligence** | 2020-12-13 23:07 UTC

But I think we have discussed many times before the information value of those intermediate states; those ‘targets’ are just noise.

For just a minute, let’s assume that those targets actually contain some useful information (proof by absurdity going on here). Now let’s think about what would be needed to completely characterize a target:

  1. the actual final resolved outcome,
  2. the set of all possible outcomes of the 3 intermediate days.



Let’s just assume that we can bin the intermediate days into 5 bins, just as we do for the target itself. Now then, for each set of unique features X, we need about 5^3 = 125 as much data in order to fully characterize outcomes. But we can’t get all of that data, even if Numer.ai would go through the hassle to go back and pull out the intermediate states. Since the actual data covers \frac{1}{125} of the phase space, it is likely that models trained on the additional data would be much more vulnerable to new and novel permutations of market regimes.

---

### Post #6 — **wigglemuse** | 2020-12-13 23:26 UTC _(reply to #5)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/lackofintelligence/48/774_2.png) lackofintelligence:

> much more vulnerable

more vulnerable or less vulnerable?

I do think there is useful information there. Just taking some intermediate day on its own it is useful to know that the ordering was such-and-such _ever_ whether it ended up in a similar state on the final day or not. It is sort of like synthetic data – it may not have ended up that way but it plausibly could have so it would help us explore market regimes that may not have even happened yet. But even if they thought it was a great idea, giving us the path the targets took to the final day would probably be too close to being a data leak for them to provide that. I just doubt anybody could convince them to make it a big priority unless Richard reads this thread and thinks it is the best dang thing he never thought of.

---

### Post #7 — **lackofintelligence** | 2020-12-13 23:31 UTC

More.

The issue is that selecting out a tiny portion of a very large phase space could lead to bad predictions if and when the market changes or fluctuates. If we had access to all of the phase space then I would agree with you.

---

### Post #8 — **tchaye59** | 2020-12-14 01:42 UTC _(reply to #5)_

I think you’re wrong. We will not need more data if intermediate days where included. Existing one will just contain one column for the main target and maybe tree other columns on intermediate targets. I also think a model trained to consider patterns in these different targets will be much more robust.

---

### Post #9 — **tchaye59** | 2020-12-14 01:54 UTC _(reply to #8)_

Also, given that targets are normalized in only 5 bins that we know nothing about, I don’t think there is a great risk of leakage from traded instruments.

---

### Post #10 — **lackofintelligence** | 2020-12-14 02:07 UTC

I am not saying that this data is not possible to use, just difficult because we don’t have as many examples as we might need. Think about a way to use that data. For example I will give two ways to use that data:

Method 1:

  1. Train models to predict those columns.
  2. Use those predictions as features with another model that then just predicts the target
  3. On live data first run the first predictor to produce the new features, then use the final model to predict the resolved target.



Method 2:

  1. Train a neural net to predict the intermediate outputs and the final outputs
  2. On live data only use the prediction for the resolved target.



Now what happens if, using either method, the intermediate days predictions are wrong? Then isn’t it the case that the resolved column has a higher probability to be wrong?

I won’t argue further, I think the phase space argument encapsulates the above thought experiment.

---

### Post #11 — **wigglemuse** | 2020-12-14 02:07 UTC _(reply to #9)_

It might allow you in some cases to correlate a row with a particular stock. I believe they are actually contractually obligated to keep the data obfuscated so that is probably not an area where they are going to take chances.

And so while it might be useful, it is hard to make an argument that it is _necessary_. As far as overfitting, there are plenty of other ways to combat that. Keep plugging away…

---

### Post #12 — **tchaye59** | 2020-12-14 02:56 UTC _(reply to #10)_

You’re right. Using it that way will require more samples. It will be much more efficient to train a neural networks to predict the final output and use those intermediate output to help in regularizing the training.  
Anyway thanks for your clarifications

---

### Post #13 — **richai** | 2020-12-14 09:54 UTC

Good question. On Numerai Signals (<https://signals.numer.ai>) we give out a weekly target. For Signals, we care only about that prediction time horizon. I think I saw that the Kaggle Jane Street competition has multiple target horizons which seemed interesting and important for them. Since we’re just getting started with weekly targets with Signals and just created a new target for Numerai, I don’t think we’ll have any new ones soon but I think at some point we will.

---

### Post #14 — **lackofintelligence** | 2020-12-14 17:27 UTC

Come to think of it the phase space problem could be reduced and the obfuscation issue could be mitigated by just giving the direction of the maximum deviation over the course of the 20 training days. That would still double the phase space, but much less than 125. For a factor of 3 hit in the phase space you could even introduce a crude magnitude of the deviation. I wonder how much that would help regularize the training compared to the phase space hit.

---

### Post #15 — **belzebot** | 2020-12-15 11:51 UTC _(reply to #14)_

I agree with the state space argument, yet I don’t come to the same conclusions. At the end of the day it is an opportunity for users to come up with different solutions and approaches that would lead to a more diverse set of predictions for the meta model. For example you could just build a model that would desregard it…
