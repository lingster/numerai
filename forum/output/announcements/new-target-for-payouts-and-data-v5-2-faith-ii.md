---
title: "New Target for Payouts and Data V5.2 - Faith II"
category: Announcements
url: https://forum.numer.ai/t/new-target-for-payouts-and-data-v5-2-faith-ii/8209
created_at: 2025-12-15T20:17:21.215000+00:00
last_posted_at: 2025-12-22T10:59:45.991000+00:00
posts_count: 4
views: 1548
tags: []
---

# New Target for Payouts and Data V5.2 - Faith II

---

### Post #1 — **master_key** | 2025-12-15 20:17 UTC

[![Faith II](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/45ab3cad17c3197d8331e06cbfde478b4d158b25_2_500x500.jpeg)Faith II1920×1920 757 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/45ab3cad17c3197d8331e06cbfde478b4d158b25.jpeg> "Faith II")

Today we are announcing a new dataset which is ready immediately, as well as a scoring change for 2026.

### New Dataset

The second Faith dataset contains 186 new features. Some are completely new types of features. Many are similar to the [original Faith features](<https://forum.numer.ai/t/data-v5-1-release-faith/8200/2>). Those were our most powerful features ever released, and we have found it helpful to include more variations of those.

Faith II also contains two new targets: Ender, and Jasper, both 20D and 60D variants. These are similar to Teager targets, which you will already be familiar with. You will find that models trained on these targets exhibit more consistency than models trained on other targets.

Of course there are new benchmark models for these as well, for example `v52_lgbm_ender20`.

### New Target for Payouts and Leaderboard

Starting with the round starting January 1, 2026, predictions will be scored based on their correlation with the new Ender20 target. This applies to both CORR and MMC.

This is our first payout target change since we introduced Cyrus in April 2023, and we don’t make the change lightly. We spent many months developing a target which encourages users to make models that are maximally valuable to our business, and Ender is the result of that work.

These are the last changes we have in the queue at the moment.

So spin up your Blackwells and build your best models for the 2026 season.

Happy Modeling

---

### Post #2 — **bernardobraga** | 2025-12-16 14:41 UTC

My Blackwell started to spin  


[![Screenshot 2025-12-16 at 14.40.25](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/868cd0be210ae835e63fb16f5d404f35c3ca790f_2_690x108.png)Screenshot 2025-12-16 at 14.40.251134×178 19.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/868cd0be210ae835e63fb16f5d404f35c3ca790f.png> "Screenshot 2025-12-16 at 14.40.25")

---

### Post #3 — **svendaj** | 2025-12-19 19:14 UTC

Dear Kagglers, V5.2 data are now available on Kaggle platform with weekly automatic update:

  * [numerai data](<https://www.kaggle.com/code/svendaj/numerai-data>) is public notebook, automatically triggered on Saturday round opening, downloading data from [v5.2 Data - Numerai](<https://numer.ai/data/v5.2>), and also producing 4 smaller subsampled datasets with non-overlapping data.
  * [numerai latest tournament data](<https://www.kaggle.com/datasets/svendaj/numerai-data-v5-2-faith-ii>) is public dataset with output data of producing notebook [numerai data](<https://www.kaggle.com/code/svendaj/numerai-data>). Dataset is updated automatically, when producing notebook is successfully executed.



You can use whichever data source as the input of your notebooks to produce Tournament submissions. Using the new dataset and new target `target_ender_20`, I have retrained and uploaded all public Kaggle example models:

  * [Hello Numerai automated](<https://www.kaggle.com/code/svendaj/hello-numerai-automated>) \- basic tutorial model with improved version trained on medium feature set
  * [numerai Feature Neutralization](<https://www.kaggle.com/code/svendaj/numerai-feature-neutralization>) \- Kaggle tutorial explaining FN
  * [numerai Target Ensemble](<https://www.kaggle.com/code/svendaj/numerai-target-ensemble>) \- Kaggle tutorial explaining ensembling
  * [Numerai Example Model Sunshine](<https://www.kaggle.com/code/svendaj/numerai-example-model-sunshine>) \- example model using both techniques above



Diagnostic data are not suggesting any improvement over v5.1, but hey it’s just backtesting. Let’s see how they will fare next year.

This is diagnostics of model trained on train.parquet with medium feature set and new target of **V5.2** data:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/02a4bbde30f6268ed92fc2bde434d161d2d4ec81_2_641x500.png)image670×522 33.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/02a4bbde30f6268ed92fc2bde434d161d2d4ec81.png> "image")

and this same model on V5.1 data:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c335889aa2d5e1171907937acd4dd0297dd3b3c1_2_667x500.png)image676×506 35.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c335889aa2d5e1171907937acd4dd0297dd3b3c1.png> "image")

---

### Post #4 — **icoup** | 2025-12-22 10:59 UTC

Looks like target_ender und target_jasper have 2 x NaN each in train - valid looks Ok to me - maybe you wanna double check
