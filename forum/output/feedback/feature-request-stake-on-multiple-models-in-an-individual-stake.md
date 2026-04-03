---
title: "Feature request: Stake on multiple models in an individual stake"
category: Feedback
url: https://forum.numer.ai/t/feature-request-stake-on-multiple-models-in-an-individual-stake/2783
created_at: 2021-04-10T10:05:43.209000+00:00
last_posted_at: 2021-04-17T16:45:05.331000+00:00
posts_count: 3
views: 831
tags: []
---

# Feature request: Stake on multiple models in an individual stake

---

### Post #1 — **ml_is_lyf** | 2021-04-10 10:05 UTC

I’m glad Numerai has introduced a minimum stake amount to reduce the amount being spent on gas. But with NMR prices being at an all-time high, the new minimum makes stake management even more challenging than it was before.

I know stake management across multiple models is a big feature request in the community. But as far as I’ve seen this request has been around having a pool of stake where you can dictate the percentage allocated to each model. This seems even more unfeasible now with sky-high gas prices, but what if instead of controlling the percentage staked on each model for a pool, we were able to specify the percentage we allocated to each model in each individual stake we make.

The way I would see this working is we’d need a new menu that would allow us to add a new stake to our account. In this menu, we’d specify how much NMR we wanted to put on the stake (a minimum of 3 NMR as per the new requirements), and the percentage of the stake we wanted to allocate to each of our models. Once the stake is in play we wouldn’t be able to change the percentage allocated to each model or the amount of NMR on it (as I think this would incur gas fees). Then the next time we wanted to stake, we’d add a new stake to our account. The stakes could then queue up in a table and disappear once we opt to individually release them, in a table something like this:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/ddd4f344ad9b1484c5e110cd8673cd85a232f545.png)image613×196 4.94 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/ddd4f344ad9b1484c5e110cd8673cd85a232f545.png> "image")

And if you click to view the details on a stake you’d see something like this:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c81a86dbddddb549c3f00fb601fbbe5386a1b581.png)image241×214 2.36 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c81a86dbddddb549c3f00fb601fbbe5386a1b581.png> "image")

Obviously, this feature request has some problems. Firstly this would dramatically increase the complexity of staking for users, hence I see this as more of an advanced feature than a replacement of how users currently stake. Secondly, users having to manage individual stakes would become unwieldy in the long term, as if you stake each month then each year you’ll add 12 stakes to your table, so I don’t see this as a long-term solution, more as a short term quick fix.

In general, I think the concept of an individual stake being allocated to multiple models could be a good way to reduce the amount being spent on gas whilst allowing us to split our minimum 3 NMR stake between multiple models. Maybe somehow the complexity of users managing these individual stakes could be abstracted away to give the illusion of a stake pool, and individual stakes on multiple models could be happening in the backend.

---

### Post #2 — **johnnyjohnny** | 2021-04-10 17:20 UTC

this also solves what is currently a big problem which is that currently there is no efficient way to keep my stake split evenly across 3 models, regardless of which one performs well/poorly in the short term.

this is a significant pain point for me.

---

### Post #3 — **mindyoself** | 2021-04-17 16:45 UTC _(reply to #2)_

Just like a portfolio should be. ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=9)
