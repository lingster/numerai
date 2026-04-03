---
title: "Q3 End-of-Quarter Updates"
category: Announcements
url: https://forum.numer.ai/t/q3-end-of-quarter-updates/4265
created_at: 2021-10-04T22:46:07.429000+00:00
last_posted_at: 2021-10-04T22:46:07.544000+00:00
posts_count: 1
views: 1365
tags: []
---

# Q3 End-of-Quarter Updates

---

### Post #1 — **ark** | 2021-10-04 22:46 UTC

**Compute 0.3.1**

In this update, we’ve added a new cron trigger functionality, meaning you can schedule your data pipelines or models to run in the cloud whenever you want. It also includes several bug fixes and infrastructure updates. Be sure to follow the [upgrade guide](<https://github.com/numerai/numerai-cli#upgrading>) to get these updates.

**Signals Diagnostics**

We have migrated Signals to our new diagnostics architecture, meaning you can now find the new Diagnostics Tool at [signals.numer.ai](<http://signals.numer.ai>) too. This contains all the Signals diagnostics you’re familiar with and is available 24/7 just like the Numerai Tournament. This is meant to replace the diagnostics you receive after submitting. The old method of receiving diagnostics will be discontinued in the coming weeks.

**TB 200, Autocorr, Adjusted Sharpe, and APY**

We are introducing new diagnostics for both Tournament and Signals.

Top/Bottom 200 (TB 200) is a copy of all diagnostics on the top 200 stocks and the bottom 200 stocks you submit predictions for; the ones that represent your most extreme predictions.

Along with this new set of diagnostics we will also be including Autocorrelation and an Adjusted Sharpe Ratio. This 1-era-lagged Autocorrelation (Autocorr) is useful in determining how repetitive your scores are over time - a high Autocorr (near 1) means that good scores this round show a higher probability of good scores next round, and vice versa. The Adjusted Sharpe Ratio accounts for skewness and kurtosis of your scores, meaning that you can get a better idea of the actual risk/reward ratio.

Finally, we will be adding Annual Percentage Yield (APY) to the Classic Tournament diagnostics, to provide an idea of the potential profitability of your models. This will bring Tournament Diagnostics into parity with Signals Diagnostics.

Here’s a preview in the Numerai Tournament page:  
![tourny_diagnostics](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b77e3653aa923b85e9d2db2949b31ca2ce5f71aa.gif)

And a preview for Signals:  
![signals_diagnostics](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4e7247d1d203608d9d8f64c17f8f9a5516065bb7.gif)
