---
title: "Ideas for replacement of leaderboard bonus"
category: Tournament
url: https://forum.numer.ai/t/ideas-for-replacement-of-leaderboard-bonus/391
created_at: 2020-05-12T05:17:40.829000+00:00
last_posted_at: 2020-07-01T00:38:50.344000+00:00
posts_count: 6
views: 1661
tags: []
---

# Ideas for replacement of leaderboard bonus

---

### Post #1 — **rappenlager** | 2020-05-12 05:17 UTC

The leaderboard bonus is going to be canceled.  
I would like to suggest ideas for a replacement.

The leaderboard bonus has mainly promoted long time good performers. But anyway every competitor wants to perform well in the long run, so it is only another way of (extra) payout for good performers. The individual success is rewarded with the normal payout anyway. To be motivated for good results I do not miss the leaderboard bonus.

I think, a bonus should be a motivation to do something different, something better: Better for Numerai, better for the community (the focus might be a matter of discussion).

**First Idea: “community bonus”**

If someone reports bugs or gives valuable feedback, numerai rewards this directly to the bug/feedback-reporter, see [bounties](<https://docs.numer.ai/tournament/bounties>). That is great.

Numerai supports activities like Office Hours with Arbitrage, this forum, channels at rocket chat by supplying infrastructure and some Numerai team members are active there. That is great too. One of the goals, I guess, is that the whole community keeps getting better. Numerai will profit from that.

A community bonus could be defined to reinforce this.

Such a bonus could be an incentive to continually improve and also help the other competitors do so - even though we are, of course, competing and nobody wants to tell his/her secrets. But I think, we could help each other to get more stable results, avoid technical issues, improve our models and use the right methods to do ML well.

Such a community bonus could be calculated in a way like this:

community bonus = any_factor * individual stake * global regular payment

If the global regular payment is negative, it should be set to zero, because it should be a bonus and not a penalty.

**Second Idea: “stability bonus”**

I think, numerai is interested in stable results. So participants could get a reward, if their models show a more stable performance.

A formula for this could be:

stability bonus = any_factor * ( 1 - individual standard deviation of correlation of last 10/20 or more predictions) * individual regular payment

In case the result is negative, it should be set to zero.

**Third Idea: “mmc bonus”**  
Instead of introducing mmc or mmc2 as optional payment (as planned for now, see: [mmc](<http://forum.numer.ai/t/mmc-payout-details-and-analysis/220>) ,  
[mmc2-announcement](<http://forum.numer.ai/t/mmc2-announcement/93>) ), an additional mmc bonus could be paid

The above suggested bonuses could be financed with the savings on the canceled leaderboard bonus or by appropriately cutting the individual payments.

What do you guys think about this?

---

### Post #2 — **quantnosticator** | 2020-05-12 13:04 UTC

I would say that any bonuses explicitly tied to model performance (stability, mmc, etc) could be tied to your stake (but not necessarily, we could have fixed “prizes” for things also), but a community bonus (or bug bounties) should not be tied to your stake value (although maybe just being staked period could be a qualifier). Any community benefit derived from [whatever is being rewarded] is going to be the same whether it came from a whale or a lowly peasant like me. Not absolutely everything has to have “the rich get richer” dynamic, and also that incentivizes the team NOT to reward good things that do come from whales because they would cost a lot more. (A regularized bureaucratized community bonus is also the least likely idea to be adopted because it is so subjective.)

---

### Post #3 — **timthabt** | 2020-05-18 22:27 UTC

I think the replacement should be based on multiple metrics. For example, a hybrid metric based on stability, MMC, CORR W/ METAMODEL, and perhaps uniqueness. Another matric might be worth testing is OHLC of the correlation throughout a tournament round. Community, reports, and feedbacks could have their own bonus but different from the replacement which can be called “Numerai Bonus.” I am still a noob in here but that’s what I think.

---

### Post #4 — **quantverse** | 2020-06-28 12:35 UTC

Let me present an alternative to current bonus system. The goal is to keep the current reputation, but instead of bonuses, user should be able to place auxiliary stakes on their relative performance. Discussion and feedback is very welcome. The proposed system should be resistant to p|1-p attacks and also to manipulating the rank by placing same model multiple times with small stakes for each.

My proposal: <https://docs.google.com/document/d/1FLpY-PymRsFs_DSX5BOjPU6r_KNL_rBQ_k8WOZuO61E/edit?usp=sharing>  
The spreadsheet of the example: <https://docs.google.com/spreadsheets/d/1xLRVaQQVkEGhb63up23dBF9g0d02TYAhMlmiTrOPJyk/edit?usp=sharing>

Let’s treat the linked material as a draft of something which may be turned into a real system. I think it would be great to agree upon on some version of payment system similar to this one before the Fire Side chat, so it can be discussed Tuesday with the team. I think many of us will miss the bonuses and I think we need some meaningful system of rewards for user with decent long term performance.

---

### Post #5 — **rappenlager** | 2020-06-30 06:19 UTC

Unfortunately i can’t participate today at fireside chat, but i would be happy if the ideas presented here would come up.  
In my opinion an easy to understand bonus system should be found.  
It should be a bonus system where both sides, Numerai competitors and host, benefit in the medium or long term.

---

### Post #6 — **joakim_arvidsson** | 2020-07-01 00:38 UTC

How about an annual performance based bonus, based on the past 2 years worth of MMC (or MMC Sharpe)? Paid as a percentage of individually capped stake size. Would align incentives, encourage long-term buy-in, and be difficult to game, no?
