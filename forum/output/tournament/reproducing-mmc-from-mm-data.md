---
title: "Reproducing MMC from MM data"
category: Tournament
url: https://forum.numer.ai/t/reproducing-mmc-from-mm-data/6972
created_at: 2024-01-19T18:37:27.258000+00:00
last_posted_at: 2024-01-19T21:57:37.977000+00:00
posts_count: 2
views: 350
tags: []
---

# Reproducing MMC from MM data

---

### Post #1 — **eleven_sigma** | 2024-01-19 18:37 UTC

I’m trying to reproduce the MMC computation using MM data and I’m a bit confusing.  
I use the era 634 predictions I sent and select one id, n0025fd06bd67f3d.  
I’m looking for this id in MM data and isn’t available.  
How are you computing MMC simulation? Why id of MM data are differents from the ids of predictions?  
Seems there is an special interest in do the things hardest than necessary: era numbers different in tournament and datasets, ids differents. Is this really necessary?

---

### Post #2 — **eleven_sigma** | 2024-01-19 21:57 UTC

I’m using a model for predict validation dataset for recent eras (eras not used in the model fitting).  
For era 1092 I’m getting 0.9327920 and this number is different to all recent closed eras:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1ef683b4d4577bc463005f6909f1f6e43536cc58.png)image824×400 19.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1ef683b4d4577bc463005f6909f1f6e43536cc58.png> "image")

Which round is the era 1092?  
This is the code I use for compute CWMM.  
Are you able to reproduce the CWMM? Someone that use R could help me?
    
    
    dtb[, mm_gauss := qnorm((rank(numerai_meta_model, na.last = 'keep') - 0.5) / .N), by = .(era)]
    dtb[, prediction_gauss := qnorm((rank(prediction, na.last = 'keep') - 0.5) / .N), by = .(era)]
    mm_correlation <- dtb[, .('mm_corr' = cor(prediction_gauss, mm_gauss, method = 'pearson')), by = .(era)]
