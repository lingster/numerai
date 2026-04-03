---
title: "True Contribution for dummies"
category: Tournament
url: https://forum.numer.ai/t/true-contribution-for-dummies/5744
created_at: 2022-10-11T15:08:11.615000+00:00
last_posted_at: 2024-08-25T12:37:15.984000+00:00
posts_count: 49
views: 3833
tags: []
---

# True Contribution for dummies

---

### Post #1 — **taori** | 2022-10-11 15:08 UTC

Here is my attempt at summarizing how TC works. I would really appreciate if you could correct me if I am wrong in any part of this. My goal is to have a quick overview of TC mechanics without going through the code details in the original [post](<http://forum.numer.ai/t/true-contribution-details/>). Although I personally prefer code over words, not everybody has the time to go through the code and that prevents useful discussions. So here is my summary:

1 - At the beginning of a round, Numerai computes the Stake Weighted Meta Model (SWMM): each model predictions count in the Metal Model as much as the model stake.

2- The SWMM predictions are given in input to the portfolio optimizer, which decides the Numerai’s portfolio positions considering also the constraints the fund has to obey (e.g. max exposition to sector, country, stock, factor etc). Because of these constraints the optimizer is limited on how much the predictions are taken into consideration, that’s why the simple correlation of each model predictions with the real market performance cannot express the true contribution of a model.

3 - At the end of a round, the real market data is used to compute the returns of the Numerai’s portfolio and its stake gradient with respect to real market returns. This gradient is the TC.

4 - TC is “the direction and relative magnitude to modify stakes” to obtain a portfolio with higher returns. That is, if we built a new SWMM with the modified stakes and gave it in input to the same optimizer of step 2, it would result in a portfolio that would have produced higher returns in that round. And if we applied this process (gradient computation and stake update) multiple times we could find the optimal stake values for that round, the one that produces the portfolio with higher returns. That would be overfitting though, so the stakes are updated only once per round.

5 - Round by round, the model stakes, which are being updated by TC, will tend to gradually reach the values that generate the optimal Stake Weighted Meta Model. i.e. the SWMM that given in input to the optimizer would result in the portfolio with higher returns

6 - However, because of market and model volatility, models addition/removal and stakes increase/decrease by users, there will never be an optimal stake value, so we have to always expect TC fluctuations.

7 - We can finally say that TC is the direction and relative magnitude to modify a model stake to make it optimal wrt the Numerai’s portfolio. The stake value is the actual model contribution and TC is the round-by-round adjustment.

8 - The payout is based on TC. This works great if a model stake is below its optimal value: TC is positive if a model is useful in the Numerai’s portfolio and it is negative otherwise. Also a model with negative TC will have its stake depleted and a model with positive TC will have its stake increased - however only to some extent.

9 - I see the following problems with the payout based on TC when a model is indeed contributing to the Numerai’s fund:

  * when the model stake reaches its optimal value then TC will be fluctuating around 0 (continuously adjusting due to the tournament noise)
  * when a user increases the model stake above the model optimal stake then TC will be negative



I have read several times users saying that the model is not useful anymore because TC is zero or even negative, however that is not correct. In the two scenarios above, If the model was useless or detrimental to the fund, then its stake would have already reached 0. So the model is still useful to the fund and if it was removed from the tournament the Numerai’s portfolio would be affected negatively.

So we have a problem here: the model is useful, but it is not rewarded for that. Even worse the model has the stake stuck in the blockchain and even burned.

The fact that the users don’t know the optimal stake value for their models makes the issue impossible to deal with. And it’s not a small issue.

10 - There is an additional step in the TC computation that I haven’t discussed yet:

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png)[True Contribution Details](<https://forum.numer.ai/t/true-contribution-details/5128/1>)

> To regularize this gradient, reduce the effect of stake size, and reduce dependencies between user predictions we can perform dropout on the user stakes (i.e. randomly zero-out 50% of the stakes) before calculating the stake weighted Meta Model and calculating the gradients. To calculate our final TC estimate we perform 100 rounds of dropout and then average the gradients across the 100 rounds:

How much these 100 dropout rounds affect the conclusions I drew on TC? Nothing that I can think of.

---

### Post #2 — **wigglemuse** | 2022-10-11 15:41 UTC

One thing to note is that TC is not computed with respect to the _actual_ Numerai portfolio. The first version of TC did that but it was deemed (properly, I think) unfair that good predictions could be essentially rejected because they didn’t match well with the actual current Numerai holdings even if they fit the constraints of the optimizer otherwise. So TC is calculated on a proxy portfolio that is created by running SWMM through the optimizer, but it isn’t the actual portfolio which has a few additional constraints concerning which trades are actually possible given current holdings. (Because SWMM is built from scratch every week, but you can’t replace the entire real portfolio every week.) You can find discussion of this change from the initial version of TC to the final version around here somewhere.

---

### Post #3 — **joakim** | 2022-10-12 08:58 UTC

How will they simulate TC on validation? Wouldn’t they need to simulate the SWMM on validation as well then? Or would they use the previous live eras from validation? If the latter, would the simulated TC really be indicative of future TC?

---

### Post #4 — **wigglemuse** | 2022-10-12 14:12 UTC

In the fireside, they seemed to indicate they’d use the actual SWMM from the period (and those SWMM preds would be available to us as well). And yes that might not hold up forever but it is better than nothing. If they keep releasing the SWMM predictions, then we can track where the metamodel is going to some extent.

---

### Post #5 — **crownholder** | 2022-10-12 16:25 UTC

I don’t understand the scoring at all and how the current process is deemed “fair” when my models out perform most all top 10 models. I have been on this platform over a year and have never been in even the top 100. It makes no sense because I can just hold numerai and don’t risk anything, without setting up compute and using my resources for such a small return.  
whats the point if a non correlating model is number 1?

---

### Post #6 — **anthill** | 2022-10-12 20:05 UTC

> I have read several times users saying that the model is not useful anymore because TC is zero or even negative, however that is not correct. In the two scenarios above, If the model was useless or detrimental to the fund, then its stake would have already reached 0. So the model is still useful to the fund and if it was removed from the tournament the Numerai’s portfolio would be affected negatively.
> 
> So we have a problem here: the model is useful, but it is not rewarded for that.

I’m not sure if Numerai does this but it would seem to me that this issue could be handled the same way the same way that MMC is calculated. For MMC they remove the model’s contribution from the MMC before — effectively they’re comparing your predictions to a metamodel _without_ your model’s predictions. Presumably a similar thing could be done with TC which should address the issue you raise. I’m not sure they do that though (I haven’t seen anything about it in the documentation).

That said, I’d be curious to know how much of a problem this turns out to be in practice. I would think that a model’s stake would have to be quite high before a valuable and unique model would get penalized in this way.

---

### Post #7 — **anthill** | 2022-10-12 20:08 UTC _(reply to #5)_

> I don’t understand the scoring at all and how the current process is deemed “fair” when my models out perform most all top 10 models.

What metric are you looking at when you say that your models outperform the top 10? Correlation?

---

### Post #8 — **crownholder** | 2022-10-12 21:46 UTC

Maybe im wrong and it was supposed to say top 100… and yes correlation. maybe Im just too simple and don’t understand the complex way in which the leader board is determined. But if models that have been burning NMR for 2 months are considered good then I have it way backwards as to what the goal is.

---

### Post #9 — **wigglemuse** | 2022-10-12 22:10 UTC _(reply to #8)_

Burns depend on what you stake on and how much round-to-round – lots of choices there. Leaderboard position is score based only – it used to be corr, now it is TC. (20 round moving average with the current live rounds gaining in weight each day while the 4 least recent of 20 lose weight each day – at least that’s how it was done on corr). Still, I only see people with a lot of green (earns) on top of the leaderboard so don’t know what you’re talking about there really.

---

### Post #10 — **crownholder** | 2022-10-12 22:51 UTC

Whether or not you see a lot of earns really doesn’t matter as I am obviously not speaking on those models. Just those that have a lot of burns. It seems they are being rewarded for the stake and not the work put into building the model. I see just as many with a lot of burns, which my models dont burn so i was just wondering. No offense to you if one of the models are yours. I mean no harm just want to understand.  
Thanks for the info on how TC is calculated.

---

### Post #11 — **joakim** | 2022-10-13 07:38 UTC _(reply to #8)_

Can you give an example of a model that’s been burning NMR the last two months that is also ranked high?

---

### Post #12 — **taori** | 2022-10-13 10:11 UTC _(reply to #6)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/anthill/48/3275_2.png) anthill:

> I’m not sure if Numerai does this

This has been already acknowledged in [here](<http://forum.numer.ai/t/question-on-tc-is-it-true-contribution-or-something-else/>), Numerai knows it works like that, but they dismissed the problem as a theoretical one that doesn’t happen in practice. I would be happy if they ran some proper simulations and proved the users that they don’t have to worry, but they simply got rid of the matter with just one questionable explanation. But that is a fundamental property of TC that requires more attention.

At the same time, users keep seeing that TC [doesn’t correlate well with model metrics](<http://forum.numer.ai/t/a-true-contribution-backtest>), so there would be good reasons to investigate more.

Numerai has properly tested the effects of the TC mechanics on their fund (it has been reported multiple times how the performance has improved with TC,how many simulations they ran, etc), so we know it has been a great change for them, but why don’t they do a thorough analysis on the payout scheme too (the user perspective of TC)? I mean, even if there was a problem in the payout, that could be improved without getting rid of the benefits that TC brings to their fund. I don’t see why there is no discussion on this topic. Maybe I am just wrong.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/anthill/48/3275_2.png) anthill:

> That said, I’d be curious to know how much of a problem this turns out to be in practice. I would think that a model’s stake would have to be quite high before a valuable and unique model would get penalized in this way.

I just would like to see evidence that it is not a real concern and I would be happy.

---

### Post #13 — **crownholder** | 2022-10-13 16:51 UTC _(reply to #11)_

No I won’t give any examples. I’ve done that before and ended up offending someone.l.

I think anyone can go through the models and compare their standing to others. How does a model with a consistent negative corr have 100 percentile TC? Thats all I want to know, and until I can answer that question I will only hold NMR.

I put so much work into learning this that at one point I had to see a doctor for a neck strain.

I knew nothing about data science a year ago, now I can build models in both python and R. I can also build compute nodes, and that alone made Numerai worth it.

I’ll be back once I have an understanding of the scoring.

Good luck to all

---

### Post #14 — **wigglemuse** | 2022-10-13 18:00 UTC _(reply to #13)_

You didn’t offend me, if I’m who you are referring to. I was just wondering what you were talking about, same as [@joakim](</u/joakim>). Because the top of the leaderboard (which I am not on I assure you) doesn’t contain a bunch of models that are doing a bunch of burning. It just seemed a weird thing to say.

---

### Post #15 — **crownholder** | 2022-10-13 20:42 UTC _(reply to #14)_

Whats even weirder is that you’re so focused on whether or not there are a bunch burns in the models. Listen this post is about TC, and my question is about TC, yes i’m a dummy. I’m sure you’re like a genius or something, but If you cant answer the question then move on.

Let me reiterate, why are there models with no correlation ranking at the top of TC? Said models would burn NMR under the previous scoring system. Im sure my question doesn’t apply to all models and i’m sure you haven’t checked all models.

Sorry I offended you or your model.

---

### Post #16 — **taori** | 2022-10-13 23:03 UTC _(reply to #15)_

I am unhappy about the current scoring system as you are and I can understand the inconsistency of the leaderboard you are referring to. I believe there are good reasons to consider the current scoring system unfair, although I think that TC is a good mechanics for the fund and should be kept while fixing the payout. I wish Numerai could provide more data, tests and explanations on why they believe the current tournament is fair.Maybe it is just a matter of seeing things from the right perspective.

---

### Post #17 — **annon** | 2022-10-14 03:42 UTC _(reply to #15)_

Hello, Though my English is very limited,  
I have tried to make an explanation for your question.

This is just a schematic of my personal understanding,  
and there may be incorrect things.

I would be happy if it helps. If not, please offend me too.

[![corrtc](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d4f56de30199f6ec03778fc59411383a6562a312_2_385x500.png)corrtc1253×1626 182 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d4f56de30199f6ec03778fc59411383a6562a312.png> "corrtc")

---

### Post #18 — **taori** | 2022-10-14 10:20 UTC _(reply to #17)_

[@annon](</u/annon>) I like you explanation, very intuitive. That explains why a model with negative correlation might be required by the Numerai’s fund and for that reason it has positive TC. All good, but what about the payment based on TC alone? Could you tell us your thoughts?

I believe you cannot pay models on TC alone. The meta model itself is built from all the models that are indeed highly correlated with it. They contribute for the majority of the predictions and they need to be paid for the computation and their stake at risk, although the gradient will give them TC~0. A fair payment logic would include not only TC but also the part of the predictions correlated with the Meta Model.

---

### Post #19 — **annon** | 2022-10-14 13:48 UTC _(reply to #18)_

Thank you for your kind reply.

I agree with you, I think the payout system that includes Corr is better than only TC.

The reason I think so is that the source of TC is finite.

I’ll try to write some more intuitive things.

Below is an intuitive diagram.

[![intuitive_diagram](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/322356a41625c013870c69467ae47092275f82c7_2_690x461.png)intuitive_diagram770×515 27.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/322356a41625c013870c69467ae47092275f82c7.png> "intuitive_diagram")

As the metamodel improves, the sources of TC will decrease.  
So TC could be more difficult to find out.

Also, if the sources of TC decrease, The signal/noise ratio will then get worse, and the volatility of TC would increase.

(Regarding why TC is noisy. Besides the guess that extreme prediction would get high TC scores, I think one reason is that the signal of TC is relatively small.)

I am currently staking on 3xCorr and trying to make adjustments for TC, but if the TC difficulty increases in the future, I may back to Corr.

---

### Post #20 — **sunkay** | 2022-10-14 14:02 UTC

When we use CORR to evaluate models, users are rewarded if the model performs well, and punished if the model performs poorly.

When it comes to TC, it’s not the case. TC is not a metric to evaluate the quality of the model itself, it reflects whether a model can improve the overall return when it working with other models.

A model may get punished for not working well with other models, even the model may be a good model itself. (For example, models with positive CORR MMC and FNC get a negative TC.) This situation is unacceptable for model developers. Therefore, TC is a big risk to me.

Doesn’t it make more sense if TC is just for rewards and no punishments?

---

### Post #21 — **autratec** | 2022-10-14 23:19 UTC

Sounds like building a model to align with market performance, vs building a model to help numerai fund to get better performance, are two different goals. For first goal, we are competing independently, between designer and market. Under the second situation, the result was heavily impacted by those unknown teammates.

Then, the followup question is, whether the quant access those data - their teammates, to help them purposely improve the model, in order to improve the TC.

---

### Post #22 — **autratec** | 2022-10-15 02:20 UTC _(reply to #21)_

I will try to understand the logic below using one example i saw from Signal. Round 329. CORR 6.5%, IC: 0.7%. TC: 95.5%. I don’t quite understand the logic and removing and add in that signal will help dramatically improve the portfolio performance, considering CORR/IC has such low score.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/251749eb5e4e926046996062fb6991425ed4fedf_2_690x426.png)image868×537 33.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/251749eb5e4e926046996062fb6991425ed4fedf.png> "image")

---

### Post #23 — **objectscience** | 2022-10-16 00:59 UTC _(reply to #15)_

First I’d like to award you my “Salt Crown”, I’ve owned it far too long. Go forth and do great things.

Secondly, there are a LOT of really helpful people on the forum and in chat, Wiggle is one of the few who can quickly boil down the really complex into simple terms we can all understand. We hold him in high regard: getting cranky with him could leave you on the outs with the rest of the community and will certainly discourage him from commenting on your queries. I’ve been there, it’s a crappy place to be. Food for thought.

Finally, “why are there models with no correlation ranking at the top of TC…” because TC isn’t correlation. You don’t have to be a genius to understand they are completely different things, you just need to accept that they are and that [TC](<https://docs.numer.ai/tournament/true-contribution-tc>) is important to Numerai.

Competing in the tournament is completely optional.  
Staking on your submissions is also completely optional.  
So TC really doesn’t pose any risk until you’re certain you have a handle on it.

“The obstaCle is the way.”

---

### Post #25 — **crownholder** | 2022-10-16 01:46 UTC _(reply to #23)_

Its even funnier that you haven’t posted in 7 months and you came back just to reply to me…lol. Thanks Numerai… you’re not obvious at all lmao.  
Im only asking questions that FINRA would ask. In order for the platform to grow integrity must be maintained.

---

### Post #26 — **crownholder** | 2022-10-16 01:47 UTC _(reply to #22)_

Thanks for this information

---

### Post #27 — **restrading** | 2022-10-16 06:51 UTC

[@crownholder](</u/crownholder>) [@objectscience](</u/objectscience>) is also an active member of the community and posts every once in a while in RochetChat. Checkout <https://rocketchat.numer.ai/> if you haven’t.

---

### Post #28 — **taori** | 2022-10-16 07:43 UTC

Let’s roll back to where we were before things became emotional and personal, keep this thread focused on TC.

It would be interesting to know how the other users perceive the payout based only on TC, is it fair or not? At the moment we have the choice of being paid on correlation too, which is fair. However I am afraid that if we keep accepting the idea that TC is the true contribution, while in reality it is just a part of it, then there will be a time when payout based on correlation will not be possible anymore and we will be stuck on an unfair tournament. And even if payout on TC was fair under a certain logic, there would still be the issues brought up by [@sunkay](</u/sunkay>) and [@annon](</u/annon>)

I wish this thread stimulate more users to give their feedback so that we can have an overview of what is the general feeling of the community around payout based on TC.

---

### Post #29 — **shatteredx** | 2022-10-16 17:27 UTC _(reply to #28)_

I think Numerai would like to remove staking on CORR. They probably will not do so to avoid a mass exodus and NMR crashing event.

I’m fine with TC only. However, I admit that my personal models suck at TC and I have been forced to buy good TC models on Numerbay to stake on (thanks Numerbay!).

---

### Post #30 — **wigglemuse** | 2022-10-16 18:01 UTC

My initial intuition about CORR was that it needed to remain in order to give the metamodel a foundational center. With TC-only we could see the metamodel “move around” for no other reason than people are trying to have their own models be less correlated to it. (i.e. it might oscillate like a pendulum back and forth over the same spots for no other reason besides individuals are incentivized by TC to not have their models be like other individuals.) Whether that is actually what would happen I don’t know. Surprisingly, Richard at one point a few months ago said pretty much the exact same thing – we need to have corr in order to having something stable. So there doesn’t seem to be a big push on Numerai’s end to get rid of corr. Which is wise, because corr is what got them this far.

However, with the effect of the payout factor and corr being limited to 1x staking, corr is becoming less and less viable a vehicle to make much return. (I’m personally trying to get away from corr as primary for just that reason.) Still, it has been interesting that from what I can tell (just looking at the corr w/ metamodel for models that have been running a long time) the metamodel has changed remarkably little since the introduction of TC.

This does not necessarily mean that people just aren’t staking on TC or changing up their models trying to get TC. It is quite possible (I’ve pointed this out before) that even if most everybody changes up their models to maximize TC and neglects corr that the metamodel that it all creates will turn out to be more-or-less the same as it would have been under a corr-only system. Different route, different results for different individuals, but when ensembled together very close to the same result. Just a huge no op. That’s definitely a possibility.

But it is also a possibility that TC just really hasn’t had much impact yet – even if large stakers adopt it you could say it doesn’t really count as “transformational” if they didn’t specifically gear their models to TC in the first place, i.e. for pre-TC existing models stakers may enable TC staking on particular models that seem to get TC, but not on others that don’t and they continue to stake corr-only on those (and without adjusting amounts too much). And I think we do see this with the biggest stakers – they’ll take some percentage of TC if it looks reliable enough, otherwise not. But no big wholesale model revolution trying to get TC. The staking feedback by itself (if it doesn’t create a impetus to make new and different models with significant stakes) will be fairly slow in reallocating stakes to higher TC models (if stakers – particularly big stakers – even allow that reallocation).

---

### Post #31 — **murkyautomata** | 2022-10-16 23:06 UTC _(reply to #24)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/crownholder/48/1743_2.png) crownholder:

> Explain TC then instead of saying “you don’t have to be a genius”

It’s already explained in the docs. Do you expect him to tutor you in linear algebra until you understand it?

---

### Post #32 — **murkyautomata** | 2022-10-16 23:27 UTC _(reply to #28)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/t/ebca7d/48.png) taori:

> It would be interesting to know how the other users perceive the payout based only on TC, is it fair or not?

I don’t expect they will make the payout entirely TC based because TC appears to be zero-sum or at least very nearly so. Neither Numerai nor the participants benefit from the tournament becoming a zero-sum game. Numerai wants data scientists to have an incentive to participate, and it’s not as if they gain anything from burns.

The question as I see it is how much incentive does there need to be, or in other words how much of a positive sum does the game need? With too much the payout factor diminishes, people farm NMR just by submitting sample predictions, and the metamodel is saturated with these lazier submissions. With too little there is no reason for the lower performing half to participate, they drop off and the next highest group becomes the lower half and they start burning and drop off and so on until no one is left.

The solution seems pretty straight forward: adjust TC multipliers in line with payout factor but keep the corr multiplier constant. Eventually an equilibrium will be found where the corr payout is just enough to maintain the current total stake sum.

I would suggest though that staking on TC probably shouldn’t be optional. As long as its possible to farm yield just by submitting sample notebooks the payout factor is likely to continue to decline.

---

### Post #33 — **objectscience** | 2022-10-17 00:07 UTC _(reply to #30)_

Wiggle do you think the Wobble could be stabilized “in-house” by them using their own CORR based models, and then relying on the crowd to provide TC? It seems to me TC only staking would greatly extend the life of the treasury and generate much higher value for NMR spent. If I’m not mistaken current payouts aren’t sustainable, and at some point payouts need to fall into some reasonable percentage of fees earned.

---

### Post #34 — **smokh** | 2022-10-17 10:54 UTC

I have a question In point #4:

> And if we applied this process (gradient computation and stake update) multiple times we could find the optimal stake values for that round, the one that produces the portfolio with higher returns. That would be overfitting though, so the stakes are updated only once per round.

Why Numerai doesn’t use optimal stake values to calculate TC (ie: apply the process multiple times )? I can only think of one reason which is because there’s no single optimal solution, is that it or there are other reasons?

Thanks for this post.

---

### Post #35 — **restrading** | 2022-10-17 11:22 UTC

IIRC, TC is the gradient of portfolio return over stake multiplied by a constant. There might be an optimal point for stake allocations each round, but it’s unlikely to be stationary over time. That constant muiltplier would control how greedily the meta model chases the optimal point, similar to the learning rate in gradient descent. Users can also control how greedily they chase the optimal allocation of their models by setting their own TC multiplers.

---

### Post #36 — **smokh** | 2022-10-17 12:13 UTC _(reply to #35)_

What I am getting after reading your reply and reading the post again is that when calculating TC of a model for a new round, my previous TC’s will be added to my current stake, did I get this right?

---

### Post #37 — **restrading** | 2022-10-17 12:26 UTC _(reply to #36)_

[@smokh](</u/smokh>) no, the TC for any round is the gradient of the portfolio return with regard to the model’s stake for “that” round (multiplied by a constant). I.e. how much the overall portfolio “would have” improved/degrade if you had 1 more NMR staked for that round. TC value doesn’t carry across rounds.

---

### Post #38 — **smokh** | 2022-10-17 12:31 UTC _(reply to #37)_

Okay good, I understand this part so my question remains:

> That constant muiltplier would control how greedily the meta model chases the optimal point

What’s wrong with greedily chasing the optimal point?

---

### Post #39 — **restrading** | 2022-10-17 12:37 UTC _(reply to #38)_

[@smokh](</u/smokh>) there’s nothing wrong with greedily chasing the optimal point. I use the word “greedily” to refer to the heuristic instead of using it as a judgement.

[en.wikipedia.org](<https://en.wikipedia.org/wiki/Greedy_algorithm>)

### [Greedy algorithm](<https://en.wikipedia.org/wiki/Greedy_algorithm>)

A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage. In many problems, a greedy strategy does not produce an optimal solution, but a greedy heuristic can yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time. For example, a greedy strategy for the travelling salesman problem (which is of high computational complexity) is the following heuristic: "At each step of the...

---

### Post #40 — **wigglemuse** | 2022-10-17 16:06 UTC _(reply to #33)_

Umm…maybe. But not as well as not doing that (i.e. not as well as it happens now). And then they would also have to decide how much weight to give those internal models. Technically possible but I have a feeling they’d reject that idea as unNumerian.

---

### Post #41 — **greyone** | 2022-10-17 18:45 UTC

In mass online collaborations (my experience being MIT’s Theory U, Aarhus University’s Quantum Moves, Stanford University’s Eterna and now Numerai), each person becomes a node in the network. Personal identities are subsumed into and become superfluous for this new organism and its mission. Within this network/organism, as each node fires, other nodes respond to weed out noise and connect signals to associated messages and nodes to formulate new meaning and organism movement. The quicker, more frictionless and the higher the node awareness is of this process, the faster and efficiently the organism develops meaning and capacity to evolve further.

---

### Post #42 — **anthill** | 2022-10-18 17:50 UTC _(reply to #22)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/a/6bbea6/48.png) autratec:

> I don’t quite understand the logic and removing and add in that signal will help dramatically improve the portfolio performance, considering CORR/IC has such low score.

To give a heuristic example of how you could see a situation where a model gets very low Corr but very high TC, imagine that the market is divided into a number of different sectors and the metamodel does extremely well on all but one of these sectors. If you provide a model which makes very good predictions on that one missing sector, but random predictions on all the other sectors, you will end up with a very low Corr, but your model will nevertheless dramatically improve the performance of the metamodel and will get a high TC.

---

### Post #43 — **wigglemuse** | 2022-10-18 17:57 UTC _(reply to #42)_

Yes, some models can be considered like vitamins for the metamodel – they are just helping supplement some deficiency.

---

### Post #44 — **autratec** | 2022-10-19 02:47 UTC _(reply to #42)_

thanks for the explanation. it helps me thinking special strategy to get higher TC, rather than general CORR.

---

### Post #45 — **f58c** | 2023-09-15 20:17 UTC _(reply to #44)_

[@wigglemuse](</u/wigglemuse>) \- I’ve uploaded some models and they are now getting tc scores. from day to day, past rounds tc changes and updates. is tc in flux until rounds are “resolved”? my best models tend to stay relatively positive even with these changes, but I’m using tc scores to judge how much NMR to stake. any insight is greatly appreciated! thx!

---

### Post #46 — **wigglemuse** | 2023-09-15 20:40 UTC _(reply to #45)_

All scores on unresolved rounds are in flux – only the final day (day 20) of the round actually counts. The in-progress scores are “as-if” it ended today and are just something to look at.

---

### Post #47 — **f58c** | 2023-09-15 21:45 UTC _(reply to #46)_

thx! my earliest models will resolve at the end of Sept. it’ll be interesting to see the results.

---

### Post #48 — **numerologist** | 2023-09-16 18:49 UTC

> is tc in flux until rounds are “resolved”?

That’s something I don’t understand myself too.  
One would expect that values would stabilize closer to the end of a round: the farther the round from resolution, the more volatile its TC value (similar behavior we have with CORR).

But I checked one of my models which is basically 1-p example predictions, and on Thursday night it had (expectedly) horrible cumulative CORR but a very attractive (literally all the way up) cumulative TC.  
However, when I checked it on Friday morning, the result for CORR was about the same but all TC values for **all** the unresolved rounds literally **flipped** , i.e. it became cumulative negative TC all the way down.

How is something like this even possible **overnight**? It feels like something is really off (a bug?) about the algorithm that computes TC.

---

### Post #49 — **gammarat** | 2023-09-21 09:11 UTC _(reply to #9)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> Leaderboard position is score based only – it used to be corr, now it is TC. (20 round moving average with the current live rounds gaining in weight each day while the 4 least recent of 20 lose weight each day – at least that’s how it was done on corr).

The leader board is now based on a 1 year average, and it can be ranked on any of the headings. It just comes up first on TC.

---

### Post #52 — **rustydata** | 2024-08-25 12:37 UTC

Wont pretend to fully understand even the intended algo, but I think sharing my understanding of the complexity of tying fund performance may help others.

Consider 3 base cases:  
Most models agree on a prediction and mine does too;  
Models are fairly distributed on a prediction, mine fell into one decent sized bucket;  
Most models agree on a prediction, mine does not;

Then consider 2 versions of being wrong across those 3 base cases:  
The fund went with my prediction, but it turned out to be sorta wrong, but only after 15 days, and they arent down, but arent up as much as I predicted.  
My prediction wasnt wrong, but the existing fund position really didnt allow for it to realize any positive outcome.

What complicates this: We are predicting market direction but are being rewarded for fund performance which holds a bunch of proxies and hurdles, not least of which being the difference between market close (train) and what we model (live) vs the fund intraday portfolio and how it actions our models. We arent telling the fund how to enter positions and arent providing confidence intervals for price ranges. We are just giving predictions on a vector (go up a lot, maybe go down), **not** targets. By choosing to stake we are saying we are ok with the layer between. It’s a choice. We can give suggestions, ask questions, scrutinize, and can stake models or start our own funds.
