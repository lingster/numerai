---
title: "ShatteredX's Improved & Compact Feature Set (225 features) for v4.3 Midnight Data"
category: Data Science
url: https://forum.numer.ai/t/shatteredxs-improved-compact-feature-set-225-features-for-v4-3-midnight-data/6982
created_at: 2024-01-22T20:25:36.566000+00:00
last_posted_at: 2024-03-07T21:23:08.861000+00:00
posts_count: 14
views: 3383
tags: []
---

# ShatteredX's Improved & Compact Feature Set (225 features) for v4.3 Midnight Data

---

### Post #1 — **shatteredx** | 2024-01-22 20:25 UTC

I have made my own feature set that is a subset of the v4.3 feature set. Here is the link:

[github.com/shatteredx/numerai](<https://github.com/shatteredx/numerai/blob/main/v4.3FeatureLists.py>)

#### [v4.3FeatureLists.py](<https://github.com/shatteredx/numerai/blob/main/v4.3FeatureLists.py>)

[`main`](<https://github.com/shatteredx/numerai/blob/main/v4.3FeatureLists.py>)
    
    
    shatFeatsv43 = ['feature_grave_prevenient_rheotrope',
     'feature_flagging_gadarene_barrymore',
     'feature_heretofore_drowsiest_conjugation',
     'feature_thorniest_laughable_hindustani',
     'feature_bumpier_maidenlike_chordata',
     'feature_canicular_overlong_avocado',
     'feature_third_discreet_solute',
     'feature_skim_expugnable_subception',
     'feature_carolean_tearable_smoothie',
     'feature_intercostal_imbricated_hypothenuse',
     'feature_overeager_pugilistic_diocletian',
     'feature_statesmanlike_tailed_herat',
     'feature_unfertilized_scaldic_partition',
     'feature_galvanizing_whirring_baroscope',
     'feature_veddoid_sport_psychobiology',
     'feature_conveyed_divisional_argemone',
     'feature_undisguised_unenviable_stamen',
     'feature_shrinelike_unreplaceable_nitrogenization',
     'feature_shakier_peskier_transfuser',
     'feature_bantam_matterful_hut',
    

This file has been truncated. [show original](<https://github.com/shatteredx/numerai/blob/main/v4.3FeatureLists.py>)

The goal of this experiment was to create a feature set with the fewest features while also maximizing CORR and MMC. I wanted to create a feature set smaller than the Numerai medium set contained in features.json but also better. The most practical application of this feature set is it allows users to train models using less RAM, which is a common roadblock for new users.

The methods I used to select the features were pretty simple:

  1. Built-in feature importances of lightgbm/xgboost.
  2. SHAP feature importances.
  3. Brute-force evaluation vs. the validation set.



(I will say at the start here: yes, this feature set is “overfit” to the validation set. I did not train on validation but I did evaluate against validation many times. Does this feature set still have value? That is for you to decide.)

Overall, I am pleased with the results. Here are the cumulative CORR20v2 results using the “example model” trained on eras 1-561 (downsampled to every 4th era) on target_cyrus_v4_20:

`model = LGBMRegressor(n_estimators=2000, max_depth=5, learning_rate=0.01, colsample_bytree=0.1, num_leaves=2**5+1)`

(I just noticed num_leaves should be `2**5-1` instead of `2**5+1` to match the example model, a minor difference).

Evaluated vs ALL validation eras 575-1092:  


[![download](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0e1e4c632b02e587728504ac3d22bab7008a9e02.png)download565×455 36.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0e1e4c632b02e587728504ac3d22bab7008a9e02.png> "download")

Suprisingly, my compact feature set of 225 features gets higher CORR than the full v4.3 feature set! In fact, all the metrics are better, including sharpe and even feature exposure (barely).

Here are the diagnostics of each feature set:

My feature set (225)  


[![diag_shat](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/aca7b355bed6f1be1c8eededd019f0593ea966ad.png)diag_shat742×500 35.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/aca7b355bed6f1be1c8eededd019f0593ea966ad.png> "diag_shat")

All v4.3 features (2,376)  


[![diag_all](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7d561c82b7f1111a314cbfde1ed188cb0b9fa213.png)diag_all735×501 31.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7d561c82b7f1111a314cbfde1ed188cb0b9fa213.png> "diag_all")

Medium v4.3 features (705)  


[![diag_medium](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4d21489fc0a350b58dcbeb02e26ec54057bffb0d.png)diag_medium734×501 32.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4d21489fc0a350b58dcbeb02e26ec54057bffb0d.png> "diag_medium")

Small v4.3 features (42)  


[![diag_small](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0773f0f04a05e2ae71bdfad63183daf44d758704.png)diag_small735×508 34.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0773f0f04a05e2ae71bdfad63183daf44d758704.png> "diag_small")

Will these features continue to beat the full feature set? Who knows, only time will tell. If you forced me to choose to stake on one, I would probably still choose the full feature set, but it will interesting to see how they perform going forward. Good luck!

---

### Post #2 — **master_key** | 2024-01-22 21:12 UTC

It might be interesting to see how many of each feature_set ShatteredX chose to include.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/70ad45b901e9a788d9cd200a49df7214804dc36a_2_450x500.png)image916×1016 45.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/70ad45b901e9a788d9cd200a49df7214804dc36a.png> "image")

Some observations

  1. It’s a pretty diverse/balanced set which is healthy
  2. It agrees nicely with our small feature set which we made quite awhile ago now (before sunshine/rain/midnight), and was our attempt to make a super super compact dataset
  3. There’s a skew towards more recent releases like midnight and rain, which makes sense because we tried to make those more compact ourselves
  4. Poor charisma and strength ![:frowning:](https://emoji.discourse-cdn.com/twitter/frowning.png?v=13)

---

### Post #3 — **master_key** | 2024-01-22 21:20 UTC

Perhaps an obvious extension for the ambitious/compute-rich/perfectionists who aim to avoid the validation overfitting problem ShatteredX mentions.

  * Turn this into a system which always picks the best 225 or so features given any data provided.
  * Walk-forward every 50 or so eras, re-evaluate your favorite 225 features (up to era X, let’s say)
  * Train on that data up era X, and predict on eras from X+5 (for embargo) to X+50.
  * Now you have an entire dataset of valid out-of-sample predictions
  * Check if those predictions are better than just training on all features in the same walk-forward approach!
  * Try not to iterate on this more than a couple of times or else you’re back in overfitting territory

---

### Post #4 — **halsmith99** | 2024-01-23 11:23 UTC

but you can avoid over-fitting by using a different model in the feature engineering step and for validation/prediction?

---

### Post #5 — **shatteredx** | 2024-01-23 16:00 UTC _(reply to #4)_

[@halsmith99](</u/halsmith99>) Yeah I thought the same. I did use two different models, not the lightgbm one, to perform the brute-force feature evaluation.

[@master_key](</u/master_key>) That is really cool to see the proportion it shares with the other feature groups!

I also forgot to mention that my original inspiration for this experiment was [@mdo](</u/mdo>) 's BorutaShap thread where he created the small feature set. [Feature Selection with BorutaShap](<http://forum.numer.ai/t/feature-selection-with-borutashap/4145>) So I have been thinking about this idea for two years now apparently ![:joy:](http://forum.numer.ai/images/emoji/twitter/joy.png?v=12) ![:older_man:](http://forum.numer.ai/images/emoji/twitter/older_man.png?v=12)

---

### Post #6 — **master_key** | 2024-01-23 16:27 UTC _(reply to #4)_

Why would using two different models avoid over-fitting?

If you give any model only the features that work for the majority of the validation period then it’s going to look great on validation guaranteed

---

### Post #7 — **shatteredx** | 2024-01-24 01:12 UTC _(reply to #6)_

Yeah still massively overfit to the validation set. I guess the idea would be that at least it might not be overfit to specific hyperparameters or tree library.

---

### Post #8 — **halsmith99** | 2024-01-24 09:57 UTC _(reply to #6)_

the idea i had was if i apply the feature set to a different model that comes up with a significantly different feature exposure distribution

then it is learning different patterns from the data set and may be less overfit than using the feature engineering model out of sample

ran it on the 20 day targets using a cat, lgb & xgb model hypertuned on an older dataset/target (v3/4 & nomi) and there is improvement across the board.

but i haven’t checked the feature exposures.

---

### Post #9 — **gammarat** | 2024-01-27 14:51 UTC

I’ve been experimenting with the v4.3 data set and it seems that the last 100 or so new features added with Midnight don’t amount to much, at least when run on the validation data with a genetic algorithm using a soft limit of around 300 features used in any given model.

This is a sample plot of the feature utility function through 4K iterations (a complete evaluation takes around 20-30K):  


[![v04.3binResponse](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d650a0f4be115c483a78511401771d220ca43d39_2_442x500.jpeg)v04.3binResponse580×655 52.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d650a0f4be115c483a78511401771d220ca43d39.jpeg> "v04.3binResponse")

  
the lower plot is done with a 51 element centered moving median over the data in the upper plot.

Do the new features have a lot of NaNs (or 2s) in the final columns which would cause that sort of problem? I don’t know yet.

---

### Post #10 — **danzell** | 2024-02-01 15:33 UTC

I used some of my feature selection ideas and adjusted the subset slightly (removed 29 + added 50 Features) and trained a lightgbm model (using the above params):

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dd45c8fe4ab6588a4ca355c458ffce41ddd75c26.png)image740×504 34.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dd45c8fe4ab6588a4ca355c458ffce41ddd75c26.png> "image")

If you are interested in the ideas behind it - you should attend the Numerai Meetup in Frankfurt ![:upside_down_face:](https://emoji.discourse-cdn.com/twitter/upside_down_face.png?v=13). I will be giving a talk there on how I do feature selection to train my Neural Nets ![:v:](https://emoji.discourse-cdn.com/twitter/v.png?v=13).

---

### Post #11 — **jxtrbtk** | 2024-02-03 12:45 UTC

Thank you for sharing this subset [@shatteredx](</u/shatteredx>). I will use it !  
I plan to refresh some of my very old models (and some more fun).

---

### Post #12 — **jxtrbtk** | 2024-02-13 08:30 UTC

Another trick maybe if you have not much RAM is to use CatBoost. It seems it handles int8 where other are converting to float32. I’m not 100% sure but it’s mentionned here and there (for example, in this article: [Machine Learning Tricks to Optimize CatBoost Performance Up to 4x](<https://www.intel.com/content/www/us/en/developer/articles/technical/optimize-catboost-performance-by-up-to-4x.html>))

---

### Post #13 — **halsmith99** | 2024-02-29 14:27 UTC _(reply to #1)_

early days but initial live results look encouraging.

lazer_02 using all features, lazer_u0013/14 using the reduced shatteredx feature set.

all are xgb ensembles on the same parameters using upto a dozen 20d targets.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/888ccc7a43cd4d703e8754a0c2edf16d3aff33e7_2_690x345.png)image1407×705 44.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/888ccc7a43cd4d703e8754a0c2edf16d3aff33e7.png> "image")

---

### Post #15 — **slashv** | 2024-03-07 21:23 UTC

The fact that you can outperform a model with 2300+ features with a model that uses only a subset of 225 of those features can mean two things imho:

  * most features contain no or redundant information
  * the model has real trouble extracting the information contained in the full feature set.



[@shatteredx](</u/shatteredx>). what’s your opinion on this?
