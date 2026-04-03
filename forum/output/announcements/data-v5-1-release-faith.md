---
title: "Data V5.1 Release - Faith"
category: Announcements
url: https://forum.numer.ai/t/data-v5-1-release-faith/8200
created_at: 2025-10-31T22:16:47.602000+00:00
last_posted_at: 2025-11-07T20:53:15.331000+00:00
posts_count: 7
views: 2072
tags: []
---

# Data V5.1 Release - Faith

---

### Post #1 — **master_key** | 2025-10-31 22:16 UTC

[![Faith Photo large](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/797fed772d38b5883d75d0c5b0c34b6c85e8e42c_2_500x500.jpeg)Faith Photo large1920×1920 435 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/797fed772d38b5883d75d0c5b0c34b6c85e8e42c.jpeg> "Faith Photo large")

Today we are releasing the biggest upgrade to Numerai data in over a year. It’s called Faith.

Dataset V5.1 introduces 186 new features, including some of the highest performing and unique features we’ve ever released.

A standard example model using the parameters found here: [Models | Numerai Docs](<https://docs.numer.ai/numerai-tournament/models#deep-lgbm-params>), built using this new V5.1 dataset, does better than an identical model built on the V5 dataset in nearly every period.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/808f1052efb1dc8b8490df35987c00148fff974c_2_589x423.jpeg)image1600×1151 67.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/808f1052efb1dc8b8490df35987c00148fff974c.jpeg> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/81113a02e6e06f55bcdc76f7c52b161a9113e2e7_2_639x458.jpeg)image1600×1146 90.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/81113a02e6e06f55bcdc76f7c52b161a9113e2e7.jpeg> "image")

You can download it and begin experimenting here: [numer.ai/data](<http://numer.ai/data>)

There are two things that make these new features particularly interesting:

  1. They are sparse in the early eras.



[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e529f95a0d6814914e7e1f248a10ac8139fd2db7_2_686x500.png)image1600×1165 48.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e529f95a0d6814914e7e1f248a10ac8139fd2db7.png> "image")

  2. They are extremely predictive and unique. Several of the faith features are by far the most predictive, information dense features we’ve ever released.



[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c7a8d68c35ed2a895f45837c9689626c113430b5_2_684x500.jpeg)image1600×1167 342 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c7a8d68c35ed2a895f45837c9689626c113430b5.jpeg> "image")

These two facts have interesting consequences for modeling.

Since many of them are missing in earlier eras, it means that most models will not use them heavily, even though doing so would increase performance in later eras.

Some candidate ways to handle this:

  * Remove the first two hundred eras from training to increase the concentration of samples which have the features present.

  * Impute the early missing data in some clever way that maintains the expected correlation vs target and correlation vs other features.

  * Ensemble the best but sparsest features with your models’ final predictions in order to upweight those features and compensate for their early sparsity




Here is a quick demo where we

  * Take the 5 best faith features from the medium set

  * Equal weight those feature values into one super feature

  * Gaussianize that super feature

  * Blend it with the V5.1 predictions with 80% weight v5.1, 20% weight Faith super feature




[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/78c06bb9297bf1ac7e9a9b8d69486fff92cd8ac4_2_688x500.jpeg)image1600×1163 84.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/78c06bb9297bf1ac7e9a9b8d69486fff92cd8ac4.jpeg> "image")

Godspeed and happy modeling

---

### Post #2 — **gb96** | 2025-11-05 01:55 UTC

The new data files are more than double the size:

v5.1 validation.parquet is 7.3 GB today versus 3.3 GB for v5.0

This will impact models that are memory-constrained (or GPU memory-constrained) during training. If a model trained on all features of v5.0 is getting close to a memory limit when training it is likely to run out of memory if attempting to train on v5.1 unless a subset of features is selected or the number of eras in the training data is reduced.

When new data is added to validation.parquet each week, the only way for participants to fetch the new data is to re-download the entire 7.3 GB file.

Has anyone considered that if the data format was CSV instead of parquet, an HTTP GET feature could allow the client to just download the new rows, saving a lot of time and network bandwidth at the numerai server.

---

### Post #3 — **bernardobraga** | 2025-11-05 15:24 UTC _(reply to #2)_

CSV files would be extremely large and difficult to download or maintain. However, it might be useful to include an option to download Parquet files for specific eras instead.

Regarding GPU OOM issues, you can train on a subset of features and/or eras, or consider upgrading to a GPU with more VRAM. If you’re using TensorFlow or PyTorch, you can also train using data generators and mini-batches to ensure the data fits within your available VRAM.

---

### Post #4 — **shatteredx** | 2025-11-06 07:09 UTC

The v5.1 validation parquet file is not 7.3 GB. It is 3.8 GB. It said 7.3 GB because it was overwriting your old validation.parquet and adding the two file sizes together. This is a known quirk with downloading new versions of parquet files with Python

---

### Post #5 — **liborty** | 2025-11-07 06:57 UTC

What is the new total number of features?  
And targets?

---

### Post #6 — **svendaj** | 2025-11-07 20:42 UTC

Dear Kagglers, V5.1 data are now available on Kaggle platform with weekly automatic update:

  * [numerai data](<https://www.kaggle.com/code/svendaj/numerai-data>) is public notebook, automatically triggered on Saturday round opening, downloading data from [v5.1 Data - Numerai](<https://numer.ai/data/v5.1>), and also producing 4 smaller subsampled datasets with non-overlapping data.
  * [numerai latest tournament data](<https://www.kaggle.com/datasets/svendaj/numerai-data-v5-1-faith>) is public dataset with output data of producing notebook [numerai data](<https://www.kaggle.com/code/svendaj/numerai-data>). Dataset is updated automatically, when producing notebook is successfully executed.



You can use whichever data source as the input of your notebooks to produce Tournament submissions. Using the new dataset, I have retrained and uploaded all public Kaggle example models:

  * [Hello Numerai automated](<https://www.kaggle.com/code/svendaj/hello-numerai-automated>) \- basic tutorial model with improved version trained on medium feature set
  * [numerai Feature Neutralization](<https://www.kaggle.com/code/svendaj/numerai-feature-neutralization>) \- Kaggle tutorial explaining FN
  * [numerai Target Ensemble](<https://www.kaggle.com/code/svendaj/numerai-target-ensemble>) \- Kaggle tutorial explaining ensembling
  * [Numerai Example Model Sunshine](<https://www.kaggle.com/code/svendaj/numerai-example-model-sunshine>) \- example model using both techniques above



Although I have left notebooks unchanged, they all show slight improvement in diagnostics.

This is diagnostics of model trained on train.parquet with medium feature set of V5.0 data:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/14186e0793f14e73c92782f1ddc189ebdb5eb51b_2_664x500.png)image678×510 35.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/14186e0793f14e73c92782f1ddc189ebdb5eb51b.png> "image")

and this same model on new V5.1 data:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c335889aa2d5e1171907937acd4dd0297dd3b3c1_2_667x500.png)image676×506 35.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c335889aa2d5e1171907937acd4dd0297dd3b3c1.png> "image")

---

### Post #7 — **svendaj** | 2025-11-07 20:53 UTC _(reply to #6)_

… and for those still using V5.0 data, I will be updating them weekly as well until their end-of-life. They can be found here:

  * [numerai data v5.0 Universe](<https://www.kaggle.com/code/svendaj/numerai-data-v5-0-universe>) \- producing public notebook
  * [numerai data V5.0 Universe](<https://www.kaggle.com/datasets/svendaj/numerai-latest-tournament-data>) \- public Kaggle dataset
