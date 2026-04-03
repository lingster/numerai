---
title: "Churn - New Signals Diagnostics Metric"
category: Announcements
url: https://forum.numer.ai/t/churn-new-signals-diagnostics-metric/6417
created_at: 2023-06-02T19:56:20.484000+00:00
last_posted_at: 2023-06-05T18:58:23.504000+00:00
posts_count: 3
views: 1376
tags: []
---

# Churn - New Signals Diagnostics Metric

---

### Post #1 — **chanes** | 2023-06-02 19:56 UTC

# Background

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4ddcd37923b7fbf68cfbc022df0fbab603c5c827.png)image742×575 45.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4ddcd37923b7fbf68cfbc022df0fbab603c5c827.png> "image")

A new metric, churn, has been added to Signals diagnostics. Churn is the correlation of predictions at time t with predictions at time t - 1.

Internal research has shown that the Meta Model performance can improve by including Signals submissions, but only signals with low churn. Real-life hedge fund trading is subject to turnover constraints and trading costs.

We don’t use churn for payouts or scoring, but we plan to incorporate it into the scoring system in the future. We haven’t set specifics, but aiming for a churn value below 0.15 is a good goal for now.

# Details

Below is example code if you want to measure churn without having to submit diagnostics.
    
    
    import pandas as pd
    from numerapi import NumerAPI
    
    napi = NumerAPI()
    
    def calculate_churn_stats(
        df,
        pred_col,
        ticker_col='bloomberg_ticker',
        era_col='friday_date'
    ):
        # rank and normalize per era
        df[f'{pred_col}_ranked'] = df.groupby(era_col)[pred_col].apply(lambda group: (group.rank() - 0.5) / len(group.dropna()))
        
        # fill na with 0.5
        df[f'{pred_col}_ranked_filled'] = df[f'{pred_col}_ranked'].fillna(0.5)
        
        # Sort the dataframe and set a multi-index with id_col and era_col
        df = df.sort_values([ticker_col, era_col], ascending=[True, False])
        df.set_index([ticker_col, era_col], inplace=True)
        
        # drop duplicates
        df = df.loc[~df.index.duplicated(keep='first')]
    
        # Unstack the dataframe to ensure every combination of id_col and era_col has a row
        df_unstacked = df.unstack(level=ticker_col)
    
        # Shift the pred_col within each id_col group
        shifted_df_unstacked = df_unstacked[f'{pred_col}_ranked_filled'].shift(-1)
    
        # Stack the dataframe back to a regular dataframe
        df_shifted = df_unstacked.stack(dropna=False)
        df_shifted[f'{pred_col}_ranked_filled_prev'] = shifted_df_unstacked.stack(dropna=False)
    
        # Calculate Spearman correlation
        churns = df_shifted.groupby(level=era_col).apply(lambda group: 1 - group[f'{pred_col}_ranked_filled'].corr(group[f'{pred_col}_ranked_filled_prev'], method='spearman'))
        
        # Calculate churn stats
        churn_stats_df = churns.agg(['mean', 'std', 'max']).rename(
            index={'mean': 'churn_mean', 'std': 'churn_std', 'max': 'churn_max'})
    
        return churn_stats_df
    
    df = pd.read_csv('example_signal_upload.csv')
    df = df[df['data_type'] == 'validation']
    df['friday_date'] = pd.to_datetime(df['friday_date'], format='%Y-%m-%d')
    
    # get historic tickers for each era from historic_targets file
    napi.download_dataset('signals/historic_targets.csv', 'historic_targets.csv')
    history = pd.read_csv('historic_targets.csv')
    
    # filter out target cols and non-validation data
    history = history[history['data_type'] == 'validation']
    history = history[['friday_date', 'bloomberg_ticker']]
    history['friday_date'] = pd.to_datetime(history['friday_date'], format='%Y%m%d')
    
    # merge diagnostic predictions with history so we know what tickers are missing from each era
    merged = df.merge(history, how='right', left_on=['friday_date', 'bloomberg_ticker'], right_on=['friday_date', 'bloomberg_ticker'])
    
    res = calculate_churn_stats(merged, pred_col='signal', ticker_col='bloomberg_ticker', era_col='friday_date')
    print(res)
    ```

---

### Post #3 — **restrading** | 2023-06-04 06:41 UTC

Why not use numerai_corr for the churn calculation instead of spearman?

---

### Post #4 — **master_key** | 2023-06-05 18:58 UTC _(reply to #2)_

Making sure that stocks in your TB200 predictions tend to be in your TB200 in the following week makes sense. Eg. of your top 200 stocks, how many of them remained as a top 200 stock?
