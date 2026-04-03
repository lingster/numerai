---
title: "Using old model that is using v2 features for daily not possible (SOLVED)"
category: Tournament
url: https://forum.numer.ai/t/using-old-model-that-is-using-v2-features-for-daily-not-possible-solved/5841
created_at: 2022-11-11T10:56:35.036000+00:00
last_posted_at: 2022-11-11T16:43:43.533000+00:00
posts_count: 4
views: 553
tags: []
---

# Using old model that is using v2 features for daily not possible (SOLVED)

---

### Post #1 — **kamikaza26** | 2022-11-11 10:56 UTC

I have model that is depending on v2 features (count = 311) and would like to use it for daily tournament.

As far as i see that is not possible? since new live data for daily tournament is only for v3 and v4.

Am i missing something?  
Model is kamikaza29 and is currently very good in TC, it would be a shame that i cant use it ![:confused:](http://forum.numer.ai/images/emoji/twitter/confused.png?v=12)

---

### Post #2 — **autratec** | 2022-11-11 14:15 UTC

You can use API to download V2 live for prediction.

---

### Post #3 — **qeintelligence** | 2022-11-11 15:50 UTC

I am running V2, V3 and V4 models on both weekly and daily with no problems. That is, I am using my own prediction pipelines for this, but yes the numerapi library and/or directly API still support V2 for dailies. As for the compute light solution, I think at the moment the current release doesn’t support this, I did manage to also get it working with compute light but only after ‘hacking’ the files.

---

### Post #4 — **kamikaza26** | 2022-11-11 16:43 UTC

Ahhh tnx for pointing me in right direction… i was using old legacy method to get dataset…  
numerapi.NumerAPI().download_current_dataset() …

now that i looked at api docs i found that i need to use:  
numerapi.NumerAPI().download_dataset(‘v2/numerai_live_data.parquet’, dest_path)

this also helped… that i saw all avaible files…  
numerapi.NumerAPI().list_datasets()
