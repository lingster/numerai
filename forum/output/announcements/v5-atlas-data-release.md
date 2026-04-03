---
title: "V5 'Atlas' Data Release"
category: Announcements
url: https://forum.numer.ai/t/v5-atlas-data-release/7576
created_at: 2024-07-17T15:02:00.897000+00:00
last_posted_at: 2024-10-06T14:42:21.976000+00:00
posts_count: 34
views: 4699
tags: []
---

# V5 "Atlas" Data Release

---

### Post #1 — **ark** | 2024-07-17 15:02 UTC

V5 “Atlas” Data is here. Don’t worry, nothing is changing right now. You cannot submit on v5 yet. Live data will be released in September.

This release expands and improves the universe we use to craft our dataset, thus evolving our features and targets to be more predictive. Because features and targets significantly changed, you will need to retrain your models as any model trained on v4.x data will soon be obsolete. The new data offers more diversification in rows in each era, higher correlation, and lower variance. Our research shows that most models will simply have higher CORR when retrained with this data.

For example, when we compare the performance of our [hello_numerai](<https://github.com/numerai/example-scripts/blob/master/hello_numerai.ipynb>) tutorial notebook running on v4.3 vs v5 we can see a drastic improvement in performance with no change to the underlying model:

CORR | v4.3 | v5.0  
---|---|---  
mean | 0.0245 | 0.0293  
std | 0.021 | 0.021  
sharpe | 1.1379 | 1.335  
max drawdown | 0.0637 | 0.0329  
  
Furthermore, since our hedge fund is now trading a different universe than v4, we must have predictions on all of these new stocks which aren’t in the old data version. We had hoped that old models would be able to predict the new universe just as well, but instead our internal research found that there is a steep decline in performance when v43 models attempt to predict on v5.

It’s clear that the new universe forces a breaking change, but we are aiming to give everyone plenty of time to re-train their models on the new dataset. For now, we have only released the v5 training and validation datasets so you can start exploring. Here is what is currently available in the API:
    
    
      "v5.0/features.json",
      "v5.0/train.parquet",
      "v5.0/train_benchmark_models.parquet",
      "v5.0/validation.parquet",
      "v5.0/validation_benchmark_models.parquet",
      "v5.0/validation_example_preds.csv",
      "v5.0/validation_example_preds.parquet"
    

Here is the current roadmap for this data release:

**July 19**

  * Support v5 data in diagnostics



**September 13**

  * Release v5 live data:
        
        "v5.0/live.parquet"
        "v5.0/live_benchmark_models.parquet"
        "v5.0/live_example_preds.csv"
        "v5.0/live_example_preds.parquet"
        

  * Support v5 data in Model Uploads

  * Start accepting v5 submissions, but v5 submissions will not be scored




**September 17**

  * Update example scripts and tutorial notebooks
  * Start submitting benchmark models to website



**September 27**

  * Change all scores and payouts to v5
  * Stop supporting v4 data
  * Stop accepting v4 submissions



**FAQ**  
What’s different about v5?  
The universe (the list of stocks we are willing to trade) has changed. This means features and targets have also changed due to the nature of ranked residual returns. Because of this, we have changed the feature names. In our research, we have found that models trained on v5 data are significantly better at predicting targets than v4 models.

Can I still train and submit on v4 data?  
Yes. All v4 data (v4 through v4.3) is still supported for the next 2 months. You can train and predict on all v4.x until September 27. After this date, all v4.x data will no longer be updated and you will no longer be able to use it for live prediction.

What will happen to my models?  
Nothing for now. No breaking changes will happen until September 27. On September 27, if your model is still submitting on v4, it will fail to submit.

Where is the live data?  
It’s coming in September. Live data is not publicly available because you will not be able to submit predictions on v5 until September.

Can I use v4.3 models on v5 data?  
No. V5 changes the universe of stocks used to craft the dataset, thus changing IDs, features, and targets. Our research has shown that v4 models are extremely bad at predicting v5 - do not use v4 models to predict v5.

Where are all of the targets?  
Upon release, the datasets only have 4 targets: cyrus_20, cyrus_60, teager_20, and teager_60. After we some more research and development, we will include the following targets in the v5 datasets:

  * Ralph
  * Victor
  * Tyler
  * Waldo
  * Alpha
  * Bravo
  * Charlie
  * Delta
  * Echo
  * Jeremy
  * Teager
  * Cyrus
  * Caroline
  * Sam
  * Xerxes

---

### Post #2 — **ark** | 2024-07-17 18:47 UTC

FYI, if you take a look at our [example_model](<https://github.com/numerai/example-scripts/blob/master/example_model.ipynb>) \- it’s performance on v4.3 validation data is as follows:  


[![Screenshot 2024-07-16 at 12.19.42 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/37b30939e05a573c5e56c2beb2151c9fd1279646.png)Screenshot 2024-07-16 at 12.19.42 PM690×316 16.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/37b30939e05a573c5e56c2beb2151c9fd1279646.png> "Screenshot 2024-07-16 at 12.19.42 PM")

  
And after updating to use v5 data it’s performance measurably improves:

[![Screenshot 2024-07-16 at 12.19.55 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3f9ae0bf7e5d0e2f2c9601c400cf8c57afb8d48d_2_345x151.png)Screenshot 2024-07-16 at 12.19.55 PM704×310 16.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3f9ae0bf7e5d0e2f2c9601c400cf8c57afb8d48d.png> "Screenshot 2024-07-16 at 12.19.55 PM")

---

### Post #3 — **psyrex** | 2024-07-17 18:51 UTC _(reply to #2)_

I think the images are duplicated [@ark](</u/ark>)

---

### Post #4 — **slashv** | 2024-07-17 18:57 UTC

I respect your dedication to keeping numerai up-to-date, however… in this post: [Midnight Data Release](<http://forum.numer.ai/t/midnight-data-release/6954>) from a mere 6 months ago, you stated:  
"  
We’ve been moving at a crazy pace for the last year or so, releasing new data or targets or payouts every couple of months, and we know some of you have whiplash trying to keep up.

There are no other target or data releases on our immediate calendar.  
"  
Followed by that you can’t guarantee anything of course…

Now this ‘promise’, if I can call it that isn’t even mentioned here and we’re now looking at a forced transition in a 2 week period in September? What if you happen to not have any time available during those 2 weeks?  
Long story short, this certainly doesn’t do much good for my confidence in Numerai.

---

### Post #5 — **ark** | 2024-07-17 20:05 UTC _(reply to #3)_

You’re right, just updated the image, thanks for pointing out.

---

### Post #6 — **ark** | 2024-07-17 20:44 UTC _(reply to #4)_

Sorry you feel that this degrades your confidence in Numerai. Our research has shown that the new universe in v5 data is a significant improvement from v4.x datasets and that the universes don’t mix well between data versions. This is why we must perform the hard cutoff of v4.x data.

---

### Post #7 — **slashv** | 2024-07-17 22:03 UTC _(reply to #6)_

As said, I understand you need to setup the data in such a way that maximizes the fund’s performance. On the other hand, it’s not clear to me how data scientists will benefit from this even though they are the ones who will have to make the effort to at least re-train their models and potentially do more than that to get good performance on the new data.  
It’s quite possible that I don’t fully understand the relation between the fund doing well and the benefit to data scientists. Maybe you could elaborate on this? I could for example imagine that the fund would buy numeraire when doing well and thus support data scientist by driving up the token’s price, but I haven’t read anything of the kind. If there’s no benefit for data scientists, then data updates are just additional work and something like a predictable data update schedule would be quite desirable imho.

---

### Post #8 — **rustydata** | 2024-07-18 02:16 UTC

Same features, renamed, and rescaled. And it does model better. It’d be nice if we could upload before the 17th.

---

### Post #9 — **joakim** | 2024-07-18 02:28 UTC _(reply to #8)_

I agree with this. I’d be happy to beta test v5.0 on live from Aug 17 [@ark](</u/ark>) .

---

### Post #10 — **svendaj** | 2024-07-18 22:32 UTC

Those who are using Kaggle, can now access public dataset with V5 data - [numerai latest tournament data (kaggle.com)](<https://www.kaggle.com/datasets/svendaj/numerai-latest-tournament-data>). It will be automatically updated about 15 minutes after Saturday round opening (webhook). Here is public Kaggle notebook producing this dataset: [numerai data (kaggle.com)](<https://www.kaggle.com/code/svendaj/numerai-data>).

No need to download the data over and over again. Just [attach the dataset or notebook as your input](<https://www.kaggle.com/docs/notebooks#adding-data-sources>) and it will be available for your experiments.

---

### Post #11 — **liborty** | 2024-07-20 22:21 UTC

What exactly are the changes to features and targets? How many more? What values? Could you give a summary here please, so we do not have to download gigabytes of data and search through it? Also, how many instances (rows) in training+validation sets?  
By how much is the overall volume of data growing again?

---

### Post #12 — **wigglemuse** | 2024-07-20 23:42 UTC _(reply to #11)_

There are more rows in every era – picking a random recent era it’s got 1487 more rows than the equivalent era in the v43 dataset. (Older eras the increase isn’t as great seems like.)

That’s the bulk of the change. There are no new features. However, since all feature and target values come in buckets in a specific fixed distribution, the addition of new rows means that a certain number of values in each row are going to change. So the row in each dataset representing the same stock in the same era with the same features will nevertheless have different feature and target values. (So more accurately, there are more rows, and all the old rows have changed as a result.)

The other part of the change (so far) is they’ve only got cyrus & teager targets included (20d & 60d), but they are promising to add back at least some of the targets we had before.

And for some reason (as of this writing) the feature column names have all changed so we aren’t quite sure if the old column order (with the “same” features) is preserved or not. And the data seems to be an inconsistent state right now as I write this, but I’m sure that will get worked out in a few days. So unless you’re in a hurry I’d watch the discord (and this thread) and give it a few days at least to see if it stabilizes and I’m hoping we’ll get some of those targets back sooner rather than later.

---

### Post #13 — **liborty** | 2024-07-21 01:20 UTC _(reply to #12)_

Thanks for that. That should be backwards compatible with my way of processing. I do not need any more targets. The only regret is that I will still need to be downloading the whole lot every week.

---

### Post #14 — **neosbrother** | 2024-07-25 16:17 UTC

The performance difference is great to see. The v5 data contains new stocks that aren’t in v4.3, right? Is there any data on how the v4.3 stocks do in the v5 data? I’m wondering if the improvement is due to the added stocks being more predictable or if the improvement is across the board.

---

### Post #18 — **rdugh** | 2024-07-29 12:18 UTC

[@ark](</u/ark>) Thanks for the update. A few questions:

  * When will you add all the above-mentioned targets?
  * Is the dataset fully ready to train new models? I see the targets follow a new naming convention (‘target_cyrusd_20’, ‘target_cyrusd_60’, ‘target_teager2b_20’, ‘target_teager2b_60’). Based on previous datasets, the name was like ‘target_cyrus_v4_20’.
  * Can you provide some details on your criteria for including or excluding the targets? For example, include Jeremy (instead of Jerome). I remember Jerome outperforming at one point.
  * What is the difference in features (or engineering of new features) between v4.3 and v5.0 to get that additional boost in performance?

---

### Post #19 — **ark** | 2024-07-29 22:57 UTC

# V5 Update: Jul 29, 2024

We have released more targets into the v5 dataset.  
The following targets are available now:

  * ralph
  * victor
  * tyler
  * waldo
  * alpha
  * bravo
  * charlie
  * delta
  * echo
  * jeremy
  * teager2b
  * cyrusd
  * caroline
  * sam
  * xerxes
  * rowan
  * agnes
  * claudia



## FAQs

**Is the dataset ready now?**  
Yes. We don’t plan on making any fundamental changes to the data. You should begin training on it as soon as possible.

**Why these targets?**  
We decided to only add targets that were most pertinent to this dataset and were easiest to release with minimal research. Some of the targets are upgraded versions of older targets and any targets not included in this release are either too old or have not been researched enough to ensure predictive quality.

---

### Post #20 — **numerologist** | 2024-08-02 17:50 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/slashv/48/3451_2.png) slashv:

> Now this ‘promise’, if I can call it that isn’t even mentioned here and we’re now looking at a forced transition in a 2 week period in September? What if you happen to not have any time available during those 2 weeks?  
>  Long story short, this certainly doesn’t do much good for my confidence in Numerai.

First off, I share your sentiment, I really do. Some of my best models will be dead after the V5 transition, because they were meticulously crafted and pre-trained on very specific sets of eras and with very specific seeds. To do all of this again takes a lot of time and resources (which is not very feasible with the current payout structure), and might not even be possible anymore (due to much lower drawdowns in the new data).

But here’s the reality check: there is a big difference between what’s good for the tournament and what’s good for Numerai’s (benchmark) models. And you can guess where I’m heading.

V5 does look better on paper. On the other hand, is it fair toward us, participants, to nuke everything that we built before V5 and on short notice? Probably not, but hey, this is the game: if you have to rely on Numerai, then you accept the rules of the game, and “the game” comes with all the broken promises and breaking changes. If you don’t like it, you can sail on your own, or try something that breaks less often - like Signals.

There is an upside to it though: new blood will come and might do something great with it. Or not. It actually doesn’t matter, as long as the benchmarks can keep the fund afloat. And, at the end of the day for this business, that’s the only thing that matters. ![:slightly_smiling_face:](https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=15)

---

### Post #21 — **slashv** | 2024-08-02 18:35 UTC _(reply to #20)_

[@numerologist](</u/numerologist>), well put. The “if you don’t like it, feel free to leave” argument always work of course and is fair enough. I am fairly new to the tournament, so I wasn’t really aware of the “rules of the game” and this is an introduction to working with a financial institution for me: “broke promises and breaking changes”. I should have known ![:stuck_out_tongue:](http://forum.numer.ai/images/emoji/twitter/stuck_out_tongue.png?v=12)

---

### Post #22 — **pschyska** | 2024-09-05 18:27 UTC

[@ark](</u/ark>) Why did you remove the v43_to_v5_map?  
I didn’t see _any_ indication that my old V4.3 models didn’t work on V5 data. They actually get much better validation results on V5, probably because V5 seem much easier to predict.

Additionally, when manually looking at the last few weeks worth of live rounds, the intersecting IDs features don’t seem to change very much (apart from a few 1-token changes at the fringes, e.g. “1” becoming “2”), but I didn’t analyze it much TBH.

Here are some validation results of a few of my models:  
p_test_a: Is an old model trained on v4.3 originally with an adapter that can accept v4.3 or v5.0 feature names, and will map v5.0->v4.3 if needed. (I call this “454”, because it will actually map v4.3->v5.0->v4.3, where the first transformation is a no-op when taking v5.0 data in - that way the model can take either). The corr graph looks similar, and the performance on v5.0 is much better, even though nothing besides mapping feature names changed (0.0337 corr 1.8104 sharpe v5.0 vs 0.0303 corr 1.4699 sharpe v4.3).

hxxps://photos.app.goo.gl/oLUkzw5pUnLYrD699  
hxxps://photos.app.goo.gl/HJ2ii5EZA8SvBkHdA  
(Can’t post images or links ![:roll_eyes:](http://forum.numer.ai/images/emoji/twitter/roll_eyes.png?v=12))

p_test_j: A new model that I trained up on v5.0 data, with “45” adapter, i.e. will map v4.3->v5.0 if called with v4.3, and take v5.0 as-is. This works fine on v4.3 data, even though it was trained on v5.0 (0.0367 corr 1.7474 sharpe v5.0, 0.0327 corr 1.5078 sharpe v4.3)

hxxps://photos.app.goo.gl/xbPNpZ82Q7Y7MDKf6  
hxxps://photos.app.goo.gl/MUSXfqbKVa5Av41y5

As both of these use benchmark model ensembling, here is a v4.3 model that doesn’t use benchmark models as well:

p_test_c: 0.0272 corr 1.5576 sharpe v5.0, 0.0264 corr 1.3589 sharpe v4.3. This model is obviously very bad, but again it seems to work fine on v5.0, and still having better validation results.

hxxps://photos.app.goo.gl/Sp6qtdrqU3RHEQjc7  
hxxps://photos.app.goo.gl/rDkP6SKu2sqS9HUg6

Am I missing something?

The v5.0 launch is honestly very stressful for me. First, you indicated that we’d have to scrap everything and start from scratch because of the feature renaming. Then I saw that you added the v43 feature map, and was relieved that I could at least still run my best v4.3 models after writing the adapter code. Now, you removed the map and I’m back at square 0. All that in an extremely tight timeframe.

---

### Post #23 — **stochastic_geometry_1** | 2024-09-09 03:08 UTC

Just to be explicit here. V5 submissions will be possible from Sept 13 onwards. Will they be scored? Honestly reading the timeline here it seems that no scoring is enabled until Sept 27? So we have to upgrade to our V5 model without knowing how it scores? This seems sub-optimal.

---

### Post #24 — **ark** | 2024-09-12 00:24 UTC

[@pschyska](</u/pschyska>) This was a mandate that we could not provide a v43->v5 map as we only want models trained on v5 data. Models trained on v4.x data, on average, will not have stable performance in the long run.

[@stochastic_geometry_1](</u/stochastic_geometry_1>) correct, V5 submissions will not receive scores right away. You can rely on validation / diagnostics to check the performance of a model.

---

### Post #25 — **pschyska** | 2024-09-12 11:43 UTC _(reply to #24)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/ark/48/3156_2.png) ark:

> [@stochastic_geometry_1](</u/stochastic_geometry_1>) correct, V5 submissions will not receive scores right away. You can rely on validation / diagnostics to check the performance of a model.

I challenge the fact that validation performance is enough to gauge the live performance adequately. In my experience, validation results don’t correlate strongly with live performance, especially when considering 0.5Xcorr + 2Xmmc scoring: one of my models, p_tt_rg, has quite poor corr (0.02208/1.2603 live, by my calculation, 0.01916/0.92306 validation), but is in the 98,4th percentile for live score due to mmc. I would have never have selected that model to deploy, it was a happy accident because I wanted to test something with it. As you can’t optimize for mmc, you are essentially asking us to stake models with close to 0 information on how they will do on Sept 27. This sounds like a huge gamble for both parties.

But if it were true we could rely on validation, your claim that models trained on V4.x data can’t have stable performance doesn’t make sense. I showed you how one of my V4.3 models (the first one linked) goes from 0.0303/1.4699 to 0.0337/1.8104 on validation. If you have more specific information about that phenomenon, please share it. In my experiments so far, I have yet to see a V4.3 model that does worse on V5.0 validation. For example: did you consider models other than GBDTs? Maybe models using deep learning or not interpreting the features mainly numerically behave differently?

---

### Post #26 — **rpica** | 2024-09-14 14:12 UTC

I just retrained and uploaded models… why not scoring them? As already discussed, I can also attest how different it is from diagnostics to live submissions.

---

### Post #27 — **smilence666** | 2024-09-19 01:46 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/ark/48/3156_2.png) ark:

>   * dia
> 

> 
> We have

so when you said no score between 9/13 - 9/27, that’s for every submission including the v4 one and it is literally no score and no payout???

---

### Post #28 — **wigglemuse** | 2024-09-19 02:14 UTC _(reply to #27)_

No, v4 will continue until switchover day. But there is no overlap of scoring both.

---

### Post #29 — **smilence666** | 2024-09-20 03:42 UTC _(reply to #28)_

Thanks, that’s fair.

---

### Post #30 — **edubergeek** | 2024-09-22 15:17 UTC _(reply to #23)_

A week of scoring would be useful.

---

### Post #31 — **edubergeek** | 2024-09-22 15:19 UTC _(reply to #19)_

Do I have to drain my v4.3 staked models or will the v4.3 staked amounts become available on Sep 27 for staking v5 models?

---

### Post #32 — **kenfus** | 2024-09-22 16:18 UTC

Always happy to see Numerai evolve! Any update on meta_model.parquet for V5?

---

### Post #33 — **wigglemuse** | 2024-09-22 18:35 UTC _(reply to #31)_

Just upload your v5 predictions to the same slots that are already staked starting on the switchover day. (The last of the v43 staked rounds will still take another month to resolve after it stops accepting them, so you can’t just move those stakes immediately to other slots.)

---

### Post #34 — **ark** | 2024-09-23 22:25 UTC _(reply to #32)_

v5 meta_model.parquet should be available on September 27

---

### Post #35 — **holden263** | 2024-09-26 06:56 UTC

Is there a chance to get v43_to_v5_map? I missed the opportunity to get that mapping when it was available.

---

### Post #36 — **svendaj** | 2024-09-28 19:58 UTC

Now also Numerai example scripts provided on Kaggle platform are retrained on v5.0 data and uploaded to the tournament (each profile has link to the Kaggle source code):

  * [JOS_KAGGLE_HELLO Profile - Numerai](<https://numer.ai/jos_kaggle_hello>) \- basic tutorial trained on small feature set. Best performer with +100% return.
  * [JOS_KAGGLE_MEDIUM Profile - Numerai](<https://numer.ai/jos_kaggle_medium>) \- same basic tutorial just trained on medium feature set. It used to be called JOS_KAGGLE_SHATT because it used [ShatteredX’s Improved & Compact Feature Set (225 features) for v4.3 Midnight Data](<http://forum.numer.ai/t/shatteredxs-improved-compact-feature-set-225-features-for-v4-3-midnight-data/6982>), but because it was worst performer with “just” +40% return, I have changed it back to medium feature set with v5.0 data.
  * [JOS_KAGGLE_MEDIUM_FN Profile - Numerai](<https://numer.ai/jos_kaggle_medium_fn>) \- tutorial #2 explaining feature neutralization, trained on medium feature set. Second worst performer with just 53% return. Interesting is that it is actually quite difficult to achieve better metrics with feature neutralization on v5.0. Anyone have an explanation?
  * [JOS_KAGGLE_MEDIUM_TE Profile - Numerai](<https://numer.ai/jos_kaggle_medium_te>) \- 3rd introductory tutorial explaining ensembling, trained on medium feature set with 55% return.
  * [JOS_KAGGLE_SUNSHINE Profile - Numerai](<https://numer.ai/jos_kaggle_sunshine>) \- older example from github (now not available) featuring both ensembling and neutralization on 1/4th downsampled “all data” with medium feature set - second best performer with above average 77% return.



So let’s see how they will work in “Atlas” era. ![:crossed_fingers:](http://forum.numer.ai/images/emoji/twitter/crossed_fingers.png?v=12)

---

### Post #37 — **kenfus** | 2024-10-06 14:42 UTC _(reply to #34)_

Hello, is it still coming? I selected my model with the help of that data in the past and if it’s no longer provided, I’ll need to change my strategy.
