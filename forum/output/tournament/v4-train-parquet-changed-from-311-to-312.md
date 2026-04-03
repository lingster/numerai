---
title: "V4/train.parquet changed from 311 to 312?"
category: Tournament
url: https://forum.numer.ai/t/v4-train-parquet-changed-from-311-to-312/5277
created_at: 2022-04-16T22:49:05.882000+00:00
last_posted_at: 2022-04-17T15:36:20.624000+00:00
posts_count: 3
views: 959
tags: []
---

# V4/train.parquet changed from 311 to 312?

---

### Post #1 — **eleele** | 2022-04-16 22:49 UTC

Hi, as far as I understand, v4/train.parquet [should not change along the weeks](<https://numer.ai/data/v4>) but today I observed some differences between `v4/train.parquet` downloaded one week ago with respect to the one downloaded today. The md5sums are:
    
    
      00b6c902c6c01aa9b93928509f0a7d70  311/train.parquet
      5e6b4f650354d5de0b274d983ef4c76a  312/train.parquet
    

Is there a reason?

Thanks

---

### Post #2 — **jaqume** | 2022-04-17 03:11 UTC

The new file has fewer lines:
    
    
    8896499 v4_311/train.parquet
    8879285 v4_312/train.parquet
    

and reading any file from previous week gives error:
    
    
    OSError: Could not open Parquet input source '<Buffer>': Couldn't deserialize thrift: TProtocolException: Invalid data
    

looks like napi.download_dataset() function left them corrupted.

---

### Post #3 — **eleele** | 2022-04-17 15:36 UTC

So a bug in `numerapi`? It is a bit unexpected given the substantial amount of users for that basic function…

Anyway, thanks!
