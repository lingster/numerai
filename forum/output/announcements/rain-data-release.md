---
title: "Rain Data Release"
category: Announcements
url: https://forum.numer.ai/t/rain-data-release/6657
created_at: 2023-09-06T21:17:19.935000+00:00
last_posted_at: 2023-10-06T12:27:48.281000+00:00
posts_count: 11
views: 5350
tags: []
---

# Rain Data Release

---

### Post #1 — **master_key** | 2023-09-06 21:17 UTC

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3612777cf77e28a0a0375843bae41b1c9594f3c2_2_547x488.jpeg)1490×1332 546 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3612777cf77e28a0a0375843bae41b1c9594f3c2.jpeg>)

# Overview

Rain is ready. Rain is our latest dataset release for Numerai. Rain contains 666 new features and 12 new targets, and entirely new feature groups to give Numerai data scientists a new way to do feature selection. Altogether, Rain contains 2132 features and 48 targets.

Rain outperforms our previous dataset, [Sunshine](<http://forum.numer.ai/t/super-massive-data-sunshine/5977>), on every metric-- in addition to being far more accessible.

# New Features

There are 666 new features in Rain. In the last several data releases, the new data came from completely new underlying sources. However, in the Rain release, almost all of the features are generated from features which are already in the tournament. For the majority of them, this was done by fitting weights to a time series of each feature in such a way that improves predictive capabilities over the training data.

For this reason, data scientists might want to treat them differently. For example, any cross-validation done within the training data alone is likely to favor some of the Rain features much more than experiments done on the validation set would, because the Rain features are built to be good specifically at training data.

Note though that there were many controls put in place to prevent overfitting these features on the training data; not a single rain feature uses any forward looking data after era 575, meaning the out of sample period after era 575 is still truly out of sample.

# New Targets

There are 6 new targets in Rain. Each has a 20D and 60D variant, for a total of 12 target columns.

Jeremy is a slight modification to the Jerome target.

The 5 other targets, Alpha, Bravo, Charlie, Delta, Echo - are intended to fill in gaps in other targets we’ve generated. They have different combinations of risk controls which interpolate between all of the other targets we’ve released in the past, and will be useful for ensembling.

# New Example Model

The Rain example model has several upgrades vs the Sunshine example model, resulting in better performance and more ease of use.

The Sunshine example model used only the medium Sunshine features.

[The Rain example model](<https://github.com/numerai/example-scripts/blob/master/example_model.ipynb>) uses the Rain features, of course, and thanks to the improved memory efficiency of the dataset, it is able to use all features instead of only the medium set.

The [Sunshine](<http://forum.numer.ai/t/super-massive-data-sunshine/5977>) example model was built using an ensemble of several targets: Ralph20, Nomi20, Jerome60, Waldo20, Tyler20, Victor20.

Since then, several more targets have been released, including a new primary scoring target: Cyrus.

While ensembling many models built on different targets certainly tends to help performance, the simplicity of a model trained only on Cyrus was prioritized for this newest example model.

The result of the new features, the reduced size of the data, and the new target, together result in a vast performance improvement over the previous example model.

[![|863.0000000000001x603](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/34c2abc693be56c81ed186a0dcec8aa883a03772_2_690x482.png)|863.0000000000001x6031600×1118 102 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/34c2abc693be56c81ed186a0dcec8aa883a03772.png> "|863.0000000000001x603")

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/42272855a704c6d2596fe7d5c8f0f3f71261a092.png)464×108 6.25 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/42272855a704c6d2596fe7d5c8f0f3f71261a092.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8536bf2f18efa13091f6b690c788288831ce3f4d.png)464×110 5.83 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8536bf2f18efa13091f6b690c788288831ce3f4d.png>)

You can track the new example model’s performance here: [numer.ai/lg_lgbm_v42_cyrus20](<https://numer.ai/lg_lgbm_v42_cyrus20>)

# Feature Groups

There have been several new feature groups added.

In addition to the familiar “small” and “medium” feature sets, which have been updated for the Rain dataset, you will also find a new collection of feature sets:

Intelligence, Charisma, Strength, Dexterity, Constitution, Wisdom, Agility, and Serenity.

These feature sets are groupings of features which tend to behave similarly.

These groupings existed in the old V2 dataset, and we saw users have success training several models leaving out one feature group at a time, which can create an ensemble of models that is more resilient in the case of any one of the feature groups performing poorly.

There are also “Sunshine” and “Rain” feature sets, which represent the features which were introduced in each of the latest data releases.

The Rain feature set is a unique one because some aspects of the features are learned over the training data. This feature group is available so you can be careful modeling these features which Numerai developed using information before era 575.

# int8

The Rain dataset no longer has a normal variation and an int8 variation. There is only int8 – int8 is the new normal.

This means that all of the features have integer values from 0-4. This allows the dataset to take up far less space than the previous default float32 representation from 0.0 to 1.0.

The total dataset size is ~3x smaller because of this, making the total size of the training data 5.3GBs. The default Sunshine training file was 16GBs and even the int8 variation was 7.5GBs, despite it having less features than Rain.

Further, there are no NaNs in this dataset, as there were in the Sunshine int8 files. Instead, features which would have been all NaN for an era are instead all set to the median value (2).

Including NaNs was an idea to allow us to add features which didn’t exist in the data until the later eras. This way, users could see that feature_x didn’t exist until era 400, and could choose to leave them as NaN and let their model handle them, or fill them with a median value, or do some more clever imputation. This is all positive because it tells users more truth, and lets them make their own decisions about how to deal with the reality of missing values.

However, including NaNs results in several complexities. For example, it forces the features to be represented using the pandas Int8 type instead of the more familiar numpy int8 typing. In addition to making the dataset nearly twice as large in memory, it also required some extra code so that standard machine learning libraries could process the data.

This new int8 format allows the best trade offs of all of the options.  
The data size is minimal.  
There is no extra processing required to allow standard ML libraries to use the data.  
There is no information lost because users can still detect missing features by finding features for each era where all of the values are 2, and then they can process them further if desired.

# V2 and V3 Deprecation

It is time to say goodbye to the oldest datasets. On October 9th we will discontinue the V2 and V3 datasets.

There are two primary reasons why we’re doing this.

The first is Numerai’s engineering bandwidth. These older datasets use two data pipelines which are separate from the pipeline that V4, Sunshine, and Rain share. Internally, we are slowed down considerably by maintaining the infrastructure required to continue supporting these legacy pipelines.

The second reason is performance. The more recent datasets have an enormous performance edge over V2 and V3 and we really want users to switch to using them. We know there are some great models built on V2 and V3 datasets, but those models could be even better if they are built on Rain.

We also know of significant issues with the V2 and V3 datasets. For example: [Removing Dangerous Features](<http://forum.numer.ai/t/removing-dangerous-features/5627>)

The Rain features.json file does contain groups which contain “v2_equivalent_features” and “v3_equivalent_features”, so if you really prefer those datasets then you can still build models on close analogs using a subset of the Rain dataset (minus the faulty features which we removed, of course).

Here we have some standard 20,000 tree models built on each dataset. Ultimately, the more recent datasets have such stronger performance, that it’s difficult to justify the effort of maintaining the older datasets anymore.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/71ccae7f718b927335c3738fadf141057a6fabf9_2_690x487.jpeg)1600×1132 120 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/71ccae7f718b927335c3738fadf141057a6fabf9.jpeg>)

# V4 and Sunshine Data Fixes

In developing Rain, we noticed an inconsistency in the previous datasets, affecting Sunshine more than others. In short, features were generated with slightly different methods for training, validation, and live. Though most features show no difference between the methods, for a few features the methods can have correlation as low as 0.75. At risk of stating the obvious, models don’t perform as well when the features have different meanings during prediction time than they do during training time.

We know many users like to continue submitting models from previous datasets, so we’ve corrected this difference in historical data. Now all features across training, validation and live are generated using the same method as training data was. This should result in better performance for nearly all models. If your model was trained using validation data as well, then it would benefit further from retraining on the updated validation data.

Here’s an example of a Sunshine model on the old Sunshine dataset (with different methods across time) vs one trained and predicted on the new Sunshine dataset (with the same method across time). Correlation increases from 0.0229 to 0.0236.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/0301b1c51988b984016388d05b49cd2c30e9b068_2_595x421.png)1600×1131 96.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0301b1c51988b984016388d05b49cd2c30e9b068.png>)

## Additional Model Slots

There are now 100 model slots available, up from 75, giving you room to begin experimenting with the Rain dataset immediately.

## Model Uploads

Going forward, Model Uploads will only support the Rain dataset.  
Existing models in Model Uploads will continue working.

You can get started training a model with Rain data here: [example-scripts/example_model.ipynb at master · numerai/example-scripts · GitHub](<https://github.com/numerai/example-scripts/blob/master/example_model.ipynb>)  
You can download the data from the website or from the API here: [Numerai](<https://numer.ai/data>)  
We hope you find the new features, feature groups and targets useful for training your Numerai models.

See you on the leaderboard.

---

### Post #2 — **ssh** | 2023-09-08 07:16 UTC

Greate work on building a new dataset! We all appreciate this.  
Let me grunt here about deprecating v2/v3 data set. 1 month of deprecating notice is too short.  
We needed to rebuild models yesterday (at round 566) to be able to see live results on the rain dataset to compare with v2/v3.  
**[@richai](</u/richai>) please consider extending v2/v3 till the end of this year 2023**, for a smoother transition period. At the cost of current “engineering bandwidth” you will be able to see differences on live data between v2/v3/v4 models - to be able to compare your backtest.

The idea that latest eras make such a big improvement in models is kind of troubling that it’s some kind of current regime and all kinds of long term momentums and this could be not an improvement but vice-versa overfit to current regime.

---

### Post #4 — **sneaky** | 2023-09-08 18:02 UTC

![:fire:](http://forum.numer.ai/images/emoji/twitter/fire.png?v=12) ![:fire:](http://forum.numer.ai/images/emoji/twitter/fire.png?v=12) Rain is fire! ![:fire:](http://forum.numer.ai/images/emoji/twitter/fire.png?v=12) ![:fire:](http://forum.numer.ai/images/emoji/twitter/fire.png?v=12)

---

### Post #5 — **neliz** | 2023-09-09 08:26 UTC

Maybe a silly question, but in v4.2 is the cyrus target still called : “target_cyrus_v4_20” ?

---

### Post #6 — **ia_ai** | 2023-09-09 10:11 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png) master_key:

> For this reason, data scientists might want to treat them differently. For example, any cross-validation done within the training data alone is likely to favor some of the Rain features much more than experiments done on the validation set would, because the Rain features are built to be good specifically at training data.
> 
> Note though that there were many controls put in place to prevent overfitting these features on the training data; not a single rain feature uses any forward looking data after era 575, meaning the out of sample period after era 575 is still truly out of sample.

[@master_key](</u/master_key>) does it mean the 666 `Rain` features from eras 1 to 574 have more predictive power in the training set because they **do** contain forward-looking data?

---

### Post #7 — **qeintelligence** | 2023-09-10 20:06 UTC

[@master_key](</u/master_key>) : As far as i can tell the 666 features are not described anywhere, or part of the features.json file (just like small/medium).Is there any documentation with a list of the features or better an updated features file describing them? Great release btw.

---

### Post #8 — **qeintelligence** | 2023-09-11 19:18 UTC _(reply to #7)_

I did some more checking myself and found out there is actually a rain and sunshine mentioned, the medium features though is not the same as before, it now also includes more features, something to keep in mind for backward compatibility.

---

### Post #9 — **pumplerod** | 2023-09-12 19:01 UTC

among the newly supplied feature groups (‘strength’, ‘constitution’, etc…) there appear to be overlaps between some of the groups and ‘constitution’. Is this intended?
    
    
    feature_stellular_paler_centralisation in charisma
    feature_stellular_paler_centralisation in constitution
    feature_sanctioned_sunny_lily in charisma
    feature_sanctioned_sunny_lily in constitution
    feature_elasmobranch_braving_typhoid in charisma
    feature_elasmobranch_braving_typhoid in constitution
    feature_wariest_vulnerable_unmorality in charisma
    feature_wariest_vulnerable_unmorality in constitution
    feature_vapourish_ichthyotic_causerie in charisma
    feature_vapourish_ichthyotic_causerie in constitution
    feature_unimpressed_uninflected_theophylline in strength
    feature_unimpressed_uninflected_theophylline in constitution
    feature_aaronic_unexampled_arguer in strength
    feature_aaronic_unexampled_arguer in constitution
    feature_dendritic_phytographic_skydiving in strength
    feature_dendritic_phytographic_skydiving in constitution
    feature_cynic_unreckonable_feoffment in strength
    feature_cynic_unreckonable_feoffment in constitution
    feature_grizzled_reformist_soberer in strength
    feature_grizzled_reformist_soberer in constitution

---

### Post #10 — **ark** | 2023-10-05 19:49 UTC _(reply to #2)_

We announced the deprecation of older datasets with the Sunshine release. It has been 9 months not 1.

---

### Post #11 — **master_key** | 2023-10-05 20:02 UTC _(reply to #10)_

V3 removal was announced then, V2 removal is a newer announcement to be fair

---

### Post #12 — **jeremy_berros** | 2023-10-06 12:27 UTC _(reply to #11)_

Fairwell old friend #saveV2data
