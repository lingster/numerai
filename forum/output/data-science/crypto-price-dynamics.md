---
title: "Crypto Price Dynamics"
category: Data Science
url: https://forum.numer.ai/t/crypto-price-dynamics/7677
created_at: 2024-08-26T20:02:21.608000+00:00
last_posted_at: 2024-10-18T13:30:11.730000+00:00
posts_count: 7
views: 1214
tags: []
---

# Crypto Price Dynamics

---

### Post #1 — **whiterider** | 2024-08-26 20:02 UTC

The report below outlines a multi-factor model developed to predict cryptocurrency prices by integrating market data, sentiment analysis, and macroeconomic indicators. The work is part of the Ocean Protocol competition hosted on Desights. Data was collected from sources including Binance, Yahoo Finance, CoinMarketCap, Google Trends, and macroeconomic databases like the World Bank and FRED.

**Data Collection and Preparation:**  
The dataset includes over 1 million rows of OHLCV data for 1,439 unique cryptocurrency symbols. Supplementary data was gathered on market sentiment through the Fear & Greed Index, coin fundamentals, and Google search trends. Macroeconomic factors such as inflation, GDP, and interest rates were also incorporated.

**Feature Engineering:**  
Features were created from the collected data, including moving averages, liquidity factors, sentiment buckets, and macroeconomic trends. These features were used to train LGBMRegressor models, with the best model achieving an R-squared of 0.645, indicating a reasonable level of predictive accuracy.

**Key Findings:**

  1. **Sentiment Indicators:** The Fear & Greed Index showed strong correlations with price trends, with values exceeding 0.94.
  2. **Macroeconomic Influence:** While valuable, macroeconomic features had a lesser impact compared to sentiment and market data.
  3. **Trading Volume Correlation:** High trading volumes were consistently aligned with price increases, indicating strong market interest.



**Conclusion:**  
This work is ongoing, with further model development and data preparation planned. Suggestions from the Numerai community are highly valued to improve the model’s accuracy and robustness.

For a detailed methodology and results, the full report is available [here](<https://github.com/LoznianuAnamaria/challenges/blob/main/Crypto%20Factor%20Modeling%2FCrypto%20Factor%20Modeling.pdf>).  
Additional details and the code can be found in the [GitHub repository](<https://github.com/LoznianuAnamaria/challenges/tree/main/Crypto%20Factor%20Modeling>).

---

### Post #2 — **mlh_alavi** | 2024-08-27 16:19 UTC

great work Ana as always ![:100:](http://forum.numer.ai/images/emoji/twitter/100.png?v=12) ![:boom:](http://forum.numer.ai/images/emoji/twitter/boom.png?v=12)

---

### Post #3 — **mitchel12** | 2024-09-10 09:46 UTC

Hi [@whiterider](</u/whiterider>)  
That’s great! ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=12)

---

### Post #4 — **lazyturtle0024** | 2024-09-18 21:21 UTC

would you mind share the process and data that supports your claim?

---

### Post #5 — **whiterider** | 2024-09-20 07:21 UTC _(reply to #4)_

**Thank you for your interest!** I’m happy to share more details on the process and data behind. Here’s a brief overview:

### **Data Collection:**

For the 1,439 unique cryptocurrency symbols from the `train_targets.parquet` dataset, the following data was downloaded and processed:

  * **[OHLCV Data](<https://github.com/LoznianuAnamaria/challenges/blob/FactorModel/Crypto%20Factor%20Modeling/notebooks/2.0%20ohlcv_data.ipynb>):** Collected from Binance and Yahoo Finance The data captures daily open, high, low, close, and volume data for each symbol.
  * **[Coin Information](<https://github.com/LoznianuAnamaria/challenges/blob/main/Crypto%20Factor%20Modeling/notebooks/4.0%20coin_details.ipynb>):** Collected from CoinMarketCap coin information: _circulating_supply_ , _total_supply_ , _market_cap_ , _is_active_ , _source_code_(relevant information for open source projects), _name_ , _keywords_.
  * **[Sentiment Data](<https://github.com/LoznianuAnamaria/challenges/blob/main/Crypto%20Factor%20Modeling/notebooks/3.0%20fear_greed_index.ipynb>):** The Fear & Greed Index was gathered from [Alternative.me](<https://alternative.me>), providing market sentiment insights, ranging from extreme fear to extreme greed.
  * **[Google Trends](<https://github.com/LoznianuAnamaria/challenges/blob/main/Crypto%20Factor%20Modeling/notebooks/5.0%20trends_data.ipynb>):** Search trend data was pulled from Google Trends to capture public interest in specific cryptocurrencies. **Note** : This is not yet integrated in the features and in the prediction model.
  * **[Macroeconomic Data](<https://github.com/LoznianuAnamaria/challenges/blob/main/Crypto%20Factor%20Modeling/notebooks/6.0%20economic_data.ipynb>):** Inflation, GDP, and interest rate data were sourced from the World Bank, FRED (Federal Reserve Economic Data), and Trading Economics, focusing on key global economies.



### **[Feature Engineering](<https://github.com/LoznianuAnamaria/challenges/blob/main/Crypto%20Factor%20Modeling/notebooks/9.0%20feature_engineering.ipynb>):**

Several features are engineered to build the model:

  * **Moving Averages (MA):** Calculated across different time periods (1, 7, 30 days) to capture price trends.

  * **Rate of Change (RoC):** Measures the percentage change in the close price over different intervals to assess price momentum.

  * **Exponential Moving Averages (EMA):** Provides a weighted average of close prices, giving more emphasis to recent data for quick trend detection.

  * **Price Lag Features:** Includes features like `close_lag_1`, `close_lag_7`, and `close_lag_30`, which capture the lagged close prices over different timeframes.

  * **Percent Change (Pct Chg):** Represents the percentage change in the close price over a 30-day window (`pct_chg_30`).

  * **Volatility Measures:** Derived from the variance in the close price over certain periods to assess market risk.

  * **Liquidity and Size Factors:** Derived from trading volumes and market capitalization data.  


[![Screenshot 2024-09-20 at 09.58.45](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b406a5debeba879b8f6125af0736f18b0c0fb2ca_2_690x337.png)Screenshot 2024-09-20 at 09.58.45914×447 73.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b406a5debeba879b8f6125af0736f18b0c0fb2ca.png> "Screenshot 2024-09-20 at 09.58.45")

  * **Sentiment Interaction Features:** Combined the Fear & Greed Index with price trend data, which showed strong correlations.  


[![Screenshot 2024-09-20 at 09.55.57](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f614f6921a03e610615cd3cc66d928b81e4cec7e_2_647x500.jpeg)Screenshot 2024-09-20 at 09.55.57921×711 168 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f614f6921a03e610615cd3cc66d928b81e4cec7e.jpeg> "Screenshot 2024-09-20 at 09.55.57")

  


[![Screenshot 2024-09-20 at 09.56.52](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/ee8f67bfde675c7451732de37fbdf4a29ee67115.png)Screenshot 2024-09-20 at 09.56.52531×191 16.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/ee8f67bfde675c7451732de37fbdf4a29ee67115.png> "Screenshot 2024-09-20 at 09.56.52")

  * **Macroeconomic Factors:** Integrated overall inflation, interest rates, and GDP as weighted global metrics to capture external economic influences.




### **Access to Data and Code:**

The code is available at the GitHub repository I shared in the initial post. Running each notebook will give you access to the data itself. PS: some environment variables are needed if you want to run all the notebooks. Specifically, you will need the following:

  * `COINMARKETCAP_API_KEY`
  * `WORLD_BANK_API_KEY`
  * `STLOUISFED_API_KEY`



You can add these keys to the `.env` file, and everything should run smoothly. These API keys are free to obtain.

I hope my response contains the information you requested. If not, please let me know. Also, if you notice something off, feel free to point it out.

---

### Post #8 — **joakim** | 2024-09-20 23:58 UTC _(reply to #5)_

Amazing work, thank you for sharing!

---

### Post #9 — **philippepro36** | 2024-10-18 13:30 UTC

Very interesting, thanks for sharing.
