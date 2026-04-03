---
title: "What does the target range mean?"
category: Tournament
url: https://forum.numer.ai/t/what-does-the-target-range-mean/4495
created_at: 2021-11-13T18:18:53.929000+00:00
last_posted_at: 2021-11-25T20:49:34.390000+00:00
posts_count: 5
views: 900
tags: []
---

# What does the target range mean?

---

### Post #1 — **cl0n3r** | 2021-11-13 18:18 UTC

Is this the following assumption correct?

The target is a number between 0-1 for each stock. 0 means price will go down. 1 means price will go up. 0.5 means the price won’t change. Can we assume if we submit 0.5 for all the stocks, then we gain or loss nothing because we are not betting on the price movement?

---

### Post #2 — **annon** | 2021-11-25 01:20 UTC

My understanding is that targets are relative strength, and 0.5 does not always mean “no price movement”.  
You might want to plot the moving average of the target for each era to see if it is a market move.

---

### Post #3 — **gammarat** | 2021-11-25 15:14 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/cl0n3r/48/1847_2.png) cl0n3r:

> Can we assume if we submit 0.5 for all the stocks, then we gain or loss nothing because we are not betting on the price movement?

No. Any ties in a prediction are broken by assigning lower ranks to those lower on the list, and higher ranks to those higher on the list… So if you submitted all as 0.5, you are essentially betting that the order in which the stocks are listed is the order in which they are to be ranked and scored.  
Statistically, that may average out to zero. But that would depend on how Numerai orders its lists.

---

### Post #4 — **mugamma** | 2021-11-25 15:47 UTC _(reply to #3)_

[zetaalpha](<https://signals.numer.ai/zetaalpha/submissions>) has been submitting all 0.5s since 271.

---

### Post #5 — **gammarat** | 2021-11-25 20:49 UTC _(reply to #4)_

Well first of all, that’s on Signals, and this channel is Tournament. But other than that, the result is what one would expect: it averages close to zero. To see that, take the final cumulative score shown on the page (around -0.06) and divide by twenty (the number of rounds shown). That yields -.003.
