---
title: "Thoughts on True Contribution"
category: Tournament
url: https://forum.numer.ai/t/thoughts-on-true-contribution/4832
created_at: 2022-01-20T17:23:19.286000+00:00
last_posted_at: 2022-07-03T01:59:20.862000+00:00
posts_count: 22
views: 2906
tags: []
---

# Thoughts on True Contribution

---

### Post #1 — **jimmy_woodford** | 2022-01-20 17:23 UTC

The beta version of TC (True Contribution) has been out for a week now, and there already has been a vivid discussion surrounding it in RocketChat. I think most participants agree that it’s a good thing to try to align their incentives with Numerai’s objective. And TC and the potential future possibility to stake on it could be seen as a step in that direction. However, a number of concerns with TC have been voiced:

  * It seems to be highly volatile (both across eras with otherwise stable CORR and MMC and across players who submit similar or even identical predictions).
  * It cannot be directly trained for (even much less so than MMC).
  * It is unclear whether it may be attackable (p, 1-p).
  * A lack of documentation (this should be cleared up soon hopefully).



I have been thinking about a few additional things (some related to the points mentioned above):

  * Is the volatility of TC due to the number of stocks traded by numerai per week? If the fund only trades a handful of stocks, and a 1% change to the meta model only changes one of those trades, then your TC depends on the performance of a single stock. Is there any info how diverse Numerai’s portfolio is?
  * TC as I understand it is not time consistent. What I mean by that is, if you calculate what difference a 1% change in your meta model makes to your trades in one week, this does not take into account that you potentially would have a different portfolio to trade, had that 1% change to your meta model also been there in previous weeks.
  * TC heavily depends on Numerai’s internal optimiser. Does Numerai think that this optimiser is already as good as it could ever be? If not, it may be “dangerous” to let us try to maximise TC until Numerai realises they want to change their optimiser and we have to start over again. CORR or MMC are much more stable in comparison.
  * More general: Why are all displayed metrics restricted to 20-week averages? We all know how auto-correlated performance is. Why not show us more long-term metrics? We could even have long-term measures with confidence intervals adjusted for auto correlation. (Maybe also fill empty eras with the median or mean of models instead of -.1.) This may lead us to think more long-term instead of chasing the leaderboard’s king of the month ;).



In general, I don’t disagree that it is a good idea to provide a measure that tells us whether we “actually” helped the fund in a given week. But I doubt that it will give us much insight beyond “Have high CORR while being unique”, which we already know. And I’m afraid that if TC were ever to replace CORR and MMC completely, the Numerai tournament could break down. But maybe Numerai proves me wrong with future improvements to TC…

What are your thoughts on TC? Do you have additional concerns/suggestions? Maybe it makes sense to gather some of the ideas around TC here in the forum where they are better documented than in the chat.

(Edited for typos)

---

### Post #2 — **gammarat** | 2022-01-21 05:10 UTC

I’ve listen to the video bits on TC, read the rather vague reports on what it’s supposed to be, and paid attention to the RC chatter. And I’m still really clueless about what it is supposed to do, how it’s calculated, and how I could put it to use. And yes, I know, that’s probably all on me (not Numerai) as I am admittedly slow on these things.

But if the aim (as I understand it) is to encourage people to generate more independent predictions, maybe it could start with something a whole lot simpler? For example, start with the root-mean-square average of the Spearman correlation of a submission against all the other submissions for that round? It’s a simple computation, and only needs to be done once a week.

A result close to zero would indicate it was quite different, and independence would fall off as that number gets closer to one. Ranking on that might also be useful. After the round, one could use that number and divide it into the corr result, which would give an indication of how useful one’s algorithm might be. IDK, I’m just spitballing here.

---

### Post #3 — **jimmy_woodford** | 2022-01-21 09:45 UTC _(reply to #2)_

A measure of average correlation is interesting… I do think that it should be stake-weighted, since that is what is important for the meta model in the end, though. So correlation with the meta model may already do the trick? A simple measure that always appealed to me is your correlation with the target times a measure for your independence from the meta model, for example: CORR*(1-cor(model, metemodel)). But Numerai seems very willing to sacrifice transparency, simplicity, and trainability for increased proximity to “real” contribution (which I don’t mean in a bad way – this trade-off exists and it is subjective which point on the spectrum you prefer).

---

### Post #4 — **jefferythewind** | 2022-01-22 11:39 UTC

Don’t want to clog up your nice post here, but it appears one big issue or drawback of the current beta TC is that is it very computationally intensive. Takes a lot of time and resources to compute.

---

### Post #5 — **jacob_stahl** | 2022-01-22 23:56 UTC

From what I understand, Numerai only trades the N lowest and highest ranked stocks in a given era. Does this mean that TB200 can be used as a proxy for TC?

---

### Post #6 — **wigglemuse** | 2022-01-23 01:10 UTC

They are (I think) primarily interested in the highest and lowest ranked stocks OF THE STAKE-WEIGHTED METAMODEL. To only look at the top & bottom of each individual submission is a whole other thing which sounds like a very bad idea, and they’ve never said they’ve done that.

TB200 raw corr etc doesn’t look like a good proxy, but TB200 FNC & metamodelCorr (you want the former high, and the latter low) might be useful indicators. (Although full model FNC doesn’t seem to correlate with TC much.) I’m not sure there are any reliable indicators for what we’ve seen so far.

---

### Post #7 — **degerhan** | 2022-01-24 12:27 UTC

I vaguely remember the concepts of [Observability](<https://en.wikipedia.org/wiki/Observability>) and Controllability from my EE days.

My intuition is that a single output that merges prediction accuracy and portfolio constraint optimization makes the prediction task unobservable therefore not controllable. As in, TC would be nice to look at, but one could not use it directly to build useful models.

I no longer have the math skills for a rigorous derivation though and would be curious to hear the thoughts of the mathematically endowed members of the community.

---

### Post #8 — **bvmcheckking** | 2022-01-26 10:22 UTC

To me the main problem with this TC is that it makes the participants responsible for something we are not supposed to be responsible for.

Currently we build predictive models for the stock market and numer.ai is responsible for using these predictions to create a profitable trading strategy. This seems a logical separation of responsibilities to me.

TC would make us responsible both for the prediction of the stock market and then on top of that on how they are going to trade those predictions. I don’t think this is something we can reasonable be asked to be responsible for. If for example you look at the outcome of round 295 you can see that NOPAIXX took some of the top spots:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/9be5bcc54fd8c89c8e3031935708d9a704a5e831_2_690x251.png)image1372×500 67.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/9be5bcc54fd8c89c8e3031935708d9a704a5e831.png> "image")

Yet he ended up with negative TCs implying NOPAIXX did not do well/help. I don’t think this is a correct interpretation of what happened. NOPAIXX did ridiculously well, unfortunately it seems that numer.ai’s trading strategy generator did not work well. Then it seems to me that it’s the responsibility of numer.ai to improve their trading strategy, not on NOPAIXX to change his models such that he thinks numer.ai would make better use of them. Which as [@degerhan](</u/degerhan>) noted might be an impossible feat due to the lack of observability a participant has.

In general I do think numer.ai might have found an important problem. Because as you can see in for example round 295, [Numerai](<https://numer.ai/round/295>), is that the correlation between CORR and TC or MMC and TC seems to be remarkably low. So this does seem something that needs solving, but I don’t believe in the current solutions. I think one of the following directions makes more sense:

  1. Improve the trading strategy generator
  2. Change the metric to something we can reasonably optimize for (e.g. classification of top 200/bottom 200 stocks).
  3. Possibly check if your TC calculations are wrong, if they are there actually might not be a problem.



P.S. I also don’t per se like the way TC and MMC want to measure contribution, by adding a model to the meta model and seeing if that helps. As they believe in using Shapley values for feature selection, ([Feature Selection with BorutaShap](<http://forum.numer.ai/t/feature-selection-with-borutashap/4145>)), why don’t they believe in it for measuring our contributions (exactly where shapley values are intended for [Shapley value - Wikipedia](<https://en.wikipedia.org/wiki/Shapley_value>)).

---

### Post #9 — **gammarat** | 2022-01-26 15:36 UTC _(reply to #8)_

They may very well be using something like Shapely values to form the TC and then just Gaussianizing/zscoring the results to spread them out more.

The reason I say this is that it’s perhaps possible to have significant rank correlations and yet have the prediction be quite at odds with what they are looking for.

I came to that conclusion through work I’m doing for Signals in which I am trying to classify regimes and how to identify an era’s membership in one regime or another. I won’t go into that here (too long winded) but a curious result was that it seems possible to create predictions that are of high average corr, but do not correlate well one against another

Below is the plot of the correlations among 50 such models; each has an average corr against historical data of from 0.08 to 0.13 and Sharpe ratios on the order of 0.8 to 1.2. But the Spearman correlations one against the other range from 1 down to -0.45

[![Corr50](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/273b877db7a512b8a4084e08dc9f064f27150da6.jpeg)Corr50560×420 32 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/273b877db7a512b8a4084e08dc9f064f27150da6.jpeg> "Corr50")

FWIW, I could have easily screwed things up, that wouldn’t be unusual at all ![:laughing:](https://emoji.discourse-cdn.com/twitter/laughing.png?v=13) But it was provocative w/r to trying to understand what’s going on with TC.

---

### Post #10 — **objectscience** | 2022-01-26 16:03 UTC

[@bvmcheckking](</u/bvmcheckking>) how would you incentivize against the majority of participants just submitting nearly identical xgboost models to farm the payout?

---

### Post #11 — **bvmcheckking** | 2022-01-26 19:49 UTC

[@gammarat](</u/gammarat>)  
I do not think they are using Shapley values due to what they said on how it works counting it with and without 1% and them never mentioning something about Shapley either, but we will know when they release more details.

---

### Post #12 — **bvmcheckking** | 2022-01-26 20:10 UTC _(reply to #10)_

I am not sure what the majority does, but I think MMC (especially if based on Shapley) would do exactly what they want. So you only get a payout if you help contribute to what the participants’ responsibility is, a good MM (meta model). This is some combination of being a good model, high CORR, and being unique, low CORR with MM.

In theory numer.ai might want to pay out solely on this metric but then you get into the problem that the bottom half will lose money and drop out, and then the next half and so on until nobody is left. Also for new participants it is not really alluring to hear that only the top 50% gets paid out, I might have not felt like trying this out if I had to be in the top 50% to get any payout especially taking into account that you need to stake using volatile cryptocurrency.

So you do want some payout like CORR such that everybody can win, such that the entry barrier is not too big. One could argue that the MMC payout is relatively too low, especially now that numer.ai is pretty big they don’t need to grow as much as before. So maybe increasing the max MMC to 3x or 4x could help incentivize people to try to improve the MM more.

But also the CORR metric might not be optimal. I saw that somebody proposed to payout based on (1 - Corr With MM) * CORR. I don’t remember if this person recommended this to replace MMC, but I think it might make a lot of sense to replace CORR with this metric. The idea is that this could have a lot higher correlation with MMC than CORR has, still allowing many people to be profitable and still being pretty clear in definition/observability.

It might make sense to tweak this last formula a bit, maybe (1 - Corr with MM) ^ 2 * Corr would be better, or maybe the square root would be more strongly correlated with MMC.

---

### Post #13 — **wigglemuse** | 2022-01-27 00:34 UTC

The first version of MMC was verymuch like the first version of TC – bagging, comparing your model in and out of the metamodel. It didn’t take them long to dump that and replace it with current version, which if I remember correctly just neutralizes your model against the metamodel, and then scores the residuals against the true targets, except on covariance instead of correlation, and there is an adjustment factor to get the scale about the same. Except when we switched to the nomi target, they dropped the ball and didn’t adjust that adjustment with the result that MMC is at a lower magnitude scale now than it should be. But nobody noticed that right away so they didn’t want to change it after the fact when it was noticed, and just left it as “well, you can enable 2xMMC if you want.”

MMC still has some unfortunate tendencies, so the ultimate answer is probably not just greater multipliers, but a TC that doesn’t suck, or just a better MMC. (And if you go back in this forum you’ll find plenty of user suggestions for their idea of what MMC should be, but most of them were hella complicated or simply not well enough presented with math and examples to sell them.) I have been thinking of a more probability/information-theory version that seems pretty simple (and correct) in my head. Maybe I’ll try to actually to implement it with a simulation and see what it looks like.

Shapley values I’ve never really taken a good look at – if they are in fact all about apportioning rewards and costs to a group of participants such as this, it seems a natural thing to at least explore and it is a bit surprising I haven’t heard it proposed for this purpose until now.

---

### Post #14 — **mic** | 2022-01-27 01:21 UTC

Way to early to assess TC, especially without documentation or historic values for most models.

However the intention for TC to address issues with MMC and to reward the models that contribute most is a good.

It seems first attempt is to release the new metric in its naked glory and let participants try to find a way to optimise for it. This is a bit rough because it can’t be optimised without knowing what the other participants are submitting. Local estimation of MMC is poor and I assume will be same for TC.

Alternatively, TC could be used behind the scenes as a tool to discover better payout schemes that encourage what is valuable to the HF, rather than directly using it as the payout metric itself.

For example, if TC shows the best models are those that have high long term FNC, then reward long term FNC. Keep monitoring and adjusting til it works.

Not as direct, but might provide the separation between the optimizer and the modeling problem spaces to allow them to be solved independently.

---

### Post #15 — **wigglemuse** | 2022-01-27 04:06 UTC

I think everybody needs to make peace with the fact for any such measure, we’ll never be able to “optimize for it directly” as it will always depend on what other people are doing. I’m totally fine with that, but still it can’t just be a seemingly random Byzantine hellscape of a fitness terrain.

---

### Post #16 — **mlinux** | 2022-01-27 15:06 UTC

I think the TC is a bit too greedy and Numerai will probably want to change the logic of this over time, granted I would not say I 100% understand how this is calculated at the moment. Really, I think Numerai should encourage the community to make a large set of high performing models that not well correlated with each other. As Numerai gains access to a larger set of diverse predictions, their ensemble should naturally improve over time.

What if we did a score like FNC but instead of neutralizing your model’s prediction with all other features, you neutralizing your model’s prediction with all model’s prediction. This would encourage the community to contribute new distinct signals that are also predictive. This may need some kind of refinement such as instead of neutralizing your model’s prediction score with all models maybe just use the top N stacked model’s predictions so we are focusing on adding a new top signal. The downside side of this metric is it would be difficult to exactly know how your model will perform on this metric before your first submission, granted I do think this score should have a better correlation with MMC than this beta TC score has. This metric will also discourage people from submitting the exact same tree based model or even Numerai’s examplePreds.

---

### Post #17 — **wigglemuse** | 2022-01-27 16:19 UTC _(reply to #16)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/e5b9ba/48.png) mlinux:

> What if we did a score like FNC but instead of neutralizing your model’s prediction with all other features, you neutralizing your model’s prediction with all model’s prediction.

That is exactly what MMC is right now – neutralized against the stake-weighted version of all models. (So unstaked models aren’t included and bigger stakes have bigger influence. Which of course makes sense because that’s the actual model they use.)

---

### Post #20 — **sunkay** | 2022-07-02 14:46 UTC _(reply to #8)_

Agree. Staking on TC is really high risk now.

Bad TC score is not our responsibility if our CORR is good.

I have an idea to give TC a lower limit in payout calculation:  
If TC<0 and CORR>0, use 0 instead of TC * TC _multiplier, because our predictions is good. It turns bad after numerai’s optimization and we should not be responsible for that.

If TC<0 and CORR<0, use max(TC,CORR)* TC _multiplier instead of TC*TC _multiplier. This is to ensure TC payout is not lower than CORR payout. In this case, our predictions is bad. Sometimes it turns even worse after numerai’s optimization and we should not be responsible for that too.

I think that would be a lot more reasonable.

[@bvmcheckking](</u/bvmcheckking>) [@jefferythewind](</u/jefferythewind>) [@wigglemuse](</u/wigglemuse>)  
Do you agree?

---

### Post #21 — **wigglemuse** | 2022-07-02 16:02 UTC _(reply to #20)_

I’m not sure. My fundamental idea about TC is that it is meant as a better feedback mechanism to create a better positive feedback loop for the fund so that stakes flow to models that will improve the metamodel. So whether it is good/bad/neutral at evaluating each round or does or does not reward or punish us for things we should or should not “be responsible” for is somewhat beside the point. It actually doesn’t matter _TO US_ what it is measuring – that’s their problem.

Even if TC is perfect for evaluating a particular round, if good or bad TC in one round is not predictive of good or bad TC (respectively) in future rounds, it doesn’t work as feedback and isn’t helping the metamodel. Looking at it one round at time, the models that get good TC will have higher stakes in future rounds and the ones that get bad TC have lower stakes in future rounds – that’s the whole point. But if your TC scores are not predictive of your future TC scores to enough of an extent to get the stakes going where they need to go, then it is a failure, i.e. TC or any main payout metric _MUST_ be consistent at some minimum threshold that it creates a positive feedback loop and isn’t just randomly shuffling stakes around. And if it is consistent enough, then we can work with it no matter what it is actually measuring because anything that gets good TC will tend to get good TC in the future. (Obviously you can’t actually judge a model by a single round and we are never going to get anything super-consistent, but each round as a data point has to mean _something_.)

And so it seems to me that is what most complaints about the struggle to find good TC models boil down to: TC is just too damned inconsistent! And to the extent that’s true, that’s bad for us but it is also bad for them and the metamodel (because the feedback loop then doesn’t work). However, there are some models getting high TC that do seem fairly consistent. Or are they? Maybe they are just the current winners of the random TC lottery. It could be there is a zone of model fitness space that isn’t so spiky and if you can find that zone you can make a reasonably consistent model, and then there are large other zones of the fitness space that are an ever-changing spike/valley-ridden hellscape and the only thing being evaluated there is your luck. Can enough of us find the zone where consistency is possible, or will the sheer counter-weight of the hellzone drag us down to the extent where TC as it is just isn’t workable?

I don’t know the answer, but I would suggest to the team that anything they can do to increase the ease of obtaining consistency without giving up too much of the “true” evaluative power of their metric then they should do that. And they should realize it may lead to a better metamodel to make their metric less accurate at the portfolio level for evaluating a particular round but better at getting stakes flowing to models more likely to help in the future (which is probably a smoother function).

---

### Post #22 — **taori** | 2022-07-02 17:20 UTC _(reply to #21)_

Thanks for your insightful analysis [@wigglemuse](</u/wigglemuse>). Let me add that, as a current workaround for the unpredictability of TC, I started looking at the cumulative TC over 20 rounds and forgot about the round by round performance. That give me the feedback I need to decide if my model is worth stacking on TC. It is a poor workaround, with many problems, but It’s my current solution.

However the main problem with TC is that we are asked to train our model on CORR and we get paid on TC. If TC is the best metric to reward our models, that has to become the target for training our models, otherwise the game is not fair.

---

### Post #23 — **yxbot** | 2022-07-02 21:06 UTC _(reply to #22)_

from what I can see, you need much more than 20 rounds to evaluate TC performance. most of my V2 models with FN have slightly above zero TC over 50+ rounds, but if you look at individuals over 20 rounds then it does go up and down and hard to make a call. I also observe that V3 models seem to have higher TC volatility, but these also yield my best TC models.

personally, I like TC more than MMC - it does seem to favor FN models, and isn’t as correlate with Corr like MMC - relatively happy with lower value multipliers perhaps until the big -0.2 burns arrive!

---

### Post #24 — **sunkay** | 2022-07-03 01:59 UTC _(reply to #21)_

I found my CORR and FNCV3 are good enough and start staking on TC, then gained very bad TC ![:rofl:](http://forum.numer.ai/images/emoji/twitter/rofl.png?v=10)

Current TC can reward and punish us. I can accept penalty if my prediction is bad. But I cannot accept penalty for not adapting to the optimizer.

Most of high stake users on the leaderboard only use CORR, but their predictions made up current meta model. Obviously they worried about TC. Is there any way to make them less worried about TC？Reducing penalty for not adapting to the optimizer is my idea.
