---
title: "Target Cyrus - New Primary Target"
category: Announcements
url: https://forum.numer.ai/t/target-cyrus-new-primary-target/6303
created_at: 2023-04-17T02:43:29.711000+00:00
last_posted_at: 2023-05-15T00:49:00.410000+00:00
posts_count: 29
views: 5517
tags: []
---

# Target Cyrus - New Primary Target

---

### Post #1 — **master_key** | 2023-04-17 02:43 UTC

**Overview**

4 new target variations are being released on Numerai. There are 20D and 60D versions of each, for a total of 8 new targets. They will be released in the v4.1 dataset starting with the round opening on April 18.

One of them, target Cyrus, will become the official target used for payouts in one month, beginning with the round opening on May 13.

Along with this change, we are also implementing a change in the way correlation is calculated. This change weights your lowest and highest predictions more, and it is called Numerai Corr.

Models trained on Nomi still perform fairly well on this new score, but we do expect models trained on the newer targets to be a bit better.

Signals has no new targets released, but it will begin using the Numerai Corr variation of correlation for all scores.

**New Correlation**

When Numerai builds portfolios out of the Meta Model, a user’s highest and lowest predictions impact the Meta Model significantly more, and ultimately are more likely to make it into the portfolio. For this reason, in addition to looking at your model’s performance across all of its predictions, it’s important to also pay attention to the performance of the most extreme predictions.

We’ve previously suggested using something like “the correlation of your top and bottom 200 predictions” in order to make sure your predictions are also good in the extremes.

Improving on this idea, we’ve made a new correlation function which does the following:

  * Rank your predictions
  * Gaussianize your ranked predictions
  * Raise those to the 1.5 power
  * Transform target to be between -2 and 2 instead of 0 and 1
  * Raise the target to the 1.5 power
  * Take the Pearson correlation between the resulting predictions and target


    
    
    def numerai_corr(preds, target):
      # rank (keeping ties) then Gaussianize predictions to standardize prediction distributions
      ranked_preds = (preds.rank(method="average").values - 0.5) / preds.count()
      gauss_ranked_preds = stats.norm.ppf(ranked_preds)
      # make targets centered around 0. 
      centered_target = target - target.mean()
      # raise both preds and target to the power of 1.5 to accentuate the tails
      preds_p15 = np.sign(gauss_ranked_preds) * np.abs(gauss_ranked_preds) ** 1.5
      target_p15 = np.sign(centered_target) * np.abs(centered_target) ** 1.5
      # finally return the Pearson correlation
      return np.corrcoef(preds_p15, target_p15)[0, 1]
    

The result is that as with Spearman correlation, you still don’t need to worry about the distribution of your submissions, only the rank ordering. However the tails are now emphasized more than in a Spearman correlation.

This correlation, when applied to every score, is more similar to TC than the Spearman version of the same scores, indicating that these tails really have been under-emphasized before now.

Here’s the before and after for Numerai scores:

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/54bf042d028ca21b6401c1e4e38d0c18dd8a3d8d_2_664x500.png)1142×860 42.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/54bf042d028ca21b6401c1e4e38d0c18dd8a3d8d.png>)

And the before and after for Signals scores:

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5806ebe23c6394b56a49af57c73ce858acb1a229_2_667x500.png)1134×850 42.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5806ebe23c6394b56a49af57c73ce858acb1a229.png>)

Both Numerai and Numerai Signals will move all non-payout scores to use Numerai Corr immediately, while the payout scores (CORR20) will switch to Numerai Corr soon. For Numerai, payouts will switch to CORR20V2 on May 13. For Signals, payouts will switch to FNCV4 on June 3.

**New Targets**

Cyrus, Caroline, Sam, and Xerxes are four new targets which are all similar, with small variations. They will be included in the v4 and v4.1 datasets beginning on April 18.

Cyrus is our best target, and will become the CORR20 payout target in one month. The other three will not be used for payouts, but you might find that they are useful for training your models to be good at predicting Cyrus.

The “target” column in the datasets will also contain values for target_cyrus_20 starting on May 13.

Below is a comparison between a model trained on Nomi scored with the current CORR20 (Spearman correlation with Nomi) and a model trained on Cyrus scored with the new Numerai Corr with Cyrus.

The mean score is about the same, but the consistency of the new model with the new scoring method is vastly improved.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/bbb64294bd5778d0a179a748319cb2d298bb7ddf_2_690x483.png)1600×1123 106 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/bbb64294bd5778d0a179a748319cb2d298bb7ddf.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d62f865370471261c88080f445dc271216b5d4c5.png)832×110 7.46 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d62f865370471261c88080f445dc271216b5d4c5.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cadced581c05fa73f26be29ce8f1e583ff116efe.png)832×108 6.91 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cadced581c05fa73f26be29ce8f1e583ff116efe.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0272283c9f3c2f212db0d22c7ca588d44ed4010b.png)834×114 8.02 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0272283c9f3c2f212db0d22c7ca588d44ed4010b.png>)

Here’s a model built on target Nomi vs a model built on target Cyrus, both scored with Spearman on Nomi.

So even before the change to the definition of CORR20, switching to target Cyrus for training your models is beneficial, especially in terms of consistency.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8b26818f5d82bf2921ce8efbe3eae6eb32255884_2_690x483.png)1600×1122 99.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8b26818f5d82bf2921ce8efbe3eae6eb32255884.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b1958b115b8a1567804e3e93fd57fa1120a60aa1.png)348×106 3.77 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b1958b115b8a1567804e3e93fd57fa1120a60aa1.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/35acf3e8eca8ddc398d6f79e4b2f04f22c3d7c2c.png)340×106 3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/35acf3e8eca8ddc398d6f79e4b2f04f22c3d7c2c.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/bb494a42a0ecbbb01eb1432afcd481adda2063c1.png)342×114 4.11 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/bb494a42a0ecbbb01eb1432afcd481adda2063c1.png>)

Here we have an assortment of models on the new scoring.

All of the targets have something to offer and we hope that you use many of them for your ensembles. By themselves however, the newer targets tend to outclass Nomi.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f0935aa75e6e8e65b0f7063c313a4d48ef259093_2_690x482.png)1600×1119 158 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f0935aa75e6e8e65b0f7063c313a4d48ef259093.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2ca5b4c5bd072875eadeae74c097ff4080fae9a7.png)392×244 7.76 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2ca5b4c5bd072875eadeae74c097ff4080fae9a7.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2a364ab2112cf0f78e06d2d97d9a04dda7c9f74d.png)390×236 7.24 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2a364ab2112cf0f78e06d2d97d9a04dda7c9f74d.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/faecfd202232e8ae69fa1b2d435bd1f75b9c15a2.png)392×246 7.91 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/faecfd202232e8ae69fa1b2d435bd1f75b9c15a2.png>)

**Website changes**

CORR20V2 is the temporary name for the new Numerai Corr Cyrus score. It has been added to the compare scores page so you can see how your existing models would be affected by the change:

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/bc8f58b6c966096ac903dc6ef793bd934a8fd79f_2_690x252.png)1600×588 88.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/bc8f58b6c966096ac903dc6ef793bd934a8fd79f.png>)

On May 13 we will remove the existing CORR20, and CORR20V2 will become known simply as CORR20, and payouts will switch over to this new measure of CORR20.

Existing stakes will automatically switch to this new CORR20 for the round opening on May 13, so there’s no action required.

For Signals, CORR20V2 uses the same Signals target as the current CORR20, except it uses the new Numerai Corr instead of Spearman. Models will have their stakes transitioned to FNCV4 on Numerai Corr starting with the round opening on June 3.

Happy modeling

---

### Post #2 — **quantverse** | 2023-04-17 09:07 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png) master_key:

> `target_p15 = np.sign(target) * np.abs(target) ** 1.5`

Should we assume the target will be binned in range <0, 1> as it used to be? If so, the expression can be simplified I guess? (no need to use SGN and ABS)…

---

### Post #3 — **perfect_fit** | 2023-04-17 13:40 UTC

Have made a prototype for Numerai Corr in Numerblox, but 1st would like clarification on what distribution you expect for this function in the targets. Do we expect the targets are in range `[-1...1]` here?

If targets are in `[0...1]` then it doesn’t seem to make sense to calculate Pearson against gaussianized rank predictions. ![:thinking:](https://emoji.discourse-cdn.com/twitter/thinking.png?v=13)

Numerblox pull request for Numerai Corr:

[github.com/crowdcent/numerblox](<https://github.com/crowdcent/numerblox/pull/127>)

####  [New Numerai Corr metric in Evaluators](<https://github.com/crowdcent/numerblox/pull/127>)

`master` ← `feature/new-corr`

opened 01:26PM - 17 Apr 23 UTC

[ ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6acbadc102d417e21702599aee66df443b1d1e45.png) crowdcent ](<https://github.com/crowdcent>)

[ +168 -157 ](<https://github.com/crowdcent/numerblox/pull/127/files>)

Implements new "Numerai Corr" metric in Numerblox `Evaluator`s. Works with bot[…](<https://github.com/crowdcent/numerblox/pull/127>)h `NumeraiClassicEvaluator` and `NumeraiSignalsEvaluator`. More info on definition and discussion of the metric: https://forum.numer.ai/t/target-cyrus-new-primary-target/6303

---

### Post #4 — **master_key** | 2023-04-17 14:23 UTC _(reply to #2)_

Thanks for pointing this out - we actually use targets in the range of -2 to 2 internally so I had missed this. I’ve updated the numerai_corr code to move targets from the [0, 1] range to [-2, 2] range before raising to the 1.5 power

---

### Post #5 — **master_key** | 2023-04-17 14:25 UTC _(reply to #3)_

You’re right - we use -2 to 2 targets, not 0 to 1 targets. I updated the code in this post accordingly. Thanks for catching this.

---

### Post #6 — **qeintelligence** | 2023-04-17 19:02 UTC

Will the change to corrv2 scoring payouts start at the same time as the daily payouts? (as in a big bang release event)

---

### Post #7 — **qeintelligence** | 2023-04-17 20:14 UTC

Another question that pops up ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) would it be technically possible to also keep the corrv1 as scoring payout next to the corrv2? As in, make it optional for users to select which scoring they want to use (similar to the multiplier options). I can imagine this one would make things quite complex and maybe is not necessary.

---

### Post #8 — **maxchu** | 2023-04-17 23:48 UTC _(reply to #5)_

`centered_target = target - 0.5`  
This line just transform the target to be -0.5 to 0.5, not -2 to 2. Am i missing something?

---

### Post #9 — **mdo** | 2023-04-18 19:14 UTC _(reply to #8)_

Correlation is invariant to scale so multiplying the [-.5, .5] centered target by 4 to make it [-2, 2] doesn’t change the score.

---

### Post #12 — **liborty** | 2023-04-19 13:46 UTC

Is this new target going to be in the same column?  
Also, my corr20v2 is like one quarter of corr20.  
Is there a way of opting out of this?

---

### Post #14 — **bpa_praec** | 2023-04-21 18:32 UTC

Hi there,  
I have downloaded the new dataset after I saw this topic and my model’s rmse is much worse using the same target_nomi_v4_20, same model. Is anyone seeing that as well? The previous dataset I was using was downloaded February 23.  
Regards

---

### Post #15 — **camaron_ai** | 2023-04-21 19:14 UTC

hi everyone, I’m having problems replicating the scores of corrv2 from the leaderboard using the code above, my correlations are not exactly the same. Have anyone succesfully implemented and tested the new metric?

---

### Post #16 — **liborty** | 2023-04-23 00:19 UTC _(reply to #14)_

Yes, me too. Most of my corr20’s which I was betting on have gone from 90% to 0%.

---

### Post #17 — **bpa_praec** | 2023-04-23 10:06 UTC _(reply to #14)_

[@master_key](</u/master_key>)  
We are getting very strange results with this new dataset, it look likes all the targets have changed after you added the cyrus target to it (mainly target_nomi_v4_20). Can you have a look, please?

Basically, I fit the same model on target_nomi_v4_20, using the same rows I had in the dataset I download in February 23 and get completely different results. Unfortunately, I overwrote the February dataset and can’t compare it against the new one.

Regards

---

### Post #18 — **wigglemuse** | 2023-04-23 19:43 UTC _(reply to #17)_

I downloaded the train set just now to double-check (and the validation set yesterday to grab the latest eras w/ targets). Ignoring the new targets, I do not detect any changes in this data from data of weeks’ past, i.e. nothing that existed in the downloads 2 weeks ago has changed. Somebody on the discord was grumbling yesterday about some file corruption or something and couldn’t extract the data, and then Mike said he was fixing…you might re-download just to make sure if it really looks like the targets have changed, but much more likely you are doing something off (check the column headers) or your model results are much more stochastic than you realized using same data…

---

### Post #19 — **jrai** | 2023-04-24 13:16 UTC _(reply to #13)_

Although corr20 has a longer right tail, corr20V2’s left tail was pulled in quite a bit (likely a large contributing factor to the increased sharpes as well). The average corr20v2 score is lower than the average old corr20 score.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a225afb4138a793411daa1730d6baf0080c4dfb3_2_690x377.png)image1015×556 41.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a225afb4138a793411daa1730d6baf0080c4dfb3.png> "image")

The correlation between corr20 and corr20v2 is quite high.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/817a7e20e5f987b75fccee883a7463aeed8ee97f_2_476x500.jpeg)image983×1031 197 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/817a7e20e5f987b75fccee883a7463aeed8ee97f.jpeg> "image")

[@master_key](</u/master_key>) Is there still any work going into open sourcing some of the scoring pipelines?

(this post was edited to be the most up to date and removed the previous post to avoid confusion)

---

### Post #20 — **master_key** | 2023-04-24 14:44 UTC _(reply to #13)_

You beat me to it - we are just triple checking things before we put it back on the website and add some more details to the post.

The scoring for the website actually had the same issue that was found in the correlation function in this original post, where the targets weren’t being centered properly.

So we’ve recalculated all of the historical scores, and you should see scores that are much more similar to the previous corr20 scores.

I see a 98% correlation between corr20 and corr20V2 rep for example.

It does look like the typical and best correlation reputations are expected to decrease, while the Sharpe of correlation tends to increase.

You might want to filter out reps from this analysis which have many missing rounds, as it makes it look like reputations are much closer to 0 than they are in practice.

---

### Post #21 — **liborty** | 2023-04-25 00:59 UTC

After a lot of effort, I finally had a model that was performing really well on Corr20 and now you have messed it all up. Corr20v2 is much worse. I feel like I can not win here with these moving goalposts and constant changes for the worse. I am draining my stake.

You already have TC. I do not understand your motivation for redefining correlation to be “more like it”.

What was wrong with correlations > 0.015, that you have to actively prevent them?

---

### Post #22 — **restrading** | 2023-04-25 01:47 UTC

Can the graphs in the thread be also updated?

---

### Post #23 — **bpa_praec** | 2023-04-25 07:54 UTC _(reply to #20)_

[@master_key](</u/master_key>) corr20v2 is much lower than corr20 for every model which means you are automatically decreasing everyone’s payouts, why is that? Also, given you doing that, isn’t now time to allow users to set the corr weight to be higher the the current max of 1?  
Regards

---

### Post #24 — **morph3us** | 2023-04-26 13:26 UTC

[@master_key](</u/master_key>) The Diagnostics are still based on the nomi target and simple corr at this moment?

---

### Post #25 — **mdo** | 2023-04-26 16:48 UTC _(reply to #21)_

[@liborty](</u/liborty>) Improving your corr20v2 may be as simple as retraining on the new target. As shown in the original post, retrained models should have similar corr and better Sharpe under the new scoring. Have you tried that?

---

### Post #26 — **mdo** | 2023-04-26 16:52 UTC _(reply to #23)_

Existing models were not trained to be good at the new Cyrus target so it is expected scores on the new target would be lower. After retraining scores should be much more similar, but with less draw-down risk!

---

### Post #27 — **master_key** | 2023-04-26 17:09 UTC _(reply to #22)_

They were correct initially actually so still valid

---

### Post #28 — **ml_is_lyf** | 2023-05-08 13:06 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png) master_key:

> On May 13 we will remove the existing CORR20, and CORR20V2 will become known simply as CORR20

I’m just thinking won’t this make things confusing for historic content? References on the forum/discord to CORR20 pre CORR20V2 are going to be talking about a different metric, and it won’t be obvious unless you know that the meaning of CORR20 changed. Also this is going to make our code confusing too, as we’re going to have to remember that our code referencing CORR20 pre this change were actually referencing CORR20V1. Wouldn’t it be clearer to keep referring to it as CORR20V2?

Also is this going to be the case for the API too, e.g. CORR20V2 will disappear from the API and will be queried via CORR20 instead? If so couldn’t that silently break people’s code?

---

### Post #29 — **sirbradflies** | 2023-05-14 18:35 UTC

Hi,  
I thought that from May 13th the training dataset would use Cyrus as the column “target” but it seems, at least for the int8 version that I have just downloaded, that Nomi is still the main target (Corr 1 with “target” column).  
Did I miss anything? Isn’t Cyrus being used from this round?

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/061cf349c3fc636a3163883f0a0dd1e29c681212.png)image333×308 11.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/061cf349c3fc636a3163883f0a0dd1e29c681212.png> "image")

Thanks

---

### Post #30 — **master_key** | 2023-05-14 19:08 UTC _(reply to #29)_

You’re right - this didn’t get changed on time but this round is scoring on Cyrus. Sorry for the confusion.

---

### Post #31 — **edubergeek** | 2023-05-14 23:41 UTC

Are both **TC** and **CORR20** payouts based on target_cyrus_v4_20 beginning with round 484?

---

### Post #32 — **wigglemuse** | 2023-05-15 00:49 UTC _(reply to #31)_

TC doesn’t have a target.
