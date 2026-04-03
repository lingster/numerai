---
title: "Target Jerome Is Dominating And That's Weird"
category: Data Science
url: https://forum.numer.ai/t/target-jerome-is-dominating-and-thats-weird/6513
created_at: 2023-06-29T20:37:14.893000+00:00
last_posted_at: 2023-07-14T18:46:08.411000+00:00
posts_count: 15
views: 3504
tags: []
---

# Target Jerome Is Dominating And That's Weird

---

### Post #1 — **richai** | 2023-06-29 20:37 UTC

I was going to write an internal email to the team at Numerai but figured I’d share this here.

Numerai uploads our own LightGBM internal models trained on on various targets. We call these Benchmark Models so Numerai data scientists can compare themselves to them and evaluate their performance against them.

Each of the targets on Numerai handle risks in different ways so models trained on them can perform quite differently out of sample. We don’t give all the details on this but the Jerome target handles risks in a more vanilla way than Ralph. Ralph is supposed to be lower risk than Jerome and Cyrus is supposed to be lower risk than Ralph.

When we create targets we aren’t engineering them to be good in sample or anything like that, we are merely trying to reduce risks in the targets in a technical sense. For example, raw return would be a high risk target because it contains factor risks and a lower risk target would take those factor risks out.

Here are the three benchmark models trained on each of the targets. Note the first two are trained on v4 data and Cyrus is trained on v41 data and we don’t currently have a Benchmark Model for Cyrus trained on v4 as it was developed more recently.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f9482d3fe7cc580d19d1d4b35a377c0ec08dc1a4.png) [numer.ai](<https://numer.ai/lg_lgbm_v4_jerome20>)

### [Numerai](<https://numer.ai/lg_lgbm_v4_jerome20>)

[![Screenshot 2023-06-29 at 4.03.19 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/689bbc609f0e8a7568b587a4a05356f361ef6bd9_2_690x386.jpeg)Screenshot 2023-06-29 at 4.03.19 PM2942×1650 291 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/689bbc609f0e8a7568b587a4a05356f361ef6bd9.jpeg> "Screenshot 2023-06-29 at 4.03.19 PM")

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f9482d3fe7cc580d19d1d4b35a377c0ec08dc1a4.png) [numer.ai](<https://numer.ai/lg_lgbm_v4_ralph20>)

### [Numerai](<https://numer.ai/lg_lgbm_v4_ralph20>)

[![Screenshot 2023-06-29 at 4.03.30 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f012253524e7afaec51af24eebc3c3e96eb67e69_2_690x384.jpeg)Screenshot 2023-06-29 at 4.03.30 PM2934×1634 302 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f012253524e7afaec51af24eebc3c3e96eb67e69.jpeg> "Screenshot 2023-06-29 at 4.03.30 PM")

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f9482d3fe7cc580d19d1d4b35a377c0ec08dc1a4.png) [numer.ai](<https://numer.ai/lg_lgbm_v41_cyrus20>)

### [Numerai](<https://numer.ai/lg_lgbm_v41_cyrus20>)

[![Screenshot 2023-06-29 at 4.03.48 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e70d4eb49bb24eef460bbd92d475350867e780ea_2_690x379.jpeg)Screenshot 2023-06-29 at 4.03.48 PM2932×1612 281 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e70d4eb49bb24eef460bbd92d475350867e780ea.jpeg> "Screenshot 2023-06-29 at 4.03.48 PM")

It’s surprising to me that in this challenging period for models on Numerai, that the safer Cyrus model has by far the worst TC ranked 9877th on the leaderboard whereas the Jerome model is ranked 499th in terms of TC. And not only that even on CORR20V2 _which is measured against Cyrus_ the Cyrus model does the worst, Ralph does the second worst and Jerome does the best with a CORR20V2 of 0.0108 (ranking 159th on the leaderboard). This is the opposite order one would expect which presents an interesting anomaly for data scientists to research.

Of course, this is just 1 year of data and that’s not nearly enough time to draw conclusions. Nevertheless it’s interesting to ask:

What techniques would improve drawdowns over the past year?  
How different are the feature exposures in models trained on Cyrus vs models trained on Jerome?  
Do the features which Cyrus models cling to stop working in the recent period?  
Does feature neutralization ([An introduction to feature neutralization / exposure](<http://forum.numer.ai/t/an-introduction-to-feature-neutralization-exposure/4955>)) or era boosting ([Era Boosted Models](<http://forum.numer.ai/t/era-boosted-models/189>)) help in the recent drawdown?  
Are there features which are particularly responsible for 2023’s bad performance?  
Does anyone have a model which does not drawdown or have the same shape as these Benchmark Models in terms of cumulative Cyrus correlation that they’d like to talk about?

Of course, one of the reason Numerai releases so many targets is we want the Numerai community to be able to experiment with many different targets even though we score on the Cyrus target. As you can see in the past year, having some exposure to a model trained on Jerome may have attenuated drawdowns and burns when combined with models trained on other targets.

We’re busy researching even more targets. We hope to release them soon.

---

### Post #2 — **wigglemuse** | 2023-06-30 03:23 UTC

Jerome has always been a good target – for corr anyway. My main model from the v3 data used Jerome as the primary target (but not the only one) and didn’t use nomi at all. And interestingly, that model was always good/consistent at corr and bad/mediocre at TC (probably averaged zero TC, or slightly negative). Retired now so I don’t know how it would have done on recent data.

Still, it isn’t that weird that things don’t stay the same, or they don’t behave the way they did in training – the relationships encoded (inherently) are non-stationary. (I’m guessing, not knowing how they are made.) If neutralizing risk involves assumptions about this being related to that in a certain way…well, that may not stay the same. I’m wondering if some targets are more complex than others which also makes them more brittle (so vanilla methods may be more robust). Is a target that is “less risky” (supposedly) also counting on more relationships between features/returns that need to hold in order for that to be true?

---

### Post #3 — **mlivako** | 2023-06-30 04:58 UTC

What I can conclude when looking at my models in this tough period is that models that are trained on 60d target and on very short period of time and retrained every week are dominating(I have several). The same model trained on way longer period was struggling a lot (going south in terms of TC from May)  
My top model TC rank: 29 Corrv2Rank: 57 and 3M return rank: 5 (at the time of writing) has actually 0 TC correlation with Jerome20 benchmark model and 0.2 CWMM.

Happy to hear thoughts from others

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/df0dfcb4bd2744265f1901215f4fe10caae121c8_2_690x379.jpeg)image2297×1263 208 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/df0dfcb4bd2744265f1901215f4fe10caae121c8.jpeg> "image")

---

### Post #4 — **mrwatson** | 2023-06-30 22:37 UTC _(reply to #3)_

how far back to you go with these models that train only on recent data? how short is very short? [@mlivako](</u/mlivako>)

---

### Post #5 — **jeremy_berros** | 2023-07-01 03:49 UTC _(reply to #3)_

Wdym by “very short period of time” [@mlivako](</u/mlivako>) ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=12)? [@richai](</u/richai>) I can confirm that jerome has been a good target for Corr with my partially neutralized model. However - like [@wigglemuse](</u/wigglemuse>) \- I’ve discontinued it and switched to the new targets over the last few months… In the meantime, my most consistent model has been ranking in the 300-400 lately for Corrv2 using V2 data…

---

### Post #6 — **unsentient** | 2023-07-01 16:32 UTC

Richard, Thank you for open sourcing your internal research! We appreciate it! I’ll be sure to incorporate this information into my own research!

---

### Post #7 — **mlivako** | 2023-07-02 06:31 UTC _(reply to #3)_

I’m considering the exact number be part of my secret sauce but I can tell it is less than year

---

### Post #8 — **thornam** | 2023-07-02 09:18 UTC

Could it be that too many models are trained on Cyrus, such that the MM actually in some sense is overfit to that target? This could potentially explain the higher TC since models trained on Jerome captures some exposure that Cyrus models do not, and maybe explain the higher CORR20v2 because of a potential overfit in MM to a more restrictive/processed target as Cyrus

Personally I have experimented more with different model architectures and have not (yet) experimented with different targets, mostly because the general message have been that Cyrus was the best target to use. But it probably will be wise to do so in the future

---

### Post #9 — **wigglemuse** | 2023-07-02 14:48 UTC _(reply to #8)_

Cyrus is too new for that, only released a few months ago. I would think that models trained primarily on Cyrus are a definite minority.

---

### Post #10 — **taori** | 2023-07-05 12:01 UTC

Without making any speculations, we cannot say anything about CYRUS since it is trained on a different dataset. Regarding RALPH vs JEROME:

  * RALPH has a better CORRV20 as it should
  * CORRV20V2 is better for JEROME, but the models do not train for CORRV20V2 optimization (unless you tell me otherwise) so that is not surprising
  * TC is better for JEROME, which tells us that at least TC is more correlated with CORRV20V2 than CORR20. This is good.



I understand that Numerai built the new targets hoping for better portfolio returns, so the expectation is to see better TC for modles built on the new targets. However that is pure theory, we haven’t seen any proof that TC is working as expected, so there is no reason to be surprised of the results.

It would be interested to see the returns of two hypothetical portfolios: one built on a model trained on RALPH and one built on a model trained on JEROME. If the returns of the portfolio built on JEROME are indeed better than the ones of the portfolio built on RALPH, then we could trust TC (a bit, one test is not really a proof of anything) and it also would mean that the way the new targets are built is not aligned with numerai’s expectation. On the other hand, if the returns of the portfolio built on JEROME are worse than the ones of the portfolio built on RALPH, then we would know TC doesn’t work as expected.

---

### Post #11 — **develuse** | 2023-07-07 07:48 UTC _(reply to #10)_

@RichardCraib, I don’t think the Jerome model should perform worse than risk corrected models. As currently Risk rewards and volatility is low. In times when risk is punished and premiums become negative, I expect Jerome to lose its lead quickly. One who filters out risk, will have less premium in good times. Is that logical?

---

### Post #12 — **numerologist** | 2023-07-07 20:47 UTC

Thank you for sharing this, [@richai](</u/richai>) . Sharing this with the community is a win-win and should definitely bring additional perspective to the table from the outside. So let me share my thoughts, I hope they’ll be of some use to your team.

> When we create targets we aren’t engineering them to be good in sample or anything like that, we are merely trying to reduce risks in the targets in a technical sense. For example, raw return would be a high risk target because it contains factor risks and a lower risk target would take those factor risks out.

Let’s say you have a model trained on raw targets. You have the best picks to buy, you have the best picks to sell. Now, you apply risk adjustment DURING training, hence skewing (to some extent) your buys and sells to be ranked worse. Since the dimensionality of ranking is **fixed** , this, in turn, pushes worse predictions higher for both sells and buys. Given the low-corr (high noise) nature of our models (data), doesn’t it just function as added noise to the already noisy data?

As such, what’s the point of risk-adjusted targets when our predictions are always ranked in a fixed way?

In the long run, for the times like these, it’d be great to have the flexibility to upload either partial predictions or specify the prediction confidence/power instead of plain rank. The technical implementation choice is less important, but the core idea is to be able to say “The market all sucks, I prefer to stay in cash”. Of course, we, as data scientists, can just miss a round, but that would also mean we’re not getting paid for a good prediction not to do anything, plus might have some TC implications.

A few other general suggestions from me:

  1. Said all the above, I do not suggest removing multiple targets. From the entropy reduction perspective, it’s truly awesome that we have multiple targets. I do understand the criticism of having more features/targets is not always better, but it’s not the fault of information theory. It’s just a lot of our models generally suck in extracting information gain + hardware constraints, but I think Numerai does a great job on this front and you can always go with a smaller set / do feature selection as you wish.
  2. Impose less bias on data scientists. As with the example of risk-adjusted targets, it’d be great if most risk-related processing is done in the pipeline AFTER data scientists’ predictions. This splits responsibility: if data scientists suck, we burn. If the fund incorrectly does risk adjustments, the changes are required to be made internally. For example, today, if there is a bad primary target introduced, everyone burns, no matter if they contribute well to the project.  
2.1. The same goes for feature exposure, FNC, and other similar concepts. Let’s say you continue to have fixed-sized predictions but you have something like `TSE:CASH` in your portfolio. In a rare event occasion, you do want to have a skewed exposure, thus assuming or let alone punishing good models for this is a bad idea. Any kind of this type of processing should be done after the submission step, not during training. To be fair, I do understand the motivation behind FNC as it allows us to be best among the average and burn less, but we’re **not** here to be average. ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #13 — **shatteredx** | 2023-07-07 22:38 UTC _(reply to #3)_

yeah my model trained on somewhat recent data only (eras ~600 to 950) has been doing the best lately (3 month return).

---

### Post #14 — **nyuton** | 2023-07-11 09:26 UTC

My model nyuton_test3 could grow during The Big Drawdown.  
It’s trained on Janet20 and uses features (~600) selected using MI with the target.  
Launched in December last year, so no full year of track record yet…

---

### Post #15 — **oraculum** | 2023-07-14 18:46 UTC

It looks like in the recent unresolved rounds some models are having high (±10%) corr with the ‘jerome’ target (and at the same time some of those even have negative correlation with ‘cyrus’ but not that big).  
For example sort this round page by CORJ60 in both direction: <https://numer.ai/round/521>  
That probably shows how much riskier jerome can be, or it’s just a random anomaly or weird models because interestingly the lg_lgbm_v4_jerome20 model trained on jerome doesn’t have this big jerome corr in recent rounds.
