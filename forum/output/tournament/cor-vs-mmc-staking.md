---
title: "COR vs MMC staking"
category: Tournament
url: https://forum.numer.ai/t/cor-vs-mmc-staking/456
created_at: 2020-05-22T14:05:09.041000+00:00
last_posted_at: 2020-06-02T14:59:28.284000+00:00
posts_count: 11
views: 2275
tags: []
---

# COR vs MMC staking

---

### Post #1 — **ssh** | 2020-05-22 14:05 UTC

Facing the dilemma of “COR vs MMC staking”, I looked closely at round performance of my (and other users’) models. I simply plotted COR vs MMC scores of my models and also included performance of current top500 users.

Each scatter-plot shows the results of all models in one round (rounds 212-209 haven’t resolved yet). Each dot represents one user model with X coordinate is correlation score and Y is MMC score (blue triangles are my own models). At each scatter-plot, I added the indifference line: **ABOVE the line model is better of staking at MMC score,** bellow that line user better to stake on correlation.  


[![Rplot212_205](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d374f77cc23a4469cd248a952bbb75ebec335b31.png)Rplot212_2051000×500 14.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d374f77cc23a4469cd248a952bbb75ebec335b31.png> "Rplot212_205")

  


[![Rplot204_197](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/798a5f5e295e0ef5fa51e2c1721e8cd6c289a0f7.png)Rplot204_1971000×500 12.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/798a5f5e295e0ef5fa51e2c1721e8cd6c289a0f7.png> "Rplot204_197")

  


[![Rplot196_189](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/649c0f4240c449b72c35e2df0c9f18e5e3bb0fd0.png)Rplot196_1891000×500 12.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/649c0f4240c449b72c35e2df0c9f18e5e3bb0fd0.png> "Rplot196_189")

  


[![Rplot188_181](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a1407c44951b426b008d5ed0ac247096fc46c216.png)Rplot188_1811000×500 13.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a1407c44951b426b008d5ed0ac247096fc46c216.png> "Rplot188_181")

  


[![Rplot180_173](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/b55b9146e276b66be3971eb98764fb61f0a4abec.png)Rplot180_1731000×500 11.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/b55b9146e276b66be3971eb98764fb61f0a4abec.png> "Rplot180_173")

  
At “bad” rounds (like 195-198), MMC is a good way to improve returns for most of the models.  
At “good” rounds like 203-209 COR staking bits MMC staking for most of the users’ models. So in general MMC staking strategy provides some kind of protection against performance volatility.

---

### Post #2 — **ssh** | 2020-05-22 18:19 UTC

update for new dayly scores for unresolved rounds (212-209) with COR distribution of unresolved rounds  


[![cor_mmc_212_209_22052020](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/57f118b1af5e8df44f8a220ca95483f54cd0d9d8.png)cor_mmc_212_209_220520201200×600 14.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/57f118b1af5e8df44f8a220ca95483f54cd0d9d8.png> "cor_mmc_212_209_22052020")

  
current round 212 today looks exactly like round 211with average COR close to zero

---

### Post #3 — **jackerparker** | 2020-05-25 11:28 UTC

I’ve done my own simple theoretical research of COR vs MMC staking using validation data. As the rough approximation of the MMC payout I’ve used the equation: 2 * (my model’s correlation - example predictions correlation * 0.5) per era in validation set. 0.5 was chosen because my predictions have 0.5 average correlation with metamodel for the last 4 rounds. The results are 0.0268 average payout (sharpe 0.9) using MMC staking and 0.0278 average payout (sharpe 1.7) using COR staking. Current live results (4 unresolved rounds) are: 0.0243 average calculated payout (sharpe 1.1) using MMC staking and 0.0268 average payout (sharpe 1.4) using COR staking.

Probably all that just mean that my model is not really useful for the metamodel

[![MMC_vs_COR](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/3d7e261ad30fda80e9a6e7f42e335ce54ccdbea0_2_690x373.png)MMC_vs_COR966×523 53.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/3d7e261ad30fda80e9a6e7f42e335ce54ccdbea0.png> "MMC_vs_COR")

---

### Post #4 — **jrdi** | 2020-05-25 11:41 UTC

I’ve been checking models returns COR vs MMC, and I think it makes no sense moving from COR to MMC. Checking returns of big stakers that have been moved to MMC…

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/eff7bea7a258a2730dffb8a7db861a47b5e7b113_2_515x500.png)image1153×1118 97.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/eff7bea7a258a2730dffb8a7db861a47b5e7b113.png> "image")

I haven’t explored other models but I have a couple of models with low MMC correlation but MMC score is heavily dependant on COR performance. When I have COR < 0, even being on top percentiles (less negative than the rest) I get a bad MMC because my model is contributing on a negative original way. I understand numerai wanting fresh approaches, that’s why I see MMC as a leaderboard/originality bonus replacement, “you do well, you get paid. you do well and your model is doing something original, you get paid a bit more”.

---

### Post #5 — **blockrocket** | 2020-05-25 16:50 UTC _(reply to #4)_

I agree with this idea - rewards originality, and avoids punishing that originality when/if the MMC correlation changes. If I understand correctly, the actions of other participants will affect the payout/burn (unlike with COR - which is determined by the market).

---

### Post #6 — **krizmanic** | 2020-05-26 14:45 UTC

What does switching the method look like? If I wanted to try MMC for a week and then go back to CORR the following week, could I? Is the 4 week time frame relevant in any way for switching?

---

### Post #7 — **wigglemuse** | 2020-05-26 15:04 UTC _(reply to #6)_

We should be able to switch for each round – wouldn’t make sense otherwise. So if you are set on MMC at the start of a round (meaning Thursday when any other stake changes would take place), then the payment for that round 4 weeks later will be on MMC. (Remember you only get paid for a round at the end of it now.) But presumably, you could change it back to CORR the next week, but it would apply to the next round. So you can’t change CORR->MMC or MMC->CORR on a round that’s already started, but you could alternate round to round if you wanted.

---

### Post #8 — **krizmanic** | 2020-05-28 02:32 UTC

Gotta admit, not crazy about MMC either. To me it seems like a way to reduce risk of volatile or bad time periods at the cost of introducing risk involving what other people do, and what random subset of them is chosen.

---

### Post #9 — **krizmanic** | 2020-06-02 14:13 UTC

Actually… If you really want to make MMC a bonus substitute, staking should just be general, and the model should just get paid on the better of the 2 choices automatically.

---

### Post #10 — **wigglemuse** | 2020-06-02 14:34 UTC _(reply to #9)_

I suggested that, but Mike pointed out that would be vulnerable to a p/1-p attack because you could have opposite accounts both getting the best return (corr vs mmc) automatically which would guarantee a net positive result.

---

### Post #11 — **krizmanic** | 2020-06-02 14:59 UTC _(reply to #10)_

So basically any form of anything that looks like compensation will get destroyed by this attack… The only way to earn anything is gambling on how predictable the stock market is, with the best loaded dice we can make. A P-1 model or anti model really just says the market wont be predictable in this era (based on whatever predictability looks like to the modler, and whatever these features are).

Choosing MMC seems super arbitrary since most of the data we can go on is for models that aren’t in prod now, assuming people have begun using the new validation data a few eras back.
