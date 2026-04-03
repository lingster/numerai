---
title: "The Meta of Numerai"
category: Tournament
url: https://forum.numer.ai/t/the-meta-of-numerai/4956
created_at: 2022-02-15T19:42:02.492000+00:00
last_posted_at: 2022-02-22T15:16:49.220000+00:00
posts_count: 15
views: 1342
tags: []
---

# The Meta of Numerai

---

### Post #1 — **by256** | 2022-02-15 19:42 UTC

Most competitive pursuits have a [Meta](<https://en.wikipedia.org/wiki/Metagaming>), and Numerai is no exception. I was trying to think of the techniques that can be considered as Meta on Numerai, but the only thing that comes to mind is feature neutralization.

What else do you think can be considered as Meta in this tournament?

---

### Post #2 — **profricecake** | 2022-02-16 18:50 UTC

Love this question!

Let’s restrict the “game” of Numerai to maximizing NMR return on the classic tourney (I don’t do signals so can’t speak to that one, and I don’t want to consider the separate “game” of maximizing fiat returns on our hard-earned NMR).

The normal game of course is to build the best model(s) you can. What’s the metagame? Aka, what things can you do outside the normal structure that will up your return?

The first thing I think of relates to the flow of model-building information readily available in chat/forum.

One reactive metagame idea is to read what everyone else is doing, then deliberately move in a different direction in order to maximize your mmc relative to them.

Whenever I see a post, for example, that says “these are the features that my analysis determined were the best” I immediately assume that some large percentage of participants will just adopt those things into their models, no questions asked, thus nudging the metamodel in that specific direction. I of course try to learn from the posts - some amazing strategies come up every now and then - but I try to give them my own secret sauce rather than just using them verbatim.

A related proactive idea is to post some amazing model-building tech/research to the chat/forum… and then move in the opposite direction for the same reasons as above. AKA: get everyone to use these a certain set of features or eras or whatever and then do something deliberately different.

One more metagaming idea is to try and reverse engineer the dataset to try and find things to exploit in order to maximize corr or mmc. I’m sure everyone has pondered this at some point and I’ve learned a few things myself from trying to find patterns, but nothing that I’d consider actionable/advantageous.

Very curious to hear other ideas!

prc

---

### Post #3 — **by256** | 2022-02-16 23:01 UTC _(reply to #2)_

Great response! I was thinking more about data pre-processing, modelling, post-processing etc., so I didn’t even consider the use of information from the forum and rocket chat.

---

### Post #4 — **autratec** | 2022-02-17 05:33 UTC

Apart from exploring META, suggest we putting more effort in the real world, attracting more non-data scientists join this investment game, which will push NMR value higher and higher.

---

### Post #5 — **by256** | 2022-02-17 08:36 UTC _(reply to #4)_

You want us to stop discussing modelling techniques and other techniques that result in better performance in the tournament, and focus on increasing the price of NMR?

---

### Post #6 — **luee** | 2022-02-17 14:29 UTC

I guess at the most basic level there is a tradeoff between maximizing corr or risk-adjusted returns. As risk of ruin with non neutralized model on the main tournament is basically 0 different participants can decide to maximize return and sidestep neutralization entirely

---

### Post #7 — **profricecake** | 2022-02-17 17:39 UTC _(reply to #4)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/a/6bbea6/48.png) autratec:

> …attracting more non-data scientists join this investment game, which will push NMR value higher and higher.

With 6 million NMR in circulation and only 1 million NMR currently staked (<https://numer.ai/nmr>), there’s plenty of supply right now for any stakers who want NMR. So I’m not convinced that adding more gamers will push the value higher. Indeed, over the last year the total amount staked has only gone up (implying increased NMR demand) but the price of NMR has gone down (on average).

We’ve already got the world’s best data scientists, and they’re doing a great job at the problem they’ve been incentivized to solve. I think that adding another bunch of similar models made with similar techniques will only:

  * lower the payout factor,
  * negligibly change the metamodel, and
  * have zero impact on NMR value given the high circulating supply.



I know this opinion flies in the face of various CoE proposals aimed at increasing participation, but I personally think we should try and _reduce_ participation. Specifically, we should look to reduce the participation of folks who are only focused on CORR. Why? Richard’s comments during the last fireside chat implied that having a ton of models maximizing CORR isn’t helping the hedge fund make the kinds of revolutionary investment decisions they seek to make. But since those players still get paid, we have misaligned incentives. Result: the meta model is flooded with similar models, payout factor goes down, no one is happy.

An easy way to re-align these incentives would be eliminating pure CORR payouts. You might think I’m crazy but guess what? It’s already happening thanks to the diminishing payout factor and instability of NMR. Right now we’re all getting 0.45 * CORR. And that factor is dropping. At the prospects of earning a 2% return with a 4% CORR model but then losing 10% due to the wildly dynamic NMR price (and of course having that stake locked up for 30 days so you can’t react to NMR price changes), you might pull your money from this game.

Numerai could nudge incentives in the right direction by removing payout factor multiplication on MMC stakes. Pay MMC stakers in full, aka: `return = payoutFactor * corr + mmcMultipler * mmc` instead of `return = payoutFactor * (corr + mmcMultiplier * mmc)`.

Another option would be to make a new MMC that directly helps the hedge fund make smarter decisions, one that is so tempting returns-wise (3x??) that folks who really want to maximize returns will make models that maximize this new MMC. This is of course what they talked about at the last fireside chat and partially/prematurely rolled out as TC version 1 earlier this year. I eagerly await the next iteration.

In the meantime, if I were the hedge fund, I’d slowly gobble up circulating NMR for the treasury. Spend a percentage of hedge fund earnings each month in an effort to keep the army of data scientists in the game. After all, NMR is the gas that fuels this particular race. Numerai counts on it having value so that they can incentivize data scientists, and data scientists count on it having value in order to put their time and energy into earning it, otherwise they’ll find other ways to make income. But with so much NMR circulating, third parties have a greater impact on NMR value right now than those for whom it counts most.

These kind of changes have to be more impactful than talking a few more data scientists into joining and staking a few hundred bucks each.

---

### Post #8 — **wigglemuse** | 2022-02-17 17:55 UTC

I think they should get rid of CORR also (or de-emphasize it) – as I laid out in the FNC thread recently – it is inevitable I think. But I’m not going to change my models to try to score high on something else until they are paying for that something else. There should be no criticism about people optimizing for CORR since they have “asked for” (by paying for it) and continue to ask for (by continuing to pay for it) models that score high on CORR. When they pay on something else, that’s what they will be asking for and no doubt receive. But they also know they are doing well now under the current structure, and a bad misstep in a new direction could damage them greatly, so I expect them to tread lightly with any big transition. And no doubt the new thing will have to have significant overlap with the old thing and calibrated so that payout levels with each are roughly the same (or better for the new thing) so that users are encouraged to make the switch without waiting for some final corr expiration date.

Back to the topic of “meta”, I’m not sure I understand the concept of what “meta” is here. (I’m not a gamer – I guess that is where it comes from?)

---

### Post #9 — **gammarat** | 2022-02-17 19:31 UTC

I’d leave corr in as it’s the easiest factor to understand, allow the payout factor to continue declining, and simply raise the multiplier limit on MMC, if MMC is what Numerai is looking for. If MMC doesn’t suit Numerai’s purpose, it might help if they specified why it doesn’t, and what sorts of things would. A dominant part of problem solving lies in specifying the problem, and as far as I can see they really haven’t done that yet.

---

### Post #10 — **profricecake** | 2022-02-17 23:23 UTC _(reply to #8)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> Back to the topic of “meta”, I’m not sure I understand the concept of what “meta” is here. (I’m not a gamer – I guess that is where it comes from?)

My understanding of metagaming is that it’s about giving yourself an advantage by doing something outside the rules/context of the game itself.

Here are some metagaming examples that come immediately to mind:

  * Talking smack to your opponent to rattle them in a chess match.
  * Timing when you play a competitive online game for when you think people might be inebriated/not playing at their best (like late Friday night).
  * The New Zealand All Blacks performing the [Haka](<https://en.wikipedia.org/wiki/Haka>) before a rugby match (an intimidating war dance of sorts).
  * Muhammad Ali using the [rope-a-dope technique](<https://en.wikipedia.org/wiki/Rope-a-dope>) against Foreman to tire him out.

---

### Post #11 — **wigglemuse** | 2022-02-17 23:48 UTC _(reply to #10)_

3 of 4 of those (and maybe 4 of 4) are just good old-fashioned gamesmanship. But I’m guessing it would also be like when Captain Kirk was a cadet and was supposed to do that simulation where you are guaranteed to fail (to see his leadership under pressure), but instead he re-programmed the computer beforehand so he could actually win, and then they had to debate whether that was brilliant and creative leadership itself or just garden-variety cheating.

---

### Post #12 — **by256** | 2022-02-18 08:56 UTC _(reply to #8)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> Back to the topic of “meta”, I’m not sure I understand the concept of what “meta” is here. (I’m not a gamer – I guess that is where it comes from?)

The definition I had in mind when I posted this question was the one used in e-sports/gaming/card games. The term “meta” is used by players and developers to describe things in a game (such as characters, items, weapons, cards, decks, etc.) that are powerful and give players that use them a significant advantage. So much so, that not using things that are meta means there is almost no way to compete at the top level.

I should have made this clearer in the original post since the term isn’t that well defined. I’d say that profricecake’s definition is the more traditional one and applies more broadly to competitions, including Numerai.

---

### Post #13 — **profricecake** | 2022-02-18 16:55 UTC _(reply to #12)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/by256/48/3317_2.png) by256:

> So much so, that not using things that are meta means there is almost no way to compete at the top level.

Thanks for clarifying. I’m familiar with this usage of meta too, sorry I didn’t pick it up from your first post. It’s definitely different from metagaming as we’ve been discussing.

This “meta” is basically “what do you need to do to compete at a high level, based on what other players have figured out.” It shifts over time as people discover new things, start winning, then everyone else realizes they can’t compete without adopting those things.

The [Fosbury Flop](<https://en.wikipedia.org/wiki/Fosbury_Flop>) became meta in the high jump when everyone saw him breaking records with it.

And I wonder when an [underhand free throw](<https://www.sportscasting.com/rick-barrys-underhand-free-throws-and-why-nba-players-today-dont-follow-suit/>) like Rick Barry used to take will become meta in the NBA. Maybe never? But it’s effective!

With this in mind I’ve seen that ensembling models is very meta around here.  
Feature neutralization used to be pretty meta back in 2021 but seems to be falling off a bit.  
There’s no verdict out yet about using the old vs the new feature set. Time will tell on this one.  
Doing one’s own validation diagnostic and not solely using Numerai’s seems rather meta, too.

Others?

---

### Post #14 — **wigglemuse** | 2022-02-18 17:02 UTC

So it is more like things you just can’t do without. Well, I stopped doing FN because it was hurting me, so I don’t think that’s meta (again, until they start paying for it explicitly). However, I do keep an eye on my feature exposure and avoid models that are very high so I do self-select along those lines somewhat without neutralizing directly.

What is meta around here would probably be very general things because unlike some other games, you don’t want to be doing the same thing as everybody else (unless you are the best at it I guess). Like I have never used or even attempted to use xgboost-type boosted trees in this competition. Not interested.

---

### Post #15 — **shatteredx** | 2022-02-22 15:16 UTC

Obviously the big difference between Numerai and games like DOTA and Overwatch is that we cannot directly observe how the top competitors win or get on the leaderboard.

So, I don’t think Numerai has much of a meta beyond the github example scripts.

Actually, I would go further and say that Numerai has incentivized a lack of meta with MMC and payout factor. You lose MMC and payout factor decreases by sharing your winning model with others.

If they wanted to, Numerai or COE could counteract this by offering large NMR bounties to top competitors in return for kaggle-style “How I got #1 on the leaderboard” posts with commented code.
