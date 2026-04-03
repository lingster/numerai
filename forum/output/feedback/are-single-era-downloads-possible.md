---
title: "Are single era downloads possible?"
category: Feedback
url: https://forum.numer.ai/t/are-single-era-downloads-possible/5763
created_at: 2022-10-21T10:05:48.932000+00:00
last_posted_at: 2022-10-29T13:46:17.104000+00:00
posts_count: 6
views: 681
tags: []
---

# Are single era downloads possible?

---

### Post #1 — **kayeffnumeraitor** | 2022-10-21 10:05 UTC

Hello,

I am currently experimenting with a model that readjusts itself every week, but for that I always need the latest era with targets, so kind of a “rolling window” model. So far I downloaded the v4/validation.parquet file, which gets updated every week with new targets, but I think it is a bit time and resource intensive to download ~ 1GB each week when I just need one specific era.

Is there a way to get the latest era with targets?

If not, could the list of datasets (the one you receive with `numerapi list-datasets`) be extended with some number of latest single era datasets where the “oldest” is deleted every week to avoid clutter? So lets say current round is 100, then I would like to have something like (I dont now the exact timeframes for new targets, but you I hope you get the idea)

`v4/round_87.parquet` ← will be deleted next week  
`v4/round_88.parquet` ← new update with 60 day target  
`v4/round_93.parquet` ← will be deleted next week  
`v4/round_94.parquet` ← new update with 20 day target

These files would probably have a size of about ~1MB.

---

### Post #2 — **wigglemuse** | 2022-10-21 13:00 UTC

We don’t want any eras to be deleted entirely ever, but yeah if there was a way to download only the most recently added (with targets), that would be nice. I too download the whole thing every week and just pick the one new era off the top and throw the rest away (because I already have it). They’ve talked about making this capability to pick and choose which eras you want to download, but have not implemented it.

---

### Post #3 — **anthill** | 2022-10-21 17:19 UTC

Although there’s no officially supported way to do this (as far as I know), you could probably hack something together. You can add a byte range to an HTTP request so that you only download a portion of the file. Then you’d have to reverse engineer the byte range you’d expect for the era you want. But because the parquet file has a predictable structure this should be possible.

---

### Post #4 — **slyfox** | 2022-10-21 22:07 UTC

Not possible just yet, but I think this is a great suggestion and we will add it to our data API improvement roadmap!

---

### Post #5 — **kayeffnumeraitor** | 2022-10-29 12:47 UTC _(reply to #2)_

[@wigglemuse](</u/wigglemuse>) Since you seem to have experience: Do you know when the validation.parquet file gets updated every week? I am done experimenting and want to actually implement it, but so far I don’t actually know when to download it

---

### Post #6 — **wigglemuse** | 2022-10-29 13:46 UTC _(reply to #5)_

From what I can tell, it gets updated with the rest of the stuff when the weekly round opens on Saturday. (And doesn’t get updated again until the next week.)
