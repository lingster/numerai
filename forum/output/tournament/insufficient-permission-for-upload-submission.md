---
title: "Insufficient permission for upload_submission"
category: Tournament
url: https://forum.numer.ai/t/insufficient-permission-for-upload-submission/4977
created_at: 2022-02-21T12:04:30.227000+00:00
last_posted_at: 2022-02-21T17:38:41.302000+00:00
posts_count: 4
views: 653
tags: []
---

# Insufficient permission for upload_submission

---

### Post #1 — **jamesjoyce** | 2022-02-21 12:04 UTC

When trying to uploading with

napi = numerapi.NumerAPI(public_key,secret_key)  
napi.upload_predictions(“preds.csv”, model_id=model_id,version=2)

the message

“Insufficient permission for upload_submission”

appears: I have checked the public and secret key and the model id for accuracy. What can I do?

---

### Post #2 — **autratec** | 2022-02-21 14:40 UTC

pls try again or use manual loading first.

---

### Post #3 — **kenfus** | 2022-02-21 16:32 UTC

You need to give the correct rights when creating the API Key

---

### Post #4 — **jamesjoyce** | 2022-02-21 17:38 UTC _(reply to #3)_

Thx for the quick fix!
