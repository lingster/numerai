---
title: "Temporary TC Bragging Rights"
category: Tournament
url: https://forum.numer.ai/t/temporary-tc-bragging-rights/6489
created_at: 2023-06-23T16:33:58.974000+00:00
last_posted_at: 2023-08-04T15:52:40.943000+00:00
posts_count: 15
views: 1509
tags: []
---

# Temporary TC Bragging Rights

---

### Post #1 — **bridgeface** | 2023-06-23 16:33 UTC

I don’t think I’ve ever had a run like this so I have to brag. This is under the model id **Bridgeface**.  
I have the top rating in a few rounds (100 percentile).  
Unfortunately I have my largest stake (200 NMR) on a different model, lol.

[![Screenshot 2023-06-23 112948](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/008f8756dc8286306f20598ab2cf23c0846ca012_2_690x371.png)Screenshot 2023-06-23 1129482026×1090 232 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/008f8756dc8286306f20598ab2cf23c0846ca012.png> "Screenshot 2023-06-23 112948")

---

### Post #2 — **ryo_matsuzaka** | 2023-06-24 13:42 UTC

mmm, beats me.  
How do you create the model?  
What is the sharp ratio?

---

### Post #3 — **bridgeface** | 2023-06-24 14:28 UTC _(reply to #2)_

Thanks for the reply. The Sharpe is not the best 0.84, max drawdown 0.2. However, none of my high scoring diagnostic models did well in the tournament (including Sharpe 1.0+). In fact, the performance was crap, very low Corr and TCs, I used all 1500 variables for those models. For my latest models I do feature engineering and use a smaller set of variables (~50), also use parameters that minimize overfitting (regularization, early stop, etc).

---

### Post #4 — **bpa_praec** | 2023-06-25 21:20 UTC

nice! what type of feature engineering you’re doing?

---

### Post #5 — **danzell** | 2023-06-26 06:43 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/bridgeface/48/2394_2.png) bridgeface:

> Unfortunately I have my largest stake (200 NMR) on a different model, lol.

classic - that’s how staking works ![:smile:](http://forum.numer.ai/images/emoji/twitter/smile.png?v=12)

---

### Post #6 — **richai** | 2023-06-26 07:33 UTC _(reply to #3)_

Wow that’s a small subset of features. I used to think it was good to use all the features because Numerai does so much to test our features. However, I think with TC creative feature selection makes a lot of sense especially to find the best features which the current Stake Weighted Meta Model has no exposure too.

---

### Post #7 — **wigglemuse** | 2023-06-26 17:36 UTC _(reply to #6)_

One of my more consistent models TC-wise uses only the “small” feature set – 32 features, no engineering.

---

### Post #8 — **ryo_matsuzaka** | 2023-06-27 20:40 UTC _(reply to #7)_

BTW, how small features were selected?

---

### Post #9 — **wigglemuse** | 2023-06-27 21:03 UTC _(reply to #8)_

This is the small feature set picked out by Numerai in the features.json file. I believe they were the features that were giving the most from an information standpoint, something like that. (So informative and non-redundant.) It’s been the same since v3 data – doesn’t use any of the newer features. (Originally it was 36 features, but 4 of them were in the 10 “bad” features they got rid of, so it’s down to 32 now.)

The reason I was using them wasn’t for a small simple model – it’s because I was playing around with this combinatorial explosion thing and it can’t handle many features at all without becoming untenable to calculate. So the 32 they picked out seemed like a good choice, and it turned out the resulting models were pretty good. So you don’t necessarily need a gazillion features. And there is a ton of redundancy in the features anyway so we don’t actually have as many as it looks like on a fundamental level.

---

### Post #10 — **shatteredx** | 2023-06-28 03:48 UTC _(reply to #8)_

The small feature set was created using BorutaShap: [Feature Selection with BorutaShap](<http://forum.numer.ai/t/feature-selection-with-borutashap/4145>)

---

### Post #11 — **ryo_matsuzaka** | 2023-07-01 00:50 UTC

Btw your model get worse.

---

### Post #12 — **svendaj** | 2023-07-21 09:41 UTC

Why does bragging feel so good?

My last drawdown on May 30th submission an then green all the way up:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4691a38f36efa69e0071c1740560710d27eb89a9_2_690x381.png)image1500×830 112 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4691a38f36efa69e0071c1740560710d27eb89a9.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d6c5fcf680beb166425c062d125c2fdc13abc902_2_690x379.png)image1526×840 107 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d6c5fcf680beb166425c062d125c2fdc13abc902.png> "image")

Because it is temporary? Anyway… _CARPE DIEM_

---

### Post #13 — **mlivako** | 2023-08-03 19:03 UTC _(reply to #12)_

I want t brag a little bit here as well . never been in top top 15 in both corr and tc. I know nothing last forever so enjoying it ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3c202d146ce54cddb9a249846637159f74e7acb1.png)image721×279 17.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3c202d146ce54cddb9a249846637159f74e7acb1.png> "image")

---

### Post #14 — **svendaj** | 2023-08-04 15:12 UTC _(reply to #13)_

Actually, if your models start with `ML_` you are doing very well:

  * 7 models in Top 100 TC leaderboard
  * 15 models in CORRV2 TOP 100



Congratulations!!!

---

### Post #15 — **mlivako** | 2023-08-04 15:52 UTC

Almost got it. ml_yn* are mine. The fact is that they are the same approach (one of the 60D targets with weekly retraining on very short period) but with different flavor of feature engineering and feature neutralization.

So in summary it is one model with different parameters. Could be just a lucky constellation of random parameters that works today. Will see
