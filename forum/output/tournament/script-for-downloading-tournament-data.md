---
title: "Script for downloading tournament data"
category: Tournament
url: https://forum.numer.ai/t/script-for-downloading-tournament-data/5746
created_at: 2022-10-13T21:28:34.309000+00:00
last_posted_at: 2022-10-18T20:39:41.805000+00:00
posts_count: 6
views: 1275
tags: []
---

# Script for downloading tournament data

---

### Post #1 — **taori** | 2022-10-13 21:28 UTC

I have been playing around with tournament data for a while and I thought to share the script I use to download the data in case someone is interested. It is easy but who can be bothered to check the API? So here is the script.

.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d02772c7ea9f77587787fcfde2abbee2709f41d6_2_690x413.png)image1135×680 46.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d02772c7ea9f77587787fcfde2abbee2709f41d6.png> "image")
    
    
    from numerapi import NumerAPI
    import pandas as pd
    import json
    
    napi = NumerAPI(
        #    public_id='',
        #    secret_key='',
        verbosity="info")
    
    START_ROUND = 280
    END_ROUND = 333
    TOURNAMENT = 8
    
    query = """
      query($roundNumber: Int!, $tournament: Int!) {
        roundDetails (roundNumber: $roundNumber, tournament: $tournament) {
          roundNumber
          tournament
          roundTarget
          status
          totalStakes
          totalAtStake
          totalPayout
          payoutFactor
          models {
            modelName
            selectedStakeValue
            tc
            correlation
            corr60
            fnc
            fncV3
            mmc
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
        perf.to_csv(f'round-{round_num}.csv', index=False)
        allPerfs.append(perf)
    
        # force type inference (infer_dtype() or convert_dtype() don't seem to work
        # and I cannot be bothered to find out why)
        perf = pd.read_csv(f'round-{round_num}.csv')
    
        r = {k: v for k, v in roundDetails.items() if k != 'models'}
    
        #perf = perf[perf.selectedStakeValue > 0]
        r['stake.mean'] = perf.selectedStakeValue.mean()
        r['stake.median'] = perf.selectedStakeValue.median()
        r['tc.mean'] = perf.tc.mean()
        r['tc.median'] = perf.tc.median()
        r['correlation.mean'] = perf.correlation.mean()
        r['correlation.median'] = perf.correlation.median()
        r['tcVScorr'] = perf.tc.corr(perf.correlation)
    
        rounds.append(r)
    
    pd.DataFrame(rounds).to_csv(f'rounds.csv', index=False)
    pd.DataFrame(pd.concat(allPerfs).dropna(how='any')).to_csv(f'round-{START_ROUND}-{END_ROUND}.csv', index=False)

---

### Post #2 — **taori** | 2022-10-16 08:01 UTC

Unfortunately `roundDetails` query doesn’t return the model correlation with Meta Model information. In case you need that too, you have to make use of `v3UserProfile` query, much less efficient, but this is the only way at the moment.
    
    
    from numerapi import NumerAPI
    import pandas as pd
    import json
    
    napi = NumerAPI(
        #    public_id='',
        #    secret_key='',
        verbosity="info")
    
    START_ROUND = 300
    END_ROUND = 333
    TOURNAMENT = 8
    
    query1 = """
      query($roundNumber: Int!, $tournament: Int!) {
        roundDetails (roundNumber: $roundNumber, tournament: $tournament) {
          roundNumber
          tournament
          roundTarget
          status
          totalStakes
          totalAtStake
          totalPayout
          payoutFactor
          models {
            modelName
          }
       }
    }
    """
    
    query2 = """
      query($modelName: String!) {
       v3UserProfile(modelName: $modelName) {
        roundModelPerformances {
          roundNumber
          roundPayoutFactor
          selectedStakeValue
          corr
          corrPercentile
          corrMultiplier
          corrWMetamodel
          fnc
          fncPercentile
          fncV3
          fncV3Percentile
          tc
          tcPercentile
          tcMultiplier
        }
       }
    }
    """
    
    rounds = []
    modelNames = None
    
    for round_num in range(START_ROUND, END_ROUND+1):
    
        arguments = {'roundNumber': round_num, 'tournament': TOURNAMENT}
        roundDetails = napi.raw_query(query1, arguments)['data']['roundDetails']
    
        r = {k: v for k, v in roundDetails.items() if k != 'models'}
        rounds.append(r)
    
        roundModelNames = set(m['modelName'] for m in roundDetails['models'])
        if modelNames is None:
            modelNames = roundModelNames
        else:
            #modelNames.update(roundModelNames)
            modelNames &= roundModelNames
    
        print(f"Round {round_num}: total names {len(modelNames)}")
    
    pd.DataFrame(rounds).to_csv(f'round-details.csv', index=False)
    
    data = []
    
    for i,modelName in enumerate(modelNames):
    
        print(f"Model {modelName} {i}/{len(modelNames)}")
    
        arguments = {'modelName': modelName}
        perf = napi.raw_query(query2, arguments)['data']['v3UserProfile']
    
        perf = pd.DataFrame(perf['roundModelPerformances'])
        perf = perf[ (perf.roundNumber >= START_ROUND) & (perf.roundNumber <= END_ROUND) ]
        perf['modelName'] = modelName
    
        data.append(perf)
    
    df = pd.concat(data).dropna(how='any')
    pd.DataFrame(df).to_csv(f'round-{START_ROUND}-{END_ROUND}.csv', index=False)

---

### Post #3 — **taori** | 2022-10-18 12:14 UTC

Follow some plots of the data from **rounds 300 to 332** …

First we plot the well known problem of **TC** being very **poorly correlated with** other metrics, such as model **correlation** and **fncV3**.

**Model TC vs CORR**

[![TCvsCORR](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/ff1a8187b9515fc7a33983339bab4f4de6dd3212_2_500x500.png)TCvsCORR600×600 41.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/ff1a8187b9515fc7a33983339bab4f4de6dd3212.png> "TCvsCORR")

**Model TC vs FncV3**

[![TCvsFncV3](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/098846162587b5e21469256824bf6d895c914e33_2_500x500.png)TCvsFncV3600×600 44.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/098846162587b5e21469256824bf6d895c914e33.png> "TCvsFncV3")

Same information but shown by round:

**Model TC vs CORR by Round**

[![TCvsCORRbyRound](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/eda0f93c768a662b5c28bd3f0ad99a81eaca0b02.png)TCvsCORRbyRound640×480 30 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/eda0f93c768a662b5c28bd3f0ad99a81eaca0b02.png> "TCvsCORRbyRound")

**Model TC vs FncV3 by Round**

[![TCvsFncV3byRound](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/22a5970b0ac80f254946be3e80e1e7218a5635a9.png)TCvsFncV3byRound640×480 30.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/22a5970b0ac80f254946be3e80e1e7218a5635a9.png> "TCvsFncV3byRound")

Now I want to see if the relationship of TC with CORR and FNCV3 is somehow influenced by “Model Correlation with Meta Model” or stake amount. So i split the “Model Correlation with Meta Model” and the stake amount in 9 bins.

**Model TC vs CORR by Correlation with Meta Model**

[![TCvsCORRbyCorrWithMM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/12671a73333d25de0f5e6e96fffb2b312ee8ff59_2_679x500.png)TCvsCORRbyCorrWithMM1500×1104 218 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/12671a73333d25de0f5e6e96fffb2b312ee8ff59.png> "TCvsCORRbyCorrWithMM")

**Model TC vs FNCV3 by Correlation with Meta Model**

[![TCvsFncV3byCorrWithMM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/ada2a5003e317073862b37e4b588f5f9a3b46a1b_2_679x500.png)TCvsFncV3byCorrWithMM1500×1104 223 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/ada2a5003e317073862b37e4b588f5f9a3b46a1b.png> "TCvsFncV3byCorrWithMM")

**Model TC vs CORR by Stake**

[![TCvsCORRbyStake](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/ac27a8bf05b410b7eaca74d7fb055d5f70b70cc5_2_679x500.png)TCvsCORRbyStake1500×1104 257 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/ac27a8bf05b410b7eaca74d7fb055d5f70b70cc5.png> "TCvsCORRbyStake")

**Model TC vs FNCV3 by Stake**

[![TCvsFncV3byStake](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f492927bd47f12b177b61fb4bf82e9009e1bd6c8_2_679x500.png)TCvsFncV3byStake1500×1104 264 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f492927bd47f12b177b61fb4bf82e9009e1bd6c8.png> "TCvsFncV3byStake")
    
    
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    df = pd.read_csv('rounds-300-332.csv')
    
    sns.jointplot(data=df, x='corr', y='tc', kind="reg", truncate=False)
    sns.jointplot(data=df, x='fncV3', y='tc', kind="reg", truncate=False)
    
    plt.show()
    
    TCvsCORR = df.groupby(['roundNumber']).apply(lambda x: x.tc.corr(x['corr']))
    TCvsCORR.name='PearsonCoeff(TC,CORR)'
    pd.DataFrame(TCvsCORR).reset_index().plot(x='roundNumber',y='PearsonCoeff(TC,CORR)',kind='line')
    
    TCvsFNCV3 = df.groupby(['roundNumber']).apply(lambda x: x.tc.corr(x['fncV3']))
    TCvsFNCV3.name='PearsonCoeff(TC,FNCV3)'
    pd.DataFrame(TCvsFNCV3).reset_index().plot(x='roundNumber',y='PearsonCoeff(TC,FNCV3)',kind='line')
    
    plt.show()
    
    df['corrWMetamodelBin'] = pd.cut(df['corrWMetamodel'], 9, labels=False)
    df['stakeBin'] = pd.qcut(df['selectedStakeValue'].rank(method='first'), 9, labels=False)
    
    sns.lmplot(data=df, x='corr', y='tc', col='stakeBin', col_wrap=3, truncate=False, scatter_kws={"alpha": 0.6})
    sns.lmplot(data=df, x='fncV3', y='tc', col='stakeBin', col_wrap=3, truncate=False, scatter_kws={"alpha": 0.6})
    
    sns.lmplot(data=df, x='corr', y='tc', col='corrWMetamodelBin', col_wrap=3, truncate=False, scatter_kws={"alpha": 0.6})
    sns.lmplot(data=df, x='fncV3', y='tc', col='corrWMetamodelBin', col_wrap=3, truncate=False, scatter_kws={"alpha": 0.6})
    
    plt.show()

---

### Post #4 — **unsentient** | 2022-10-18 19:48 UTC

wow really fascinating, thanks for sharing!

I’m not the greatest data scientist but I will take a stab at drawing some conclusions from your analysis. Maybe you tell me if you agree or if I’m off base.

From the plots ‘Model TC vs CORR’ and ‘Model TC vs FncV3’ I would agree with you TC is poorly correlated with CORR and FNCV3.

From the plots ‘Model TC vs CORR’ and ‘Model TC vs FncV3’ I would conclude that there is decay or divergence in the relationship betweent CORR/FNCV3 and TC that increases with time. I would suspect that this is true over the entire period since TC was introduced. (Can anyone tell me the round when TC was introduced and also became the base of payout?) I would also guess that this divergence will continue and that the divergence is a feature of TC, not a bug. Perhaps with the introduction of TC users now optimize to that metric and subsequently let their CORRs/FNCV3s drift.

Looking at the plots ‘Model TC vs CORR by Correlation with Meta Model’, ‘Model TC vs FNCV3 by Correlation with Meta Model’, ‘Model TC vs CORR by Stake’, and ‘Model TC vs FNCV3 by Stake’, it doesn’t seem like there is a noticeable effect of “Correlation with Meta Model” or “Stake Size” on the relationship of Model TC and CORR, or the relationship of Model TC and FNCV3.

Maybe we can think about the tournament as a mine. Numerai owns the mine but lets anylone mine it. They give their miners a cut of whatever precious gems (alpha) they dig up and bring to the mine office (payouts). They also beat the miners mercilessly if they bring up useless rocks (burns). All the miners work in the dark, looking for precious gems. For the first few years of the mine, the miners were told that only one kind of precious gem was worth bringing up to the mine office. Because of this all of the miners would look for the same signs in the rock and dig in the same places. After a while, the mine office found out that they had sold too much of the same gem to the wider gem market. They decided to tell the miners that they could bring any precious gem that they could find in the mine up to the office. But now they would be paid a cut of what the wider gem market would pay for these new gems. Neither the office nor the miners know what the new gems (new sources of alpha) are worth until they are sold on the wider market. And even then, the value of the gems is not clear. All the gems from all the miners are sold in one bulk lot. Fortunately, the mine office can calculate the what value of the lot that would have been without an individual miner’s contribution. That difference is the new payout for the miner. Under this new regime, the miners go back into the mine and begin searching for the different gems; each looking for different signs in the rock and digging in different places; all still digging in the dark.

---

### Post #5 — **taori** | 2022-10-18 20:19 UTC _(reply to #4)_

oh my, the mine metaphor is great. I enjoyed reading it…“They also beat the miners mercilessly if they bring up useless rocks (burns)” Lol!

Regarding the analysis I agree with you, except for the decay or divergence. I would avoid drawing too many conclusions from a short period of time, although the plots agree with what you are saying.

All in all I am disappointed by those plots, nothing interested has emerged. However someone might start from this data and dig deeper.

---

### Post #6 — **taori** | 2022-10-18 20:39 UTC _(reply to #4)_

I believe the first round that accepted payout based on TC was 311
