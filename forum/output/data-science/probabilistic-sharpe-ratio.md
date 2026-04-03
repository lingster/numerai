---
title: "Probabilistic Sharpe Ratio"
category: Data Science
url: https://forum.numer.ai/t/probabilistic-sharpe-ratio/446
created_at: 2020-05-21T17:25:30.164000+00:00
last_posted_at: 2020-07-01T14:34:12.176000+00:00
posts_count: 5
views: 3408
tags: []
---

# Probabilistic Sharpe Ratio

---

### Post #1 — **richai** | 2020-05-21 17:25 UTC

From [@jrai](</u/jrai>) in the forums, a nice description with code of probabilistic sharpe. Has anyone written a version of this for Numerai? Of course on Numerai, we don’t use returns but instead correlation with the target but perhaps this idea can be used as a way to choose models that generalize much better out of sample. I think things like skewness, kurtosis will matter for your distribution of era correlations for the same reasons.

<https://quantdare.com/probabilistic-sharpe-ratio/>

---

### Post #2 — **richai** | 2020-05-21 17:32 UTC

Can anyone show with cross validation whether it’s better to optimize for probabilistic sharpe than smart sharpe from [@mdo](</u/mdo>)?

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png)

[Performance Stationarity](<http://forum.numer.ai/t/performance-stationarity/151/2>) [Data Science](</c/data-science/5>)

> Great post Richard, much appreciated! These issues have been on my mind recently as I’ve been playing around with fitting models to feature neutral targets. I’ve been testing out the Sortino ratio as an alternative to Sharpe for doing hyperparameter selection, because it makes sense to me to only penalize downside volatility/variance. Interestingly I’m finding that Sortino does favor different and narrower ranges of hyperparameters than Sharpe. def sortino_ratio(x, target=.02): xt = x - tar…

---

### Post #3 — **jrai** | 2020-05-21 19:00 UTC

here is some of the code (not by me):

  * <https://github.com/rubenbriones/Probabilistic-Sharpe-Ratio/blob/master/src/sharpe_ratio_stats.py>
  * <https://github.com/rubenbriones/Probabilistic-Sharpe-Ratio/blob/master/notebooks/Probabilistic%20Sharpe%20Ratio%20Example.ipynb>



May also be helpful in Numerai Quant

---

### Post #4 — **of_s** | 2020-05-22 17:57 UTC

Better confidence intervals around a flawed metric is still a…flawed metric. What this adjustment is trying to get at is to maximize the upside variance / downside variance, which partial moments already do.

---

### Post #5 — **arbitrage** | 2020-07-01 14:34 UTC

Adjusted Sharpe ratio was introduced by Pezier (2005) in:

Alexander, Carol and Sheedy, Elizabeth, eds. (2005) _The professional risk managers’ handbook: a comprehensive guide to current theory and best practices._ PRMIA Publications, New York & London. ISBN 9780976609704

Adjusted Sharpe Ratio adjusts for skewness and kurtosis by incorporating a penalty factor for negative skewness and excess kurtosis.

The formula is given in a different paper since i couldn’t access the book:

*NOTE: Carol Alexander is a personal friend/mentor

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/5eab232227a53e3f87d607ceec741a1cf43eb1e7_2_563x500.jpeg)image729×647 151 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/5eab232227a53e3f87d607ceec741a1cf43eb1e7.jpeg> "image")

I calculate the adjusted sharpe ratio which adjusts for Numerai’s trading costs as well:
    
    
    import numpy as np
    import scipy
    from scipy.stats import skew, kurtosis
    
    def annual_sharpe(x):
        return ((np.mean(x) -0.010415154) /np.std(x)) * np.sqrt(12)
    
    def adj_sharpe(x):
        return annual_sharpe(x) * (1 + ((skew(x) / 6) * annual_sharpe(x)) - ((kurtosis(x) - 3) / 24) * (annual_sharpe(x) ** 2))
    

You should pass validation scores to these functions since they are monthly; adjust to weekly compounding to use this on your live performance.
