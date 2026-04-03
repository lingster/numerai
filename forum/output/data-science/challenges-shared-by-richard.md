---
title: "Challenges shared by Richard"
category: Data Science
url: https://forum.numer.ai/t/challenges-shared-by-richard/4996
created_at: 2022-02-28T17:07:29.491000+00:00
last_posted_at: 2022-03-03T15:43:08.409000+00:00
posts_count: 3
views: 1014
tags: []
---

# Challenges shared by Richard

---

### Post #1 — **nyuton** | 2022-02-28 17:07 UTC

I guess it’s worth sharing here. Continue reading on Twitter.

[https://twitter.com/richardcraib/status/1498167957263839233?s=20&t=fOGaXayexv6TG476YqwE3g](<https://twitter.com/richardcraib/status/1498167957263839233?s=20&t=fOGaXayexv6TG476YqwE3g>)

---

### Post #2 — **luee** | 2022-02-28 18:08 UTC

In my experience, simulated data is kinda useless for training, especially when the data is so noisy. Fun blue sky project but I strongly doubt we can build a convincing generative model for the kind of data where a spearman of 3-4% is considered good, clearly our data is barely understood by our models

---

### Post #3 — **lcrmorin** | 2022-03-03 15:43 UTC _(reply to #2)_

Depending on how you see it adding noise is a form of augmentation. I think custom noise (swapping / masking / etc.) layers can practically add robustness and performance. Custom layers are way more practical than metric learning or topological data analysis.
