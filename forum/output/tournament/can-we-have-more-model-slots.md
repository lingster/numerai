---
title: "Can we have more model slots?"
category: Tournament
url: https://forum.numer.ai/t/can-we-have-more-model-slots/5205
created_at: 2022-04-03T14:48:30.629000+00:00
last_posted_at: 2022-04-05T16:31:44.400000+00:00
posts_count: 7
views: 896
tags: []
---

# Can we have more model slots?

---

### Post #1 — **gbrecht** | 2022-04-03 14:48 UTC

# Reasoning

Why do I want to have more model slots?

# Live time needed to assess performance

Although it is not an exact science how long you have to gather live performance to assess, it takes a significant amount of time of live predictions to judge if a model is worth keeping or not.

# New metrics

When you look at my [top TC model](<https://numer.ai/gbrecht5>) you notice a gap and a comment that says that something changed in round 305. I have discontinued that model a few weeks before TC became a thing. So I am unable to judge which model makes sense based on computable metrics performance ==> I want to be able to test many ideas live

# Innovation

At any given point in time there is a myriad of tabs open with papers, github repos, blog posts about innovation which I want to try out. Now, in all honesty, the biggest reason I have not yet processed all of these ideas is not my lack of free model slots, but it would definitely help.

# Random thoughts

  * I have a quite diverse staking policy, which fills slots with production models rather than testing
  * A few of my slots are investments from family & friends in my predictions
  * I have a hard time “killing” a model
  * I wonder how many other people a full since months like I am. Maybe I am so queer that my problem is unique. Afaik there is no way from the API to get account-specific information to make a statistic, but if anybody from the team where to share stats on average model slots I would be interested



How many slots would I want? I remember Anson saying that he wants to remove the limit entirely. That is not what I am asking for! I can imagine Numerai would have to safeguard for a lot of trolling and attacks. I would be happy with a lot less than infinite slots.

---

### Post #2 — **bvmcheckking** | 2022-04-03 15:14 UTC

To me it seems the main reason you want these slots is just to estimate live performance, and telling us that this need increases with the amount of changes in the tournament.

To estimate live performance we have always had the trouble that we didn’t have recent data available, luckily this should soon change with their new planned data release. This should allow us to properly evaluate CORR and FNC(v3) ourselves. Then we still have the problem of not being able to estimate MMC,TC and Corr with meta model ourselves.

Since all data is released anyways, it might make more sense to add this to the validation diagnostics as well. Maybe the computations of TC is a bit more costly to allow unlimited, then either a cap of number of daily evaluations can be added or maybe you can submit some number of predictions each day/hour that then can be processed in batch reducing the computational power required. This seems to me to be a nicer way to evaluate your models then having to wait weeks or months before getting an idea of your new model’s TC score.

---

### Post #3 — **johnnywhippet** | 2022-04-03 17:28 UTC

I’d like to be able to delete models.

---

### Post #4 — **gbrecht** | 2022-04-03 18:32 UTC _(reply to #3)_

Delete in the sense that the complete history is wiped and you can start fresh?  
Not delete in the sense that you have one slot less?

If the former, that would be cool.

---

### Post #5 — **johnnywhippet** | 2022-04-03 19:25 UTC _(reply to #4)_

As in annihilation of a model and it’s history. ![:grinning:](http://forum.numer.ai/images/emoji/twitter/grinning.png?v=10)

---

### Post #6 — **wigglemuse** | 2022-04-04 15:55 UTC

Although I’d certainly accept some more slots, as far as testing models, it does seem that a better way forward would be just be some fairly accurate estimation of TC as it would have been at the time for old rounds (which don’t have to be so old anymore), i.e. if I can just get a pretty good approximation of the last year of TC scores on a new model, then the rest I can calculate myself, and that is better than slogging through actual live rounds in real-time.

---

### Post #7 — **yxbot** | 2022-04-05 16:31 UTC

in an ideal world, I would like an unlimited amount of slots.  
but obviously, we recognise the constraints, especially the computational resource regarding TC.

Still, a larger limit for slots would be very useful for testing different combinations of modelling approaches.

How about something like 500 unstaked slots (and if needed be, without TC computation - Corr, FNCv3, and other easier to compute metrics would suffice), and up to 100 staked slots?
