---
title: "TC strikes back"
category: Tournament
url: https://forum.numer.ai/t/tc-strikes-back/5725
created_at: 2022-09-27T08:28:44.592000+00:00
last_posted_at: 2022-09-28T13:25:50.411000+00:00
posts_count: 6
views: 705
tags: []
---

# TC strikes back

---

### Post #1 — **taori** | 2022-09-27 08:28 UTC

Today is one of those days when I am puzzled by the inconsistency between TC and other metrics. Look at the top positions in the Leaderboard, what is the metrics or combination of metrics that can explain the good TC for all of them? I am especially surprised to see my models constantly having good correlation, but inconsistent TC. [If i wasn’t lazy, I could train a decision tree on the leaderboard metrics as features and TC as output and check how metrics explain TC]

All of that doesn’t make TC wrong anyway, It is just surprising. I read multiple times the explanation of TC and I like it, it is an elegant solution. However the theoretical explanation of TC doesn’t prove that TC is doing a good job in achieving the purpose that numerai wants it to achieve: promote models that contribute to the fund and penalize models that are detrimental to it.

So, I was wondering if numerai has some sort of testing in place to verify that TC is working properly. More precisely, How does numerai verify that TC is working “fine”? And how does numerai define “fine”?

Are there models similar to integration_test used to monitor the behaviour of TC (e.g. numerai could create models that artificially and constantly predict 25%, 50% or 75% correct output of the target)?

Given the inconsistency of TC with respect to the other metrics, only proving that TC is working as expected can bring back some confidence in it.

But even if we trust TC, the fact that the users cannot compute it is a game changer in the tournament. I would like to be sure numerai are aware of the enormous size of this change (problem) as much as the users do. In the long run this issue has to be solved, right?

---

### Post #3 — **taori** | 2022-09-27 13:03 UTC

For example I would love to see how TC performs on syntethic pools of submissions, where the predictions are simulated and predict, each one, a fixed percentage of correct target. How the evolution of TC would be like for each submission? Would it converge? Would it continue to increase? I would expect the stakes to converge to the optimal values that maximize the portfolio derived from the predictions and so i expect TC to becomes zero.

---

### Post #4 — **restrading** | 2022-09-27 14:26 UTC

[@taori](</u/taori>) perhaps you can consider post some questions in the slido for the upcoming fireside, they will answer live: [Join Slido: Enter #code to vote and ask questions](<https://app.sli.do/event/fp6Y8WAAiArHBqeqJjC8Hy/live/questions>)

---

### Post #5 — **taori** | 2022-09-27 14:33 UTC _(reply to #4)_

Good point, I didn’t know about it.

---

### Post #6 — **taori** | 2022-09-28 08:08 UTC

I have been thinking at an insightful set of tests that can clarify important property of TC. Here they are…

We could use training and/or validation data target to simulate the evolution of TC and stake on a fixed set of models whose predictions are artificially created. Let’s say we have 3 models, one that correctly predicts 25% of correct target every round/era, one that predicts the 50% of correct target and the last one predicts the 75%.

We can then simulate for every era (which is a tournament round) the portfolio construction and consequent TC computation. The portfolio doesn’t need to be the same as Numerai’s, since we are interested in the evolution of TC and stake, so we can disregard the details on the constraints Numerai has.

Finally, how does the evolution of TCs and stakes look like during the simulation? Do TCs and stakes converge to some values? Or do TCs converge to some values and stake keep increaseing? Or, more likely, do stakes converge to the optimal values and TCs to 0?

This test alone could open our eyes already to the effectiveness of the current TC, stake and payout scheme. However there is more…

Once, in the simulation, stakes and TCs converge to some values and there is nothing interesting happening anymore, let’s say we reached era X of the simulation, is time to introduce some variance:  
1 - In one test we add a forth model at era X whose predictions are a copy of one of the 3 existing models. What happens to the TCs and stakes of the 3 existing models? And to the new one? Do the copies converge to the same amount of TC and stake?  
2 - In a second test we double the stake of one of the existing models at era X. What happens to the TCs and Stakes of the 2 other models? And to the one with doubled stake? (we could also do the complementary of this test, that is double the stake of 2 models)  
3 - In a third test we add a forth model at era X whose predictions are just random. What happens to the TCs and stakes of the 3 existing models? And to the new one?  
4 - In a forth test we add a forth model at era X whose predictions are 100% correct. What happens to the TCs and stakes of the 3 existing models? And to the new one?

---

### Post #7 — **wigglemuse** | 2022-09-28 13:25 UTC

Although we can’t compute the actual TC for the real metamodel, for a simulation you could actually do this yourself with a selection of fake models on fake targets and see what you see. Your simulation idea is quite a bit different from reality though – for instance a model that predicted even 25% of the targets correctly would blow any of our actual models out of the water by a huge margin. 1-10% is more like it. (And our predictions aren’t used as values at all, but by ranking order so getting them “right” is about ordering.)
