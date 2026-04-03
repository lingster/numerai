---
title: "Leverage numerai signal solution in real trading"
category: Signals
url: https://forum.numer.ai/t/leverage-numerai-signal-solution-in-real-trading/3769
created_at: 2021-07-15T09:26:44.688000+00:00
last_posted_at: 2021-08-19T17:16:08.639000+00:00
posts_count: 15
views: 2262
tags: []
---

# Leverage numerai signal solution in real trading

---

### Post #1 — **autratec** | 2021-07-15 09:26 UTC

For those, getting positive CORR in weekly signal submission, did any try it in live trading environment t? For example, you get 30 stocks in the portfolio, and based on the regression result from your model, for those >0.5, you buy 1 lot, less than 0.5, sell 1 lot. and holding for 5 days and restart again.

Did you get similar positive result as you got in signal competition ?

pls help share your experience. thanks.

---

### Post #2 — **gammarat** | 2021-07-15 14:50 UTC

Not yet, but I’m working towards that (in a way). But i’d be interested in hearing others’ thoughts on this.

Here’s some of mine, in no particular order.

It’s summer, I’m very old school, so I really tend towards “Sell in May and go away, come back in on St. Leger’s Day”. While it’s not exactly the best strategy, it does make for a pleasanter life ![:tropical_drink:](http://forum.numer.ai/images/emoji/twitter/tropical_drink.png?v=9)

Right now I have about 14 different different, mostly technical analysis, signals, and I’m putting them through Numerai individually to see the effect of their feature removal, etc.

My signals are actually calculated in terms of relative returns, and also contain a number of tickers that aren’t in the live_universe. The submissions for Numerai are taken from those, cleaned up, and normalized to (0,1), but it would be the relative returns I would trade off of, not the submitted ones.

I had about 5100+ tickers on my last submissions, and I’m not rich enough to trade on all of them ![:laughing:](http://forum.numer.ai/images/emoji/twitter/laughing.png?v=9) Or even very many of them. But most anyway are clustered around an expected return of 0, and/or have a high degree of uncertainty (i.e. conflicting results from different indicators). So those I would ignore.

The ones I am most interested in trading are those that lie roughly in the top or bottom few percent consistently across indicators. I check these out by hand for now, and (unsurprisingly) they are better than I am on my own. That is, of course, a very low bar, but it is promising.

---

### Post #3 — **autratec** | 2021-07-16 01:40 UTC _(reply to #2)_

thanks for the sharing. here is my plan and might take couple days to turn to a program.

I am using MT4 station to pull stock(cdf) data from broker which provided around 300 stock couldb be found in numerai universe. Data with my own indicator will be loaded to AZURE ML for modeling. And API service also provided from AZURE after training being done. I am writing another program based on MT4 and MQL4 language to call Azure ML webservice with live data collected on Friday for those 300 stocks. If the web service return >0.5, then i just buy 0.01 lot, <0.05 then, sell 0.01 lot, hold for one week, close them all and restart again. I might also move to top 5% buy and top 5% sell decision model.

That’s my high level design and working on the coding now. hope can use that program to do some backward data using broker data and see how it goes in last one year.

---

### Post #4 — **gammarat** | 2021-07-16 03:05 UTC _(reply to #3)_

Best of luck! I loved MT4 back when I used it from ~2005-2009, it was pretty easy to work with, had lots of built in tools, and a useful public repository for experimental code. I’ve never worked with Azure, or systems like that, these days it’s just MatLab, more from habit (and good documentation) than anything else. I’d be interested in how it works out.

---

### Post #5 — **mattiasl** | 2021-07-19 14:33 UTC _(reply to #4)_

The real problem is that for most of us the statistical edge of our models is low (~1% spearman rank correlation is what best models have) and the volatility is too high. If you do a long/short model on US stocks for example with the Numerai universe of US stocks (about 2300 stocks), and then decide to go long the top 10 stocks and short the bottom 10 stocks, the outcome might be very different to going long the top 500 stocks and short the bottom 500 stocks. The much larger sample of 500/500 is obviously much more likely to reflect the actual correlations with ground truth of the whole universe that our models are expected to predict.

My view is that the minimum number of stocks required to build a portfolio designed to extract alpha over time is about 100 long / 100 short. Anything less is going to have big mismatches that will cause a lot of volatility. The salient point I’m trying to make is that trading one’s own capital on a 100/100 portfolio portfolio requires at least USD 300,000 - at 300% gross leverage, that represents individual positions of USD 4,500 which is still quite small.

---

### Post #6 — **gammarat** | 2021-07-19 15:24 UTC _(reply to #5)_

That’s probably all true [@mattiasl](</u/mattiasl>), but would anyone interested in trading or investing in just a small number of stocks actually do so on the same basis as a fund trading a large number of stocks on a primarily seeking alpha basis? One size doesn’t fit all.

---

### Post #7 — **liz** | 2021-07-19 16:06 UTC _(reply to #6)_

yeah trading for yourself you can get beta too

---

### Post #8 — **gammarat** | 2021-07-19 17:04 UTC _(reply to #7)_

There’s all sorts of things one can trade on, for small investors. Oneof the best bits of advice I ever got was “If you like the product, look at the stock”. (I think that’s a Warren Buffettism, but I’m not sure). Since I’m a pretty average person, I figure that if I like something, particularly a new product, many others will as well. That’s been the basis of a lot of great trades, from MSFT in the 80s, AMZN, and even Tim Hortons (now QSR). It also means I miss some, like AAPL, but so what? It also means I missed most of the dot-com bubble, and I’m grateful for that.

And it means that when you like, you can play small fast markets that are running short term on developing news, like the gold market during the Iranian Hostage Crisis, or the USD/CAD post Katrina. These effects don’t last long, but when they do it’s profitable to take advantage of them. Trade primarily on historical information, you’ll miss most of those.

---

### Post #9 — **autratec** | 2021-07-19 23:16 UTC _(reply to #5)_

How about we predict the components of etf, like sp500. Base upon the net prediction result to decide buy/sell sp500 at certain volume ?

---

### Post #10 — **aventurine** | 2021-07-20 00:16 UTC _(reply to #9)_

Possibility. Was thinking of doing an S&P stocks only model at some point.

---

### Post #11 — **mattiasl** | 2021-07-20 01:22 UTC _(reply to #10)_

I did start with an SPX stocks only model and started by doing 20 longs and 20 shorts but a single stock having big news (an outlier) had a disproportionate effect on performance. While the mean performances of a 20/20 and 100/100 portfolio should be very close (by definition the 20/20 should be slightly better as the prediction scores are more extreme) the risk/volatility is going to be incomparably better for the 100/100 portfolio (both samples are then large enough that they are more likely going to be close to their sub-population means). Even my 100/100 portfolio returns are quite noisy because my signals models are just not good enough yet! Though they have been making money on a net basis. On a daily Sharpe ratio, it’s not great though.

Numer.ai’s fund should be able to take the top signals submissions and create a meta-model with the same mean return of these top submissions but with a much lower volatility, especially if these models are decorrelated to each other.

By all means, I encourage every contestant to trade their own money on their models (there’s no better to focus the mind on a problem when you stand to lose real cash!), my only point was to say that it’s really difficult to get a good return to risk ratio on a small portfolio.

[@autratec](</u/autratec>) I like your idea though you would probably have to redesign your numer.ai signals targets as these should currently be based on relative rankings and not on absolute performance. Though what you could do with your existing Signals model is to score all the individual components of ETFs and go long/short the ETFs with the biggest score differentials. If QQQ components have a mean score of 0.52 while the SPY components have a mean score of 0.48, it would be a rational trade to go long QQQ vs a SPY short…

---

### Post #12 — **autratec** | 2021-07-20 02:16 UTC _(reply to #11)_

Thanks for sharing new idea here: analysis the components of sp500 and qqq, based on the accumulated prediction score and long short two etf accordingly. It is more effective than buy/sell 200 stocks at same time.

---

### Post #13 — **mattiasl** | 2021-07-20 05:43 UTC _(reply to #12)_

You would probably need to have mean score differences that are big enough to justify such a trade. A real long short strategy would probably go long stocks with scores of 0.55 or more and shorts with scores of 0.45 or less, so does it make sense to do the QQQ/SPY trade if the means are 0.51 and 0.49? I’m not sure!

Also, one would have to consider that these ETFs are market cap weighted and not equal weighted, and that some components are in both indices (AAPL, ADBE etc). Maybe a strategy where the weighted predictions of components is done for all the large ETFs, and then you go long the ETF with the highest weighted prediction and short the lowest. The obvious problem with such a strategy is that you would probably find yourself often in situations where you are long XLK or QQQ (long technology), and short XLU (short utilities). While the cost of trading and stock diversification would be low, the sector concentration risk would be quite high. It might be worth a try - the advantage is that such a strategy is that it can be experimented on in a very small scale.

---

### Post #14 — **autratec** | 2021-08-16 01:41 UTC

Here are some quick update of my experiment of using signal method in my real trading. I start to build a 10 currency portfolio using my leveraged FX trading account and observe the result after one week. The first week result is slide negative. Littlie profit was taken by spread and daily interests (swap). I am fine turning my model and also expand the portfolio to 30 currencies and hope there will be some improvements.

---

### Post #15 — **dev0n** | 2021-08-19 17:16 UTC _(reply to #14)_

See also: [Stake on Signals, vs. Trade Directly](<http://forum.numer.ai/t/stake-on-signals-vs-trade-directly/3793>)
