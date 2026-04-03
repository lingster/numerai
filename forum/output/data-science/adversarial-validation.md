---
title: "Adversarial Validation"
category: Data Science
url: https://forum.numer.ai/t/adversarial-validation/407
created_at: 2020-05-15T14:42:48.150000+00:00
last_posted_at: 2021-04-13T18:30:34.395000+00:00
posts_count: 3
views: 2642
tags: []
---

# Adversarial Validation

---

### Post #1 — **kainsama** | 2020-05-15 14:42 UTC

There is a strong assumption behind many machine learning algorithms, and it’s the belief that the data is comprised of i.i.d (independent and identically distributed) random variables. This assumption could be way off when data gathered from different time periods, various sources (like different geolocations or markets), or the number of samples is just too small. The violation of the i.i.d assumption means that the training data may be considerably different from the test data in terms of statistical characteristics.

This situation makes it hard to devise a robust validation scheme to evaluate our ideas and models. To alleviate this problem, we could use adversarial validation. It is a method for selecting training examples that are most similar to test samples and then using them as our validation set.  
To implement this idea, we can do the following steps:

  * pick a classifier (preferably one that can give us output probabilities)
  * label test samples as class one (y=1) and training data as class zero (y=0)
  * using k-fold cross-validation scheme on train calculate the out of fold (oof) probabilities of being labeled one for the training examples (we are interested in training samples that are most likely to be indistinguishable from the test data)
  * select a set of most similar training samples (ones with high probabilities) and create a validation dataset and use the rest as the training data
  * throw the kitchen sink at the problem and validate your tries!



Here’s a Python implementation:
    
    
    import pandas as pd
    import numpy as np
    from sklearn.ensemble import ExtraTreesClassifier
    from sklearn.model_selection import KFold
    
    #  data
    training_data = pd.read_csv("https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_training_data.csv.xz")
    
    tournament_data = pd.read_csv("https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_tournament_data.csv.xz")
    
    # features
    feature_cols = training_data.columns[training_data.columns.str.startswith('feature')]
    
    # training the classifier
    kf = KFold(n_splits=5, shuffle=True, random_state=666)
    oof = np.zeros(training_data.shape[0])
    for i, (tdx, vdx) in enumerate(kf.split(training_data[feature_cols])):
        print(f'Fold : {i + 1}')
        x_train, x_valid, y_train, y_valid = pd.concat([tournament_data[feature_cols], training_data.loc[tdx, feature_cols]]),\
                                                        training_data.loc[vdx, feature_cols], np.array([1] * tournament_data.shape[0] + [0] * len(tdx)), np.array(len(vdx) * [1])
        clf = ExtraTreesClassifier(n_estimators=100,
                                   random_state=666,
                                   n_jobs=-1,
                                   max_depth=10,
                                   max_features=0.65)
        clf.fit(x_train, y_train)
        oof[vdx] = clf.predict_proba(x_valid)[:, 1]
        
    # picking top 80% as validation data
    threshold = np.percentile(oof, 80)
    validation = training_data.loc[oof >= threshold]
    train = training_data.loc[oof < threshold]

---

### Post #2 — **arbitrage** | 2020-05-15 14:57 UTC

I tried this several years ago and found that the omission of certain data made my models worse. That said, I used completely different training data than what we are using now. I would be careful because I recall that my scores using this method were more volatile, not less. YMMV.

---

### Post #3 — **nillwatson532** | 2021-04-13 18:30 UTC

I’ll assume you’ve loaded the training and test data into pandas DataFrames and called them df_train and df_test, respectively. Then we’ll do some basic cleaning by replacing missing values.

# Replace missing categoricals with “”

df_train.loc[:,cat_cols] = df_train[cat_cols].fillna(’’)  
df_test.loc[:,cat_cols] = df_test[cat_cols].fillna(’’)

# Replace missing numeric with -999

df_train = df_train.fillna(-999)  
df_test = df_test.fillna(-999)  
For adversarial validation, we want to learn a model that predicts which rows are in the training dataset, and which are in the test set. We therefore create a new target column in which the test samples are labeled with 1 and the train samples with 0, like this:  
df_train[‘dataset_label’] = 0  
df_test[‘dataset_label’] = 1  
target = ‘dataset_label’  
This is the target that we’ll train a model to predict. Right now, the train and test datasets are separate, and each dataset has only one label for the target value. If we trained a model on this training set, it would just learn that everything was 0. We want to instead shuffle the train and test datasets, and then create new datasets for fitting and evaluating the adversarial validation model. I define a function for combining, shuffling, and re-splitting:  
def create_adversarial_data(df_train, df_test, cols, N_val=50000):  
df_master = pd.concat([df_train[cols], df_test[cols]], axis=0)  
adversarial_val = df_master.sample(N_val, replace=False)  
adversarial_train = df_master[  
~df_master.index.isin(adversarial_val.index)  
]  
return adversarial_train, adversarial_val

features = cat_cols + numeric_cols + [‘TransactionDT’]  
all_cols = features + [target]  
adversarial_train, adversarial_test = create_adversarial_data(df_train, df_test, all_cols)  
The new datasets, adversarial_train and adversarial_test, include a mix of the original training and test sets, and the target indicates the original dataset. Note: I added TransactionDT to the feature list. The reason for this will become apparent.  
For modeling, I’m going to be using Catboost. I finish data preparation by putting the DataFrames into Catboost Pool objects.

* * *

[Hi-Lo Industrial Trucks Co.](<https://www.hiloindustrial.com/>)
