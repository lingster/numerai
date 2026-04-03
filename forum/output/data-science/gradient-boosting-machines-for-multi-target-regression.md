---
title: "Gradient Boosting Machines for multi-target regression"
category: Data Science
url: https://forum.numer.ai/t/gradient-boosting-machines-for-multi-target-regression/4417
created_at: 2021-10-28T11:45:46.961000+00:00
last_posted_at: 2021-10-30T11:22:13.664000+00:00
posts_count: 6
views: 9103
tags: []
---

# Gradient Boosting Machines for multi-target regression

---

### Post #1 — **perfect_fit** | 2021-10-28 11:45 UTC

Hi guys!

Just wanted to share some insights on training Gradient Boosting Machines (GBMs) for multi-target regression to prepare for the new dataset. It also would be cool to get a discussion going on this and hear your insights.

[XGBoost](<https://xgboost.readthedocs.io/en/latest/python/python_api.html#module-xgboost.sklearn>) does not seem to support multi-target regression out of the box. This can be fixed by using [sklearn’s MultiOutputRegressor](<https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html>). However, it will fit one regressor per target, so interactions between targets will not be learned.

As far as I understand, [LightGBM](<https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMRegressor.html>) and sklearn’s [GradientBoostingRegressor](<https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor.fit>) also do not support multi-target regression out of the box.

**Example of using MultiOutputRegressor for XGBoost:**
    
    
    from xgboost import XGBRegressor
    from sklearn.multioutput import MultiOutputRegressor
    
    estimator = XGBRegressor(objective='reg:squarederror')
    model = MultiOutputRegressor(estimator=estimator).fit(X_train, y_train)
    

In contrast, [CatBoost](<https://catboost.ai/en/docs/concepts/python-reference_catboostregressor>) provides support for multi-target regression. Just make sure you set `loss_function` and `eval_metric` to `'MultiRMSE'`.

**Example for CatBoost:**
    
    
    from catboost import Pool, CatBoostRegressor
    dtrain = Pool(X_train, label=y_train)
    dvalid = Pool(X_val, label=y_val)
    
    params = {'learning_rate': 0.1, 'depth': 6, 
              'loss_function': 'MultiRMSE',  'eval_metric': 'MultiRMSE'}
    
    model = CatBoostRegressor(**params)
    model.fit(dtrain, eval_set=dvalid, use_best_model=True)
    

Another thing to look out for is that you might want to evaluate performance on each target separately. For this I loop over all targets, calculate spearmanr and aggregate:

**Evaluation example:**
    
    
    import numpy as np
    from scipy.stats import spearmanr
    
    y_pred_valid = model.predict(X_val).clip(0, 1)
    y_pred_train = model.predict(X_train).clip(0, 1)
    train_spearmans = []
    val_spearmans = []
    targets = [col for col in df.columns if col.startswith("target")]
    for i, target in enumerate(targets):
        tr_spearman = spearmanr(y_train[:, i], y_pred_train[:, i]).correlation
        val_spearman = spearmanr(y_val[:, i], y_pred_valid[:, i]).correlation
        train_spearmans.append(tr_spearman)
        val_spearmans.append(val_spearman)
        print(f"Spearman correlation for {target}:")
        print(f"Train: {tr_spearman.round(4)}")
        print(f"Valid: {val_spearman.round(4)}")
    mean_train_spearman = np.mean(train_spearmans)
    mean_val_spearman = np.mean(val_spearmans)
    print("Average Spearman over all targets:")
    print(f"Train: {mean_train_spearman.round(4)}")
    print(f"Valid: {mean_val_spearman.round(4)}")
    

Hope this helps! Very curious to hear how you are tackling the multi-output regression problem using GBMs.

---

### Post #2 — **eleven_sigma** | 2021-10-28 19:41 UTC

Interesting. Do you found any documentation of how apply CatBoost the boosting with multitarget?  
I didn’t found nothing about the approach used.

---

### Post #3 — **perfect_fit** | 2021-10-28 20:02 UTC _(reply to #2)_

Good question. The CatBoost documentation can be really vague.

I found this short note on how MultiRMSE is calculated:  
<https://catboost.ai/en/docs/concepts/loss-functions-multiregression#MultiRMSE>

[@hedgingcat](</u/hedgingcat>) has an awesome implementation example. This was one of the few code examples I found for using MultiRMSE with CatBoost:  
<https://www.kaggle.com/gogo827jz/multiregression-catboost-1-model-for-206-targets>

---

### Post #4 — **hedgingcat** | 2021-10-28 20:17 UTC _(reply to #3)_

This notebook is old. I have found the latest version of Catboost even supports multilogloss with custom metric. However, GPU is stil not supported.

---

### Post #5 — **eleven_sigma** | 2021-10-28 21:04 UTC _(reply to #4)_

In documentation refers to ‘error metric’ when talk about multiRMSE, not ‘objective’ that is usually the name of internal function used for compute gradient / hessian for boosting.  
Do you think this is a true multiresponse and not a wrapper to something like MultiOutputRegressor in sklearn?  
I’m looking the code and don’t find the part of gradient computation for multiRMSE.

---

### Post #6 — **perfect_fit** | 2021-10-30 11:22 UTC _(reply to #5)_

Hmm, the documentation seems to imply that ‘loss_function’ is an alias of ‘objective’, so MultiRMSE should be an objective. However, I also can’t find any information about the internal function to compute gradient / Hessian. The documentation uses loss function and metric synonymously sometimes, which makes it even more confusing. ![:confused:](//forum.numer.ai/images/emoji/twitter/confused.png?v=9)

Docs including ‘loss_function’ definition:  
<https://catboost.ai/en/docs/references/training-parameters/common>
