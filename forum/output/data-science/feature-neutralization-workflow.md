---
title: "Feature neutralization workflow"
category: Data Science
url: https://forum.numer.ai/t/feature-neutralization-workflow/1059
created_at: 2020-10-12T18:15:48.628000+00:00
last_posted_at: 2021-02-24T16:27:45.842000+00:00
posts_count: 7
views: 5579
tags: []
---

# Feature neutralization workflow

---

### Post #1 — **jackerparker** | 2020-10-12 18:15 UTC

Hi everyone! I’m going to leave Numerai tournament and would like to share my workflow which is focused on feature neutralization topic.

The workflow:

  1. Find optimal hyperparameters using 5-fold shuffled by-eras CV and Random Search (~100 trials). Metric for maximization was mean CORR after full feature neutralization of predicted values (full means all features and 1.0 coefficient for neutralization). LightGBM was used for boosting.
  2. Find all features which increase mean CORR when they are “not used” for prediction. It was done by shuffling features one-by-one in an era-wise way and applied for prediction using normally trained model.
  3. Generate a short list of features and train a new model. This is jackerparker3 account predictions.
  4. Neutralize predictions for this model using a short list of features except one for all these features one-by-one. Calculate difference in sharpe and mean CORR for every feature.
  5. Take the short list of features and remove all features which decrease sharpe when used in neutralization. Neutralize basic predictions on this list and it will be jackerparker2.
  6. Take the short list of features and remove all features which decrease mean CORR when used in neutralization. Neutralize basic predictions on this list and it will be jackerparker6.



I don’t really want to share the code for this workflow because it is too messy and contains a lot of bugs. For example, a list of features used in jackerparker6 for neutralization contains features which were not used for prediction. But despite all the bugs, the results for both validation and live-performance are quite interesting and it seems that the general idea is worth investigating. Here is a link to [github](<https://github.com/markmipt/numerai_models>) with all features lists, pickled model and iPython notebook which are ready to generate predictions from jackerparker2 (#12 position right now) and jackerparker6 (#33) accounts.

Hope someone will find it useful,  
Regards,  
Mark

---

### Post #2 — **olivepossum** | 2020-10-12 21:54 UTC

Hi Mark,  
Thanks a lot for sharing.

I have a doubt about your workflow. In step 3, you mean train a new model removing the features you found in step 2?

And… why are you leaving the tournament? ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

Thanks in advance.

---

### Post #3 — **jackerparker** | 2020-10-13 09:39 UTC _(reply to #2)_

Steps 2-3 represent permutation importance procedure which is discussed in Lopez de Prado book. I agree that it is highly arguable method, especially when features are in strong correlation with each other.

I’m leaving the tournament due to risks related to a new government regulation of cryptocurrencies (just a new law in my country) which I’m not ready to take. So, there is nothing wrong with the tournament itself ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #5 — **olivepossum** | 2020-10-18 20:41 UTC _(reply to #3)_

Thanks Mark!

I have another doubt. In step 2, to find the features that improve CORR when not present, you predict against train or validation data? My guess is that to discard features by predicting against validation would lead to overfitting but you hit outstanding results.

Thanks!

---

### Post #6 — **jackerparker** | 2020-10-19 10:10 UTC _(reply to #5)_

Hi!

I agree that using validation would lead to overfitting. But I’m using training data for that. See the part of code:
    
    
    def objective_ftr4(df, hyperparameters, neut_features):
    """Objective function for grid and random search. Returns
       the cross validation score from a set of hyperparameters."""
    
    all_res = []
    all_iters = []
    
    # Number of estimators will be found using early stopping
    if 'n_estimators' in hyperparameters.keys():
        del hyperparameters['n_estimators']
    
    out = []
    feature_columns = get_features(df)
    aqs = list(range(1, 121, 1))
    kf = KFold(n_splits=5, shuffle=True, random_state=SEED)
    
    all_models = []
    
    for sp1 in kf.split(aqs):
        test_eras = set()
        train_eras = set()
        for i in sp1[0]:
            train_eras.add('era'+str(i))
        for i in sp1[1]:
            test_eras.add('era'+str(i))
        model = get_cat_model(df, hyperparameters, feature_columns, train_eras, test_eras)
        all_iters.append(model.best_iteration)
        
        
        test_df = df[df['era'].isin(test_eras)]
        xarr = get_X_array(test_df, feature_columns)
        
        
        test_df[PREDICTION_NAME] = model.predict(xarr)
        
        test_df["preds_neutralized"] = test_df.groupby("era").apply(
            lambda x: normalize_and_neutralize(x, [PREDICTION_NAME], neut_features, 1.0) # neutralize by 50% within each era
        )
        scaler = MinMaxScaler()
        test_df[PREDICTION_NAME] = scaler.fit_transform(test_df[["preds_neutralized"]]) # transform back to 0-1
        
        all_res.append(test_df[[TARGET_NAME, PREDICTION_NAME, 'era']])
        
        all_models.append(model)
        
    test_df6 = pd.concat(all_res)
    basic = test_df6.groupby("era").apply(score)
    
    out = []
    for ftr_idx, ftr in enumerate(feature_columns):
        all_res = []
        for model, sp1 in zip(all_models, kf.split(aqs)):
    
            test_eras = set()
            train_eras = set()
            for i in sp1[0]:
                train_eras.add('era'+str(i))
            for i in sp1[1]:
                test_eras.add('era'+str(i))
        
        
            test_df = df[df['era'].isin(test_eras)]
            xarr = get_X_array(test_df, feature_columns)
            xarr[:, ftr_idx] = np.flip(xarr[:, ftr_idx])
        
        
            test_df[PREDICTION_NAME] = model.predict(xarr)
        
            test_df["preds_neutralized"] = test_df.groupby("era").apply(
                lambda x: normalize_and_neutralize(x, [PREDICTION_NAME], neut_features, 1.0) # neutralize by 50% within each era
            )
            scaler = MinMaxScaler()
            test_df[PREDICTION_NAME] = scaler.fit_transform(test_df[["preds_neutralized"]]) # transform back to 0-1
        
            all_res.append(test_df[[TARGET_NAME, PREDICTION_NAME, 'era']])
        
    
        test_df6 = pd.concat(all_res)
        validation_correlations = test_df6.groupby("era").apply(score)
        dif_corr = basic - validation_correlations
        mn_v = dif_corr.mean()
        std_v = dif_corr.std()
        out.append((ftr, mn_v))
        
    hyperparameters['n_estimators'] = int(np.mean(all_iters))
    
    return out

---

### Post #7 — **supernovalx** | 2020-11-01 11:23 UTC

Hi Mark,  
Thanks for sharing the workflow.

Would you mind sharing some information regarding step 1 in the workflow?

  * What were the hyperparameters that you optimizing?
  * What was the best mean CORR you find after the optimization?



Thanks!

---

### Post #8 — **gunturhakim** | 2021-02-24 16:27 UTC

I still making the flow and training, thanks guys the discussion really helps me  
[kost](<https://roomme.id>),best regards
