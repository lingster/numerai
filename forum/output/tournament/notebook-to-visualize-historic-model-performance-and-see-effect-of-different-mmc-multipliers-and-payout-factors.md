---
title: "Notebook to visualize historic model performance and see effect of different MMC multipliers and payout factors"
category: Tournament
url: https://forum.numer.ai/t/notebook-to-visualize-historic-model-performance-and-see-effect-of-different-mmc-multipliers-and-payout-factors/3316
created_at: 2021-05-16T10:42:39.288000+00:00
last_posted_at: 2021-07-31T21:19:03.590000+00:00
posts_count: 5
views: 1522
tags: []
---

# Notebook to visualize historic model performance and see effect of different MMC multipliers and payout factors

---

### Post #1 — **ml_is_lyf** | 2021-05-16 10:42 UTC

The compare model graphs on our user pages are really helpful for getting an idea of how our models are performing. But they only show cumulative scores, so we don’t see the compounding effect. Also, we don’t see the combined performance of our stake on CORR and MMC, as there is no option to plot CORR+MMC. To bridge this gap I made a notebook to do all of the above.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b25815f604bb07e0cd89ea8bb7ac4e5f1998a335.png) [colab.research.google.com](<https://colab.research.google.com/drive/1_rcTxKYiTt7M88OLx1QS2-HFhkkLyBOD?usp=sharing>) ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/568c419c14aca7a2f68749c9fff9598dd1d7b5e1.png)

### [Google Colab](<https://colab.research.google.com/drive/1_rcTxKYiTt7M88OLx1QS2-HFhkkLyBOD?usp=sharing>)

You can tabualise how your model is performing like so:
    
    
    pc.tabualise_performance(model_name="ml_is_lyf", start_round=251, include_unresolved_rounds=True)
    

roundNumber | correlation | mmc | mmcMultiplier | roundPayoutFactor | roundResolved | roundPerformance | performance  
---|---|---|---|---|---|---|---  
251 | 0.021753 | 0.005382 | 0.0 | 1.000000 | True | 0.021753 | 1.021753  
252 | 0.001437 | -0.007038 | 0.0 | 1.000000 | True | 0.001437 | 1.023190  
253 | 0.045462 | 0.014470 | 0.0 | 1.000000 | True | 0.045462 | 1.068652  
254 | 0.109404 | 0.018124 | 0.0 | 1.000000 | True | 0.109404 | 1.178056  
255 | 0.090115 | 0.005993 | 0.0 | 1.000000 | True | 0.090115 | 1.270132  
256 | 0.091006 | 0.013482 | 0.0 | 1.000000 | True | 0.091006 | 1.363248  
257 | 0.133398 | 0.006555 | 1.0 | 1.000000 | True | 0.139953 | 1.512809  
258 | 0.079414 | 0.011544 | 1.0 | 0.994762 | True | 0.090481 | 1.619401  
259 | 0.034874 | 0.023977 | 1.0 | 0.922645 | True | 0.054298 | 1.688367  
260 | 0.017037 | 0.016032 | 2.0 | 0.922092 | False | 0.045277 | 1.750091  
261 | 0.000008 | 0.020641 | 2.0 | 0.827971 | False | 0.034187 | 1.801810  
262 | 0.031496 | 0.018036 | 2.0 | 0.805855 | False | 0.054450 | 1.889985  
263 | 0.018071 | 0.008058 | 2.0 | 0.769843 | False | 0.026318 | 1.934420  
  
The data is fetched from NumerAPI, except I calculate roundPerformance and performance in the code using the other columns.

For each round,
    
    
    roundPerformance = (correlation + mmc * mmcMultiplier) * payoutFactor
    

and is clipped to the bounds -0.25 and 0.25. So it is the score that is used to calculate our stake return.

Performance is calculated in the same way as 3 month and 1 year return on the leaderboard, we assume a lump sum starting stake of 1, we then calculate how this stake changes over the rounds. The performance for any given round is
    
    
    performance = peformanceFourRoundAgo * roundPerformance + performanceLastRound
    

If fourRoundsAgo is less than start_round, peformanceFourRoundAgo is taken as 1, as this is the starting stake, and similar applies for performanceLastRound.

Interestingly I noticed it looks like the 3 month and 1 year return on the leaderboard are not taking into consideration the roundPayoutFactor. I realized this as round 263 was my first round of seeing my 3 month returns on the leaderboard, and round 251 was my first staked round. But my 3 month return for ml_is_lyf on the leaderboard is 99.2%, and my performance for round 263 calculated above is 1.934420, which is a 93.4420% return. But you’ll notice if I set all the roundPayoutFactor to 1 (as if there was no payout factor) as I do below, then my calculated return is the same as on the leaderboard, with a performance of 1.991507, which is a 99.1507% 3-month return. I’ll make a separate feedback post about this issue.
    
    
    pc.tabualise_performance(model_name="ml_is_lyf", start_round=251, include_unresolved_rounds=True, payout_factor=1)
    

roundNumber | correlation | mmc | mmcMultiplier | roundPayoutFactor | roundResolved | roundPerformance | performance  
---|---|---|---|---|---|---|---  
251 | 0.021753 | 0.005382 | 0.0 | 1 | True | 0.021753 | 1.021753  
252 | 0.001437 | -0.007038 | 0.0 | 1 | True | 0.001437 | 1.023190  
253 | 0.045462 | 0.014470 | 0.0 | 1 | True | 0.045462 | 1.068652  
254 | 0.109404 | 0.018124 | 0.0 | 1 | True | 0.109404 | 1.178056  
255 | 0.090115 | 0.005993 | 0.0 | 1 | True | 0.090115 | 1.270132  
256 | 0.091006 | 0.013482 | 0.0 | 1 | True | 0.091006 | 1.363248  
257 | 0.133398 | 0.006555 | 1.0 | 1 | True | 0.139953 | 1.512809  
258 | 0.079414 | 0.011544 | 1.0 | 1 | True | 0.090958 | 1.619963  
259 | 0.034874 | 0.023977 | 1.0 | 1 | True | 0.058851 | 1.694711  
260 | 0.017037 | 0.016032 | 2.0 | 1 | False | 0.049102 | 1.761649  
261 | 0.000008 | 0.020641 | 2.0 | 1 | False | 0.041291 | 1.824114  
262 | 0.031496 | 0.018036 | 2.0 | 1 | False | 0.067567 | 1.933570  
263 | 0.018071 | 0.008058 | 2.0 | 1 | False | 0.034187 | 1.991507  
  
Aside from that slight digression. I also added functionality to allow you to override your historic mmcMulitplier, for example here I override mine as 2 for all rounds:
    
    
    pc.tabualise_performance(model_name="ml_is_lyf", start_round=251, include_unresolved_rounds=True, mmc_multiplier=2)
    

roundNumber | correlation | mmc | mmcMultiplier | roundPayoutFactor | roundResolved | roundPerformance | performance  
---|---|---|---|---|---|---|---  
251 | 0.021753 | 0.005382 | 2 | 1.000000 | True | 0.032517 | 1.032517  
252 | 0.001437 | -0.007038 | 2 | 1.000000 | True | -0.012638 | 1.019879  
253 | 0.045462 | 0.014470 | 2 | 1.000000 | True | 0.074403 | 1.094282  
254 | 0.109404 | 0.018124 | 2 | 1.000000 | True | 0.145653 | 1.239935  
255 | 0.090115 | 0.005993 | 2 | 1.000000 | True | 0.102101 | 1.345355  
256 | 0.091006 | 0.013482 | 2 | 1.000000 | True | 0.117970 | 1.465670  
257 | 0.133398 | 0.006555 | 2 | 1.000000 | True | 0.146508 | 1.625991  
258 | 0.079414 | 0.011544 | 2 | 0.994762 | True | 0.101965 | 1.752421  
259 | 0.034874 | 0.023977 | 2 | 0.922645 | True | 0.076420 | 1.855233  
260 | 0.017037 | 0.016032 | 2 | 0.922092 | False | 0.045277 | 1.921594  
261 | 0.000008 | 0.020641 | 2 | 0.827971 | False | 0.034187 | 1.977182  
262 | 0.031496 | 0.018036 | 2 | 0.805855 | False | 0.054450 | 2.072601  
263 | 0.018071 | 0.008058 | 2 | 0.769843 | False | 0.026318 | 2.121427  
  
This should help users better understand whether they would benefit from staking on MMC (of course past performance does not necessarily indicate future performance though, so don’t totally rely on this to decide). For instance, as you can see from the above, if I’d staked on 2x MMC from the beginning I would have a 112.1427% 3-month return, so at least for the moment, it seems switching to 2x MMC was a good call for me.

You can also plot performance for multiple models like so:
    
    
    # Replace this list of model_names with the model_names you want to plot
    model_names = ["ml_is_lyf", "ml_is_lyf_1", "ml_is_lyf_2", "ml_is_lyf_3", "ml_is_lyf_4"]
    pc.plot_performance(model_names, start_round=251, include_unresolved_rounds=True)
    

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/cce98eae85bba251abf45b74c697c207d971e50f.png)image454×366 20.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/cce98eae85bba251abf45b74c697c207d971e50f.png> "image")

Note that the roundPerformance of a model that didn’t submit in a given round is 0, hence if you have models that started submitting later like I do, then their performance is 1 until their first submission as the below table shows.

roundNumber | ml_is_lyf | ml_is_lyf_1 | ml_is_lyf_2 | ml_is_lyf_3 | ml_is_lyf_4  
---|---|---|---|---|---  
251 | 1.021753 | 1.000000 | 1.000000 | 1.000000 | 1.000000  
252 | 1.023190 | 1.019722 | 1.000000 | 1.000000 | 1.000000  
253 | 1.068652 | 1.055539 | 1.056875 | 1.050942 | 1.049340  
254 | 1.178056 | 1.162888 | 1.148465 | 1.151440 | 1.181595  
255 | 1.270132 | 1.264500 | 1.236276 | 1.232669 | 1.287270  
256 | 1.363248 | 1.355706 | 1.313295 | 1.304228 | 1.378816  
257 | 1.512809 | 1.507501 | 1.413956 | 1.407881 | 1.552366  
258 | 1.619401 | 1.605970 | 1.528384 | 1.470967 | 1.641629  
259 | 1.688367 | 1.662180 | 1.553643 | 1.501384 | 1.695785  
260 | 1.750091 | 1.724341 | 1.596503 | 1.528973 | 1.704174  
261 | 1.801810 | 1.770446 | 1.648185 | 1.562138 | 1.742399  
262 | 1.889985 | 1.834763 | 1.737652 | 1.663298 | 1.798643  
263 | 1.934420 | 1.871560 | 1.775585 | 1.709448 | 1.822666  
  
And you can also override their MMC multipliers like discussed for tabualise:
    
    
    pc.plot_performance(model_names, start_round=251, include_unresolved_rounds=True, mmc_multiplier=2)
    

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/868b8a7baace70b88066efcb07e32e0c1f57b48a.png)image454×366 22 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/868b8a7baace70b88066efcb07e32e0c1f57b48a.png> "image")

Or even just for individual models if you want:
    
    
    pc.plot_performance(model_names, start_round=251, include_unresolved_rounds=True, mmc_multiplier={"ml_is_lyf_4": 2})
    

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d8be3b6eec7d8a8691f02133a79b9d58bd8e3613.png)image454×366 21.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d8be3b6eec7d8a8691f02133a79b9d58bd8e3613.png> "image")

The payout factor argument also helps you understand how smaller payout factors in the future will affect your model. For instance, if I set it to 3/12, then I can see what the last 3 months would have looked like if there was 1.2 million NMR staked.
    
    
    pc.plot_performance(model_names, start_round=251, include_unresolved_rounds=True, payout_factor=3/12)
    

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/998146819802113e83c121d8fde097590e362875.png)image452×366 21.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/998146819802113e83c121d8fde097590e362875.png> "image")

That’s a very thorough explanation of what you can do with the notebook, but I’ve also added docstrings to the methods too which should explain what the arguments are doing further.

---

### Post #2 — **ml_is_lyf** | 2021-05-16 10:51 UTC

I’ve created a separate post about the issue with leaderboard returns

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/e56c9b/48.png) [Feature request/bug report: Calculate leaderboard returns considering the payout factor](<http://forum.numer.ai/t/feature-request-bug-report-calculate-leaderboard-returns-considering-the-payout-factor/3317>) [Feedback](</c/feedback/2>)

> I noticed that it doesn’t look like the returns on the leaderboard are taking into consideration the payout factor. I discovered this as I wrote a notebook to do the calculations for myself and noticed I get different numbers to the leaderboard unless I override the payout factor as 1 for all rounds. I’m assuming not including it was just an accident as the payout factor is pretty new, but I think it’s pretty important to include it in the calculations for the transparency of the tournament. Mor…

---

### Post #3 — **qeintelligence** | 2021-05-16 13:24 UTC

[@ml_is_lyf](</u/ml_is_lyf>) very nice post and definitely helpful for analysis and such, i would think this would be a nice feature that could also be integrated into the website models page for example.

---

### Post #4 — **ml_is_lyf** | 2021-07-24 11:09 UTC

v2UserProfile got deprecated a few weeks back which broke the old code, I’ve now updated the code to use v3UserProfile

---

### Post #5 — **qeintelligence** | 2021-07-31 21:19 UTC _(reply to #4)_

yes, there were some changes here and there, interestingly enough the other endpoints are still named ‘v2’ which makes it a bit confusing for new people starting to work with the api. I am working on a more complete pbi dashboard which contains a lot of information, not only for selected models but a more complete overview of the classic tournament. Will take some time though before its there ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

btw v2userprofile is still being used, for example at the Models page in numerai
