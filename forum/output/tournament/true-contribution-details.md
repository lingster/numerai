---
title: "True Contribution Details"
category: Tournament
url: https://forum.numer.ai/t/true-contribution-details/5128
created_at: 2022-03-22T14:58:55.791000+00:00
last_posted_at: 2022-10-30T16:52:23.858000+00:00
posts_count: 39
views: 10766
tags: []
---

# True Contribution Details

---

### Post #1 — **mdo** | 2022-03-22 14:58 UTC

Alignment between the performance of tournament participants and hedge fund profitability is a key element in the construction of Numerai. If a model is ranked at the top of the Numerai leaderboard it should be because it is helping to improve the profitability of the hedge fund the most. Currently, users are evaluated only at the signal level: how well their signal correlates with the target (CORR) and their contribution to the Meta Model signal (MMC). However, Numerai’s portfolio is created by running our custom optimizer on the Meta Model signal. The optimizer enforces constraints and penalties on the portfolio that affect which aspects of the Meta Model signal are reflected in the final portfolio. This can create divergence between what appears to be a good model at the signal level and a model that is truly helping the fund create better portfolios.

For example, the optimizer penalizes feature exposure and thus large feature exposures in the Meta Model signal will not be reflected in the final portfolio. A user with a high feature exposure model may get great correlation with the target (for a while), but their signal will have limited influence on the portfolio since the feature exposure of the portfolio is constrained. Such a user could earn large payouts without ever contributing much information to the portfolio. This is obviously undesirable.

To better align our evaluations of users and the hedge fund performance we are introducing a new metric we call “True Contribution”. The goal of this metric is to estimate how much a user’s signal improves or detracts from the returns of Numerai’s portfolio. By using this metric for payouts, user incentives and hedge fund performance are in perfect alignment. With True Contribution as the payout metric, a user’s stake would increase if their model increased portfolio returns and decrease (burn) if the model reduced returns.

In our first first pass creating True Contribution we calculated the stake weighted Meta Model by leaving each user out in turn used the production optimizer to generate the corresponding portfolios, calculated the returns and then compare to the full stake weighted Meta Model in order to calculate “True Contribution”. There are a few problems with this formulation:

  1. A user’s contribution is then heavily dependent upon their stake and identical signals with the same stake get different scores
  2. Because users with 0 stake would always have 0 contribution there is no way to calculate the metric for unstaked users
  3. Users with small stakes would always have ~0 contribution
  4. Because the production optimizer starts from our current portfolio and enforces turnover constraints, the TC scores are heavily dependent on our past portfolios which users have no knowledge of or control over



Our latest version of TC fixes all these issues while retaining the realism of portfolio construction and returns. To do this, first we realized that the leave-one-user-out method is really just approximating a gradient calculation. What we really want is a quantification of how changing a user’s stake changes the portfolio returns, which is the gradient of portfolio returns with respect to users’ stakes. A true gradient calculation would also have the nice properties that 1) it can be computed for all users simultaneously from a single portfolio optimization rather than computing a separate optimization for each user held out and 2) it will assign the same values to identical signals with different stakes 3) it will assign proper values to 0 stakes. This first property is important for our AWS bills while the second and third properties are important for fairness in the tournament.

But performing a true gradient calculation would require taking a derivative through our portfolio optimizer, which is impossible, right? Actually, no! This seemingly magical feat can be accomplished quite simply using [cvxpylayers](<https://github.com/cvxgrp/cvxpylayers>). This remarkable package based on this award winning 2019 [research paper by Agrawal et al.](<https://web.stanford.edu/~boyd/papers/pdf/diff_cvxpy.pdf>) allows you to include a cvxpy defined convex optimization as a layer in a PyTorch model. Below is our fully differentiable PyTorch module for calculating a portfolio from user predictions and stakes using a simple Linear layer and our cvxpy based optimizer.
    
    
    class SWMModel(nn.Module):
        # Simple end-to-end portfolio model
        def __init__(self, num_stakes, context, optimizer):
            super().__init__()
            
            self.optimizer = optimizer
            self.context = context
    
            # set initial portfolio to 0
            self.context.current_portfolio[:] = 0
            
            # stake weighted Meta Model as a Linear layer
            self.lin1 = nn.Linear(num_stakes, 1, bias=False)
    
        def forward(self, user_predictions):
            # calculate stake weighted Meta Model signal
            x1 = self.lin1(user_predictions)
    
            xin = cp.Parameter(x1.shape)
    
            # get cvxpy problem from optimizer
            self.context.alpha_scores = xin
            self.optimizer._build_optimization_routine(self.context.current_portfolio, self.context, True)
            problem = self.optimizer._optimization_routine
            
            assert problem.is_dpp()
            
            # insert cvxpy problem into a CvxpyLayer
            cvxpylayer = CvxpyLayer(problem, parameters=[xin], variables=problem.variables())
    
            # solve the problem using output of swmm as input to cvxpylayer
            solution = cvxpylayer(x1, solver_args={"max_iters": 1500})
            out = solution[0] - solution[1]
    
            return out, x1
    

We can use this module to calculate portfolio returns and the gradient of the portfolio returns with respect to stakes as follows:
    
    
    swmm = SWMModel(len(stakes), context=context, optimizer=n1_optimizer)
    
    # set weights of linear layer to be user stakes
    swmm.lin1.weight.data=stakes.T
    
    swmm.zero_grad()
    
    # get optimized portfolio and swmm signal
    swmm_port, swmm_signal = swmm(user_preds)
    
    # calculate portfolio returns and then stake gradient wrt returns
    portfolio_returns = swmm_port.T @ stock_returns
    
    # calculate gradient
    portfolio_returns.backward()
    
    # extract gradients from Linear stake weighting layer
    stake_grads = swmm.lin1.weight.grad.numpy().copy()
    

To regularize this gradient, reduce the effect of stake size, and reduce dependencies between user predictions we can perform dropout on the user stakes (i.e. randomly zero-out 50% of the stakes) before calculating the stake weighted Meta Model and calculating the gradients. To calculate our final TC estimate we perform 100 rounds of dropout and then average the gradients across the 100 rounds:
    
    
    for i in range(100):
        print(f'bag {i}', end='\r')
        # set stakes with dropout
        swmm.lin1.weight.data=F.dropout(stakes.T, .5)
        
        swmm.zero_grad()
        # get optimized portfolio and unoptimized signal
        swmm_port, swmm_signal = swmm(user_preds)
    
        # calculate portfolio returns and then stake gradient wrt returns
        portfolio_returns = swmm_port.T @ stock_returns
        portfolio_returns.backward()
        stake_grads.append(swmm.lin1.weight.grad.numpy().copy())
    

This process gives very stable estimates that are 99.5% correlated across repeated trials with different dropout masks. The regularization also doesn’t produce results that are vastly different from the unregularized gradient, they are in fact about 90% correlated. While perhaps not absolutely necessary, we feel this regularization helps with the fairness and robustness of the metric, especially given that in reality models are dropping in and out of Numerai’s Meta Model all the time.

Taking a proper gradient solves the first three problems with our initial formulation. To address the fourth problem of making True Contribution independent of our current portfolio holdings, we can create a modified version of our optimizer where we remove the turnover constraint and allow the optimizer a full trading budget to find the optimal portfolio given the Meta Model signal. This generates a hypothetical but realistic portfolio which satisfies all the constraints of the optimizer. While this modified optimizer won’t produce the real portfolio we actually trade, the portfolio it does produce is a realistic reflection of how the Meta Model signal interacts with the portfolio optimizer and its various constraints and penalties.

Hopefully you find this formulation of TC as compelling as we do. In any case you are probably wondering what existing metrics best correspond to TC. To get a better sense of the relationship we can fit a model to predict TC scores from other metrics. A good choice for building flexible and interpretable models is the [Explainable Boosting Machine](<https://github.com/interpretml/interpret>) (EBM). The EBM fits a generalized additive model (GAM) with 2-way interactions. The EBM is tree based like standard Gradient Boosting Machines (e.g. XGBoost, LightGBM) but is restricted to fit only GAMs. In the GAM formulation each variable (and interaction) gets its own learned function and these are all additively combined. To interpret the model you can compare importance scores and visualize the learned functions for each variable. A good proxy metric for TC would have both a high importance score and a monotonic relationship to TC. For this analysis I fit a model predicting TC from various metrics for rounds 272-300. Obviously this can only show us what TC has historically been related to and is no guarantee of what can happen in the future as user change their models. But caveats aside, let’s see what we find:  


[![newplot \(18\)](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b7490b169a43f7da6eaab4c22370d076d15269a6_2_690x352.png)newplot (18)882×450 28.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b7490b169a43f7da6eaab4c22370d076d15269a6.png> "newplot \(18\)")

  
We see that far and away the best proxy is FNCv3, that is a prediction’s correlation with the target after prediction has been neutralized to the 420 features in the “medium” feature set (it will be formally announced later this week!). This measures how much alpha your signal has that isn’t linearly explained by the features. FNCv3 also shows a nice monotonic relationship to TC. (The bit of jaggedness in the functions is just overfitting and can be removed by tuning the EBM hyperparameters. The general trend is pretty obvious.)  


[![newplot \(19\)](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/ee3320114bf05c34ef75a3db2e9f874851ee2fea_2_690x352.png)newplot (19)882×450 28.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/ee3320114bf05c34ef75a3db2e9f874851ee2fea.png> "newplot \(19\)")

The next best proxy is the interaction between FNCv3 and “Exposure Dissimilarity”. The “Exposure Dissimilarity” is a simple metric to compare a model’s pattern of feature exposure to the example predictions. The basic idea is that a signal containing information not already in the example predictions is likely to have a very different pattern of feature exposures. To calculate Exposure Dissimilarity:

  1. Calculate the correlation of a user’s prediction and the example prediction with each of the features to form two vectors U and E.
  2. Take the dot product of U and E divided by the dot product of E with E. This measures how similar the pattern of exposures are and is normalized to be 1 if U is identical to E.
  3. Subtract from 1 to form a dissimilarity metric where 0 means the same exposure pattern as example predictions, positive values indicate differing patterns of exposure and negative values indicate similar patterns but even higher exposures. Note that models with 0 feature exposure will have a dissimilarity value of 1.



Exposure Dissimilarity: 1 - U•E/E•E

By itself, Exposure Dissimilarity doesn’t explain TC, but the combination with FNCv3 in a multiplicative interaction is the next best proxy for TC. (This interaction was included explicitly because in preliminary analysis the EBM kept finding what looked like strong multiplicative interaction between these variables.) This interaction term also makes intuitive sense: TC rewards signals that are both unique and that contain feature independent alpha. This interaction term also bears a strong monotonic relationship to TC.  


[![newplot \(20\)](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e34142378865a3c7c2859c63d6234390e28bb356_2_690x352.png)newplot (20)882×450 29.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e34142378865a3c7c2859c63d6234390e28bb356.png> "newplot \(20\)")

The next most important metric is the venerable [MMC](<http://forum.numer.ai/t/mmc2-announcement/93>), which also shows a strong monotonic relationship to TC.  


[![newplot \(14\)](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/866acf69157997d9a5977c7b55656f7f99da7837_2_690x352.png)newplot (14)882×450 30.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/866acf69157997d9a5977c7b55656f7f99da7837.png> "newplot \(14\)")

This is followed by the correlation of the top/bottom 200 elements of the feature neutralized prediction with the target, i.e. FNCv3 TB 200. This metric also shows a strong monotonic relationship to TC that is in addition to the FNC relationship. Indeed, if this metric had no additional useful information the function would not appear fairly cleanly monotonic, as we will see with CORR. This shows that good performance in the tails is also important for explaining TC.  


[![newplot \(21\)](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/55c83f144d615c3187b134e289d5f6c08bc18274_2_690x352.png)newplot (21)882×450 30.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/55c83f144d615c3187b134e289d5f6c08bc18274.png> "newplot \(21\)")

The next most important metric is Maximum Exposure. While this metric doesn’t strongly influence TC, as you can see by the comparably small dynamic range of the function on the Y-axis, the interesting thing in this plot is that TC seems most associated with small, but nonzero maximum feature exposures. The optimal range for max feature exposures seems to be in [0.05, 0.30].  


[![newplot \(16\)](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a0288c2de14758c955c20510f5b192c4a377d791_2_690x352.png)newplot (16)882×450 24 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a0288c2de14758c955c20510f5b192c4a377d791.png> "newplot \(16\)")

The final metric we will discuss is CORR. As you can see from the plot below the relationship between CORR and TC has small dynamic range and is notably non-monotonic. I want to emphasize that if it was only CORR in the EBM’s input, we would see an apparent monotonic relationship to TC. On average higher CORR is associated with higher TC, but when the other metrics are included they more cleanly explain TC and leave CORR with little additional variance to account for.  


[![newplot \(17\)](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3f649b064d733de23a13bf0d3e3dfa5908597811_2_690x352.png)newplot (17)882×450 29.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3f649b064d733de23a13bf0d3e3dfa5908597811.png> "newplot \(17\)")

As you can see from the above, TC seems to capture the properties we have long recommended for user models to possess: predictive power that isn’t too dependent on single features, predictive power in the tails, uniqueness. To help everyone out, I made a [follow up post demonstrating methods for directly optimizing metrics like FNC and TB200](<http://forum.numer.ai/t/optimizing-for-fnc-and-tb-scores/5132>). Judging by the models doing the best at TC, some of you have been listening closely and have figured a lot of things out already ![:wink:](https://emoji.discourse-cdn.com/twitter/wink.png?v=13)

To maximize backward compatibility while maximizing the impact of TC, starting April 9th users will be able to stake on (0x or 1x CORR) + (0x or 1x or 2x TC). Staking on MMC will be automatically discontinued on that date. So if you are currently staking on 1x CORR and 2x MMC, your stake will be 1x CORR only starting April 9th unless you also elect to stake on 1x TC or 2x TC. Numerai will not automatically convert any MMC stakes to TC stakes. TC staking will start as opt-in only. There will be no changes to the payout factor for the time being.

---

### Post #2 — **ia_ai** | 2022-03-22 18:14 UTC

Are we also keeping the payout factor for the time being (say, until staking on CORR is no longer available)?

---

### Post #3 — **johnnywhippet** | 2022-03-22 19:42 UTC

This is a great filtering mechanism. Who’s dropping out? Assuming CORR will be disappearing soonish, 5037 models have a TC score higher than 0.0, of those 1890 have a score greater than 0.01, 638 have a score higher than 0.02 and so on and so forth. My highest ranked model by TC is 243rd.

I estimate my returns will be halved. Wondering what the effect on the value of NMR will be. My guess is there will be a mass exodus (i know some competitors have multiple models…) and its value will plummet.

incentive to develop a better model perhaps but not if the value of NMR plumments.

Hmmm. badly thought out rant over.

---

### Post #4 — **wigglemuse** | 2022-03-22 19:53 UTC _(reply to #3)_

You make it sound there is no choice but to keep submitting the same models and suffer, or else quit. You can instead submit models more suitable for scoring on TC, which is where the incentive will be so I’m sure that’s what people will do. My staked models – which do ok under current payout scheme – all suck on TC. Doesn’t bother me a bit – I didn’t build them to be good on TC. Frankly, I can’t wait to get rid of them and bet on some more interesting stuff instead. I expect my earning rate to go up.

---

### Post #5 — **johnnywhippet** | 2022-03-22 20:06 UTC _(reply to #4)_

Point taken. i will be reducing my stake for the foreseeable future. until i come up with or don’t come up with a better model.

---

### Post #6 — **wigglemuse** | 2022-03-22 20:13 UTC

Of course if a bunch of people pull their stakes then the payout factor goes up so that helps too (if you’re scoring positively).

---

### Post #7 — **johnnywhippet** | 2022-03-22 20:18 UTC _(reply to #6)_

very positively, for now anyway.

---

### Post #8 — **eleven_sigma** | 2022-03-22 20:19 UTC _(reply to #1)_

[@mdo](</u/mdo>)  
Which would be the behaviour if a model is stacked two times? It will reduce its TC? And if so, it will depend of the relative amount of the stack of both models or will be independent of the relative size of them?

---

### Post #9 — **mdo** | 2022-03-22 20:35 UTC _(reply to #8)_

Identical signals get identical TC regardless of stake. Theoretically a signal could get a negative TC if it is overstaked, but empirically the distribution of people’s gradients when their stake is zeroed out by dropout vs when their stake is kept are indistinguishable.

---

### Post #10 — **yxbot** | 2022-03-22 20:35 UTC

any chance you can enable 0.5xTC ? ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

---

### Post #11 — **qeintelligence** | 2022-03-22 22:24 UTC

I am wondering how many people will reduce their stake in april, and what the overall impact will be on the metamodel. There must be models who rely heavily on MMC and suddenly that option is gone. I hoped for some kind of transition period.

---

### Post #12 — **mic** | 2022-03-23 02:24 UTC

Thanks for the write up [@mdo](</u/mdo>)

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> perform dropout on the user stakes (i.e. randomly zero-out 50% of the stakes)

when doing this dropout, is it a random 50% of total stake value, or 50% of the total number of discrete stakes?

is the users own stake always zeroed?

---

### Post #13 — **johnnywhippet** | 2022-03-23 08:35 UTC _(reply to #10)_

And introduce an abs(TC) too please…

---

### Post #14 — **yxbot** | 2022-03-23 08:49 UTC _(reply to #11)_

> what the overall impact will be on the metamodel

Looking forward to higher PF ![:grinning:](http://forum.numer.ai/images/emoji/twitter/grinning.png?v=12)

---

### Post #15 — **perfect_fit** | 2022-03-23 11:39 UTC

So beautiful! The core idea sounds weirdly obvious in hindsight, but undoubtably tough to come up with and implement.

Since stake size plays a significant role before regularization, will models with large stakes (1+% of metamodel) have more volatile metrics on TC or even be at a disadvantage? Or does the regularization reduce almost all effect of stake size?

Would you recommend large stakers to spread out the stake over more (diverse) models when optimizing for TC?

---

### Post #16 — **maxchu** | 2022-03-23 11:58 UTC

I hope we can have these metrics’ importance w.r.t. TC in every resolved round to see the dynamics. I am curious about the new TC stacking options, how will it affect mmc importance as the meta-model may become more different from the example model. I am still not sure if i should optimize for mmc directly by the example prediction.

---

### Post #17 — **red_leader** | 2022-03-23 16:30 UTC

I am very excited for these changes. Even if there is a slight dip in NMR value, this is a big step forward for the hedge fund which we all want and need to stick around for a long time :). Also from a profitability stand point, I appreciate that the barrier to entry is rising and that it is strategy related (feature engineering and modeling to optimize TC) not necessarily hardware dependent (looking at you supermassive dataset).

I am wondering though if the team has done any testing and experimentation with the validation set and optimizing TC? Was the above analysis done inclusive of validation eras?

I have mixed feelings about the current validation set for Corr and MMC and so wondering if there are any related changes or improvements down the pipe in this regard?

---

### Post #18 — **mdo** | 2022-03-23 17:36 UTC _(reply to #15)_

I think I answered this here: [Question on TC: Is it True Contribution or something else? - #3 by mdo](<http://forum.numer.ai/t/question-on-tc-is-it-true-contribution-or-something-else/5134/3>)

---

### Post #19 — **qeintelligence** | 2022-03-23 19:03 UTC _(reply to #14)_

no doubt in the end this will happen ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

---

### Post #21 — **sunkay** | 2022-03-24 00:11 UTC

[@mdo](</u/mdo>) Assume someone stake 100 NMR , what’s the differences between stake on (0 x CORR+2xTC) and (1xCORR+2xTC) ?

---

### Post #22 — **thomasxthomas** | 2022-03-24 08:54 UTC

Is this new metric TC robust towards p / (1-p) type of vulnerability?

[Leaderboard Bonus Exploit Uncovered - Tournament - Numerai Forum](<http://forum.numer.ai/t/leaderboard-bonus-exploit-uncovered/200>)

---

### Post #23 — **greyone** | 2022-03-24 11:49 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/aa8b0236319a5b2a756b98232ca464e0f6b70365_2_367x500.png)image790×1075 27.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/aa8b0236319a5b2a756b98232ca464e0f6b70365.png> "image")

  
this makes sense. Outliers like Round 304 Alfaprism_41 corr and mmc in 99 pct and TC in 25pct needs some unpacking.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/576a5413b1a5ef1107f116ec8e23c2f51dc24fec_2_690x346.png)image1421×714 68.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/576a5413b1a5ef1107f116ec8e23c2f51dc24fec.png> "image")

---

### Post #24 — **wigglemuse** | 2022-03-24 14:39 UTC _(reply to #22)_

It is symmetrical (1-p will get exactly opposite TC), and there is no bonus anymore, so shouldn’t be an issue.

---

### Post #25 — **yoshiso** | 2022-03-31 13:21 UTC

Is there any preprocessing for user’s predictions before SWMModel in the production system? In MMC, user’s predictions are converted to uniform distribution but I am wondering the behavior for TC.

Especially whether only rank matters or magnitude matters for TC calculation, and this information is useful for us to understand the TC behavior.

---

### Post #26 — **dzheng1887** | 2022-04-02 17:36 UTC

For those who are commenting that they will likely withdraw from the competition due to the change as their currently optimized model (CORR/MMC) is not suitable for TC, I think that is their intention. Because those models are earning rewards without helping TC/hedge fund performance.

I am fortunately not in that group somehow. I recently checked my model and it would have made 1% more per week if I could stake on 2xTC instead of 2xMMC. It does however increase volatility as others have mentioned, but perhaps for a different reason. I currently have a 2.1 Sharpe with Corr+2xMMC but it will drop to 1.3 with Corr+2xTC. This is mainly due to the lack of correlation between CORR and MMC in my submissions, but a 40% correlation between CORR and TC. Ideally, having some validation diagnostics to historically backtest TC will be helpful if that can be provided in the diagnostic tool.

---

### Post #27 — **pumplerod** | 2022-04-06 03:55 UTC

Will a `train_example_preds.parquet` file, at some point, be provided? If we are interested in modeling an optimization for `Exposurer Dissimilarity` (mentioned in the original post from [@mdo](</u/mdo>) )? For those willing/wanting to build a new tran/validation set via mixing eras from each, it becomes impossible to draw from an existing `example_pred`.

Would a relatively decent equivalent be to use the example model provided to produce predictions for the training set? Or are the `example_preds` in the validation file specially chosen by the Numerai team for a particular reason?

---

### Post #28 — **qeintelligence** | 2022-04-06 20:15 UTC _(reply to #26)_

lol well I will stay skeptical initially and see what will happen with TC rankings and daily/weekly scores for example, I can imagine we will see some huge swings when people start experimenting. At the moment I have a model ranked #11 for TC, yet I have absolutely no clue why this one would be up there so high in the ranking ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

---

### Post #29 — **johnnywhippet** | 2022-04-06 23:21 UTC _(reply to #28)_

Time to get staking! but before you do, tell me about your model… ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=10)

---

### Post #30 — **qeintelligence** | 2022-04-07 18:01 UTC _(reply to #29)_

lol nothing fancy here, its an ensemble of different regression algo’s with the small feature selection, and also only 1/4 of the v2 dataset (1 out of 4 era’s to avoid overfitting).

---

### Post #31 — **johnnywhippet** | 2022-04-07 18:45 UTC _(reply to #30)_

you know, i tried something like that with ElasticNet, Ridge, Lasso and Lars. Nil Nada Niet.

I hope you’re gonna sell those predictions on numerbay, fame and fortune beckons… if you’re in the market for an agent… ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=10)

---

### Post #32 — **qeintelligence** | 2022-04-07 19:42 UTC _(reply to #31)_

Well… be my guest I would say ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=10) : <https://numerbay.ai/product/numerai-predictions/bigcreeper_4>

---

### Post #33 — **taori** | 2022-04-12 08:24 UTC

Maybe this has been already answered somewhere else and I missed that, but How is that the documentation and diagnostic tool still mention `mmc` instead of `tc`? Is there a way to know the `tc` for models not submitted ?

---

### Post #34 — **joakim** | 2022-10-14 09:04 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> we remove the turnover constraint and allow the optimizer a full trading budget to find the optimal portfolio given the Meta Model signal.

[@mdo](</u/mdo>) wouldn’t removing the turnover constraint unfairly benefit ‘faster’ signals, that you actually wouldn’t be able to trade due to the high turnover? In Signals especially it would be easy to create fast high turnover models. If you can’t actually trade the signal though (due to high turnover, which isn’t constrained) then the signal wouldn’t be ‘contributing’ to the portfolio returns, right? Maybe I’m misunderstanding ‘turnover constraint’ in this context?

---

### Post #35 — **wigglemuse** | 2022-10-14 13:38 UTC _(reply to #34)_

Doesn’t the turnover constraint just refer to limitations from stuff they are currently holding (i.e. they can’t turnover their whole portfolio every time they trade) and not some inherent “speed” of certain types of signals? (The removal of this constraint is what I was referring to in the other thread btw when I said TC isn’t computed against the actual Numerai portfolio.) Sure, in signals (or classic), somebody can switch up their model constantly to something else, but it has to be something else _good_ (if they want to benefit from it). And consider that (at the moment anyway) there are two different funds with two different portfolios using two different optimizers but only one metamodel.

The definition of a model “contributing” doesn’t need to be strictly limited to trades the model “recommended” (via its rankings) that _actually happened_ , but to creating via the metamodel a varied menu of good potential trades that the (real full) optimizer can choose from to actually trade that also fit it with the real-world turnover limitations from their current position. (And again, now you’ve got two optimizers doing this for two funds.) In other words, good choices on the menu (that time shows would have worked out well) should be rewarded if they were actually chosen or not. TC is arbitrary enough (from user perspective even if it isn’t really). Reward/punishment differences for what are actually equivalent choices of trades (in terms of “surviving the optimizer” and in ultimate real-world performance) based on _timing_ because of what Numerai happens to be actually holding this week introduces a truly arbitrary/random element (because it is all a black box to us) that would mess up the feedback mechanism. (Because “good” trades would be essentially randomly denied reward or even punished.)

---

### Post #36 — **kayeffnumeraitor** | 2022-10-19 12:07 UTC _(reply to #35)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> In other words, good choices on the menu (that time shows would have worked out well) should be rewarded if they were actually chosen or not.

While this would probably yield a more stable metric, I suspect that it might be too closely related to CORR, which is what Numerai does not want. Instead they want predictions that can be still correlated to the target even after filtering out some of the entries. Otherwise everyone will just optimize for the easiest to retrieve signal that works most of the time. But what happens if exactly this signal is filtered out after all constraints? Then you have something that is random noise or even systematically anti correlated with the target.

For example consider the optimizer decides that all rows with feature_foo_bar not equal to 0.5 cannot be traded because risk is too high. Lets say this feature is most of the time the most correlated one to the target, so most of the users models will like this feature very much and depend heavily on it (Similar to the risky features). But now that this feature is filtered on the remaining predictions are probably trash.

I guess this is the main reason why FNC & exposure related metrics are good proxies for TC.

But I agree that we should not be punished for the black box that comes after our submission. When I think about it, the list of proxy variables are probably the best metrics Numerai could offer to stake on, if TC is what Numerai wants. These variables basically say: If these are high, your ranking recommendations are likely to be surviving the constraint black box and are still yielding profit. This would also decouple the user stakes from the noise of the market, which is something that we as users cannot do something about and should actually be the task of the risk optimizer.

---

### Post #37 — **wigglemuse** | 2022-10-19 21:31 UTC _(reply to #36)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/kayeffnumeraitor/48/991_2.png) kayeffnumeraitor:

> ![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:
>
>> In other words, good choices on the menu (that time shows would have worked out well) should be rewarded if they were actually chosen or not.
> 
> While this would probably yield a more stable metric, I suspect that it might be too closely related to CORR, which is what Numerai does not want. Instead they want predictions that can be still correlated to the target even after filtering out some of the entries. Otherwise everyone will just optimize for the easiest to retrieve signal that works most of the time. But what happens if exactly this signal is filtered out after all constraints? Then you have something that is random noise or even systematically anti correlated with the target.

What I was saying here was just defending what they are already doing with TC, i.e. we already can be rewarded for good choices even if they don’t actually trade them. TC is based on a proxy portfolio created from running the metamodel through the optimizer, but it is not based on their actual trading portfolio, nor should it. (For the reasons I was laying out in previous post that would create unnecessary randomness on our end and make TC even more capricious.)

On the subject of proxy measures, there can’t really be a single true proxy because if there was, then that would just be TC too. Anything correlated with TC (like FNCv3) is only correlated with a subset of the space – for instance nobody should conclude that in order to get good TC you _must_ also get good FNCv3 (or whatever) as that just isn’t true. It just means if you are looking for TC, having high FNCv3 might be one place to find it, but certainly not the only place. As we are discussing in the other thread, you can get high TC just by being “corrective” to some bias in the metamodel but without being a good signal on your own (and without being correlated to anything in particular).

---

### Post #39 — **olivepossum** | 2022-10-29 19:34 UTC _(reply to #27)_

[@pumplerod](</u/pumplerod>) was there any update on this? A few months ago I tried to build them myself by training excluding the era to predict and some adjacent eras to avoid leakage. Then I applied something like this [Optimizing for FNC and TB scores - #32 by olivepossum](<http://forum.numer.ai/t/optimizing-for-fnc-and-tb-scores/5132/32>)

But didn’t have successful results.

---

### Post #40 — **pumplerod** | 2022-10-29 22:56 UTC _(reply to #39)_

Sorry, I tried to delete my post in time because I realized what I was asking isn’t actually something the API provides. I was curious about the correlation of TB_Corr and TC.

I was able to test for a very limited run on one of my models for rounds 322-334 and found that if I looked at a 50% Feature Neutralization against the fncv3_features my Feature Neutralized TB200 corr score correlated with my TC scores to a value of 0.7562. It’s a pretty limited run, so I’m not sure that’s valuable.

---

### Post #41 — **pumplerod** | 2022-10-30 16:52 UTC _(reply to #39)_

[@olivepossum](</u/olivepossum>) I also used that post for some inspiration, though I’m using a TB percentage rather than a strict n (200) samples. I actually showed a reversal in my long negative down-slide of TC when I incorporated this in rounds 322-334, though the current live rounds have me buried and probably setting new records for how terrible a model can perform. So again, after months of feeling positive about this approach, I find myself questioning everything I thought to be true.
