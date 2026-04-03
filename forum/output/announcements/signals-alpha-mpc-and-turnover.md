---
title: "Signals Alpha, MPC, and Turnover"
category: Announcements
url: https://forum.numer.ai/t/signals-alpha-mpc-and-turnover/8162
created_at: 2025-07-31T17:21:12.293000+00:00
last_posted_at: 2025-07-31T17:21:12.352000+00:00
posts_count: 1
views: 803
tags: []
---

# Signals Alpha, MPC, and Turnover

---

### Post #1 — **ark** | 2025-07-31 17:21 UTC

We just announced the Signals updates [over on our blog](<https://blog.numer.ai/signals-alpha-and-mpc/>) and I’m here to add a bit more color to the why and how of Alpha, MPC, turnover, etc. I recommend reading the blog post first to get a basic idea of what we are talking about before continuing with this post.

List of Updates:

  * The new Signals v2.1 Dataset includes a few new files: 
    * train_neutralizer.parquet
    * train_sample_weights.parquet
    * validation_neutralizer.parquet
    * validation_sample_weights.parquet
  * The Signals tournament has 3 new metrics: 
    * 60D Alpha: The dot product of the 60D chili target with your predictions after they’ve been neutralized and sample-weighted.
    * 60D Meta-Portfolio Contribution: Your model’s contribution to the 60D Alpha of the Stake-Weighted Portfolio (using the Alpha gradient with respect to stakes).
    * Turnover: After your signals are neutralized and sample-weighted, turnover is the maximum week-over-week change in weights.
  * Rounds starting on or after September 2nd will have their payouts switched to Alpha and MPC and will use the new 25% turnover threshold. The multipliers will be 0.3xAlpha + 0.8xMPC.
  * Numerai Tools 0.4.2 introduces new functions to calculate neutralized weights (given a signal, neutralization matrix, and sample weights weights vector), alpha, meta portfolio contribution, and turnover.



# New Scores and Data

This release adds 2 new scores: Alpha and Meta Portfolio Contribution (MPC):  


[![Screenshot 2025-07-30 at 14.32.11](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3fba956ac1f9f06fd000da1c3ac1908234a71f8d_2_690x389.png)Screenshot 2025-07-30 at 14.32.113062×1730 506 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3fba956ac1f9f06fd000da1c3ac1908234a71f8d.png> "Screenshot 2025-07-30 at 14.32.11")

The new datasets `neutralizer` and `sample_weights` are meant to help you train models that can generate a raw signal that performs well in Alpha / MPC space. As of now, we have decided not to provide you with live files for this data - this is for a reason similar to live targets in that we feel more comfortable with the obfuscation when there is a significant lag between live and the release of the neutralizers and sample weights.

To utilize these new pieces of data and calculate scores locally, you can leverage the `alpha` and `meta_portfolio_contribution` functions from numerai-tools. We also updated the [Signals Tutorial Notebook](<https://colab.research.google.com/github/numerai/signals-example-scripts/blob/master/example_model.ipynb>) to show you how to calculate the alpha score over the validation data.

# Turnover Threshold

Similar to the [churn threshold](<https://forum.numer.ai/t/signals-churn-threshold/7648>), the turnover threshold will compare the neutralized weights of your current submission to the neutralized weights of the last 5 submissions. This maximum weight change must be below 25%. If it is above 25%, you will be prevented from staking for the round.

To calculate turnover between two signals:

  1. ensure both signals have the same tickers
  2. `tie_kept_rank__gaussianize__pow_1_5` each signal
  3. `generate_neutralized_weights` on each normalized signal from 2
  4. `center` then `weight_normalize` the neutral weights from 4
  5. finally, give both to the `turnover` function



Use functions from numerai-tools to accomplish the above.

# Payouts

Alpha and MPC are 60-Day scores, which means a few things:

  * Rounds will officially resolve 12 weeks later instead of 4 weeks.
  * Staking on 60D rounds will lock up your stake for 12 weeks instead of 4.
  * There will be an 8-week gap between the last 20D payment and the first 60D payment



Rounds starting on or after September 2nd, 2025 will have their payouts switched to 60D Alpha and MPC. The multipliers for these scores will be **0.3xAlpha + 0.8xMPC**.

Based on relative magnitudes of Alpha & MPC vs. FNCv4 & MMC, we believe these multipliers will keep average payouts and burns similar to what they are now for top performers.

# FAQ

**Do I need to retrain my models?**  
Yes, probably.

**Why are you changing scores and payouts???**  
Because the Signals Meta Model is not currently additive to the Numerai Meta Model and our internal models. We need it to be strongly additive to the Numerai Meta Model.

**Why do we need the neutralizers and sample_weights?**  
To optimize for Alpha and MPC, your predictions must be aware that they will be neutralized and sample-weighted during scoring.

**I just got used to churn, why are you changing it to turnover?**  
Churn works in signal space, but after neutralizing and weighting your signal, it is no longer in signal space, so churn doesn’t quite make sense as a metric. Instead, we need to measure the absolute distance between 2 sets of weights - this is turnover.
