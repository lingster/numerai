---
title: "Signals will soon change to a 20 day target"
category: Announcements
url: https://forum.numer.ai/t/signals-will-soon-change-to-a-20-day-target/3898
created_at: 2021-08-02T19:55:59.080000+00:00
last_posted_at: 2021-08-02T19:55:59.180000+00:00
posts_count: 1
views: 1921
tags: []
---

# Signals will soon change to a 20 day target

---

### Post #1 — **_liamhz** | 2021-08-02 19:55 UTC

From round 279 onwards (August 28th), Signals will use a 20 day target for scoring and payouts.

We believe that this longer horizon target will increase user payouts on Signals, and incentivise signals that are more valuable to Numerai’s metamodel and hedge fund.

### What will change

Signals rounds will resolve after ~4 weeks instead of the current 1 week. The first daily score of a round will be released on Friday, and the last daily score on the Thursday 4 weeks later.

Here’s what the new scoring schedule looks like

[![Corr20 Calendar2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/ccb7e458a354eca07c041a20211dcd5ebb898399_2_541x500.png)Corr20 Calendar21370×1265 36.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/ccb7e458a354eca07c041a20211dcd5ebb898399.png> "Corr20 Calendar2")

This new scoring schedule means that Signals will have overlapping rounds, similar to the regular Numerai tournament. In addition to rounds resolving after ~4 weeks instead of 1 week, NMR stake compounding (from round payouts) and stake decrease requests will be processed after a ~4 week delay rather than a ~1 week delay.

Currently, the historical targets file we give out has two target columns: `target` and `target_20d`. The column named target will be renamed to `target_4d`. `target_20d` will maintain its column name.

The Signals website will be updated to show Corr20 and MMC20 reputations on the leaderboard. For all other charts and tables (e.g. model performance / rank / rep charts, round performance table) existing values will not be changed, but for round 279 onwards will display values for Corr20 and MMC20. Medals from old rounds will be kept, and new medals will be awarded for scores on the 20 day target.

#### Summary of changes

  * From round 279 onwards (August 28th), Signals will use a 20 day target for scoring and payouts
  * Rounds will take ~4 weeks to resolve
  * Stake decreases will take ~4 weeks to resolve
  * `target` is being renamed to `target_4d` in the historical targets file
  * Signals leaderboard will only display Corr20 and MMC20 reputations



### What You’ll Need to Do

Updating your model to train and predict for the new target may be as simple as changing the name of the target column you use. Here’s the one line [commit](<https://github.com/numerai/example-scripts/pull/84/commits/9eb697f93ec981967b9a6edaff17ff85b9c1397d>) needed to update the Signals’ example_model.py for 20d scores.

You may also want to consider changing which features you use or other aspects of your model - but this is up to you.

If you do nothing, your current Signals stakes will automatically be converted to a 4 week stake. If you don’t want your stake to be converted, unstake your model before staking for round 279 closes.
