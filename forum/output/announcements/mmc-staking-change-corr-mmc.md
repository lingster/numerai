---
title: "MMC Staking Change - Corr+MMC"
category: Announcements
url: https://forum.numer.ai/t/mmc-staking-change-corr-mmc/698
created_at: 2020-07-21T19:16:53.254000+00:00
last_posted_at: 2020-07-21T19:16:53.353000+00:00
posts_count: 1
views: 2849
tags: []
---

# MMC Staking Change - Corr+MMC

---

### Post #1 — **master_key** | 2020-07-21 19:16 UTC

## Summary

There will be an upcoming change to MMC staking. Starting for round 222, MMC stakes will be applied to both Corr and MMC.

## Payout Details

For example, if your round scores are `0.04 Corr`, and `-0.01 MMC`, your payout for the round would be `stake * 0.03`.

There is still a maximum risk of 25% of stake. So if `(Corr + MMC) < -0.25` or `(Corr + MMC) > 0.25`, then then your payout/burn will be clipped.

Notice that MMC is not multiplied by 2 as it is in the current MMC system.

Current MMC stakers will be automatically migrated to the new payout system for round 222. All in-progress rounds which have MMC selected will continue to be paid based on the current MMC*2 curve.

## Motivation

The decision to stake on MMC or Corr so far seems to be focused around predicting if your MMC or Corr will be better (and Corr has been great lately). This is a metagame that we see as a distraction, and we don’t want it to take away from the purpose of MMC: that is, to encourage you to build great unique models and get rewarded for them.

Having to sacrifice Corr payouts to play MMC was something that caused some of the best MMC users to still be better off selecting Corr payouts in some rounds. We think that if you have a model that scores well and is consistently improving the metamodel by having positive MMC, you should be rewarded for that. You shouldn’t have to try and guess whether MMC or Corr will have better payouts for you in the next round.

## Leaderboard

A secondary change will be to the leaderboard. We feel that having two leaderboards right now, MMC and Corr, is diluting the meaning and prestige of the leaderboard. For this reason, the leaderboard ranks will change to be Corr + MMC only.

Since for typical models Corr is significantly higher magnitude than MMC, Corr might still be the dominant factor for broad leaderboard positioning. However, having a model which is consistently finding good signal that few other models are finding will be the key to separating yourself at the very top of the leaderboard, and distinguishing yourself from the integration_tests of the world.

Reputation payouts are still in effect through September 9th, so the leaderboard change won’t take place until September 10th. This way the reputation payouts will continue as expected.

## Timeline

  * The staking interface will undergo minor updates to reflect these changes prior to Monday July 27th.
  * MMC Payouts for round 222, opening July 27, will be calculated as Corr + MMC, rather than MMC*2.
  * Reputation bonus will cease September 9th
  * Leaderboard will change to only show Corr + MMC ranks September 10th



Join the conversation on this recent post introducing the idea

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png)

[MMC Payouts Adjustment Proposal](<http://forum.numer.ai/t/mmc-payouts-adjustment-proposal/614>) [Data Science](</c/data-science/5>)

> Right now, we are in a historically great time for standard models, such as integration_test. Take a look at this chart of integration_test cumulative scores since Kazutsugi started. [[image]](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a9516ddfd306c7c3da557ceb2d6521a0855385a3.png> "image") The goal of MMC is to encourage users to find unique models that perform well. Right now though, even the models that we internally really like are preferring correlation payouts right now, even though they were the models that we specifically set out to reward more with MMC. Now, this trend is unlikely…
