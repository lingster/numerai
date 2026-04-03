---
title: "Decoding the signals target"
category: Signals
url: https://forum.numer.ai/t/decoding-the-signals-target/2501
created_at: 2021-03-22T20:26:58.389000+00:00
last_posted_at: 2021-06-09T08:20:56.968000+00:00
posts_count: 6
views: 2322
tags: []
---

# Decoding the signals target

---

### Post #1 — **degerhan** | 2021-03-22 20:26 UTC

There was an RC discussion as to what the signals target represents.

This notebook [decode_signals_target](<https://gist.github.com/degerhan/72bc2888ef0edf091d81e71378613397>) explores the question. The official target and the rank of 2day-6day (per documentation) returns are 0.71 correlated.

Update:  
The computed field matches 63% of the official targets exactly, and is only one category away (e.g. 0.25 vs 0.50) for 35% of the cases. Only 1.5% are two or more categories away.

I am chalking up the one-category difference to: i) mostly not having as many tickers from yahoo as the numerai internal data, and ii) early-exit criteria in the target for profit-taking and stop-loss. The final 1.5% is likely some Michael Oliver secret sauce.

Conclusion: **key component of the official target is the binned ranked 2day-6day return** , as computed in this notebook.

---

### Post #2 — **sirbradflies** | 2021-06-09 03:39 UTC

Hi Degerhan,  
Thanks for sharing your code, that is very helpful as I am also trying to reverse engineer the target.

I have noticed that you always add a fixed 10 days timedelta to calculate the day of the final results. Is that always the case? If in one week there is an holiday for instance, then if you always publish the results 10 calendar days after it means that you have less trading days and your target will be 5day_2day instead that a 6day_2day right?

Hope the question makes sense. Thanks!

---

### Post #3 — **gammarat** | 2021-06-09 04:01 UTC _(reply to #2)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/sirbradflies/48/2766_2.png) sirbradflies:

> Hope the question makes sense.

It does to me, if that’s any comfort ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) I’ve moved most of my programs to a 2/6 trading schedule from the Tuesday to Monday versions, it just makes life simpler. Now if it would help my scores, I’d feel happier still.

Now if Numer.ai would only be so helpful as to be clear about what they are correlating submissions to—I assume returns,but it’s not clear in the docs—life would be even better. E.g. suppose someone submitted signals that ranged from 0 being _no risk, buy lots_ to 1 being _It’s going down hard!!_ , and 0.5 being _meh_. And suppose the signal was perfect (for the sake of argument).

Now according to the docs, that would be fine. But if they’re correlating against returns, that would be terrible.

---

### Post #4 — **degerhan** | 2021-06-09 06:48 UTC _(reply to #2)_

You are correct, the notebook does not handle market holidays. Took a quick look now, it seems this code will actually not generate a target row for the prediction Friday when target Monday is a holiday (when there is no price for Monday, there is no way to get the prediction Friday by subtracting 10 calendar days).

---

### Post #5 — **sirbradflies** | 2021-06-09 08:04 UTC _(reply to #4)_

Do we know if the targets are based on the 6th trading day after the friday_date or on the following Monday (10 calendar days after friday_date), regardless of the actual trading days in between?

---

### Post #6 — **degerhan** | 2021-06-09 08:20 UTC _(reply to #5)_

I think they likely backfill the price data from the previous market close when Monday is a holiday. They may not be able to finalize scores on Wednesday if they wait for 6 complete trading days.
