---
title: "Better LGBM Params, Signals V2 Data, and Reducing Signals Churn"
category: Announcements
url: https://forum.numer.ai/t/better-lgbm-params-signals-v2-data-and-reducing-signals-churn/7638
created_at: 2024-08-06T23:19:38.260000+00:00
last_posted_at: 2024-08-15T19:37:24.552000+00:00
posts_count: 25
views: 2406
tags: []
---

# Better LGBM Params, Signals V2 Data, and Reducing Signals Churn

---

### Post #1 — **ark** | 2024-08-06 23:19 UTC

Numerai has a few high-impact ideas that we would like to immediately disseminate to the community to give you all some time to consider and comment. The topics are as follows:

  * Better LGBM Parameters
  * Signals V2 Data
  * Reducing Signals Churn



## Better LGBM Parameters

The [Atlas Data Release](<http://forum.numer.ai/t/v5-atlas-data-release/7576>) brought with it new validation example predictions that can achieve a correlation Sharpe of 2 on our validation dataset. The way we achieved this performance was with the following LGBM parameters:
    
    
    {
      "n_estimators": 30000,
      "learning_rate": 0.001,
      "max_depth": 10,
      "num_leaves": 1024,
      "colsample_bytree": 0.1,
      "min_data_in_leaf": 10000
    }
    

After grid-searching several parameters, we found that max_depth and min_data_in_leaf had the most impact on improving model performance. You may be able to get better results with your own modeling techniques. When we start accepting Atlas data submissions on September 13, we will also update our examples and tutorials to use these “deep” parameters so that new users can start at a higher level.

## Signals V2 Data

Numerai is planning to release Signals V2 Data this quarter. V2 Data will significantly increase the size of the Signals Universe - a similar update to the Atlas release, but less of a breaking change than Atlas data due to the lack of encryption / obfuscation.

We don’t currently have a timeline on when this universe expansion will occur as it’s still in R&D, but we hope to have it released sometime in September. Something to note here is that the features and targets will change with the universe so it will be a good idea to retrain your models for the new Signals universe as soon as possible.

# Reducing Signals Churn

Churn is a statistic describing how the alpha scores of a signal changes over time. If a submission to Numerai Signals has high churn, then Numerai can’t trade the signal easily. We added a churn statistic to Signals Diagnostics in June 2023 (see [here](<http://forum.numer.ai/t/churn-new-signals-diagnostics-metric/6417>) for details) to help users reduce their churn. Many models built on Numerai data have low churn organically, but Signals Churn is very high. Most Signals models have > 20% week-over-week Churn:

**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/fd2f4b5037418174f62f9035165ed7e52b87e0bd_2_584x303.jpeg)1600×831 90.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fd2f4b5037418174f62f9035165ed7e52b87e0bd.jpeg>)

**

We know that this negatively impacts the churn of the Signals Meta Model because the average individual churn of Signals models is nearly 70% correlated with the Signals Meta Model Churn:

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/7190614cc1dd271bb5894014c357e6496d626a9c_2_436x75.png)946×162 9.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7190614cc1dd271bb5894014c357e6496d626a9c.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/626fa6a03bbfc4514b3ba7db6514203a51df3d87_2_607x311.jpeg)1600×819 106 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/626fa6a03bbfc4514b3ba7db6514203a51df3d87.jpeg>)

Thus the Signals Meta Model’s churn is too high to be useful to Numerai:

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/6cb772191887ad246911a4ff1d18ff81e73bfc73_2_582x411.png)1600×1130 166 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6cb772191887ad246911a4ff1d18ff81e73bfc73.png>)

Signals Meta Model churn is too high.

To lower the churn of the Signals Meta Model, we must lower the churn of all Signals - so we are implementing a strict churn threshold that operates as follows:

  * Any model that has not submitted in the previous week will earn 0 payouts 
    * Any model that does not submit weekly will naturally cause high churn in the Meta Model
  * When you upload a new submission we: 
    * Calculate churn with respect to each of this model’s submissions from the previous week
    * Check if this submission has >= X% churn with respect to any of this model’s accepted submission in the previous week, then this submission will not be accepted - the API will return an error such as “Error: Churn is too high. Submission has Y% churn from [DATE]”



We are going to roll this out over a 2 week:

  1. Start enforcing a threshold of 30% on September 6, 2024
  2. Reduce the threshold to 20% on September 13, 2024
  3. Finally, set the threshold to 10% on September 20, 2024



You’ll notice both our v43.cyrus_plus_teager model and Numerai Meta Model have breached the 10% churn threshold only twice, so we know this is an achievable level of churn that will guarantee a sufficient reduction in overall Signals Meta Model churn.

## FAQs

**How do I know what my churn is?**

We will be open-sourcing the churn calculation we use in diagnostics so that you can calculate it yourself. Then, we will use this calculation to display the new statistic on the Signals website. Any submissions that breaches the threshold will be highlighted as “high churn” in the website.

**When will this churn threshold take effect?**

On September 6, 2024 the threshold will be 30%. On September 13, 2024 the threshold will be 20%. On September 20, 2024 the threshold will be 10%.

**What about Numerai models?**

This does not affect Numerai models as they cannot control their churn level due to the obfuscation of the dataset. Instead, we have crafted a dataset that naturally results in lower-churn models. Signals, on the other hand, can easily reduce their churn because Signals models can easily calculate it. Signals models can be trained to minimize churn just the way we did with our v43.cyrus_plus_teager model.

**What if everyone breaches the threshold?**

This is exceptionally improbable as there will always be a niche for reliably low Signals models. Furthermore, this new mechanic, any round with a large number of models that breach the churn threshold will have a higher payout factor - thus rewarding reliably low churn models.

---

### Post #2 — **ark** | 2024-08-06 23:28 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/ark/48/3156_2.png) ark:

> Check if this submission has >= X% churn with respect to any of this model’s accepted submission in the previous week

One other idea here is using an average instead. This would avoid the scenario in which you are penalized for changing your model or dataset and have a single round with high churn, but low churn other rounds.

---

### Post #3 — **wigglemuse** | 2024-08-06 23:39 UTC

Seems like once in a while an event would occur (some big market event, the world is on fire) where high churn might be the right thing to do. Also, yeah, wanna be able to change up your models. So if you just skip a week (or several weeks), then the first submission after that essentially doesn’t count except to be a “churn marker” for the week after that?

---

### Post #4 — **ark** | 2024-08-06 23:45 UTC _(reply to #3)_

High churn might seem like the right thing to do, but it would make the Signals Meta Model un-tradable. We are really searching for Signals that can withstand these market events and still stay on track.

To answer your question: Yes, if you skip a week or more, the first submission gets no payouts and will be used to calculate churn for subsequent submissions.

---

### Post #5 — **wigglemuse** | 2024-08-07 00:12 UTC _(reply to #4)_

I mean in rare events, a reversal actually might be called for, so if you “outlaw” reversals then it can’t respond to those events. Maybe. Whereas of course just “random” constant week to week churn is undesirable. But imagine if you took the regular dataset and a huge number of rows radically changed their features in a short time period – you’d naturally expect to get radically different predictions all of the sudden. So for signals, where you bring your own data – if your own features have suddenly gone wonky (because pandemic or nuclear meltdown or whatever) the same thing follows. Big changes in the real-world conditions lead to big changes in future prognostications. Again, only at very rare times, but they do happen now and again. Sometimes, the market itself is the leading indicator – all my predictions are wrong suddenly, I want to change them. If people are just dropping weeks, or the system refuses predictions (same effect), doesn’t that itself cause churn? Just musing, feel free to ignore.

---

### Post #6 — **numerologist** | 2024-08-07 03:19 UTC

1. Worst-case 10% churn might sound like overkill. Avg 10% churn can also be too much. How about the best-case churn? I.e. if you are correlated to ANY prediction from the last week 90+% - you should be fine.

  2. Banning submissions sounds cumbersome and harsh. How about incorporating churn into payouts? As a final scale of 0 to 1. Let’s say the baseline is 20% and the total range is 0-40%:



  * If you are at 20% avg churn - your payouts won’t change.
  * If your churn is 10%, you get paid let’s say 1.5 times more (both burns and gains), 0% churn - 2x more.
  * If your churn is 30%, you get paid 0.5 times more. If you’re at 40+%, you get paid 0x times more. No submission rejections, just payout multiplied by 0 for high churn.


  3. Please add the churn metric to the “Scores” page metrics, preferably ASAP so that we can check and discuss thresholds objectively. We can only assume so much about thresholds before we can see live historic performance.  
Ideally, all 3: worst-case churn (against the least correlated submission last week), avg churn, best-case churn (against the most correlated submission last week).

---

### Post #7 — **ark** | 2024-08-07 03:57 UTC _(reply to #6)_

1. This seems too game-able, you could just alternate models in a slot and end up causing very high churn in the meta model, but still pass the test? I’m not sure that achieves our goals.
  2. Banning is harsh, but not cumbersome. An extra multiplier makes it harder to explain how payouts work to users and creates a lot of support burden to direct users to documentation. But a maximum threshold is easy to understand as it will say directly in the error message why it’s failing.
  3. I’ll be adding churn to the website for your convenience, but you will be able to calculate this locally, so it shouldn’t be required to start making lower-churn models.

---

### Post #8 — **gammarat** | 2024-08-07 13:20 UTC

Just out of curiosity, what does the result look like if one applies the churn calculation to the actual historic market returns? And how do those compare to the churn from their contemporary predictions?

---

### Post #9 — **jrai** | 2024-08-07 15:12 UTC

If you’re targeting a metamodel churn with 10%, limiting all of the constituent models to 10% is likely not the best way to get there and still have the best possible metamodel. One of the advantages of Signals is the high variance between underlying submissions. It seems possible that a 15% churn user and a 5% churn user could create a better 10% churn metamodel than two 10% churn users.

Also, I’d guess that dropping user models out by the day that are close to the limit (because their churn was 13% instead of 10%) will be worse for the metamodel’s churn than if you kept those 10-13% user churn models in consistently. Yes, doing a rolling average over N rounds will help smooth this out, but setting the user churn limit so close to the threshold you want and simply rejecting those submissions seems less than ideal. An immediate solution seems like making N sufficiently large and not setting the final threshold so low at 10% (or not at least without first seeing what happens at higher thresholds and allowing things to run for a bit longer than proposed)

As always, the best and simplest way to penalize anything is to penalize in payouts/incentives directly. If someone has a churn >10% for N number of rounds in a row, add some payout penalty? N can be set where the impact of a one time model/strategy change is enough to get a model back to its “steady state” churn.

If the Signals universe is about to expand, will churn also change, and by how much? Why not slow down the pace of the threshold decreases with all of the other changes ongoing?

---

### Post #10 — **numerologist** | 2024-08-07 16:09 UTC _(reply to #7)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/ark/48/3156_2.png) ark:

>   * Banning is harsh, but not cumbersome. An extra multiplier makes it harder to explain how payouts work to users and creates a lot of support burden to direct users to documentation. But a maximum threshold is easy to understand as it will say directly in the error message why it’s failing.
> 


I cannot agree with this one. Payouts are simple - if you are into signals, you **have to** know about churn. If you know you’re high-churn, you **expect** to get paid less. No confusion among anybody.

On the other hand, to require users to build an additional level of their pipeline infrastructure - specifically for signals only - just to handle submission rejections, is a lot more cumbersome than just having a lower payout and later analyzing retrospectively how can churn can be improved. With rejections, you’ll require users to immediately act and likely **will break a lot of pipelines**.

---

### Post #11 — **numerologist** | 2024-08-07 16:21 UTC _(reply to #7)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/ark/48/3156_2.png) ark:

>   * This seems too game-able, you could just alternate models in a slot and end up causing very high churn in the meta model, but still pass the test? I’m not sure that achieves our goals.
> 


This is a tricky question. On the one hand - yes, _theoretically_ it could be possible. On the other hand, it sounds like that sybil attack I found that you didn’t fix yet: it can still be possible, but will anyone bother to actually execute it? The same goes here: do you think people will actually sacrifice good predictions from their best model to actively swap to whatever else they have - sacrificing payouts and maybe actually getting burns in the process - just to “game” the churn? This sounds unlikely to me, but I do see realistic scenarios where I’d want to rearrange models based on the market regime change.

Meaning, if the regime changes and I need to change models (not actively to “game”, but legitimately to shift), the entire week you’ll be rejecting my good predictions - despite they’re legitimately telling you “sell everything you bought ASAP and from now on, buy something else”.

---

### Post #12 — **ark** | 2024-08-07 18:10 UTC

Re: Payout Penalties  
The primary issue with having a payout penalty (rather than rejecting outright) is that users can still submit and profit from high-churn signals - thus raising the Signals Meta Model churn. A good analogy here is back when we had choose-your-own multipliers - there were cohorts of users that coasted on CORR payouts and were never burned for hurting the MM.

Plain and simple: We can’t provide an **option** to submit a high-churn signals and we are willing to break pipelines over this because the **Signals MM churn is broken**.

* * *

Re: [@numerologist](</u/numerologist>)

> do you think people will … “game” the churn?

I don’t think anyone will sacrifice good submissions just to game a churn check - on the contrary, I think high-churn users are probably already “slot swapping” their best models to get the best possible corr/mmc. I don’t think anyone would purposefully game the churn just to stick it to us, but are simply acting in accordance with incentives. If you can make money with high-churn models, then we will get high-churn models.

> if the regime changes … you’ll be rejecting my good predictions

Yes this is true and it’s why I admit the threshold is harsh. However, I think it’s important to consider how we trade the MM. We can only afford a certain amount of turnover in our portfolio each trading day, so during a regime change it doesn’t help to have the MM reverse direction and tell us to trade the opposite - how do we get to the opposite portfolio while minimizing loss? Which stocks should we buy / sell right now? There seems to be a path-dependency issue. The only response I might have to these questions (and maybe you have a better one) is to ensure that the constituent models of the ensemble all handle the regime change smoothly and try to minimize loss as well.

* * *

Re: 10% is too low of a threshold

This is seems very speculative. It could prove out to be correct - leading to lower Signals MM corr or paradoxically lead to higher churn in the MM, but we won’t know until we see what kinds of low-churn models everyone can make. We are tracking these metrics and will react to them if we see the 10% threshold does not lead to a better Signals MM.

The reason why we chose 10% is because our benchmark models are able to achieve this level of churn for very long periods of time. According to the charts above, half the models built on our data also stay around this 10% threshold for long periods of time - and they can’t even optimize for this characteristic, we just built data that leads to lower-churn models. We know Signals models will have a much easier time lowering churn because the data is not obfuscated, so it should be relatively simple to update models to handle churn.

---

### Post #13 — **sandro_niut** | 2024-08-09 13:14 UTC

I can see why the churn limits are wanted, I guess. But one can also argue, once you get a buy signal from the signal meta-model you fdecide what to do. Because another way of saying max 10% churn is: at least 4500 out of around 5000 stocks in the universe atm are equally good or bad to buy today or to buy tomorrow (actually the proposed solution compares this weeks with last weeks–> so friday submission compares with monday 9 days ago–> you want therfore stocks that have very similar signal over 9 days!!!). Does this reflect reality? I doubt, but then I am not with finance-background.

But the implementation does not make sense, rejecting submissions will just mean people find a hacky way to get solutions accepted (like remove just the signals which changed too much, I do not see how such a move takes quality up).

This were my first thoughts after reading this, can elaborate/explain.

---

### Post #14 — **numerologist** | 2024-08-09 19:19 UTC

Another point to consider: there is a user-induced churn, but there is also a Numerai-induced churn.

This is a plot of a week-to-week symmetric difference in tickers (`len(set(era_tickers) ^ set(last_era_tickers))`), v1 data:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d16f6fe8f03bfe85973c2123ff349c88066e726f.png)image570×424 16.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d16f6fe8f03bfe85973c2123ff349c88066e726f.png> "image")

As you can see, some weeks are over 1000 (over ~20%) churn - just on the Numerai side. Meaning, if the 10% churn limit is introduced, it doesn’t matter how good your churn is in these weeks - Numerai will basically say “WE decided to pivot, but YOU are the one who will get rejected for the whole week”.

It also means that if you target a specific market (e.g. US tech stocks) and submit let’s say <500 tickers, you might churn out too just because Numerai swaps on average 74 tickers a week (i.e. with 500 tickers, you are practically guaranteed to hit the 10% churn mark).

As a suggestion: you can incorporate Numerai’s churn into the churn threshold. Meaning, if Numerai enforces a 4% churn, the end-user churn limit could be 14% (10% avg churn + 4% Numerai churn).

Full stats:
    
    
    mean       73.964444
    std        49.387679
    min        16.000000
    25%        56.000000
    50%        65.000000
    75%        79.000000
    max      1111.000000

---

### Post #15 — **ark** | 2024-08-09 21:48 UTC

Universe churn doesn’t affect the submission churn calculation, we filter down to matching IDs and compute churn as 1 - correlation between the remaining predictions.

---

### Post #16 — **joakim** | 2024-08-11 21:26 UTC

Hi [@ark](</u/ark>) , thank you for this! Did you use all the features when you tuned the LGBM? Or the medium subset? And did you train on train and evaluate on val? Or did you use an era walk-forward CV? Or something else? Thanks.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/ark/48/3156_2.png) ark:

> 
>     {
>       "n_estimators": 30000,
>       "learning_rate": 0.001,
>       "max_depth": 10,
>       "num_leaves": 1024,
>       "colsample_bytree": 0.1,
>       "min_data_in_leaf": 10000
>     }
>

---

### Post #17 — **ark** | 2024-08-12 17:06 UTC _(reply to #16)_

We used all features with walk-forward CV to train our v5 benchmarks

---

### Post #18 — **gammarat** | 2024-08-13 05:42 UTC _(reply to #15)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/ark/48/3156_2.png) ark:

> compute churn as 1 - correlation between the remaining predictions

I’ve sort of dropped out of Signals for awhile(time constraints ![:sob:](https://emoji.discourse-cdn.com/twitter/sob.png?v=13) ) but I found this issue interesting as it’s something I was looking at last year. So I adapted a bit of code, and this is what I got. It’s highly simplified and idealized as I didn’t want to spend too much time at it.

  1. I only used the Round 809 live US tickers which also match the EOD names for the same. There’s about 1700 of those.
  2. I used about 21 months of data
  3. I assumed that on a given day I could perfectly predict the rank ordering of the relative returns 20 days later.
  4. I then correlated each (using matLab’s Spearman correlation) with the following day’s similar perfect prediction



Now given those restrictions, I got a mean result (i.e. 1-corr) of around 6.5% exceeding the 10% threshold, with an std of ~2.5%. I guess that will mean it’ll happen pretty frequently once foreign securities, and less stable ones, are added into the mix. So (once/if I get back into Signals) it’s something I’ll have to deal with…

Here’s a plot of the resulting data:  


[![IdealSignalsSubmissionCorrs](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d257d1137116820989b2299f2b54a2bd45f60d7f_2_690x263.jpeg)IdealSignalsSubmissionCorrs1099×420 31.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d257d1137116820989b2299f2b54a2bd45f60d7f.jpeg> "IdealSignalsSubmissionCorrs")

---

### Post #19 — **jrai** | 2024-08-13 12:30 UTC _(reply to #12)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/ark/48/3156_2.png) ark:

> Re: 10% is too low of a threshold
> 
> This is seems very speculative. It could prove out to be correct - leading to lower Signals MM corr or paradoxically lead to higher churn in the MM, but we won’t know until we see what kinds of low-churn models everyone can make. We are tracking these metrics and will react to them if we see the 10% threshold does not lead to a better Signals MM.
> 
> The reason why we chose 10% is because our benchmark models are able to achieve this level of churn for very long periods of time. According to the charts above, half the models built on our data also stay around this 10% threshold for long periods of time - and they can’t even optimize for this characteristic, we just built data that leads to lower-churn models. We know Signals models will have a much easier time lowering churn because the data is not obfuscated, so it should be relatively simple to update models to handle churn.

Since the change hasn’t been made, we’re both speculating. The task isn’t to have people build new low churn models, it is to lower the Signals metamodel overall churn to 10%. Those are similar, but fundamentally different things. If the individual user threshold was 15%, what would the metamodel’s churn be? Given the stats you’re showing that over 50% of signals models have >20% week/week churn, what does the metamodel churn become if you just remove those models (i.e. setting the limit to 20%)?

If you do that analysis, my guess is that 10% is too low of a threshold because there are probably very good models _around_ 10% that will sometimes simply be rejected, ultimately leading to larger metamodel churn. It doesn’t make sense for a user to retrain that model if they are confident in its long term potential. And why would Numerai not want to use that model if it rarely has 13% churn and oftentimes 10%?

If you are cooking a meal that needs the right amount of seasoning, it usually makes sense to add the salt gradually. Similarly, by moving the churn threshold too quickly to 10%, you might be missing the chance to observe and adjust gradually, potentially losing contributions from models that could have performed well with just a bit more flexibility. In any case, 10% may actually be the correct, final threshold, but by immediately (a few weeks is ~immediate) reducing it there, you are giving up an opportunity to see how things adjust, which may create a better metamodel within your predefined limits.

“Show me the incentive and I’ll show you the outcome.” If you’re not penalizing payouts then the natural behavior will be to just submit your model that you’re confident in and if it gets rejected, some users will simply say, “oh well, I guess I can just keep submitting until these get accepted.” Or maybe it’s easier to just start a new model slot fresh. All of these outcomes lead to higher metamodel churn.

---

### Post #20 — **joakim** | 2024-08-14 01:08 UTC _(reply to #19)_

I highly doubt they want their daily target portfolio turnover to be as high as 10%. Probably more like 5%, since the target is 20 days, or lower even since their median holding period is probably double or triple that, and more in line with quarterly reports. I’d say they allow a threshold of as high as 10% for individual Signals, since when combined with other high churn signals, the combined Signal (after optimizer) ideally has a much lower turnover (10 Signals each with 10% daily turnover doesn’t necessarily mean that they would have a completely new portfolio every day, and if it does, those Signals are all quite useless).

I don’t know how much currently they have under management in their fund, but let’s say it’s USD 200 Million leveraged 5x, so 1 Billion in capital. With that much money you couldn’t profitably turn over your portfolio 10% every day. 2% daily maybe (20M)?

Anyway, if your Signal has over 10% daily churn, just take a moving average of the Signal until it’s below the threshold and submit that. Though ideally I think the Signal should be designed to have low turnover in the first place (I.e. less mean reversals, more longer window factors, quarterly earnings surprise factors, changes in analysts’ estimates, etc).

---

### Post #21 — **jrai** | 2024-08-14 16:48 UTC _(reply to #20)_

Isn’t it weekly turnover, not daily? In any case, that’s all fair. My main point is simply that it may make sense to bring the threshold down at a slightly slower pace and observe what the metamodel’s churn does, because you may get to your target turnover (even 5%) with a better metamodel at a higher constituent threshold than you imagine because of the blend of models with high variance in churn. The other point is that it likely makes more sense to penalize churn in payouts directly, but I understand the tradeoff in ease of implementation.

---

### Post #22 — **joakim** | 2024-08-14 21:10 UTC _(reply to #21)_

I would think it’s daily turnover, since they rebalance and trade daily now. We had the same issue on Quantopian back in the day. Some people had some amazing looking backtests but with 50% or higher turnover even (usually some type of mean reversion on a small universe), which isn’t tradable even in a small portfolio (just because someone got filled at a certain price for a certain size doesn’t mean that you would have traded at that price). Trading is expensive, but it’s not usually because of commission, clearing fees, borrowing costs, etc. It’s because of slippage, and if you trade in size you can easily move the market. So the alpha you thought you had wasn’t actually real. On Quantopian I always aimed for less than 5% turnover and as large a universe as possible, and they licensed 8 of my strategies. I doubt they licensed any of the high turnover ones. Same thing here I’d say - High Corr is fairly useless if turnover is also high.

Can’t wait to get back into Signals again! If my v5.0 Tournament models ever finish training that is… ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #23 — **ark** | 2024-08-14 22:46 UTC

Hey all, thank you so much for the comments. I considered all of your arguments, took a second at the data, and decided the following:

  1. set the threshold to 15% and remove the gradual reduction of the threshold. Our goal is to drastically reduce churn of the Signals MM and a low threshold is the only way to ensure this. Removing the gradual reduction of the threshold just simplifies and clarifies this incentive mechanism.
  2. avoid errors in the API - instead set stake to 0 for the round and add website features to explain why users get their stake set to 0 for the round. This will avoid breaking pipelines and allow high-churn users to continue submitting instead of getting errors. It also allows the hedge fund to make intelligent decisions about churn and user filtering.
  3. move the release date to September 20 to give everyone a bit more time. I know 1 month is still a bit short notice, but this is a non-negotiable mandate. We **must** crush Signals churn by the end of September.



I think these changes to the threshold and the release plan will simplify the feature for you all and solve a few problems stated in these comments. I’ll be formally posting a new forum post with the churn release plan and sending an email to notify all signals users.

Thanks for the input,  
ark

---

### Post #24 — **gammarat** | 2024-08-15 03:53 UTC _(reply to #23)_

I just started looking at the Signals 5 validation file data; I thought I could get something from that as I shift to deep learning procedures for Signals from the haphazard mess I had before…  
So I took a look at the correlations in the “target” variable. The full week delay between eras kills that as well; here’s a plot of week to week correlations over roughly the same period you use in the plots above:  


[![Signals050Churn](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e7140109d1f03a6e989c30f6a3819f3a065443e6.jpeg)Signals050Churn560×420 17 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e7140109d1f03a6e989c30f6a3819f3a065443e6.jpeg> "Signals050Churn")

So that’s going to cause problems. I haven’t looked at the other targets yet.

Fwiw, I did run off correlations of 20 day returns with delays of 1 to 5 days on just the American stocks used in the validation file. That looks like this:  


[![SignalsChurn1Small](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f49725b44d90dafcd096c5521d82237a35253afe.jpeg)SignalsChurn1Small560×420 32 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f49725b44d90dafcd096c5521d82237a35253afe.jpeg> "SignalsChurn1Small")

  
with the one day delay in blue at the bottom, moving up to the 5 day delay in green at the top.

The mean and std of the churn (over 2020 to now) with 1 to 5 days delay are:

delay(days) 1 2 3 4 5  
mean 0.068265 0.13125 0.1908 0.24776 0.30186  
std 0.027267 0.049722 0.067465 0.082164 0.094161

The kernel-smoothed density distributions of the churn look like this:  


[![SignalsChurn1Ksd](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1bcb46a7887d2cc5aefd17d108a7e71ec07d8224.jpeg)SignalsChurn1Ksd560×420 14.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1bcb46a7887d2cc5aefd17d108a7e71ec07d8224.jpeg> "SignalsChurn1Ksd")

  
with the same color scheme.

Now TBH, I think the trick here in training might be adapt the target response by looking at the variation in a given ticker return over some number of periods? Maybe that’s in the other validation targets, IDK. But it’s interesting to think about…

---

### Post #25 — **gammarat** | 2024-08-15 19:37 UTC

Just a wee thought here - several years ago now Numerai expanded Val, Train, and Live files from a few hundred features to over a thousand for the Tournament, I suspect by tacking on feature data from 4 or so previous days (or weeks?). I suspect that because when I’d look at the correlations of the target with the features, one would get similar patterns repeated every 210 bins or so. I wrote about that back in 2021:

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gammarat/48/3281_2.png) [Visualizing the New Data](<http://forum.numer.ai/t/visualizing-the-new-data/4067>) [Data Science](</c/data-science/5>)

> So I’ve started looking at the new data, first by looking at the correlations between the features and the targets for the training set. There’s some interesting patterns showing up. By way of process, what I did was take each era, Spearman correlate it with all the available targets. A small percentage of the targets, ~0.25%, had to be cooked (replaced with 0.5) as they were showing up as NaNs. There’s better ways, but that’ll do for now. There’s 21 targets for each era, two of which (“target… 

Anyway, I think I might try something like that with the Signals data, it might help stabilize the predictions. That should keep me out of trouble for awhile ![:laughing:](https://emoji.discourse-cdn.com/twitter/laughing.png?v=14)
