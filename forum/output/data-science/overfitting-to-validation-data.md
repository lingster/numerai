---
title: "Overfitting to Validation Data"
category: Data Science
url: https://forum.numer.ai/t/overfitting-to-validation-data/3442
created_at: 2021-05-26T04:21:34.432000+00:00
last_posted_at: 2021-07-08T09:46:49.090000+00:00
posts_count: 14
views: 1833
tags: []
---

# Overfitting to Validation Data

---

### Post #1 — **nenco** | 2021-05-26 04:21 UTC

I was thinking about something that could increase test performance a little and was wondering if any of you do this:

  * Train models on training set
  * Compare models on validation set
  * Pick best model
  * Retrain model on training + validation set for extra performance



Does anyone do this? Why or why not? I don’t because it confuses me when model validation scores come back so high on submission receipts. But this could possibly improve test performance. Let me know thoughts and opinions.

---

### Post #2 — **mic** | 2021-05-26 07:16 UTC

When you submit, Numerai report validation scores on the same validation set that you are given. So when you train on validation, just ignore the validation scores because they are not meaningful.

As for if people train with the validation data, some people do it and some people don’t!

---

### Post #3 — **jackerparker** | 2021-05-26 08:06 UTC

I’m against picking best model using validation set (If I got your idea right): it just a small piece of info compared to performance analysis which you can get during training. It’s similar to Kaggle’s situation when people choose model by Public Leaderboard score instead of local CV and here is just one example what usually happens in that case: [medium article](<https://medium.com/hmif-itb/overfitting-the-leaderboard-da25172ac62e>) (and much more can be googled using “shake up kaggle”). It was the thing which I’ve learned in the hard way during my first Kaggle competition ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #4 — **sirbradflies** | 2021-05-26 09:01 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/mic/48/2949_2.png) mic:

> et that you are given. So when you train on validation, just ignore the validation scores because they are n

Hi nenco,  
This is actually what I do and I believe is a perfectly reasonable approach which I personally follow (including for these models ([Sirbradflies](<https://numer.ai/sirbradflies>), [Flabridrises](<https://numer.ai/flabridrises>), [Fbaldisserri](<https://numer.ai/fbaldisserri>)).

Regarding the step 4, retraining on training + validation, I don’t have a clear answer yet. Currently I am using 8 models slots with:

  * 4 for models trained only on training data
  * 4 with exactly the same models but trained on training and validation data



I will post the comparison between these 2 groups when I have an history of at least 20 rounds to compare.

---

### Post #5 — **nenco** | 2021-05-26 10:46 UTC _(reply to #4)_

sirbradflies,

I am very interested in this comparison. Can you send profile links of the 4 models trained only on training, and the same models trained on training and validation? Which one has higher performance so far?

---

### Post #6 — **javiermoral** | 2021-05-26 11:04 UTC _(reply to #4)_

Could you share the models?

---

### Post #7 — **sirbradflies** | 2021-05-26 11:20 UTC _(reply to #6)_

I wanted to wait until all models have at least 20 weeks of history but sure, no problem.

Here’s all model pairs (training / training+validation):

  * sirbradflies / bradfliessir
  * firlasersbid / lasersbidfir
  * fbaldisserri / baldisserrif
  * flabridrises / ridrisesflab



Don’t make fun of my model names and please share any analysis you may do, thanks!

---

### Post #8 — **sirbradflies** | 2021-07-06 05:04 UTC _(reply to #7)_

I finally managed to complete the analysis of my models trained and non trained on validation for the rounds 248-267.

To recap, I have 4 models (sirbradflies_01/03/05/07) that are not trained on validation and 4 (sirbradflies_02/04/06/08) that are exactly the former models but trained on train+validation data (with early stopping) right before submission.

Below are the comparisons of the aggregate results. In the end I have found no critical reason to train on validation data. It may be useful to diversify the portfolio of models and maybe pickup different regimes but, given my bias for simplicity, I believe I’ll revert to using validation data as validation only.

Hope it’s helpful and let me know what you think.

[![correlation_valtrain_vs_nonvaltrain](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/13604234579d27d9ffcb3684f9be79f2047aaa67_2_690x474.png)correlation_valtrain_vs_nonvaltrain800×550 47 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/13604234579d27d9ffcb3684f9be79f2047aaa67.png> "correlation_valtrain_vs_nonvaltrain")

[![mmc_valtrain_vs_nonvaltrain](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a12cea167b18b339e168a4b60ffa5c224249f215_2_690x474.png)mmc_valtrain_vs_nonvaltrain800×550 49.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a12cea167b18b339e168a4b60ffa5c224249f215.png> "mmc_valtrain_vs_nonvaltrain")

---

### Post #9 — **jackerparker** | 2021-07-06 06:52 UTC _(reply to #8)_

Hi sirbradflies,

Could you please add some details about your procedure for training on validation data. From the messages above it seems like you used validation data only for early stopping. Is that right?

Regards,  
Mark

---

### Post #10 — **sirbradflies** | 2021-07-06 09:01 UTC _(reply to #9)_

Hi jackerparker,

Sorry I was not clear on the process. Here’s more details:

  1. Each model is first trained on train data (and early stopping on train data) and the predictions are submitted (sirbradflies_01/03/05/07)
  2. Then each model is trained again from scratch but this time on train + validation data combined (and both are used for early stopping)
  3. The retrained models’ prediction are submitted (sirbradflies_02/04/06/08)



Let me know if anything is not clear!

---

### Post #11 — **autratec** | 2021-07-06 10:49 UTC _(reply to #10)_

I don’t see significant difference due to different combinations, between training , training+ validation data etc. Btw, even the goal of numerai is to find a ultimate model to handle market situation in the long term. In the real trading world, only those adapting changes survived.

It means, those old validation data didn’t contribute too much to recent trading results, and continue filter features will be necessary.

---

### Post #13 — **andy_shaps** | 2021-07-07 13:48 UTC

Hi [@sirbradflies](</u/sirbradflies>)

interesting insight and thanks for sharing. Would you mind sharing a bit more info about your model? I have found similar things using gbm (but admittedly haven’t been doing this long enough to know for sure!) and was thinking to try it on a nnet.

my thinking is just that given the era differences in the validation set and that the training set has a smaller era range, the added complexity that (some) of the validation data has could help identify some non-linear relationships that might be less apparent in the training data?

(first time posting, happy to be part of the community ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) )

---

### Post #14 — **sirbradflies** | 2021-07-08 06:57 UTC _(reply to #13)_

Hi [@andy_shaps](</u/andy_shaps>)

No problem at all. These are 4 different type of models, including:

  1. Catboost
  2. SKLearn MLP
  3. SKLearn Ridge
  4. Keras



I compared the results also at a model level and I have found a setup where training also on Validation leads to an advantage. My theory is that the small advantage of having additional data for training get balanced by the lack of data for proper validation.

I will personally go back to use Validation only as intended, hoping that the Numerai dataset will be soon expanded on a regular basis so that training constantly expands ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

Hope it helps and welcome to the community!

---

### Post #15 — **andy_shaps** | 2021-07-08 09:46 UTC _(reply to #14)_

Hi [@sirbradflies](</u/sirbradflies>)

Thanks for the reply. That’s fair enough and i think the majority of people are doing the same (train, val separate).

Just in the interest of sharing, I find that combining the train/val sets, then creating a random 90:10 split, the corr i get with the holdout set is much higher than i would just training on the train set (admittedly the holdout set is smaller than the validation so might be inherently easier to score better). I think I will continue to try my current models with some of the validation data incorporated but may set up some new models which just use the test data.

I just wish there was more diversity or more recent era data in the training data. It feels like we are using prehistoric data to predict the future ![:sweat_smile:](http://forum.numer.ai/images/emoji/twitter/sweat_smile.png?v=9)! modern (ish) data would make it easier in my opinion (hence my desire to use some validation data in the training).

Nonetheless, thanks for sharing and… Good Luck! ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=9)
