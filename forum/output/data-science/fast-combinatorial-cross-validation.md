---
title: "Fast Combinatorial Cross Validation"
category: Data Science
url: https://forum.numer.ai/t/fast-combinatorial-cross-validation/3350
created_at: 2021-05-19T22:01:34.820000+00:00
last_posted_at: 2021-05-28T16:43:50.977000+00:00
posts_count: 6
views: 4204
tags: []
---

# Fast Combinatorial Cross Validation

---

### Post #1 — **jackerparker** | 2021-05-19 22:01 UTC

Hi everyone,

Combinatorial purged cross fold validation (CPCV) is a concept proposed by Marcos Lopez de Prado in the “Advances in financial machine learning” book and it was discussed here on the forum ([Cross-validation done right](<http://forum.numer.ai/t/cross-validation-done-right/2979>)). My post can be useful only for those who are already familiar with the CPCV concept.

In a normal K-fold CV, you estimate AUC/RMSE/ or other metrics using a small test set from every fold and it’s ok for data sets where you can split data randomly. But in finance, you usually split data grouping by date periods and you cannot expect similar metrics values on the different date periods. Thus, the common solution is to combine all your test sets with predicted targets from every fold and calculate only 1 metric such as returns (COR in case of Numerai) for combined test sets. Using CPCV you combine test sets in multiple paths and get multiple values of COR/Sharpe/… metrics.

Here I present an idea on how to obtain ~75% reduction in time required for random hyperparameters search combined with CPCV. My assumption here is that COR values from different paths in CPCV should follow the normal distribution. And here is an example of average COR values for 1-132 eras obtained using 11paths/12Groups/66splits (N=12, k=2) CPCV I’ve performed on the Numerai dataset: [0.05233829, 0.05250924, 0.05166095, 0.05273881, 0.05253379, 0.05207856, 0.05245192, 0.05234268, 0.05219343, 0.05202705, 0.05215169]. My goal is to find the best hyperparameters in terms of maximal average (by paths) COR. On the first step, I calculate COR values using all 66 splits of train data for 11 paths. But on the next step when I check the next random hyperparameters, I train models only for the first 11 splits to obtain COR value for the first path. If this COR value is less than threshold, I just skip calculations for these hyperparameters. If not - just do the same for the second path (+10 next splits) and so on. Threshold is defined as average (by paths) COR - 3 standard deviation of COR for best hyperparameters at the current iteration. For my example above, the threshold is 0.05143 = 0.05227 - 3 * 0.00028. Indeed, if the COR values for different paths follow the normal distribution, one can estimate probability that at least one of 11 COR values from another “better” hyperparameters (by mean COR) has lower value than defined threshold using the formula: 1 - (1 - 0.0013)**11 = 1.4%. 0.0013 here is the probability that a random sample from normal distribution has value less than “mean - 3 std”, which can be obtained from the Z score table. Thus, only 1.4% of really useful hyperparameters will be skipped by chance in this approach.

In the ideal case when your first hyperparameters will be the best, for checking of 110 random hyperparams you have to calculate only 66 + 109 * 11 splits = 1265 (of 7260 splits required for normal CPCV). In the real case, I’ve calculated only 2079 splits for 110 hyperparams which means 72% reduction in time.

Regards,  
Mark

---

### Post #2 — **jackerparker** | 2021-05-20 21:26 UTC

An example Python code is available here: [Github](<https://github.com/markmipt/fast_combinatorial_cv>)

---

### Post #3 — **nyuton** | 2021-05-21 06:16 UTC

Good idea! CPCV is good bug very time consuming!

---

### Post #4 — **gbrecht** | 2021-05-24 08:27 UTC

[@jackerparker](</u/jackerparker>) was kind enough to accept a PR linking CPCV with optuna for a supposed imrovement of the parameter sampling over random search.

[github.com](<https://github.com/markmipt/fast_combinatorial_cv/blob/main/cpcv.py>)

#### [markmipt/fast_combinatorial_cv/blob/main/cpcv.py](<https://github.com/markmipt/fast_combinatorial_cv/blob/main/cpcv.py>)
    
    
    from itertools import combinations
    import pandas as pd
    import lightgbm as lgb
    import csv
    import numpy as np
    from ast import literal_eval
    import random
    from collections import Counter, defaultdict
    import os
    import ast
    import matplotlib.pyplot as plt
    from util.data import read_training_data
    from loguru import logger
    import optuna
    
    NUMBER_OF_GROUPS = 6
    path_to_numerai_training_data = ''
    TARGET_NAME = "target"
    PREDICTION_NAME = "prediction"
    

This file has been truncated. [show original](<https://github.com/markmipt/fast_combinatorial_cv/blob/main/cpcv.py>)

---

### Post #5 — **sneaky** | 2021-05-28 13:28 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jackerparker/48/1580_2.png) jackerparker:

> N=12, k=2

Nice job! Noob question: how did you come up with the N and k parameters? Was it by an experiment, a heuristic, random, or educated guess?

---

### Post #6 — **jackerparker** | 2021-05-28 16:43 UTC _(reply to #5)_

Hi sneaky! Short answer : random.

I don’t know about benefits which k > 2 can provide me. As for the N, I have two models with N = 6 (as in the original book example) and N = 12 (just for more accurate post-analysis). In my opinion, there is a huge difference between having 1 path metric (“standard” kfold CV) and multi-path metric (CPCV), but the difference between 5 and 11 paths is not that important.

I’ve already attached this figure in the chat: the validation performance for my models generated using N=6 and N=12 are pretty the same (CV was slightly better for 11 path model, validation was the opposite).  


[![VAL2_for_CPCV](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/ff8779990c79dfe9821563cc6b9c13d0cae08831_2_690x371.png)VAL2_for_CPCV966×520 76.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/ff8779990c79dfe9821563cc6b9c13d0cae08831.png> "VAL2_for_CPCV")

For the next experimental workflow I’m using N=6 k=2 CPCV and with the algorithm described here in the post it is close in computational time to the standard 5-fold CV.

Regards,  
Mark
