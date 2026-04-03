---
title: "Numerai Crypto TB100 and Statistical Risk Model"
category: Data Science
url: https://forum.numer.ai/t/numerai-crypto-tb100-and-statistical-risk-model/7835
created_at: 2024-11-07T20:24:23.171000+00:00
last_posted_at: 2024-11-08T20:53:47.003000+00:00
posts_count: 8
views: 953
tags: []
---

# Numerai Crypto TB100 and Statistical Risk Model

---

### Post #1 — **jefferythewind** | 2024-11-07 20:24 UTC

**Introduction**

Following up on some exploratory work on simulating portfolios built from Numerai’s crypto meta model, I wanted to investigate a **statistical risk factor model** for the crypto market and apply the model to more realistic backtest of the **TB100 portfolio**. This is largely unexplored territory but there are several precedents coming from traditional portfolio theory applied to the equity market, from where I draw most of the tools here.

**TB100 Portfolio**

The “TB100” stands for “top and bottom 100”, which means to go long and short the top and bottom 100 assets each round, sorted by meta model score. Here is a portfolio simulation of this strategy. On each day we initiate equally weighted positions, long and short, which last for 20 days (the duration of our prediction targets).

[Previously I had made a simplified version of the backtest for the TB10 simulation](<http://forum.numer.ai/t/numerai-crypto-tb10/7828>), where on each day we assume we earn the future 20 day log returns of each position. Keeping the position weights correct allows us to simulate this return stream which should be attainable in real life.

> One thing to note is that we can only simulate tickers for which we have data (from Yahoo) and also we require to have the data for the 600 preceeding days of each trading date, in order to create our statistical risk model in the next section.

[![Screenshot 2024-11-07 at 1.52.21 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b2ef7c4bda02a1591b119d827732878a03f6528e_2_592x500.jpeg)Screenshot 2024-11-07 at 1.52.21 PM1220×1030 75 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b2ef7c4bda02a1591b119d827732878a03f6528e.jpeg> "Screenshot 2024-11-07 at 1.52.21 PM")

However this simulation falls short of clearly defining entry and exit prices, a portfolio cash account and positions, and the effect of overlapping 20 day trading periods. Because of this I put together a backtest which simulates trades and exact portfolios based on the close prices and meta model signal every day, **in such a way that should replicate _the idea_ from the simulation of log returns above**. Here we plot the portfolio value, assuming the initial investment is **1.0**.

[![Screenshot 2024-11-07 at 1.53.51 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d9696b2a14a7eeb2e98d128ddb7c73abb958dabb_2_646x500.jpeg)Screenshot 2024-11-07 at 1.53.51 PM1136×878 55.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d9696b2a14a7eeb2e98d128ddb7c73abb958dabb.jpeg> "Screenshot 2024-11-07 at 1.53.51 PM")

Here we get about 9% return instead of the theoretical 14% above. But this is now realistic, where we can track individual transactions throughout the simulation.

With this simulation we can also monitor things like cash account position and total portfolio leverage. We know from brief inspection that this portfolio makes most of the money short selling, and the crypto assets move a lot, so this greatly affects the leverage of the portfolio without and adjustments. The cash account stays at 1.0 for 20 days until our first round of trades expires, since each day we enter into equally weighted new positions, the new positions do not affect the cash account.

[![Screenshot 2024-11-07 at 2.24.03 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/53f8810b65d03a658c729544be665f80582ed286_2_644x500.png)Screenshot 2024-11-07 at 2.24.03 PM1140×884 59.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/53f8810b65d03a658c729544be665f80582ed286.png> "Screenshot 2024-11-07 at 2.24.03 PM")

[![Screenshot 2024-11-07 at 2.24.53 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8cfe528e1431fbe6130df6fbe66d7dcfc0c14a0d_2_625x500.jpeg)Screenshot 2024-11-07 at 2.24.53 PM1110×888 55.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8cfe528e1431fbe6130df6fbe66d7dcfc0c14a0d.jpeg> "Screenshot 2024-11-07 at 2.24.53 PM")

We also record the portfolio weights at each date and can then compute the churn of this portfolio over time.

[![Screenshot 2024-11-07 at 2.25.37 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/7fcf49bcd8cbc548d71cfaf22e36297f19720ffc_2_621x500.jpeg)Screenshot 2024-11-07 at 2.25.37 PM1124×904 70.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7fcf49bcd8cbc548d71cfaf22e36297f19720ffc.jpeg> "Screenshot 2024-11-07 at 2.25.37 PM")

[![Screenshot 2024-11-07 at 2.26.09 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/9838e0ce8b8461005bbc9a35a51a07cc372536c5_2_611x500.jpeg)Screenshot 2024-11-07 at 2.26.09 PM1126×920 55.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/9838e0ce8b8461005bbc9a35a51a07cc372536c5.jpeg> "Screenshot 2024-11-07 at 2.26.09 PM")

The theoretical churn for this portfolio is **10%** of net liquidity, since each day 5% new positions and 5% ending positions, since 1/20 (days) = 5%. Since we start with a portfolio value of 1$, the $ churn is also about 0.05 per day at the start.

Finally, if we have a risk model, we can compute portfolio exposures to market risk factors. This leads me to the next section.

**Crypto Statistical Risk Model**

The basic concept of an equity risk model is a linear **factor model** , that models cross-sectional market returns as a weighted linear combination of known factor returns. Visualize this with some pseudo code as follows.

`return_asset_i = factor_0_beta_i * factor_return_0 + factor_1_beta_i * factor_return_1 + ... + noise`

According to this model, on any date, we believe an asset’s return can be (to a certain extent) explained by the asset’s exposures (betas) multiplied by market factor returns. What the factors are is a big uncertain question. The idea of CAPM is that there is one general market factor, and all assets have exposure to this market factor, to some degree. The idea of the existence of the CAPM market factor is generally accepted mathematically and practically in the equity market.

However, common risk factor models tend to contain many more factors, leading some academics to describe the state of factor modeling in finance as a “factor zoo”. Traditional finance has approached this problem generally from two angles. The first is to assume we know some factor returns, and we fit a linear model by finding the betas to these known factor returns. This kind of modeling is driven by domain knowledge.

The an alternative technique is to assume that we don’t know what the factors are and we want to learn them from our data. This kind of factor model is usually called a **statistical** factor model, since it is created using statistical tools, namely PCA, or the singular value decomposition (SVD). I’ve always been intrigued by this second approach, thinking it must be informative and useful. This technique will decompose historical returns into principle components, where by the first component captures the largest portion of **explained variance** , and each successive component captures a diminishing portion. I decided to pursue this second approach in this article, to explore how to create and use a statistical factor model in the crypto market.

I consider this a work in progress and perhaps with more help from the community we can make this better.

**The Process**

The process is identical for each date throughout our simulation time span. Each time we must compile a set of usable historical return data. In my case I used the 20 day returns, and required 600 past days of return data. If we have `N` assets, this results in a `(600 x N)` matrix of asset returns. The SVD is then computed on this matrix, which results in the information we are looking for. Here we are most interested in **factor returns** and **factor loadings (betas)**.

There are couple tricky parts here, in that the components of the SVD are unique up a sign. So as we shift our historical data set for every day that goes by, the `(600 x N)` matrix changes, because of changes of returns and also usable assets entering and exiting the universe. Every day the data is slightly different. I enforced that the direction of the first component always goes in a similar direction as the mean return of the market, since the first component is the largest market factor. We will see later it is very close to the mean return of the market. I also put in logic to keep the directions of the secondary factors (2nd component of higher) to be consistent.

**Some Results**

As we should expect, the first component of the SVD captures a factor that is almost identical to the mean return of the market, so we can think of this first risk factor as the “market return”, consistent with CAPM ideas, this statistical factor also shows that largest explained variance by far.

[![Screenshot 2024-11-07 at 2.36.16 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b00d0f0818100da7283e34184b76c1e6acf0ba22_2_646x499.png)Screenshot 2024-11-07 at 2.36.16 PM1084×838 115 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b00d0f0818100da7283e34184b76c1e6acf0ba22.png> "Screenshot 2024-11-07 at 2.36.16 PM")

[![Screenshot 2024-11-07 at 2.36.40 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b75ea1168a04ebd6b83136118d1ea4489f7b8259_2_690x448.png)Screenshot 2024-11-07 at 2.36.40 PM1708×1110 54.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b75ea1168a04ebd6b83136118d1ea4489f7b8259.png> "Screenshot 2024-11-07 at 2.36.40 PM")

so for this date we can now rank the betas and we find that BTC does not have the largest beta, instead the largest beta is for a coin called **SNS**. We can confirm with some plots that indeed BTC differs from the market factor more than SNS.

[![Screenshot 2024-11-07 at 2.38.38 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f37179c437c93a78bcd7540125d6d1a38ca3923b_2_652x499.jpeg)Screenshot 2024-11-07 at 2.38.38 PM1104×846 66.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f37179c437c93a78bcd7540125d6d1a38ca3923b.jpeg> "Screenshot 2024-11-07 at 2.38.38 PM")

[![Screenshot 2024-11-07 at 2.38.54 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/392c9766522177883e1aeed8fbb334f65b3416b8_2_649x500.png)Screenshot 2024-11-07 at 2.38.54 PM1094×842 122 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/392c9766522177883e1aeed8fbb334f65b3416b8.png> "Screenshot 2024-11-07 at 2.38.54 PM")

With this technique we can also get the higher components of the SVD, and use them as risk factors too, in my test here, I used the first 3 components as risk factors. One thing to check is that the betas stay somewhat consistent over time, since the input data to the SVD changes as time goes by. Here we plot the beta rank of the first risk factor of BTC over time.

[![Screenshot 2024-11-07 at 2.41.03 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/385300a42825064e4ee0cab9ae29133455a010e3_2_600x500.jpeg)Screenshot 2024-11-07 at 2.41.03 PM1156×962 55.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/385300a42825064e4ee0cab9ae29133455a010e3.jpeg> "Screenshot 2024-11-07 at 2.41.03 PM")

The beta ranges between the 25 and 27th percentile over the 5 months, this is pretty consistent. So now using this risk model we can compute portfolio exposures using asset and date - specific factor exposure to the top 3 factors, from our TB100 simulation above.

[![Screenshot 2024-11-07 at 2.53.26 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/51506de3d876b06301feafeb540e4138bf7e5142_2_655x500.jpeg)Screenshot 2024-11-07 at 2.53.26 PM1166×890 89.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/51506de3d876b06301feafeb540e4138bf7e5142.jpeg> "Screenshot 2024-11-07 at 2.53.26 PM")

**Risk Mitigation**

The last part of this article is to investigate mitigating portfolio risk by _neutralizing_ our portfolio to these risk factors. What I tried here was to project the real-time portfolio onto the null space of the risk betas at each date, thus getting a portfolio not much different from our original, but now neutral to the risk factors. In theory this should smooth out our return stream. This is by way of making slight adjustment each day. This actually seems to work, slightly, resulting in a bit less than overall return than the original, but a higher Sharpe ratio, Here the non-annualized Sharpe is 0.1765, compared to 0.15 of the original. Here is the return stream and portfolio betas.

[![Screenshot 2024-11-07 at 2.59.19 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4c7214c341eda585f1ae678c365b96add4ebeffc_2_652x499.jpeg)Screenshot 2024-11-07 at 2.59.19 PM1130×866 53.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4c7214c341eda585f1ae678c365b96add4ebeffc.jpeg> "Screenshot 2024-11-07 at 2.59.19 PM")

[![Screenshot 2024-11-07 at 3.01.15 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/9dabcaa2cbea4edfca9c1b190d293fda086f45e8_2_620x500.jpeg)Screenshot 2024-11-07 at 3.01.15 PM1140×918 67.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/9dabcaa2cbea4edfca9c1b190d293fda086f45e8.jpeg> "Screenshot 2024-11-07 at 3.01.15 PM")

The slight increase to churn after this neutralization was minimal.

So there we have it, a market-neutral TB100 Crypto portfolio with statistical risk mitigation.

**Code**

[Please find all code to replicate this simulation here.](<https://github.com/jefferythewind/crypto_portfolio/blob/master/Meta%20Model.ipynb>)

**Thoughts/Discussion**

I meant this to be more of a starting point than an end in itself, so please let me know with any feedback. If you noticed I didn’t do any optimization here. I did try an idea to optimize the portfolio input vector at each date, instead of the naive equal weights, but then you still have the problem of exposures getting out-of-whack during the simulation period, and adjustment may still be required.

Also interested to see if any and point out some mistakes or bugs. I was maybe expecting the result of the risk neutralization to work better than it did.

With this framework, we can also apply other risk models just as long as we know how to compute the betas at each date, so this framework can be used to compare competing strategies and risk control ideas.

---

### Post #2 — **kiwibot** | 2024-11-07 21:13 UTC

Thanks Jeffery for getting the ball rolling on this and also providing a really insightful piece of work!

I have a few thoughts / comments:

  1. Given the Numerai Crytpo universe is ~ 500 names, I think going long and short 100 names each is a bit large. I would recommend focusing in on maybe TB 20 / 30, to focus on the highest conviction trades of the Crypto MM. This would significantly reduce overall transaction costs and short-borrow costs/constraints.

  2. Are you simulating any transaction costs here? If I understand correctly, if you have a prediction on day T, you are assuming you transact at the close price of T? That seems reasonable if the MM preds are indeed published a few hours after the round’s submission period closes. However, I do believe short borrow rates can be pretty steep, especially on low mkt cap coins which from my observations the Crypto MM likes to short. I think this needs to be included in the simulation to build conviction to actually trade this.

  3. If I understand correctly, you are entering a set of trades on each day, and then holding these positions until expiration in 20 days? I think an approach worth exploring is each day, estimate desired positions based on updated MM predictions, and then perturb positions towards these desired positions based on certain constraints around maximum churn etc. This would reduce the amount of cash deployed… unless I’m missing something in your approach?




Thanks again for this.

---

### Post #3 — **jefferythewind** | 2024-11-07 22:01 UTC _(reply to #2)_

Yes a quick check shows the TB25 portfolio does better than TB100. With the risk mitigation we get a higher Sharpe. Also, because of the layering affect of the trades, on the last day of simulation our portfolio in this setting is holding 167 assets.

[![Screenshot 2024-11-07 at 4.59.03 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/dee20cbdec951fc6b2a395e43e6b10f128dde4ab_2_639x500.jpeg)Screenshot 2024-11-07 at 4.59.03 PM1156×904 59.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dee20cbdec951fc6b2a395e43e6b10f128dde4ab.jpeg> "Screenshot 2024-11-07 at 4.59.03 PM")

So far there are not any transaction costs incorporated here. And, yes it is pretty flexible about how the trades are allocated, that is all about the art of crafting a strategy. We could definitely have a target portfolio and only take small steps in that direction each day. That should reduce churn, thereby reducing transaction costs.

---

### Post #4 — **mrwatson** | 2024-11-07 22:52 UTC _(reply to #3)_

How are you calculating Sharpe?

Can you change to annualized return / annualized volatility?

Visually you have 25% return here in just 6 months and max drawdown around -5%, this is not annualized Sharpe of 0.19…

---

### Post #5 — **jefferythewind** | 2024-11-07 23:52 UTC _(reply to #4)_

Thanks, correct. Here we have daily returns, so I think the general technique is to multiply this Sharpe ratio by sqrt(252), which results in an annualized Sharpe of 3.09!

[![Screenshot 2024-11-07 at 6.48.59 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/ce768fa161a01768daa823874f2d7321631de66e_2_690x430.jpeg)Screenshot 2024-11-07 at 6.48.59 PM1644×1026 116 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/ce768fa161a01768daa823874f2d7321631de66e.jpeg> "Screenshot 2024-11-07 at 6.48.59 PM")

---

### Post #6 — **rift** | 2024-11-08 02:48 UTC _(reply to #5)_

Nice work [@jefferythewind](</u/jefferythewind>)! One more important thing to consider from a practical perspective, adding to [@kiwibot](</u/kiwibot>) 's comments earlier, is that I don’t think you can easily short many of the coins at the bottom of the rank. Performance of a tradeable universe is much worse recently. If we reduce the universe to just the coins in the intersection between the universe of perps that are listed on dYdX and the Numerai Crypto universe we get the following prediction corr for a range of dollar neutral top-bottom portfolios:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a39fa0a9c95bd431dd899cecf4cd1cc6572f3372_2_690x230.png)image1500×500 68.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a39fa0a9c95bd431dd899cecf4cd1cc6572f3372.png> "image")

---

### Post #7 — **jefferythewind** | 2024-11-08 14:42 UTC _(reply to #6)_

Yes perfectly reasonable, do you have a link to a list of tradable assets, I could definitely see if I can incorporate this shortable list to the backtest. Also, what the heck is a perp?!

---

### Post #8 — **rift** | 2024-11-08 20:53 UTC _(reply to #7)_

Current dYdX universe:

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4e650039409fd28004410e4f5b9d71cbec3f6a12.png) [dropbox.com](<https://www.dropbox.com/scl/fi/kgkpl2s0sfh4eg7yd2rhx/dydx_universe.csv?rlkey=juel10tz5qz7v9054wclhcm01&st=6hnxnccx&dl=0>)

### [Dropbox](<https://www.dropbox.com/scl/fi/kgkpl2s0sfh4eg7yd2rhx/dydx_universe.csv?rlkey=juel10tz5qz7v9054wclhcm01&st=6hnxnccx&dl=0>)

Also, with dYdX rolling out Unlimited soon, this should get much bigger and its going to be hard for CEXs to compete with universe size.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b20cddd19c4ace70bc3cc5c3363181f66b52447f.png) [dydx.xyz](<https://www.dydx.xyz/blog/dydx-unlimited-coming-this-fall>)

### [dYdX.xyz](<https://www.dydx.xyz/blog/dydx-unlimited-coming-this-fall>)
