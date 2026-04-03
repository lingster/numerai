---
title: "Crypto Factor Modeling for evaluating crypto return"
category: Data Science
url: https://forum.numer.ai/t/crypto-factor-modeling-for-evaluating-crypto-return/7688
created_at: 2024-08-27T12:16:52.051000+00:00
last_posted_at: 2024-08-27T20:28:15.497000+00:00
posts_count: 9
views: 595
tags: []
---

# Crypto Factor Modeling for evaluating crypto return

---

### Post #1 — **mlh_alavi** | 2024-08-27 12:16 UTC

**Introduction**

Crypto factor modeling is an approach used to analyze and predict the return of cryptocurrencies by identifying and assessing various factors that influence their returns. These factors can include market trends, liquidity, volatility, momentum, and other economic indicators. By modeling these factors, investors and analysts can gain insights into the potential risks and opportunities within the crypto market, helping to inform investment strategies and portfolio management decisions.  
In this work , using market factors like Momentum, Value_Factor , size_factors , … and economic factors like inflation rate, unemployment_rate , … and also environment factors like google trends we tried to investigate and analyze the behavior of nearly 120 cryptos over time.  


[![1_vZy9QeLFX4QaYSy8WUoWxg](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c961b81d0fd5e8be885bfe27f4294a880be630a8_2_690x426.jpeg)1_vZy9QeLFX4QaYSy8WUoWxg995×615 67.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c961b81d0fd5e8be885bfe27f4294a880be630a8.jpeg> "1_vZy9QeLFX4QaYSy8WUoWxg")

**key findings**  
**Correlation Analysis:** The research identified strong correlations among market factors, particularly between returns and HML (High Minus Low) factors, indicating that these factors significantly influence cryptocurrency performance.

**Impact of Economic Factors** : Economic indicators like the Federal Funds Effective Rate and inflation expectations showed weak correlations with cryptocurrency returns, suggesting limited predictive power when analyzed in isolation.

**Modeling Results:** The OLS regression models indicated that HML and momentum are significant predictors of returns, while other factors like market cap and volatility did not show significant effects.

**Residual Analysis** : The residuals from the regression models displayed patterns suggesting potential heteroscedasticity, indicating that the variance of errors may change with different levels of predicted values.

**Google Trends Influence** : Although Google Trends data was included in the analysis, it showed weak correlations with cryptocurrency returns, indicating it may not be a strong standalone predictor.

**Liquidity Metrics** : The analysis of liquidity across tokens revealed that higher liquidity is generally associated with better market performance, although this relationship was not uniformly strong.

**Market Dynamics:** The findings suggest that market dynamics, particularly momentum and value factors, play a critical role in forecasting cryptocurrency returns, which could aid investors in making informed decisions.

**Conclusion**

The report provides a comprehensive analysis of various factors influencing cryptocurrency returns, emphasizing the importance of market and economic indicators. The significant correlation between HML and momentum with returns suggests that these factors should be prioritized in investment strategies.  
However, the limitations in predictive power of certain economic indicators highlight the complexity of the crypto market, necessitating further research and model refinement.  
Overall, the insights gained from this study can assist investors and analysts in navigating the volatile cryptocurrency landscape. By leveraging the identified factors and understanding their interactions, stakeholders can enhance their investment strategies and improve portfolio management decisions.

you can read the complete report from [here ](<https://github.com/mlh-ps/crypto-factor-modelling-/blob/main/crypto-factor-modelling-report.pdf>)  
also you can access to the source code from this [link](<https://github.com/mlh-ps/crypto-factor-modelling->)

feel free to ask any further question ![:relieved:](https://emoji.discourse-cdn.com/twitter/relieved.png?v=13)

---

### Post #2 — **datahunter** | 2024-08-27 12:42 UTC

Hey [@mlh_alavi](</u/mlh_alavi>), Wasn’t able to read the report (access issues maybe?), but yeah, excited to read! Do drop some feedback on mine, I’ll keep that in mind to improve in the future!

---

### Post #3 — **yunusgumussoy** | 2024-08-27 13:36 UTC

I couldnt access to the report. Can you check links again?

---

### Post #4 — **accountnumber1** | 2024-08-27 13:39 UTC

Can’t see either link. Did you mean [GitHub - mlh-ps/github-crypto-desight](<https://github.com/mlh-ps/github-crypto-desight>) ?

---

### Post #5 — **mlh_alavi** | 2024-08-27 16:09 UTC _(reply to #2)_

thank you for informing me … can you check it again please , I changed the accessibility of my github

---

### Post #6 — **mlh_alavi** | 2024-08-27 16:16 UTC _(reply to #3)_

thank you so much , I changed the accessibility … would you check it again please ?

---

### Post #7 — **mlh_alavi** | 2024-08-27 16:16 UTC _(reply to #4)_

no that’s the link of previous challenge … would you check it again please ??

---

### Post #8 — **accountnumber1** | 2024-08-27 16:28 UTC _(reply to #7)_

Yeah I can see it now.

---

### Post #9 — **datahunter** | 2024-08-27 20:28 UTC _(reply to #5)_

Really liked the analysis! Really elaborate and very well presented, definitely one of the top submissions indeed. I like how you found a balance between momentum, size, trends and market factors.
