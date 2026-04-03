---
title: "Validation Metrics Backtest"
category: Data Science
url: https://forum.numer.ai/t/validation-metrics-backtest/3003
created_at: 2021-04-21T21:47:06.767000+00:00
last_posted_at: 2021-04-21T21:47:06.903000+00:00
posts_count: 1
views: 947
tags: []
---

# Validation Metrics Backtest

---

### Post #1 — **jimmy_woodford** | 2021-04-21 21:47 UTC

A few months ago, I wondered whether I should use era-wise correlation (spearman) between predictions and targets or its sharpe ratio as my primary metric for early stopping, model comparison, etc. So I ran the following experiment: I split the data three times into trainset, validationset, and testset(s) as follows. 

trainset | validationset | testset(s)  
---|---|---  
eras 1-37 | eras 49-72 | eras 73-96, eras 97-120, and eras 121-132 & 197-213  
eras 1-60 | eras 73-96 | eras 97-120 and eras 121-132 & 197-213  
eras 1-84 | eras 97-120 | eras 121-132 & 197-213  
  
For each split I trained 100 lightgbm models with random hyperparameters (on an already somewhat optimised space) and used era-wise correlation on validation as early stopping criterion. I used each model to predict the testset(s). I then calculated the correlation of both era-wise correlation as well as sharpe on the validation set with the return (the product of 1+era-wise-corr) on the testset(s). Note that return is all I care about on the live set.

**The average correlation between era-wise correlation on the validation set and return on the testset(s) was`.71`, while for sharpe it was only `.35`.** (For validation FNC, the correlation was `.53`, but only since era-wise correlation and FNC are quite correlated.) For each of the six validation-test combinations, era-wise correlation was the best predictor of return. For all six combinations, I also ran simple linear regressions of test-return on val-era-wise-correlation, val-sharpe, and val-FNC and found that sharpe and FNC add no predictive power compared to solely using era-wise-correlation.

In a nutshell, it seems like in the past correlation on the validationset was a much better predictor of future return than sharpe (at least for lightgbm models). In fact, in my experiment sharpe did not add any information when already using correlation, which surprised me. That’s what led me to use correlation as basically my only metric when comparing models.

My experiment was partly inspired by [@nasdaqjockey](</u/nasdaqjockey>)’s [post](<http://forum.numer.ai/t/does-good-model-diagnostics-correlate-with-tournament-performance/1454>), so check that out too if you’re interested in these kind of things.
