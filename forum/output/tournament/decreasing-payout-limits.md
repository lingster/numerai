---
title: "Decreasing Payout Limits?"
category: Tournament
url: https://forum.numer.ai/t/decreasing-payout-limits/5443
created_at: 2022-05-27T01:53:13.416000+00:00
last_posted_at: 2022-05-27T03:04:17.227000+00:00
posts_count: 2
views: 737
tags: []
---

# Decreasing Payout Limits?

---

### Post #1 — **red_leader** | 2022-05-27 01:53 UTC

My buddy and I have recently noticed that the calculation for payouts, and specifically the payout limits, seems to be incongruent with what is posted in the docs. In particular, the docs say that payouts are limited to “+/-25% of the stake value” but we’re finding that the actual payout is applying the limiter before the payout factor is applied leaving a true limit of approx +/-11.5% right now (i.e. true limit is payout factor * +/-25%).

Besides the fact that that doesn’t align with the example given in the docs (see screen shots below) we are concerned about the long term ramifications of the payout limit being on a sliding scale tied to payout factor.

With this calculation at a .25 payout factor all payouts would be bound to +/-.0625 and the scale would continue to decrease compressing all max payouts closer to zero. Our chief concern is that at first look this feels contrary to the ethos of the project. Wouldn’t compression of the payout range decrease the ability of the MM to penalize bad actors and reward the good ones?

This past round (313) the average TC was approx 0.01. My buddy had a great week and his model [gold_leader](<https://numer.ai/gold_leader>) had TC approx .21 staked at Corr + 2x TC. Before any payout factors or limiters his total payout was about .46.

If return was calculated as stated on the site his payout should be max(.25, .46*payout_factor) = approx 20%.

Instead it is being calculated as payout_factor * max(.25, .46) = approx 11.5%

Has it always been this way or is it a change? Also, can someone help address our concerns about the long term implications this has on payouts and the health of the MM?

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a9f325f0311e176ad63e38b19e19b0f4e9238fa4_2_690x297.png)image952×410 33.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a9f325f0311e176ad63e38b19e19b0f4e9238fa4.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/19c03e310b2cb7d3970c75c824a7903817b8b815_2_690x207.png)image944×284 14.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/19c03e310b2cb7d3970c75c824a7903817b8b815.png> "image")

---

### Post #2 — **wigglemuse** | 2022-05-27 03:04 UTC

Yes, the “payout factor” should be called the “effective stake scaling factor” (or something) because that’s the most sensible way to think about it, i.e. if you stake 100 NMR, but the PF is 0.5 then it is like you only staked 50 NMR, and then the rest of the payout math including the full 25% limit is applied to THAT (giving you a max of +/-12.5% of the actual real stake amount). Before TC, it never really came up too much if at all. Now I’ve hit both the upper and lower limits in the last 3 rounds. (However, I was grateful for the cap being the way it is on the negative side.)
