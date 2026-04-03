---
title: "Super Massive Data: Sunshine"
category: Announcements
url: https://forum.numer.ai/t/super-massive-data-sunshine/5977
created_at: 2022-12-27T16:36:40.603000+00:00
last_posted_at: 2023-03-23T19:38:58.549000+00:00
posts_count: 25
views: 7966
tags: []
---

# Super Massive Data: Sunshine

---

### Post #1 — **master_key** | 2022-12-27 16:36 UTC

# Super Massive Data: Sunshine

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/53525290ea68586b334349ef72bd62908ccc21d9_2_375x375.jpeg)1024×1024 176 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/53525290ea68586b334349ef72bd62908ccc21d9.jpeg>)

We believe that if we give the best data to the best community of data scientists, we will create the best hedge fund. And [evidence is building](<https://numerai.fund>) that we may be right.

As recently as 2019, Numerai had only 40 features data scientists could use for their machine learning models. Last year, we expanded the number of features to 1050 with the [Super Massive Data Release](<http://forum.numer.ai/t/super-massive-data-release-deep-dive/4053>).

Today, we’re releasing the largest set of features since Super Massive Data.

The new dataset contains 405 new features. It also contains all of the features from v4.0, besides the 10 dangerous features described in the [dangerous features post](<http://forum.numer.ai/t/removing-dangerous-features/5627>), for a total of 1586 features. It’s called Super Massive Data: Sunshine also known as Data Version 4.1.

Download Sunshine now from [numer.ai/data](<http://numer.ai/data>). Step into the light.

**Overview**  
Here’s a quick rundown of the updates talked about in this post:

  * 405 new features, for a total of 1586 features
  * Meta Model historical predictions released
  * New example script using new features, new targets, and better modeling
  * Can submit 20 more models per user now, for a total of 70 models
  * We are increasing the staking threshold by 20% from `300k` → `360k` on Numerai, and from `150k` → `180k` on Signals
  * Benchmark models are finally in development and coming soon
  * V3 dataset is being deprecated (but not breaking any automatic pipelines)



**New Features**  
Based on tests with two identical LightGBM models, by only adding the new Sunshine features, average correlation against target_nomi would increase from 0.033 to 0.035. We expect the Numerai community to be able to make significantly larger improvements to their performance.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/dc010a28319a8a924a5511d5b2a841168f8d1bcc_2_624x431.png)1600×1104 133 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dc010a28319a8a924a5511d5b2a841168f8d1bcc.png>)

Information on how to download the data can be found at [numer.ai/data](<http://numer.ai/data>).

One important difference between v4.0 and this new dataset is that some of the new features are not available for all of history. You will see some eras which contain missing values everywhere for some features. If you choose to use these features, make sure your code can properly handle NAs or use some method to impute the missing values.

Furthermore, we plan to add features to this dataset in the coming months, so make sure your code is robust to additional columns by always choosing the exact features and targets you want by name.

You can continue to use all previous versions of the data without your scripts breaking, but we believe large gains in performance and True Contribution are possible with Sunshine.

**Meta Model Release**

In addition to new features, the historical Numerai Meta Model is now also available for download.

With True Contribution, you are being rewarded for making positive alterations to the Meta Model.

Now you can test exactly how your model would have altered the Meta Model historically, and even train directly towards improving the Meta Model. For example, you could build a new target which is the difference between target_nomi and the Meta Model. In essence, training specifically to correct the mistakes the Meta Model makes.

The latest Meta Model predictions will be released 4 weeks after each weekend round, at the same time that the first 20D targets come out for that era.

We plan on adding these to diagnostics in the future to give better estimates of MMC than we are currently able to give today.

Download it at numer.ai/data or through the API with
    
    
    from numerapi import NumerAPI
    napi = NumerAPI()
    napi.download_dataset("v4.1/meta_model.parquet")
    

New Example Script

There is a [new example script](<https://github.com/numerai/example-scripts>), called example_model_sunshine.py, which uses the new data, [new targets](<http://forum.numer.ai/t/new-targets-for-the-tournament/5842>), and the new feature set. Below is the performance difference between the previous example model and the new one.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/45bae12b98a1eb766a4d8a99ceffe6d9453f8214_2_574x386.png)1600×1078 114 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/45bae12b98a1eb766a4d8a99ceffe6d9453f8214.png>)

This Sunshine example script builds models on our 6 favorite targets, ensembles them, and does some partial feature neutralization, resulting in a model with much higher Correlation and Numerai Sharpe than the previous example script.

**Research Suggestions**

With the recent target release, the new data release, and the release of the Meta Model, there are many new directions of research to pursue.

_To facilitate and encourage new research, we’ve increased the number of models that each user can submit by 20. This means you can now submit up to 70 models per week._

_We’ve also raised the staking threshold by 20% for the Numerai Tournament, from 300k to 360k._

The easiest way to get started is to copy the new example script, which is one of our best internal models to date.

When you are ready to conduct new experiments, here are some of our ideas for the next most valuable directions to take your research.

  * [Feature selection](<http://forum.numer.ai/t/feature-selection-with-borutashap/4145>) is more important than ever. This data set is much larger, with almost 1600 features. For one, there is a lot of redundancy in the features, and you can decrease your compute needs greatly by selecting a subset of features. Aside from saving compute though, using a subset of features for some of your models can increase the variety of your models and decorrelate them.
  * Build a new target by neutralizing an existing target to the Meta Model. A model trained on this target would then be trained specifically to correct the mistakes it expects the Meta Model to make.
  * Find a tournament round where your model gets an unexpected result on True Contribution, for example when you have high Corr and FNC, but your TC is low. For which targets does the Meta Model’s predictions outperform your model for this round? Does it do better on its top and bottom 200 predictions than your model? The answers may be clues to how you can alter your model to improve its True Contribution scores.
  * What’s the best way to deal with missing data? Should you fill missing features with the median? Is it better to leave them as NaN and let LGBM deal with it? Should you build a separate model that includes the features which have NaNs, and blend it with a model which has none of the NaN features? Can imputing the missing values with state-of-the-art imputation methods improve models?
  * Feature Neutralization - The new example script finds that 50% feature neutralization is a good balance between correlation and consistency (Numerai Sharpe). Is it better to neutralize only to a subset of features? Should some features be neutralized more aggressively than others?



Feel free to join us in [Numerai Quant Club](<http://forum.numer.ai/t/numerai-quant-club-with-michael-oliver/5933>) to discuss your findings on these topics or other ones.

**Benchmark Models First Look**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/70024aa2e228a32b604d8b7aca71a0deddba8c3a_2_122x260.png)516×1094 132 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/70024aa2e228a32b604d8b7aca71a0deddba8c3a.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/1f5e4b8cd4075610e2d431e62a949e94b6850298_2_485x213.png)1600×705 163 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1f5e4b8cd4075610e2d431e62a949e94b6850298.png>)

Here is the first wave of benchmark models that we’re working on.

If you look at the top model: LG_LGBM_V4_VICTOR60

This is a model which uses a large LGBM model (same parameters as the new example script), uses the V4 dataset, and trains using target_victor_v4_60.

The idea is for these models to be constantly testing various ways to build predictions, and showing their TC, in order to illuminate what the Meta Model needs more or less of.

It’s only been a few weeks, but so far all 12 of these models have positive TC, suggesting that more people should try building models in a similar fashion.

The next steps for us are

  1. To fill in these scores historically so that you can get a more complete picture of how each of these models has performed over time.
  2. To add the code to the example script repo showing how to build these models, so that you can build them yourself and improve on them directly.



The [Sunshine example model](<https://numer.ai/sunshine_example>) has been added now, so you can track how it performs going forward.

**Deprecating V3 Dataset**

The V3 dataset has various problems that we solved in V4. These issues make models trained on V3 worse, and they make the dataset much harder to maintain.

That is why on April 1 2023, we will be doing a soft deprecation of the V3 dataset.

We recommend that you update any models which are still relying on the V3 dataset by retraining them on the V4.1 dataset, or replacing those models with new ideas entirely, based on experiments with Sunshine.

However, we will keep the V3 dataset running in order to avoid any completely broken pipelines.

There are a couple of changes happening.

First, we will remove the V3 dataset from the website. Although we will continue serving the V3 data files through the API in order to not break any automated pipelines.

Second, the V3 features will be slightly altered.

Recall that the V4.0 data has one-to-one analogs of all 1050 features in the V3 dataset, albeit slightly improved. So the features in the V3 dataset will be changed to be the V4 versions of those features (while retaining their V3 names of course) at the time of deprecation. This will have little to no effect for the vast majority of models as the corresponding V4 features are very highly correlated with the V3 version. Even so, it would be safer to have migrated to the V4 dataset already by this time.

Even though this is a very soft deprecation, we don’t take it lightly, and we don’t have any plans to deprecate any of the other datasets.

The V2 dataset will continue to be available as always, and we plan on continuing support for the V4 and V4.1 datasets for years to come.

---

### Post #2 — **glenk** | 2022-12-28 15:13 UTC

I’ve been curious about how strong the meta-model was for quite a while, so thank you for providing the historical predictions.

However, I must say that I’m a bit disappointed after seeing them. I decided to benchmark the meta-model predictions against a plain LightGBM model trained on V4 data from prior (up to 724) eras. The LightGBM model got a spearman score of 0.0268 while the meta-model got a score of 0.0275 (both scored on eras 888-1028). Am I missing something here?

---

### Post #3 — **master_key** | 2022-12-28 17:02 UTC _(reply to #2)_

A couple of things that you might be missing:

  1. The Meta Model typically excels in consistency more than it does in pure mean. You should pay attention to statistics like drawdown as well when doing comparisons of model performances.

  2. V3 Data didn’t even exist yet at the start time of the Meta Model! So you’re comparing your V4 model vs a Meta Model which only had access to V2 data for the beginning, V3 data around half way through, and then V4 data towards the very end.

---

### Post #4 — **wigglemuse** | 2022-12-28 17:22 UTC _(reply to #3)_

And didn’t even have the nomi target (which I assume you are scoring on?) until 40-something eras in. Be interesting how much difference from something trained on v2 data with uniform target.

---

### Post #5 — **shatteredx** | 2022-12-28 18:40 UTC

Hi,

Please consider not altering the v3 features, even a little.

Thank you.

---

### Post #6 — **taori** | 2022-12-28 23:37 UTC

The historical Numerai Meta Model data is such a great addition, well done. Also the 20 additional models per user are very welcome as well, especially now with all the new possibilities to test. If only you could deploy the account level staking feature too, then I would be happy to start trying new experiments again.

---

### Post #7 — **liborty** | 2022-12-30 03:19 UTC _(reply to #3)_

Randomly missing data is a really bad practice. There is no good way of dealing with it.

---

### Post #8 — **wigglemuse** | 2022-12-30 03:22 UTC _(reply to #7)_

Randomly missing data is the rule rather than the exception with real-world data. There are certainly ways of dealing with it. And it is missing for everybody here so you’re at no disadvantage.

---

### Post #9 — **liborty** | 2022-12-30 03:25 UTC _(reply to #8)_

I meant there is no satisfactory way of dealing with it conceptually, except ad-hoc hackery.  
On the technical side, if I am converting .parquet to .csv, how are these missing items going to show up? Will there be space between two commas , , in its place, or will all the following features in a row be shifted up and then missing at the end? Would you consider at least introducing a marker, such as ,2.0, (= missing item) , by which they can be recognized?

---

### Post #10 — **wigglemuse** | 2022-12-30 03:48 UTC _(reply to #9)_

Ad-hoc hackery is underrated. And although you can’t really deal with questions of _why_ something is missing in an obfuscated dataset, you can deal with it in a conceptually coherent way just treating it as “thing you must deal with that everybody else also has to deal with” and think about what is the best way that is going to work for your methods?

They’d show up as NaNs or NAs I believe but there may be settings somewhere to control that (in your import/parquet function) – we already have rows with some of the targets sometimes missing in v4 – same as those I woud think.

---

### Post #12 — **liborty** | 2022-12-30 06:11 UTC _(reply to #10)_

Could you please explain how you arrived at 1586 features?  
Under 4.0 we had 1191 + 405 new ones = 1596

---

### Post #13 — **jefferythewind** | 2022-12-30 11:36 UTC _(reply to #12)_

There were 10 “dangerous” features removed from the data set.

---

### Post #14 — **yvasilev** | 2022-12-31 19:35 UTC

Hi master_key,

Could you please elaborate on the meaning of:

> _We’ve also raised the staking threshold by 20% for the Numerai Tournament, from 300k to 360k._

Is that when the exponential decay for payout factor starts? or what is the new threshold for?

Thanks!

---

### Post #15 — **morph3us** | 2023-01-03 12:34 UTC

Does the validation dataset now contain the daily eras? If yes how can we identify them? Round numbers and era numbers don’t match. It would be misleading to train or validate on dataset that has weekly cadence for most of it and daily cadence for the last part. This would scew the model towards towards the very end of it

---

### Post #16 — **pumplerod** | 2023-01-03 14:34 UTC

Love the addition of meta_model prediction results! Regarding these; currently the `meta_model.parquet` consists of eras 0888-1038. Assuming Numerai continues to update this parquet file with new eras as they become available, is there a plan to back fill eras earlier than 0888? Is that even possible with nomi?

The Diagnostics eras start at 0857. I think it would at least make some sense to include all the eras from the diagnostics set, if possible

---

### Post #17 — **master_key** | 2023-01-08 19:16 UTC _(reply to #15)_

No all of the data is still only weekly

---

### Post #18 — **master_key** | 2023-01-08 19:16 UTC _(reply to #16)_

Not really possible to include older meta models just due to system changes prior to the first era chosen

---

### Post #19 — **master_key** | 2023-01-08 19:19 UTC _(reply to #14)_

You can see some more detail here: [Overview | Numerai Docs](<https://docs.numer.ai/tournament/learn#payouts>)

The gist is that once there is more than 300k staked across all users, everyone’s payouts are multiplied by `300k / total_stake` .

But that 300k is being changed to 360k now.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/fd707a689e26b1ce442964f80721759f8cc07eec_2_690x259.png)image1662×626 78.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fd707a689e26b1ce442964f80721759f8cc07eec.png> "image")

---

### Post #20 — **nameofmyai** | 2023-01-09 08:50 UTC

It’s great that the historical meta model predictions have been released. I’m wondering what the correct way to calculate TC of my models based on his is though. Any pointers?

---

### Post #21 — **sneaky** | 2023-01-09 11:04 UTC

Just in case, should we expect NAs to appear in tournament data as well, or are they only in the historical data? Thank you!

---

### Post #23 — **jaca_ml** | 2023-03-12 14:32 UTC

Hi, I have a question, It is not clear to how to ‘Build a new target by neutralizing an existing target to the Meta Model’. You only can neutralize a prediction (or target) but not one out of the other right?

---

### Post #24 — **wigglemuse** | 2023-03-12 14:42 UTC _(reply to #23)_

Basically subtracting the metamodel from one of the given targets, and training on the residuals. (You can only do this eras >= 888 where we have the metamodel predictions.) And then if the future metamodel is like the old metamodel, and the new eras are like the old eras, then the mistakes it makes going forward should be similar and your model will pick up the slack. The first assumption is not bad – the metamodel seems to change slowly. However it may not stay that way precisely because people can now make models in this way. The second assumption is more dubious but we have that problem of non-stationarity of the market no matter what strategy we use.

---

### Post #25 — **osyokuji** | 2023-03-18 16:04 UTC

Am I missing something?  
Where does the number total of features 1586 come from, 1050(v4)+405(v4.1)=1455 and where are the other 131 features?

---

### Post #26 — **wigglemuse** | 2023-03-18 16:21 UTC _(reply to #25)_

1050 was v3. v4 had 141 more = 1191. But then 10 were designated “bad” from v3 & v4, and those were gotten rid of for v4.1. So 1181 v4 features carried over to v4.1 + 405 more = 1586.

---

### Post #27 — **lcrmorin** | 2023-03-23 19:38 UTC

Is the gap between the last era with targets in the validation data and the live era known ? constant ?
