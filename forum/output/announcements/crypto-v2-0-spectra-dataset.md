---
title: "Crypto V2.0 'Spectra' Dataset"
category: Announcements
url: https://forum.numer.ai/t/crypto-v2-0-spectra-dataset/8197
created_at: 2025-10-08T16:43:07.830000+00:00
last_posted_at: 2025-10-08T16:43:07.880000+00:00
posts_count: 1
views: 997
tags: []
---

# Crypto V2.0 "Spectra" Dataset

---

### Post #1 — **ark** | 2025-10-08 16:43 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/dc6f0baa828a49c201c9a09a71e562815c631958_2_627x352.jpeg)image2048×1152 703 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dc6f0baa828a49c201c9a09a71e562815c631958.jpeg> "image")

The Numerai Crypto V2.0 “Spectra” Dataset is here!

This update includes a number of improvements to the overall quality of the Numerai Crypto data including: an improved universe, new features and targets, and a more standardized dataset. Let’s dive in.

**The Universe**

The universe is now _just 300 tokens_ \- this is because we wanted to improve the shortability of the universe. For a recent date, we checked Hyperliquid against our new universe and observed an increase of short coverage from under 20% (v1) to over 35% (v2). We did this by improving the universe filtering logic to include coins that are more likely to be shortable in crypto marketplaces.

The universe is now also easier to parse because we are including a “ucid” column - this is the unified crypto ID based on [CoinMarketCap’s UCID system](<https://support.coinmarketcap.com/hc/en-us/articles/20092704479515-Unified-Cryptoasset-ID-UCID>). This will make it easier on data scientists to craft more reliable models and ensure they are predicting the correct universe.

**New Features and Targets**

We’ve added 22 new features to the dataset so new users have an easier way to start modeling. These features include 20D and 60D variants of common TA features such as RSI, momentum, volatility, bollinger bands, and different averages of common coin data like market cap, volume, and close price. These features are then ranked and binned in a similar way to the other tournaments, keeping overall data structure standard across the tournaments.

We’ve also updated the targets to include both 20d and 60d variants of a ranked & binned return target. This provides more ways to make models that could improve a users long-term performance on a 20D target.

**Standard UX**

Finally, we’ve changed the file structure and names to more closely match our other tournaments. The files we offer are now `train.parquet`, `live.parquet`, and `live_example_preds.parquet` to keep them consistent with the other tournaments and we’ve added an example model notebook that you can find [in our example scripts repository](<https://github.com/numerai/example-scripts/blob/master/crypto/example_model.ipynb>).

We don’t currently have meta_model files for v2.0 yet, but we will be starting to produce those before the cutoff date below.

**Important Dates**

For rounds starting on or after November 12th, the Meta Model and payouts will be switched to V2.0 and V1.0 data will be deleted.
