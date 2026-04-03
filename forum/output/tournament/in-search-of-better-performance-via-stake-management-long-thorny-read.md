---
title: "In search of better performance via stake management ( long, thorny read )"
category: Tournament
url: https://forum.numer.ai/t/in-search-of-better-performance-via-stake-management-long-thorny-read/6551
created_at: 2023-07-14T01:41:48.226000+00:00
last_posted_at: 2023-07-27T10:34:06.664000+00:00
posts_count: 9
views: 1491
tags: []
---

# In search of better performance via stake management ( long, thorny read )

---

### Post #1 — **traveler** | 2023-07-14 01:41 UTC

This year has been abysmal for my stakes at Numerai, from a high of about 10K NMR to currently about 6.5K NMR ( rounds 429 and 434 were especially dire with 1.2K in loses), all in I am about a net 200 NMR down for the year which is not terrible I guess but as I am currently in the 3rd spot by TC something simply doesn’t add up ( _If you hate suspense I shot myself but there’s a case to be made that Numerai is tossing around loaded guns with the safety off_).

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a4644c2a7552ce9b1f04d166e5b514d6bdfd1825_2_690x358.jpeg)image1408×732 85.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a4644c2a7552ce9b1f04d166e5b514d6bdfd1825.jpeg> "image")

**Diagnostics ?** After 3 years I’ve mostly given up on asking for help to the Numerai team as they either don’t care, can’t help or don’t know how to, but the end result I think is that we have superfluous metrics that misguide us, constant changes that make tracking performance difficult and a messianic obsession with more data as the sole thing that will evolve the competition and generate the market neutral results the fund needs, which based by the latest and upcoming results might not be playing out, all this simply because we can’t efficiently allocate our stakes ( _more on this later_).

**So why not simply quit the competition ?** And believe me I think about rage quitting very often, but unless Bridgewater or Black rock comes knocking on my door, there is a better alternative ( _CrunchDAO imho was not worth the effort vs $_) or I can make my own fund, Numerai is still the only player so far, I also think most early competitors are waiting for another crypto/market cycle or 2 to cash out.

**So why share this ?** In short, our performance as a group is terrible at a time when the fund is trying to get more AUM ( _probably not a good look_ )and since they can’t help we either get better on our own or the project dies/languishes along with whatever value you have invested/earned, tokenomics are simply not working, so more burns will not necessarily generate a higher price to pare down your loses.

**So what to do about this ?** Before moving on I’d like to share my findings which gave me an upset stomach yesterday, these are simple payout “ _backtests_ ” on my 5 current models for resolved rounds starting at round 474 ( _daily rounds_ ) :

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/bcec294c34a599986af649b078d869bc1005d19f_2_690x297.jpeg)image1920×828 271 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/bcec294c34a599986af649b078d869bc1005d19f.jpeg> "image")

There’s a few simplifications and assumptions, but the end result is that my model **k3_02** would have generated the biggest return ( _**with multis TC 3x and Corr 1x**_ _)_ while the worst would have been **k3_04 (_with 3x Corr_ )**, only one model was staked in the period and you guessed it, it was the worst possible payout combination, so why did I stake so much on the worst strategy/model ?

**Greed and misdirection ?,** If I run the same backtest from the start of the year (R 369 to daily starts ) I get :

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4b81de4c64b925805c48083d780cb948e781533c_2_690x308.jpeg)image1920×858 252 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4b81de4c64b925805c48083d780cb948e781533c.jpeg> "image")

The allure of higher TC was my undoing, but there was also not much in the way of risk metrics provided, TC on the leaderboard is 1 Yr which doesn’t make sense when within a 20 day period you can now blow most of your stake and gives you a false sense of security, changing data and targets also muddle this picture and the diagnostics are more of an afterthought, they should be provided automatically and be front and center, the payout scheme also aggravates the issue of chasing high TC.

**The problem with rebalancing. Stakes and models.**

So after this backtest the obvious measure would be to rebalance stakes to models periodically, something that is still not easily done, In my case I need to re upload/overwrite the models in compute and keep a log somewhere with model specifics and mapping through time, hardly ideal but I can’t do anything about it, I might even end up removing my stakes and have to wait 20 days… but more importantly is the issue of how predictive are these backtests and the sad reality is that after 3+ years of rounds we don’t have enough data as the change to daily and other ( _and upcoming_ ) changes effectively were a reset of the competition, and to monitor the drift you need to run tests on unresolved rounds which are very volatile, here’s my current one for instance, rounds tend to “improve” with time but this is not a hard metric :

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4308d7c0a82eea9b75e696ab6e40bfaea39f1977_2_690x319.jpeg)image1920×890 334 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4308d7c0a82eea9b75e696ab6e40bfaea39f1977.jpeg> "image")

And these tests are just the start, I hope that with enough rounds one can start using correlation between backtests and future performance to increase predictability.

**Are you running backtests ?**

And lastly here’s the basic script so you can run your own backtests if you aren’t already doing so ( _please do check the logic as it is not trivial_ ) :

[Colab notebook for Payout Backtests ](<https://colab.research.google.com/drive/1sVtn6kak7LbFmnYuZXKdU43CXLSdGUKQ?usp=sharing>)
    
    
    import pandas as pd
    from numerapi import NumerAPI
    import numpy as np
    
    api = NumerAPI()
    
    def simulate_payout(model_name, start_round, end_round):
        stake = 10000
        payout_factor = 0.10
        max_payout_burn = 0.05
        corr_multipliers = [0.0, 0.5, 1.0]
        tc_multipliers = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    
        model_performances = api.round_model_performances(model_name)
        model_performances = [performance for performance in model_performances if start_round <= performance['roundNumber'] <= end_round]
    
        payout_data = {}
    
        for performance in model_performances:
            round_num = performance['roundNumber']
            corr = performance['corr']
            tc = performance['tc']
    
            for corr_mult in corr_multipliers:
                for tc_mult in tc_multipliers:
                    if tc_mult == 0.0 and corr_mult == 0.0:
                        continue  # Skip the combination of 0x TC and 0x Corr
    
                    payout = stake * np.clip(payout_factor * (corr * corr_mult + tc * tc_mult), -max_payout_burn, max_payout_burn)
    
                    key = f"TC {tc_mult} - CORR {corr_mult}"
                    if key not in payout_data:
                        payout_data[key] = {}
                    payout_data[key][round_num] = payout
    
        df = pd.DataFrame.from_dict(payout_data, orient='columns')
        df.index.name = 'Round'
    
        total_payout = df.sum().sum()
        df.loc['Total'] = pd.Series(df.sum(), name='Total')
    
        # Rank total payouts by multiplier in descending order
        rankings = df.loc['Total'].sort_values(ascending=False)
    
        return rankings
    
    # Example usage
    model_name = "k3_01"
    start_round = 474 # Start Daily
    end_round = 502
    
    # start_round = 369 #Start Year
    # end_round = 474
    
    rankings = simulate_payout(model_name, start_round, end_round)
    print( model_name)
    print(rankings)
    print('///////////////////////////// \n')
    
    model_name = "k3_02"
    rankings = simulate_payout(model_name, start_round, end_round)
    print( model_name)
    print(rankings)
    print('///////////////////////////// \n')
    
    model_name = "k3_03"
    rankings = simulate_payout(model_name, start_round, end_round)
    print( model_name)
    print(rankings)
    print('///////////////////////////// \n')
    
    model_name = "k3_04"
    rankings = simulate_payout(model_name, start_round, end_round)
    print( model_name)
    print(rankings)
    print('///////////////////////////// \n')
    
    model_name = "k3_05"
    rankings = simulate_payout(model_name, start_round, end_round)
    print( model_name)
    print(rankings)
    print('///////////////////////////// \n')
    

  * K

---

### Post #2 — **oraculum** | 2023-07-14 10:49 UTC

Yea, the current period is pretty bad for most of us. I also unstaked my small stake for now not only because of the current period but because of the hard to figure out TC and corr20v2 and low PF. There are always some weird experimental model (like for example the training on recent eras) that doing well for a while, but those are hard to trust because I think with less training data they can go easily bad when the regime changes.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/traveler/48/2417_2.png) traveler:

> they either don’t care, can’t help or don’t know how to

I’m sure they care, it’s the “don’t know how to”. It’s the hardest data science tournament not only for us but for them too, which is also why there is no worthy competitor to Numerai. Also they are trying to help with more data and adjusting the metrics closer to TC, but it looks like it’s not enough and TC in theory seems the right thing but in the current state it seems unpredictable.  
I’m not sure how much the (faster) stake management would help, isn’t ensembling your multiple predictions into one model with the same weight that you would weight your stakes between separate models has the same effect? (maybe only for CORR since TC is so weird)

---

### Post #3 — **prettytoaster** | 2023-07-14 19:04 UTC

I totally share your frustration…

I’ve given up on keeping track of all the changes, today I must say that I don’t understand the tournament anymore, to the point that I’m developing a replacement for numerapi to see if I can understand things better, I’ve also just finished migrating everything to the cloud as microservices (I’m close to 40 microservices and counting…) and I’m building my own dashboards (eg [looker studio](<https://lookerstudio.google.com/reporting/7205b8c4-07e9-4122-9271-4603bad33e15/page/U5VKD>))

My main idea right now is to track submissions individually to decouple the actual models from the accounts… then I’ll split the 70 accounts into tiers and as models accumulate resolved rounds and payouts, they will go up through the tiers (upper tiers will have bigger stakes and multipliers)… much later I will add some feature to like “reset” the tracked stats and reduce the multipliers when I feel that new changes to the tournament break everything again

---

### Post #4 — **edubergeek** | 2023-07-17 00:11 UTC

I had a top 10 model [Diorite](<https://numer.ai/diorite>) for a bit just before data release 4.1. Right about the time I had confidence enough to go all in with my stake **THINGS CHANGED**! This happened to me again with the new cyrus target and the TC payout. My _diorite_ model in DR4 never did as well after that. Of course the market plunged in 2022 so there’s that. I started with v2 then v3 then v4 then v4.1 and I’ve seen target nomi change to cyrus and payouts change from CORR to TC then CORR changed to CORRv2. On the one hand it’s hard to optimize across these changes but on the other hand, the world is dynamic not static. I do appreciate that Numerai maintains backward compatibility. I’m still staking some V3 models (but retrained to predict cyrus).

---

### Post #5 — **edubergeek** | 2023-07-17 01:08 UTC

[@traveler](</u/traveler>) thanks for the code example. I hacked it a bit for my own purposes:
    
    
    import pandas as pd
    from numerapi import NumerAPI
    import numpy as np
    
    api = NumerAPI()
    
    def simulate_payout(model_name, start_round, end_round):
        stake = 10000
        payout_factor = 0.10
        max_payout_burn = 0.05
        corr_multipliers = [0.0, 0.5, 1.0]
        tc_multipliers = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    
        model_performances = api.round_model_performances(model_name)
        model_performances = [performance for performance in model_performances if start_round <= performance['roundNumber'] <= end_round]
        #print('Simulated rounds ', len(model_performances))
    
        payout_data = {}
    
        for performance in model_performances:
            round_num = performance['roundNumber']
            corr = performance['corr']
            tc = performance['tc']
    
            if not(corr is None or tc is None):
                #print("Simulating round ", round_num)
                for corr_mult in corr_multipliers:
                    for tc_mult in tc_multipliers:
                        if tc_mult == 0.0 and corr_mult == 0.0:
                            continue  # Skip the combination of 0x TC and 0x Corr
    
                        payout = stake * np.clip(payout_factor * (corr * corr_mult + tc * tc_mult), -max_payout_burn, max_payout_burn)
    
                        key = f"TC {tc_mult} - CORR {corr_mult}"
                        if key not in payout_data:
                            payout_data[key] = {}
                        payout_data[key][round_num] = payout
    
        df = pd.DataFrame.from_dict(payout_data, orient='columns')
        df.index.name = 'Round'
    
        total_payout = df.sum().sum()
        df.loc['Total'] = pd.Series(df.sum(), name='Total')
    
        # Rank total payouts by multiplier in descending order
        rankings = df.loc['Total'].sort_values(ascending=False)
    
        return rankings
    
    # Usage
    # Up to the last resolved round
    end_round = api.get_current_round() - 24
    
    # Up to the current round
    #end_round = api.get_current_round() - 1
    
    #start_round = 474 # Start Daily payouts
    #start_round = 389 # Jan 2023
    #start_round = 306 # data v4
    #start_round = 385 # data v4.1
    start_round = 474 # target cyrus + CORR20V2 
    
    print('Simulating round %d to %d' %(start_round, end_round))
    
    models = ['shatteredx', 'k3_01', 'k3_02', 'diorite', 'andro_m31', 'rhyolite', 'gneiss', 'geode', 'bodes_m81', '']
    
    model_best = []
    for model_name in models:
        rankings = simulate_payout(model_name, start_round, end_round)
        print( model_name)
        print(rankings)
        best = {'model': model_name, 'stake': rankings.index[0], 'payout': rankings[0]}
        model_best.append(best)
        print('///////////////////////////// \n')
    
    dfs = pd.DataFrame.from_dict(model_best)
    dfs.index.name = 'model'
    dfs = dfs.sort_values(by='payout', ascending=False)
    dfs

---

### Post #6 — **edubergeek** | 2023-07-17 01:10 UTC _(reply to #5)_

[![Screenshot 2023-07-16 151006](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3fec242fc558673d0ed7705e08522fcf303ddb5b.jpeg)Screenshot 2023-07-16 151006348×298 32 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3fec242fc558673d0ed7705e08522fcf303ddb5b.jpeg> "Screenshot 2023-07-16 151006")

---

### Post #7 — **traveler** | 2023-07-17 01:32 UTC _(reply to #5)_

Ohh sweet, so it takes the best multipliers for each model and ranks them ?  
Coincidentally I am about to try to move all my stakes to k3_02 so good to see it’s still performs !

Cheers !

---

### Post #8 — **edubergeek** | 2023-07-17 05:37 UTC _(reply to #7)_

Correct. It ranks the models by the simulated payout of the best stake multiplier for each model. Because I don’t always upload daily predictions I modified simulate_payout() to skip rounds having no prediction. However, that means the total is unnormalized across models. I added an average mode so the payout is normalized by the number of rounds used. This then gives the average payout per round rather than the total payout over all rounds in the range start to end.
    
    
    import pandas as pd
    from numerapi import NumerAPI
    import numpy as np
    
    api = NumerAPI()
    
    def simulate_payout(model_name, start_round, end_round, mode='Total'):
        stake = 10000
        payout_factor = 0.10
        max_payout_burn = 0.05
        corr_multipliers = [0.0, 0.5, 1.0]
        tc_multipliers = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    
        model_performances = api.round_model_performances(model_name)
        model_performances = [performance for performance in model_performances if start_round <= performance['roundNumber'] <= end_round]
        #print('Simulated rounds ', len(model_performances))
    
        payout_data = {}
    
        for performance in model_performances:
            round_num = performance['roundNumber']
            corr = performance['corr']
            tc = performance['tc']
    
            if not(corr is None or tc is None):
                #print("Simulating round ", round_num)
                for corr_mult in corr_multipliers:
                    for tc_mult in tc_multipliers:
                        if tc_mult == 0.0 and corr_mult == 0.0:
                            continue  # Skip the combination of 0x TC and 0x Corr
    
                        payout = stake * np.clip(payout_factor * (corr * corr_mult + tc * tc_mult), -max_payout_burn, max_payout_burn)
    
                        key = f"TC {tc_mult} - CORR {corr_mult}"
                        if key not in payout_data:
                            payout_data[key] = {}
                        payout_data[key][round_num] = payout
    
        df = pd.DataFrame.from_dict(payout_data, orient='columns')
        df.index.name = 'Round'
    
        #total_payout = df.sum().sum()
        if mode == 'Total':
            df.loc[mode] = pd.Series(df.sum(), name=mode)
        else:
            df.loc[mode] = pd.Series(df.mean(), name=mode)
    
        # Rank total payouts by multiplier in descending order
        rankings = df.loc[mode].sort_values(ascending=False)
    
        return rankings
    
    # Up to the last resolved round
    end_round = api.get_current_round() - 24
    
    # Up to the current round
    end_round = api.get_current_round() - 1
    
    # Example usage
    #start_round = 474 # Start Daily payouts
    #start_round = 389 # Jan 2023
    #start_round = 306 # data v4
    #start_round = 385 # data v4.1
    start_round = 474 # target cyrus + CORR20V2 
    
    print('Simulating round %d to %d' %(start_round, end_round))
    
    models = ['shatteredx', 'k3_01', 'k3_02', 'diorite', 'andro_m31', 'rhyolite', 'gneiss', 'geode', 'bodes_m81', '']
    
    model_best = []
    # Set mode to 'Total' for the total payout over the range of rounds
    #mode = 'Total'
    # Set mode to 'Average' for the average payout per round over the range of rounds
    mode = 'Average'
    for model_name in models:
        rankings = simulate_payout(model_name, start_round, end_round, mode=mode)
        print( model_name)
        print(rankings)
        best = {'model': model_name, 'stake': rankings.index[0], 'payout': rankings[0]}
        model_best.append(best)
        print('///////////////////////////// \n')
    
    dfs = pd.DataFrame.from_dict(model_best)
    dfs.index.name = 'model'
    dfs = dfs.sort_values(by='payout', ascending=False)
    dfs

---

### Post #9 — **taori** | 2023-07-27 10:34 UTC

I am baffled (annoyed) that stake management hasn’t improve yet. They announced the account level staking one and something year ago right? Then TC is still a [problem](<http://forum.numer.ai/t/true-contribution-for-dummies>) for the users as it was at its inception. TC is at the foundation of the tournament, not like a nice-to-have feature. Our needs are very low in the priority list of Numerai. This is not a positive symbiosis anymore, where numerai wins when users win.

My take away is that users are considered only data crunchers at this point. I do not particularly care what numerai considers us, I only care about my investment in Numeraire and time. Up to know it has been a good (too good) investment and I wish It could continue, but I have had doubts for the last year or so.
