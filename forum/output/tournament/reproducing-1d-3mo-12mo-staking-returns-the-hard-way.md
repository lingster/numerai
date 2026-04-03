---
title: "Reproducing 1d, 3mo, 12mo staking returns the hard way"
category: Tournament
url: https://forum.numer.ai/t/reproducing-1d-3mo-12mo-staking-returns-the-hard-way/5850
created_at: 2022-11-15T00:45:55.434000+00:00
last_posted_at: 2022-11-15T21:13:25.054000+00:00
posts_count: 4
views: 950
tags: []
---

# Reproducing 1d, 3mo, 12mo staking returns the hard way

---

### Post #1 — **pschork** | 2022-11-15 00:45 UTC

Returns are meant to represent the return on a 1NMR stake over the give time frame. This post will  
explain the returns compounding logic and how users can validate these number themselves.

The examples in this post are available in this [Google Sheet](<https://docs.google.com/spreadsheets/d/1uZmS93ZgDub1cpq0rjQNnaihfCG3b0IuA5ci-vCpgnY/edit?usp=sharing>).

Note:

  1. Staking returns calculation currently only considers weekend rounds. We will update the returns calculation to include daily rounds when daily round payouts start.
  2. Staking returns calculation includes both resolved and unresolved round payouts



**1 Day Staking Returns**  
The 1 day returns take the delta between the current day’s projected payout vs yesterdays projected payout for all pending rounds. We divide the delta by the stake value for each of these rounds and then sum these percentages to get the 1d return.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/cb6a7b69a7d4de2c711761f75fd8444f8a0e72d4_2_690x457.png)image1694×1122 159 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cb6a7b69a7d4de2c711761f75fd8444f8a0e72d4.png> "image")


**N Month Staking Returns**  
The 3 month and 12 month returns use a different method (from 1d) that only considers the latest pending or resolve payouts going N weeks back. We divide the round payout by the round at-risk, then we compound these values with 5 weeks of compounding lag starting at week 13.

_NOTE: For these examples, I simply selected all rows from the model submissions page and pasted them into Google sheets. Because of this there can be slight rounding error when comparing to actuals._

_BTW: If you do this for your own model, make sure to update any the burns as negative since the copy/pasted as absolute values (non-negative)_

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b02a1b73997f48f6e049a5f3754c1114c9d2ee6a_2_690x301.jpeg)image1920×838 149 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b02a1b73997f48f6e049a5f3754c1114c9d2ee6a.jpeg> "image")


The 12 month return works the exact same way except that it goes further back and needs to handle a special case transition for round 298 which increased the compounding lag from 4 weeks to 5 weeks (because we moved stake selection to Mondays @ round 298).

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d9a59e31a50dfcf9edb1feac03a228f17eface45_2_475x500.jpeg)image1554×1634 262 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d9a59e31a50dfcf9edb1feac03a228f17eface45.jpeg> "image")

---

### Post #2 — **jay1100** | 2022-11-15 07:44 UTC

Thanks for this detailed explanation. Would it be possible to exclude unresolved rounds form the returns calculation? The unresolved rounds make the returns (even the 3 months returns) fluctuate a lot from day to day. This generates unnecessary headache.

---

### Post #3 — **nyuton** | 2022-11-15 08:28 UTC _(reply to #2)_

Hehe, daily returns generates headache! That’s true!

Showing results for resolved rounds should be sufficient.  
OR we could learn, not to watch scores every day, but that’s hard ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #4 — **pschork** | 2022-11-15 21:13 UTC _(reply to #2)_

We’ve debated this. I’m open to it.
