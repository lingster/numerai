---
title: "Numerai Fireside Chat Aftermath"
category: Feedback
url: https://forum.numer.ai/t/numerai-fireside-chat-aftermath/6726
created_at: 2023-10-13T11:35:38.372000+00:00
last_posted_at: 2023-11-04T21:50:26.770000+00:00
posts_count: 62
views: 2058
tags: []
---

# Numerai Fireside Chat Aftermath

---

### Post #1 — **taori** | 2023-10-13 11:35 UTC

After the [last fireside chat](<http://forum.numer.ai/t/numerai-fireside-chats>) there have been lots of comments on Discord and some of them were very interesting. Since I like to hear the voice of the community (and Numerai team for that matter) I am opening this thread so that people can share their thoughts here.

Compare to discord, I believe that a forum post encourage a more thought-out exposition of ideas and also it is nice to collect all related thoughts on a single place.

Note: I believe all of us like Numerai, even though for different reasons, so please do not abuse this post for rants, but just for constructive ideas.

---

### Post #2 — **taori** | 2023-10-13 11:56 UTC

These are my thoughts.

I don’t mind sudden changes in the payout scheme, so the last announcement on this regard didn’t bother me at all. I actually love the new emphasis on CORR. What bothers me is the drastic decrease in payout: 1xCORR + 3xTC doesn’t equal 2xCORR + 1xTC. However they say it is a temporary solution, so I might be ok with that if “temporary” means some weeks.

What really worries me is the bad performance of the fund and Numerai uses of some model performance as scapegoat. It seems as if Numerai hasn’t figured out yet a way to transform the fund’s needs into a proper payout scheme and this makes the hedge fund suffers. There should be no need to explain what a model should do or not do, but everything should be the consequence of a smart payout scheme that encourages and rewards the models which are useful to the fund.

---

### Post #3 — **taori** | 2023-10-13 19:33 UTC

I would like to better explain what I meant in my previous post.

The hedge fund has recently suffered serious losses, then my question is: **was there a combination of model submissions that performed well in the same period that the hedge fund performed bad?**

**A)** If that is not the case, then we have a problem: **the community or the data sources are not good enough to provide what the hedge fund needs.**

**B)** If there was indeed a combination of model submissions that performed better than the hedge fund, then the question becomes: **Why Numerai’s team hasn’t figure out yet how to properly select the predictions they need?** If the problem is so hard they could transform it in a new tournament.

---

### Post #4 — **liborty** | 2023-10-15 22:15 UTC

I have stated before my doubts about the emphasis on some artificial ‘true contribution’, no matter how clever might be the constructs used to justify it. Anything that is not based on the actual predictions (correlation performance) is going to be sub-optimal.

While it is true that any model tends to learn more from the outliers, it is rarely in the right direction.

---

### Post #5 — **dd_dd** | 2023-10-16 12:38 UTC _(reply to #4)_

Corr is a simplification. Optimizing corr doesn’t necessarily mean optimizing fund performance.

---

### Post #6 — **dd_dd** | 2023-10-16 12:45 UTC

I see a problem with the incentive system allowing compensation for inferior model performance with more stake.  
Stake is just a signal. There’s no point to allow 10 times more weight than average if there’s no reason to believe that your model is 10 times better than average.

Don’t know how to fix this except by enforcing stake limits based on historical performance.

---

### Post #7 — **wigglemuse** | 2023-10-16 15:58 UTC _(reply to #6)_

The theory is that more stake = more risk = more confidence = it must be better?

It sounds stupid when you put it like that, but it isn’t a totally bankrupt theory. Assuming historical performance of a model (or of the modeller) can’t be known (by the fund at least) – which was always the dream, to be able to use signals that any person came and added to the mix – what else can be done? Everything else involves some sort of gatekeeping system of proving yourself, etc – i.e. you move towards normal hedge fund operation, not really crowd-sourcing (basically you’re hiring people then, but with a more open audition system).

Something that can be done within current system is enforcing limits to weight in the metamodel, but NOT based on performance, just enforced period – nobody should have too much weight no matter what. (More accurately, redundant signals shouldn’t have too much aggregate weight as you can get around limits on people or model slots.) Surprisingly, they have always blown off questions about this when it seems so obviously a potential problem.

But still, I keep pointing this out. YOU ARE GOING TO HAVE DRAWDOWNS NO MATTER WHAT. Not every drawdown is an emergency situation calling for a sudden rug pull like we’ve just had. (Even if the change is ultimately good, implementing it as a rug pull where all your work is trashed without compensation is not. You destroy good will, etc etc) What I see going on now is panic taking over – “getting caught in the switches”. I would bet money that recently at Numerai they’ve been asking “well…what thing that if we had been doing that instead of what we were doing…would have gotten us through this last drawdown period doing good/ok instead of bad?” It sounds reasonable on the face of it – let’s just tweak things so that we would have done good in this recent past period if we had done this tweak sooner…but it is the road to ruin, ask any gambler.

---

### Post #8 — **dd_dd** | 2023-10-16 16:28 UTC

(note: this is account leaderboard data, last week’s data, so numbers may differ a bit if you want to check now)  
I take stake x TC as a measure of total influence on fund performance.  


[![Figure_10_200000](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b8cf9a0e321d6d1b68589cc79ac8bc5102a8d1ba_2_690x460.jpeg)Figure_10_200000900×600 78.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b8cf9a0e321d6d1b68589cc79ac8bc5102a8d1ba.jpeg> "Figure_10_200000")

  
If stake weighting worked, one would expect to see some positive correlation between stake and influence.  
Zoom in to lower stakes:  


[![Figure_10_8000](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4dd74aa52515d05bcda1af4fbb6c9876933bbe90_2_690x460.jpeg)Figure_10_8000900×600 93.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4dd74aa52515d05bcda1af4fbb6c9876933bbe90.jpeg> "Figure_10_8000")

  
The density plots look similar to the above for accounts staked up to 8k.  
Above 8k, the plots diverge you get results depending on which of the few big accounts get included.  


[![Figure_10_20000](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/315872a81e7d9d01913eb2b263579c7621ca9742_2_690x460.jpeg)Figure_10_20000900×600 83.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/315872a81e7d9d01913eb2b263579c7621ca9742.jpeg> "Figure_10_20000")

To me, sparsity of the point cloud looks like the real issue here.  
When expanding into sparse territory the metamodel might actually pick up more noise than signal.  
Another reason to limit stakes and have participants not move too far away from the crowd.

Also note that the range of (Stake x TC) is nearly constant between 2k and 8k and how it explodes after that. That means increased dependence on fewer models. Not really desirable.

---

### Post #9 — **wigglemuse** | 2023-10-16 16:35 UTC _(reply to #8)_

So this is stake-weighted TC numbers and (current) stake as shown on leaderboard? Not sure that really will capture what has gone on round-to-round over time. Interesting nonetheless.

---

### Post #10 — **dd_dd** | 2023-10-16 16:38 UTC _(reply to #9)_

It’s account (DS) leaderboard data, as per edited text.  
It’s about the big picture. Not round to round.

---

### Post #11 — **thornam** | 2023-10-16 16:57 UTC _(reply to #6)_

Agree, the stake signal becomes less useful when there are big differences in the amount staked by accounts. Just as is seen in the Signals tournament.

How about a within-account stake weighted MetaModel. This would give a more precise signal of the beliefs of the individual model. If an account distributes its overall staked amount 90/10 on two models, it clearly indicates his beliefs between those two models.

At the same time, the account weighting could be based on the ranking from the account-leaderboad. This would give higher weights to accounts that have proved their worth.

E.g., with some arbitrary numbers:  
An account is ranked in the top 20 of the Account-Leaderboard and thereby has an overall weighting of 0.02 on his account. And he has two models (Model A and Model B), which he has distributed his total stakes to 90/10 on A and B. Then the MM weights from each model would be:  
Model A = 0.02 * 0.9 = 0.18  
Model B = 0.02 * 0.1 = 0.002

This system might be more robust to large stakers and emphasize accounts that have already proven their worth.

---

### Post #12 — **wigglemuse** | 2023-10-16 17:17 UTC _(reply to #11)_

With datasets (and even metrics) changing all the time, what good is proving your worth? I mean, _what_ have you proven? (Putting aside the whole fooled by randomness issue with any such scheme based on track record, which is a huge issue.) Is it assumed if you are good at one thing you are good at everything that comes along?

They used to actually not accept predictions that didn’t have a threshold minimum correlation with the examples – they just said “those tend to not be good models”.

---

### Post #13 — **thornam** | 2023-10-16 17:37 UTC _(reply to #12)_

Well, changes to metrics would also alter the leaderboard and thereby automatically change the account weighting to those metrics that the fund believes are most useful.

And the account leaderboard, in my opinion, gives a good indication of how well individual people have performed during the past year, which definitely has been in a changing environment. So they might also be good at handling new changes to eg. the dataset. And if they are not, they will decrease in account weight by falling in the account ranking, just as the case is now by burning their model stakes.  
So this would also be a system that ‘optimize’ itself, just as the one we have now with the stake weighting.

However, these are all just thoughts

---

### Post #14 — **wigglemuse** | 2023-10-16 17:43 UTC _(reply to #13)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/t/eb9ed0/48.png) thornam:

> Well, changes to metrics would also alter the leaderboard and thereby automatically change the account weighting to those metrics that the fund believes are most useful.

Yeah, but you wouldn’t have been optimizing for those – they might not even have existed before (probably didn’t). So then we get rug pulled because we didn’t do well on a metric in the past that didn’t even exist in that past. This has got to work for the participants somehow as well…

---

### Post #15 — **thornam** | 2023-10-16 17:53 UTC _(reply to #14)_

Think we are talking about two different things. I’m talking about the MM weights and how to maybe optimize the MetaModel.

I don’t see how changing the MM weight system will rug-pull anyone since they don’t affect payouts (or at least to a minimal amount). The only thing that might be affected is the MM performance, and the fund should obviously only do this if it could improve MM performance

---

### Post #16 — **wigglemuse** | 2023-10-16 18:03 UTC _(reply to #15)_

Well, they are talking about restricting staking, i.e. keeping the link between staking and MM control, but controlling who gets to stake and how much. So you do bad, and you don’t get to stake seems to be the likely result of any gatekeeping scheme. In any case, I think they will always want to keep the link between MM control and potential rewards – if they’ve downgraded you in the MM weights due to some rule change, you can bet your payoffs are going with it. Which is fine, but not overnight.

---

### Post #17 — **wigglemuse** | 2023-10-16 18:11 UTC

Here’s the larger thought about all of this that’s happening. Numerai has a plan. Anybody finds it easy to follow a plan when things are going good. If the first thing you do when something goes badly is change the plan…THEN YOU NEVER HAD A PLAN. The whole point of a plan is so you know what to do when things go wrong – you stick to the plan. That’s the most important reason for having a plan. If you make changes, you do them holistically and because you realize the plan is flawed – something going badly in a probabilistic game like this isn’t in and of itself evidence of a flawed plan. Again, it is the entire reason for the plan because things are ABSOLUTELY GUARANTEED to go badly sometimes – the plan is what gets you through.

And if you find that you have a flawed plan and there are necessary changes to be made…well first of all you don’t blame the people who were just following the plan you set-up. You apologize, you say we’ve made a mistake, we recognize that this plan will never work (or this part of it, whatever), and its got to change. But its all our fault, we’ll try to make good any damage we’re doing, and we’ll start from there and think it over very carefully. That’s not what I see happening.

---

### Post #18 — **nyuton** | 2023-10-16 18:18 UTC _(reply to #7)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> The theory is that more stake = more risk = more confidence = it must be better?

This is true for most individuals, but not for big investors/institutions.  
Big investors stake big, because they have a lot of money to allocate.  
Their stake is not proportionate to the quality of their model.

It can’t be! There are some very smart inidiviuals here, submitting great models.  
Bigger investors/instituitions can’t be 10x better, but they can have 100x more money to allocate.

---

### Post #19 — **nyuton** | 2023-10-16 18:18 UTC

Also worth noting the potential effect of un-staking some big accounts for bad performance.  
If they sell their stake, NMR could collapse and then it takes the whole ecosystem with them!

Unstaking big accounts or many small bad bad performing accounts means the end of the game.  
NMR is weak anyway. All cryptos are. Such an event would be the final one.

---

### Post #20 — **wigglemuse** | 2023-10-16 18:29 UTC _(reply to #18)_

Yes, I agree. The biggest stakers often just want a return…maybe any return because they are really just NMR hodlrs or whatever. But even if they are top-class models, as you say they still can’t be exponentially better than everybody else, so I think some sort of anti-top-heaviness clamp on staking (or something equivalent) would be appropriate. The stakes tend to conform to a power law distribution but the quality of the models don’t. Its the distribution of the stakes/mm control that needs to be adjusted to be more like the other.

---

### Post #21 — **f58c** | 2023-10-16 23:05 UTC _(reply to #20)_

catching up on the thread- i’ve noticed that some models perform well as measured by the metrics (CORR20v2, TC) but aren’t staked. are unstaked models ignored? i like that each person takes on risk when staking their models, but i also recognize that not everyone can stake NMR- i.e. staked NMR is confounded by a person’s economic circumstance. staked NMR isn’t a pure measure of confidence due to this confounding effect.

---

### Post #22 — **dd_dd** | 2023-10-17 13:26 UTC

The stake weighting is linear, grouping models into accounts first and combining that into the metamodel shouldn’t matter, if I understand what you’re saying [@thornam](</u/thornam>) .  
Anything differing from linear weighting (including rank, hard stake limits, log stake weighting etc) is Sybil attackable. I guess that’s why numerai didn’t want to do it.  
That’s another reason why I suggested track record based limits:  
Making sybil accounts with a good track record requires time and makes attackers easier to spot.

Just to illustrate how broken the current system is: the “sparse” zone consists of 15 accounts and controls 50% of the metamodel.  
7 negative TC ~240kNMR and 8 positive TC ~170k  
The low stake portion isn’t great either but at least you can spot some order, which is of course destroyed as soon as a whale gets in a bad mood.  
Doesn’t sound like crowdsourcing to me.

---

### Post #23 — **thornam** | 2023-10-17 14:05 UTC _(reply to #22)_

Actually, I think we suggest sort of the same thing, as I do also suggest a track record based system.

And when you say ‘track record based limits’ you mean limits to the staked amount on a given model, right? However, this I might not be a fan of since it can discourage participants whenever falling short of those limits and restricting their payoff/stake. As was the case Richard brought up at the Fireside about how Millenium had created some angry former managers by stopping the collaboration when they fell short of the limit.

Personally, I would prefer a smoother system that automatically incorporates the track record, which is why I suggested a MetaModel that was weighted based on one’s account track record. (Notice this would not affect the possible stake on a given model).

Moreover, the great thing about the current MetaModel weighting system (in theory) is that it incorporates participants’ beliefs about how good a given model is by putting more weight on models with high stakes. However, I think we can all agree that high stakes is not equal to a good model in practice, as multiple people have argued in this thread (and that I agree with).

But we still want to incorporate people’s beliefs about how good a model is into any new weighting system because it holds much information. So that is why I suggested a combination of the track record based and the stake weighted system.

Hope this makes sense, and please correct me if I’m wrong

---

### Post #24 — **dd_dd** | 2023-10-17 17:45 UTC _(reply to #23)_

I meant account based limits.  
If you want to modify the system away from the current linear stake weighting, you need to do it account-based, and you need to ensure that people don’t register multiple accounts (sybils).

IMO, the pressure from foul players will be lower if there is a time component included in the limits such as a multi-month track record.

---

### Post #25 — **thornam** | 2023-10-17 19:42 UTC _(reply to #24)_

Yes exactly, it would need to be account-based.

But you do not need to worry about multiple accounts if the MM weights are track record based. New accounts would have zero (or very low weights to the MM) and only gradually contribute to the MM as the account show good performance. However, they would still be able to stake as much as they want, but only gradually contribute to the MM if the account performs well

---

### Post #26 — **f58c** | 2023-10-17 22:24 UTC _(reply to #25)_

i’d propose separating meta model contribution calculation from NMR staking. NMR staking is great for making sure valid/performant models are submitted. whether or not a model is incorporated into the meta model could be solely based upon corr20v2 and tc (or any performance metric(s) developed in the future). this does deviate from the white paper conception of the auction, so maybe i’m missing something? <https://numer.ai/whitepaper.pdf>

---

### Post #27 — **thornam** | 2023-10-18 06:41 UTC

One more post, and then I’ll let the thread be for other good ideas.

To be more tangible, what I initially suggested was a two-factor system where the individual model contribution to the MM was based on an **Account Weight** and a **Stake Weight**.

E.g.  
Imagine an account with a 90 percentile ranking on the account leaderboard and 3 models (Model A, B, and C). The account chooses to stake 80% of their stakes on Model A and 10% on each of Model B and C. Then the contribution to the MM from each of the models would be created something like this:  


[![MM weight system 2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/703a8c25e463de370664aba7e2fd52b9bbfe1e8c_2_690x313.png)MM weight system 21197×544 58.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/703a8c25e463de370664aba7e2fd52b9bbfe1e8c.png> "MM weight system 2")

  
_Notice that the Account weight numbers in this example are just arbitrary numbers and should be set by the fund. And that there are no stake limits._

The benefits of the **Account weight** are that it separates the MM contribution from the staking system (as [@f58c](</u/f58c>) proposes) and creates a track record based system (as [@dd_dd](</u/dd_dd>) proposes) by limiting contribution from “bad” accounts to the MM and putting more emphasis on contributions from “good” accounts. At the same time, it does not hold the multiple-account problem, since new accounts would have zero, or at least diminishing, contribution to the MM.

The benefit of the **Stake weight** is that it incorporates the Data Scientist’s information about his/her model. This is based on the assumption that the Data Scientist holds more information about how good or risky their model is, which is the same assumption the current stake-weighted system is based on. Thereby, a higher stake equals a better model, but without the proportionality problem between high stakes and model quality caused by differences in people’s economic situations (As [@nyuton](</u/nyuton>) and [@dd_dd](</u/dd_dd>) argue).

Moreover, the system doesn’t limit people’s ability to stake but only limits people’s contribution to the MM. And in my opinion, it is not necessarily the fund’s job to prevent people from staking on bad models, but it is their job to prevent bad models from contributing to the MM.

This could create a system that holds multiple of the good ideas I’ve seen in this thread (separating the MM contribution from the current stake weighting, creating a track record based system) while tackling the proportionality problem, and at the same time having a flexible system that doesn’t limit peoples ability to stake on a given model, but instead limits the contribution from a given model to the MM.

---

### Post #28 — **nyuton** | 2023-10-18 12:25 UTC

Stake limit MUST be avoided, because that results in the liquidations of large NMR holdings, thus causing the collapse of the whole ecosystem!!!

I suggest a “personal payout factor”, where the ranking (past performance) of the account is incorporated into the payout factor as a multiplier.

New or bad performing account would get a lower PPF, thus they can lower influence on the MM and lower payouts.  
Good performing accounts would get a hiher PPF, thus enabling hiher MM impact and higher payouts.

Note that, this approach doesn’t directly force participants to liquidate NMR holdings. It just limits the account’s impact and payouts.

---

### Post #29 — **wigglemuse** | 2023-10-18 15:40 UTC _(reply to #28)_

Payout factor black market created?

---

### Post #30 — **dd_dd** | 2023-10-18 23:11 UTC

1. The stake limit is tied to model’s TC history. (EDIT: maybe stake weighted TC should go here instead, need to think more on this)
  2. An auction system enables whales to compete for free stake space of each model. Bigger whales can pay more and will get the best model.
  3. If overstaked, the TC mechanics will gradually reduce TC/stake limit, so that the next best model becomes more attractive



That way stakes should move to better models and enable more earnings for model owners, compensating for the PF reduction caused by whales.

If the TC reduction works as advertised, then it should also automatically take care of the sybil problem, as TC would detect similar models belonging to different accounts and reduce their TC/stake space accordingly.

---

### Post #31 — **quantverse** | 2023-10-19 07:43 UTC

Why do you guys think “track record before staking” should help in the first place?

This is the ATOL performance just before the drawdown:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/61a8cdda20370b509e4307d2f1491148012542fb_2_423x499.png)image769×908 37.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/61a8cdda20370b509e4307d2f1491148012542fb.png> "image")

If you waited those 6 months before letting them stake, you would actually end up in a much worse position, because you would miss those 6 months of profit…

---

### Post #32 — **nyuton** | 2023-10-19 08:01 UTC

The only reasonably good metric that let’s you judge, how good someone is: the all time returns.

Ultimately that’s what we all are optimizing for.  
Even a random model can have decent TC for 6 months…

All time returns include good modeling for many eras, drawdowns included.  
All time returns include years of experience, with many models.  
All time returns include good risk management. Let’s face it 3xTC is rarely a good idea.  
All time returns include good allocation of stake. Anyone can have a model in the top100. But putting most stake to the best future(!) performance is a skill.

1year TC doesn’t mean much.  
I have two in the top100. Based on that one could say I’m one of the best.  
But as a matter of fact, I haven’t earned anything with them ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=12)  
Look at all time returns to get a good judgement of real performance.  
Good stake allocation is just as important as good modelling.

It’s somewhat unfortunate that there is no way to get a good judgement of someone faster.  
Any monkey can have good one year performance.  
Warren Buffet is admired for his 60+ year track record.  
Noone knew his name after the first few years and not because those were bad.

---

### Post #33 — **quantverse** | 2023-10-19 08:12 UTC _(reply to #32)_

Well, apart from models bought at Numerbay most of ATOL models are actually mine. They had a good track history before handing them to ATOL:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/2667f999d4a4c65db704bf27cc9166bf05bec79e_2_455x500.png)image824×904 46.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2667f999d4a4c65db704bf27cc9166bf05bec79e.png> "image")

My account has been there since 2017 and has a return of 651%, so I would definitely have the track record anyway.

You can’t have model performance with longer history, because there is a new major dataset release each year and it is pointless or even impossible to use older datasets for anything.

So what you propose is completely unrealistic.

Also, one of the reasons for our drawdown is that we kept staking on old (but proven!) nomi-trained models and nobody told us that it was a bad idea. These models failed the most. So this example actually proves that nothing based just on past performance can actually work.

A few points to take out of this:

  * Past performance is not an indicator of future performance
  * Not everything is the fault of big guys
  * Drawdowns happen and avoiding them just causes other drawdowns

---

### Post #34 — **dd_dd** | 2023-10-19 08:27 UTC

[@quantverse](</u/quantverse>) Compare your 1y plot to the top 100 accounts.

With the auction system I suggested, you would be allowed to place a slightly above average stake, maybe ~1k, but if you really want to stake more, you can bid for something from the top of the LB.

My point is not to blame a specific account, but to show that letting 15 individuals have control over 50% of the metamodel counters every principle that numerai is built on.

I’m trying to figure out sustainable ways to force whales to join the crowd or at least to get some order into the stake distribution.

---

### Post #35 — **quantverse** | 2023-10-19 08:27 UTC _(reply to #20)_

I don’t think that it was ever meant that a model with a stake 1000 times higher than an average stake is supposed to be 1000x better. It was about the more confident you are about the model it will be good, the more you stake and therefore the more you risk. Then you should be more careful what you stake on and if your models burn, you are more incentivized to do something about it. And if you don’t, the burning stake self-corrects the meta-model by decreasing the weight.

The two biggest stakers here are funds, so they stake their client’s capital and they have the responsibility to the clients. So if they are not bringing a return to their clients for some time, they will be forced to stop staking eventually. So I would think the incentive alignment still works.

And no, this feedback loop aside is not enough to prevent drawdowns. Nothing is.

---

### Post #36 — **quantverse** | 2023-10-19 08:34 UTC _(reply to #34)_

It won’t work, because the ranking in the leaderboard is

  1. often pure luck
  2. based on historical performance



The best model with rank #1 can be the worst in one year. Believe me, I had many models in top 50 for long time.

This account uses my models too: [Numerai](<https://numer.ai/~matmish1>) and it is #23 in TC. Just the stake distribution and timing made it appear better and have a better rank.

---

### Post #37 — **dd_dd** | 2023-10-19 08:43 UTC _(reply to #36)_

But I guess you didn’t put all of your stake on these lucky models.  
I corrected “TC history” to “stake weighted TC” in the auction proposal.  
If that doesn’t work for some reason I’m currently not aware of, account performance history should work.

Claiming that history means nothing is equivalent to the claim that eventually everybody’s performance is the same. A pretty destructive argument and it’s actually not true.

---

### Post #38 — **quantverse** | 2023-10-19 08:44 UTC _(reply to #34)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/d/57b2e6/48.png) dd_dd:

> you can bid for something from the top of the LB.

Actually, we did that - we bought the top LB models and staked on them. This caused a major loss. This is a big mistake and a good example of how selecting models based on LB rank is doomed to fail.

---

### Post #39 — **quantverse** | 2023-10-19 08:46 UTC _(reply to #37)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/d/57b2e6/48.png) dd_dd:

> But I guess you didn’t put all of your stake on these lucky models.  
>  I corrected “TC history” to “stake weighted TC” in the auction proposal.  
>  If that doesn’t work for some reason I’m currently not aware of, account performance history should work.

But my example of my track record _is_ stake weighted, so it would be relevant if track records were considered.

---

### Post #40 — **dd_dd** | 2023-10-19 08:48 UTC _(reply to #38)_

But some others made a fortune doing the same. That’s another evidence how extreme staking and letting a few individuals control the MM only introduces noise and volatility.

---

### Post #41 — **quantverse** | 2023-10-19 08:57 UTC _(reply to #37)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/d/57b2e6/48.png) dd_dd:

> Claiming that history means nothing is equivalent to the claim that eventually everybody’s performance is the same. A pretty destructive argument and it’s actually not true.

No, it is not. I clearly said that I mean: past performance does not indicate future performance. Totally different statement.

Example: you see a model with really good historical performance. You buy it on numerbay and stake on it. The model will now burn 50% of your stake, because:

  1. The author of the model decided to submit something else since you staked (or has a bug in his pipeline)
  2. The numerai fund raised AUM significantly and now is not able to trade small caps; but the model you have bought is trained on an old target, not optimized for large caps
  3. …



The point is - you base your stake on something, that already happened in history, but your profits are purely based on what happens in the future and you are missing the extra context needed. And the historical performance was based on factors which just did not persist but you don’t know that. That’s why just using the historical performance is never enough.

---

### Post #42 — **quantverse** | 2023-10-19 09:00 UTC _(reply to #40)_

But that actually proves my point ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) My argument was that selecting models using just LB rank does not work and it is a stroke of pure luck.

If that ever worked, Numerai would not need to introduce the staking in the first place. It was like this till June 2017 and it apparently did not work.

---

### Post #43 — **quantverse** | 2023-10-19 09:05 UTC _(reply to #40)_

1. It is not really my problem how Numerai selects their MM weights. If they are unhappy with linear system, they can use whatever works best for them.

  2. You don’t know, maybe without the big stakers the fund performance could be much worse. Everyone talking about big stakers but nobody here proved that average stakers delivered something much better. Considering how bad LightGBM models did in the drawdown I would not expect anything great.

---

### Post #44 — **taori** | 2023-10-19 09:37 UTC

Better than considering the past performance of a model, I would say users should submit the prediction of the current round plus some other eras (synthetic eras or historical eras with a different obfuscation settings so that past eras cannot be recognized). This additional eras serve to gain confidence on the model over different period of times. Let’s say this additional eras are 10 per round, then over a period of 4 weeks (a full round) Numerai can collect the model performance over 220 eras (20 rounds + 10 test eras * 20 rounds). This would certainly improve the confidence on models.

---

### Post #45 — **quantverse** | 2023-10-19 09:41 UTC _(reply to #44)_

It used to work like this before March 2022 in the pre-v4 dataset era. But they moved away from this setup for multiple reasons.

But using historical eras would not solve the drawdown we had. These models worked great in historical eras, just not in the following ones.

Using synthetic eras could work, I agree. But not sure how difficult is to craft them in an useful way.

---

### Post #46 — **taori** | 2023-10-19 09:42 UTC _(reply to #45)_

> It used to work like this before March 2022 in the pre-v4 dataset era. But they moved away from this setup for multiple reasons.

Do you think they changed the extra eras every round or they used the same?

Also they didn’t compute the score on the additional eras, that’s a problem

---

### Post #47 — **quantverse** | 2023-10-19 09:44 UTC _(reply to #46)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/t/ebca7d/48.png) taori:

> Do you think they changed the extra eras every round or they used the same?
> 
> Also they didn’t compute the score on the additional eras, that’s a problem

  1. it was a fixed hold out few years long
  2. nope (it would allow a ladder climbing attack)

---

### Post #48 — **taori** | 2023-10-19 12:41 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/quantverse/48/2022_2.png) quantverse:

> nope (it would allow a ladder climbing attack)

That would be the case only for a fixed hold out era set, correct? So my original idea would still work and I still believe it would make any type of score more meaningful and less noisy. The only problem i see in my approach is the increase in computation: if Numerai asks for X more era submissions, then the computation requirements increase X times and given the limited amount of time we have for the daily tournament that might be a problem.

On a different note, I believe the stake weighted portfolio concept has to go away (as many of you already said). It was an interesting idea but it bundles two concepts that have nothing to do with each other: the optimal model weight (optimal from the hedge fund point of view) and the user investment capacity. To be honest, the whole Numeraire thing has to go away. It’s an additional layer that users don’t need/want. I hope Numerai can find the way to make the best use of the model predictions so that the hedge fund goes well and we can get paid in FIAT eventually.

---

### Post #49 — **wigglemuse** | 2023-10-19 14:20 UTC _(reply to #35)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/quantverse/48/2022_2.png) quantverse:

> ver meant that a model with a stake 1000 times higher than an average stake is supposed to be 1000x better. It was about the more confident you are about the model it will be good, the more you stake and therefore the more you risk. Then you should be more careful what you stake on and if your models burn, you are more incenti

I’m worried more about total signal weight/mm control than staking (or avoiding drawdowns) per se, i.e. I’m in the camp that thinks a tiny number of signals shouldn’t be essentially controlling the fund. Why have all these thousands of models when only 10 of them really count?

---

### Post #50 — **quantverse** | 2023-10-19 15:07 UTC _(reply to #48)_

I think it could perhaps work with synthetic eras, but hardly with historical eras. Where would you get so many historical eras that they never wear out considering the whole history is now public?

About NMR - the fund needs it and I want it ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) What are users going to stake … fiat? Also, the whole point of NMR is that payouts don’t cost them anything. If they had to pay with fiat, the earnings would be negligible…

---

### Post #51 — **quantverse** | 2023-10-19 15:12 UTC _(reply to #49)_

Fair enough, but nobody forces Numerai to calculate the weights in the way they do now (weight == stake). They can use something else (like `log(stake)`) if this does not work for them. It is an internal thing.

Also, the concentration of MM weights can be caused by Numerbay as well (too many participants staking on the same model)…

---

### Post #52 — **wigglemuse** | 2023-10-19 15:30 UTC _(reply to #51)_

Yes, exactly. SOMETHING should be done about too much top-heaviness – it doesn’t have to be staking restrictions. Although I’d listen to such arguments as one part of a solution – should there really be zero top limit if the average stake is X whatever [ factors of magnitude less ]. Earlier in the tournament we had a single guy (who worked for Numerai and designed the scoring!) dominating the staking in a huge way. Giant whales dominating (and reducing the payout factor) _does_ impact the participation (in a negative way) of everybody else and that should be recognized. But it is a thorny problem, with no perfect solutions. I’d like to keep the crowd in crowd-sourcing though. (And I tend to think any schemes based on historical performance will be more problematic than beneficial which I think we agree on.)

---

### Post #53 — **wigglemuse** | 2023-10-19 16:07 UTC

Another thought: we already have de facto staking restrictions with the payout factor (which take the form of earning restrictions on your stake…it’s similar anyway). Still, one mega whale can eat the whole pie if they choose to. I keep coming back to some thought of tying payout factor to CWMM for everybody – then whales will be disincentivized from _becoming_ the MM. They can still stake a ton, but not all on the same/similar signal. And those with high-performing but low-CWMM models can earn at better rates. Doesn’t that sound about right? Or is it attackable?

---

### Post #54 — **maxchu** | 2023-10-20 05:51 UTC

I think the current stake burning and TC are theoretically enough to address most problems such as big whales and bad performing models by auto-correction (i.e. burning). But the problem is that the burning is too slow for participant who choose low multiplier for TC. From what i have seen, most big stakers’ TC multiplier is small. So the auto-correction is slow or even non-existing if TC is set to 0 (during period where TC is negative but Corr is good).  
So i think the stake weighted ensemble is not ideal if ppl can choose different multipliers. Maybe the ensemble weights should be based something like a accumulated “virtual stake” that is calculated using fixed corr + 3*tc (the optimal multipliers should be researched and determined by numerai so that it will have a better auto-correction speed, higher multipliers should have faster auto-correct speed but maybe higher churn so more research should be done. It can even be a moving average or some sort).  
Alos, i think the “virtual stake” can be used as an actual staking limit factor as it is somehow related to the accumulated actual TC of the MM. So, if you have a very high virtual stake, then naturally you can stake more.

---

### Post #55 — **maxchu** | 2023-10-20 06:07 UTC

Here is one of the example on how to implement “virtual stake” (VS) system:

  1. We can first initialize the VS to be the current stake
  2. Then we calculate the virtual payout (VP) each round normally using a _Corr + b_ TC, a and b are determined by numerai
  3. Participant’s stake level cannot exceed accumulated “virtual stake” (AVS) or avs_factor * AVS, where avs_factor is set by numerai.
  4. Now at least you will not be burnt by TC if you choose not to, but your round to round stake limit will be changed based on your AVS. So, stake that exceed AVS will be return to your wallet while stake that do not exceed AVS will be compound as usual.

---

### Post #56 — **unsentient** | 2023-10-23 20:34 UTC

The switch to 2xCorr+1xTC is a huge pay cut. Naturally this will stifle innovation/contribution.

Also, it will take longer to for high TC stakes to grow in significance to the MM and longer for low TC stakes to diminish in significance to the MM.

Flat out: the new changes reek of “downturn panic”.

First the optimizer… now the incentive structure… What next?

---

### Post #57 — **nyuton** | 2023-10-25 06:23 UTC _(reply to #55)_

There shouldn’t be any stake limit for users, who EARN their NMR. They are good data scientists, their big stake improve the meta model.

Stake limit should apply only for those who BUY their stake. They may or may not be good…

---

### Post #58 — **maxchu** | 2023-10-25 09:44 UTC _(reply to #57)_

If they are good scientists with good models, then the “virtual stake” should be basically unlimited for them. I think the main problem here is that they can chose to just use 2xCorr + 0 * TC, then they are not burnt properly based on their contribution (Here i assume TC can actually measure their contribution correctly, which i think it does to some extent).

---

### Post #59 — **profricecake** | 2023-10-26 15:13 UTC _(reply to #57)_

Many ideas have emerged; the following are particularly resonant with me:

Moving from linear stake MM weights to weights using factors such as CWMM, MCWNM, and submitter’s selected payout multiplier(s). This would help keep multiple voices in the conversation and avoid “whale emphasis”. MCWNM values equal to 1.0 signal that this a voice that’s already been heard, and that someone is just repeating someone else’s (or their own) predictions.

Having a performance-based payout multiplier that starts at 1 (aka no change to payouts) for new users but can go up or down based on daily returns. Consistent positive returns and it crawls upward, vice versa for burns. No limit on upward growth. This incentivizes people to find net positive models and run with them. They could have a 2.0 multiplier rather quickly. Note this multiplier could also be used in calculating MM stake weighting contributions as it is a measure of historical confidence.

Awards/multipliers that incentivize low CWMM and MCWNM (and CWEP–corr with example preds) but only when there’s high/positive CORR as well.

Monthly/annual NMR bonuses for steady performance.

---

### Post #60 — **taori** | 2023-11-02 10:09 UTC

I have realized that there is something I still don’t understand. I have my ideas, but I would like to ask if anybody has a better understanding of the Numerai’s point of view.

The bad performance of the hedge fund depends largely to the large stakes on models that performed bad lately, despite the tournament having many models with good performance in the same period of time (but with smaller stakes).

However Numerai still likes the idea of the Stake Weighted Meta Model, so they keep this approach and instead they have temporarily change the payout scheme from a maximum of 1xCorr+3xTC to 2xCorr+1xTC

  * How would that solve the problem? Didn’t the large stake models performed equally bad on both CORR and TC?

  * Since they are putting more weight on CORR instead of TC, that does mean TC is not useful for the hedge fund after all?

---

### Post #61 — **wigglemuse** | 2023-11-02 15:13 UTC _(reply to #60)_

Their explanation and their reaction were full of contradictions, many of which were pointed out by users afterward. So none of it really made too much sense on the face of it. (Which is why many of us are saying it sure looks like panic taking over the decision-making.) However, he did say that the payout change scheme was a very temporary stop-gap. (Again, apparently the change was an emergency and needed to happen overnight despite it not making sense and the given reasons for the problems not existing, but anyway.) But we haven’t heard a peep about what it might change to, so I don’t know. Possibly they are now doing the due consideration we were asking before the change happened (we did get SOME warning SOMETHING was going to change because Richard had started publicly dumping on TC a few weeks prior which up until then was their golden shining achievement.) Maybe they’ll even ask for some feedback…?

---

### Post #62 — **thornam** | 2023-11-04 21:50 UTC

One problem with the current MM weight system is that it is affected by the payout factor. The higher the total NMR staked, the less the MM corrects itself towards good models.

At some point (or maybe already), the correction of the MM weights toward good models by the burn/payout system will be too slow for the MM to create good performance.
