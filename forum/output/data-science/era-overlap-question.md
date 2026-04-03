---
title: "Era overlap question"
category: Data Science
url: https://forum.numer.ai/t/era-overlap-question/2371
created_at: 2021-03-15T09:00:22.464000+00:00
last_posted_at: 2021-03-15T14:48:48.519000+00:00
posts_count: 2
views: 826
tags: []
---

# Era overlap question

---

### Post #1 — **nyuton** | 2021-03-15 09:00 UTC

Hi,

Is it known, whether the eras in the training set are overlapping?

Is this 120 eras 10 years or 2.5 years worth of data.

Thanks

---

### Post #2 — **wigglemuse** | 2021-03-15 14:48 UTC

Training & validation eras are non-overlapping – each era is roughly a month. (test & live are overlapping)
