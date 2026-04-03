---
title: "Is NMR Decorrelated from other Crypto Assets? A small study"
category: Numeraire
url: https://forum.numer.ai/t/is-nmr-decorrelated-from-other-crypto-assets-a-small-study/5315
created_at: 2022-04-26T01:22:41.833000+00:00
last_posted_at: 2023-03-07T12:00:16.809000+00:00
posts_count: 5
views: 2110
tags: []
---

# Is NMR Decorrelated from other Crypto Assets? A small study

---

### Post #1 — **aventurine** | 2022-04-26 01:22 UTC

**Decorrelate NMR?**

“As institutional investors [and retail traders] evaluate crypto assets, how can they think about properly assessing their risks, especially in the context of a broader, multi-asset class portfolio?”

The **Pearson Correlation Coefficient** quantifies the estimated strength of the linear association between two variables. It ranges from +1 to -1: +1 indicates a perfect positive linear correlation, -1 a perfect negative linear correlation, 0 indicates no linear correlation. The charts below represents the change in the correlation over time (rolling correlation with a rolling window width of 20 data points).

The **Confidence Interval** represents the interval in which the true Pearson correlation coefficient will be located with 95% probability. If the confidence interval includes the value of zero (it crosses the dashed line), the correlation can be regarded as non-significant (not different from 0).

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0c448bd2140d532891bd96cfe14478cc5097d4bb.png)image730×219 11.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0c448bd2140d532891bd96cfe14478cc5097d4bb.png> "image")

As like this TwoSigma article: [Risk Analysis of Crypto Assets - Two Sigma](<https://www.twosigma.com/articles/risk-analysis-of-crypto-assets/>)  
to compare correlations, we first need to establish a universe of crypto assets to create correlation matrices. I have chosen for this universe of crypto assets BTC, ETH, the top 5 “data” coins as well as Doge and the S&P 500 for further analysis. It was found in the TwoSigma article above that Doge appeared most unique compared to their chosen universe so will the same follow here?

With the past 24hr spike in $NMR how do our correlations look?  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/46c48ecdf24a3358ffe60d47f69bf8491409b45c_2_690x449.png)image964×628 47.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/46c48ecdf24a3358ffe60d47f69bf8491409b45c.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/772b37d1524d2e08b48b4b77404045926319852a_2_690x314.png)image1565×713 87.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/772b37d1524d2e08b48b4b77404045926319852a.png> "image")

As you would expect, $NMR was one of the most decorrelated assets over the past 24hrs from all other assets in our universe. BTC/ETH kept a very tight correlation of 98% while $NMR to $BTC and $ETH were 40% and 46% respectively.

How does this change over 30days and 1 year?  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e0f60ca5739467beba1421cf4298b2b9de83f148_2_690x320.png)image1577×733 101 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e0f60ca5739467beba1421cf4298b2b9de83f148.png> "image")

Over 30 days we see a big change from the 24hr window. NMR is mostly correlated with all assets in our universe, even with the S&P. $NMR keeps a correlation over 90% for both BTC and ETH. Interestingly though, Doge is the odd one out with less than 50% correlation to almost every asset.

Would this correlation hold out to 1 year?  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/420a0343264e8818d602163f82eb855a7e60d7cd_2_690x302.png)image1664×729 96.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/420a0343264e8818d602163f82eb855a7e60d7cd.png> "image")

This is where things get a bit interesting. $NMR is keeping a fairly tight correlation to most of the other “data” coins as well as Doge but when we look at correlation to BTC, ETH and the S&P we see a noticeable decorrelation. $NMR is very decorrelated from the S&P with a -29% correlation. Looking at BTC and ETH we see correlations of 51% and 32% respectively. Doge keeps its low correlation to BTC, ETH and the S&P 500 but interestingly, has a high correlation to mostly all “data coins”(Is NMR a meme coin?) ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13) . As with the TwoSigma article, BTC and ETH has kept a very consistent correlation to each other over various time frames.

In conclusion, although we find that BTC and ETH are highly correlated with each other, NMR over the long term does seem to show a deviation from BTC and ETH. It is also negatively correlated with the S&P.

---

### Post #2 — **25sigma** | 2022-04-26 12:47 UTC

Very curious what the correlation numbers are for HEX comparisons too. Thank you for this study. Been needing correlations. This helps tremendously.

---

### Post #3 — **andralienware** | 2023-03-04 19:20 UTC

As a quick aside, what software did you use to make the correlation graphics?

---

### Post #4 — **thornam** | 2023-03-05 13:48 UTC

Very interesting!  
Thanks for the small study. I think it’s very helpful with more of these small studies in NMR to get a better understanding of the NMR risk. Personally I see the NMR as the biggest challenge to use the Numerai tournaments as a real investment. With a less volatile NMR (less risk) people would probably put more real money into the Numerai universe and thereby have an even larger incentive to use time and effort for creating new/good models, which would ultimately benefit Numerai as a whole.

So a “Nice job” from here!

---

### Post #5 — **lcrmorin** | 2023-03-07 12:00 UTC

Are you looking at correlations of prices or returns ?
