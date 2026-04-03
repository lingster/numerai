---
title: "New Target Nomi Release"
category: Tournament
url: https://forum.numer.ai/t/new-target-nomi-release/959
created_at: 2020-09-19T01:41:12.121000+00:00
last_posted_at: 2020-12-15T15:00:04.417000+00:00
posts_count: 16
views: 6961
tags: []
---

# New Target Nomi Release

---

### Post #1 — **mdo** | 2020-09-19 01:41 UTC

We are releasing today a new target, target_nomi, that you can optionally use to train your models. You should still submit predictions in the same exact way as before but just using the outputs of the newly trained model. Fundamentally, this target represents the same thing as target_kazutsugi, but just a bit more faithfully. Consequently, it is compatible with target_kazutsugi and we will continue scoring using target_kazutsugi for the time being. We will give plenty of warning before we eventually switch to scoring with target_nomi (likely late October). In my experiments, training models using target_nomi and scoring against target_kazutsugi, gave about the same scores on average as training on target_kazutsugi, but with less variance era-to-era, and therefore higher Sharpe. On our side, this target allows us to construct portfolios with higher expected returns. We expect this to be win-win and want to make the transition as smooth as possible. Even after the transition to scoring on target_nomi, your old models trained on target_kazutsugi will still work, but will likely score slightly worse than if you had retrained on target_nomi. So let us know how it goes!

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/f076d72fad8f2d7b35820125eadd28fb47da5c40_2_690x415.png)image967×582 64.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/f076d72fad8f2d7b35820125eadd28fb47da5c40.png> "image")

You can download it here as a parquet file:  
<https://drive.google.com/file/d/1K7CnXKoEW7sKCwb9D6TboQsVDWgVdiez/view?usp=sharing>

Or here as csv:

[drive.google.com](<https://drive.google.com/file/d/190NsspVfMqNega_8nOpqgKkKELrxjtTv/view?usp=sharing>) [](<https://drive.google.com/file/d/190NsspVfMqNega_8nOpqgKkKELrxjtTv/view?usp=sharing>)

### [numerai_training_validation_target_nomi.csv.tar.gz](<https://drive.google.com/file/d/190NsspVfMqNega_8nOpqgKkKELrxjtTv/view?usp=sharing>)

Google Drive file.

You can watch the discussion of the new target in OHWA here:

---

### Post #2 — **perfect_fit** | 2020-09-19 11:26 UTC

Nice, excited to check it out!

Are there diagnostics on how the example model (INTEGRATION_TEST) performance changes with the new target (including feature exposure, max drawdown, etc.)? Or is that something we have to figure out ourselves? ![:slightly_smiling_face:](http://forum.numer.ai/images/emoji/twitter/slightly_smiling_face.png?v=9)

---

### Post #3 — **jrb** | 2020-09-19 14:38 UTC _(reply to #2)_

Here’s a [modified version](<https://github.com/jeethu/numerai-example-scripts/blob/nomi/example_model.py>) of the [example model](<https://github.com/numerai/example-scripts/blob/master/example_model.py>) that trains on the new target. And here’s the [diff view](<https://github.com/numerai/example-scripts/compare/master...jeethu:nomi?expand=1>), if you’d like to see what I’ve changed.

---

### Post #4 — **wigglemuse** | 2020-09-19 21:49 UTC

[@mdo](</u/mdo>) So obviously you’ve compared models trained with old targets vs models trained with new targets and both scored the same way, and concluded that trained with new targets = better. And for the time being we are still be scored on the old targets. So that’s all good.

But (and I missed the office hours and haven’t watched that video yet), if we transition to being scored on the new targets, I have a slight concern (based on a very quick test with sample size of one) that being scored on the new targets will lower the magnitude of scores overall and therefore even if they are better we may all end up with a slight haircut going forward (i.e. the whole range of scores will shift slightly caused by the new target distribution). At least people that are positive most of the time will get a haircut, however the effect would be symmetrical and change the magnitude on the negative side in the same way. Have you looked into this question? So for instance if you took 100 models (doesn’t matter how they were trained) and scored them on old targets, and score the _same_ (not retrained on different targets) 100 models on the new targets, is the average score going to be pretty much equal, or will the distribution of the new targets tend to cause greater magnitude or lower magnitude? Which would mean everybody possibly getting paid less, but also burning less I guess. In my test, there is a not insignificant difference, but obviously there is going to be SOME difference when I’m only looking at a single model so wondering if you’ve done any such tests in bulk. (I should watch that video in case you’ve covered this.) Thoughts?

---

### Post #5 — **lackofintelligence** | 2020-09-19 22:08 UTC

Same delicious Lucky Charms, (LARGE SIZE), but in a thinner box?

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/9c9a1be33a1df691df9b6e94f2a1105f7a2d33f4.jpeg)image500×500 104 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/9c9a1be33a1df691df9b6e94f2a1105f7a2d33f4.jpeg> "image")

---

### Post #6 — **wigglemuse** | 2020-09-19 22:23 UTC

Well, yes, we can actually figure this out analytically. Since the targets are not continuous and have a bunch of ties in them (that are not broken), but our predictions do have their ties broken, and then are scored based on cor(preds,targets) the actual range of possible scores under the current system is not [-1,+1]. With the current system of 5 roughly equal buckets, the range is about [-0.98,+0.98]. With the new distribution of 5,20,50,20,5 (percents), the range narrows to about [-0.91,+0.91]. So the mathematical capacity to get higher (or lower) scores is reduced because the whole magnitude is reduced. Now of course we aren’t getting anywhere near the max/min values of with our predictions, but still this will be a change that may hurt somewhat, i.e. we will make less than what we would have made under current system. HOWEVER, we are also promised that our models will be improving (if we retrain), so then maybe it is a wash? Maybe, maybe not. (And burns would be lessened also.) It would seem to indicate at the very least that we probably will not be making more under new system. Does it matter? (The current system is the current system, but that doesn’t make it sacred.) Possibly there should be an adjustment factor to our CORR scores (even under current system) to fix the range at [-1,+1], or maybe just to fix the new range to match the old range. (Or just keep scoring under old targets.) Thoughts?

---

### Post #7 — **mdo** | 2020-09-19 23:15 UTC _(reply to #6)_

The range issue you mention is interesting, thanks for pointing that out. I will investigate and see if we need a scoring/payout adjustment that is due the the distribution of the new target.  
I do think the new target is slightly harder because there is less regularization built in and it more closely matches the quantity of interest. For example, the increased rareness of the extreme values 0&1 can make it easier to overfit. The flip side is that if you do well with the new target your model should generalize better than before whether scored again Kazutsugi or Nomi. I think if you make your goal to get the same generalization performance when training and scoring against Nomi as you had when training and scoring against Kazutsugi, your model will end up much better overall and you should see no haircut after the transition (barring the scaling issued already discussed).

---

### Post #8 — **ia_ai** | 2020-09-19 23:36 UTC

Can we add two more lines (based on `integration_test`) to the comparison, please?

  * train_kaz_predict_nomi
  * train_nomi_predict_nomi

---

### Post #9 — **permistiro** | 2020-09-20 01:11 UTC

In case anyone needs to fetch the new files from command line/script, I pinned them to Infura’s Ipfs service. Here’s the link to Cloudflare’s fast http gateway:

<https://cloudflare-ipfs.com/ipfs/QmX1cDy6iqKGy8B4wSx8PkwxDTgPmWuZZBTM7tL1WNizv8/>

---

### Post #10 — **permistiro** | 2020-09-20 01:14 UTC

I have a question:

will the target be named nomi or kazutsugi after the migration?

---

### Post #11 — **wigglemuse** | 2020-09-20 03:36 UTC _(reply to #7)_

> The range issue you mention is interesting, thanks for pointing that out. I will investigate and see if we need a scoring/payout adjustment that is due the the distribution of the new target.

Cool, thanks. I’m sure you will make the right decision!

---

### Post #12 — **jeremy_berros** | 2020-09-20 04:44 UTC _(reply to #3)_

Hi [@jrb](</u/jrb>). Thanks for your update. However I get the following error message while submitting using strictly your version of example model with nomi:

**invalid submission ids. ids must match current tournament data exactly, including ordering. make sure you are using the latest tournament data**

---

### Post #13 — **jrb** | 2020-09-20 07:26 UTC _(reply to #12)_

[@jeremy_berros](</u/jeremy_berros>) Are you sure you’ve got the latest tournament data that was released yesterday? I don’t intend on ever submitting example predictions (or any xboost model for that matter), but I tried it out of curiosity, after I saw your post and here’s what I got:

[![Screenshot](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/49ef32dfae4ee492a80ecf6deb8c52386bdb4ca8.png)Screenshot254×494 19 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/49ef32dfae4ee492a80ecf6deb8c52386bdb4ca8.png> "Screenshot")

---

### Post #14 — **jeremy_berros** | 2020-09-20 19:53 UTC _(reply to #13)_

[@jrb](</u/jrb>). Tried again this morning and it works. I guess that’s what happens when you try too hard too late ![:sleeping:](http://forum.numer.ai/images/emoji/twitter/sleeping.png?v=9)

---

### Post #15 — **mdo** | 2020-09-20 23:42 UTC _(reply to #10)_

It will either continue as “target_nomi”, or possibly just “target”

---

### Post #16 — **loracle** | 2020-12-15 15:00 UTC _(reply to #9)_

Hello, do you have old tournament data pinned somewhere on ipfs by any chance ?
