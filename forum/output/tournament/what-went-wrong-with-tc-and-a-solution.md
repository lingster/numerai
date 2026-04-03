---
title: "What went wrong with TC and a solution"
category: Tournament
url: https://forum.numer.ai/t/what-went-wrong-with-tc-and-a-solution/5554
created_at: 2022-07-03T15:03:27.805000+00:00
last_posted_at: 2022-07-07T08:23:22.920000+00:00
posts_count: 16
views: 1528
tags: []
---

# What went wrong with TC and a solution

---

### Post #1 — **taori** | 2022-07-03 15:03 UTC

Since Numerai’s hedge fund portfolio is weighted accordingly to the stake value of the models, the more they are valuable to the hedge fund the more their stakes have to increase. That enables a feedback mechanism where the most useful models are most rewarded and consequently they increase their hedge fund weight.

In the beginning all was straightforward: models were rewarded as much as their predictions were correlated to the stock market.

However the model predictions are not used “as is” in the construction of the Numerai’s hedge fund portfolio. Their predictions are subject to constraints such as maximum exposure to a single equity, maximum exposure to a single sector, maximum turnover etc.

For that reason TC was introduced, which “represents how a stake should be changed to increase overall returns of a hypothetical portfolio” and models rewarded on this metrics.

That raises a problem though: models are not rewarded for what they are trained for (the actual stock market performance), but on a derived metrics, TC, which is not trainable by the models. In other words, the models are not trained to predict what the hedge fund needs (the actual stock exposure in the portfolio). Also the users are unfairly rewarded, because they have no way to train models to maximize TC.

One solution to this problem is to drop the current data target (“stock performance ~4 weeks into the future”) and to use a new target instead: the exposure a hypothetical portfolio should have had in each stock in the last ~4 weeks to maximize whatever is the hedge fund goal, keeping into consideration all the portfolio constraints.

This change would re-align the model training target with the hedge fund requirements and the user reward.

---

### Post #2 — **kayeffnumeraitor** | 2022-07-03 19:06 UTC

While I somehow share your sentiment, you can at least try to optimize for FNCv3, which is a metric that can be calculated beforehand. In my experience so far, FNCv3 is the best indicator for TC, which was also stated at TC introduction.

---

### Post #3 — **sunkay** | 2022-07-03 23:43 UTC _(reply to #2)_

I found my CORR and FNCV3 are good enough and started staking on TC, and then suddenly I got very bad TC. The correlation between TC and FNCv3 is not so robust. ![:rofl:](http://forum.numer.ai/images/emoji/twitter/rofl.png?v=10)

---

### Post #4 — **wigglemuse** | 2022-07-04 00:56 UTC

I think its a very big “if” whether or not training on such a target would be predictive of future rounds (and the future needs of the fund). I’m not sure such a target would even be feasible to create. Seems like it would be pretty random, and training on random numbers would not help you to predict future random numbers. (i.e. the undesirable behavior of TC might be the same or worse) It kinda sounds like v1/beta of TC where the actual current portfolio was being used to determine TC (that is no longer the case – it is now generating a hypothetical portfolio from scratch without regard to their current positions).

The sticking points with the current TC are:

  1. It isn’t a “target”. Can’t train/optimize for it directly.
  2. You can’t validate a model TC-wise on historical data. (related to #1, but different)
  3. It is highly volatile/inconsistent.



#1 seems to be a major complaint around here, but personally I find that one a non-issue. (I think many people want a kaggle-style thing where they are competing to see who’s best at training things on fixed data.)

But #2 & #3 are real problems. #2 could be solved by fixing #1 and creating a trainable target (maybe not possible), but #2 could be fixed independently also by some validation tool that made fairly accurate TC estimates (but might fail if you over-optimize for it). Because right now we basically can’t tell if we have good models or not. I’m not sure it is even clear if “good models” in the sense that they can earn TC and keep earning it for anything beyond the short-term are even possible. So it could certainly use some improvements or smoothing out (or a tool that allowed us to learn more about it on old data).

As I pointed out in the other thread, if TC fails as a feedback mechanism to create a positive loop, then it is a failure and they won’t fail to notice that because the metamodel will suffer (or everyone will have switched back to corr – maybe it is all just a plot to no longer pay us on MMC?).

---

### Post #5 — **sunkay** | 2022-07-04 02:21 UTC _(reply to #4)_

If TC score of a model is highly volatile, then its TC reward goes up and down or its owner turn off TC multiplier.  
If TC score of a model is consistent high, then its TC reward and stake amount goes up and up and up and that’s what numerai need.  
Few models got consistent high TC, but there were.  
Find out those models and reward them will help numerai.

We don’t know how to get consistent TC, that’s a problem.  
Even if FNCv3, TB200, CORR,MMC are all high, it’s still easy to get negative TC.  
Maybe we just don’t know how to adapt to the optimizer.

---

### Post #6 — **danzell** | 2022-07-04 07:01 UTC _(reply to #2)_

Yes …  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6d5eb31ba0b33b17b821464507f6e7485c5b4736.png)image250×138 1.73 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6d5eb31ba0b33b17b821464507f6e7485c5b4736.png> "image")

---

### Post #7 — **taori** | 2022-07-04 07:18 UTC

I believe I fail to properly explain my idea of the possible solution.

The new hypothetical target I am suggesting, would be the optimal exposure/position Numerai wish they had in each stock at a specific point in time. That has to keep into considerations all the constraints the real hedge fund has (there would be multiple targets if they have multiple funds). To compute these optimal positions (i.e. the hedge fund portfolio) Numerai has to make use of the current target (“stock performance ~4 weeks into the future”) but that is not given to the users.

if we trained our models on this new target, the models would learn how to build an optimal portfolio given the stock features. That would be like integrating stock prediction and portfolio optimization in a single model.

The benefit of this new target would be that the models could be rewarded on the pure correlation between their predictions and the portfolio Numerai wish they had at that particular round knowing the actual stock market performance at round end. That optimal portfolio used to compute the correlation against our model would be the target in the training data.

---

### Post #8 — **bor1** | 2022-07-04 07:29 UTC _(reply to #6)_

Tell us your secret? :-). What kind of model are you running?

---

### Post #9 — **danzell** | 2022-07-04 07:55 UTC _(reply to #8)_

Feels like building the type of model that minimizes TC score … ![:thinking:](http://forum.numer.ai/images/emoji/twitter/thinking.png?v=10)  
For me TC is super random and I’m still not sure what to do.  
Optimizing on CORR, MMC, FNC, FNCv3 isn’t working for me ![:upside_down_face:](http://forum.numer.ai/images/emoji/twitter/upside_down_face.png?v=10)

---

### Post #10 — **danzell** | 2022-07-04 07:56 UTC _(reply to #8)_

Feels like building the type of model that minimizes TC score … ![:thinking:](http://forum.numer.ai/images/emoji/twitter/thinking.png?v=10)  
For me TC is super random and I’m still not sure what to do.  
Optimizing on CORR, MMC, FNC, FNCv3 isn’t working for me ![:upside_down_face:](http://forum.numer.ai/images/emoji/twitter/upside_down_face.png?v=10)

---

### Post #12 — **sunkay** | 2022-07-04 08:53 UTC _(reply to #6)_

Good example

If we ignore TC, the model is very very good ![:rofl:](http://forum.numer.ai/images/emoji/twitter/rofl.png?v=10)

---

### Post #13 — **sunkay** | 2022-07-04 23:49 UTC _(reply to #10)_

I have a similar situation to you.

In my validation diagnostics, every metrics are fine except TB200 standard deviation and TB200 feature exposure.

[@danzell](</u/danzell>) Do you mind sharing these two metrics？

[@mdo](</u/mdo>) Are these two metrics related to TC consistency?

---

### Post #14 — **mdo** | 2022-07-05 06:30 UTC _(reply to #7)_

We have actually tried to make targets that work much like that, but haven’t released them because they don’t actually work very well to train on as they are very sparse. However, we are about to revisit target construction and do take your feedback seriously. I could see us doing something like moving to a new correlation target that’s very similar to what you describe, but with the caveat that we really don’t recommend training on it directly, or at least in isolation. But some version of TC isn’t going away as it solves the problem of properly rewarding unique contributions.

---

### Post #15 — **taori** | 2022-07-05 09:47 UTC _(reply to #14)_

> they don’t actually work very well to train on as they are very sparse.

Thank you for sharing this info. I wasn’t sure if such an idea could work and it is very interesting to know that you had already tried it.

---

### Post #16 — **sirmobius** | 2022-07-05 12:43 UTC _(reply to #6)_

I wonder why I like TC:  


[![my_model](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8bd05880359af2a5b3457350960b7f688317f6f9.png)my_model273×147 2.17 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8bd05880359af2a5b3457350960b7f688317f6f9.png> "my_model")

(This is an unfair comparison as my model missed rounds, and these missed rounds do not seems to impact TC as negatively as CORR rank)

---

### Post #17 — **danzell** | 2022-07-07 08:23 UTC _(reply to #13)_

I’m not using built in validation diagnostics nor tb200 to select my models - sorry ![:upside_down_face:](http://forum.numer.ai/images/emoji/twitter/upside_down_face.png?v=10)
