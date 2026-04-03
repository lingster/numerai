---
title: "Introducing the Crypto Price Variance Model (CPVM)"
category: Data Science
url: https://forum.numer.ai/t/introducing-the-crypto-price-variance-model-cpvm/7690
created_at: 2024-08-27T13:51:18.478000+00:00
last_posted_at: 2024-08-27T14:36:54.304000+00:00
posts_count: 2
views: 439
tags: []
---

# Introducing the Crypto Price Variance Model (CPVM)

---

### Post #1 — **polymawutor** | 2024-08-27 13:51 UTC

[![correlation_heatmap](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/83435f7318973cb19402a933eff10c4ba12c8724_2_600x500.png)correlation_heatmap1200×1000 54.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/83435f7318973cb19402a933eff10c4ba12c8724.png> "correlation_heatmap")

# Abstract

We introduce the Crypto Price Variance Model (CPVM), a novel approach to understanding and predicting cryptocurrency price movements. Building upon the foundation of the Fama-French model, the CPVM incorporates three key factors: Price Momentum, Fear & Greed Index, and Interest Rates. These factors were identified through a comprehensive correlation analysis of various economic indicators against crypto price variance. The model aims to provide a more tailored and relevant framework for analyzing cryptocurrency markets, addressing the unique characteristics and dynamics of this emerging asset class. While the CPVM offers valuable insights into the drivers of crypto price variance, it also acknowledges the limitations inherent in applying traditional financial models to the rapidly evolving and often unpredictable crypto landscape. This research contributes to the growing body of knowledge on cryptocurrency valuation and risk assessment, offering both practitioners and researchers a new tool for understanding this complex market.

GitHub Repository (Research Report, Datasets, Code Samples, and Charts): <https://github.com/polymawutor/cpvm>

---

### Post #2 — **polymawutor** | 2024-08-27 14:36 UTC

### Sample Size

Using data from CoinMarketCap, we limited our analysis to crypto assets with a market cap greater than USD 100 million. As of August 24 at 10:00 UTC, this criterion yields 357 crypto assets.

Among these, we identified 17 stablecoins—crypto assets pegged directly to the value of the USD. Since stablecoins are designed to maintain a constant value and do not exhibit the price variability we are interested in, we excluded them from our analysis. This leaves us with 340 crypto assets, which served as the foundation for our study.

### Factor Selection

To build a model around the most relevant factors influencing average quarterly price variance, we aim to identify the top three factors most highly correlated with price variance from a pool of seven potential factors. We constructed a correlation matrix to assess the relationships between six factors and the average quarterly price variance.

Below are the results from the correlation matrix:  


[![correlation_heatmap](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/83435f7318973cb19402a933eff10c4ba12c8724_2_600x500.png)correlation_heatmap1200×1000 54.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/83435f7318973cb19402a933eff10c4ba12c8724.png> "correlation_heatmap")

Top 3 Highly Correlated Factors with Price Variance:

  1. Price Momentum: 0.6049
  2. Fear & Greed Index: 0.2508
  3. Interest Rate: 0.2011



### The CPVM

**The model can be expressed as:**
    
    
    E(R) = Rf + β1(PM - Rf) + β2(FGI) + β3(IR)
    

Where: E(R) = Expected return of the cryptocurrency Rf = Risk-free rate PM = Price Momentum factor FGI = Fear & Greed Index factor IR = Interest Rate factor β1, β2, β3 = Factor coefficients (sensitivities)

### Detailed Explanation

  1. Risk-free rate (Rf): This represents the return an investor can expect from a risk-free investment. In the crypto context, this could be the yield from stablecoin lending or a traditional short-term government bond rate.
  2. Price Momentum factor (PM - Rf): This factor captures the tendency of crypto assets that have performed well in the recent past to continue performing well. It’s calculated as the difference between the returns of high-momentum and low-momentum cryptocurrencies.
  3. Fear & Greed Index factor (FGI): This factor represents market sentiment. It captures the psychological aspects of the crypto market, which can significantly influence price movements.
  4. Interest Rate Factor (IR): This factor accounts for the impact of broader economic interest rates on crypto prices. It could be based on global average short-term interest rates or a specific benchmark rate.
