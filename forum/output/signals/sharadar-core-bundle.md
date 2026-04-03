---
title: "Sharadar Core Bundle"
category: Signals
url: https://forum.numer.ai/t/sharadar-core-bundle/4856
created_at: 2022-01-27T15:36:45.332000+00:00
last_posted_at: 2022-01-27T15:36:45.525000+00:00
posts_count: 1
views: 936
tags: []
---

# Sharadar Core Bundle

---

### Post #1 — **stacktrace** | 2022-01-27 15:36 UTC

I recently subscribed to the Sharadar Core Bundle on Quandl/Nasdaq. The (apparent) value is very good; there is a ton a data for reasonable cost. Does anyone use this data?

I am just doing some basic exploration of this data and I think they are doing the dividend adjustment incorrectly in the pricing data. For example, when looking at a split,

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/7c1641058c06112b901e8d67f196101192530834_2_517x262.png)image1064×541 76.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7c1641058c06112b901e8d67f196101192530834.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/554d9997cb63f1534c7ec9a44d00d28043dd2b89_2_517x267.png)image1058×546 63.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/554d9997cb63f1534c7ec9a44d00d28043dd2b89.png> "image")

…you can see that the “close” column **is adjusted**.

However, when we look at a dividend (ABT went ex-dividend on 2022-01-13), it is backwards:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a11385d7926f375b64814df99683472a7001d5d9_2_517x280.png)image1051×570 56 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a11385d7926f375b64814df99683472a7001d5d9.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/1f6809f05001f779ea08dfc4107b8c186a5871e0_2_517x282.png)image1057×576 47.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1f6809f05001f779ea08dfc4107b8c186a5871e0.png> "image")

Here we see that the “close” column is **not** adjusted.

Am I misunderstanding this? I’ve emailed Sharadar to ask.

EDIT:

Looking into this further, I see this convention is the same as Yahoo Finance (yfinance). The footnote on Yahoo Finance:

> *Close price adjusted for splits. **Adjusted close price adjusted for splits and dividend and/or capital gain distributions.om Yahoo Finance

This is a really bad convention IMHO and very confusing. I am sure it is creating issues with many Signals models. I suppose that open, high, and low are consistent with “close”.
