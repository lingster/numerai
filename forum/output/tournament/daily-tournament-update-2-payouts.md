---
title: "Daily Tournament - Update #2 (Payouts)"
category: Tournament
url: https://forum.numer.ai/t/daily-tournament-update-2-payouts/6189
created_at: 2023-02-28T22:39:10.897000+00:00
last_posted_at: 2023-05-03T05:47:21.288000+00:00
posts_count: 6
views: 2756
tags: []
---

# Daily Tournament - Update #2 (Payouts)

---

### Post #1 — **slyfox** | 2023-02-28 22:39 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/16166b37467c13e9775e8c8d0e2b3c098ecc1ac0.png)image690×365 49.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/16166b37467c13e9775e8c8d0e2b3c098ecc1ac0.png> "image")

**Key Metrics**  
It has now been 4 months since the last update [initial launch](<http://forum.numer.ai/t/daily-tournaments/5766>) of daily tournaments. Adoption numbers looking strong and continue to grow every week. A huge thank you to everyone who has already migrated their model pipelines!

| Numerai | Signals  
---|---|---  
**Staked Models** | 45% | 30%  
**NMR staked** | 59% | 43%  
  
**Daily Tournament Payouts – starting May 1st**  
At a high level, the plan is to 1/5x payouts for 5x more rounds to keep overall weekly payouts roughly the same.

Recall our payout function below. 1/5x payouts is mathematically equivalent to dividing both the clip and the payout factor threshold by 5 in the payout function.

`payout = stake * clip(threshold/total_stake * (corr * cmult + tc * tmult))`

| Rounds Per Week | Payout Clip | PF Threshold (Numerai/Signals)  
---|---|---|---  
**Current** | 1x | 25% | 360K / 180K  
**New** | 5x | 5% | 72K / 36K  
  
These changes will take effect starting on May 1st 2023 (about 2 months out from today) to give everyone a final chance to migrate to daily if they haven’t done so already.

**What to expect**  
Models already submitting daily should expect roughly the same payouts after this change. Payouts may be temporarily higher due to the expected higher payout factor on daily rounds at least until we reach full adoption.

Models that are only submitting weekly should expect a 80% reduction in payouts after this change. If this is you then we recommend that you migrate to daily immediately!

**Compute & Automation**  
Do you need help with setting up your daily model pipeline? We want to help!

If you haven’t already, please check out one of our recommend solutions

  * [Numerai Compute](<https://docs.numer.ai/tournament/compute>) \- Our official low-cost and fully-featured framework to help you deploy your model pipeline to AWS. Best for big or complex model pipelines.
  * [Numerai Compute Lite (Beta)](<https://docs.google.com/document/d/1RCKgL4SAqEJ2atnMsdaPHdlV-d7pxJl9dB__mSx11CM/edit#>) \- A light weight version of compute designed to get you going in under 15 minutes! Best for small and simple model pipelines.
  * [Google Cloud Functions Example (Alpha)](<https://github.com/Raynos/numerai-example>) \- Don’t want to use our custom frameworks? Deploy your model to GCP using just the Google Cloud CLI.
  * [Local NGROK Example (Alpha)](<https://github.com/Raynos/numerai-example/tree/ngrok-test>) \- Don’t want to use the cloud at all? Deploy your model pipeline to your local machine using NGROK.



If you have any questions, please reach out to us on the [automation channel in rocketchat](<https://rocketchat.numer.ai/channel/automation>)!

**Improved submission endpoint flexibility – live now**  
One of the top feature requests we have heard from the community is to make the submission endpoint more flexible. Specifically, it seems to be difficult for some model pipelines to run within the 1 hour submission window of the new daily rounds. What can we do to help these models still participate in the daily tournament?

One solution that has been floated was to automatically “carry forward” late submissions in one round to the next. However, there are many UX issues with this as it muddies the simplicity of the current submission rule of “on-time good, late bad”. Should this be opt-in or opt-out? How should we display the status of these “queued” submissions?

A simpler solution is to just allow users to submit predictions from the previous round. So if your model takes too long to run and you miss the submission window of the current round, you are free to submit your predictions in the next round.

This feature is live now and supported in [NumerAPI version 2.13.2](<https://github.com/uuazed/numerapi>) or directly via our [GraphQl API](<https://api-tournament.numer.ai/>). All you need to do is to specify an additional `data_datestamp` argument to the submission endpoint.

---

### Post #2 — **unsentient** | 2023-03-02 03:19 UTC

Has the compute example been updated? I got one node up and running by following the example, but it only submits weekly.

---

### Post #3 — **slyfox** | 2023-03-21 17:37 UTC _(reply to #2)_

Hello unsentient,

Daily triggering for Compute is not enabled by default, but all you have to do is flip a switch in the compute modals on the website to enable daily compute triggers.

Just go to the Models page, click the three dots next to a model, select “compute” and flip the switch labeled “daily triggers”.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/57ae3620aa71d7a04da7295726c20c39abc0666c.png)image537×409 29 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/57ae3620aa71d7a04da7295726c20c39abc0666c.png> "image")

---

### Post #4 — **virgo94** | 2023-03-29 17:38 UTC _(reply to #3)_

The switch “daily trigger” no longer shows up for me as well…

---

### Post #5 — **ml_is_lyf** | 2023-03-29 19:33 UTC

[@slyfox](</u/slyfox>) [@pschork](</u/pschork>) not sure which of you is more appropriate to answer this, so I’ve tagged you both. There’s this forum post from a while back that explains how returns are calculated. Is it possible for you to do a similar one for the new payout format before daily tournaments go live so we can backtest using the new payout format?

![](http://forum.numer.ai/user_avatar/forum.numer.ai/pschork/48/2495_2.png) [Reproducing 1d, 3mo, 12mo staking returns the hard way](<http://forum.numer.ai/t/reproducing-1d-3mo-12mo-staking-returns-the-hard-way/5850>) [Tournament](</c/tournament/7>)

> Returns are meant to represent the return on a 1NMR stake over the give time frame. This post will explain the returns compounding logic and how users can validate these number themselves. The examples in this post are available in this [Google Sheet](<https://docs.google.com/spreadsheets/d/1uZmS93ZgDub1cpq0rjQNnaihfCG3b0IuA5ci-vCpgnY/edit?usp=sharing>). Note: Staking returns calculation currently only considers weekend rounds. We will update the returns calculation to include daily rounds when daily round payouts start. Staking returns calculation includes both resolved and unresolved round pa… 

In particular, how is the compounding going to work?

---

### Post #6 — **rpica** | 2023-05-03 05:47 UTC

Is legacy data going to be supported? Re-do all the models to adapt to the newer data versions is unfeasible for me ![:cry:](http://forum.numer.ai/images/emoji/twitter/cry.png?v=12) , it’s a lot of work that I can’t afford, unfortunately.
