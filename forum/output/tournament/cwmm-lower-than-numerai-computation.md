---
title: "CWMM lower than numerai computation"
category: Tournament
url: https://forum.numer.ai/t/cwmm-lower-than-numerai-computation/7297
created_at: 2024-04-13T11:57:22.540000+00:00
last_posted_at: 2024-06-13T07:59:22.260000+00:00
posts_count: 4
views: 590
tags: []
---

# CWMM lower than numerai computation

---

### Post #1 — **eleven_sigma** | 2024-04-13 11:57 UTC

I’m using this function to compute CWMM:
    
    
    cwmm <- function(mm, preds, era) {
      pred_dt <- data.table('era' = era, 'pred' = preds, 'mm' = mm)
      pred_dt[, preds_ranked_gauss := qnorm((rank(pred, na.last = 'keep') - 0.5) / .N), by = .(era)]
      pred_dt[, preds_ranked_gauss_pot := sign(preds_ranked_gauss) * abs(preds_ranked_gauss)^1.5]
      pred_dt[, mm_ranked_gauss := qnorm((rank(mm, na.last = 'keep') - 0.5) / .N), by = .(era)]
      pred_dt[, mm_ranked_gauss_pot := sign(mm_ranked_gauss) * abs(mm_ranked_gauss)^1.5]
      corr_dt <- pred_dt[, .(CWMM = cor(mm_ranked_gauss, preds_ranked_gauss, method = 'pearson'),
                             CWMM_pot = cor(mm_ranked_gauss_pot, preds_ranked_gauss_pot, method = 'pearson')), by = .(era)]
      return(corr_dt)
    }
    > cwmm(mm, preds, era)
         era      CWMM  CWMM_pot
       <int>     <num>     <num>
    1:  1100 0.8589433 0.8400368
    2:  1101 0.8624765 0.8466103
    3:  1102 0.8651279 0.8510147
    4:  1103 0.8685777 0.8562474
    5:  1104 0.8814365 0.8703542
    

The CWMM of the model in numerai CWMM column is always greater than 0.93

Do you know where is the problem? Can you reproduce CWMM?  
In numerai-tools in github there isn’t the script for computing CWMM.

---

### Post #2 — **eleven_sigma** | 2024-04-13 20:08 UTC

I’ve tried with:  
ranked pred vs ranked mm  
ranked gauss pred vs ranked gauss mm  
ranked gauss pot 1.5 pred vs ranked gauss pot 1.5 mm  
and all combinations give me CWMM < 0.90 but numerai says in 0.92-0.93  
Did someone get reproduce the calculation?

---

### Post #3 — **ark** | 2024-04-22 21:53 UTC

This is the code we use for it:
    
    
        predictions = tie_kept_rank__gaussianize__pow_1_5(predictions)
        scores = predictions.apply(lambda sub: pearson_correlation(sub, meta_model))

---

### Post #5 — **eleven_sigma** | 2024-06-13 07:59 UTC _(reply to #3)_

It wasn’t trivial to find the correct combination: predictions are ranked, gaussianized and powered but meta model only ranked.  
Curious about why to apply different postprocessing to meta model and predictions before computing CWMM. At least power to 1.5 meta model as we do in CORRV2 with target.
