---
title: "Do really someone feel comfortable with TC?"
category: Tournament
url: https://forum.numer.ai/t/do-really-someone-feel-comfortable-with-tc/5457
created_at: 2022-06-02T21:37:03.375000+00:00
last_posted_at: 2022-06-03T23:16:30.637000+00:00
posts_count: 7
views: 1045
tags: []
---

# Do really someone feel comfortable with TC?

---

### Post #1 — **eleven_sigma** | 2022-06-02 21:37 UTC

Last round we see the Totally_random model getting:  


[![random](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a0a8637963fdb89c8c897439faf9dfcea3d82868_2_690x484.jpeg)random915×643 55.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a0a8637963fdb89c8c897439faf9dfcea3d82868.jpeg> "random")

All metrics consistently negative and TC in percentile 97-99.

This is my model in last round:  


[![model_1](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e73a0ba2a1f5d0e9c524d6a6831e66c8ca1c23a1_2_690x236.jpeg)model_1917×314 29.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e73a0ba2a1f5d0e9c524d6a6831e66c8ca1c23a1.jpeg> "model_1")

All metrics consistently in 95-99 percentile, and poor TC.

Are numeraire people comfortable seeing a random submission getting 97-99 percentile?

I will put my two cents…

TC is computed using a gradient in a layer of the optimization framework.  
I don’t know more details but I think the problem is TC is overfitted to the optimization process.

Let me use a more familiar example.  
All of you know the built-in feature importance of lightgbm or xgboost are biased towards some variables that are overfitted in the training and / or have a big cardinality.  
This is the reason why we use permutation based feature importance, that uses a fresh dataset instead of training dataset.  
If we add a random feature to a dataset and fit a model, built-in feature importance of it will be positive and probably a big value if the dataset have low level of signal and big level of noise (like numerai datasets).  
Returning to TC I think using the training values of TC they are overfitting it, so if you use random predictions you have a high probability to get high TC.  
As for feature importance we need to use a fresh dataset, for TC computing should be good to do something similar and don’t use the same data for adjust the metamodel and compute the TC.

---

### Post #2 — **rigrog** | 2022-06-02 22:44 UTC

I’m not exactly _comfortable_ with TC, but I am kind of liking it.

My models (rigrog and riglax) are getting high TC (shoulda staked on it!), and _negative_ correlation with the meta-model. Go figure.

---

### Post #3 — **jefferythewind** | 2022-06-03 14:32 UTC

For your second example there, I wouldn’t say you’re getting poor TC, .025 isn’t that bad. It definitely is a big experiment they are doing with it. The score is in fact the gradient of our stake w.r.t. the portfolio return. The thing that is hard for us to grasp is how the optimizer is augmenting our predictions before computing. What I am thinking is that more people are giving predictions close to your main model, and hardly any are submitting random predictions that match yours. Hardly anyone is staking heavily on purely random predictions, so the existing weights for this kind of prediction are basically zero in the portfolio. So it’s saying random staked predictions would be high TC for this particular round. If they gave your stake more weight, they would have done better. If a large portion of the community was actually staking on random predictions, I think your score here would be much less.

What has been preoccupying my mind is that this gradient reading is non-linear and very much depends on the simulated stake value they give to our submissions. You’re aren’t staking on the random predictions, so they need to assume some stake value for your predictions, and they calculate the gradient **at that stake value**. I’m pretty sure they assume a fairly low stake value here.

The gradient is non-linear, it will be wildly different depending on this assumed stake value. If they first assumed your model’s stake was 90% of entire round, I think the gradient (TC) value would be much lower, since increasing your stake from 90% would make negligible difference on the returns, and probably increasing other stakes (of the remaining 10%) would make a better improvement.

---

### Post #4 — **d3monw3st** | 2022-06-03 16:48 UTC

The volatility with TC has led me to stop staking on it. I’ve seen some of my models yo-yo between <5% to >95% between rounds and I don’t have the stomach to hang on.

---

### Post #5 — **richai** | 2022-06-03 19:11 UTC _(reply to #3)_

if your stake is 0 we actually assume it’s 0 for computing TC – the gradient is saying for a small change above 0 how much will your model help post-optimized portfolio returns of the stake weighted meta model.

---

### Post #6 — **richai** | 2022-06-03 19:22 UTC

Certainly, in rounds where the stake weighted meta model performs very badly a random submission could have very positive TC. But I like the totally_random account and I think in future versions of TC we might want to consider caring about random submissions having low TC variance in normal rounds.

The reality is with the current optimizer settings, individual signals (especially uncorrelated ones like random signals) can peturb the resulting optimization with large effects on the portfolio returns (eg a single submission can help us avoid just one short which ends up going up 100% in a month which would have large effects on the optimized portfolio returns).

---

### Post #7 — **ark** | 2022-06-03 23:16 UTC

Hey, thank you for posting about TC. It’s valuable for everyone to scrutinize and improve the system and this is a great check to have. If I may, I’d like to summarize some points made in this thread and add a few points:

  1. You’ve cherry-picked a single round in which a random model performs well. The results of a single round are calculated on compounding performance. Meaning that a random lucky portfolio can look less random than it actually is especially at 0 stake. I could cherry-pick a different round for the opposite argument:



Look how well it performs in 313 across all metrics:  


[![Screen Shot 2022-06-03 at 3.23.04 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/0d27c9c18bb985e1aac79406f46ec702b5418072_2_465x500.png)Screen Shot 2022-06-03 at 3.23.04 PM933×1003 107 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0d27c9c18bb985e1aac79406f46ec702b5418072.png> "Screen Shot 2022-06-03 at 3.23.04 PM")

Or look at round 315, the round after the one you show, in which it performs terribly:  


[![Screen Shot 2022-06-03 at 3.47.02 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e0fd3932b5918a70f1cc5a612c6c32659aec3072_2_514x500.png)Screen Shot 2022-06-03 at 3.47.02 PM933×907 91.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e0fd3932b5918a70f1cc5a612c6c32659aec3072.png> "Screen Shot 2022-06-03 at 3.47.02 PM")

  2. Overfitting isn’t necessarily what’s happening. We aren’t using a large, complex model to calculate TC so overfitting does not really make sense.

  3. Noise sometimes helps during rounds in which people perform poorly, but sometimes it hurts. Here is the Final TC per round of two random models I backfilled while doing some research. Here, I use integration_test as a proxy for round difficulty. Notice that sometimes the TC scores of random noise have positive correlation and sometimes negative:




[![Screen Shot 2022-06-03 at 4.12.08 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/2ee88737b8d5c20fde7e266eb165abeb2181f28e_2_317x500.png)Screen Shot 2022-06-03 at 4.12.08 PM550×865 54.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2ee88737b8d5c20fde7e266eb165abeb2181f28e.png> "Screen Shot 2022-06-03 at 4.12.08 PM")

Let me know if anything is still unclear or if you feel I left some questions unanswered.
