---
title: "Stake Decrease Proposal"
category: Feedback
url: https://forum.numer.ai/t/stake-decrease-proposal/361
created_at: 2020-05-09T02:53:15.255000+00:00
last_posted_at: 2020-05-09T02:53:15.511000+00:00
posts_count: 1
views: 1203
tags: []
---

# Stake Decrease Proposal

---

### Post #1 — **budbot** | 2020-05-09 02:53 UTC

Numerai Stake Decrease Proposal

Hi all, this is just my thoughts on digital paper on a potential way that users can get some of those sweet sweet gains earlier when decreasing stakes. Interested in thoughts. This system allows for payments along the way and a 3 week decrease period instead of 4. Thanks

STAKE DECREASES AND UNRESOLVED ROUNDS

Currently when you initiate a stake decrease in week 0, numerai is unable to execute this decrease into your wallet immediately as there are still four rounds of unresolved payouts on your stake value prior to initiating the decrease. In each of these 4 rounds the unresolved loss is up to 25% of your stake so you could have losses of up to 100% on your pre-decrease stake still pending.

PROGRESSIVE RELEASE BASED ON MAXIMUM LOSS

As these four rounds resolve though your maximum potential loss decreases significantly, meaning that numerai could gradually reduce the amount it holds as security over the decrease period. It requires a slight change in thinking about decreases though from a fixed NMR amount to a % amount of your stake.

This is the basic concept:

  * In week 0, you initiate a decrease of 50% of your stake
  * Over the next 4 weeks (as the rounds which have your pre-decrease stake resolve), numerai will continue to calculate your “Gross stake” amount as normal as if no decrease was made.
  * This “Gross stake” will then be used to calculate your “At stake” and “Pending decrease” based on your decrease %
  * In this case 50% of your gross stake will be your “At stake” and 50% will be your “Pending decrease”
  * Your pending decrease is now having unrealized gains/losses rolled into it just like your stake
  * As each round resolves numerai will calculate the “Maximum unrealized loss” that could occur to your decrease amount and release any funds above this amount still owing into your wallet



WHY A PERCENTAGE DECREASE?

Having the decrease as a fixed % rather than a fixed amount of NMR is critical as this allows unrealized gains and losses to be apportioned between your “Pending decrease” and your “At stake” Currently all your unrealized losses are taken out of your “At stake” which could result in your stake going negative. Apportioning gains/losses between your “At stake” and “Pending decrease” prevents this from happening and is what allows numerai to progressively release funds early.

EXAMPLE DECREASE SCENARIO

During the week of round 207, you initiate a stake decrease of 50%, at this point we don’t know the gains/losses of rounds 204-207 for the “At stake” amount of 94NMR, so we won’t know if you will have enough money to have the full decrease paid into your wallet. We DO know however what the maximum unresolved loss is, which is the sum of 25% of the stake values for those rounds. In this case the maximum loss at Week 0 is 100NMR. So we’re gonna need to hold onto that decrease as collateral.

Side Note: The maximum loss actually already exceeds the amount “At stake”, so while extremely unlikely, theoretically you can still go negative even without initiating a decrease [@slyfox](</u/slyfox>)???!!!

[![stake table](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/b4c598c52916f78f34c08077b3c4693f2c277354.png)stake table1117×346 17.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/b4c598c52916f78f34c08077b3c4693f2c277354.png> "stake table")

ROUND 204 RESOLVES

Week 1, Round 204 resolves, you realize a loss of -10NMR (you trained on val2 didn’t you?), your gross stake is now 94-10 = 84NMR. 50% of the loss was rolled into your “At stake”, 50% is rolled into your “Pending decrease”. Now that round 207 has resolved we have realized those losses from your “At stake” and “Pending withdrawal”. You have an “At stake” of 42NMR for round 208 and a “Pending decrease” of 42NMR.

Following the resolution of round 204, the remaining maximum loss on your pending withdrawal is 50% of the maximum loss for rounds 205-207 (as we’ll only be taking half those losses out of your stake) which is 0.5*77 = 38.5NMR. Note that your maximum loss is now 3.5NMR less than your pending decrease so numerai no longer needs to hold onto this and it can be paid into your wallet.

ROUND 205 RESOLVES

On the resolution of round 205 you have a loss of -5 NMR, this is apportioned as above and it turns out that there is an extra 9.75 NMR that numerai no longer needs to hold on to, So after the resolution of round 205 you’ve been paid a total of 13.25 NMR into your wallet.

ROUND 206 RESOLVES

Round 206 resolves and disaster strikes, you have a correlation of -0.99, your loss is a full 25% of the stake for that round which is -29NMR. Unfortunately, this means that 50% of that loss – 14.5NMR - gets rolled into your “Pending decrease”. Your change in maximum loss on the resolution of 206 is also 14.5NMR so you get no additional funds paid into your wallet.

ROUND 207 RESOLVES

Round 207 resolves, happy days, you’re back in black! 50% of this gain is rolled into your pending decrease and, being the last unresolved round – the maximum loss has reduced to 0. Numerai pays you the remained of the amount owing – 19.25NMR - into your wallet. You’ve now been paid a total of 32.5 NMR which is 50% of your gross stake.

SOME NOTES

Note: that bonuses were ignored but they can be included in with the normal payout calculations.

Note: that this scenario is very pessimistic. If you have lower losses or even more gains (including bonuses) the amount that would be paid into your wallet week to week would be much higher.

Note: Once a decrease is in progress that’s it, no going back until it is complete.
