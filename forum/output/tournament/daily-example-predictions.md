---
title: "Daily example predictions?"
category: Tournament
url: https://forum.numer.ai/t/daily-example-predictions/5775
created_at: 2022-10-22T13:33:10.273000+00:00
last_posted_at: 2022-10-25T13:44:56.569000+00:00
posts_count: 2
views: 599
tags: []
---

# Daily example predictions?

---

### Post #1 — **kayeffnumeraitor** | 2022-10-22 13:33 UTC

Hello,

Will example predictions be made available in the daily submission windows? I have one model ensemble that uses the example predictions and another one that gets retrained where I use the example predictions as a proxy for the meta model to teach my model to be different from it.

Apart from that, I am really pleased that there is basically no work to be done to switch to daily submissions.

---

### Post #2 — **slyfox** | 2022-10-25 13:44 UTC

yep you can download daily example predictions using

`napi.download_dataset("v4/live_example_preds.parquet")` or similar

you can find all the available files using our listDatasets endpoint in graphql (not sure if numerapi supports this yet)

<https://api-tournament.numer.ai/>

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f9e5cb81a778c2130906b360e3eac6e7b2c7a832_2_634x500.png)image1167×919 121 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f9e5cb81a778c2130906b360e3eac6e7b2c7a832.png> "image")
