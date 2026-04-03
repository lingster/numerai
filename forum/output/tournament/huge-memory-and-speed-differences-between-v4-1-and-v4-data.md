---
title: "Huge memory (and speed) differences between v4.1 and v4 data"
category: Tournament
url: https://forum.numer.ai/t/huge-memory-and-speed-differences-between-v4-1-and-v4-data/6608
created_at: 2023-08-09T07:34:33.278000+00:00
last_posted_at: 2023-09-18T04:07:42.031000+00:00
posts_count: 10
views: 1154
tags: []
---

# Huge memory (and speed) differences between v4.1 and v4 data

---

### Post #1 — **selowan** | 2023-08-09 07:34 UTC

So, when reading the first 1000 columns of the `v4.1/train_int8.parquet` and `v4/train_int8.parquet` files there are massive differences even though the data are exactly the same:
    
    
    data = pd.read_parquet('training_data_v41.parquet', columns=feature_cols[:1000])
    data.info()
    
      <class 'pandas.core.frame.DataFrame'>
      Index: 2420521 entries, n003bba8a98662e4 to nfff2bd38e397265
      Columns: 1000 entries, feature_honoured_observational_balaamite to 
      feature_intime_impassible_ferrule
      dtypes: Int8(1000)
      memory usage: 4.5+ GB
    

and
    
    
    data = pd.read_parquet('training_data_v4.parquet', columns=feature_cols[:1000])
    data.info()
    
      <class 'pandas.core.frame.DataFrame'>
      Index: 2420521 entries, n003bba8a98662e4 to nfff2bd38e397265
      Columns: 1000 entries, feature_honoured_observational_balaamite to 
      feature_intime_impassible_ferrule
      dtypes: int8(1000)
      memory usage: 2.3+ GB
    

The 4.5 GB vs. 2.3 GB causes a 10.3 times slowdown in my pipeline. I figured the memory difference is probably because the capitalized “Int8” dtype of pandas has inherent support for missing values while the lowercase “int8” does not (I believe). But most columns don’t have missing values, so in that case the organizers should store these as regular “int8” types.

Does anyone have a nice workaround for this? I guess you can cast it to int8 but I haven’t really tested it yet (and it seems like this requires a fair bit of data copying).

---

### Post #2 — **numerologist** | 2023-08-14 19:38 UTC

I never use the “raw” data. I download it once a week, fill in NAs, convert to int8, cache locally, and then just use my cache. Rinse and repeat when the historical data is updated.

---

### Post #3 — **dmmiller** | 2023-08-19 23:20 UTC

[@numerologist](</u/numerologist>), what do you mean by caching locally? Are you saving it to disk, or something else?

---

### Post #4 — **numerologist** | 2023-08-20 18:12 UTC _(reply to #3)_

yeah, preprocess and then just pickle it

---

### Post #5 — **liborty** | 2023-09-03 00:03 UTC _(reply to #2)_

Is the historical data updated every week, or how can we tell when it has actually been updated? I do not want to duplicate this massive processing, even if it is just once every week.

---

### Post #6 — **wigglemuse** | 2023-09-03 01:53 UTC _(reply to #5)_

Nothing changes, it is only added to. Except this particular week, because MikeP said he found some things that weren’t quite right in v4 & v4.1. So validation data has changed slightly, and training data has changed very very slightly apparently. But normally nothing changes.

---

### Post #7 — **liborty** | 2023-09-03 02:26 UTC _(reply to #6)_

Thanks. But is it added to each week and is the added part detectable? Last few x lines?

---

### Post #8 — **wigglemuse** | 2023-09-03 02:41 UTC _(reply to #7)_

It is detectable by being more than last time. Once in a while it is not updated for a week and then double the next week, but possibly they’ve addressed that so it is always adding an era a week (with new targets). Basically if you want to keep up-to-date, you need to download the validation data each week and compare the eras available (and the targets available if you’re interested in that) to what you’ve already got, and add the new stuff. But you don’t have to worry about the old stuff changing.

---

### Post #9 — **wigglemuse** | 2023-09-03 14:50 UTC

Let me clarify some more: a new era is added each week (usually), and targets are added to existing eras as those targets are available. (20d & 60d). So there will be some brand-new era added with no targets, some previous existing era will have 20d targets added, and farther back some era will get their 60d targets added. So there are actually changes to different eras (target-wise). But the feature data never changes (except in special cases like this week as per above), and once filled-in, the targets don’t change.

I only care about eras with all targets filled-in (20d & 60d), so I’m just looking for that one new fully finished era each week and I ignore all the newer stuff.

---

### Post #10 — **hellozml** | 2023-09-18 04:07 UTC

Switch to the new V4.2  
Now I can read train and validation (downsample by 4) with a 16GB laptop with no kernel ‘suicide’. Was really surprised!!!

Finally - I think anyone can numeraie without excessive hardware upgrades.

“Here comes the Rain - The Cult”

Cheers
