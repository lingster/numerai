---
title: "Model Diagnostics Update"
category: Announcements
url: https://forum.numer.ai/t/model-diagnostics-update/902
created_at: 2020-09-03T19:46:11.808000+00:00
last_posted_at: 2020-09-03T19:46:11.885000+00:00
posts_count: 1
views: 11741
tags: []
---

# Model Diagnostics Update

---

### Post #1 — **master_key** | 2020-09-03 19:46 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/abfec3344ca67c7e6b56e400a615d77dc1117dba_2_188x375.png)image538×1070 48 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/abfec3344ca67c7e6b56e400a615d77dc1117dba.png> "image")

Starting with the coming round, you will receive additional information about your model when you submit.

These metrics will better inform users about the strengths and weaknesses of their models, and give users more direction and insight into the nuances of this unique problem.

The metrics are split into 3 categories.  
Performance - Overall measures of performance over the validation set.  
Risk - Different ways to assess how likely it is that your model has severe burns in the future  
MMC - Different estimates of how your model would perform from an MMC perspective on validation, using Example Predictions as an estimate for the metamodel.

When choosing metrics, we looked for metrics which add one or more of several benefits:

  * Convenience for staking decisions
  * Correlation to overall model performance (mean and/or sharpe)
  * Highlighting the most interesting, unique parts of the Numerai problem.



You will notice that each of the metrics are a different color from red to black(neutral) to green. These grades are based on both research about how the metrics seem to predict future performance, as well as consideration for the general distribution of submissions.

You will also find that in the latest [example_models.py](<https://drive.google.com/file/d/18VC_sE0aMUpG_C1ScmBADkAH82R7xWql/view?usp=sharing>) (this link is a snapshot of the file as of round 230) which comes in the zip file when you download the round data, we have added the code for calculating all of these metrics. This will allow you to iterate on your model more easily mid-week, as well as explore these metrics in the training part of the data.

For specific information about the features, you can read these community-written posts. We are looking forward to seeing the conversation on these posts and would love it if others shared their additional research contributions.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/jackerparker/48/1580_2.png)

[Model Diagnostics: MMC](<http://forum.numer.ai/t/model-diagnostics-mmc/898>) [Data Science](</c/data-science/5>)

> Introduction There are two main metrics which everyone would like to maximize: average payout and payout sharpe. Since the last MMC update we have an opportunity to choose between pure CORR payout and CORR+MMC payout. An optimal payout scheme and variance between training, validation and live metrics are main topics of this post. Methods All training data were predicted using 2-fold CV with dividing data into two ranges of 1-60 and 61-120 eras. Validation data were generated using model fitte… 

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/jrb/48/2767_2.png)

[Model Diagnostics: Feature Exposure](<http://forum.numer.ai/t/model-diagnostics-feature-exposure/899>) [Data Science](</c/data-science/5>)

> This post is about feature exposure. I’ll try explain the intuition behind feature exposure, and why it matters. I’ll also discuss ways to reduce feature exposure (regularization and feature neutralization). Feature Exposure The idea behind feature exposure is as follows: Any supervised ML model from a very high level perspective, is a function that takes an input feature vector (X) and outputs a prediction (y). At training time, the model learns a mapping between input features and the predict… 

![](https://avatars.discourse-cdn.com/v4/letter/d/5f8ce5/48.png)

[Model Diagnostics: Risk Metrics](<http://forum.numer.ai/t/model-diagnostics-risk-metrics/900>) [Data Science](</c/data-science/5>)

> Metrics which can be used to assess the model risk: Sharpe Ratio Max Drawdown Sharpe Ratio Sharpe Ratio describes the returns distribution. It is a ratio of mean returns divided by its standard deviation. The preferred distribution is with high mean and narrow distribution (and small tails). Such distribution will result in a high Sharpe Ratio (the higher Sharpe the better). For me, when I’m looking for new models, I’m considering as good, all models with Sharpe Ratio > 1.0 on validation dat…
