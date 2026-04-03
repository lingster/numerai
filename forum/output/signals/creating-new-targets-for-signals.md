---
title: "Creating new targets for Signals"
category: Signals
url: https://forum.numer.ai/t/creating-new-targets-for-signals/2582
created_at: 2021-03-29T07:19:07.838000+00:00
last_posted_at: 2021-06-20T13:34:19.057000+00:00
posts_count: 5
views: 1186
tags: []
---

# Creating new targets for Signals

---

### Post #1 — **rolanddeschain** | 2021-03-29 07:19 UTC

Hi, I have a question about the Signals target.

Let’s say I have a perfect model to predict the stock returns for any given day, the perfect signal let’s say, so on friday_date I should take the historical data and use the model to predict such returns/signal for which day in the future? is it the next Wednesday? or the one the next week, or is it the first Monday?

I ask because what I want to do is to build a custom target for my ML model, but my target would need to know somehow how far in the future is trying to predict (given the data on friday_date)

Thanks for your time and happy numeraing ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=9)

---

### Post #2 — **jrai** | 2021-03-29 12:50 UTC

Assuming Friday’s price is t0, you probably want to create your target as (t6 - t2) / t2. This is the closest to the “4 day return with 2 day lag” that we can create ourselves.

---

### Post #3 — **autratec** | 2021-06-20 07:54 UTC _(reply to #2)_

General speaking, I feel the hedge fund behind signal tournament is running on weekly chart. So for us, we need to reduce our trading frequency from hour chart, 4hour, daily, to weekly.

And very interesting comments found in document section:

Numerai Signals is not about predicting stock returns, it is about finding original signals that Numerai doesn’t already have.

---

### Post #4 — **gammarat** | 2021-06-20 13:10 UTC _(reply to #3)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/a/6bbea6/48.png) autratec:

> Numerai Signals is not about predicting stock returns, it is about finding original signals that Numerai doesn’t already have.

So they say. But if that is the case, what are they correlating your predictions against in order to determine a score?

---

### Post #5 — **autratec** | 2021-06-20 13:34 UTC _(reply to #4)_

Couple thoughts and assumptions:

Hedge fund was evaluated by relative return, rather than absolute return.  
The traget is related to the relative return to the benchmark.  
The new signal provided by participate will be benchmarked, or correlated with the benchmark.  
No duplicated signal needed, that purpose to go through neutralisation process.  
Those signal/feature with strong correlation with benchmark with higher relative return, but unrelated with existing features will survive.
