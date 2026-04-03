---
title: "[ACTIVE] Bounty for using and feedback on NumerBlox"
category: Council of Elders
url: https://forum.numer.ai/t/active-bounty-for-using-and-feedback-on-numerblox/6786
created_at: 2023-11-10T19:31:40.028000+00:00
last_posted_at: 2023-11-15T18:07:27.682000+00:00
posts_count: 6
views: 835
tags: []
---

# [ACTIVE] Bounty for using and feedback on NumerBlox

---

### Post #1 — **bor1** | 2023-11-10 19:31 UTC

Hi all,

Our first bounty is here. The makers of [NumerBlox ](<https://github.com/crowdcent/numerblox/tree/rewrite/numerbloxv1#3-quick-start>), [@perfect_fit](</u/perfect_fit>) and [@jrai](</u/jrai>), are interested in feedback from users.

Numerblox is a library to simplify software engineering around Numerai inference pipelines. Its older sibling is being used by the [CrowdCent ](<https://crowdcent.com/>) models, and [@perfect_fit](</u/perfect_fit>) and [@jrai](</u/jrai>) are interested in feedback on this new version.

**What is NumerBlox 1.0?**

NumerBlox 1.0 focuses on:

  1. End-to-end pipelines and full scikit-learn compatibility.
  2. Simplification of the package structure, with fewer mandatory dependencies.
  3. Leveraging new v4.2 data fully.



For more details on the library’s features and improvements, see the [preview post](<http://forum.numer.ai/t/preview-numerblox-1-0/6696>).

**Installation Instructions:**

The library is compatible with Python 3.9+. You install numerbloc v1 with:  
`pip install -U numerblox`

**How to Participate in the Bounty:**

  1. Use the library
  2. Provide constructive feedback on your experience, including any bugs or improvement suggestions in this bounty thread for a 1 NMR bounty (bounties are low, but their purpose is to give starting numerati outside of the crypto-sphere an opportunity to add some NMR to their accounts and get into the _stake in the game_ mode).
  3. Bonus NMR for pull requests and bug fixes on github.
  4. If the system is not being gamed, and you want to get paid, add your discord link or an address capable of receiving NMR, and [@bor1](</u/bor1>) will sporadically go through the posts and organize the payouts.



Thanks for participating in community-made tools!  
[@bor1](</u/bor1>).

---

### Post #2 — **perfect_fit** | 2023-11-11 00:27 UTC

Thanks for organizing this [@bor1](</u/bor1>)! Really appreciate it! Excited to improve the library with this feedback.

For more context check this forum post:

![](http://forum.numer.ai/user_avatar/forum.numer.ai/perfect_fit/48/2527_2.png) [Preview: NumerBlox 1.0](<http://forum.numer.ai/t/preview-numerblox-1-0/6696>) [Data Science](</c/data-science/5>)

> About 1.5 years ago [@jrai](</u/jrai>) and I created an open source library called [NumerBlox](<https://github.com/crowdcent/numerblox/tree/master>) to simplify the software engineering around Numerai inference pipelines. After hearing your feedback and using it internally for all [CrowdCent](<https://crowdcent.com/>) models we had many insights and integrated everything we have learned into NumerBlox 1.0. We invite you to try out this [preview version](<https://github.com/crowdcent/numerblox/tree/rewrite/numerbloxv1>) and give feedback before we merge it. Quickstart (v4.2. data): [GitHub - crowdcent/numerblox at rewrite/numerbloxv1](<https://github.com/crowdcent/numerblox/tree/rewrite/numerbloxv1#3-quick-start>) Overview of NumerBlox fu… 

UPDATE: NumerBlox v1 has been merged and uploaded to PyPi.

From now on you can install the new NumerBlox version with

`pip install -U numerblox`

---

### Post #3 — **perfect_fit** | 2023-11-11 00:39 UTC _(reply to #2)_

One recent fun thing we included in NumerBlox v1 is the ability to add benchmark models to your evaluation. If you include benchmark model columns in the evaluator it will return Corrv2 and Sharpe outperformance of your predictions vs. benchmark models and correlation of your predictions with benchmarks.

Here is a simple example for usage:
    
    
    from numerblox.evaluation import NumeraiClassicEvaluator
    
    # fast_mode will skip calculation of FNC, because this can take a while.
    evaluator = NumeraiClassicEvaluator(fast_mode=True)
    
    # Your validation data with columns prediction, era, target
    # example_preds, meta_model_prediction and rain_ensemblev2 cols.
    val_df = ... 
    
    # meta_model_col and benchmark_cols are optional
    metrics = evaluator.full_evaluation(val_df, 
                                        example_col="example_preds", 
                                        pred_cols=["prediction"], 
                                        meta_model_col="meta_model_prediction",
                                        target_col="target",
                                        benchmark_cols="rain_ensemblev2")
    # Pandas DataFrame with metrics
    metrics
    

[Quick overview of core metrics.](<https://github.com/crowdcent/numerblox/blob/5e6b001749161d7e1e3aacd62ce43f8c06154014/numerblox/evaluation.py#L20>)

---

### Post #4 — **halsmith99** | 2023-11-15 12:00 UTC _(reply to #1)_

mentioned was calculating local MMC & EPC. is that something that will be in the Numerblox pipeline?

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a15561c626a62829f695d93a6c9967db20025a93_2_690x116.png)image1247×211 29.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a15561c626a62829f695d93a6c9967db20025a93.png> "image")

---

### Post #5 — **bor1** | 2023-11-15 17:46 UTC _(reply to #4)_

From the developers - yes, that will come.

---

### Post #6 — **perfect_fit** | 2023-11-15 18:07 UTC _(reply to #4)_

Good one! `NumeraiClassicEvaluator` will now give legacy EPC and MMC metrics with `.full_evaluation`. Legacy MMC will only be calculated if you define a `meta_model_col` and have meta model predictions in your validation DataFrame.

N**OTE: Numerai hasn’t released the full details on these metrics yet so we use the[“MMC2”](<http://forum.numer.ai/t/mmc2-announcement/93>) calculation and deliberately call it “legacy”.**

This quickstart notebook explains evaluation in step 3. Note that you also need to add meta model predictions and specify `meta_model_col`.

[github.com](<https://github.com/crowdcent/numerblox/blob/master/examples/quickstart.ipynb>)

#### [crowdcent/numerblox/blob/master/examples/quickstart.ipynb](<https://github.com/crowdcent/numerblox/blob/master/examples/quickstart.ipynb>)
    
    
    {
     "cells": [
      {
       "cell_type": "markdown",
       "metadata": {},
       "source": [
        "# 0. Dependencies"
       ]
      },
      {
       "cell_type": "code",
       "execution_count": 1,
       "metadata": {},
       "outputs": [],
       "source": [
        "import pandas as pd\n",
        "from xgboost import XGBRegressor\n",
        "\n",
        "from numerblox.misc import Key\n",
        "from numerblox.numerframe import create_numerframe\n",
    

This file has been truncated. [show original](<https://github.com/crowdcent/numerblox/blob/master/examples/quickstart.ipynb>)
