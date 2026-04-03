---
title: "Question on TC: Is it True Contribution or something else?"
category: Tournament
url: https://forum.numer.ai/t/question-on-tc-is-it-true-contribution-or-something-else/5134
created_at: 2022-03-23T02:19:59.910000+00:00
last_posted_at: 2022-09-28T10:28:02.228000+00:00
posts_count: 8
views: 1814
tags: []
---

# Question on TC: Is it True Contribution or something else?

---

### Post #1 — **mic** | 2022-03-23 02:20 UTC

Thanks [@mdo](</u/mdo>) for writing up the [true contribution details](<http://forum.numer.ai/t/true-contribution-details/5128>) and [@richai](</u/richai>) for the big picture [blog post](<https://medium.com/numerai/alien-stock-market-intelligence-numerais-true-contribution-6bc7652bd6ac>)

I have a question from before, but might have been missed, or I didn’t understand the answer, so I try again.

You write the goal of true contribution is

> “to estimate how much a user’s signal improves or detracts from the returns of Numerai’s portfolio”

and true contribution is

> “gradient of optimized portfolio returns with respect to the NMR staked”

and

> “if a data scientist staked slightly more on their model (thereby increasing their weight in the Stake-Weighted Meta Model), what would the change be to post-optimization portfolio returns?”

So is the gradient the appropriate metric for true contribution goal?

For instance, imagine the user with the best predictions and the perfect stake. Sure, other users predictions can be used to improve, but this particular user shouldn’t increase or decrease their stake because it is already just right.

Do they get a TC of zero? Then as a result, would they be incentivised not to stake on this model?

If so the interests might be misaligned. HF wants `TC=0` (ie optimal stake on a model) but staker wants to maximise `(TC*stake)` and so wants `TC>>0`

Or is the users own stake always zeroed out when calculating the TC?

**TLDR** : where am i going wrong if I conclude that TC encourages increased staking on models that will help HF, but discourages continued staking on models already contributing closer to optimal ?

---

### Post #2 — **gammarat** | 2022-03-23 16:42 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/mic/48/2949_2.png) mic:

> imagine the user with the best predictions and the perfect stake. Sure, other users predictions can be used to improve, but this particular user shouldn’t increase or decrease their stake because it is already just right.

I don’t think it works that way; if someone’s prediction is the best, then increasing their stake will increase the performance of the portfolio, so TC should be positive.

One would, OTOH, get a zero TC if neither increasing nor decreasing one’s stake makes any difference to the portfolio. Which would imply that one’s predictions are pretty much the same as an average prediction.

Note: this is predicated on the assumption I understand TC. That’s still a very weak assumption…

---

### Post #3 — **mdo** | 2022-03-23 17:35 UTC

Thanks [@mic](</u/mic>) for the great question. This is a concern I had as well, but it turns out to be far more of a theoretical than an empirical or practical concern. A nice way to assess this is to evaluate the distribution of gradients for each user across the 100 rounds of dropout. Because in each round of dropout ~50% of staked users have their stakes zeroed out, for each user there are ~50 gradients taken with their stake set to 0 and ~50 taken at their full stake. If we compare these two distributions of gradients using a t-test and find their difference to be statistically insignificant then the effect of stake on the TC estimate isn’t much of a concern. I did this analysis on with the largest staker, user [stocks_ai_g](<https://numer.ai/stocks_ai_g>), and found that indeed it was the case that the difference between the two distributions was statistically insignificant. It looks like there _could_ be a significant difference with extremely large stakes, i.e. 5%+ of the total staked, but no one is even close to that so it really doesn’t matter. Furthermore, the optimal distribution of stakes is a moving target as the market evolves, i.e. what is optimal one week may not be next week, which makes it even less of a concern. And to encourage originality, it _has_ to work such that increased stakes on similar signals yield less and less payout, otherwise it would have the same problems as CORR. But it is something we’ll keep an eye on, just in case!

---

### Post #4 — **mic** | 2022-03-24 04:47 UTC _(reply to #2)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gammarat/48/3281_2.png) gammarat:

> Note: this is predicated on the assumption I understand TC. That’s still a very weak assumption…

Lol me too, but working on it

---

### Post #5 — **mic** | 2022-03-24 08:35 UTC _(reply to #3)_

Thanks [@mdo](</u/mdo>)

The results of your gradient analysis are interesting.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> Furthermore, the optimal distribution of stakes is a moving target as the market evolves, i.e. what is optimal one week may not be next week, which makes it even less of a concern.

Yes, and then throw in the effect of TC feedback on staking, which is obviously not represented in the back filled history. This will probably have a longer response time, but both could affect the stability of TC numbers.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> And to encourage originality, it _has_ to work such that increased stakes on similar signals yield less and less payout, otherwise it would have the same problems as CORR

Yes, with care to maintain the core existing signals which have value themselves and upon which the originality of the new signals is valuable.  
  
  
Have you tried a simulation on a round where stakes are modified in response to TC feedback over a number of iterations? To see if it is stable and where HF returns end up in relation to existing staking and to optimal staking?  
  


There are many interactions and levers, it’s definitely going to be interesting to see how it works! Good job so far!

---

### Post #6 — **taori** | 2022-09-27 20:27 UTC

Initially I was totally sold by the explanation of [@mdo](</u/mdo>), but now that I think again about it I am not convinced anymore. However it is simple to verify if [@mic](</u/mic>) concerns are real: compute TC on some predictions, then update stakes with TC values, then compute TC again on the same predictions and if you get TC=0 then you know it’s a real problem. However if you don’t get TC=0 then you still have a problem, but somewhere else, since TC is not working as it should.

---

### Post #7 — **mdo** | 2022-09-28 10:00 UTC _(reply to #6)_

Remember TC is a gradient, so it tells you the direction and relative magnitude to modify stakes, not the step you need to make all TC values go to 0. Also remember it is calculated with dropout, so about half the time it is computed as if your stake was 0. Generally speaking, the stake updates (i.e. step sizes) are pretty small and so one update wouldn’t shift TC values that much for a given round.

---

### Post #8 — **taori** | 2022-09-28 10:28 UTC _(reply to #7)_

> Remember TC is a gradient, so it tells you the direction and relative magnitude to modify stakes,

Exactly my point. The gradient tells you how much you need to modify the stake so that the same predictions but with an updated stake (stake+TC) would result in a portfolio construction that produces higher returns.

Recomputing TC with same predictions but updated weights (stake+TC), either gives lower TCs (in absolute value - close to 0) because the new weights improved the returns of the portfolio and so less changes (TC) are now required to improve the returns of the portfolio, or the whole process is not giving you a better portfolio, which means something is broken in the code.

> not the step you need to make all TC values go to 0

TC going towards 0 is the consequence of the above, not the goal.

> Generally speaking, the stake updates (i.e. step sizes) are pretty small and so one update wouldn’t shift TC values that much for a given round.

Agree but It would make the TCs smaller. Not 0, but smaller. Run the test I suggested and tell us what you get.

> Also remember it is calculated with dropout, so about half the time it is computed as if your stake was 0.

I initially thought you were right, but I have changed my mind. If a certain set of predictions requires a certain set of weights (stakes) to build an optimal portfolio out of them, then if you zeroed half of them, it not required that the gradients change because you didn’t modify the whole balance of the system. If the dropout process follows a uniform distribution then it doesn’t modify the system balance, so the TCs won’t change much. Try to zero out only one model and check how much TC change.
