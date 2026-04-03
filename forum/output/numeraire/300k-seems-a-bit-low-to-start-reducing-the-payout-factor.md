---
title: "300K Seems a bit low to start reducing the payout factor"
category: Numeraire
url: https://forum.numer.ai/t/300k-seems-a-bit-low-to-start-reducing-the-payout-factor/2845
created_at: 2021-04-13T04:55:39.372000+00:00
last_posted_at: 2021-05-16T10:46:51.959000+00:00
posts_count: 6
views: 2890
tags: []
---

# 300K Seems a bit low to start reducing the payout factor

---

### Post #1 — **asteeber** | 2021-04-13 04:55 UTC

I’ve notice that we have started down the steep slope of the payout factor curve. I feel like any token economy wants about half of the circulating supply at stake but that brings the payout factor to 0.12. Now if you’ve got a top dog model averaging 5% CORR every week, that’s still a nice 36% yearly return on stake, but if you’re floating around 2% CORR that’s only 13% return which you can get within many alt-coin ecosystems without having to create a machine learning model.

Wouldn’t it make more sense to push the decline of the payout factor further down (say, 1 million NMR instead of 300K NMR) and put a max on the amount someone can stake? This would control the supply better since compounding interest on re-staked NMR runs away a lot faster than the rate of decrease on the payout factor curve.

But I guess the obvious work-around would be to create a bunch of different accounts… It’s just looking like this tournament is going to have a _huge_ wealth disparity when we reach the max number of NMR that can be minted. Any ideas on how to keep this machine alive for longer? Is the answer in Signals?

---

### Post #2 — **ml_is_lyf** | 2021-04-13 16:49 UTC

I’m not really sure where you got the 36% for 5% CORR and 13% for 2% CORR from. By my math, 2% CORR gives a 146% return a year, and 5% gives a 696% return a year. The way I calculated this is to calculate your stake gain at week n, you multiply your CORR by your stake at week n-4, then you calculate your stake at week n as your gain at week n plus your stake at week n-1. Hopefully, those numbers will reassure you for a start.

With regard to what happens if the payout factor only comes in at 1 million NMR staked, I created a spreadsheet a few days ago to forecast when the treasury runs out. I’ve updated it a bit for this question, but this is how it goes with the payout factor coming in at 300k.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/24c3c84c6dc12f3ffb7aade4b23f1a717650a2ed.png)image979×927 27.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/24c3c84c6dc12f3ffb7aade4b23f1a717650a2ed.png> "image")

So the treasury runs dry in about 6 years assuming we make 69% a quarter.

Here’s what happens when I set the payout factor coming in at 1M.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/9258d7d0a75308f24ae7780715775798dde3d29e.png)image973×917 27.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/9258d7d0a75308f24ae7780715775798dde3d29e.png> "image")

So the treasury runs dry in 2 years.

It’d be crazy if we did return 69% a quarter, so I’d not worry about how many years it will be until it runs out. But importantly if the payout factor comes in at 1M the treasury runs dry 3 times quicker. So setting it to 1M seems like it might not be healthy for the competition.

Capping staking seems to go against the principles of the competition. The high performer’s bubble to the top with no capping. As demonstrated by the 2% vs 5% example for stake after a year. An average 5% CORR has a stake 5 times larger at the end of the year than someone with a 2% CORR (assuming they had the same stake at the beginning of the year). This is desirable as it means high performers have more weight in the meta-model. If you cap it then in the long term the meta-model will approach equal weighting, which Numerai have already said underperforms the stake weighted model.

---

### Post #3 — **pacio** | 2021-04-16 02:29 UTC _(reply to #2)_

So this is a newbie question. What happens when the treasury runs dry? Is the tournament over then? If so, what happens to the value of Numaire? Since the use of Numeraire is exclusive to Tournament and Signal, why wouldn’t its value go to zero?

---

### Post #4 — **themicon** | 2021-04-16 07:33 UTC

We don’t know what happens when the treasury runs out. We are hoping that the hedge fund will be forced to buy NMR on the open market to pay the tournament participants, but we don’t know that for sure. If they do buy NMR on the market, it will certainly keep the price at some level above zero I would hope.

---

### Post #5 — **johnnyjohnny** | 2021-04-16 14:49 UTC

If they wanted to slow the speed at which the treasury runs out, while also providing a clear signal that they plan to support NMR in the long term, they could have a shifting percentage of the NMR rewards that come from the treasury vs from Numerai the company buying them on the market. The percentage that comes from the treasury could be 100% in 2021, 90% in 2022, etc.

---

### Post #6 — **ml_is_lyf** | 2021-05-16 10:46 UTC

People in this thread who are concerned about payout factor might be interested in a notebook I created. You can replay your historic model performance with different payout factors to see how it affects your payouts.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/e56c9b/48.png) [Notebook to visualize historic model performance and see effect of different MMC multipliers and payout factors](<http://forum.numer.ai/t/notebook-to-visualize-historic-model-performance-and-see-effect-of-different-mmc-multipliers-and-payout-factors/3316>) [Tournament](</c/tournament/7>)

> The compare model graphs on our user pages are really helpful for getting an idea of how our models are performing. But they only show cumulative scores, so we don’t see the compounding effect. Also, we don’t see the combined performance of our stake on CORR and MMC, as there is no option to plot CORR+MMC. To bridge this gap I made a notebook to do all of the above. You can tabualise how your model is performing like so: pc.tabualise_performance(model_name="ml_is_lyf", start_round=251, inclu…
