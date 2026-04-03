---
title: "A Detailed Case Study on Crypto Multi-factor Risk Analysis"
category: Data Science
url: https://forum.numer.ai/t/a-detailed-case-study-on-crypto-multi-factor-risk-analysis/7682
created_at: 2024-08-27T03:53:00.402000+00:00
last_posted_at: 2024-08-27T20:35:37.062000+00:00
posts_count: 4
views: 709
tags: []
---

# A Detailed Case Study on Crypto Multi-factor Risk Analysis

---

### Post #1 — **datahunter** | 2024-08-27 03:53 UTC

**Introduction**  
In recent years, cryptocurrencies have garnered significant attention from researchers and inventors, among other financial investments. Many investment firms have been investing in and maintaining a strong portfolio of cryptos. More than 1,500 crypto currencies are being actively traded by individual and institutional investors worldwide across different exchanges. Over 170 cryptocurrencies focussed hedge funds, have emerged since 2017.  
This report as a part of Desights.ai Data Challenge (OCEAN and Numer.ai) explores cryptocurrency investment strategies by adapting the robust framework of multi-factor investing, traditionally applied in equity markets, to the distinctive landscape of cryptocurrency assets.

  1. We conduct an in-depth examination of prominent cryptocurrencies from 2018 to 2024 (in some cases – 2020/21), employing models such as (i) Fama–MacBeth regression method, (ii) Fama-French 3 and 4-factor model, (iii) Carhart 4-factor model, (iv) GARCH, (v) CAPM (single factor) and (vi) Machine Learning-based regressions (LSTM, PCA based Statistical Risk Analysis) to assess the predictive capabilities of market, size, value, and momentum factors, adjusted for the unique characteristics of the cryptocurrency market.
  2. We extract and identify other factors such as Macroeconomic factors (Comparison with NASDAQ100, S&P500, CPI) and Social Media factors (Google Trends, Wikipedia page visits) along with other indirect factors to identify the correlation between the cryptocurrency market and their volatility, returns, risks and sentiment.



At the core of this study is the idea that there may be predictability in returns arising from systematic inconsistencies. This research introduces factors specific to the cryptocurrency realm, investigating their connection to market irregularities. With Bitcoin often serving as the benchmark currency on many trading platforms, this study suggests a re-examination of conventional methods for evaluating factor portfolios, proposing a shift in investors’ perspectives to accommodate this unique market characteristic.

**Need for this analysis**  
There is a need to analyse the cryptocurrency market from the empirical rule-based approach for at least two reasons.

  * The first reason is to understand whether the returns of cryptocurrencies share similarities with other asset classes, most importantly, with equities.
  * The second reason is that to assess and develop theoretical models of cryptocurrency, it is meaningful to build an empirical model to be used as stylized facts and inputs. Since there is no simple universal framework to construct a crypto portfolio unlike the equity market, we, therefore, propose to create a factor model for cryptocurrencies.
  * The factor model has been traditionally used in the equity markets to decompose the assets return and risk. (e.g., CAPM, Fama-French, Carhart-4-factor, BARRA), so it could also provide a paradigm to analyze such patterns in the cryptocurrency market.



**Report Link:** [Click here](<https://drive.google.com/file/d/1378ZJbdqqP2DBlrPS1Pg6oHQYD7hyB9j/view?usp=sharing>)

**Datasets Link:**

  1. **[CoinGecko.com](<http://CoinGecko.com>):** Collected data from Coin Gecko (<https://www.coingecko.com/en>). Coin Gecko has information on more than 6900 coins from over 400 exchanges and has daily data on prices, volume, and market capitalization (in dollar terms). Out of which, collected the Top-1000 cryptocurrencies based on Market Cap for this analysis.



**Data Link:** [CoinGecko Dataset](<https://drive.google.com/drive/folders/1rA_KjpnyKqmXqb-slqk9eFz-Xwzooy1Y?usp=sharing>)

  2. **CryptoCompare:** This database is used to download aggregated and exchange level OHLC pricing and volume cryptocurrency data each day



**Data Link:** [CryptoCompare Dataset](<https://drive.google.com/drive/folders/1Zk8FNgJRUnXUyRRBv_q72IWMgSUKCPPB?usp=sharing>)

  3. **[IntoTheBlock.com](<http://IntoTheBlock.com>)** database, which is used to source information on blockchain activity, such as the number of new addresses and the number of active unique addresses.
  4. **CCXT:** Here we use the ccxt library and list current exchanges supported by ccxt and identify arbitrage opportunities with the shortest and longest chains. Downloaded Binance Dataset using `exchange = ccxt.binanceus()`

---

### Post #2 — **mlh_alavi** | 2024-08-27 16:06 UTC

great work [@datahunter](</u/datahunter>)  
I read your report and your point of view in solving this challenge is amazing !!!

---

### Post #3 — **mlh_alavi** | 2024-08-27 16:08 UTC

hope to see you in top places on the leaderboard ![:100:](http://forum.numer.ai/images/emoji/twitter/100.png?v=12) ![:crossed_fingers:](http://forum.numer.ai/images/emoji/twitter/crossed_fingers.png?v=12)

---

### Post #4 — **datahunter** | 2024-08-27 20:35 UTC

**Visualisations and EDA:**  


[![Picture 1](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a39c20ce34d7bd2d4ede5f60305b684fb0f2928e.png)Picture 1546×438 139 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a39c20ce34d7bd2d4ede5f60305b684fb0f2928e.png> "Picture 1")

  


[![Picture 2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2ef334b387949b017076dc0d57a9ce3e4660ab19.png)Picture 2560×452 122 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2ef334b387949b017076dc0d57a9ce3e4660ab19.png> "Picture 2")

  


[![Picture 3](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4a9d5ec1b65d9e09a4b6d36fb00696cf5dffb2b5.png)Picture 3580×454 130 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4a9d5ec1b65d9e09a4b6d36fb00696cf5dffb2b5.png> "Picture 3")

  


[![Picture 4](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/244ca628d70942c4ccde5b86b874a2f90f646cab.png)Picture 4560×438 89.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/244ca628d70942c4ccde5b86b874a2f90f646cab.png> "Picture 4")

  


[![Picture 5](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2918b36eefa2e58cfba5bd13a58c0b5ecb27b321.png)Picture 5678×400 91.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2918b36eefa2e58cfba5bd13a58c0b5ecb27b321.png> "Picture 5")

  


[![Picture 6](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/aed75194ab9577bec3cfb77764bba5a8bddfec7d_2_690x404.png)Picture 6908×532 171 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/aed75194ab9577bec3cfb77764bba5a8bddfec7d.png> "Picture 6")
