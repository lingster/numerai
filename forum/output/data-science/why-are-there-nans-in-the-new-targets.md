---
title: "Why are there NaNs in the new targets?"
category: Data Science
url: https://forum.numer.ai/t/why-are-there-nans-in-the-new-targets/5830
created_at: 2022-11-08T08:27:49.006000+00:00
last_posted_at: 2022-11-11T10:27:24.395000+00:00
posts_count: 4
views: 874
tags: []
---

# Why are there NaNs in the new targets?

---

### Post #1 — **nyuton** | 2022-11-08 08:27 UTC

Can anyone explain? It doesn’t make sense to me…

---

### Post #2 — **bor1** | 2022-11-08 14:02 UTC

In general & if you are talking about the 60 day targets - we get the live data as new training data soon as possible, that means after 20 workdays have passed and the targets can be computed and filled in based on the actual stock market prices. But that is before the 60 day target is known, so those are still NaN.

---

### Post #3 — **wigglemuse** | 2022-11-08 15:29 UTC

But there are also just NaNs (that stay NaNs forever) here and there among the non-nomi targets. No explanation given, but for some reason not computable for those I guess. (They did announce there would be some like this, so I don’t think it is a bug.)

---

### Post #4 — **bor1** | 2022-11-11 10:27 UTC _(reply to #3)_

I am guessing those are companies that went bankrupt, went private, merged with another company, delisted from an exchange. Stuff like that.
