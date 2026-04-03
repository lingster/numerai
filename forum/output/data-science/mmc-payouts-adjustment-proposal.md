---
title: "MMC Payouts Adjustment Proposal"
category: Data Science
url: https://forum.numer.ai/t/mmc-payouts-adjustment-proposal/614
created_at: 2020-07-06T01:54:00.724000+00:00
last_posted_at: 2020-07-28T16:04:04.436000+00:00
posts_count: 28
views: 4928
tags: []
---

# MMC Payouts Adjustment Proposal

---

### Post #1 — **master_key** | 2020-07-06 01:54 UTC

Right now, we are in a historically great time for standard models, such as integration_test.  
Take a look at this chart of integration_test cumulative scores since Kazutsugi started. 

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a9516ddfd306c7c3da557ceb2d6521a0855385a3.png)image378×264 11.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a9516ddfd306c7c3da557ceb2d6521a0855385a3.png> "image")

The goal of MMC is to encourage users to find unique models that perform well. Right now though, even the models that we internally _really like_ are preferring correlation payouts right now, even though they were the models that we specifically set out to reward more with MMC.

Now, this trend is unlikely to continue, but even so, the existence of this type of scenario to me highlights a shortcoming of MMC: that is, making users play a meta game of having to choose between two different tournament. Users should just simply be rewarded for having a more unique and better model, period.

The example I like to use is Nasdaqjockey. This model has very high correlation and very low correlation with the metamodel, _but is still being payed less than integration_test lately_ , since both are staking on corr.

So my proposal is to not make users choose between corr and MMC. Instead, users could simply opt in to being exposed to MMC at the same time as correlation. Here’s what it looks like for Nasdaqjockey  
**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/7c20dc7e4b7b45d7dc0874d2b938a8ec868e6b9e.png)362×264 12.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/7c20dc7e4b7b45d7dc0874d2b938a8ec868e6b9e.png>)

**

And when you show the same for integration_test: **

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/cd7ca26c3fbd644cb420d6872075033ac6d9c734.png)372×264 13.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/cd7ca26c3fbd644cb420d6872075033ac6d9c734.png>)

**

Notice the difference in Y axis. Nasdaqjockey, in this format, makes almost 2x as much as integration_test, despite overall having very similar correlation scores. This is exactly what we want to reward with MMC.

Note that in in this scenario MMC would not have a 2x payout multiplier as it does now, since the purpose of that was to bring the two separate tournament more in line in terms of risk. If they are combined, then we no longer need this adjustment since you aren’t choosing one over the other.

Will leave this up for some time before making anything official, so others can discuss and give feedback about if this change would make them more interested in finding high MMC models than the current structure.

---

### Post #2 — **joakim** | 2020-07-06 02:03 UTC

Makes perfect sense to me. I hope it’s rolled out.

---

### Post #3 — **lackofintelligence** | 2020-07-06 02:14 UTC

It looks like serious progress is being made to fix MMC from a motivation perspective. I would like to reiterate my suggestion to fix MMC from a data scientist perspective by providing the metamodel because what myself and others have found in practice is that having the example predictions does not provide enough information to train a model that is oblique to the metamodel. I have suggested publishing weights that Numer.ai publishes every week that only indicate which rows of the live data are relevant.

I think the main objection to the weights is that it seems to allow one to get extra information about the meta model itself and therefore this method can be gamed. Now I am sure that there is a way around this detail. Didn’t Numer.ai guys engineer a crypto currency? So they must know something about cryptography. What I am saying is push that cryptographic technique further to give us a one-way cryptographic loss function for MMC. It takes predictions as input and using encrypted truth spits out the MMC Spearman correlation function. Now why can’t you do that?

The encrypted truth that I am talking about is only the best estimate of what the metamodel would have done and I think you have more than enough data to estimate it.

---

### Post #4 — **master_key** | 2020-07-06 02:24 UTC _(reply to #3)_

I agree! But not as straight forward to productionize as my suggestion ![:laughing:](https://emoji.discourse-cdn.com/twitter/laughing.png?v=13)

---

### Post #5 — **lackofintelligence** | 2020-07-06 02:25 UTC _(reply to #4)_

OK, just giving it my best shot. Maybe when you get some more funding.

---

### Post #6 — **no_formal_agreement** | 2020-07-06 03:20 UTC

I am highly confident that the past few rounds are highly atypical for what we should expect going forward. My main NO_FORMAL_TRAINING which been getting optimized for MMC since about round 200 is performing better with respect to CORR under this current regime than it performs on ~half of the eras it was TRAINED on. I would not extrapolate how MMC and CORR behave under this paradigm to how they will behave normally. I think we are falling for the streetlight effect.

Another thing to keep in mind is that low correlation to metamodel predictions does not necessarily imply low correlation to metamodel era performance, ie a model that has very low correlation to the metamodel may still burn on the same eras the metamodel burns. See my posts under [Learning Two Uncorrelated Models](<http://forum.numer.ai/t/learning-two-uncorrelated-models/400/15>).

Unless there is some information you have access to that the users don’t, I think we should wait for more live information before making major changes like this.

---

### Post #7 — **wigglemuse** | 2020-07-06 03:51 UTC

This suggestion, like the ones in the other thread from of_s and bor do not require inside information to calculate the MMC figure itself (in which case they could only test it internally – note that in of_s’s suggestion he is using the meta_corr number AS the mmc, but we have that number too), so I suggest we do the calculations and graphs and put all these suggestions side-by-side for a historical backtest (like Mike has done here for integration_test and nasdaqjockey) but with many different users and see if there are scenarios where someone looks over-penalized or over-rewarded.

---

### Post #8 — **jrb** | 2020-07-06 09:19 UTC

That brings us back to where it all began, homomorphic encryption. ![:stuck_out_tongue:](https://emoji.discourse-cdn.com/twitter/stuck_out_tongue.png?v=13)  
If you’d like to give it a shot, [TFHE](<https://github.com/tfhe/tfhe>) is pretty much the fastest HE implementation out there.

Coming to think of it, I like your idea because of the inherent hardness of it. It’d probably take in the order of a couple of hours to days to compute spearman’s rank correlation coefficient between two sequences with ~5000 data points (roughly, the size of each week’s live set) in a fully homomorphic system.

Edit: Message threading does not seem to work here. For context, this was in reply to [@lackofintelligence](</u/lackofintelligence>)’s [“crypto”](<http://forum.numer.ai/t/mmc-payouts-adjustment-proposal/614/3>) idea.

---

### Post #9 — **nasdaqjockey** | 2020-07-06 16:59 UTC

Obviously this looks great for my models. I like to pick models that are off the beaten path, and up until now, it has treated me quite well. I switched to the MMC tournament for 3 submissions and I’m significantly under-performing CORR. I an VERY interested in this new approach. Can you explain what you mean by “exposed to MMC at the same time as correlation”? Does it mean take the max(CORR, 2*MMC)? Probably not, so what are the cons? I see the pros!

---

### Post #10 — **wigglemuse** | 2020-07-06 18:28 UTC _(reply to #9)_

It means simply CORR + MMC. (both 1x)

---

### Post #11 — **joakim_arvidsson** | 2020-07-06 20:36 UTC

[@master_key](</u/master_key>), would you be increasing the 1*MMC multiplier as MMC gets more difficult to find?

---

### Post #12 — **lackofintelligence** | 2020-07-06 20:55 UTC

[@jrb](</u/jrb>) , We probably want the encrypted one way MMC loss function for the training and validation sets, not for unlabeled eras, and we want to be able to make 100 passes across it per week. [@master_key](</u/master_key>) , having this function for the last week only is needed. That is, publish last week’s encrypted meta model loss function only , not even an estimate of the future model. That would be a very very solid way of creating unique models for the future and its a lot easier.

---

### Post #13 — **jrb** | 2020-07-06 21:24 UTC _(reply to #12)_

[@lackofintelligence](</u/lackofintelligence>) What is an “encrypted one way MMC loss function”? That’s not how a HE system works. What you’re asking for could be trivially exploited, if implemented.

---

### Post #14 — **lackofintelligence** | 2020-07-06 22:43 UTC _(reply to #13)_

[@jrb](</u/jrb>) , I think you understand. The idea is that there is some difficulty in obtaining the loss. Maybe a minute to obtain the loss for the entire dataset. Even if somebody expends a week of computer power to obtain an estimate of last week’s metamodel predictions for all of the rows, it is just last week’s meta model predictions on the training set, what good is it? In fact if you think about it why wouldn’t Numer.ai release it totally free? It does not give you predictions on any live data. In fact, I’ll just say that right now. Why not just release last week’s metamodel predictions on the training and validation data sets? That would be the absolute best place to start looking for a unique model.

---

### Post #15 — **master_key** | 2020-07-06 23:57 UTC _(reply to #9)_

[@wigglemuse](</u/wigglemuse>) is correct, it’s literally MMC + CORR = Payouts. So if your MMC is -0.1 and your Corr is 0.3, your payout would be 0.2

---

### Post #16 — **master_key** | 2020-07-06 23:59 UTC _(reply to #11)_

Good question. I’m not sure how much harder it will be to get MMC over time! We’ll stay committed to making sure we reward models that help us though. Just don’t know if it will be by a multiplier for MMC or what

---

### Post #17 — **muppetshow** | 2020-07-07 00:19 UTC

Seems like a quite usable system. Can’t speak for anyone else but it’d certainly push me more towards MMC.

---

### Post #18 — **seroxatic** | 2020-07-07 15:57 UTC

For Numerai’s long term succes, among other things, it is important that the users with the best and most unique models should have the highest returns.

Just CORR only covers rewarding the ‘best’ models and is therefore unfit. I would even go as far as saying that it is up for replacement as soon as something better comes along.

To increase model uniqueness MMC was introduced earlier this year. But MMC is not just model uniqueness, it also covers relative model performance. Unfortunately, this proved to be it’s biggest flaw. Let me give an (unfortunately fictional) example: I have made the perfect model (for Numerai), an insanely consistent model with 0.03 CORR and a deemingly impossible high sharpe. With such a consistent model I would for sure like to stake on CORR, a stable ~3% return each week is both safe (low risk) and more than profitable enough. Given the uniqueness of this model you would think MMC would be even more profitable. And it might be in the long term. But in the recent period this would result in losses far exceeding your CORR risks & drawdowns. Why? Because all the boosting models achieve >0.06 CORR in these tournament rounds leaving you with negative MMC. And such a risk is not worth it to switch to MMC from your stable CORR returns.  
Relative performance is not a good metric. Integration_Test outperforms NasdaqJockey on more weeks than vice versa, but it is those weeks where Integration_Test does bad where NasdaqJockey shines and the sole reason why it is rightfully praised as a model.

Now MMC+CORR is proposed. I like it much more than just increasing the MMC payouts (i.e.: MMC payouts get 3*MMC values). It covers both unique and good models and could be seen as best of both CORR and MMC. In theory, one could therefore suggest to replace both current tournaments with this new CORR+MMC tournament.

Although parts might be unclear or misunderstood, this message is not meant as critique. I applaud MikeP in his search for the ‘best’ (in all ways) payout metric and whilst it might not last for much longer, MMC was a good step in this journey and we can learn much from it. I believe that CORR+MMC could be a useful next step. But I have the feeling we can come up with something better. CORR+MMC still has the ‘relative performance’ drawback of MMC that I do not like.

I have some ideas, but nothing worth sharing yet. But these thoughts might help others:

  * Can we change MMC to cover only uniqueness? Just as CORR rewards raw performance?
  * Is uniqueness as simple as correlations with other models, or more complicated? If trading is done only on the largest sell/buy signals and/or Numerai first neutralizes our predictions, shouldn’t we include this somewhere/somehow?
  * If NasdaqJockey is one of the ‘best’ models for Numerai - why is it not on top of either (or the combined) leaderboard? Does MMC not correlate that well with their in-house metrics of model usefulness?
  * To reward unique and consistent good performing models like NasdaqJockey, we might need to move away from just correlation and move towards sharpe-based metrics? Sharpe between rounds? Sharpe within rounds (over the individual days of a round)?
  * _EDIT: If we would have a metric for uniqueness, integration_test should be one of the worst models on this metric._ OLD: Why does integration_test not have a negative MMC consistently? It is the least unique model there is.

---

### Post #19 — **wigglemuse** | 2020-07-07 16:57 UTC _(reply to #18)_

It makes sense for integration_test to have positive MMC as it still is one of the best models outright. Any model can (theoretically) get copied, so uniqueness changes with time and trends. (The only reason integration_test is not unique is nothing intrinsic to it – it is because everybody copies it or just submits the exact duplicate predictions.) Negative MMC for a round is basically saying the metamodel would have been better off without this model in it (for this round). So lack of uniqueness itself can’t be the thing that gets you negative MMC – it always has to be tied up with performance somehow.

---

### Post #20 — **seroxatic** | 2020-07-07 17:13 UTC _(reply to #19)_

Thanks for your response Wigglemuse. I understand what you mean and fully agree. My last sentence was meant slightly different, more like: “If we would have a metric for uniqueness, integration_test should be one of the worst models on this metric.”. Edited this in my original post.

If there would be a payout scheme purely based on performance and uniqueness, integration_test should be positively rewarded for it’s performance, and negatively because it is probably one of the least unique models around.

---

### Post #21 — **wigglemuse** | 2020-07-07 17:31 UTC _(reply to #20)_

Well, that’s the question – “negatively” doesn’t seem right, but whatever uniqueness bonus is given, it shouldn’t get much relative to others certainly. And simple CORR+MMC accomplishes that. I’d still be interested in comparing the numbers of different ideas though, so I’m gonna see if I can pull some data since nobody is taking my hints to do it for me. (Somebody else will have to make graphs though.)

---

### Post #22 — **alfa137** | 2020-07-07 20:07 UTC

**Another proposal to merge CORR & MMC: A Dynamic Payout Scheme**

**Motivation:**  
If models with MMC>0 have Mean(CORR)=0.0318 and Mean(MMC)=0.015 and you demand models with high MMC, the multiplier of MMC should be at least twice the multiplier of CORR. That is to say:  
_Payout = w CORR + (2-w) MMC ; such that w <0.667_  
Why? Because improving CORR by +2d is easier than improving MMC by +d. This is in average terms, in marginal terms it can change a little bit.

**Proposal:**  
1.- Start with this initial scheme:  
_Payout = w CORR + (2-w) MMC ; such that w=0.65_  
2.- Adjust “w” depending on the marginal improvement of the average CORR and MMC over time.  
3.- In this way the payout scheme can be changed for every tour in order to give an incentive to the submission of high MMC models.

an example is included in a “Tournament category” post.

---

### Post #23 — **joakim_arvidsson** | 2020-07-08 13:12 UTC

[@master_key](</u/master_key>) would you consider keeping 2*MMC as an option, for people who want to only stake on MMC?

---

### Post #24 — **themicon** | 2020-07-23 21:28 UTC

Some code to check your historical payout using only CORR or MMC or CORR+MMC:
    
    
    #!/usr/bin/env python3
    
    import numerapi
    import matplotlib.pyplot as plt
    import pandas as pd
    import sys
    import numpy as np
    
    api = numerapi.NumerAPI()
    
    # metrictoplot = 'corr'
    # metrictoplot = 'mmc'
    # metrictoplot = 'comb'
    # metrictoplot = 'all'
    
    metrictoplot = sys.argv[1]
    
    username_list = ['integration_test', 'sugaku']
    
    fig1 = plt.figure()
    cmap = plt.cm.get_cmap('tab20b', len(username_list)*3)
    i = 0
    for user in username_list:
    	print("Collecting data for: ", user)
    	user_df = pd.DataFrame(api.daily_submissions_performances(user)).sort_values(by="date").groupby("roundNumber").last()
    	start_round=np.min(user_df.index)
    	end_round=np.max(user_df.index) # most recent resolved round
    	stake_corr = 1.0 # initial stake
    	stake_mmc = 1.0
    	stake_comb = 1.0
    	for r in range(start_round, end_round):
    		if r in user_df.index:
    			corr_score = user_df.loc[r, "correlation"]
    			mmc_score = user_df.loc[r, "mmc"]
    		else:
    			corr_score = 0.0
    			mmc_score = 0.0
    		if np.isnan(user_df.loc[r, "correlation"]) or np.isnan(user_df.loc[r, "mmc"]):
    			corr_score = 0.0
    			mmc_score = 0.0
    		if corr_score:
    			stake_corr *= 1.0 + corr_score*1.0
    			stake_mmc *= 1.0 + mmc_score*2.0 #2x leverage for mmc
    			stake_comb *= 1.0 + corr_score+mmc_score
    		user_df.loc[r, "weekly_stakes_corr"] = stake_corr
    		user_df.loc[r, "weekly_stakes_mmc"] = stake_mmc
    		user_df.loc[r, "weekly_stakes_comb"] = stake_comb
    
    	color = cmap(float(i)/len(username_list))
    
    	if metrictoplot == "corr":
    		plt.title('Expected CORR payout for models', fontsize=17)
    		user_df.weekly_stakes_corr.plot(label=user, color=color)
    		plt.text(end_round-0.75, user_df.loc[r, "weekly_stakes_corr"], user, color=color, fontweight="bold")
    	if metrictoplot == "mmc":
    		plt.title('Expected MMC payout for models', fontsize=17)
    		user_df.weekly_stakes_mmc.plot(label=user, color=color)
    		plt.text(end_round-0.75, user_df.loc[r, "weekly_stakes_mmc"], user, color=color, fontweight="bold")
    	if metrictoplot == "comb":
    		plt.title('Expected CORR+MMC payout for models', fontsize=17)
    		user_df.weekly_stakes_comb.plot(label=user+'_comb', color=color)
    		plt.text(end_round-0.75, user_df.loc[r, "weekly_stakes_comb"], user+'_COMB', color=color, fontweight="bold")
    	if metrictoplot == "all":
    		plt.title('Expected CORR and MMC payout for models', fontsize=17)
    		user_df.weekly_stakes_corr.plot(label=user+'_corr', color=color)
    		plt.text(end_round-0.75, user_df.loc[r, "weekly_stakes_corr"], user+'_CORR', color=color, fontweight="bold")
    		user_df.weekly_stakes_mmc.plot(label=user+'_mmc', color=color)
    		plt.text(end_round-0.75, user_df.loc[r, "weekly_stakes_mmc"], user+'_MMC', color=color, fontweight="bold")
    		user_df.weekly_stakes_comb.plot(label=user+'_comb', color=color)
    		plt.text(end_round-0.75, user_df.loc[r, "weekly_stakes_comb"], user+'_COMB', color=color, fontweight="bold")
    	i += 1
    
    plt.grid(linestyle='--', linewidth=0.5, color="black")
    plt.xlabel('Round number')
    plt.ylabel('Expected payout factor')
    plt.xticks(np.arange(start_round, end_round, 1), rotation=60)
    ax = plt.gca()
    ax.set_facecolor((0.9, 0.9, 0.9))
    plt.show()
    
    sys.exit()

---

### Post #25 — **antonioai** | 2020-07-25 08:17 UTC

Similar to the above but allowing to use a rolling window over the rounds  
(update 12:01:31 25 July 2020: reduce repeated code, accept rolling window size as input)
    
    
    #!/usr/bin/env python3
    
    import sys
    import numerapi
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    
    api = numerapi.NumerAPI()
    
    metrics = ["correlation", "mmc", "comb"]
    metrictoplot = sys.argv[1]
    if metrictoplot not in metrics + ["all"]:
        raise Exception("Valid metric values are %s" % (metrics + ["all"]))
    
    username_list = ['integration_test', 'nasdaqjockey']
    
    plt.figure(figsize=(18, 6))
    cmap = plt.cm.get_cmap('cubehelix', len(username_list)*3)
    rolling_window_size = int(sys.argv[2])
    
    metric_to_style = {"correlation": "-", "mmc": "--", "comb": ":"}
    
    for i, user in enumerate(username_list):
        print("Collecting data for:", user, flush=True)
        user_df = pd.DataFrame(api.daily_submissions_performances(user))\
            .sort_values(by="date")\
            .groupby("roundNumber")\
            .last()
        start_round = user_df.index.min()
        end_round = user_df.index.max()
        user_df["comb"] = user_df["correlation"] + user_df["mmc"]
        user_df["mmc"] *= 2
    
        rolling_series = (user_df[metrics].fillna(0) + 1) \
            .rolling(rolling_window_size)\
            .apply(np.prod, raw=True)
    
        color = cmap(float(i)/len(username_list))
    
        if metrictoplot == "all":
            plt.title('Expected correlation, mmc and comb payout for models', fontsize=17)
            for metric in metrics:
                rolling_series[metric].plot(label=user, color=color, ls=metric_to_style[metric])
                plt.text(end_round, rolling_series[metric].values[-1], "%s - %s" % (user, metric), color=color, fontweight="bold")    
        else:
            plt.title('Expected %s payout for models' % metrictoplot, fontsize=17)
            rolling_series[metrictoplot].plot(label=user, color=color, ls=metric_to_style[metrictoplot])
            plt.text(end_round, rolling_series[metrictoplot].values[-1], "%s - %s" % (user, metrictoplot), color=color, fontweight="bold")    
    
    plt.grid(linestyle='--', linewidth=0.2, color="black")
    plt.xlabel('Round number')
    plt.ylabel('Expected payout factor')
    plt.xticks(np.arange(start_round, end_round, 1), rotation=60)
    ax = plt.gca()
    plt.show()

---

### Post #26 — **alfa137** | 2020-07-25 16:03 UTC

It is an improvement compared to the previous situation. In particular, it is more fear with the best MMC user.  
However, I think it is not enough incentive for users to focus on MMC rather than CORR. You will see it in a couple of months.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/a/54ee81/48.png) [Another proposal to merge CORR & MMC: A Dynamic Payout Scheme](<http://forum.numer.ai/t/another-proposal-to-merge-corr-mmc-a-dynamic-payout-scheme/630>) [Tournament](</c/tournament/7>)

> Motivation: If models with MMC>0 have Mean(CORR)=0.0318 and Mean(MMC)=0.015 and you demand models with high MMC, the multiplier of MMC should be at least twice the multiplier of CORR. That is to say: Payout = w CORR + (2-w) MMC ; such that w<0.667 Why? Because improving CORR by +2d is easier than improving MMC by +d. This is in average terms, in marginal terms it can change a little bit. Proposal: 1.- Start with this initial scheme: Payout = w CORR + (2-w) MMC ; such that w=0.65 …

---

### Post #27 — **jackerparker** | 2020-07-27 12:08 UTC _(reply to #26)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/a/54ee81/48.png) alfa137:

> However, I think it is not enough incentive for users to focus on MMC rather than CORR.

Why do you think that such incentives should exist? In my opinion, developing high MMC models are good for your CORR by itself. If your high MMC model has low CORR but unique enough, you’ll just combine your model with example predictions and will get a model with positive MMC and high CORR. If your high MMC model has high CORR - you will be already happy.

---

### Post #28 — **alfa137** | 2020-07-28 16:04 UTC _(reply to #27)_

jackerparker look at this topic  
[Discussion on incentives: MM clones vs MM improvement](<http://forum.numer.ai/t/discussion-on-incentives-mm-clones-vs-mm-improvement/726>)
