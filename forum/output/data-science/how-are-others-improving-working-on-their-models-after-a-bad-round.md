---
title: "How are others improving/working on their models after a bad round?"
category: Data Science
url: https://forum.numer.ai/t/how-are-others-improving-working-on-their-models-after-a-bad-round/3364
created_at: 2021-05-20T18:08:58.383000+00:00
last_posted_at: 2021-06-23T06:08:21.675000+00:00
posts_count: 7
views: 1303
tags: []
---

# How are others improving/working on their models after a bad round?

---

### Post #1 — **jaam** | 2021-05-20 18:08 UTC

Hi - I’ve seen quite a few posts on here and Twitter about users putting a lot of work into their models and continuously making improvements to them. I’m curious, what are people doing / what does this entail?

For example, I did a rough analysis on everyone’s results in round 260 of the main tournament and it looks like there was more NMR burned than paid out for the first time in a few months (~2k net NMR burned). Even a huge chunk of the top 100 models lost NMR in round 260. So what does this mean for your model? How would you identify what went wrong and improve on it? And if you change your model, how do you know it will be better than your current one? (all of these questions are assuming you’re already happy with your val diagnostics)

I’m still fairly new, but so far my model has decent diagnostics on val and has done fine on live data. If I have a bad round, does that mean I should go back to try and build a model with better val diagnostics?

---

### Post #2 — **jimmy_woodford** | 2021-05-20 21:52 UTC

In general, I would not put too much weight on one round. You need a lot more observations to get an idea of your model’s quality.

However, if you experience one or more weeks in which your performance is a lot worse than your worst performance on your internal validation, this is an indication that you are overfitting your validation data or that your validation data is not very representative of the live data. In that case, I would reasses my model-building pipeline.

Mind you, both of these issues are hard to avoid. To avoid overfitting your validation data, you can use cross-validation on the training data and only rarely compare models on the validation data. You can also designate validation as well as test data: use validation data for early-stopping and other decisions and use test data only for final model selection. What data is representative of live data? Who knows? One thing you can do is look at historical live performance of other long-term participants. Then split your data into a couple of folds and run a couple of models to get an estimate of performance on the different eras in your data. Pick eras on which your models perform roughly as well as the average participant has in the last few years (corr and sharpe)… or, if you’re more optimistic, pick eras that reflect performance on the whole dataset you have available.

These are just a few ideas, decide for yourself what works and makes sense.

---

### Post #3 — **gammarat** | 2021-05-21 02:43 UTC

It led me to start making synthetic “training* (I use the word loosely as I’m not using NNs) data that on a broad statistical basis is the same as the real training data, but on a narrower basis is more closely aligned with the test data. The big thing that caught my eye was that the variance in the various feature groups in the training data is significantly different from that in the test and live data. I wrote a bit about it in this thread, and what I learned from that seems to have improved my modelling.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gammarat/48/3281_2.png) [Analyzing Training Data](<http://forum.numer.ai/t/analyzing-training-data/3143>) [Data Science](</c/data-science/5>)

> I’ve been playing around with the feature groups a bit, and two things popped out having to do with the standard deviations of the features. Referring to these plots: [[RawDataVariances]](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c075c83bf685b69c53cb6bfc3f6967c9f66548ed.jpeg> "RawDataVariances") The numbers down the side of the first plot are feature numbers, down the side of the second plot they are simply levels. Sorry about the mess. Across the bottom are file numbers from 1 to 148. 1 to 120 are training data era, 121 to 148 are validation. In the first plot, I just took the standard deviation of…

---

### Post #4 — **put** | 2021-06-22 00:10 UTC

it’s simple!  
Just trust ur local CV!  
This is famous in Kaggle.  
If your machine learning process is correct, you shouldnt change your model.

---

### Post #5 — **liz** | 2021-06-22 22:35 UTC

I think that tweaking a model(s) because of 1 bad round is a grievous error of judgment, and quite clearly what is referred to as “results-oriented thinking” in the professional gambling community. Confidence in a model should be established (by whatever means, CV, live testing, etc) before staking a substantial amount, and changes should indeed be made, but modelers should expect a bit of variance in round-by-round performance due to the nature of the problem we’re competing about. I think it makes sense to make a snappy change because you’ve realized a major error, found a major improvement, or the parameters of the tournament have changed. But responding to a single (large) loss by changing things up is (in my opinion) optimizing risk at the cost of returns and informed model preparation, as well as training the modeler themself to forsake their own process of vetting models (scrapping what you have because of one bad round is an invalidation of whatever process was used for the modeler to put the model in play in the first place)

---

### Post #6 — **wigglemuse** | 2021-06-22 23:02 UTC

There is a gambler’s phrase to sum this up: “Don’t get caught in the switches.”

---

### Post #7 — **sneaky** | 2021-06-23 06:08 UTC

Market is imperfect information game, that is prone to be often irrational. I like the phrase “In the short term, market is voting machine. In the long term, market is weighing machine.” So, your model cannot be right about the market all the time.
