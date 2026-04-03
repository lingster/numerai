---
title: "New data frequency"
category: Tournament
url: https://forum.numer.ai/t/new-data-frequency/6963
created_at: 2024-01-17T13:19:11.239000+00:00
last_posted_at: 2024-01-18T22:54:51.218000+00:00
posts_count: 8
views: 516
tags: []
---

# New data frequency

---

### Post #1 — **a_sarfa** | 2024-01-17 13:19 UTC

Hi,  
I would like to know if there is a constant frequency of new data to re-train our models or if new data arrives at a random frequency ?

---

### Post #2 — **wigglemuse** | 2024-01-17 18:52 UTC

Random, but with the just released data they announced their intention to cool it for a while since we’ve had many changes lately. So we’ll probably have at least a good number of months with the v43 dataset before more changes…unless they think of a good reason to do otherwise (or especially if they discover some issue with the latest data). That’s about as sure as we can be.

---

### Post #3 — **eleven_sigma** | 2024-01-18 08:53 UTC

I don’t understand what random mean. I’m submiting daily predictions with 4.3. dataset and seems OK. What is the problem?

---

### Post #4 — **a_sarfa** | 2024-01-18 09:42 UTC _(reply to #3)_

What I mean is that in 4.3, there is no new era data every week. For example, the era 1092 will remain the last until version 4.4 arrives.

---

### Post #5 — **andralienware** | 2024-01-18 14:45 UTC _(reply to #4)_

I thought that no new data means no new feature columns or target columns, not that we will stop receiving weekly data updates in the validation set. (This way of interpreting the announcement seems consistent with how the announcement for Midnight brought up the idea of no new data). If you interpret “new data” as just new rows in the dataset (eras and stocks within eras), that should be weekly, if you interpret it as new columns in the dataset, that is mostly random.

---

### Post #6 — **a_sarfa** | 2024-01-18 16:05 UTC _(reply to #5)_

Sorry I wasnt’ clear enough. Thank you for ur answer, this way I can expect to have the data of era 1093 next week if I run ‘napi.download_dataset(“v4.3/validation_int8.parquet”)’ ?

---

### Post #7 — **andralienware** | 2024-01-18 16:17 UTC _(reply to #6)_

Yep. Do keep in mind that some of the results may be unresolved from the latest weeks. It might be worth having a part of your scripts that identifies unresolved rounds and only saves new/newly resolved data and throws out the old data so you don’t have tons of copies of eras ~600 to 1000

---

### Post #8 — **wigglemuse** | 2024-01-18 22:54 UTC

Oh right, I thought you meant whole new data. Yeah, yeah, v43 (and even v42) data will continue with a new era every week and targets being filled in as available, etc.
