---
title: "Https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/signals_train_val_bbg.csv' access denied"
category: Feedback
url: https://forum.numer.ai/t/https-numerai-signals-public-data-s3-us-west-2-amazonaws-com-signals-train-val-bbg-csv-access-denied/7256
created_at: 2024-04-08T10:41:02.652000+00:00
last_posted_at: 2024-04-08T18:22:30.882000+00:00
posts_count: 4
views: 499
tags: []
---

# Https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/signals_train_val_bbg.csv' access denied

---

### Post #1 — **robprofit** | 2024-04-08 10:41 UTC

I am using opensignals to access the following file. The script was adapted from Numerai’s example code.

<https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/signals_train_val_bbg.csv>’

For about the last week I have been receiving the error message : HTTPError: HTTP Error 403: Forbidden

Has something changed in this area making the file inaccessible? Is the an alternative location of the file which I can access ?

---

### Post #2 — **thinkdevdo** | 2024-04-08 13:45 UTC

That file, and all public aws files, are no longer available. See <http://forum.numer.ai/t/signals-v1-data-release> .  
I think the ticker map may still be downloaded via the api but I’m not sure.

---

### Post #3 — **robprofit** | 2024-04-08 16:56 UTC _(reply to #2)_

Why are you saying it if you’re not sure ?

---

### Post #4 — **thinkdevdo** | 2024-04-08 18:22 UTC _(reply to #3)_

Sorry about the incomplete thought. They said they were going to keep the tickermap around for a while in the api, but I haven’t looked at it, so I don’t know if it’s the same as the file you’re requesting, or some modification of it.
