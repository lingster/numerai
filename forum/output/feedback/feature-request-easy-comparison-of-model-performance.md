---
title: "Feature request - Easy comparison of model performance"
category: Feedback
url: https://forum.numer.ai/t/feature-request-easy-comparison-of-model-performance/3383
created_at: 2021-05-22T14:10:57.595000+00:00
last_posted_at: 2021-12-14T01:05:43.035000+00:00
posts_count: 9
views: 1454
tags: []
---

# Feature request - Easy comparison of model performance

---

### Post #1 — **nyuton** | 2021-05-22 14:10 UTC

I often struggle to compare performance of my models. Comparing CORR and MMC model by model is very time consuming.

I found the rainbow chart on the models page useful, but many of my models don’t have 20 weeks of history and I would like to compare them on a CORR + 2xMMC basis as well.

I would suggest to improve the rainbow chart with the following features.

  * add a “from round” input field. So that selected models are displayed and compared for the selected rounds only. (Less than 20 round) This allows easy comparison of new models on the cumulative chart, which have a few rounds of history only.

  * allow CORR+MMC and CORR+2xMMC options as well. These are the metrics we are paid for, thus these give the most comprehensive information.




Thank you

Peter

---

### Post #2 — **jacob_stahl** | 2021-05-22 22:22 UTC

It would also be nice to compare our models with the metamodel’s CORR, so we can use it as a benchmark.

---

### Post #3 — **nyuton** | 2021-05-23 08:47 UTC

[@degerhan](</u/degerhan>) 's script is very helpful for this purpose.  
It would be great if we could get this on the homepage:

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/degerhan/48/3449_2.png)

[Sharpe and Sortino ratios on live performance of your models](<http://forum.numer.ai/t/sharpe-and-sortino-ratios-on-live-performance-of-your-models/1551>) [Data Science](</c/data-science/5>)

> As numerai models only earn or burn when the round is resolved, you may be ignoring the information content of the 20 daily scores in between. The daily gyrations of a model is similar to the daily account value of a buy-and-hold brokerage account. Yes, you don’t realize profit or loss until you sell, yet a slow and steady climb might be more deserving of your hard earned NMRs. More critically, historical daily scores are a high resolution indicator of your model’s volatility under different s…

---

### Post #4 — **aventurine** | 2021-05-25 02:54 UTC

Is this what you might be looking for? <https://dashboard.numeraipayouts.com/>

---

### Post #5 — **bvmcheckking** | 2021-05-25 08:40 UTC _(reply to #4)_

This is great Aventurine, are you the developer behind this? Only thing missing for me is CORR + 2x MMC

---

### Post #6 — **nyuton** | 2021-05-25 09:25 UTC _(reply to #4)_

I’m aware of this dashboard. It’s pretty good, but it doesn’t have cumulative returns. It’s still hard to compare return over let say 10 round. One model is better is some rounds, another model in other rounds. The cumulative return counts most…

---

### Post #7 — **aventurine** | 2021-05-25 16:34 UTC _(reply to #5)_

Not me. I believe [@ia_ai](</u/ia_ai>) did it?

---

### Post #8 — **ml_is_lyf** | 2021-05-25 16:44 UTC

Did you see my post a few weeks back? I added a notebook that pretty much does all this:

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/e56c9b/48.png) [Notebook to visualize historic model performance and see effect of different MMC multipliers and payout factors](<http://forum.numer.ai/t/notebook-to-visualize-historic-model-performance-and-see-effect-of-different-mmc-multipliers-and-payout-factors/3316>) [Tournament](</c/tournament/7>)

> The compare model graphs on our user pages are really helpful for getting an idea of how our models are performing. But they only show cumulative scores, so we don’t see the compounding effect. Also, we don’t see the combined performance of our stake on CORR and MMC, as there is no option to plot CORR+MMC. To bridge this gap I made a notebook to do all of the above. You can tabualise how your model is performing like so: pc.tabualise_performance(model_name="ml_is_lyf", start_round=251, inclu… 

If your point is though that this kind of functionality should be implemented into the website as its easier to access, I agree with that, as you’ll only come across my notebook if you know what you’re looking for.

---

### Post #9 — **ia_ai** | 2021-12-14 01:05 UTC

Just saw this (about 7 months late ![:rofl:](http://forum.numer.ai/images/emoji/twitter/rofl.png?v=10))

<https://dashboard.numeraipayouts.com/> is the result of two community projects:

  * Data from my daily scores collection pipeline (with a simple [CSV output](<https://github.com/woobe/numerati/blob/master/data.csv>)). It is a part of my old dashboard [project](<https://github.com/woobe/numerati>).

  * The cool [dashboard](<https://dashboard.numeraipayouts.com/>) developed by [@ceunen](</u/ceunen>)




So if you need to calculate additional stats like 2xMMC and cumulative returns, you can just download the CSV and play with it. The collection pipeline usually finishes around 30-40 mins after you see the daily-scores bot message in RocketChat.
