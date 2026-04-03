---
title: "Initial MM Correlation Tests with Rain Dataset"
category: Data Science
url: https://forum.numer.ai/t/initial-mm-correlation-tests-with-rain-dataset/6825
created_at: 2023-11-27T15:29:11.056000+00:00
last_posted_at: 2023-11-27T19:56:25.216000+00:00
posts_count: 6
views: 563
tags: []
---

# Initial MM Correlation Tests with Rain Dataset

---

### Post #1 — **nasdaqjockey** | 2023-11-27 15:29 UTC

I ran a quick test of the Rain dataset by training a LightGBM model using each of the feature sets defined in 609_v4_2_features.json. I then calculated corr using the validation targets (CWVAL) and the “numerai_meta_model” column in 609_v4_2_meta_model.parquet (CWMM). Here are my results:

[![results](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3ec3531b54595f9d99681cb4c8a963cf12dd6942_2_690x249.jpeg)results917×332 76.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3ec3531b54595f9d99681cb4c8a963cf12dd6942.jpeg> "results")

It makes sense that CWVAL generally increases when more features are used but the inverse relationship shown in the top 5 models is interesting. The CWMM increases as the CWVAL decreases. This hints to me that optimizing for correlation on the training and validation data will not necessarily lead to better performance on mmc (I probably shouldn’t be surprised ![:roll_eyes:](https://emoji.discourse-cdn.com/twitter/roll_eyes.png?v=13)). I also noticed that when I applied any feature neutralization the CWVAL and CWMM always decrease.

Does anyone have any other insights or test results with the Rain dataset?

---

### Post #2 — **eleven_sigma** | 2023-11-27 17:46 UTC _(reply to #1)_

I realized we only have MM data of last 200 eras aprox, so my original comment doesn’t makes sense.  
The explaining of this could be that a lot of V2 & V3 models have been actives after V4 was released, and MM had a big weight of these models.

---

### Post #3 — **f58c** | 2023-11-27 18:57 UTC

i’ve been wondering if correlation with cyrus_v4_20 ~ corr20v2 or with t.c. most of the models i’ve trained do well on t.c. but not corr20v2. through trial and error, i’ve been trying to increase correl. with corr20v2, to get the 2X NMR payout. thanks [@nasdaqjockey](</u/nasdaqjockey>) for the great analysis! i’ll definitely put it to work! care to share your code? ![:smile:](http://forum.numer.ai/images/emoji/twitter/smile.png?v=12)

---

### Post #4 — **nasdaqjockey** | 2023-11-27 19:36 UTC _(reply to #3)_

"""
        train_models.py
        train models defined in models.csv
    """
    
    import pandas as pd
    import json
    from os.path import exists
    from train import train
    from validate import validate
    from tools import time, create_folder
    
    
    if __name__ == '__main__':
    
        with open('d:/rain/609_v4_2_features.json', 'r') as json_file:
            feature_sets = json.load(json_file)['feature_sets']
        models = pd.read_csv('models/models.csv', index_col='model_name')
        for m in models.index.values:
            if not exists(f'models/{m}'):
                row = models.loc[m]
                feature_cols = feature_sets[row['feature_set']]
                model = train(
                    model_name=m,
                    feature_cols=feature_cols,
                    n_estimators=row['n_estimators'],
                    learning_rate=row['learning_rate'],
                    max_depth=row['max_depth'],
                    num_leaves=row['num_leaves'],
                    colsample_bytree=row['colsample_bytree']
                )
    
                # calculate validation metrics & save in validation_results.csv
    
                validate(
                    model_name=m,
                    model=model,
                    feature_cols=feature_cols
                )
    
                # save model and results
    
                print(f'  {time()} save model')
                create_folder('models', m)
                model.booster_.save_model(f'models/{m}/model.txt')
    
    """
        train.py
        train v4.2 rain data with LightGBM
    """
    
    import lightgbm as lgb
    import pandas as pd
    from tools import time
    
    
    def train(model_name,
              feature_cols,
              n_estimators,
              learning_rate,
              max_depth,
              num_leaves,
              colsample_bytree):
        print(f'train model {model_name}')
    
        print(f'  {time()} read training data')
        train_data = pd.read_parquet('d:/rain/609_v4_2_train_int8.parquet')
    
        model = lgb.LGBMRegressor(
            n_estimators=int(n_estimators),
            learning_rate=learning_rate,
            max_depth=int(max_depth),
            num_leaves=int(num_leaves),
            colsample_bytree=colsample_bytree,
            device_type='gpu',
            verbose=-1
        )
        print(f'  {time()} train model')
        model.fit(
            train_data[feature_cols],
            train_data['target']
        )
        return model
    
    """
        validate.py
        validate trained model
    """
    
    import lightgbm as lgb
    import pandas as pd
    from scipy import stats
    import matplotlib.pyplot as plt
    import numpy as np
    from tools import time, full_neutralization
    
    
    def validate(model_name, model, feature_cols):
        print(f'validate model {model_name}')
        if model is None:  # load model if not passed in
            model = lgb.Booster(model_file=f'models/{model_name}/model.txt')
    
        print(f'  {time()} read validation data')
        # Load the validation data, filtering for data_type == 'validation'
        validation = pd.read_parquet('d:/rain/609_v4_2_validation_int8.parquet',
                                     columns=['era', 'data_type'] + feature_cols + ['target'])
        validation = validation[validation['data_type'] == 'validation']
        del validation['data_type']
    
        print(f'  {time()} calculate statistics')
        # Eras are 1 week apart, but targets look 4 weeks into the future,
        # so we need to 'embargo' the 4 eras following our last train era to avoid data leakage.
        eras = [str(era).zfill(4) for era in [575 + i for i in range(4)]]  # eras to embargo
        validation = validation[~validation['era'].isin(eras)]
        predictions = pd.DataFrame(validation.index.values, columns=['id'])
    
        print(f'  {time()} generate predictions')
        y = model.predict(validation[feature_cols])
        validation['prediction'] = y
        predictions['prediction'] = y
        print(f'  {time()} read meta model data')
        # Load the validation data, filtering for data_type == 'validation'
        metamodel = pd.read_parquet('d:/rain/609_v4_2_meta_model.parquet',
                                    columns=['era', 'numerai_meta_model'])
        eras = metamodel['era'].unique()  # eras to keep
        val_data = validation[validation['era'].isin(eras)]
        val_data.loc[:, 'target'] = metamodel['numerai_meta_model']
    
        results = pd.read_csv('results/validation_results.csv', index_col='upload_name')
        for neutralize in range(1):
            upload_name = f'{model_name}_{neutralize}'
            if neutralize > 0:
                print(f'  {time()} neutralize predictions {neutralize}% ({upload_name})')
                predictions['prediction'] = full_neutralization(validation, feature_cols, neutralize / 100).flatten()
    
            print(f'  {time()} compute per-era correlation and mmc')
            per_era_corr = validation.groupby('era').apply(lambda x: numerai_corr(x['prediction'], x['target']))
            per_era_mmc = val_data.groupby('era').apply(lambda x: numerai_corr(x['prediction'], x['target']))
            corr = np.mean(per_era_corr)
            mmc = np.mean(per_era_mmc)
            results.loc[upload_name] = [corr, mmc]  # update validation results
    
            # Plot the per-era corr & mmc
    
            per_era_corr.plot(kind='bar', title=f'Validation Correlation for {upload_name}: {corr}',
                              figsize=(12, 6), xticks=[], snap=False)
            plt.savefig(f'results/{upload_name}_validation_corr.png')
            plt.close()
            per_era_mmc.plot(kind='bar', title=f'Meta Model Correlation for {upload_name}: {mmc}',
                             figsize=(12, 6), xticks=[], snap=False)
            plt.savefig(f'results/{upload_name}_meta_model_corr.png')
            plt.close()
    
        print(f'  {time()} save results')
        results.to_csv('results/validation_results.csv')
    
    
    # NumerAI's primary scoring metric
    def numerai_corr(preds, target):
        # rank (keeping ties) then gaussian-ize predictions to standardize prediction distributions
        ranked_preds = (preds.rank(method='average').values - 0.5) / preds.count()
        gauss_ranked_preds = stats.norm.ppf(ranked_preds)
        # center targets around 0
        centered_target = target - target.mean()
        # raise both preds and target to the power of 1.5 to accentuate the tails
        preds_p15 = np.sign(gauss_ranked_preds) * np.abs(gauss_ranked_preds) ** 1.5
        target_p15 = np.sign(centered_target) * np.abs(centered_target) ** 1.5
        # finally return the Pearson correlation
        return np.corrcoef(preds_p15, target_p15)[0, 1]
    
    """
        tools.py
        miscellaneous functions
    """
    
    from datetime import datetime
    from os.path import exists
    from os import mkdir
    from sklearn.preprocessing import MinMaxScaler
    from numpy import linalg, float32
    from scipy.stats import norm
    
    
    def time():
        return str(datetime.now())[:-7]
    
    
    def prints(text, max_len=80):
        text = '\b' * max_len + ' ' * max_len + '\b' * max_len + text
        print(text, end='', flush=True)
    
    
    def create_folder(path_name, folder_name):
        # create folder in path if it does not exist
        folder = f'{path_name}/{folder_name}'
        if not exists(folder):
            mkdir(folder)
    
    
    def full_neutralization(df, feature_names, neutralize):
        df['prediction'] = df.groupby('era', group_keys=False)\
            .apply(lambda x: normalize_and_neutralize(x, ['prediction'], feature_names, neutralize))
        scaled_preds = MinMaxScaler(feature_range=(0.01, 0.99)).fit_transform(df[['prediction']])
        return scaled_preds
    
    
    def _neutralize(df, columns, by, proportion):
        scores = df[columns]
        exposures = df[by].values
        scores = scores - proportion * exposures.dot(linalg.pinv(exposures.astype(float32)).dot(scores))
        return scores / scores.std()
    
    
    def _normalize(df):
        return norm.ppf((df.rank(method='first') - 0.5) / len(df))
    
    
    def normalize_and_neutralize(df, columns, by, proportion):
        # Convert the scores to a normal distribution
        df[columns] = _normalize(df[columns])
        df[columns] = _neutralize(df, columns, by, proportion)
        return df[columns]

---

### Post #5 — **shatteredx** | 2023-11-27 19:41 UTC

This is not MMC. MMC is metamodel contribution. Your “mm_corr” is CWMM.

---

### Post #6 — **nasdaqjockey** | 2023-11-27 19:56 UTC

Yes, you are correct. I’ll change the post to clarify that. The column names in the graphic are correct though. Thanks.
