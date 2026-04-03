---
title: "Marketplace: jackerparker4 model for sale"
category: Tournament
url: https://forum.numer.ai/t/marketplace-jackerparker4-model-for-sale/3641
created_at: 2021-06-23T18:34:49.460000+00:00
last_posted_at: 2021-07-04T10:38:44.458000+00:00
posts_count: 24
views: 2779
tags: []
---

# Marketplace: jackerparker4 model for sale

---

### Post #1 — **jackerparker** | 2021-06-23 18:34 UTC

Upd: you can buy predictions [here](<https://gumroad.com/jackerparker>)

Hi everyone, I would like to start selling predictions for my model [jackerparker4](<https://numer.ai/jackerparker4>) (started only at Round 263). Since we don’t have a marketplace yet, I decided to create a post here on the forum.

Brief overview of the model: The model was developed using LightGBM with strong focus on accurate CV, feature selection and feature neutralization. Actually, I used the same principles a year ago with another model which I’ve discussed and shared in this post ([Feature neutralization workflow](<http://forum.numer.ai/t/feature-neutralization-workflow/1059>)). That old model is still freely available on github. However, at this time I’ve revised all the stages and finished with a new model. In particular, the fast combinatorial cross validation was used and it was discussed in this forum post ([Fast Combinatorial Cross Validation](<http://forum.numer.ai/t/fast-combinatorial-cross-validation/3350>)). As for the new feature selection and feature neutralization workflows - I didn’t discuss it anywhere and it is my “secret sauce” right now. The model was trained using training (1-120 eras) + val1 (121-132) data, and val2 (197-212 eras) data was used as holdout. That is why there is no sense to compare and look into normal validation report, but here is a comparison of jackerparker4 vs example_predictions for val2 data:

[![val2_JP4_vs_examplepreds](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c34bdb083a83aad32d121bb9bab82751bc5a2e5e_2_690x371.png)val2_JP4_vs_examplepreds966×520 47.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c34bdb083a83aad32d121bb9bab82751bc5a2e5e.png> "val2_JP4_vs_examplepreds")

The statistics from my local CV: 0.04636 COR, 1.84 sharpe and -0.0297 min COR value for eras 1-132.

And here are the current live results (the model was started only at round 263):

[![JP4_live](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1fbbd625c0cc9a5bca48eca95262d25308c77c27.png)JP4_live921×324 14.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1fbbd625c0cc9a5bca48eca95262d25308c77c27.png> "JP4_live")

Additional info that does matter here:

Kaggle ([markmipt | Contributor | Kaggle](<https://www.kaggle.com/markmipt>)): I participate in a similar competition ([Jane Street Market Prediction | Kaggle](<https://www.kaggle.com/c/jane-street-market-prediction>)). It will be finally ended only in 2 months, but my model has 56th position on the current live leaderbord. That kaggle model is something average between my current workflow and the workflow I’ve shared a year ago. The fact that my methods in general work well in different competitions adds some confidence, at least for me.

Science ([‪Mark V Ivanov‬ - ‪Google Scholar‬](<https://scholar.google.com/citations?user=Z_NKnLMAAAAJ>)): I have a PhD in bioinformatics, my h-index is 12 and one of my strongest skills is creation of schemes for validation of results in my field (proteomics). The latter also helps me in the model development for finance-related stuff.

Other models: I also have 5 additional active accounts (jackerparker-jackerparker6), but these models are just dot products of jackerparker4. For example, jackerparker5 is the same predictions as the jackerparker4, but 100% feature neutralized. Jackerparker6 is 0% feature neutralized. Jackerparker1-3 are similar models as 4-6, but developed using less reliable CV. So, I have only one model which I trust and that reduces chances of random fit into live data.

To assess the prospects of predictions selling and since my model has not many live rounds, I would like to start with a 25$ price for a single round.

Please contact me for more details here or in the chat.

Regards,  
Mark

---

### Post #2 — **autratec** | 2021-06-24 09:07 UTC

Good try. Hope your model working. Should u charge based on principal ?

---

### Post #3 — **jackerparker** | 2021-06-24 09:30 UTC _(reply to #2)_

Not sure if I understand correctly: do you mean that the price should be based on the stake which user is going to stake on the model? If yes - than my answer is no. I’m not sure if that will be legal in my jurisdiction, as well as any relations with cryptocurrency. I just want to sell model using [gumroad.com](<http://gumroad.com/>) (platform for creators, that will simplify taxes stuff for me) for fixed fiat price.

---

### Post #4 — **autratec** | 2021-06-24 10:29 UTC _(reply to #3)_

Recent earning model change make it feasible to charge based on real earning. For example 20% profit with watermark etc.

---

### Post #5 — **restrading** | 2021-06-24 10:32 UTC _(reply to #4)_

[@autratec](</u/autratec>) Without a marketplace doing the submissions for the buyers there would not be a good way to enforce the profit-sharing. Also such profit-sharing most likely will cause regulatory complexities.

---

### Post #6 — **autratec** | 2021-06-24 10:47 UTC _(reply to #5)_

Let’s leave regulation aside, the weekly prediction data still under control of scientist. No profit sharing, no prediction file.

Performance fee paid by NMR. Direct wallet to wallet transfer.

---

### Post #7 — **restrading** | 2021-06-24 10:52 UTC _(reply to #6)_

[@autratec](</u/autratec>) An attack can be done by buying->not sharing profit->change NMR wallet->buying again->…

---

### Post #8 — **autratec** | 2021-06-24 10:57 UTC _(reply to #7)_

Not such complex. Basic kyc will be necessary…

---

### Post #9 — **restrading** | 2021-06-24 10:57 UTC _(reply to #8)_

KYC won’t be quite well-received given this is a crypto project

---

### Post #10 — **jackerparker** | 2021-06-28 05:34 UTC

Predictions are available here: [jackerparker](<https://gumroad.com/jackerparker>)

---

### Post #11 — **autratec** | 2021-06-28 14:02 UTC _(reply to #10)_

Not quite sure your business model. Assume u will send one time prediction for one round with 25 USD as return ?

---

### Post #12 — **jackerparker** | 2021-06-28 14:18 UTC _(reply to #11)_

Yeah, you are right. For 25 USD buyer will get predictions for a single round. What is approximately 100$/month and 1200$/year, assuming the price will not be adjusted

---

### Post #13 — **jnolan9** | 2021-06-29 12:33 UTC _(reply to #4)_

Autratec, can you elaborate?

---

### Post #14 — **autratec** | 2021-06-30 09:14 UTC _(reply to #13)_

Be honest, with those no code/ low code machine learning as service be more popular in the world, submitting weekly prediction with GBTree model won’t be a rocket science any more.

With no much data scientist background, a normal person with some statistics concept is able to submit the model, get a fair result (0.05 + CORR ) in 4 to 8 hours as one time effort. Weekly updating, including 2.5G + data download and upload , might take 60 to 90 mins.

In the near future, I believe tournament will be less challenging. Every one using tree model to grab 5-9% return weekly and payout ratio will be reach to minum faster then we thought.

It means, hard to sell any model in this game.

---

### Post #15 — **sirbradflies** | 2021-07-01 06:36 UTC _(reply to #14)_

I agree with this reasoning, the only factor that could change this situation could be a switch to a 100% MMC payout. In that scenario “commodity” models will be of little value and so “real” models could still command a premium.  
Assuming the priority for Numerai is the meta-model development then CORR payouts should be phased out at some point and only actual contributions (i.e. MMC) get rewarded, which is much more difficult to obtain with “off-the-shelf” models.  
Just my opinion! ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #16 — **jay1100** | 2021-07-01 08:44 UTC _(reply to #15)_

If you go for 100% MMC payout people could submit random numbers. This would give high MMC because very different from meta-model, but of course not useful at all. Therefore you always have to reward/penalize CORR as well.

---

### Post #17 — **mic** | 2021-07-01 08:55 UTC _(reply to #16)_

MMC is how much you help or hurt the meta model. Random numbers won’t help.

---

### Post #18 — **hydration** | 2021-07-01 10:37 UTC _(reply to #10)_

This is such a great idea that I am going to copy it! Who wants to buy predictions from my top 20 [model](<https://numer.ai/hydration9/>)? The model has not changed since round 238. DM me on Rocketchat or on [Twitter](<https://twitter.com/hydration_ds>) if you are interested.

---

### Post #19 — **jay1100** | 2021-07-01 11:16 UTC _(reply to #18)_

Why are you stacking so little on your models?

---

### Post #20 — **jay1100** | 2021-07-01 11:28 UTC _(reply to #17)_

Your are right. Thanks for pointing this out.  
MMC is regressing (= neutralizing) the meta model predictions out of your predictions. Then it is calculating the correlation of your adapted predictions and the target. So you want your predictions to not be correlated with the meta-model predictions but still be correlated with the target.

---

### Post #21 — **hydration** | 2021-07-01 13:26 UTC _(reply to #19)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/j/e5b9ba/48.png) jay1100:

> Why are you stacking so little on your models?

Sold all my crypto and used that in part to buy a house. I don’t have the appetite to take more risks in crypto. But of all the cryptocurrencies I am most optimistic about NMR and my models seem to be performing well.

---

### Post #22 — **gockgang** | 2021-07-03 09:59 UTC

… Isn’t the example model included in dataset (the one using xgboost) perform better than your commercialized model? sorry if I am wrong, I don’t know much details but just look at the corr and mmc value…

---

### Post #23 — **jackerparker** | 2021-07-03 18:14 UTC _(reply to #22)_

Hi gockgang! The live results are close enough, but the number of finished rounds for my model is too low for any strong conclusions (jackerparker4 is live only from round 263). The local CV and validation stats are much better for my model compared to example predictions. But in general your question is good and I don’t have enough live data to prove that my model is much better what I’m trying to compensate by collateral information and low price right now.

Regards,  
Mark

---

### Post #24 — **jackerparker** | 2021-07-04 10:38 UTC _(reply to #23)_

Gumroad page is updated with [jackerparker6](<https://numer.ai/jackerparker6>) model now (a user requested it in the private messages).
