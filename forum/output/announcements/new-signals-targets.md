---
title: "New Signals Targets"
category: Announcements
url: https://forum.numer.ai/t/new-signals-targets/5853
created_at: 2022-11-16T22:45:22.839000+00:00
last_posted_at: 2022-11-16T22:45:22.958000+00:00
posts_count: 1
views: 1553
tags: []
---

# New Signals Targets

---

### Post #1 — **master_key** | 2022-11-16 22:45 UTC

There are now four new scores on the Signals website and three new targets in the historical_targets file.

On [Numerai Signals](<https://signals.numer.ai>), data scientists submit quantitative signals across Numerai’s ~5000 global equity stock universe. To help data scientists train models which produce more valuable signals, Numerai has released three new targets.

**target_20d_raw_return**

It can be difficult for even an experienced data scientist to build a subsequent return column correctly if they are calculating it themselves from publicly available data. This is due to complications with returns such as stock splits and dividends. This target handles all of those complications, and then bins the returns into Numerai’s standard distribution.  
With this target we are also replacing the existing IC score with ICv2, which is the simple rank correlation between your prediction and this new target.

**target_20d_factor_neutral**

This is a target which has been neutralized to a selection of standard factors: country, sector, beta, momentum, and size.

This target will be used to calculate a new score called Residual Information Coefficient, RIC.  
Since Numerai’s hedge funds are neutral to these factors, RIC is much closer to what Numerai actually wants from signals than IC.

**target_20d_factor_feat_neutral**

This is similar to the existing target_20d in that it is neutral to a large set of factors and features, but it is additionally neutral to many new features from the v3 and v4 Numerai datasets.

This target is used to compute two new scores: CORRv4, and FNCv4.

CORRv4 and FNCv4 on Signals work similarly to how CORR and FNC work on Numerai.

CORRv4 is your submission’s rank correlation with target_20d_factor_feat_neutral (without any pre-neutralization).

In FNCv4 we neutralize your submission to all of the factors and features that the target is neutral to, before scoring the submission against target_20D_factor_feat_neutral.

FNCv4 can be considered the next iteration of the existing Signals CORR score, and we plan to change scoring and payouts to FNCv4 early in 2023. ‘CORR’ for Signals was always a bad name because it has always actually been a feature neutral correlation. In early 2023, we’ll remove the current CORR.

Until then, payouts on staked NMR will continue to be based on the existing CORR metric.

**Score comparison**  
Below is a matrix showing how correlated all of the scores are with one another. This data is collected from rounds 279 to 331, for users who staked more than 1 NMR.

You will notice that many of the scores are dissimilar from one another, while being decently correlated with TC.

This implies that models which are good on all of these measures might have especially high TC.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/de7482af2662dac2ec92c9f4d59c88d9acd65987_2_690x263.png)1206×462 125 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/de7482af2662dac2ec92c9f4d59c88d9acd65987.png>)

Diagnostics on Signals will be improved to include these new targets in the coming months. Numerai suggests training new signals to have strong correlation with target_20d_factor_neutral and target_20d_factor_feat_neutral because both are correlated with TC.

The existing [example scripts](<https://github.com/numerai/signals-example-scripts>) use target_20d only. We’d be happy to review a PR by anyone who wants to work on an advanced example model which incorporates the new targets as well.
