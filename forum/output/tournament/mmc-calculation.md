---
title: "MMC Calculation"
category: Tournament
url: https://forum.numer.ai/t/mmc-calculation/6882
created_at: 2023-12-21T22:40:49.948000+00:00
last_posted_at: 2023-12-21T22:40:50.081000+00:00
posts_count: 1
views: 548
tags: []
---

# MMC Calculation

---

### Post #1 — **studym8** | 2023-12-21 22:40 UTC

Hey everyone,

With the recent scoring changes, I thought I’d post some sample code to compute MMC locally using numerai-tools, since it was a bit confusing for me at first.

For those who also use colab I made a notebook that handles setup as well [here](<https://colab.research.google.com/drive/1hTfUO1SQ3mDE4_rehKTR39UzLvAWWxMS?usp=sharing>)

I might still have it wrong, so let me know if any feedback!
    
    
    #Install packages with scoring function and numerapi
    !git clone https://github.com/numerai/numerai-tools.git
    !mv numerai-tools/numerai_tools/scoring.py /content/
    !pip install numerapi
    
    from numerapi import NumerAPI
    import pandas as pd
    
    napi = NumerAPI()
    
    napi.list_datasets()
    
    #Download example predictions, meta model preds, and live targets
    napi.download_dataset("v4.2/meta_model.parquet")
    napi.download_dataset("v4.2/validation_benchmark_models.parquet", "validation_benchmark_models.parquet")
    napi.download_dataset("v4.2/validation_int8.parquet")
    
    df_mm = pd.read_parquet("v4.2/meta_model.parquet")
    
    #Get eras that have data from meta model
    mm_eras = df_mm["era"].unique()
    
    bm_val = pd.read_parquet("validation_benchmark_models.parquet")
    
    #Get bechmark predictions only for eras that have meta model data
    bm_val_recent = bm_val.loc[bm_val["era"].isin(mm_eras)]
    
    #Do the same for live targets
    live_targets = pd.read_parquet("v4.2/validation_int8.parquet", columns=["era","target"])
    live_targets_recent = live_targets.loc[live_targets["era"].isin(mm_eras)]
    
    from scoring import correlation_contribution
    
    #correlation_contribution(predictions: pd.DataFrame, meta_model: pd.Series, live_targets: pd.Series)
    mmc = correlation_contribution(bm_val_recent, df_mm["numerai_meta_model"], live_targets_recent["target"])
