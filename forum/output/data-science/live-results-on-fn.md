---
title: "Live Results on FN"
category: Data Science
url: https://forum.numer.ai/t/live-results-on-fn/1369
created_at: 2020-12-25T04:10:28.097000+00:00
last_posted_at: 2020-12-26T15:12:47.556000+00:00
posts_count: 9
views: 1883
tags: []
---

# Live Results on FN

---

### Post #1 — **budbot** | 2020-12-25 04:10 UTC

[![Numerai_Client](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e1d39e8f38ae51c1189ee85fd9578a2a555a3c06.jpeg)Numerai_Client646×431 60.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e1d39e8f38ae51c1189ee85fd9578a2a555a3c06.jpeg> "Numerai_Client")

Hi All,

This post is an analysis comparing 0% and 100% feature neutralization (FN) using the analysis and tips python code for three models across 30 weeks of live data from round 209 to 238.

I decide to write this post following the attention that budbot_7 got for being an early adopter of FN in hope that the community might find it useful. I am not a formally trained data scientist, but I am an engineer who works in a field where poor validation practices can have deadly consequences. I love what the numerai team and community represent. There may be opinions expressed in this post that you disagree with, these comments are made with the utmost respect for the team and community and intended for constructive discussion.

We are going to look at the performance of three models and their 100% neutralized counterparts as per the table below:

Model Designation | Description  
---|---  
ENS | An ensemble model with 0.94 correlation with example predictions.  
ENS_FN | As above, 100% neutralized to features  
EP | Example predictions taken from integration_test_  
EP_FN | As above, 100% neutralized to features  
NN | A simple deep neural network with 0.75 correlation with example predictions  
NN_FN | You should be able to guess what this one is by now  
  
Lets look at a summary of the performance of these models over 30 weeks of resolved rounds from 209 to 238.

[![fig 1](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a8b799df288cecf7d695bd4b39050b90cdbaa5bf.jpeg)fig 1728×217 46.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a8b799df288cecf7d695bd4b39050b90cdbaa5bf.jpeg> "fig 1")

Surprisingly and contrary to validation results, the live corr is slightly higher for the FN models indicating that this period was good for FN models. As expected, the MMC for FN models is significantly higher given their low correlation with the example predictions. If not many other users were using FN models over this time then this makes sense. Remember though that with the attention and recent performance of FN models this is likely to significantly increase adoption which will likely reduce the benefits FN has on MMC for individual users. I’m going to discuss this more later. Corr+2MMC looking very attractive for this period, average 5.3% weekly return for EP_FN if you were able to stake on Corr+2MMC over this period. Pretty amazing for copy and pasting the analysis and tips code and applying it to the example predictions file!!!

[![1fig2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/e86b449a87d80fd9872c10d0bb74a044a0485d69_2_690x205.jpeg)1fig2727×217 48.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e86b449a87d80fd9872c10d0bb74a044a0485d69.jpeg> "1fig2")

[![1fig3](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/9da1369574b9e6e1a036d650e6a5289f125f2000.jpeg)1fig3728×217 41.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/9da1369574b9e6e1a036d650e6a5289f125f2000.jpeg> "1fig3")

With leaderboard bonuses now gone from the tournament the main thing I care about as a user is my models’ long term Sharpe. I want my models to have consistent positive performance and particularly be resilient to burns, even if they “underperform” during the good times. This is what makes FN so attractive to me.

You can see that live Sharpe on corr for the FN models is pretty awesome, being significantly above 1 compared to around 0.6 for the non-FN models. Sharpe on MMC is lower, which is one of the reasons I don’t like MMC. In fairness to the MMC staking mechanism though, which is corr+MMC, this improves Sharpe even further. Note that adding too much MMC (x2) starts to reduce Sharpe again.

So now lets look at what we all care about, how much NMRs would I have if I had staked 1 NMR on each of these models over this period.

[![1fig4](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/371b233053a36f621ceb7c90a1b53835fc1272ae.jpeg)1fig4727×217 40.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/371b233053a36f621ceb7c90a1b53835fc1272ae.jpeg> "1fig4")

I know you can’t just stake on MMC, but I wanted to include this to make the point that if corr is ever removed from staking altogether (as in can only stake on pure MMC) then I’m out. As expected there is no staking scenario that is better for non-FN compared to FN models. Of particular note are the corr + 2 x MMC returns. Again, look at that return on example predictions neutralized, 4.59 NMRs for 1 NMR down in only 30 weeks! I’m a poorer person for staking on corr the whole time.

So based on this analysis you would be silly to do anything other than FN and stake on Corr + 2 x MMC. But be careful. This period has been extremely good for FN. And with the likely increased adoption of FN it may not be as beneficial for MMC in the future.

Even after this analysis I am still going to stake on corr only. Why? Well I just don’t like the concept of single round MMC scoring as a user that aims for realistic corr and high Sharpe and values robust validation practices. The advice for getting good MMC is to do things without trying to focus on MMC. I find this completely unhelpful. Essentially an admission that as a user you can’t apply robust validation practices to MMC so just pray. We are provided with obfuscated data, have no idea what other users are doing, and are staking using a highly volatile cryptocurrency. You take away my ability to apply robust validation to performance with something like MMC and I’m essentially gambling now. As a user this is not something I am willing to put money behind.

Judge me on my long term performance, add in a bonus for originality if you like but don’t potentially punish me for something I have no mechanism to validate and is ever changing.

Thanks to the Numerai team for all their great work. Hope this data is useful to others.

---

### Post #2 — **shonumerai123** | 2020-12-25 10:09 UTC

I’m with you on mmc. It might prove to be more profitable staking strategy but I just feel betting on that is like turning data science into a Keynes’ beauty contest. The increasing popularity of FN is certainly making it less unique as you pointed out.  
If you are confident that your model is unique enough in other perspectives, it could still make sense to bet on mmc of course. I’m not there (yet) unfortunately so I won’t stake on mmc but will keep using FN models for better Corr Sharpe.

Thank you for sharing the thorough analysis!

---

### Post #3 — **nasdaqjockey** | 2020-12-25 13:19 UTC

Great analysis! I feel the same way about MMC, it feels like a shot in the dark. Have you done any analysis by varying the FN PROPORTION parameter?

---

### Post #4 — **objectscience** | 2020-12-25 16:27 UTC

Budbot, do you have any sense for the performance correlation over-time. When I was tracking FN, it seemed to work better when No_FN did poorly, and vice versa. I wonder if there is an argument for splitting risk between the models, 50% exposure on No_FN, 50% on 100_FN, or maybe betting the farm on 50_FN captures both sides?

---

### Post #5 — **lackofintelligence** | 2020-12-25 20:14 UTC

The analysis is great, the comments are pertinent. I am also curious to know about trends, specifically whether fn versus non-fn models flip flop in performance and MMC over time.

---

### Post #6 — **budbot** | 2020-12-25 22:36 UTC _(reply to #3)_

Thanks. I only started doing 50% feature neutralisation in round 227, so don’t really have a good history yet. Will have a quick look and see if there is anything interesting and get back.

I would like to repeat this analysis at 52 weeks and will be able to include some 50% then.

---

### Post #7 — **budbot** | 2020-12-25 22:39 UTC _(reply to #4)_

I now submit 50% and 100% versions of my main models and stake on those. I have limited experience with 50% though as only been submitting since round 227. Anecodotely I really like the 50%.

---

### Post #8 — **budbot** | 2020-12-25 22:59 UTC _(reply to #5)_

[![capture](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/2ffb4f9934bb2a6755e5470a128c5738055a566a_2_690x496.jpeg)capture1021×735 50.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2ffb4f9934bb2a6755e5470a128c5738055a566a.jpeg> "capture")

I don’t know if flip flop is the term I would use, more of a reduction in variance around the mean. I’m sharing this graph of perfromance for the NN only but they all perform the same in my experience. Feature neutralisation just seems to smooth out performance closer to the mean. Note that the mean corr performance is very similar between FN and non-FN.

Correlation between corr for FN and non-FN is resonably high, about 0.75 across most models.

---

### Post #9 — **nasdaqjockey** | 2020-12-26 15:12 UTC

Round 242 I submitted 15 models with 100%. Now all but 1 is 75%. I also use MinMax = 0.01, 0.99. In a good period and most of my models are performing well, where else can you make 2% on your money every week?

I hate there is no good way to validate on past live data. I do what I can with the validation data, working on a new metric using the new Diagnostics.
