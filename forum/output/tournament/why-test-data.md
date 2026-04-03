---
title: "Why 'test' data?"
category: Tournament
url: https://forum.numer.ai/t/why-test-data/4997
created_at: 2022-02-28T17:57:16.081000+00:00
last_posted_at: 2022-04-10T03:18:52.198000+00:00
posts_count: 5
views: 961
tags: []
---

# Why "test" data?

---

### Post #1 — **eleele** | 2022-02-28 17:57 UTC

According to the description of the latest dataset, data with `data_type == 'test'`

> …is used for internal testing, but is not part of the tournament scoring and payouts

So, why internal testing if what matters is only the live performance? Any explanation/suggestion about internal testing?

Thanks!

---

### Post #2 — **luee** | 2022-02-28 18:04 UTC

Seems to be legacy at this point, I believe the data will be released in full with targets sometime in March

---

### Post #3 — **ambrul11** | 2022-04-08 13:43 UTC

I think they’re testing your submission to make sure it scores (based on test part) above some benchmark. If test scores of your submission are below benchmark, then they may not want to include your model into the mix. I’m a newbie to numerai, so, don’t take it as a fact.

---

### Post #4 — **themicon** | 2022-04-08 21:49 UTC _(reply to #3)_

They used to use the test data for internal stuff.

With the release of data V4, the test data has been added to the validation data and the targets are now also provided.

---

### Post #5 — **rigrog** | 2022-04-10 03:18 UTC _(reply to #4)_

It seems MikeP accepted the suggestion I made, and you upvoted (thanks!), so ‘train’ and ‘validation’ go up to era 1000, and include target numbers. After that, there are still about 27,000 rows of ‘test’ data, currently eras 1001 - 1005, with empty targets.

Next week, era 1001 will become ‘validation’ and have target numbers, era 1006 will become ‘test’. And so forth, each week.
