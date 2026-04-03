---
title: "Daily submission error"
category: Tournament
url: https://forum.numer.ai/t/daily-submission-error/5851
created_at: 2022-11-15T14:42:00.749000+00:00
last_posted_at: 2022-11-16T14:31:17.591000+00:00
posts_count: 5
views: 796
tags: []
---

# Daily submission error

---

### Post #1 — **ihab** | 2022-11-15 14:42 UTC

Good morning,  
I got this error today (tried twice) although I am using the latest data as show in the image attached.  
Any help is greatly appreciated. Thank you.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/388e0aeb9292b97618ab5484267f454d2575ae3a_2_690x115.png)image1845×310 40.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/388e0aeb9292b97618ab5484267f454d2575ae3a.png> "image")

---

### Post #2 — **kayeffnumeraitor** | 2022-11-15 16:15 UTC

Based on similar errors that several people reported over the last few weeks in relation with daily rounds, you are probably not using the correct function for downloading the live data:

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/ee59a6/48.png) [Daily Tournament - Update #1](<http://forum.numer.ai/t/daily-tournament-update-1/5817/8>) [Tournament](</c/tournament/7>)

> You need to download numerai_live_data.parquet instead. numerai_tournament_data only gets updated weekly.

---

### Post #3 — **ihab** | 2022-11-16 04:04 UTC _(reply to #2)_

Thank you [@kayeffnumeraitor](</u/kayeffnumeraitor>)  
Why then Numerai told everyone that there is no change needed.  
Also, what you saying seems to apply the new massive dataset. How about legacy data?

---

### Post #4 — **shatteredx** | 2022-11-16 14:26 UTC _(reply to #3)_

[@ihab](</u/ihab>) Yes, this is for v2 (legacy) as well. I had this same problem and as you said, this change “broke” the legacy pipeline for daily submissions. However, I would say it is a good change as it is much more efficient for everyone to only download the live data instead of the whole tournament file.

numerai_tournament_data.csv only gets updated weekly so download v2 numerai_live_data.parquet instead:
    
    
    from numerapi import NumerAPI
    napi = NumerAPI()
    napi.download_dataset("v2/numerai_live_data.parquet", "numerai_live_data.parquet")

---

### Post #5 — **ihab** | 2022-11-16 14:31 UTC _(reply to #4)_

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/21be8d6d88436e8b2c245275a4350cb51cf47277.png)image948×100 5.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/21be8d6d88436e8b2c245275a4350cb51cf47277.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f25386f11629c9638272412b1376407108305791.png)image1103×126 4.67 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f25386f11629c9638272412b1376407108305791.png> "image")

Same issue even when I used v2.

Any help is greatly appreciated. thank you.
