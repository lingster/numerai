---
title: "The Signals Meta Model Has Been Released: Here Are The Feature Exposures"
category: Signals
url: https://forum.numer.ai/t/the-signals-meta-model-has-been-released-here-are-the-feature-exposures/6626
created_at: 2023-08-20T04:21:18.738000+00:00
last_posted_at: 2023-08-23T20:30:33.205000+00:00
posts_count: 10
views: 2231
tags: []
---

# The Signals Meta Model Has Been Released: Here Are The Feature Exposures

---

### Post #1 — **richai** | 2023-08-20 04:21 UTC

In a recent Live Stream, Numerai released the historical values of the Signals Naive Meta Model. This is a Meta Model which is built by equal weighting all the signals on Numerai Signals (<https://signals.numer.ai>) with a stake >0.1. [Watch the live stream for more details](<https://www.twitch.tv/videos/1902094143>).

Because Signals is all about submitting predictions on raw stock tickers, you can now see the raw values of the Signals Meta Model with a 3 month lag. You can download these simply by signing into Signals and clicking Data to download all data.

I looked at the correlation to some basic Numerai features myself.

Here are 10 features the Signals Naive Meta Model has a lot of correlation with on a recent date:

**Feature, Correlation with Signals MM**  
_Williams %R Indicator, 0.518934_  
Forecast Earnings Volatility, 0.362848  
Volatility of Volume Divided by Price, 0.344192  
Residual Volatility, 0.318293  
Earnings Dispersion, 0.256236  
…

USD Market Cap, -0.444220  
_TRIX, -0.444385_  
_Bollinger Bands, -0.494701_  
_Commodity Channel Index, -0.509648_  
Stock Price (Ranked By Country), -0.535897  
Price to 52 Week High, -0.628304

First of all, you can see there is a lot of correlation with technical indicators (emphasized in italics) on the long and the short side. These features are easy to produce with price data. And since Numerai doesn’t give out data for Signals, many users seem to be using price data in their signals.

The problem with technical indicators such as these is that they are very well known among market participants, and they also tend to be very high churn. A stock could have attractive Williams %R Indicator score in one month and then a very bad score a month later. The problem with this is that trading costs make this signal unmonetizable in a large hedge fund. The trading costs and market impact costs required to trade in an out of the stock quickly would remove the edge.

I would encourage Signals users to try to reduce their reliance on high churn technical features. This will improve your ability to earn TC and decorrelate you from the other signals on Numerai. You can see your churn in Diagnostics.

Another thing you’ll notice is that the Signals Meta Model is heavily short high market cap stocks. It wants to go long small caps and short large caps. Since Numerai neutralizes signals to size before scoring them, taking size exposure like this is unlikely to be rewarded. I don’t think it makes sense for anyone to submit a signal correlated with size or (similar) the stock price.

The Price to 52W High exposure seems especially large (-0.62 correlation). The Signals Naive Meta Model would have a tough time performing well if that feature were to reverse. New models which reduce the exposure to that would probably be very additive here.

I hope this is useful to the Numerai Signals users. And of course, please not there could be many more features which you are correlated with which Numerai can’t detect from our features. This is indeed the point of Signals and since Signals is additive to the Numerai Meta Model it is very likely that many Signals are contributing powerful signals we can’t detect with a simple correlation like this.

Given that the Signals Meta Model produced by hundreds of models is now public, I’m curious to know what other feature correlations can be detected in the signal and what else you can see in it.

---

### Post #2 — **jrai** | 2023-08-20 12:53 UTC

I’m not sure I agree with the idea of releasing the metamodel for Signals (even with a 3 month lag). Ultimately, it may just limit the max quality of signals. If the metamodel is released, now a participant’s signals are no longer just theirs and Numerai’s. As soon as you contribute to the metamodel, your contribution to it is leaked and I’m also not sure if participants agreed to this or had any idea that the metamodel would be released using their historical signals.

It also seems like a possible attack vector. Other funds may think of creative ways to use the historical metamodel data in a way that degrades Numerai’s alpha.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/richai/48/2493_2.png) richai:

> Since Numerai neutralizes signals to size before scoring them, taking size exposure like this is unlikely to be rewarded. I don’t think it makes sense for anyone to submit a signal correlated with size or (similar) the stock price.

How do you square that with the fact that submitting a ranking of market cap would have done extraordinarily well in Signals over a 1.5 year timeframe?  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4ecc2083b53b19d1fad81247efc1b5a44fd05da3_2_690x474.png)image1811×1246 219 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4ecc2083b53b19d1fad81247efc1b5a44fd05da3.png> "image")

  
[Numerai](<https://signals.numer.ai/cc_size>)

---

### Post #3 — **wigglemuse** | 2023-08-20 17:18 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/richai/48/2493_2.png) richai:

> Since Numerai neutralizes signals to size before scoring them, taking size exposure like this is unlikely to be rewarded. I don’t think it makes sense for anyone to submit a signal correlated with size or (similar) the stock price.

Maybe we can actually reverse this logic – since Numerai neutralizes to size (or whatever X), don’t worry about being correlated to that thing, what’s leftover still might be a good signal? Put another way, why is it important to be neutral to things Numerai is going to neutralize for us anyway?

---

### Post #4 — **richai** | 2023-08-20 17:56 UTC _(reply to #2)_

I appreciate the feedback.

I wouldn’t call 0.0026 FNCV4 “extraordinarily well”. A great value for FNCv4 is >0.01. Like one of your other models which is currently the best on this on the leaderboard!

[![Screenshot 2023-08-20 at 10.39.56 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d2ebd70ebd9a426aa13ec35ad639c9348f930e9b_2_690x85.png)Screenshot 2023-08-20 at 10.39.56 AM1646×204 15.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d2ebd70ebd9a426aa13ec35ad639c9348f930e9b.png> "Screenshot 2023-08-20 at 10.39.56 AM")

We neutralize size slightly differently to straight market cap so that could explain why this market cap signal isn’t zero everywhere (but it is close to zero on all of TC, FNCV4 and CORRV4) and might have a mean of zero long term on all of these measures.

The issues you mention are the reason we released the Numerai Meta Model much sooner than Signals. It’s also the reason we released Naive Signals instead of Stake Weight which would make one user account for 22% of the signal and reveal a decent amount of what they’re doing. With Naive Signals Meta Model each signal is only 1/500th of the signal or so and people change and improve their signals all the time so I don’t see it as possible to use the Naive Signal to determine what an individual signal is.

Our goal is to make the Signals Meta Model better and we think there is low hanging fruit to make it better and the best way to show that is to show you what it currently looks like in terms of feature exposures and give you the signal. One of the big complaints from users is not knowing how to get TC or how to be uncorrelated from other signals. Now you know. Do you think this knowledge will be helpful to some users?

Very open to suggestions. We could do a much longer lag in the future? Is there a middle ground you’d like a little more? I don’t think the attack vector is a big deal at all. This signal is not in a steady state at all. Three months from now we could see the -0.62 correlation with price to 52 week high be 0.

---

### Post #5 — **richai** | 2023-08-20 18:00 UTC _(reply to #3)_

I think there’s something to this! When we try testing blending in pre neutralized signals it doesn’t work as well as leaving them more raw. However, although I think it’s fine for individual signals to have say large exposures to things, it would be nice if they aggregated into something at the Signals Meta Model level which was low exposure. For example, if your signal had -0.62 correlation with Price to 52 Week High, then maybe that’s fine for you. But it would be nice if on average at the Meta Model level, the correlation to that went down because we had a far greater number of signals with higher average pairwise correlation.

---

### Post #6 — **jrai** | 2023-08-20 23:37 UTC _(reply to #4)_

I think the main consideration is whether releasing the metamodel caps its performance by the fact that it is released. Although I’m arguing that it would, it very well might not. I can tell you personally, though, that it does impact my willingness to stake on more proprietary data and models. I also feel like I’m being rugged by having the historical signals released without thinking that would have happened.

It’s all well and good to use the metamodel to try to get orthogonal signal or improve upon the metamodel, but if the metamodel is worse to begin with or is being poked/prodded by other market participants, those benefits of releasing the metamodel may not net out.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/richai/48/2493_2.png) richai:

> I wouldn’t call 0.0026 FNCV4 “extraordinarily well”. A great value for FNCv4 is >0.01. Like one of your other models which is currently the best on this on the leaderboard!

But 134% NMR-on-NMR return in 1 year is extraordinary (or at least it probably should be considered extraordinary). And 308.5% in 1.5 years. So if the scores aren’t impressive, but the returns are, then are things incentivized correctly?

![](http://forum.numer.ai/user_avatar/forum.numer.ai/richai/48/2493_2.png) richai:

> One of the big complaints from users is not knowing how to get TC or how to be uncorrelated from other signals.

Being uncorrelated from other signals can be determined from correlation with metamodel (CWMM) statistics on the leaderboard and doesn’t require releasing the raw signal. I like your idea of also releasing max pairwise corr with other models.

Releasing the raw signal also doesn’t necessarily help with TC. You can do everything right, get positive corr20v2, be perfectly orthogonal to the metamodel, optimize all of your hyperparameters, properly purge and embargo your folds with era-wise splits, and still get negative TC. There is no way to know how to get TC, because you can’t train for it. IMO, it’s almost dangerous to suggest to users that there currently are ways to get consistent, positive TC. On average and over time, I would think Numerai wants the users who are properly doing the machine learning, but it seems to me like some of those users are going into unrecoverable drawdowns on TC and will just churn out of the tournament. I think there are other topics on the forum that cover this better.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/richai/48/2493_2.png) richai:

> I don’t think the attack vector is a big deal at all. This signal is not in a steady state at all. Three months from now we could see the -0.62 correlation with price to 52 week high be 0.

Just because the signal is changing doesn’t mean the attack vector isn’t a big deal. It seems more like a binary: either it’s an attack vector or it’s not. Unclear to me, but seems like it’s worth thinking about more closely.

---

### Post #7 — **richai** | 2023-08-21 03:03 UTC _(reply to #6)_

I hear you. I wouldn’t want this to cap the performance.

I think you’re right that it’s binary and don’t think there is an attack vector. But maybe you can describe a procedure (the attack) to determine a user’s signal which has a weight of 1/500th of the Signals Meta Model? If you can show it does leak individual signals, we’d probably stop releasing it.

On the vector of other funds attacking Numerai, if they do think the Signals Meta Model has alpha it definitely won’t have any with a 3 month lag.

And in the current state of it a fund could probably replicate the exposure described quite easy if they had the data in the exposures and they could make a signal with these feature correlations which is quite correlated with Naive Signals but not nearly as good and without much FNCv4.

**Feature, Correlation with Signals MM**  
_Williams %R Indicator, 0.518934_  
Forecast Earnings Volatility, 0.362848  
Volatility of Volume Divided by Price, 0.344192  
Residual Volatility, 0.318293  
Earnings Dispersion, 0.256236  
…

USD Market Cap, -0.444220  
_TRIX, -0.444385_  
_Bollinger Bands, -0.494701_  
_Commodity Channel Index, -0.509648_  
Stock Price (Ranked By Country), -0.535897  
Price to 52 Week High, -0.628304

I agree it’s not great you’ve made 300% on this size signal! It looks like you’ve had to take a lot of risk with 2xFNCv4 and 2xTC to get there. And I wouldn’t personally have much hope this holds up on FNCv4 terms or in TCv2 terms (which will be more aggressive on impact costs).

I agree wholeheartedly we can do more than just show correlation to give better clues about how to get good TC. I like the idea of something like True Return which is simply your own Signal’s performance under our backtest constraints (without all the interaction effects of how you’ll blend with other signals we have). I think uncorrelated signals with large True Return are very likely to have large more durable and predictable TC if their True Return holds up and their correlation stays low. This is an area of research but probably a 2024 thing unfortunately. If you could run True Return style backtests even better but could be insanely costly for us to give unlimited intense historical backtests to everyone. There could be an easier way to do it.

On the Signals Meta Model release if people agree with you or can describe attack vectors, we’d be happy to reconsider. Maybe the CoE can weigh in. My feeling is still this is super additive to the average user still.

---

### Post #8 — **guillem** | 2023-08-22 21:03 UTC

I’ve just seen the Livestream, and I’m excited about the new features/metrics/tools that you talked about to be implemented [@richai](</u/richai>)!

Releasing FIGIs for all tickers and some basic data will be a major upgrade… I spent a lot of time earlier this year trying to map as many tickers as possible from the historical universe to build biass free models. Actually, I used the OpenFIGI API you mentioned, and it seemed to be pretty good with live tickers, but not so good with the full tickers universe. I guess there are a lot of delisted companies and ticker changes in the data maybe? I sent an email about this stuff earlier this year, but never heard back… ![:sweat_smile:](http://forum.numer.ai/images/emoji/twitter/sweat_smile.png?v=12)

Anyway, **I’m attaching a mapping file I created which has FIGIs**. It includes: bloomberg_ticker, company name, ISINs, FIGIs, Share Class FIGI, and Composite FIGI. I haven’t added FIGIs to new tickers since February, but names and ISINs were updated like 3 weeks ago.

There are in total 12,400 FIGIs, but there is a high chance that between 15-25% are wrong. Then, there are 10,000 ISINs, and these are the ones I trust. Among these last ones, the FIGIs should be mostly accurate.

File: <https://github.com/guillemservera/signals-map/blob/4e425933ec6dc54f2238546e710efb8c5f7626d0/signals_map_guillem.csv>

Hope it helps! ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #9 — **richai** | 2023-08-23 20:27 UTC _(reply to #8)_

This is awesome. We can soon give you the best FIGI data we have up until 2021. We can make it better with your help.

---

### Post #10 — **richai** | 2023-08-23 20:30 UTC _(reply to #7)_

Had a call with [@jrai](</u/jrai>) more on this. I think it’s useful to users that we’ve released the Signals Meta Model to date but I agree with [@jrai](</u/jrai>) could be bad if we kept giving it out daily even with a long lag.

Plan going forward which [@jrai](</u/jrai>) likes. We continue to give out the Naive Signals Meta Model file in the download because its fair for everyone to have it but it will stop updating from tomorrow. Thanks for your help thinking through this [@jrai](</u/jrai>).
