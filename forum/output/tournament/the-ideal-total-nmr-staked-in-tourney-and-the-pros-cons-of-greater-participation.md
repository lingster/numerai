---
title: "The ideal total NMR staked in tourney, and the pros/cons of greater participation"
category: Tournament
url: https://forum.numer.ai/t/the-ideal-total-nmr-staked-in-tourney-and-the-pros-cons-of-greater-participation/3308
created_at: 2021-05-15T17:30:43.153000+00:00
last_posted_at: 2021-05-17T18:54:35.540000+00:00
posts_count: 6
views: 1209
tags: []
---

# The ideal total NMR staked in tourney, and the pros/cons of greater participation

---

### Post #1 — **profricecake** | 2021-05-15 17:30 UTC

At the suggestion of [@surajp](</u/surajp>), I am posting this here.

This proposal in the CoE category [[Proposal]: Incentivized submissions for a greater reach (on 1729.com)](<http://forum.numer.ai/t/proposal-incentivized-submissions-for-a-greater-reach-on-1729-com/3300>) seeks to build visibility of (and participation in) the tournament. Implied in the proposal is the idea that more participants is better.

But is this true? I’d like to look more closely at the impact of greater participation, because in the last few weeks the growing amount of staked NMR has led to plummeting payout factors for everyone. So “greater participation” in that sense isn’t necessarily benefitting staking participants. But is it somehow better for the stability/visibility of NMR? Or the health of the metamodel?

Consider this statement:

> The ideal amount of NMR staked in the tourney should be X.

What is the value you assign X, and why?

As tourney participant, my value for X is X <= 300k, given that at 300k is when the payout factor begins dropping.

What is X from the perspective of Numerai HQ if different from mine? And why?

The CoE has been given some funding to enact proposals such as the one linked above. Before they begin doing that, I would love to hear what the CoE’s version of X is (and why).

A related statement:

> The best way to maximize the stability and value of NMR is Y.

This might open a whole new can of worms, but since the proposal I linked at the top seems to couple participation with token appreciation, I figured I’d float it here too. Because maybe I’m better off with an X > 300k if Y means that the NMR I have in the tourney is less volatile.

As a single data point: since I’ve been staking in the tourney (4ish months), the value of my total NMR portfolio in USD has moved almost 2x more due to NMRs variable value than due to tourney performance. So stability of the token is arguably of greater concern than payout factor!

Thanks all for your thoughts on this. I’m sure there are many interconnected factors at play and I’d like to understand them better.

prc

---

### Post #2 — **jrai** | 2021-05-15 22:11 UTC

This question is particularly interesting for Numerai because the answer is so different from basically any other tech company which would want to grow its userbase at all costs. I’ve often thought that Numerai _shouldn’t_ want to grow its userbase past a certain threshold. Bringing on certain participants is just bad for the meta-model. There are a bunch of colliding factors that might help weight the pros/cons of greater participation:

  * Increasing the userbase increases demand for NMR, increased demand (all else equal) will increase the value of NMR
  * Increasing the userbase does not necessarily increase meta-model efficacy
  * In the long run, increasing the userbase and then churning out negative contributors may increase meta-model efficacy
  * In the short run, increasing the userbase and waiting for negative contributors to churn may decrease meta-model efficacy



> The ideal amount of NMR staked in the tourney should be X.  
>  What is the value you assign X, and why?

Who knows? X will be determined by market equilibrium and that’s what’s so cool about it. All of the factors above will come into play for all of the market participants. Those participants will determine whether they will increase their stake or withdraw their stake based on those pieces and how it effects them at the margin. It will also be constantly changing. And so, like an individual stock price at any given time, it’s probably impossible to predict what X should be.

Directionally, it seems easier to predict (also like a stock price). I would say that X should be a lot higher than it is right now. Based on circulating supply of NMR, less than 7% (393,221 / 5,704,183) of that supply is being staked right now. The utility of NMR is to stake it and a significant minority of the supply is being staked. Maybe 25% staked tokens to circulating supply is a good target? Maybe 50%?

---

### Post #3 — **profricecake** | 2021-05-17 05:55 UTC _(reply to #2)_

Thanks for your reply!

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/jrai/48/3291_2.png) jrai:

> The utility of NMR is to stake it and a significant minority of the supply is being staked. Maybe 25% staked tokens to circulating supply is a good target? Maybe 50%?

I’m curious about this.

If more of the circulating NMR were tied up in the tourney, then I agree prices would go up because there’d be more demand. That seems good for all NMR holders, tourney participants or buy-and-hold investors.

But, the more NMR in the tourney, the lower the payouts. Indeed, at 1MM NMR staked (according to the graph here: [Overview | Numerai Docs](<https://docs.numer.ai/tournament/learn#payouts>)) the payout factor would be 0.3. At 1MM NMR, everyone will be getting 30% of their returns, assuming the payout rules don’t change. BTW 1MM is around 18% of the circulating NMR, much lower than the 25% or 50% numbers you floated.

To get a sense of what a payout factor of 0.3 would mean to participants, I sorted the leaderboard by top yearly earnings. The highest is approximately 525% and corresponds to (on average) a weekly return of about 3.6% compounding over 52 weeks. With everything else held constant, and a payout factor of 0.3, that would be a 75% annual return instead. Still impressive. Of course, this is the top model from the last 12 months.

Using a super non-scientific approach, I sorted the leaderboard by yearly return. Of all the models that had a 1-year return, positive or negative, I took the middle one at approximately 150%. This corresponds to a weekly return of about 1.8% compounded over 52 weeks.

If you slap a payout factor of 0.3 on that, you get a 32% annual return. So the more average models in the tourney would be hitting returns that are less tempting from an investment standpoint.

The tourney returns are percentages scaled by the payout factor, totally independent of the value of NMR. It doesn’t matter if NMR is priced at $1 or $100: the possibility of a big % payout is what lures participants to stake in such a risky landscape. Once that payout is worse than other more stable options in the marketplace, people will take their capital elsewhere.

So perhaps one way to answer the question about the ideal X is to pick X such that the expected percentage returns in the tourney are better than other investment options with similar risk.

In the following plot I show the best, worst, and aforementioned ‘middle’ model from the current leaderboard based on 12-month returns. I’m showing what their returns would be if the only thing that changed was the payout factor (based on the total NMR staked in the tourney, along the x-axis).

[![Screen Shot 2021-05-16 at 10.13.52 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/d463620d645d7eee80817f175f39c6c60d864b2f_2_690x427.png)Screen Shot 2021-05-16 at 10.13.52 PM881×546 46.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d463620d645d7eee80817f175f39c6c60d864b2f.png> "Screen Shot 2021-05-16 at 10.13.52 PM")

Some observations:

  * The tourney gets less volatile/risky the higher X is. Returns go down, but so do burns.
  * That middle model with a 153% return @ 300k NMR staked hits 21% @ 1.5MM NMR staked and 10% @ 3MM NMR staked.
  * With around 3MM NMR staked, the performance extremes lie around +/- 20% annually.



On the left of the graph, you get numbers that are pretty special. Sure there’s risk, but the reward is real. As we move towards the middle, less so.

I’m curious how far to the right of this chart readers would be willing to go before deciding to move their stakes elsewhere.

prc

---

### Post #4 — **mic** | 2021-05-17 10:01 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/jrai/48/3291_2.png) jrai:

> In the long run, increasing the userbase and then churning out negative contributors may increase meta-model efficacy

I suspect it is extra important now that the reward scheme is working efficiently, in that the models that are actually more valuable to the MM are the highest rewarded. Because I guess the lower rewarded models will go first.

---

### Post #5 — **one5hot76** | 2021-05-17 14:45 UTC _(reply to #4)_

Just speaking of things that people might not be thinking of, not my own personal feelings. Is there a rate of return on that chart where data scientists decide their models can do better elsewhere (perhaps even the live market)? A point where the good models start leaving instead of the bad? I speak of this now in the hopes of preventing such a thing if it were possible.

---

### Post #6 — **lucky_chicken** | 2021-05-17 18:54 UTC _(reply to #5)_

My personal feeling is that if it is no longer feasible to get 100% yearly return in NMR, it makes no sense to participate. The volatility/risk related to NMR is to big. But maybe that is what is wanted, it would force me to look at signals to see if 300% per year is a possibility there.
