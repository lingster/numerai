---
title: "Code to Calculate MMC vs Regular Payouts"
category: Data Science
url: https://forum.numer.ai/t/code-to-calculate-mmc-vs-regular-payouts/238
created_at: 2020-04-22T18:42:30.691000+00:00
last_posted_at: 2020-04-26T13:01:45.402000+00:00
posts_count: 9
views: 3296
tags: []
---

# Code to Calculate MMC vs Regular Payouts

---

### Post #1 — **master_key** | 2020-04-22 18:42 UTC

After my MMC [payout announcement](<http://forum.numer.ai/t/mmc-payout-details-and-analysis/220>) in which I included some payout charts for various users comparing MMC and Regular Payouts, many users have been requesting their own charts, so I’m posting some code to help users generate their own.

First you need to get a pandas.DataFrame that looks like this  
where index is round number, with each round’s correlation and mmc scores as columns.  
This df is called `user_df` in my code.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/25134c39eb5146192258de2aefdee4a395698a12.png)image538×424 12.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/25134c39eb5146192258de2aefdee4a395698a12.png> "image")

You can get a similar DataFrame like this, but might have to rename a column or two.  
(I’m having trouble with this right now but hopefully a user can reply saying how to actually do this correctly)
    
    
    import numerapi
    api = numerapi.NumerAPI()
    user_df = pd.DataFrame(api.daily_submissions_performances("integration_test")).groupby("roundNumber").last()
    

Then running the following code will generate the stakes plot for MMC vs Primary Tourn.
    
    
    end_round=204 # most recent resolved round
    weekly_stakes_corr = {}
    weekly_stakes_mmc = {}
    stake_corr = 1 # initial stake
    stake_mmc = 1
    for r in range(168, end_round):
        if r in user_df.index:
            corr_score = user_df.loc[r, "correlation"]
            mmc_score = user_df.loc[r, "mmc"]
        else:
            corr_score = 0.0
            mmc_score = 0.0
        if corr_score:
                stake_corr *= 1 + corr_score*1
                stake_mmc *= 1 + mmc_score*2 #2x leverage for mmc
        weekly_stakes_corr[r] = stake_corr
        weekly_stakes_mmc[r] = stake_mmc
    
    pd.DataFrame({"corr": weekly_stakes_corr, "mmc": weekly_stakes_mmc}).plot()
    

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a66b279e014b2d1b6ac3ffe22170d16c87d75338.png)image376×267 12.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a66b279e014b2d1b6ac3ffe22170d16c87d75338.png> "image")

This code is slightly simplified because technically the stake selection would be from r-4 but it just makes the code a bit hard to read (r-4 and r+4s everywhere), and this is like 98% similar.

---

### Post #2 — **hb_scout** | 2020-04-22 23:22 UTC

Probably doesn’t happen very often, if ever, but you could include the 25% caps on change in stake as well:
    
    
    stake_corr *= 1 + (max(-0.25,min(0.25, corr_score*1)))
    stake_mmc *= 1 + (max(-0.25,min(0.25, mmc_score*2))) #2x leverage for mmc

---

### Post #3 — **jrdi** | 2020-04-23 08:11 UTC

Thanks for sharing [@master_key](</u/master_key>)! I added a clip (just in case) on (-0.2, 0.2) range for correlation and (-0.25, 0.25) for mmc.

I have been playing around with the code, the results aren’t as good as in [@master_key](</u/master_key>) original post but looks promising.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/c2c3b26f21d1a5b07a714d9fec540023592bf2b7_2_518x500.png)image1159×1118 72.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c2c3b26f21d1a5b07a714d9fec540023592bf2b7.png> "image")

Also some of my new models are developed focusing on MMC (especially “mine4”) so, I would expect that after a few more rounds the numbers improve a bit!

---

### Post #4 — **steppenwolf** | 2020-04-23 10:04 UTC

Hi, [@master_key](</u/master_key>)

Please, keep in mind, that daily_submissions_performances() function returns data in not strictly sorted by date order.

Look at the ‘date’ field in your DataFrame for rounds 176-179, they all have the same date.  
To fix this we should sort rows by date before grouping:

napi.daily_submissions_performances(user)).sort_values(by=‘date’).groupby(“roundNumber”).last()

Maybe this bug can crawl out elsewhere, so be careful!

[![Screenshot 2020-04-23 at 12.52.07](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/9589c9d88631971a3f36b57d870ff49923d3c166_2_690x446.png)Screenshot 2020-04-23 at 12.52.071630×1054 121 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/9589c9d88631971a3f36b57d870ff49923d3c166.png> "Screenshot 2020-04-23 at 12.52.07")

---

### Post #5 — **jrdi** | 2020-04-23 16:38 UTC _(reply to #4)_

[@steppenwolf](</u/steppenwolf>) good point, I also miss it, and plots are affected significantly!

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/c55974db59de94a4a0bb1ebf1f00b94852a653f6_2_518x500.png)image1159×1118 73.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c55974db59de94a4a0bb1ebf1f00b94852a653f6.png> "image")

---

### Post #6 — **jrdi** | 2020-04-26 09:50 UTC

Hi [@master_key](</u/master_key>) there’s something have been bothering me since the announcement of removing the leaderboard bonus and the introduction of the MMC payout. First of all, I understand the decision but I don’t think it will benefit the TOP N as it’s supposed. I have been making some calculation taking as an example niam model (sorry [@mdo](</u/mdo>)) since it’s usually on top 100 and has a huge stake and have been taking profit of the leaderboard bonus for a while.

I computed the return of this model with and without bonus and the difference is obviously huge (+256% vs +67%)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/4a4aadd7db0fd5efd300c43a96d783a8075a5b8e_2_690x419.png)image1161×706 72.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/4a4aadd7db0fd5efd300c43a96d783a8075a5b8e.png> "image")

Since seems that MMC is coming to compensate removing the bonus, let’s see how it looks the payout comparison

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/2418303492f363cbf90a8917ff49a96bf6dbff89_2_690x448.png)image918×597 57.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2418303492f363cbf90a8917ff49a96bf6dbff89.png> "image")

If we take already resolved rounds niam can benefit from jumping to MMC leaderboard (only a 6% increase) but taking into account th,e upcoming rounds it doesn’t… (I know there aren’t resolved yet and the situation can change a lot but still…)

So, a model making huge profits (without exploiting anything) will experience a big cut on his profits once the bonus it’s removed. I’ve been wondering if the time spent on improving my models is going to be worthy.

Do you have any plan to compensate this situation? Or we just should expect a cut in our payouts?

---

### Post #7 — **themicon** | 2020-04-26 11:48 UTC _(reply to #6)_

On your graph 1.6 on the y-axis is a 60% increase from 1.0 not 6%. Or am I not reading this right?

Edit: I also don’t think it’s fair that you used an example model that has a 95% correlation with the metamodel. The original post by [@master_key](</u/master_key>) does also state that 84 out of the top 100 will have better returns using MMC. Did you perhaps pick a model that does not? Have you done the analysis on all the top 100? Does it lead to the same conclusion?

---

### Post #8 — **jrdi** | 2020-04-26 12:55 UTC _(reply to #7)_

You are right, it is not a 6% increase but a 25% at round 204 (the last completely resolved, dotted line), aprox numbers from 1.3 to 1.4 (from 30% to 40%), still far from 250%.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a0ff9d7517242f38a30fe08e23372dd18881fc49.png)image563×366 16.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a0ff9d7517242f38a30fe08e23372dd18881fc49.png> "image")

As far as I understand, they are presenting the MMC payout as a kind of alternative to the leaderboard bonus (or at least it’s what they are doing, removing the bonus and adding the mmc payout), even “dataman_ai” that was taking advantage of the bonus for only a few rounds…

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/7cf9845bbaad14dc9a659f16a97eeeab5a960837_2_690x426.png)image730×451 20.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/7cf9845bbaad14dc9a659f16a97eeeab5a960837.png> "image")

[@master_key](</u/master_key>) statement says 84 out of the top 100 will have better returns using MMC comparing Corr payout vs MMC payout, and not Corr + Bonus payout vs MMC payout, that’s my point here.

---

### Post #9 — **themicon** | 2020-04-26 13:01 UTC _(reply to #8)_

OK, I get what you are doing. I’ve been looking at the MMC vs Corr payout for most of the top MMC models and there are very few that actually get to the 250% mark (which is what you are saying was the expected return for someone with Corr+Bonus in the top 100).
