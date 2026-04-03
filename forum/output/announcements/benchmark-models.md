---
title: "Benchmark Models"
category: Announcements
url: https://forum.numer.ai/t/benchmark-models/6754
created_at: 2023-10-28T21:04:49.140000+00:00
last_posted_at: 2024-03-10T13:23:06.604000+00:00
posts_count: 10
views: 3703
tags: []
---

# Benchmark Models

---

### Post #1 — **master_key** | 2023-10-28 21:04 UTC

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/942d12f1abacbd4315a781ce81719810b1101071_2_690x182.png)1600×424 97.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/942d12f1abacbd4315a781ce81719810b1101071.png>)

Numerai develops new datasets and new targets to help our data science community build better models. Numerai builds models on each new target and data release. Today, we will begin giving out the predictions for all of these models, and details about how they are created.

# Why?

**New User Acceleration**

Numerai has a steep learning curve. After you make it through the tutorial notebooks, you are left with several datasets, many targets, and many modeling options. There are an unlimited number of experiments you’ll want to run as you begin your journey to the top of the leaderboard. With benchmark models, you can immediately see how well different combinations of data and targets do. I think you’ll find that exploring these models and their predictions and subsequent performance will inspire even more ideas for new models you can build yourself.

**Better Stake Allocation**

If you’re a returning user and you’re a few updates behind, you can see at a glance if your model is still competitive, or if you’d be better off staking on one of the newer benchmark models until you have time to catch back up.

**A Meta Model of Meta Models**

Some users may not have the resources to train large competitive cutting-edge models themselves. However, by just downloading targets, the Meta Model predictions, and Benchmark Model predictions, it may still be possible to recognize that the Meta Model is underweight some types of models, or you might be able to find that certain targets ensemble especially well together, or you might have a strong belief that one target will outperform into the future. You can explore all of these possibilities yourself and even submit and stake on these ensembles with minimal resource requirements.

# Where?

Go to [numer.ai/~benchmark_models](<http://numer.ai/~benchmark_models>) to see a list of models and their recent performance.  
Go to the [docs](<http://docs.numer.ai/numerai-tournament/benchmark_models>) to see more details about how they are made.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/99908941c44aee643ec7feb01fd527fe5a44a38d_2_690x411.png)1600×954 137 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/99908941c44aee643ec7feb01fd527fe5a44a38d.png>)

The validation and live predictions are available through the [api](<https://github.com/uuazed/numerapi>).

> pip install numerapi
    
    
    from numerapi import NumerAPI
    napi = NumerAPI()
    napi.download_dataset("v4.2/validation_benchmark_models.parquet", "validation_benchmark_models.parquet")
    napi.download_dataset("v4.2/live_benchmark_models.parquet", "live_benchmark_models.parquet")
    

There is now a dotted line on your account page’s score charts to directly compare yourself with the benchmark models account.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/bf95f3e6255d2d0b46b7caea9fcd2272d778b803_2_690x226.png)1600×525 73.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/bf95f3e6255d2d0b46b7caea9fcd2272d778b803.png>)

Happy Modeling

---

### Post #2 — **numerologist** | 2023-10-29 03:44 UTC

Thanks for the hard work, [@master_key](</u/master_key>) and Numerai team.

Would it be possible to add a toggle switch (next to “Cumulative” in “…”) to compare user/model performance to MetaModel instead of example models? As a not-very-new user, I’d be interested to see how I perform versus the competition and whether I underperform/contribute to the fund.

---

### Post #3 — **degerhan** | 2023-10-29 07:53 UTC

Thank you [@master_key](</u/master_key>) very helpful. Is v42_example_preds a rename of the former 20k tree lg_lgbm_v42_cyrus20? The docs say v42_example_preds is a standard model (I assume that means 2k trees), looking to understand for benchmark continuity.

---

### Post #4 — **master_key** | 2023-10-29 16:33 UTC _(reply to #3)_

Yeah that’s correct it’s a rename. And all of the benchmark models (still) have 20,000 trees.

---

### Post #5 — **taori** | 2023-10-30 09:17 UTC

This is a bold move, I like it.

---

### Post #6 — **zoliveres** | 2023-11-02 08:09 UTC

[@master_key](</u/master_key>) Can you specify what the `rank_keep_ties_keep_na` function does in the `rank_gauss_pow1` function? I’ll be better put it in the Documentation.

I found a similar funtion in the numerai-tools repo, is this what you are using?

[github.com](<https://github.com/numerai/numerai-tools/blob/1c666a480c988578ca63304d7ed6b358c53c9f5a/numerai_tools/scoring.py#L54>)

#### [numerai/numerai-tools/blob/1c666a480c988578ca63304d7ed6b358c53c9f5a/numerai_tools/scoring.py#L54](<https://github.com/numerai/numerai-tools/blob/1c666a480c988578ca63304d7ed6b358c53c9f5a/numerai_tools/scoring.py#L54>)
    
    
          
    
    
              
        44.     return df.apply(
    
              
        45.         lambda series: (series.rank(method=method).values - 0.5) / series.count()
    
              
        46.     )
    
              
        47. 
                   
    
    
        48. 
                   
    
    
        49. def tie_broken_rank(df: pd.DataFrame) -> pd.DataFrame:
    
              
        50.     # rank columns, breaking ties by index
    
              
        51.     return rank(df, "first")
    
              
        52. 
                   
    
    
        53. 
                   
    
    
        54. def tie_kept_rank(df: pd.DataFrame) -> pd.DataFrame:
    
              
        55.     # rank columns, but keep ties
    
              
        56.     return rank(df, "average")
    
              
        57. 
                   
    
    
        58. 
                   
    
    
        59. def min_max_normalize(s: pd.Series) -> pd.Series:
    
              
        60.     # scale a series to be between 0 and 1
    
              
        61.     return (s - s.min()) / (s.max() - s.min())
    
              
        62. 
                   
    
    
        63. 
                   
    
    
        64. def validate_indices(live_targets: pd.Series, predictions: pd.Series) -> None:

---

### Post #7 — **danzell** | 2023-11-12 08:47 UTC _(reply to #6)_

Would be nice to have a functioning example ![:v:](http://forum.numer.ai/images/emoji/twitter/v.png?v=12)

---

### Post #8 — **danzell** | 2023-11-17 09:00 UTC _(reply to #7)_

I’m still confused. What do you exactly mean by:

> **Ensembles**
> 
> All of the ensembles use the following steps:
> 
>   1. gaussianize each of the predictions on a per-era basis
>   2. standardize to standard deviation 1
>   3. dot-product the predictions with a weights vector representing the desired weight on each model
>   4. gaussianize the resulting predictions vector, and neutralize if there are any features to neutralize to
> 


It would be super helpful if you could provide an example ![:nerd_face:](http://forum.numer.ai/images/emoji/twitter/nerd_face.png?v=12) and share underlying code pls.

---

### Post #9 — **tessier_ashpool** | 2023-11-17 13:39 UTC _(reply to #8)_

But they did provide the code.
    
    
        def gauss_pred(self, X: pd.DataFrame, ensemble_cols, weight_vector):
            for col in X[ensemble_cols]:
                if "era" in X.columns:
                    X[col] = X.groupby("era", group_keys=False)[col].transform(
                        lambda s1: rank_gauss_pow1(s1)
                    )
                else:
                    # check X contains only a single era
                    assert 1800 < X.shape[0] < 6000
                    X[col] = rank_gauss_pow1(X[col])
            return X[ensemble_cols].dot(weight_vector)
    

as for the `rank_keep_ties_keep_na` method, I imagine it is something like this.

for keeping ties use method average and instead of len(s.dropna()) do just len(s) or s.count() so in essence looks something like this
    
    
    def rank_gauss_pow1(s: pd.Series) -> pd.Series:
        # do rank-normalize
    
        # s_rank = rank_keep_ties_keep_na(s)
        # s_rank = (s.rank(method="average") - 0.5) / len(s.dropna())
        s_rank = (s.rank(method="average") - 0.5) / s.count()
        
        # gaussianize
        s_rank_norm = pd.Series(scipy.stats.norm.ppf(s_rank), index=s_rank.index)
    
        # Standardize to 1 std
        result_series = s_rank_norm / s_rank_norm.std()
    
        return result_series

---

### Post #10 — **nasdaqjockey** | 2024-03-10 13:23 UTC

It would be good if this was updated for MMC now.
