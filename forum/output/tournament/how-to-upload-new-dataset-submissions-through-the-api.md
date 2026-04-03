---
title: "How to upload new dataset submissions through the API"
category: Tournament
url: https://forum.numer.ai/t/how-to-upload-new-dataset-submissions-through-the-api/4311
created_at: 2021-10-10T22:10:57.820000+00:00
last_posted_at: 2021-12-18T07:52:56.062000+00:00
posts_count: 8
views: 1409
tags: []
---

# How to upload new dataset submissions through the API

---

### Post #1 — **nyuton** | 2021-10-10 22:10 UTC

Hi,

maybe stupid question, but how do you upload the submission through the API with the new dataset?

I could do it without any hassle with the old dataset. Now I get this error:

`ValueError: Test prediction ids do not match. IDs must match current tournament data exactly, including ordering. Make sure you are using the latest tournament data.`

When I upload the same file manually, it works, so I guess something is wrong with my scripts…

The example script doesn’t contain automated submission either.

Thanks

---

### Post #2 — **shatteredx** | 2021-10-10 23:03 UTC

Add version=2 to the submission parameters, ala `submission_id = napi.upload_predictions("predictions.csv", model_id=model_id, version=2)`

---

### Post #3 — **zubinator** | 2021-10-11 05:40 UTC _(reply to #2)_

omg THANK YOU SO MUCH I SPENT LIKE TWO HOURS TRYING TO FIGURE THIS OUT.

---

### Post #4 — **objectscience** | 2021-10-11 18:22 UTC

Thought I was losing my mind last night. Thanks for posting this!

---

### Post #5 — **nyuton** | 2021-10-13 06:21 UTC _(reply to #2)_

Thanks!  
Looks like I was not the only one looking for this info.

---

### Post #6 — **rehoboam** | 2021-10-16 21:36 UTC

anyway to upload new validation diagnostic using numerapi?

---

### Post #7 — **shatteredx** | 2021-10-16 23:41 UTC _(reply to #6)_

It’s almost the same command as uploading submissions (no version parameter necessary): `submission_id = napi.upload_diagnostics("predictions.csv", model_id=model_id)`

---

### Post #8 — **swallowroot** | 2021-12-18 07:52 UTC _(reply to #2)_

thank you for saving a lot of my time
