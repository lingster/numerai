---
title: "True Contribution: what's the point?"
category: Tournament
url: https://forum.numer.ai/t/true-contribution-whats-the-point/6383
created_at: 2023-05-21T04:51:37.234000+00:00
last_posted_at: 2023-07-20T23:08:20.418000+00:00
posts_count: 3
views: 1377
tags: []
---

# True Contribution: what's the point?

---

### Post #1 — **numerologist** | 2023-05-21 04:51 UTC

Kind of a philosophical post.  
What’s the point of TC if you can produce 0 or even negative CORRs for months and yet [score #1](<https://numer.ai/k3_04>) on the leaderboard?

[![Screenshot from 2023-05-20 21-39-44](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/49246080a4dcb1960e42320d2d462c0f4c3622df.png)Screenshot from 2023-05-20 21-39-44291×434 6.52 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/49246080a4dcb1960e42320d2d462c0f4c3622df.png> "Screenshot from 2023-05-20 21-39-44")

I guess the game is to have as unique predictions as possible without sacrificing corrs too much (i.e. 0 or slightly negative is acceptable as long as TC profit covers it), but does this help the fund in any way? I’d assume the fund’s profit depends on corrs and not on 0-corr unique predictions.

---

### Post #2 — **wigglemuse** | 2023-05-21 16:16 UTC

The fund’s profit depends on the results of specific positions held over time, and which number in the hundreds, not on on the corrs of a point-in-time for thousands of stocks. So the question should be reversed. They are telling us that TC is the thing, or the best approximation of it that also is workable as a score for us (using the actual portfolio doesn’t quite for a few reasons).

So what is the point of corr if we can get good TC without it? One reason is that it is not a black box like TC. The new corr scoring seems rather tougher than the old one, but maybe that’s just because no one has optimized for it, I don’t know. But maybe an even better question is how can we use corr to guide us to get better TC? With the old scoring, getting good corr was certainly no guarantee of getting decent TC also – I wonder if that relationship is more in-sync now?

---

### Post #3 — **numerologist** | 2023-07-20 23:08 UTC _(reply to #2)_

Ok, I understand that they trade in hundreds, not thousands of stocks. And yet, those hundreds are supposed to be sampled out of the results based on the corrs of those thousands, no? In other words, you submit ~5k predictions, and they take, let’s say, TB200 based on CORR/CORRv2: top 100 to buy, bottom 100 to sell. But even those samples _are supposed_ to be correlated if not to the entire era, then to the sampled batch for sure, right?

Therefore, this would explain the scenario when corr payouts are negative but TC is positive since even when a particular batch of predictions gives positive CORR, the majority of stocks together might produce 0 or even slightly negative CORR.

What I really don’t understand is how the complete diversion is possible:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/136679f12a3a8d98b7a616cc5fb47a0d5930a49d_2_410x500.png)image424×517 13.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/136679f12a3a8d98b7a616cc5fb47a0d5930a49d.png> "image")

If the above intuition is correct, how is it even possible that particular batches continuously perform well when the general performance of thousands of stocks, even with the new CORR20v2 metric, sucks a lot? Wouldn’t the great-performing batch skew CORR (let alone CORRv2) in the positive direction? Or at least make CORRv2 closer to 0. But what we see here is a clear diversion, which realistically doesn’t make much sense.
