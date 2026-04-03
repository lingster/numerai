---
title: "Legacy Data Expiration"
category: Tournament
url: https://forum.numer.ai/t/legacy-data-expiration/4229
created_at: 2021-10-01T15:29:18.540000+00:00
last_posted_at: 2021-12-22T22:00:00.614000+00:00
posts_count: 9
views: 1737
tags: []
---

# Legacy Data Expiration

---

### Post #1 — **thekizoch** | 2021-10-01 15:29 UTC

Is there a timeline estimation for when the legacy dataset will be fully deprecated and unsubmittable?

---

### Post #2 — **autratec** | 2021-10-02 02:40 UTC

i hope no. not everyone is ready to move to mass data set.

---

### Post #3 — **jxtrbtk** | 2021-10-03 09:47 UTC

up ! I’d like to know also…

---

### Post #4 — **wigglemuse** | 2021-10-03 16:09 UTC

They have said it would be many months at least, and you’ll get plenty of notice. There is no scheduled date (that has been made public anyway). I’m assuming they will wait until legacy data submissions have tapered off quite a bit…

---

### Post #5 — **mic** | 2021-10-03 22:04 UTC _(reply to #4)_

and maybe the relative performance of legacy data submissions

---

### Post #6 — **kmtk49** | 2021-10-24 01:34 UTC

FYI  
<http://forum.numer.ai/t/october-2021-updates/4384>

---

### Post #7 — **dev0n** | 2021-12-21 21:25 UTC

Do they have enough info to distinguish legacy uploads from new data uploads? I don’t think they do… If I’m right maybe we should have users tag their model bio with #legacy so they can see which models are still using legacy data. (I’ve gone ahead and done that for numer.ai/dev0n and numer.ai/dev1n)

It would be a shame if they turned off legacy and were surprised by how much value the legacy models are still providing to the metamodel.

---

### Post #8 — **yxbot** | 2021-12-22 11:07 UTC _(reply to #7)_

in my view, the 6 millions dollar questions is whether new models are better than legacy models. if models trained on new data really do prove to be consistently outperforming models trained on legacy data, then for sure they can retire the legacy dataset and we should all be happy about it.

However, my baseline assumption is that at least you need 1 year worth of live performance - i.e. 3 times the 20 round window - to decide that. So I think it is reasonable to at least keep the legacy dataset for 1 year. beyond that, it should be depend on new/legacy model’s relative performance, and meta model performance with/without legacy models.

---

### Post #9 — **platemort** | 2021-12-22 22:00 UTC _(reply to #8)_

I agree that the relative performance needs to be evaluated over a long period. Here is a plot of the last 6 months of resolved rounds. The two models are different, but had similar performance until one model switched over to the super massive dataset. I would be interested if others are seeing different results, but this doesn’t look promising so far.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/713275c722f3fadb5d9048cc8e0f5aa0d50cf465_2_690x435.jpeg)image991×626 70.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/713275c722f3fadb5d9048cc8e0f5aa0d50cf465.jpeg> "image")
