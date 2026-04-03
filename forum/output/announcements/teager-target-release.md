---
title: "Teager Target Release"
category: Announcements
url: https://forum.numer.ai/t/teager-target-release/6832
created_at: 2023-11-29T20:58:57.967000+00:00
last_posted_at: 2023-12-04T20:03:46.709000+00:00
posts_count: 2
views: 1711
tags: []
---

# Teager Target Release

---

### Post #1 — **master_key** | 2023-11-29 20:58 UTC

Numerai has released a new target named Teager, as well as 3 additional related targets: Agnes, Claudia, and Rowan. The payout and scoring target on Numerai will remain the Cyrus target. However, these new targets have been designed to improve the performance of models trained on them.

Teager is one of the most significant targets Numerai has released to date. It handles risk in a totally new way versus all previous Numerai targets making it uncorrelated and uniquely additive as a target to train on.

There are several new accompanying benchmark models. Their historical scores are available on the website and the predictions are available for download via the API.  
More info on benchmark model predictions: [Numerai Docs](<https://docs.numer.ai/numerai-tournament/benchmark_models>)

The model trained on target_teager_v4_20 is doing particularly well over the last year: [V42_LGBM_TEAGER20](<https://numer.ai/v42_lgbm_teager20>)

Models trained on Teager tend to ensemble very well with models trained on Cyrus. A 50/50 blend of a target_cyrus_v4_20 model and a target_teager_v4_20 model improve the Cyrus correlation mean and Sharpe when compared to either a standalone Teager model or standalone Cyrus model.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/fe96e1c47f0058e87aeb9399cd3dcaedda0430ae_2_690x484.png)1600×1124 132 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fe96e1c47f0058e87aeb9399cd3dcaedda0430ae.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/55a293477b6789d58527acb3364e3ab1bfae031e.png)1200×234 19.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/55a293477b6789d58527acb3364e3ab1bfae031e.png>)

An ensemble model of Cyrus and Teager leads to higher correlation Sharpe, higher mean correlation and lower maximum drawdown.

Happy modeling

---

### Post #2 — **taori** | 2023-12-04 20:03 UTC

Target heatmap

[![heatmap](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/14f1ae32938b185abf257e209e2ae77a4e1d84c6_2_500x500.jpeg)heatmap1920×1920 493 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/14f1ae32938b185abf257e209e2ae77a4e1d84c6.jpeg> "heatmap")

Target clustermap

[![cluster](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/832c3b2fa4cf3524f55749f071a20a72a9994bd9_2_500x500.png)cluster3590×3590 302 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/832c3b2fa4cf3524f55749f071a20a72a9994bd9.png> "cluster")
    
    
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    targets = ['target_nomi_v4_20', 'target_nomi_v4_60', 'target_tyler_v4_20', 'target_tyler_v4_60', 'target_victor_v4_20', 'target_victor_v4_60', 'target_ralph_v4_20', 'target_ralph_v4_60', 'target_waldo_v4_20', 'target_waldo_v4_60', 'target_jerome_v4_20', 'target_jerome_v4_60', 'target_janet_v4_20', 'target_janet_v4_60', 'target_ben_v4_20', 'target_ben_v4_60', 'target_alan_v4_20', 'target_alan_v4_60', 'target_paul_v4_20', 'target_paul_v4_60', 'target_george_v4_20', 'target_george_v4_60', 'target_william_v4_20', 'target_william_v4_60', 'target_arthur_v4_20', 'target_arthur_v4_60', 'target_thomas_v4_20', 'target_thomas_v4_60', 'target_cyrus_v4_20', 'target_cyrus_v4_60', 'target_caroline_v4_20', 'target_caroline_v4_60', 'target_sam_v4_20', 'target_sam_v4_60', 'target_xerxes_v4_20', 'target_xerxes_v4_60', 'target_alpha_v4_20', 'target_alpha_v4_60', 'target_bravo_v4_20', 'target_bravo_v4_60', 'target_charlie_v4_20', 'target_charlie_v4_60', 'target_delta_v4_20', 'target_delta_v4_60', 'target_echo_v4_20', 'target_echo_v4_60', 'target_jeremy_v4_20', 'target_jeremy_v4_60', 'target_teager_v4_20', 'target_teager_v4_60', 'target_agnes_v4_20', 'target_agnes_v4_60', 'target_claudia_v4_20', 'target_claudia_v4_60', 'target_rowan_v4_20', 'target_rowan_v4_60']
    
    # analyse the validation data, but we could do the same on the training data
    df = pd.read_parquet('v4.2/validation_int8.parquet', columns=targets + ['era'])
    
    # compute the mean of the era correlation of every target with any other target
    corr = df.groupby('era').corr(method='spearman').mean(axis=0, level=1)
    
    # arrange the order of the columns and rows (for visualization) so that they
    # are sorted by correlation with the target 'target_cyrus_v4_20' 
    corr = corr.sort_values(
        'target_cyrus_v4_20',
        axis=0,
        ascending=False).sort_values(
            'target_cyrus_v4_20',
            axis=1,
        ascending=False)
    
    
    plt.rcParams["figure.figsize"] = [24,24] # default is [6.4, 4.8]
    
    ax = sns.heatmap(corr, annot=True)
    ax.get_figure().savefig('heatmap.png')
    
    sns.clustermap(corr, figsize=(36,36)).savefig('cluster.png')
