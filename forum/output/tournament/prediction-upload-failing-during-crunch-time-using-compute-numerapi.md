---
title: "Prediction upload failing during crunch time using compute & numerapi"
category: Tournament
url: https://forum.numer.ai/t/prediction-upload-failing-during-crunch-time-using-compute-numerapi/4510
created_at: 2021-11-15T21:36:46.725000+00:00
last_posted_at: 2021-11-16T08:53:44.953000+00:00
posts_count: 3
views: 584
tags: []
---

# Prediction upload failing during crunch time using compute & numerapi

---

### Post #1 — **profricecake** | 2021-11-15 21:36 UTC

Hi all.

I have a compute node that calculates and submits all of my predictions, one per model, one after the other.

I recently added a few more models and with that addition I started seeing failures during the auto-triggered compute runs on Saturdays.

Specifically, the failures occur with the `upload_predictions()` call from numerapi. The return message only contains the mysterious single word “data” (it normally contains the submission ID).

When I trigger the compute node myself a few hours later, it runs fine.

I suspect that heavy submission traffic might be causing this failure, and that the upload is timing out or something like that. Has anyone else experienced this? Any suggestions for how to avoid it?

Thanks in advance if so.

prc

---

### Post #2 — **by256** | 2021-11-15 22:17 UTC

I think there were some API issues on Saturday. A few of my predictions also failed to submit when I tried shortly after the round opened. There was also some discussion on RocketChat about this on the day, so I think quite a few people had the same issues.

---

### Post #3 — **jay1100** | 2021-11-16 08:53 UTC

I also had this issue several times over the last weeks.
