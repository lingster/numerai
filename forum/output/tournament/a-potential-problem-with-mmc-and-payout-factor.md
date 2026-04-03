---
title: "A potential problem with MMC and payout_factor"
category: Tournament
url: https://forum.numer.ai/t/a-potential-problem-with-mmc-and-payout-factor/2703
created_at: 2021-04-05T20:37:24.605000+00:00
last_posted_at: 2021-04-06T12:15:59.807000+00:00
posts_count: 6
views: 1445
tags: []
---

# A potential problem with MMC and payout_factor

---

### Post #1 — **liz** | 2021-04-05 20:37 UTC

I want to acknowledge up front that my understanding of the mathematics underpinning MMC is not as deep as I would prefer. I welcome feedback or expansion on any ideas here if other posters feel it is helpful or clarifying.

As we approach a phase in the life of the Classic Numerai tournament in which payout_factor will come into play, I believe I have identified a potential flaw of MMC that is worth avoiding, to maximize unique signal for the fund, and minimize metastrategy elements to the tournament that incentivize individuals to behave in a way that benefits themselves, but hurts other modelers, and more importantly (to the fund) hurts Numerai.

A recent single-choice poll I submitted to the #general channel of numer.ai’s rocket chat (opened April 3, 2021 9:39 AM, n = 31, poll results taken April 5, 2021, 10:29 AM) :

“if payout factor were below ____ would you be more than 90% likely to withdraw majority of your stake? (pick highest amount)”

0.99 (withdrawing asap!)  
0.00% (0)  
0.95  
0.00% (0)  
0.9  
0.00% (0)  
0.8  
0.00% (0)  
0.75  
3.23% (1)  
0.5  
██████████ 54.84% (17)  
0.25  
██ 12.90% (4)  
0.1  
█████ 29.03% (9)

(note : I have removed usernames from the votes)

Although reality may differ from this opinion poll, it may give a sense of where people are at. I think in the longrun most modelers will have substantial stakes on the Classic tournament.

The mechanism of the attack I believe I identified is a throttle that modelers have some access to : payout_factor. Many modelers believe that a 0.5 payout factor would be motivation enough for them to withdraw a majority of their stake from the Classic tournament.

There are two main avenues for the attack,  
(A) self-staking  
(B) other-staking

(A) self-staking refers to modelers increasing their own stake. This is boring and I skip it in this post.

(B) other-staking is where some spiciness enters. A simple way to illustrate this would be to imagine if modeler X wants to push out other modelers (like the 17 from the poll above). I will explain the ‘why’ of it shortly. The mechanism to accomplish lowering the payout_factor could be : giving their predictions away for free. Could be from a current high-performance model of theirs, or a past one, or a new one entirely. At the price of free, it wouldn’t take much time to attract some (possibly large) amount of NMR speculators who want to stake their NMR without doing to the work of modeling. These people exist and frequently ask in Rocket chat, Reddit, and other locations how to to stake without doing the work. Many of them may be happy to be gifted a .csv (“better” than example_predictions) to stake their NMR on. So if a top modeler goes to twitter and says “hey, if you want the predictions from the model I’ve had in the top 100 for a while, , go to on Saturday nights for a .csv of the predictions” It would probably be best for modeler X if this model is one that tends to do poorly on MMC. Speculators will load up their coins, payout_factor will decrease, and then some large stake-weighted, skilled modelers will take their NMR elsewhere (Signals, sell on market, sit out and wait).

I think it’s a fair assumption that many of the modelers who leave on account of diminishing returns (who doesn’t love crypto-level returns?) will be withdrawing, on average, positive-MMC models. This itself should in turn cause modeler X (and other remaining modelers) MMC to go up, as well as some payout_factor effect offsetting in relation to the negative effect from the speculators participation, and if the speculators run predictions with negative MMC, that’s even more bonus to the remaining modelers.

This means that it may be possible for a single modeler to increase their return, while punishing other modelers, and perhaps most importantly to Numerai, degrading the quality of the signal they derive from the Classic tournament. Additionally, this would magnify competitiveness in a way that is not healthy for the community.

Other effects are possible in this scenario if modeler X decides to withdraw from their commitment to providing predictions, or changes the underlying model of the predictions being donated. A similar, but different enough case that might be worth considering is that some generous modeler may decide that they want to give (good) predictions away for free because they think everyone with access to cryptocurrency should have easy access to high returns via the Numerai tournament. In either case, if donated predictions become a substantial thing, it might make sense to somehow allow modelers to participate in the donations as a community.

I chatted with [@master_key](</u/master_key>) about this, I’ve left out his comments so he can say what he wants, if anything.

---

### Post #2 — **hb_scout** | 2021-04-05 23:54 UTC

I think if Numerai ended up getting too many submissions that were too similar (for whatever reason, not just because someone is trying to push out others), they would just turn off the Corr payment and only pay on MMC. Then modeler X gets additionally punished by having large stakes on the models they’re presumably also staking on. Furthermore, I’m not sure anyone would choose to purposefully drive the payout factor to 0.5 in an attempt to get participants to leave, even if they could by waving a magic wand. I think that would sacrifice a huge amount of earnings without any guarantee that the payout factor would go back up. And the actual process of purposefully decreasing the payout factor would require a huge amount of new stakers willing to gamble on your predictions who are also facing the same decreased payout. Certainly what you describe is possible, but I would categorize it as very unlikely and it could be solved by changes to the payouts that they haven’t hesitated to implement in the past like adjusting the balance between Corr/MMC payouts.

---

### Post #3 — **liz** | 2021-04-06 00:05 UTC _(reply to #2)_

I’ll respond to other points tomorrow if I get time, but I want to point out this concept applies more and more the closer we get to whatever imaginary quit-threshold modelers hold, in relation to the potential benefit to MMC. It is much easier to instigate 0.65 → 0.5 than 0.99 → 0.5.

---

### Post #4 — **sdmlm** | 2021-04-06 07:41 UTC

I think by the time we reach 0.5, the team would implement various changes if they weren’t happy with what’s going on. While your described scenario is plausible, by the time modeler X starts gathering followers, either the team or the community would detect what’s going on and take action. For instance, a few weeks ago I noticed a lot of identical predictions in a round and quickly posted about it on rocket chat. In just a few minutes the community and team all started looking into it. In the end it was just a large number of new users all submitting the ols example script. So if something like what you’re describing were to happen, I think it would get detected and addressed very quickly.

---

### Post #5 — **sdmlm** | 2021-04-06 07:43 UTC

Additionally, I think the team monitors regularly the sharpe/corr of the meta-model in relation to various events, so if one of those suddenly drops they would start investigating. E.g. I think the team said at some point that the diagnostics appearing on the website most likely increased the meta model’s sharpe significantly, by helping modelers see what they should optimize for.

---

### Post #6 — **liz** | 2021-04-06 12:15 UTC

yeah, indeed I think the team would take action if this happened. I thought laying this idea out would be useful, sorry to waste anyone’s time reading it.
