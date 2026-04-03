---
title: "Longer Signals Target - A Proposal For Higher Payouts"
category: Signals
url: https://forum.numer.ai/t/longer-signals-target-a-proposal-for-higher-payouts/3357
created_at: 2021-05-20T06:39:06.807000+00:00
last_posted_at: 2021-07-02T22:52:08.269000+00:00
posts_count: 26
views: 3086
tags: []
---

# Longer Signals Target - A Proposal For Higher Payouts

---

### Post #1 — **richai** | 2021-05-20 06:39 UTC

We’ve been working on new ways to increase the payouts on Numerai Signals. We want early Numerai Signals users to be able to earn as much as the early Numerai users have.

Recently [@_liamhz](</u/_liamhz>) spoke with [@arbitrage](</u/arbitrage>) [about some early ideas we had on YouTube](<https://www.youtube.com/watch?v=QbxT_0WbJuM>). But currently our best idea to increase payouts on Signals is to increase the horizon of the target from its current _6 days minus the first 2 days_ to _22 days minus the first 2 days_. [Read more about the current 6 day target in docs](<https://docs.numer.ai/numerai-signals/signals-overview#six-day-neutralized-return-targets>).

We analyzed how well all current Numerai Signals users would do if their signals were instead scored against the new longer horizon target. It turns out that most users do much better on the new longer horizon target – even though the new target is still neutral to the same features.

| current target | new target  
---|---|---  
Mean user corr | 0.000801 | 0.003860  
Standard deviation of corr | 0.004622 | 0.005687  
Average corr Sharpe | 0.0495 | 0.2340  
# of users who have higher corr mean on target | 20 | 58  
# of users who have higher corr Sharpe on target | 17 | 61  
  
If we had scored on this new target, the mean correlation with the target would go up 481% but the variance would only increase by only 20% resulting in a much higher average Sharpe for NMR staked on Numerai Signals (0.0495 to 0.2340). It’s important to note that payouts would likely improve even further once we gave out these targets historically, updated the validation diagnostics to show results based on these targets, users optimized their signals to be good at this target, etc.

In the new few days we will be showing a new correlation on Numerai Signals called **CORR20**. This will be your signal’s correlation on the new target.

[![image-6](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/27eb6b62974d275c27bcb85272e6f514fce89bff_2_651x500.png)image-61896×1456 267 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/27eb6b62974d275c27bcb85272e6f514fce89bff.png> "image-6")

  
_how it looks so far, not yet live or finalized_

After it displays on the website, you won’t be able to stake on CORR20 but we want to start showing it so you could get a sense of it.

What do you think of the proposed new target?

Related:  
[see data shared by @degerhan on how different prediction horizons contribute to alpha](<http://forum.numer.ai/t/signals-payout-improvement/3107/3>).  
[see @v1nc3n7’s well-argued proposal for increasing payouts](<http://forum.numer.ai/t/signals-payout-improvement/3107>) (not sure if this is as necessary with longer horizon target).  
I also think there are good reasons to allow 3-4x MMC payouts on Numerai Signals – some, especially some staking on less the whole universe, are very likely to have low volatility signals anyway and would hence benefit from increased MMC leverage.

---

### Post #2 — **aventurine** | 2021-05-20 07:19 UTC

Wow awesome news! Great timing with the signals roundtable coming up today too. This is even more of a motivation to get moving on signals models. Looking forward to learning more tomorrow.

---

### Post #3 — **minou** | 2021-05-20 08:44 UTC

This sounds a great idea Richard; having both the existing CORR6 comp and a CORR20 one might also be attractive for users, and if that were feasible to operate, running like that for at least for some period of time to see what happens and whether it’s beneficial could be worthwhile.

---

### Post #4 — **gund** | 2021-05-20 11:50 UTC

Allowing 3-4x MMC is great to increase payouts, but it also increases risk of high negative return.

One thing important to me with Signals is that staked NMR are blocked only for 10 days, vs 4 weeks on the tournament. Staking on CORR20 wouldn’t be a good thing in that sense.

What about allowing both short-term AND long-term payouts for the same model:

  * after 6 days, payout 2 _CORR6 + x_ MMC
  * after 20 days, payout 2 _CORR20 + x_ MMC  
And let the user choose if he wants to get payout after 6 days only, 20 days only, or both?

---

### Post #5 — **mindyoself** | 2021-05-20 12:40 UTC

This is great for Signals have to start looking into it more.

---

### Post #6 — **senadorancap** | 2021-05-20 13:31 UTC

It’s exactly what I was looking for when signed up for Signals at first time (I’ve discovered Numerai by searching for something like Signals). One week time horizon can be too noisy (the term “noise trader” is there for some reason, right :P) and 4 or 3 weeks is way better. But I still think it’s not enouth, I’m hoping to see even longer targets in the future (like a target for 2 or 6 months, maybe 1 year). Can’t wait to back with my efforts on Signals

Senador cheers!

---

### Post #7 — **arbitrage** | 2021-05-20 13:53 UTC

I tested my measure with a 6-week lag and it was still performant. I expect a longer horizon to be much better from a volatility perspective and a payout perspective. This is a great development!

---

### Post #8 — **bensch** | 2021-05-20 14:27 UTC _(reply to #6)_

Are there data based approaches that can bring you useful predictions on a one year time horizon for individual stocks?

---

### Post #9 — **degerhan** | 2021-05-20 18:17 UTC

I really like this and think it will be a great boost to signals payouts when the scoring switches to corr20. Look forward to the release.

---

### Post #10 — **gund** | 2021-05-21 08:10 UTC

Whatever is the final payout formula, I think Signals deserves to pay a lot more than the tournament because it’s more complex in many ways. For the reasons listed below, it will attract way less users than the tournament, and it will mainly attract experts which expect to be eligible to high rewards.

  * entry cost is much higher: users cannot use a pre-built dataset and train first model in minutes
  * competing is not necessary free: users need to call some API to collect data, which are either free and slow, or faster but not free.
  * once data is collected, we need to spend time to clean and process it in order to build a proper training dataset.
  * each week users have to collect data again, to build the test dataset and its features. This takes both human and computing time, which means $ if you do it on an instance
  * it requires a mix of rare data-science skills and expertise and creativity, which is not the case for the tournament (anyone can submit a model on the tournament after reading a short tutorial on random forests).

---

### Post #11 — **chaotician** | 2021-05-25 00:06 UTC

If your intend is to increase participation in Signals, more than just increasing payout, I think a better track for Numerai is to provide free historical price and fundamental data (FactSet or Morningstar). As gund pointed out, there is a cost in trying to get some meaningful models and this could be a deterrant to prospective participants.

---

### Post #12 — **crownholder** | 2021-05-25 05:38 UTC _(reply to #10)_

I can agree with this because I actually started building a machine on aws but stopped because I determined that at least for now its cost prohibitive.

---

### Post #13 — **gammarat** | 2021-05-25 06:47 UTC _(reply to #10)_

For the financial data there’s a bit of a start up headache to be sure. But after that, it doesn’t seem to be too much of a problem if you’ve settled on a model. I just download data updates from Yahoo once a week (they seem to have about 98% of the live universe tickers, plus lots of other stuff, like indexes, rates, and currencies) and models (once they are stable) should only need marginal adaptation.

Mind you I’m no expert—this is only my second round in Signals (otoh, I have been doing similar stuff since the 90s). And my models do need more work; I checked my submissions and one of the strongest short term buy recommendations was for GME. ![:scream_cat:](http://forum.numer.ai/images/emoji/twitter/scream_cat.png?v=9)

---

### Post #14 — **wander** | 2021-05-26 01:50 UTC

The new scoring might be better for Numerai, but I don’t think it constitutes a higher payout due to the longer compounding period, user orbitalTeaPot on chat came up with some early calculations:

![](https://community.numer.ai/channel/signals/thread/KWz9xkd3KCwwkkCzA/assets/favicon_16.png) [community.numer.ai](<https://community.numer.ai/channel/signals/thread/KWz9xkd3KCwwkkCzA>) ![](https://community.numer.ai/channel/signals/thread/KWz9xkd3KCwwkkCzA/assets/favicon_512.png)

### [Numerai Community](<https://community.numer.ai/channel/signals/thread/KWz9xkd3KCwwkkCzA>)

Hinting at a decrease of between 12% - 25%… had some time to model what that would look like for my 3 main models (BLINKI, INKI and WANDER ) and indeed they have a combined decrease in payouts of about 11% (staking on middle of the ground CORR + MMC ) from round 238, my models are somehow low quality/time invariant so take it with a grain of salt ( yet they’ve been/were in the top 10 ) before signalsgate.

Just my 2cts.

---

### Post #15 — **v1nc3n7** | 2021-05-26 16:47 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/richai/48/2493_2.png) richai:

> [see @v1nc3n7’s well-argued proposal for increasing payouts ](<http://forum.numer.ai/t/signals-payout-improvement/3107>) (not sure if this is as necessary with longer horizon target).

Modifying the payout formula wouldn’t only increase the payouts, but also allow weaker signals to be submitted. In theory, using not only strong signals but also weak signals could improve the metamodel. It seems however, if I understood well, that you currently have difficulties to use weak signals? If it is indeed the case, modifying the payout formula may be of lesser interest.

One concern I have about modifying the horizon to 4 weeks is that you may lose part of the information that you find interesting in Signals models. Are you sure that one reason that Signals models can help to improve the Numerai Classic metamodel isn’t partly because models on both tournaments have different horizons?

---

### Post #16 — **richai** | 2021-05-26 17:08 UTC _(reply to #15)_

We were talking about it yesterday and it seems like a very small change. In your proposal, a -0.03 CORR becoming a -0.03/(1+0.03) = -0.0291 doesn’t seem to be a large enough effect even though I agree with the argument.

That’s a good question – we like how Signals is now in terms of how good the Signals are for helping the fund. And there’s no guarantee that the top Signals users might adjust their models in such a way to do better on CORR20 but actually worse at contributing to our live trading for some other reason. One good thing about optimizing for CORR20 is that it will tend to produce lower churn models but the benefit of that might not offset the cost. Very difficult to say ahead of time – especially with our whole analysis being done on users who don’t yet have the new longer target to train on.

---

### Post #17 — **gammarat** | 2021-05-26 18:45 UTC _(reply to #16)_

Out of curiosity, why not open up a separate Signals20 competition? To me—and I am admittedly very new to Numerai—doing 1 week vs 4 week predictions are quite different kettles of fish.

---

### Post #18 — **gammarat** | 2021-05-27 02:59 UTC

I don’t want to be the proverbial sourpuss, but this just struck me. If people believe that the models they’ve built for the 6-2 competition actually would perform better on a 22-2 basis, wouldn’t it just make more sense for them to hold off submitting a given prediction for several weeks (or alternatively not use data from within two or three weeks of the submission date)?

Or am I missing something? I do tend to do that.

---

### Post #19 — **v1nc3n7** | 2021-05-27 09:51 UTC _(reply to #16)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/richai/48/2493_2.png) richai:

> we like how Signals is now in terms of how good the Signals are for helping the fund. And there’s no guarantee that the top Signals users might adjust their models in such a way to do better on CORR20 but actually worse at contributing to our live trading for some other reason.

What I like about corr20 is that it should probably be easier, we can expect to have a better Sharpe. What I don’t like about it is that our stakes are going to be locked for a way longer time. What would be great is to have a choice between corr4 and corr20. And that could also be interesting on your side, since you would be able to see how much the horizon has an impact on the usefulness of the models for live trading.

Another interesting and fun problem would be to have signals that have good results for both horizons. But that would be more complicated, so it is not really practical.

By the way, you can definitely forget about the modified payout function I was proposing, it is not immune to attacks.

---

### Post #20 — **wigglemuse** | 2021-05-27 16:36 UTC _(reply to #18)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gammarat/48/3281_2.png) gammarat:

> If people believe that the models they’ve built for the 6-2 competition actually would perform better on a 22-2 basis, wouldn’t it just make more sense for them to hold off submitting a given prediction for several weeks (or alternatively not use data from within two or three weeks of the submission date)?

That’s interesting. Since the user is creating their own data, they can actually predict for any future time horizon they want.

---

### Post #21 — **degerhan** | 2021-05-27 17:41 UTC _(reply to #18)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gammarat/48/3281_2.png) gammarat:

> If people believe that the models they’ve built for the 6-2 competition actually would perform better on a 22-2 basis, wouldn’t it just make more sense for them to hold off submitting a given prediction for several weeks (or alternatively not use data from within two or three weeks of the submission date)?

I think we should not evaluate 6-2 models on 22-2 basis. My view is the numerai team confused the issue by making this comparison the primary data point of their corr20 proposal.

What I inferred from Richard at last week’s roundtable is that numerai experimented with an internal model with both corr6 and corr20 targets, and what they saw excited them sufficiently to at least roll out the corr20 display.

Due to my previous (non-numerai) data for predicting ranked-returns of a large stock universe, I believe the relatively small predictive signal accumulates better over 20 days rather than 4 to help rise above the noise.

That said, I think the discussion on which time period works better for either hedge fund or the participants’ payout is premature until we build target20 models, see their corr20 performance, and compare with how life would be different compared to corr6. With 4 weeks for resolution, and maybe at least 10 rounds of live performance, I think we are easily looking at three months before a tournament change decision could be made.

---

### Post #22 — **gammarat** | 2021-05-27 18:11 UTC _(reply to #20)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> Since the user is creating their own data, they can actually predict for any future time horizon they want.

Yes, especially as it is sort of a relative delta {(t6-t2)/t2 sort of thing}, rather than an absolute one.

Thinking about it overnight, it seems the issue opens up a whole range of interesting problems to look at. I’ve mentioned before I spent most of my career in target detection, tracking, and localization (ASW), which is really quite related to the market problem. And in that a significant “similar problem” was over/under estimation of a target track, which in turn is often related to the weighting one gives recent data over older data, given a particular method of analysis. Or it may point more towards using an adaptive prediction method (say, a la Kalman filtering) rather than a static, one off estimate.

Anyway, I’m happy, I enjoy this sort of thing.

---

### Post #23 — **chaotician** | 2021-05-30 14:51 UTC _(reply to #20)_

I agree with this premise. The real added value of Signals is the ability to source your own data that is perhaps not in the 310 obsfucated features in Numerai classic albeit comes with a cost. The models can adjust with any predition time horizon if it’s worth more than salt. So with the DeFi revolution, data prices are starting to come down. So for me a better track to attract crowd source talent is to provide them a pool of free data they can pick and choose from. Then and only then will you see the talent unleash its creativity thus uniqueness!

---

### Post #25 — **mic** | 2021-05-30 22:45 UTC _(reply to #23)_

So would that essentially be the same as the classic tournament, except without the obfuscation?

---

### Post #26 — **chaotician** | 2021-05-31 01:19 UTC _(reply to #25)_

Not necessarily, in the numeraI CLASSIC, we are given 310 features that are obfuscated so we have no idea what there are. We can pluck prices for free with Yahoo but fundamental data from FactSet or Morningstar would be good, also other alternative data like analyst estimates and broker recommendations. Sentiment indicators like Twitter or stocktwits, etc. This is what I mean. I am saying this because of my experience with Quantopian.

---

### Post #27 — **ihab** | 2021-07-02 22:52 UTC

This is a great idea. Awesome! Thank you Richard.
