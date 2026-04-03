---
title: "Tournament Test Type With NA Target"
category: Tournament
url: https://forum.numer.ai/t/tournament-test-type-with-na-target/2426
created_at: 2021-03-18T01:28:44.971000+00:00
last_posted_at: 2021-03-18T02:44:52.263000+00:00
posts_count: 4
views: 806
tags: []
---

# Tournament Test Type With NA Target

---

### Post #1 — **evanhennis** | 2021-03-18 01:28 UTC

I am digging through the data and I got to the part where I was going to use the tournament dataset to test my results. Well, all of the data_type == ‘test’ records don’t have a target value. What is the reason for this subset? The ‘live’ set is what we turn in, right?

Sorry if this is dumb and I am missing something.

---

### Post #2 — **wigglemuse** | 2021-03-18 01:41 UTC

You “turn in” predictions for everything in the “tournament file” – validation, test, and live. Live is what you are scored on (live hasn’t happened yet). test is data for which Numerai has the targets but you don’t – for internal backtesting.

---

### Post #3 — **evanhennis** | 2021-03-18 01:54 UTC

Cool. Thanks for the info. That is going to be a large list.

---

### Post #4 — **gammarat** | 2021-03-18 02:44 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/evanhennis/48/702_2.png) evanhennis:

> Sorry if this is dumb and I am missing something.

Well, at least you’re in good company, I suffered from the same confusion just a few days ago, but [@wigglemuse](</u/wigglemuse>) cleared me up.
