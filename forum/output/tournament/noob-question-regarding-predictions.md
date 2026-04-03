---
title: "Noob question regarding predictions"
category: Tournament
url: https://forum.numer.ai/t/noob-question-regarding-predictions/2299
created_at: 2021-03-11T20:16:07.219000+00:00
last_posted_at: 2021-04-01T09:39:52.009000+00:00
posts_count: 4
views: 983
tags: []
---

# Noob question regarding predictions

---

### Post #1 — **flipperpie** | 2021-03-11 20:16 UTC

Why are the example predictions not one of the 5 discrete values (0, 0,25, 0.5, 0.75, 1) ? Would my predictions suffer if I submitted them that way?

I suspect there is something obvious I’m missing.

---

### Post #2 — **wigglemuse** | 2021-03-11 20:26 UTC

Yeah, it’s a bit strange, but your predictions should be real-valued continuous like the example file, and not just the 5 values in the targets. You are not scored on error, but on ranking correlation, so the first thing that happens is your predictions are ranked and any ties eliminated. If you submit only with those 5 values, you may suffer, you may gain, but there will be a big random component to your scores so you probably don’t want that…

---

### Post #3 — **eltonwisk** | 2021-03-31 20:07 UTC

It is often the case that a number is naturally associated to the outcome of a random experiment: the number of boys in a three-child family, the number of defective light bulbs in a case of 100 bulbs, the length of time until the next customer arrives at the drive-through window at a bank. Such a number varies from trial to trial of the corresponding experiment, and does so in a way that cannot be predicted with certainty; hence, it is called a _random variable_ . In this chapter and the next we study such variables.

* * *

[J.E. Flores Bakery Service](<http://floresbakeryservice.com/>)

---

### Post #4 — **minou** | 2021-04-01 09:39 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/e/cdc98d/48.png) eltonwisk:

> drive-through window at a bank

Never knew these existed!
