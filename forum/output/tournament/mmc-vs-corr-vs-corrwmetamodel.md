---
title: "MMC vs CORR vs CorrWMetaModel"
category: Tournament
url: https://forum.numer.ai/t/mmc-vs-corr-vs-corrwmetamodel/6856
created_at: 2023-12-15T12:41:42.265000+00:00
last_posted_at: 2023-12-15T12:51:05.938000+00:00
posts_count: 3
views: 555
tags: []
---

# MMC vs CORR vs CorrWMetaModel

---

### Post #1 — **taori** | 2023-12-15 12:41 UTC

Follow-up to [this one](<http://forum.numer.ai/t/tc-vs-corr-vs-fncv3-vs-corrwmetamodel>). This time the focus is on MMC in the round range 300~614.

Let’s see how MMC relates to CORRv2: Plotted below are:

  * scatter plot + regression line of corr and mmc values for each model for each round
  * same plot as above, this time using z-score of corr so that we compare absolute mmc values to relative corr values (relative to the round). z-score(x) = (x - round-x-mean) / round-x-std
  * same plot as above, this time using z-score of both corr and mmc



[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/1d4bc179dcb43273760ae4ec5084f0624e6670ae_2_690x230.png)image1800×600 100 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1d4bc179dcb43273760ae4ec5084f0624e6670ae.png> "image")

Let’s see how MMC relates to CORRv2 depending on the correlation with the meta model (CWMM). CWMM is split in symmetric-to-0 quantiles called corrWMetaModelBin (positive CWMM values becomes 1,2,3,4,5 bins and negative CWMM values becomes -1,-2,-3,-4,-5 bins).

[![MMC-vs-CORRZscore-By-MetaModelCorr](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/47c56b54acd1ac609fc29c4b118fd734cffc0fc8_2_690x276.png)MMC-vs-CORRZscore-By-MetaModelCorr2500×1000 376 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/47c56b54acd1ac609fc29c4b118fd734cffc0fc8.png> "MMC-vs-CORRZscore-By-MetaModelCorr")

Finally let’s see the mean-round-model-correlation-with-meta-model, the mean-round-model-MMC, mean-round-model-CORRv2 and the round-pearson-coefficient between MMC and CORRv2.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f9bd12735772218fa6279cb14399e268557804de_2_676x500.png)image2028×1500 351 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f9bd12735772218fa6279cb14399e268557804de.png> "image")

---

### Post #2 — **taori** | 2023-12-15 12:50 UTC

Data download:
    
    
    #!/usr/bin/env python3
    
    from numerapi import NumerAPI
    import pandas as pd
    import json
    
    napi = NumerAPI(
        #    public_id='',
        #    secret_key='',
        verbosity="info")
    
    START_ROUND = 300
    END_ROUND = 614
    TOURNAMENT = 8
    
    query = """
      query($roundNumber: Int!, $tournament: Int!) {
        roundDetails (roundNumber: $roundNumber, tournament: $tournament) {
          roundId
          roundNumber
          tournament
          roundTarget
          status
          isDaily
          roundResolved
          roundResolveTime
          totalStakes
          totalAtStake
          totalPayout
          payoutFactor
          totalSubmitted
          models {
            roundId
            modelName
            selectedStakeValue
            payoutSettled
            tc
            tcPercentile
            mmc
            mmcPercentile
            v2Corr20
            v2Corr20Percentile
            corrWMetaModel
            fncV3
            fncV4
          }
       }
    }
    """
    
    allPerfs = []
    rounds = []
    for round_num in range(START_ROUND, END_ROUND+1):
    
        print("roundNumber   ", round_num)
    
        arguments = {'roundNumber': round_num, 'tournament': TOURNAMENT}
        roundDetails = napi.raw_query(query, arguments)['data']['roundDetails']
    
        perf = pd.DataFrame(roundDetails['models'])
        perf['roundNumber'] = round_num
        perf['isDaily'] = roundDetails['isDaily']
        allPerfs.append(perf)
    
        r = {k: v for k, v in roundDetails.items() if k != 'models'}
        rounds.append(r)
    
    pd.DataFrame(rounds).to_csv(f'round-details-{START_ROUND}-{END_ROUND}.csv', index=False)
    pd.DataFrame(pd.concat(allPerfs)).to_csv(f'round-{START_ROUND}-{END_ROUND}.csv', index=False)

---

### Post #3 — **taori** | 2023-12-15 12:51 UTC

Plots:
    
    
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
    
    def symmetricBins(df, numBins, column):
        if (df[column] > 0).any():
            df.loc[ df[column] > 0, column+'Bin'] = pd.qcut(df.loc[ df[column] > 0, column], numBins, labels=False) + 1
        if (df[column] < 0).any():
            df.loc[ df[column] < 0, column+'Bin'] = pd.qcut(df.loc[ df[column] < 0, column], numBins, labels=False) - numBins
        df.loc[ df[column] == 0, column+'Bin'] = 0
    
    def zscore(df, column):
        b = df.groupby(['roundNumber']).apply(lambda x: (x[column] - x[column].mean()) / x[column].std())
        b.name = column + 'Zscore'
        b = pd.DataFrame(b).reset_index(level='roundNumber')
        df[column + 'Zscore'] = b[column + 'Zscore']
    
    #
    # Add few additional columns to our data
    #
    
    NUM_BINS=5
    
    symmetricBins(df, NUM_BINS, 'corrWMetaModel')
    
    zscore(df, 'mmc')
    zscore(df, CORR_COL)
    zscore(df, 'corrWMetaModel')
    
    symmetricBins(df, NUM_BINS, 'mmcZscore')
    symmetricBins(df, NUM_BINS, CORR_COL+'Zscore')
    
    #
    # Drop models without stake (optional) after z-score computation
    #
    # df = df[ df["selectedStakeValue"] > 1.0 ]
    
    
    #
    # Do the plotting
    #
    
    sns.jointplot(data=df, x=CORR_COL, y='mmc', kind='reg', truncate=False)
    plt.savefig('MMC-vs-CORR.png')
    sns.jointplot(data=df, x=CORR_COL+'Zscore', y='mmc', kind='reg', truncate=False)
    plt.savefig('MMC-vs-CORRZscore.png')
    sns.jointplot(data=df, x=CORR_COL+'Zscore', y='mmcZscore', kind='reg', truncate=False)
    plt.savefig('MMCZscore-vs-CORRZscore.png')
    sns.lmplot(data=df, x=CORR_COL+'ZscoreBin', y='mmc', x_estimator=np.mean)
    plt.savefig('MMC-vs-CORRBin.png')
    
    
    sns.jointplot(data=df, x='corrWMetaModel', y='mmc', kind='reg', truncate=False)
    plt.savefig('MMC-vs-MetaModelCorr.png')
    sns.jointplot(data=df, x='corrWMetaModel', y='mmcZscore', kind='reg', truncate=False)
    plt.savefig('MMCZscore-vs-MetaModelCorr.png')
    sns.lmplot(data=df, x='corrWMetaModelBin', y='mmc', x_estimator=np.mean)
    plt.savefig('MMC-vs-MetaModelCorrBin.png')
    
    
    sns.lmplot(data=df, x=CORR_COL, y='mmc', col='corrWMetaModelBin', col_wrap=5, truncate=False, scatter_kws={'alpha': 0.6})
    plt.savefig('MMC-vs-CORR-By-MetaModelCorr.png')
    sns.lmplot(data=df, x=CORR_COL+'Zscore', y='mmc', col='corrWMetaModelBin', col_wrap=5, truncate=False, scatter_kws={'alpha': 0.6})
    plt.savefig('MMC-vs-CORRZscore-By-MetaModelCorr.png')
    sns.lmplot(data=df, x=CORR_COL+'Zscore', y='mmcZscore', col='corrWMetaModelBin', col_wrap=5, truncate=False, scatter_kws={'alpha': 0.6})
    plt.savefig('MMCZscore-vs-CORRZscore-By-MetaModelCorr.png')
    
    
    
    plt.rcParams["figure.figsize"] = [25,4] # default is [6.4, 4.8]
    
    
    TMP = df.groupby(['roundNumber']).apply(lambda x: x['mmc'].corr(x[CORR_COL]))
    TMP.name='PearsonCoeff(MMC,CORR)'
    ax = pd.DataFrame(TMP).reset_index().plot(x='roundNumber',y='PearsonCoeff(MMC,CORR)',kind='line')
    if ax.get_ylim()[0] < 0:
        ax.axhspan(ymin=ax.get_ylim()[0], ymax=0, facecolor='red', alpha=0.3)
    ax.get_figure().savefig('MMC-vs-CORR-by-Round.png')
    
    TMP = df.groupby(['roundNumber']).apply(lambda x: x[CORR_COL].mean())
    TMP.name='MeanCORR'
    ax = pd.DataFrame(TMP).reset_index().plot(x='roundNumber',y='MeanCORR',kind='line')
    if ax.get_ylim()[0] < 0:
        ax.axhspan(ymin=ax.get_ylim()[0], ymax=0, facecolor='red', alpha=0.3)
    ax.get_figure().savefig('MeanCORR-by-Round.png')
    
    TMP = df.groupby(['roundNumber']).apply(lambda x: x['mmc'].mean())
    TMP.name='MeanMMC'
    ax = pd.DataFrame(TMP).reset_index().plot(x='roundNumber',y='MeanMMC',kind='line')
    if ax.get_ylim()[0] < 0:
        ax.axhspan(ymin=ax.get_ylim()[0], ymax=0, facecolor='red', alpha=0.3)
    ax.get_figure().savefig('MeanMMC-by-Round.png')
    
    TMP = df.groupby(['roundNumber']).apply(lambda x: x['corrWMetaModel'].mean())
    TMP.name='MeanCorrWMetaModel'
    ax = pd.DataFrame(TMP).reset_index().plot(x='roundNumber',y='MeanCorrWMetaModel',kind='line')
    if ax.get_ylim()[0] < 0:
        ax.axhspan(ymin=ax.get_ylim()[0], ymax=0, facecolor='red', alpha=0.3)
    ax.get_figure().savefig('MeanCorrWMetaModel-By-Round.png')
    
    TMP = df.groupby(['roundNumber']).apply(lambda x: x['payoutSettled'].mean())
    TMP.name='MeanPayout'
    ax = pd.DataFrame(TMP).reset_index().plot(x='roundNumber',y='MeanPayout',kind='line')
    if ax.get_ylim()[0] < 0:
        ax.axhspan(ymin=ax.get_ylim()[0], ymax=0, facecolor='red', alpha=0.3)
    ax.get_figure().savefig('MeanPayout-By-Round.png')
