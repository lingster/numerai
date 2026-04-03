---
title: "Factor Analysis of Cryptocurrency Returns Using Momentum Indicators"
category: Data Science
url: https://forum.numer.ai/t/factor-analysis-of-cryptocurrency-returns-using-momentum-indicators/7667
created_at: 2024-08-24T11:28:24.675000+00:00
last_posted_at: 2024-08-30T05:51:07.305000+00:00
posts_count: 9
views: 794
tags: []
---

# Factor Analysis of Cryptocurrency Returns Using Momentum Indicators

---

### Post #1 — **accountnumber1** | 2024-08-24 11:28 UTC

This is my entry for the Numerai/Ocean competition.  
Hope you enjoy.  
Let me know if there are any questions!

Factor Analysis of Cryptocurrency Returns Using Momentum Indicators

[docs.google.com](<https://docs.google.com/document/d/1r_JKz4gts3TzndR8KOxnAuXXLTRD-BxSekPD5l_F3a0/pub>) [](<https://docs.google.com/document/d/1r_JKz4gts3TzndR8KOxnAuXXLTRD-BxSekPD5l_F3a0/pub>)

### [Factor Analysis of Cryptocurrency Returns Using Momentum Indicators](<https://docs.google.com/document/d/1r_JKz4gts3TzndR8KOxnAuXXLTRD-BxSekPD5l_F3a0/pub>)

This Doc is private

---

### Post #2 — **accountnumber1** | 2024-08-24 11:31 UTC

Ok, I think that hasn’t worked? Its set to private? Here is the text version:

### Factor Analysis of Cryptocurrency Returns Using Momentum Indicators

### Abstract

This report investigates the effectiveness of momentum-based indicators in predicting cryptocurrency price movements, using Numerai’s discretized return data. Key methodologies include the application of Simple Moving Average (SMA) and Moving Average Convergence Divergence (MACD) indicators, with a focus on identifying both inductive and anti-inductive price patterns. Through a series of experiments, optimal window sizes for momentum indicators were determined, and the performance of these indicators was evaluated across different subsets of cryptocurrencies. Simulations of future returns suggest a high probability of profitability using the SMA-based MACD (SMACD) strategy. However, potential limitations such as data discretization and coding errors are acknowledged. The results indicate that momentum-based strategies, particularly those employing SMACD, offer promising predictive power in the cryptocurrency market, with significant opportunities for further research.

Introduction

In technical analysis, various indicators have been developed to predict asset price movements, with momentum-based indicators being among the most popular. Indicators like the Relative Strength Index (RSI), Moving Average Convergence Divergence (MACD), Simple Moving Average (SMA), and Exponential Moving Average (EMA) are all variations of the fundamental idea that an asset’s expected return is, in some way, influenced by its past returns.

Numerai’s crypto contest provides historical return data for various cryptocurrency assets, categorized into five discrete bins that approximate a bell curve. This raises an intriguing question: can momentum indicators, typically based on raw price data, still function effectively when applied to these binned returns?

In this study, I will explore this question by comparing different momentum-based indicators and their respective parameters to determine whether any of them show a significant correlation with future returns. Additionally, I will consider refinements such as focusing on different subgroups of cryptocurrencies, and I will evaluate the confidence intervals of these models to assess the robustness of their future performance.

### Data

Numerai’s signals data consists of discretized returns for the top cryptocurrencies, recorded at each weekday to maintain consistency with their other competitions. These returns are calculated over a 30-day time horizon. Notably, the dataset reflects the top cryptocurrencies at each individual timestep, rather than the top cryptocurrencies as of the current date. This approach helps mitigate the risk of survivorship bias, as it includes assets that may no longer be in the top ranks at present. One major advantage of using Numerai’s data is its simplicity, as the required data has already been collated and preprocessed. Additionally it can be accessed freely and easily via their api, as detailed on Numerai’s website.

The dataset spans from June 1, 2020, to May 22, 2024 (at the time of writing), covering periods of both bull and bear markets. This broad timeframe provides a diverse range of market conditions, which is essential for testing the robustness of momentum-based indicators across different market environments.

### Iteration 1: Initial Indicator Performance Assessment

In this analysis, I tested various momentum indicators by examining their correlation with Numerai’s targets. Initially, I used a 20-day window for most indicators, as suggested by prior research, with the MACD (Moving Average Convergence Divergence) calculated as the difference between 20-day and 100-day moving averages. Additionally, I experimented with a longer 100-day Simple Moving Average (SMA).

Since Bollinger Bands are typically represented as a discrete step function, which isn’t suitable for direct correlation analysis, I modified the Bollinger Bands to use a ratio of the average price divided by the standard deviation. This adjustment allowed for a continuous measure that could be better correlated with the targets.

Momentum indicators can correlate with future returns in two primary ways:

  1. Inductive Momentum: Assets that have performed well in the past continue to do well in the future (positive correlation).
  2. Anti-Inductive Momentum: Assets become ‘overbought’ or ‘oversold,’ leading to a reversal towards the mean (negative correlation).



In this case, the latter, anti-inductive momentum, appears to be the dominant effect. Therefore, I have inverted the following graph to present anti-correlations as upward trends, which I believe makes the visualization more intuitive.

The results show that the MACD, which is composed of the ‘MACD line,’ the ‘Signal line,’ and the ‘MACD histogram,’ performs comparably to the SMA. However, its performance varies across different periods, highlighting the importance of considering multiple indicators over different time horizons.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/fe45a7c814bbcfacdb2392089ffbfd6eac1c6803_2_690x273.png)1403×556 96.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fe45a7c814bbcfacdb2392089ffbfd6eac1c6803.png>)

### Iteration 2: Refining Indicator Accuracy by Subgroup Analysis

To refine the analysis, I focused on the two most promising indicators identified in the first approach: the Simple Moving Average (SMA) and the Signal Line from the MACD. I applied these indicators across various subsets of cryptocurrencies to investigate whether different types of coins exhibit distinct momentum behaviors.

The subsets of coins were derived based on themes, which were generated using ChatGPT. These themes categorize coins into groups, such as “utility tokens” and “governance tokens.” Each subset contains approximately 10 coins, with some overlap between the lists. Correlations were calculated within each subset to assess the performance of the SMA and Signal Line indicators.

To avoid double counting due to the 20-day prediction horizon, hypothesis tests were conducted on every 20th data point. The specific coin subsets will be listed in the appendix for reference.

#### MACD Signal Line Graph:

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/1efe20e1ea295b5d525f604a028e47023d5b132e_2_690x273.png)1403×556 113 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1efe20e1ea295b5d525f604a028e47023d5b132e.png>)

In the case of the MACD Signal Line, the “utility tokens” and “all tokens” subsets showed stronger correlations with future returns compared to the entire universe of coins. These correlations were significant at the standard 95% confidence level, and even at the 99.5% confidence level for the “all tokens” subset, without corrections for multiple hypothesis testing.

#### SMA Graph:

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/06860f5398e7335ac4a4e0417a85a7fc37f0b621_2_690x273.png)1403×556 109 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/06860f5398e7335ac4a4e0417a85a7fc37f0b621.png>)

For the SMA indicator, the “governance tokens,” “utility tokens,” and “all tokens” subsets demonstrated better correlations than the entire universe. These results were significant at the 95% confidence level, with the “all tokens” subset reaching significance at the 99.8% confidence level, again without correcting for multiple hypothesis testing.

These findings suggest that certain subgroups of cryptocurrencies may be more responsive to momentum-based indicators. The results indicate potential opportunities for emphasizing specific subgroups, such as utility and governance tokens, in momentum-based analysis to achieve better predictive performance.

### Iteration 3: Search for Optimal Window Size

In this iteration, I conducted a grid search to identify the optimal window size for momentum indicators. Since we are only exploring a single dimension of parameters (the window size), a simple grid search was sufficient, eliminating the need for more complex optimization algorithms.

The results indicate that short windows of 5-20 days are optimal for capturing anti-inductive momentum (where assets revert to the mean), while longer horizons of around 200 days are more effective for detecting inductive momentum (where past performance continues into the future).

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/89d4c6e98912c373ba2a10ad50d2fda3b7fa0823_2_690x273.png)1403×556 145 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/89d4c6e98912c373ba2a10ad50d2fda3b7fa0823.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/6513bd9585cffabf5f6a27c1a6e2b2117ca2dd33_2_690x273.png)1403×556 25.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6513bd9585cffabf5f6a27c1a6e2b2117ca2dd33.png>)

These findings suggest that the difference between the 10-day and 200-day windows could yield an effective MACD (Moving Average Convergence Divergence) indicator. To test this, I calculated the MACD using both the traditional Exponential Moving Average (EMA) and a Simple Moving Average (SMA) for a more direct comparison. I delayed the start of the analysis by 250 days to ensure that both the 10-day and 200-day averages were fully established.

Interestingly, the SMA-based MACD outperformed the traditional EMA-based version, suggesting that the simpler approach may be more effective in this context.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b9afc7bf4629657a875da02580b55546b946c642_2_690x275.png)1394×556 87.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b9afc7bf4629657a875da02580b55546b946c642.png>)

### Simulating Future Returns

To assess the robustness of the SMA-based MACD (or SMACD), I simulated future returns by randomly sampling 20-day chunks of data over 10,000 iterations. The resulting graph of projected returns indicates a 95% probability of achieving a profit within just over 100 days.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/2aae6dbfddea87cae9081fe748a379ae397f64dd_2_690x275.png)1394×556 82.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2aae6dbfddea87cae9081fe748a379ae397f64dd.png>)

### Conclusion

While the findings from the SMA-based MACD (SMACD) simulation are promising, it’s important to consider several caveats:

  1. Potential Coding Errors: Despite careful efforts to avoid mistakes, there’s always a chance of errors in the code. The most significant concern—data leakage from future values—would likely cause an inductive rather than anti-inductive relationship, which is not observed here.
  2. Discretization and Data Bias: The discretization of returns in Numerai’s data might introduce biases. This process could oversimplify the true behavior of the assets. For example, an asset with consistent small losses (e.g., -5%) and occasional large gains (e.g., +20%) might be incorrectly categorized if the losses fall within a neutral or positive bin, distorting the overall picture. This kind of data handling could affect the validity of the results, making it crucial to consider how discretization might be influencing the observed patterns.



Assuming these results hold, the SMA-based MACD seems to be an effective momentum indicator with a high probability of generating positive returns. Further research should explore the behavior of this indicator across different cryptocurrency subgroups, as this could provide additional insights and opportunities for model refinement.

### Appendix: stock subsets

#### Privacy Coins

  1. Monero (XMR) - Known for its strong privacy features, Monero is a leading privacy coin [1](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DMonero%2520%2528XMR%2529&sa=D&source=editors&ust=1724445405455687&usg=AOvVaw1lxdyaqD3JXe7vb4UgidhI>)[2](<https://www.google.com/url?q=https://bravenewcoin.com/insights/best-crypto-to-invest-today-august-2024-top-10-cryptocurrency-coins-to-buy-now-for-the-bull-run%23:~:text%3DMonero%2520%2528XMR%2529&sa=D&source=editors&ust=1724445405456038&usg=AOvVaw2c7b7VrZgDBZBOsV8vEU33>).
  2. Zcash (ZEC) - Offers optional privacy features through its “shielded” transactions [3](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DZcash%2520%2528ZEC%2529&sa=D&source=editors&ust=1724445405456308&usg=AOvVaw0AnkT-n1xPvg67jUB7yXLs>)[4](<https://www.google.com/url?q=https://bravenewcoin.com/insights/best-crypto-to-invest-today-august-2024-top-10-cryptocurrency-coins-to-buy-now-for-the-bull-run%23:~:text%3DZcash%2520%2528ZEC%2529&sa=D&source=editors&ust=1724445405456516&usg=AOvVaw0V44BdKC4N_gPbeFtlShST>).
  3. Dash (DASH) - Includes a feature called PrivateSend for enhanced privacy [5](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DDash%2520%2528DASH%2529&sa=D&source=editors&ust=1724445405456797&usg=AOvVaw2sLVq-WGXOPsb9e0AckiPB>)[6](<https://www.google.com/url?q=https://bravenewcoin.com/insights/best-crypto-to-invest-today-august-2024-top-10-cryptocurrency-coins-to-buy-now-for-the-bull-run%23:~:text%3DDash%2520%2528DASH%2529&sa=D&source=editors&ust=1724445405457007&usg=AOvVaw2eWskjXCX12L_X-zZ7lTce>).
  4. Secret (SCRT) - Focuses on privacy-preserving smart contracts [7](<https://www.google.com/url?q=https://bravenewcoin.com/insights/best-crypto-to-invest-today-august-2024-top-10-cryptocurrency-coins-to-buy-now-for-the-bull-run%23:~:text%3DSecret%2520%2528SCRT%2529&sa=D&source=editors&ust=1724445405457367&usg=AOvVaw1Zvt8_8F_8zNsFMlr_QP9c>).
  5. Oasis Network (ROSE) - Aims to provide privacy and scalability for decentralized applications [8](<https://www.google.com/url?q=https://bravenewcoin.com/insights/best-crypto-to-invest-today-august-2024-top-10-cryptocurrency-coins-to-buy-now-for-the-bull-run%23:~:text%3DOasis%2520Network%2520%2528ROSE%2529&sa=D&source=editors&ust=1724445405457679&usg=AOvVaw2pEptC_xxfPGlC7h9VfZJ9>).



#### Meme Coins

  1. Dogecoin (DOGE) - Originally created as a joke, Dogecoin has gained a large following [9](<https://www.google.com/url?q=https://www.tokenmetrics.com/blog/top-meme-coins-2024%23:~:text%3DDogecoin%2520%2528DOGE%2529&sa=D&source=editors&ust=1724445405458176&usg=AOvVaw0n-Kk39DLbo0G7NHqfu2KD>)[10](<https://www.google.com/url?q=https://bravenewcoin.com/insights/best-crypto-to-invest-today-august-2024-top-10-cryptocurrency-coins-to-buy-now-for-the-bull-run%23:~:text%3DDogecoin%2520%2528DOGE%2529&sa=D&source=editors&ust=1724445405458385&usg=AOvVaw1WnF3fMtT4rksRqe5E43Wt>).
  2. Shiba Inu (SHIB) - Often referred to as the “Dogecoin killer,” it has a strong community [11](<https://www.google.com/url?q=https://www.tokenmetrics.com/blog/top-meme-coins-2024%23:~:text%3DShiba%2520Inu%2520%2528SHIB%2529&sa=D&source=editors&ust=1724445405458678&usg=AOvVaw0bSkOdE0ihFYBTny5PG9l4>).
  3. Bonk (BONK) - A newer meme coin gaining popularity [12](<https://www.google.com/url?q=https://www.tokenmetrics.com/blog/top-meme-coins-2024%23:~:text%3DBonk%2520%2528BONK%2529&sa=D&source=editors&ust=1724445405458960&usg=AOvVaw018DzQsm0Q0C_EpnRqzKF6>).
  4. Pepe (PEPE) - Inspired by the popular internet meme, Pepe the Frog [13](<https://www.google.com/url?q=https://www.tokenmetrics.com/blog/top-meme-coins-2024%23:~:text%3DPepe%2520%2528PEPE%2529&sa=D&source=editors&ust=1724445405459236&usg=AOvVaw0Fprqn8T1ytLN8dDmqQKLV>).
  5. Myro (MYRO) - Another meme coin with a growing community [14](<https://www.google.com/url?q=https://www.tokenmetrics.com/blog/top-meme-coins-2024%23:~:text%3DMyro%2520%2528MYRO%2529&sa=D&source=editors&ust=1724445405459563&usg=AOvVaw37x_JYfbNkLtXnSvW1lgY9>).
  6. FLOKI - Named after Elon Musk’s dog, it has a dedicated fanbase [15](<https://www.google.com/url?q=https://www.tokenmetrics.com/blog/top-meme-coins-2024%23:~:text%3DFLOKI&sa=D&source=editors&ust=1724445405459832&usg=AOvVaw1tNoq8fZodiCM-9gV7Glct>).
  7. Dogwifhat - A lesser-known but emerging meme coin [16](<https://www.google.com/url?q=https://www.tokenmetrics.com/blog/top-meme-coins-2024%23:~:text%3DDogwifhat&sa=D&source=editors&ust=1724445405460105&usg=AOvVaw1Pszk0lI7m1ICF7wK7JhCt>).



#### Payment Tokens

  1. Ethereum (ETH) - Widely used for transactions and smart contracts [17](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DEthereum%2520%2528ETH%2529&sa=D&source=editors&ust=1724445405460463&usg=AOvVaw2Y7G_tkKHK3DQH9npMSpRF>)[18](<https://www.google.com/url?q=https://bravenewcoin.com/insights/best-crypto-to-invest-today-august-2024-top-10-cryptocurrency-coins-to-buy-now-for-the-bull-run%23:~:text%3DEthereum%2520%2528ETH%2529&sa=D&source=editors&ust=1724445405460675&usg=AOvVaw1fGIgNeasFKVRHu9CQq0zN>).
  2. Bitcoin Cash (BCH) - Designed for faster and cheaper transactions compared to Bitcoin [19](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DBitcoin%2520Cash%2520%2528BCH%2529&sa=D&source=editors&ust=1724445405460985&usg=AOvVaw1S9J_lorm-zpxJQsV3yW16>).
  3. Ripple (XRP) - Known for its quick and low-cost international payments [20](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DRipple%2520%2528XRP%2529&sa=D&source=editors&ust=1724445405461253&usg=AOvVaw35yvl2RhXi_-wDPhFe-v78>).
  4. Dash (DASH) - Also used for everyday transactions due to its speed and low fees [5](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DDash%2520%2528DASH%2529&sa=D&source=editors&ust=1724445405461510&usg=AOvVaw08D7zTF1gGLa8C-iFXg33P>).
  5. Stellar (XLM) - Focuses on cross-border payments and remittances [21](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DStellar%2520%2528XLM%2529&sa=D&source=editors&ust=1724445405461770&usg=AOvVaw0Qj_AaMhq6FQYBaH9EZBKg>).
  6. Binance Coin (BNB) - Used for transactions within the Binance ecosystem [22](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DBinance%2520Coin%2520%2528BNB%2529&sa=D&source=editors&ust=1724445405462083&usg=AOvVaw30v70tFB6frTlXlG9G6rrl>).
  7. Monero (XMR) - Also used for private transactions [1](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DMonero%2520%2528XMR%2529&sa=D&source=editors&ust=1724445405462375&usg=AOvVaw152FZlmjV3bRu1cR5Kc7X7>).
  8. Zcash (ZEC) - Offers private transactions as well [3](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DZcash%2520%2528ZEC%2529&sa=D&source=editors&ust=1724445405462694&usg=AOvVaw2Gt7d4Rm2q6QGnCKgcSmop>).
  9. Tether (USDT) - A stablecoin often used for transactions [23](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DTether%2520%2528USDT%2529&sa=D&source=editors&ust=1724445405463117&usg=AOvVaw1y5zsia6jsJIJY1d-bNCkN>).
  10. Cardano (ADA) - Known for its secure and scalable transactions [24](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DCardano%2520%2528ADA%2529&sa=D&source=editors&ust=1724445405463373&usg=AOvVaw20Kw3DtT5wqIYrzjOW6D86>).



#### Utility Tokens

  1. Ethereum (ETH) - Used for gas fees on the Ethereum network.
  2. Binance Coin (BNB) - Used for transaction fees on Binance.
  3. Chainlink (LINK) - Used to pay for services on the Chainlink network.
  4. Uniswap (UNI) - Used for governance and transaction fees on Uniswap.
  5. Filecoin (FIL) - Used to pay for storage on the Filecoin network.
  6. Basic Attention Token (BAT) - Used within the Brave browser ecosystem.
  7. VeChain (VET) - Used for supply chain management.
  8. Theta (THETA) - Used for decentralized video streaming.
  9. Golem (GLM) - Used to pay for computing power on the Golem network.
  10. Synthetix (SNX) - Used for creating synthetic assets on the Synthetix platform.



#### Governance Tokens

  1. Uniswap (UNI) - Allows holders to vote on protocol changes.
  2. Compound (COMP) - Used for governance in the Compound protocol.
  3. Maker (MKR) - Used for governance in the MakerDAO system.
  4. Aave (AAVE) - Used for governance in the Aave protocol.
  5. Curve DAO Token (CRV) - Used for governance in the Curve Finance protocol.
  6. SushiSwap (SUSHI) - Used for governance in the SushiSwap protocol.
  7. Yearn Finance (YFI) - Used for governance in the Yearn Finance protocol.
  8. Balancer (BAL) - Used for governance in the Balancer protocol.
  9. 1inch (1INCH) - Used for governance in the 1inch network.
  10. Kyber Network (KNC) - Used for governance in the Kyber Network.



#### Security Tokens

  1. tZERO (TZROP) - A security token for the tZERO platform.
  2. Polymath (POLY) - Used for creating and managing security tokens.
  3. Securitize (DS) - Used for digital securities on the Securitize platform.
  4. Harbor (HBR) - Used for compliance and issuance of security tokens.
  5. Swarm (SWM) - Used for tokenizing real-world assets.
  6. Tokeny (T-REX) - Used for issuing and managing security tokens.
  7. Blockstack (STX) - Used for decentralized applications and security tokens.
  8. Neufund (NEU) - Used for equity tokens on the Neufund platform.
  9. Science Blockchain (SCI) - A security token for the Science Blockchain fund.
  10. SPiCE VC (SPICE) - A tokenized venture capital fund.



#### Other

  1. Bitcoin (BTC) - The original and most well-known cryptocurrency [25](<https://www.google.com/url?q=https://bravenewcoin.com/insights/best-crypto-to-invest-today-august-2024-top-10-cryptocurrency-coins-to-buy-now-for-the-bull-run%23:~:text%3DBitcoin%2520%2528BTC%2529&sa=D&source=editors&ust=1724445405466283&usg=AOvVaw0-8xS_S_zuSn9W-by05ECI>).
  2. Ethereum (ETH) - A leading platform for decentralized applications [17](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DEthereum%2520%2528ETH%2529&sa=D&source=editors&ust=1724445405466801&usg=AOvVaw3mlyoQ5vzNmXrKIB26Ea53>)[18](<https://www.google.com/url?q=https://bravenewcoin.com/insights/best-crypto-to-invest-today-august-2024-top-10-cryptocurrency-coins-to-buy-now-for-the-bull-run%23:~:text%3DEthereum%2520%2528ETH%2529&sa=D&source=editors&ust=1724445405467082&usg=AOvVaw09wZUp5UqT25aMtCMah4gl>).
  3. Binance Coin (BNB) - Used within the Binance ecosystem [22](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DBinance%2520Coin%2520%2528BNB%2529&sa=D&source=editors&ust=1724445405467343&usg=AOvVaw2zvXyhRnYjfCdyLWiQE8zU>).
  4. Cardano (ADA) - Known for its secure and scalable transactions [24](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DCardano%2520%2528ADA%2529&sa=D&source=editors&ust=1724445405467604&usg=AOvVaw0CqdHHdIqGKVVmrzyM1lSQ>).
  5. Polkadot (DOT) - Aims to enable different blockchains to interoperate.
  6. Solana (SOL) - Known for its high-speed transactions.
  7. Avalanche (AVAX) - Focuses on high throughput and low latency.
  8. Chainlink (LINK) - Provides real-world data to smart contracts.
  9. Litecoin (LTC) - Often referred to as the silver to Bitcoin’s gold.
  10. Stellar (XLM) - Focuses on cross-border payments and remittances [21](<https://www.google.com/url?q=https://b2binpay.com/en/10-best-altcoins-to-accept-as-payment-in-2024/%23:~:text%3DStellar%2520%2528XLM%2529&sa=D&source=editors&ust=1724445405468178&usg=AOvVaw3hltMYzIhBRdKSioyT-Znk>).

---

### Post #3 — **accountnumber1** | 2024-08-26 14:57 UTC _(reply to #2)_

P.S. I am AKA ‘duckmatter’ on discord/the desight submission site.

Source code is available upon request.

---

### Post #4 — **yunusgumussoy** | 2024-08-26 17:12 UTC _(reply to #2)_

I enjoyed reading your report. Analysis of momentum-based indicators always interest me. I agree that SMA and MACD have an impressive predictive power in cryptocurrency price variance. I also like the way you approach to determining optimal window sizes and evaluating indicator performance across different cryptocurrency subsets. Your recognition of potential coding errors and the impact of data discretization reflects a balanced and realistic perspective

---

### Post #5 — **nishimoto** | 2024-08-27 04:58 UTC _(reply to #2)_

Thank you for your comments on my post and good report. I also enjoyed reading your report.

The idea of SMA-based MACD and the idea of categorizing the tokens by token type is interesting. Is the price movement similar for each type of token? I thought it would be more useful to classify them by price movement rather than by type.

---

### Post #6 — **accountnumber1** | 2024-08-27 10:47 UTC _(reply to #5)_

Thanks!

Categorizing the tokens by price movement is an alternative worth considering. Price movement can differ between types of coin, for example meme coins tend to have dramatic bubbles! How would you suggest identifying coins by price movement? Binning them by volatility, perhaps?

---

### Post #7 — **datahunter** | 2024-08-27 12:46 UTC _(reply to #6)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/a/f05b48/48.png) accountnumber1:

> Categorizing the tokens by price movement is an alternative worth considering. Price movement can differ between types of coin, for example meme coins tend to have dramatic bubbles! How would you suggest identifying coins by price movement? Binning them by volatility, perhaps?

Not sure if I’m right (weak on my finance skills), but maybe - Use RSI to categorize tokens into overbought, oversold, or neutral conditions, which can help identify potential price reversals or sustained trends (or) as you said Volatility, Calculate the standard deviation of daily or weekly price changes for each token over a specified period (e.g., 30 days, 90 days) maybe?

---

### Post #8 — **accountnumber1** | 2024-08-27 13:44 UTC _(reply to #7)_

Well, the idea is to categorise coins by type and then look at indicators like RSI to order the coins within each category. This means there is no point in using RSI or SMA to categorise coins, only to use the same indicator to order the coins within the categories! However, the idea of using one indicator to categorise and then another to order - for example, categorise by 90-day SMA and then order by 20-day SMA is quite intriguing. They will have to organise another contest so we can try new ideas!

---

### Post #9 — **mlh_alavi** | 2024-08-30 05:51 UTC

Wow!!! you have done a really great work  
the analysis and insights are well-studied  
good luck ![:love_you_gesture:](http://forum.numer.ai/images/emoji/twitter/love_you_gesture.png?v=12)
