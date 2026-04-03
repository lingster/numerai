---
title: "Stake on Signals, vs. Trade Directly"
category: Signals
url: https://forum.numer.ai/t/stake-on-signals-vs-trade-directly/3793
created_at: 2021-07-19T19:36:16.562000+00:00
last_posted_at: 2021-09-28T18:05:41.985000+00:00
posts_count: 21
views: 2670
tags: []
---

# Stake on Signals, vs. Trade Directly

---

### Post #1 — **rigrog** | 2021-07-19 19:36 UTC

As noticed in another thread: what one attempts to predict for Signals, is directly applicable to managing one’s own portfolio. Of course, because that’s what it’s designed for!

So I’m introducing this topic, to sound you all out about relative advantages (how staking is better than trading) and disadvantages (how staking is worse), and perhaps some fundamental differences I’ve not though of.

---

### Post #2 — **sneaky** | 2021-07-19 20:45 UTC

I am primarily Numeraire investor and I think of the gains as an additional edge. If you trade in $ your money are backed by depreciating asset.

---

### Post #3 — **arbitrage** | 2021-07-19 22:41 UTC

with staking, you have none of the following:

transaction costs, borrow fees, margin call risk, prime broker fees, etc.

Sure, you could potentially deploy your model on the live stock market, but I hope you have enough money to buy all the positions your model calls for! Imagine your top long pick is BRK.A!

---

### Post #4 — **aventurine** | 2021-07-19 23:12 UTC

Would be a cool experiment to create model and stake it if corr/mmc looks good and then using a paper trade account and buying say top 10 or 20 highest stock signals sorted out Round start and selling them all round end for several months and seeing what happens

---

### Post #5 — **autratec** | 2021-07-20 04:39 UTC

I feel safe to stake on signals. But looking at the pattern of tournament, not sure how long the payout rate can be sustained. At the end, everything we learned from numerai, should be reapplyed to the live trading environment.

---

### Post #6 — **mattiasl** | 2021-07-20 05:42 UTC _(reply to #5)_

I fully agree.

Every thing is in the cards for a much lower average payout in main tournament (best models will probably get the same), and a higher payout in Signals. Data Scientists will only start staking big in Signal if they think they can make at least the same return over time as in the tournament.

---

### Post #7 — **minou** | 2021-07-20 10:59 UTC _(reply to #4)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/aventurine/48/2333_2.png) aventurine:

> Would be a cool experiment to create model and stake it if corr/mmc looks good and then using a paper trade account

I’ve been doing this for 4 weeks so far on the demo side of my UK spread bet account. Choosing just a few stocks with the highest expected returns to see what the ride might be like. Overall it looks promising but would need a proper backtest, and promising results can fall apart when switching to live, particularly if there’s any discretionary element, which ideally is best avoided.

---

### Post #8 — **objectscience** | 2021-07-20 14:43 UTC

My personal experience has been, it’s ok to use something like the Signals pipeline as an initial filter. If you’re trading small baskets, you could add sanity checks with a secondary trend or regression forecast (I use fbprophet), then optimize your allocation with pyport.

[pypi.org](<https://pypi.org/project/pyportfolioopt/>)

### [Client Challenge](<https://pypi.org/project/pyportfolioopt/>)

[![algs_lt_trend](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/49d32b140397236e5626fa97616be4b42109a55f_2_690x206.png)algs_lt_trend2000×600 84.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/49d32b140397236e5626fa97616be4b42109a55f.png> "algs_lt_trend")

---

### Post #9 — **olivepossum** | 2021-08-14 15:11 UTC _(reply to #3)_

I’ve seen that Alpaca support fractional trading, is commission free (I guess they sell orders to HFT & co.) and the API looks simple.  
Might be a good thing to look into for US stocks.

---

### Post #10 — **olivepossum** | 2021-08-14 15:13 UTC _(reply to #7)_

Which day of the week do you buy/sale/rebalance?

Thanks!

---

### Post #11 — **dev0n** | 2021-08-19 14:53 UTC _(reply to #10)_

I’d like to explore this just to diversify a bit. I think the Signals target change to 20days from 4days will be OK but I know some people are more worried about it. Having a way to monetize your work on a target that works for you is an advantage of direct trading.

So I looked into paper trading on alpaca. My current blocker is that while Alpaca supports fractional shares, they don’t support shorting them, making a long-short portfolio less straightforward. Also, borrow fees over night can be very large (particularly because they short in lots of 100 IIRC).

I wonder if IB is a better option. If anyone knows of a library for maintaining a long/short portfolio (or would want to collaborate on a simple one) please let me know.

---

### Post #12 — **olivepossum** | 2021-08-19 23:49 UTC _(reply to #11)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/dev0n/48/3389_2.png) dev0n:

> 100 IIRC

I know about [this one](<https://github.com/blampe/IbPy>) for IB but have not tried it. [Backtrader](<https://www.backtrader.com/docu/live/ib/ib/>) uses this 3rd party library.

---

### Post #13 — **dev0n** | 2021-08-20 02:11 UTC _(reply to #12)_

Thanks for sharing. It’s too bad it’s been archived/not touched for 5 years. I wonder if there is a good replacement? Or if some of us would be interested in “dusting it off”?

---

### Post #14 — **olivepossum** | 2021-08-21 18:03 UTC

[@dev0n](</u/dev0n>) with the target_20d how would you trade in real live? Would you trade once per week and keep 4 portfolios in parallel with different start dates? (something like what Numerai does on the classic tournament). Each portfolio would be rebalanced every 20d and each week you would be rebalancing one of the portfolios.

The other way I see is to have just 1 portfolio and rebalance every 20d. That has more time risk but it’s simpler to manage.

I guess that independently of how many portfolios, you should hold the securities for 20 days right?

[@mattiasl](</u/mattiasl>) what is your take on this one?

---

### Post #15 — **dev0n** | 2021-08-21 18:06 UTC _(reply to #14)_

Since the overnight borrowing fees were so high (at least on alpaca) I thought of just starting by using my data to train a 1d target and enter after open and exit before close. The offline correlation for 1d looked good, so I am interested to see how it does in paper trading.

---

### Post #16 — **mattiasl** | 2021-08-22 03:46 UTC _(reply to #14)_

[@olivepossum](</u/olivepossum>) if you wanted to trade on the same Numerai signals as you submit to the contest, it would make more sense to allocate a quarter of your capital to each weekly model submission but this requires at least 4x the capital vs beforehand. If having a USD 500k portfolio (100x5k longs and 100x5k shorts) was prohibitive, having 4 x 500k portfolios would be impossible for most people. From a personal investment perspective, I’m wondering whether retaining a single portfolio rebalanced weekly makes more sense, even if Numerai measures its success over 4 weeks.

It’s a velocity of money versus mean return issue. With a fixed gross exposure through the year and zero cost of trading assumption (obviously not what happens in practice), the mean performance of a 4 week holding should be more than 4x as big as the mean performance of a weekly model in order to be at least as profitable at the end of the year. (1 + weekly mean performance mean) ^ 52 vs (1+ 4-week performance mean) ^ ~12.

That said we should all be delighted to move to a 22-2 target from a 6-2 target for the competition as the mean 4 week-return should intuitively be much higher for a 22-2 target than a 6-2 target (there’s more time for anomalies/alpha to resolve). Plus, even really good models are going to have a week or two that bleed like crazy on a 6-2 target. The incidences of having a horrible 4 consecutive week period will probably be lower than having a horrible week on a 4 day measurement. This is important because of the compounding effect on our stakes. A 20% stake loss, requires a 25% profit to come back!

---

### Post #17 — **olivepossum** | 2021-08-22 08:03 UTC _(reply to #16)_

Thanks for the comments!

And what about trading a single portfolio every 20 days? Targets should be easier to predict than the one of 5 days but I guess with 20 days the portfolio is more sensitive to rebalance dates?

---

### Post #18 — **mattiasl** | 2021-08-22 09:25 UTC _(reply to #17)_

You can do that but if you only rebalance once per month (1 month is about 22 trading days), your entire annual performance is derived from only 12 prediction output files which is more risky than speculating on 52 predictions. Your Numerai signals staking performance is going to be based on 52 predictions but if you only speculate with real money on 1 out of 4 of these windows, you might have a very different real average performance, as you might miss out on some of the best or worse 4 week window predictions.

In general, the whole idea with algorithmic trading is that you want have as many trades as you can on as many predictions as possible over a given timeframe. Imagine having an uneven coin where you know you have a 51% edge of winning a coin flip, you are much better off doing 10,000 coin flip bets of USD 10 each than 100 coin flips at USD 100 each. The odds of being a winner after 10,000 coin flips is much great than with only 100 coin flips - even if the overall USD amount at risk is the same.

I’m not 100% sure but I would think that with a limited pool of money, a weekly prediction timeframe is probably more profitable over time if transaction fees are very low.

---

### Post #19 — **olivepossum** | 2021-08-22 10:42 UTC _(reply to #18)_

Thanks [@mattiasl](</u/mattiasl>). One of the things I would like to see is how the predictions behave if I take the risks implied in factors Signals neutralizes against (no clue which they are but some candidates might be volatility, short term reversal, value, size, momentum and sector. My models rely heavily on some of them).  
I might paper trade a weekly rebalanced, 5 day target portfolio using [Alpaca](<https://alpaca.markets/>) and see what happens

---

### Post #20 — **mattiasl** | 2021-08-23 12:37 UTC _(reply to #19)_

Paper trading for a while would definitely make sense.

Other strategies worthwhile considering are just having a long only strategy with just the top 50 or 100 stocks. You could also probably take 15-25% or so leverage on such a portfolio if you used an inverse vol weighting scheme or an Equal Risk Contribution (ERC) scheme (Both of these weighting schemes would create a lower vol and higher sharpe ratio portfolio on average).

---

### Post #21 — **derekam** | 2021-09-28 18:05 UTC

The main (only?) reason that I haven’t tried to do this yet is leverage. Even ignoring broker fees, being stuck in fiat, and the time to build an automated system, Signals staking on 2xCORR3xMMC is effectively “trading” with ~4X+ leverage without the possibility of ever losing more than your initial. This is hard to replicate when generally you can only go 2X buying on margin. The best equivalent would be maybe buying options one month out (for the 20d target), but that adds another layer of volatility and complexity that has to be dealt with. Trying this out manually with the top and bottom 5-10 signals for a few weeks, I’ve quickly run into issues with many of the tickers with the strongest signals being so low-volume that options trading just isn’t reasonable. I can also foresee that with an automated system set up I might be tempted to interfere with it manually at times, which isn’t possible once a stake is locked in and would most likely have negative results.
