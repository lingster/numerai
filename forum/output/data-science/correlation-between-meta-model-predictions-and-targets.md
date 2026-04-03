---
title: "Correlation between Meta Model Predictions and Targets"
category: Data Science
url: https://forum.numer.ai/t/correlation-between-meta-model-predictions-and-targets/6197
created_at: 2023-03-04T00:24:27.030000+00:00
last_posted_at: 2023-03-04T02:47:01.472000+00:00
posts_count: 2
views: 1222
tags: []
---

# Correlation between Meta Model Predictions and Targets

---

### Post #1 — **unsentient** | 2023-03-04 00:24 UTC

I took a look at the correlation between historical meta-model predictions and the actual targets. The results should interest anyone looking to have more control of their model’s correlation with the meta-model.

For the 150 eras where we have labeled meta-model data and no NaNs in the targets (eras 888 to 1038), I found the pearson correlation between each target and the meta-model prediction. I did this for the entire period and era-wise. I then sorted the results by overall correlation and plotted them in the heatmap below. I also included era-wise standard deviation in correlation. I checked the overall p-values and they were (unsurprisingly) much much lower than 0.05.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c72201080b249c45e7c4604568ea62172b88c905_2_690x410.png)image1068×635 66.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c72201080b249c45e7c4604568ea62172b88c905.png> "image")

If you’re like me then the outliers will pique your interest.

Targets Aurthur, Alan, and Janet - 20d and 60d - all fall on the low side of correlation. They also fall on the low side of standard deviation. I.e. they are consistently un-correlated (less-correlated) with the meta-model. For anyone looking to reduce their correlation with the meta-model, they may want to start training on Aurthur, Alan, or Janet.

On the other end of the spectrum, targets seem to fall into two different camps. Targets: thomas_60, ben_60 and george_60 are all high-corr/high-std, while targets: william_60 nomi_60, waldo_60, jerome_60, ralph_60, are tyler_60, all more in the high-corr/low-std camp. If you’re strategy is to stay consistently in the pack and close to the meta-model maybe you want to be training on the latter group, and if you want more of a wild ride then try Thomas Ben or George.

… all very interesting… For me, it raises a lot more questions and paths to investigate.

code to make heatmap, just plug into a colab!
    
    
    !pip install --upgrade numerapi
    import numerapi
    napi = numerapi.NumerAPI()
    napi.download_dataset("v4.1/validation.parquet", "validation.parquet")
    napi.download_dataset("v4.1/meta_model.parquet", "meta_model.parquet")
    import pyarrow.parquet as pq
    import pandas as pd
    md = pq.read_metadata('validation.parquet')
    tgt_cols = [i for i in md.schema.names if i.startswith('target')]
    val_df = pq.read_table('validation.parquet',columns=(['id','era']+tgt_cols),).to_pandas().astype({'era': 'int32'})
    val_df = val_df.drop(columns=['target'])
    val_df = val_df[(val_df.era>=888)&(val_df.era<=1038)] #888 to 1038 represents the eras with labled meta data and targets
    mm_df = pq.read_table('meta_model.parquet').to_pandas().astype({'era': 'int32'})
    mm_df = mm_df[(mm_df.era>=888)&(mm_df.era<=1038)]
    mm_df.drop(columns=['data_type','era'])
    df = pd.concat([val_df,mm_df.numerai_meta_model], axis=1)
    del val_df, mm_df
    new_cols={}
    for col in df.columns:
        new_cols.update({col:col.replace('target_','')})
    df = df.rename(new_cols, axis='columns')
    for col in df.columns:
        new_cols.update({col:col.replace('v4_','')})
    df = df.rename(new_cols, axis='columns')
    df = df.rename({'numerai_meta_model':'meta_model'}, axis='columns')
    overall_corr = df.corrwith(df.meta_model).to_frame().transpose().drop(columns=['era','meta_model'])
    erawise_corr = df.groupby('era').corrwith(df.meta_model).drop(columns=['meta_model'])
    overall_corr = overall_corr.sort_values(by=0,axis=1).rename(index={0: 'Row_1'})
    erawise_corr = erawise_corr[overall_corr.columns.tolist()]
    ew_std = erawise_corr.std().to_frame().transpose()
    import seaborn as sns
    import matplotlib.pyplot as plt
    %matplotlib inline
    fig, axes = plt.subplots(3, 1, figsize=(20,10), gridspec_kw={'height_ratios':[1,1,20]}, sharex=True)
    axes[0].set_title('Overall Target/Meta Model Correlation (with values)')
    axes[1].set_title('Standard Devaition of Overall Correlation (with rank)')
    axes[2].set_title('Erawise Target/Meta Model Correlation')
    sns.heatmap(overall_corr, ax=axes[0], cmap='rocket_r', xticklabels=False, annot=overall_corr)
    sns.heatmap(ew_std,       ax=axes[1], cmap='rocket_r', xticklabels=False, annot=ew_std.rank(axis='columns',).astype('int'))
    sns.heatmap(erawise_corr, ax=axes[2], cmap='rocket_r')
    pass
    

Comments and criticisms are welcome!

---

### Post #2 — **andralienware** | 2023-03-04 02:47 UTC

Thanks, this will be good for ensemble development.
