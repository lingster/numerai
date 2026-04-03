---
title: "About the Stake Weighted Meta Model"
category: Data Science
url: https://forum.numer.ai/t/about-the-stake-weighted-meta-model/6858
created_at: 2023-12-16T15:36:52.899000+00:00
last_posted_at: 2023-12-22T10:48:46.397000+00:00
posts_count: 4
views: 908
tags: []
---

# About the Stake Weighted Meta Model

---

### Post #1 — **taori** | 2023-12-16 15:36 UTC

EDIT: updated plots

After the unfortunate recent big drawdown of the hedge fund, I have wondered if a stake weighted meta model is still a [good choice](<http://forum.numer.ai/t/are-the-meta-model-weights-optimal>) for Numerai.

Looking at the model performance during the drawdown, it becomes clear that even in such difficult times there were very good performing models, whose contribution to the hedge fund was minimal due to their low stake.

Despite that, Numerai seems still confident in the stake weighted meta model approach, and instead they have been focusing on changing the payout scheme to discourage bad performing models from having large stakes.

I can understand Numerai’s decision to stick to their plan. I do not believe it is obvious how to aggregate models so that the meta model performance are maximized - in fact I mentioned once or twice that this would be a challenge worth a dedicated tournament.

Still, I am curious, so I ran some simple simulations of how the meta model performance would look like by adopting different model aggregation methods:

  * model stake weighted (the Numerai preferred choice)
  * mean of all submitted models
  * mean of all staked models (all models whose stake is >= 1NMR)
  * mean of the top 3/10/30 models with highest mean rolling correlation



To compare the performance of these different meta models I used cumulative CORR20V2. I understand that is not exactly the same as comparing the hedge fund performance, though I believe it is a good proxy.

[![cumulative](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3973c5f10312d75dc0feeed186225082ecf382d2_2_690x459.png)cumulative1200×800 87 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3973c5f10312d75dc0feeed186225082ecf382d2.png> "cumulative")

[Download the data](<http://forum.numer.ai/t/mmc-vs-corr-vs-corrwmetamodel/6856/2>), then plot
    
    
    #!/usr/bin/env python3
    
    import sys
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    if len(sys.argv) < 2:
        print("Usage:")
        print(f" {sys.argv[0]} round-xxx-yyy.csv")
        sys.exit(1)
    
    CORR_COL='v2Corr20'
    
    df = pd.read_csv(sys.argv[1])
    
    df = df[ df["isDaily"] == False ] # because of the rolling mean we cannot mix daily and weekly rounds
    
    # keep only the needed columns
    df = df[ ["modelName","selectedStakeValue","v2Corr20","roundNumber"] ]
    
    # make sure of the sorting
    df = df.sort_values(by="roundNumber", ascending=True)
    
    def zscore(df, column):
        s = df.groupby(['roundNumber'])[column].transform(lambda x: (x - x.mean()) / x.std())
        df[column + 'Zscore'] = s
    
    def rolling_mean(df, column, window, shift):
        # shift(...) is required to avoid look-ahead bias
        s = df.groupby(['modelName'])[column].transform(lambda x: x.rolling(window=window).mean().shift(shift) )
        df[column + 'RollingMean'] = s
    
    
    rolling_mean(df, CORR_COL, 4, 4) # 4 rounds rolling mean
    zscore(df, CORR_COL)
    rolling_mean(df, CORR_COL + "Zscore", 4, 4)  # 4 rounds rolling mean
    
    df = df.dropna(how="any") # the rolling mean generates nan to avoid look-ahead bias
    
    staked = df[ df["selectedStakeValue"] > 1.0 ]
    
    plt.rcParams["figure.figsize"] = [12,8] # default is [6.4, 4.8]
    
    def plot(s):
        ax = ((s.fillna(0.) + 1.0).cumprod() - 1.0).plot(kind='line', legend=True, linewidth=3)
        return ax
    
    tmp_series = df.groupby(['roundNumber']).apply(lambda x: x[CORR_COL].mean())
    tmp_series.name='All models Mean v2Corr20'
    plot(tmp_series)
    
    tmp_series = staked.groupby(['roundNumber']).apply(lambda x: x[CORR_COL].mean())
    tmp_series.name='Staked Models Mean v2Corr20'
    plot(tmp_series)
    
    tmp_series = df.groupby(['roundNumber']).apply(lambda x: (x[CORR_COL]*x["selectedStakeValue"]).sum()/x["selectedStakeValue"].sum() )
    tmp_series.name='Stake Weighted v2Corr20'
    plot(tmp_series)
    
    tmp_series = df.groupby(['roundNumber']).apply(lambda x: x.nlargest(3, CORR_COL+"RollingMean")[CORR_COL].mean())
    tmp_series.name='Top 3 Model Rolling Mean v2Corr20'
    plot(tmp_series)
    
    tmp_series = df.groupby(['roundNumber']).apply(lambda x: x.nlargest(10, CORR_COL+"RollingMean")[CORR_COL].mean())
    tmp_series.name='Top 10 Model Rolling Mean v2Corr20'
    plot(tmp_series)
    
    tmp_series = df.groupby(['roundNumber']).apply(lambda x: x.nlargest(30, CORR_COL+"RollingMean")[CORR_COL].mean())
    tmp_series.name='Top 30 Model Rolling Mean v2Corr20'
    ax= plot(tmp_series) 
    
    ax.get_figure().savefig(f"cumulative.png")

---

### Post #3 — **taori** | 2023-12-21 11:38 UTC

Another curiosity, how do top staked models (models != accounts) perform ?

[![cumulative](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/844b251c7da7ffeabc9052a1a0c16cd846f114cf_2_690x459.png)cumulative1200×800 80.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/844b251c7da7ffeabc9052a1a0c16cd846f114cf.png> "cumulative")

[Download the data](<http://forum.numer.ai/t/mmc-vs-corr-vs-corrwmetamodel/6856/2>), then plot
    
    
    #!/usr/bin/env python3
    
    import sys
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    if len(sys.argv) < 2:
        print("Usage:")
        print(f" {sys.argv[0]} round-xxx-yyy.csv")
        sys.exit(1)
    
    CORR_COL='v2Corr20'
    
    df = pd.read_csv(sys.argv[1])
    
    # keep only the needed columns
    df = df[ ["corrWMetaModel","mmc","modelName","payoutSettled","selectedStakeValue","tc","v2Corr20","roundNumber"] ]
    
    # keep only staked models
    df = df[ df["selectedStakeValue"] > 1.0 ]
    
    # make sure of the sorting
    df = df.sort_values(by="roundNumber", ascending=True)
    
    plt.rcParams["figure.figsize"] = [12,8] # default is [6.4, 4.8]
    
    def plot(s):
        ax = ((s.fillna(0.) + 1.0).cumprod() - 1.0).plot(kind='line', legend=True, linewidth=3)
        return ax
    
    tmp_series = df.groupby(['roundNumber']).apply(lambda x: x[CORR_COL].mean())
    tmp_series.name='All staked models Mean v2Corr20'
    plot(tmp_series)
    
    tmp_series = df.groupby(['roundNumber']).apply(lambda x: (x[CORR_COL]*x["selectedStakeValue"]).sum()/x["selectedStakeValue"].sum() )
    tmp_series.name='Stake Weighted v2Corr20'
    plot(tmp_series)
    
    tmp_series = df.groupby(['roundNumber']).apply(lambda x: x.nlargest(3, "selectedStakeValue")[CORR_COL].mean())
    tmp_series.name='Highest 3 Staked Model Mean v2Corr20'
    plot(tmp_series)
    
    tmp_series = df.groupby(['roundNumber']).apply(lambda x: x.nlargest(10, "selectedStakeValue")[CORR_COL].mean())
    tmp_series.name='Highest 10 Staked Model Mean v2Corr20'
    plot(tmp_series)
    
    tmp_series = df.groupby(['roundNumber']).apply(lambda x: x.nlargest(30, "selectedStakeValue")[CORR_COL].mean())
    tmp_series.name='Highest 30 Staked Model Mean v2Corr20'
    ax = plot(tmp_series)
    
    ax.get_figure().savefig(f"cumulative.png")

---

### Post #4 — **andralienware** | 2023-12-22 02:48 UTC _(reply to #3)_

This is the definition of backtest overfitting.

---

### Post #5 — **taori** | 2023-12-22 10:48 UTC

There is no model training here, so there could be no overfitting. These plots show how certain groups of model performed compare to each others.
