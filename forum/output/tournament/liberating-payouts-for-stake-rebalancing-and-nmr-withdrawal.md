---
title: "Liberating payouts for stake rebalancing and NMR withdrawal"
category: Tournament
url: https://forum.numer.ai/t/liberating-payouts-for-stake-rebalancing-and-nmr-withdrawal/3012
created_at: 2021-04-22T04:59:17.384000+00:00
last_posted_at: 2021-06-25T16:07:32.082000+00:00
posts_count: 19
views: 1918
tags: []
---

# Liberating payouts for stake rebalancing and NMR withdrawal

---

### Post #1 — **profricecake** | 2021-04-22 04:59 UTC

Hi all.

I’ve begun grappling with the clumsiness of stake decreases because I want to allocate my NMR differently across my models like I know many users also want. But it’s horribly clumsy and slow. I have to queue up a stake decrease and wait 4 weeks until the NMR posts in my wallet. And if all I wanted was to put that right NMR back into the tourney, it takes a month to do so.

The explanation for why this is so slow is that the tourney rounds last a month, so the NMR I have tied up needs a month to work through the system.

However, not all NMR is tied up in the tourney. **If and when I get a payout, those earnings should be free for me to work with**. They could be rolled into the stake of one or more of my other models, or sent straight to my wallet. But instead of either of these things, Numerai forces each model’s earnings back into that model’s stake for future rounds, tying that NMR up for another month.

Maybe they’re doing this to keep NMR in the tournament, because staked models in the tournament are important to their meta model. Or maybe they’re doing it because moving NMR in and out of wallets incurs a gas fee. Or both.

I don’t think reason one is important. Maybe it was at some point, but the tournament feels quite mature to me. If people are earning, that’s incentive enough to keep their money in. Numerai doesn’t have to hold earnings prisoner.

And gas fees? I’ll come back to gas fees in a moment.

Earnings shouldn’t be encumbered. Period. Users should be able to allocate their earnings wherever they want. If that allocation keeps the NMR in the tourney, then it never leaves Numerai’s control and therefore won’t incur gas fees. **In fact, having more control over earnings will personally incentivize me to put more NMR into the tournament, whereas now I’m hesitant because the payouts are so illogically illiquid**.

I suggest adding a “payout allocation” interface to the website. The default behavior would be that 100% of a model’s earnings goes back into that model’s stake (as it is now). But users could allocate with different percentages to their models, and their wallet.

If the gas fee for wallet allocations remains a deal breaker, then Numerai could create a “pool” for each user, kind of like an escrow account, where any earnings that are not allocated to stake could gather but remain in Numerai’s control, thereby not triggering a gas fee. Then Numerai could allow one free withdrawal per user every two weeks from the pool to their wallet but allow any number of immediate withdrawals if the user pays the gas fee. This is like how PayPal will transfer your money immediately to your bank for a fee, or do it in a few days for free. This would incentivize users to keep their earnings in the tournament, but stop short of holding those earnings hostage for a whole month.

I’m sure that liberating payouts is not a new idea but my frustrations with stake management certainly are, so I thought I’d share this to re-kindle the conversation. Curious for folks’ thoughts.

prc

---

### Post #2 — **asteeber** | 2021-04-22 08:36 UTC

I have to agree. In the Kusama and Polkadot networks, you have an option for your stake rewards to go to stake _or_ stash. We should have that same option especially for people who want to sell their weekly reward as passive income.

---

### Post #3 — **of_s** | 2021-04-22 13:08 UTC

Technically, 25% of the stake is no longer at risk after a week ends corresponding to prior round limits. At the very least, they should release the stake decrease request every week up to that 25% level (less any burns).

I have mentioned this several times in RC over the last year, but the upvotes and thumbs up didn’t translate to enacting.

---

### Post #4 — **wigglemuse** | 2021-04-22 14:04 UTC

They are well aware of all of this. They’re working on it – or at least working on working on it. “Soon.” But yes, it is terrible and just not right.

---

### Post #5 — **arbitrage** | 2021-04-22 16:04 UTC

I’ve been begging for stake management for over a year. This remains my highest priority ‘feature request’ and I ask about it every chance I get.

---

### Post #6 — **ml_is_lyf** | 2021-04-22 17:58 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/profricecake/48/2528_2.png) profricecake:

> If that allocation keeps the NMR in the tourney, then it never leaves Numerai’s control and therefore won’t incur gas fees.

Smart contracts incur gas fees tho, so surely every time the contract is edited (e.g. stake is changed) a gas fee is incurred. From a quick Google I think you can’t edit contracts either, you’d have to cancel it and make a new contract. If that is the case then to move stake between two models you’d have to cancel both contracts and make new ones. So I think this is probably where the real expense must be.

---

### Post #7 — **johnnyjohnny** | 2021-04-22 23:44 UTC _(reply to #6)_

for US people there are also tax consquences to a lot of the possible options so I imagine part of what is taking them a while is considering what systems would / would not be triggering a lot of tax events.

---

### Post #8 — **lucky_chicken** | 2021-04-24 01:15 UTC _(reply to #7)_

Given all the current limitations, is there a best practice? it seems to me that unstaking once per 4 weeks seems the best. For reallocating between models, is it not easier to just upload the predictions to a different ‘slot’ you have every week to opportunity to change where you upload predictions. Or does that mess up something else?

---

### Post #9 — **ml_is_lyf** | 2021-04-24 09:59 UTC _(reply to #8)_

You definitely can upload different models in different slots each week. I was thinking about this the other day and this probably is the best way to keep models as balanced as possible. I think it probably makes the most sense to randomly assign each model to a slot each week if you want to try and equally balance your models.

I wrote some code to backtest the idea and it seems to somewhat work. I tested it with hydration as it was easy to identify which models belonged to them.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/c5fa90f9e764e33bbbdc488d326aad5cf495b225_2_690x358.png)image1174×610 140 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c5fa90f9e764e33bbbdc488d326aad5cf495b225.png> "image")

Here’s the code if you want to give it a go with your own models
    
    
    from tqdm import tqdm
    import datetime
    import copy
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns
    from numerapi import NumerAPI
    
    api = NumerAPI()
    sns.set(rc={'figure.figsize':(20,10)})
    
    """ SET THESE """
    round_min = 238 # start round for the backtest
    round_max = 255 # final round for the backtest
    model_names = set(["hydration"]+["hydration{}".format(model_no) for model_no in range(2,16)]) # the names of the models you want to backtest
    # you could also write model_names like set(["hydration1","hydration2",...]) if your names can't be expressed in a list comprehension
    """ END OF SET THESE """
    
    # in the range of the rounds specified, get the CORRs for the models specified, this takes a few minutes
    model_corrs_by_round = {}
    for round_no in tqdm(range(round_min, round_max+1)):
        model_corrs_by_round[round_no] = {}
        for round_detail in api.round_details(round_no):
            username = round_detail["username"]
            detail_date = round_detail["date"]
            corr = round_detail["correlation"]
            if username in model_names:
                latest_date = model_corrs_by_round[round_no][username][0] if model_corrs_by_round[round_no].get(username) else datetime.datetime.min
                if latest_date < detail_date:
                    model_corrs_by_round[round_no][username] = (detail_date, corr)
    # restructure this into a dataframe with a row for each round
    data = [[round_num]+[round_detail[model_name][1] for model_name in sorted(model_names)] for round_num, round_detail in model_corrs_by_round.items()]
    round_performances = pd.DataFrame(data, columns=["round"]+sorted(model_names))
    round_performances.set_index("round", inplace=True)
    round_sums = round_performances.expanding(1).sum()
    # plot the performance of our models if we always use the same slot for the same model
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    sns.lineplot(data=round_sums, ax=ax1)
    ax1.set(xlabel="Round Number", ylabel="Cumulative Correlations", title="Keep each model in the same slot")
    # create a new dataframe and shuffle the columns in each row so the model in the slot is random for each round
    shuffled_round_performances = copy.deepcopy(round_performances)
    for round_num in round_performances.index.values:
        model_corrs = shuffled_round_performances.loc[round_num].values
        np.random.shuffle(model_corrs)
        shuffled_round_performances.loc[round_num] = pd.Series(model_corrs, index=shuffled_round_performances.loc[round_num].index)
    shuffled_round_performances["average"] = round_performances.mean(axis=1) # add a column for a model with the average performance of all our models as a baseline for if we could equally weight the corrs of all our models
    shuffled_round_performances = shuffled_round_performances.reindex(sorted(shuffled_round_performances.columns), axis=1) # if we sort the columns then the average model is the first plotted, which makes it a little easier to identify
    shuffled_round_sums = shuffled_round_performances.expanding(1).sum()
    # plot performance of this model
    sns.lineplot(data=shuffled_round_sums, ax=ax2)
    ax2.set(xlabel="Round Number", ylabel="Cumulative Correlations", title="Randomly assign models to a slot each week")
    

Of course if you do this keep track of which model is in each slot each work, as otherwise it’ll be hard to keep track of their individual performance

---

### Post #10 — **lucky_chicken** | 2021-04-24 15:28 UTC _(reply to #9)_

Thanks, that confirms what I was thinking. I have not done it because I then need to keep track of all the stats myself and can’t rely on the UI anymore. Might still do at some point though.

---

### Post #11 — **liborty** | 2021-04-26 02:26 UTC

This does not raise my confidence to buy some NMRs and sink them into this if I may never see them again. Thanks for the warning!

---

### Post #12 — **amorfevo** | 2021-04-26 11:58 UTC _(reply to #5)_

I agree with you 100% ^^  
And I won’t stake anything till it’s not done.

---

### Post #13 — **profricecake** | 2021-05-05 17:43 UTC _(reply to #9)_

Stake rebalancing continues to be so maddening!

It just hit me today (I’m slow) that if I run four models, and stagger an NMR withdrawal from each model each week to get NMR out for the purposes of rebalancing, this does put NMR in my wallet but it doesn’t help in the rebalancing effort. Why? Because while those withdrawals are pending on the models, I can’t increase their stake! I’d have to cancel the pending decreases to make an increase, even if I have the NMR to spend in my wallet and want to get it into the tourney ASAP.

That’s so dumb. If I have 10 NMR staked in round X and I try to withdrawal 5 NMR, I understand why it takes until round X+4 for the 5 NMR to appear in my wallet. But if I decide I want to stake 2 NMR back into that model for round X+1, I can’t. Nor can I change my ongoing stake reduction from 5 to 3 (which would be the equivalent) because to change the decrease from 5 to 3 requires cancelling the previous decrease and starting a new month-long process.

Grr!

(and sorry - didn’t intend this to be a reply to [@ml_is_lyf](</u/ml_is_lyf>) but I guess that’s how I began the post)

---

### Post #14 — **wigglemuse** | 2021-05-05 18:29 UTC

You can submit the same model on a new slot with a new stake (of at least 3 NMR) though. If you have a small number of models, you can use the 15 slots to get around some of this nonsense…

---

### Post #15 — **asteeber** | 2021-05-06 03:21 UTC _(reply to #14)_

Isn’t that detrimental to the Meta Model though?

---

### Post #16 — **wigglemuse** | 2021-05-06 15:14 UTC _(reply to #15)_

Staking same model on more than one slot? No – it is exactly the same metamodel-wise as staking it on one slot with the same total stake. i.e. if you have a model and you stake it on one slot for 100 NMR, or if you take that same model and stake it on 4 slots for 25 NMR each there is no difference whatsoever to Numerai.

What _is_ bad for the metamodel is not being able to express our actual confidence in our models through staking because we have no stake management. Right now everything gets automatically compounded which means every week whatever did well the previous round gets bumped up in the metamodel. Which is possibly good to an extent, but at some point we are just pumping up one particular style of model and then there is a big burn (for us and the metamodel) when it stops working. Many of us would like to keep more balanced stakes on diverse models (which would lead to more balanced performance of the MM, instead of extreme earn and burn cycles), which right now is very hard to do. Now I know human nature will dictate that people are still going to chase whatever is doing well recently, but that only would make the MMC better for those of us will a more balanced approach – if only we could rebalance our stakes so that some of the profits from recently high-performing models could be allocated to other models we know are going to do well again eventually. (Or heck, if we could just take profits in a sensible way.) Instead we just compound the bubble until it bursts, and we STILL can’t get our stakes over to the other models, we can only unstake and wait a month.

(You can switch models week-to-week on the same slot of course, and play other tricks with the slots to some extent as I’ve been saying. All of which is a very poor substitute for real stake management.)

---

### Post #17 — **profricecake** | 2021-05-06 16:34 UTC _(reply to #15)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/asteeber/48/605_2.png) asteeber:

> Isn’t that detrimental to the Meta Model though?

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> No – it is exactly the same metamodel-wise as staking it on one slot with the same total stake.

However, it does have an impact on the meaning of the leaderboard, the running-average CORR reputation, the utility of the performance graphs and medals, the value of those 3 month and 12 month returns measures, and so on.

The website, the Compute framework, and essentially the entire competition appear to be built around the idea that Numerai slots correspond to single models. But in order to get more of the kind of stake management we all want, users are throwing all that great supporting stuff out and tracking their own model performance, creating more slots than they’d ideally want, and in general doing blackbelt level stake- and model-fu like suggested above.

All this time wasted by an army of data scientists! I’d so much rather be improving my models.

---

### Post #18 — **wigglemuse** | 2021-05-06 16:45 UTC

^ Yes, it’s a confusing mess this way.

---

### Post #19 — **profricecake** | 2021-06-25 16:07 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/profricecake/48/2528_2.png) profricecake:

> **If and when I get a payout, those earnings should be free for me to work with**.

Good news, everyone!

You can now route your earnings to your wallet if you want. See [this post](<http://forum.numer.ai/t/stake-management-earnings/3643>) from [@slyfox](</u/slyfox>) for more information.

Thanks numerai team!
