---
title: "MMC and other metrics for all targets"
category: Tournament
url: https://forum.numer.ai/t/mmc-and-other-metrics-for-all-targets/6839
created_at: 2023-12-04T17:39:25.813000+00:00
last_posted_at: 2023-12-17T14:09:45.410000+00:00
posts_count: 7
views: 934
tags: []
---

# MMC and other metrics for all targets

---

### Post #1 — **nasdaqjockey** | 2023-12-04 17:39 UTC

I trained models using LightGBM with the parameters shown on the charts for each target. This test used cyrus 20 as the scoring target and `scoring.contributive_correlation()` to estimate MMC and other metrics for the validation data. The other metrics are correlation, standard deviation, sharpe, and consistency across eras. Consistency is simply the count of the eras where correlation > 0.01 divided by the number of eras.

Here are the targets with the best MMC:

[![1](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e83f5159d7a3cc9500842b7c39f1b02732af9961.jpeg)1629×107 29.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e83f5159d7a3cc9500842b7c39f1b02732af9961.jpeg> "1")

Even though rowan 20 has a slightly higher MMC, teager 20 and claudia 20 have better Sharpe and consistency values. The targets that had the best correlation (and consistency) are…

[![2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0357cdf57edd70c3b81d33ce67e2983a434abcdf.jpeg)2635×107 29.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0357cdf57edd70c3b81d33ce67e2983a434abcdf.jpeg> "2")

I assume cyrus 20 has the best correlation since it was used in the correlation metric.  
This is just a starting point to see which targets may perform better.

Here are some charts and the data for all the tests:

[![3](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/fc3671566f462348d7680eb4f044eecaf3d66b8b_2_690x354.png)3830×427 130 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fc3671566f462348d7680eb4f044eecaf3d66b8b.png> "3")

  


[![4](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e0400ac6c788bda66b2fcf533a4a21983e257f0c_2_690x354.png)4830×427 131 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e0400ac6c788bda66b2fcf533a4a21983e257f0c.png> "4")

  


[![5](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/52b0e7ea8c77e3473f00a79ee7e65047254b181b.png)5367×864 62 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/52b0e7ea8c77e3473f00a79ee7e65047254b181b.png> "5")

---

### Post #2 — **pumplerod** | 2023-12-06 03:06 UTC

was this using all the features or were you using “medium” features_set as in the example models?

---

### Post #3 — **nasdaqjockey** | 2023-12-06 12:23 UTC

All features were used.

---

### Post #4 — **bulldozer** | 2023-12-13 03:24 UTC

On a similar note, I ran a comparative test between CORR and MMC metrics on my main model today using the main target. My key takeaways were:

  1. MMC and CORR are positively correlated, so training on CORR still makes sense
  2. MMC Sharpe is about half of CORR Sharpe but still attractive
  3. Average MMC is about 10x smaller than average CORR (aligned with your numbers)



However, I believe the expected return-on-risk must be kept high for innovative models as a compensation for the volatility in NMR. So hopefully, these two things will happen after the transition:

  * Higher payout factor thanks to a reduction in high stake models under-performing benchmarks
  * Large MMC multipliers on offer



All we have to do now is wait and hope for the best!

---

### Post #5 — **gammarat** | 2023-12-13 15:49 UTC _(reply to #4)_

I just did the same, my corr and mmc results are pretty close:

[![SharpeComp](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/590a95fc0d3dc5c50dea363defecd31337829c80.jpeg)SharpeComp560×420 12.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/590a95fc0d3dc5c50dea363defecd31337829c80.jpeg> "SharpeComp")

---

### Post #6 — **eleven_sigma** | 2023-12-16 14:45 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nasdaqjockey/48/2933_2.png) nasdaqjockey:

> contributive_correlation

Thanks.  
Which are the validation eras used?  
Have you compute for several seeds to see the estimation error of the metrics?

---

### Post #7 — **nasdaqjockey** | 2023-12-17 14:09 UTC

For MMC I used filter_sort_index(predictions, meta_model) and for CORR I used filter_sort_index(predictions, validation) so all eras with no NaNs are used.

I did not use several seeds. My intent was to get a relative comparison between the targets as a sanity check. I also computed the same metrics for all the benchmark models shown here:  


[![benchmarks](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/01e2469567d1feaf7677dd0e641cd03ba7ecf49b.png)benchmarks571×766 60.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/01e2469567d1feaf7677dd0e641cd03ba7ecf49b.png> "benchmarks")
