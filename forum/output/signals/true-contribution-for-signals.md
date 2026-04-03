---
title: "True Contribution for Signals"
category: Signals
url: https://forum.numer.ai/t/true-contribution-for-signals/5505
created_at: 2022-06-15T04:11:11.998000+00:00
last_posted_at: 2022-06-15T04:11:12.122000+00:00
posts_count: 1
views: 1264
tags: []
---

# True Contribution for Signals

---

### Post #1 — **ark** | 2022-06-15 04:11 UTC

We recently released [True Contribution on Numerai](<http://forum.numer.ai/t/true-contribution-details/5128>).

True Contribution computes the value of adding a new signal into Numerai’s Meta Model. We have now built True Contribution into Signals. It takes the signal you’ve submitted to Numerai Signals and calculates its True Contribution with respect to all **all stake-weighted predictions** in Numerai’s Meta Model (including Tournament and Signals; Numerai Tournament TC will not change).

We prepare each signal as follows:

  * Percent-rank the signal with no tie-breaking
  * fill missing predictions with 0.5
  * Rank again with no tie-breaking
  * normalize into a gaussian distribution (we do this for Numerai predictions too)
  * include all signals submitted to Numerai Signals in the same Meta Model as Numerai predictions at their current stake value.



The 20-round Signals TC Leaderboard (rounds 291 - 310) has moderate correlation with the Corr and MMC leaderboards, but lower correlation with the IC leaderboard:
    
    
    corr_20d_rep    0.400512
    mmc_20d_rep     0.366898
    ic_rep          0.079883
    

Along with its relationship to existing metrics, Signals TC could be easy to optimize for if we start showing something called RIC - the Residual Information Coefficient - which is a signals correlation with residual returns. Stay tuned for updates on RIC, medal announcements, and staking.
