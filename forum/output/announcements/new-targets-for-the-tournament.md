---
title: "New Targets for the Tournament"
category: Announcements
url: https://forum.numer.ai/t/new-targets-for-the-tournament/5842
created_at: 2022-11-12T05:12:32.138000+00:00
last_posted_at: 2022-11-12T05:12:32.231000+00:00
posts_count: 1
views: 2657
tags: []
---

# New Targets for the Tournament

---

### Post #1 — **master_key** | 2022-11-12 05:12 UTC

On November 12, we will release four new targets, with each target having both the 20-day and 60-day horizons, for a total of eight new columns in the train, validation, and live v4 data files described [here](<https://numer.ai/data/v4>).

Numerai scores submissions from data scientists against target_nomi. The Nomi target represents a transformation of the underlying stock returns with certain risks taken out eg. market beta. You can think of the targets as a residual return.

There are many different ways to compute residual returns and therefore many ways to create targets. For example, one target might be neutral to all market factors (country, sector, value, momentum, etc). Another target might be neutral to just some of them.

At Numerai we believe there is no “best model” which is why we ensemble thousands of models. For the same reason, we don’t believe there is one “best target” which is why Numerai releases multiple targets. Each target is a different way to train a model to learn how to earn returns under different risk constraints.

# The 4 New Targets

  * The four new targets are named target_ralph, target_tyler, target_victor, and target_waldo.
  * Target_ralph is an improvement to Nomi in our internal backtests. Specifically, target_ralph purges certain uncompensated dimensions of risk and packs more portfolio-implementable returns into the target. For these reasons, we believe it will also help TC. Another interesting fact about target_ralph is that models trained on this target tend to have higher capacity, which is important as our AUM grows.
  * Models trained on target_tyler, target_victor, and target_waldo are all diversifying in different ways, and they ensemble well with models trained on target_nomi.
  * Target_tyler helps regulate how portfolios achieve neutrality with respect to various types of risk. In today’s volatile market environment, this is especially important. Our research indicates that an equal-weighted ensemble of models trained on Nomi and target_tyler tends to improve both portfolio return and Sharpe ratio.
  * Target_victor takes the idea of stock-specific return, and applies it to a much bigger set of risk variables. We believe models trained on this target would be less correlated with common predictors that people use, and thus potentially reducing crowding risk.
  * Target_waldo is in the same vein as target_tyler. While it is a bit less restrictive than target_tyler on certain risk dimensions, models trained on it also ensemble well with models trained on Nomi.



These four new targets will be in this Saturday morning’s data.

# New Target Highlights

The new targets are reasonably different from Nomi, as shown in the correlation table below.

Correlation among Targets

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/da8826c0250232fdb832a9606ad28c6592504cbc_2_620x236.png)998×380 24.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/da8826c0250232fdb832a9606ad28c6592504cbc.png>)

Predictions from the models trained on these new targets can predict Nomi, and in some cases even beat the Nomi target, during the 433-era validation period.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b20ef78c24740d55a49855c39d860e2f5cce301d_2_690x86.png)1296×162 10.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b20ef78c24740d55a49855c39d860e2f5cce301d.png>)

The figure below shows that a model trained on target_ralph tends to outperform a model trained on target_nomi over 433 eras on the validation data.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5e58a6fc2f384eaf6d7355c0451c28a112c9773f_2_482x370.png)928×712 74 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5e58a6fc2f384eaf6d7355c0451c28a112c9773f.png>)

# Possible Avenues of Research

New targets can help data scientists in all kinds of ways. But here are some ideas for how to begin researching them.

  * Train a model with the same architecture or parameters as your best Nomi model on all the new targets. Can you find a set of weights for all four models which outperforms your current best Numerai model?
  * [Feature selection](<http://forum.numer.ai/t/feature-selection-with-borutashap/4145>) can be important on Numerai especially as the number of features has increased over time. Via cross-validation can you show whether or not there are good subsets of features which work for some targets but not for others? Or is it a good idea to only use a subset of features which works on all targets?
  * Numerai gives out standard parameters for a LightGBM in our example script. We grid searched these parameters for target_nomi a long time ago. Is the set of LightGBM we use in the example script for Nomi not optimal for target_ralph, target_tyler, target_victor, and target_waldo? What works better for those targets?



We would be happy to review any of your initial results on the target in this forum thread. We have little doubt that the Numerai community will quickly discover interesting results we’ve missed while developing these for the last few months.

If the community can find easy improvements to the example script using these new targets, we always like updating it to give new Numerai users a head start. We’d be happy to review your pull request which updates that [script](<https://github.com/numerai/example-scripts/blob/master/example_model.py>).
