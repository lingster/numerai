---
title: "Score Submissions and Liquidity"
category: Tournament
url: https://forum.numer.ai/t/score-submissions-and-liquidity/6441
created_at: 2023-06-08T12:44:28.642000+00:00
last_posted_at: 2023-06-10T14:24:23.993000+00:00
posts_count: 3
views: 617
tags: []
---

# Score Submissions and Liquidity

---

### Post #1 — **nuowenlei** | 2023-06-08 12:44 UTC

Hello,

I’m just getting into all of this tournament and just recently submitted my first score. And it got me thinking about how the scores or stock rankings I submit would actually translate into portfolios. How do the NMR stakes translate into the amount of actual dollars put into a submission in the hedge fund?And how does liquidity of the stocks that we rank play a role in how much any particular submission is used?

Perhaps a follow up would be whether we know what are the stocks we’re ranking?

Any thoughts?

---

### Post #2 — **unsentient** | 2023-06-10 03:39 UTC

Welcome to the tournament!

To answer that question, let me first call your attention to metic called “meta model control.”

[![Screenshot_20230609_200547_Chrome](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3a35b775ea832129e2b092b7ee1684c766c216c4_2_566x500.jpeg)Screenshot_20230609_200547_Chrome1080×953 112 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3a35b775ea832129e2b092b7ee1684c766c216c4.jpeg> "Screenshot_20230609_200547_Chrome")

That is basically the the “wight” or your contributions to the metamodel on a percentage basis. The larger your stake, the more Numerai will “trust” your predictions as stake size is a measure of your confidence in your own predictions.

So how would that translate to the trades the Numerai is making on the open stock market. Well lets assume Numerai has one billion USD in assets under management (AMU). If my model has 0.0013% control than that roughly represents 1.3 million USD in buying/selling power in the primary market.

To your follow up question we dont know which stocks we are predicting on. We dont need to know.

---

### Post #3 — **wigglemuse** | 2023-06-10 14:24 UTC _(reply to #2)_

Your math is off there – that meta model control is a percentage, not the actual multiplier, so you’re overestimating control of a 10NMR stake by 100x.

As far as the actual amount they are dealing with, according to the latest fireside chat (just this week), there is currently about 350M AUM, but they are trading with leverage which puts them at about 2B in the actual market.

But it isn’t like they are just buying/shorting X percentage of whatever each user’s predictions recommend – they only take a few hundred total positions (roughly half long and half short). So that’s the weight your predictions have in that decision process, and it all goes into the optimizer, and they of course have to consider their current portfolio at all times, etc. So it is just an ever-evolving target to go for starting from wherever they are at presently each trading day. (Although they are still only trading weekly at the moment but are moving towards daily.)
