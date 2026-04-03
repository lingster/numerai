---
title: "Validation metrics example script vs website diagnostics"
category: Data Science
url: https://forum.numer.ai/t/validation-metrics-example-script-vs-website-diagnostics/6051
created_at: 2023-01-19T12:31:31.229000+00:00
last_posted_at: 2023-01-25T14:48:12.084000+00:00
posts_count: 5
views: 879
tags: []
---

# Validation metrics example script vs website diagnostics

---

### Post #1 — **tessier_ashpool** | 2023-01-19 12:31 UTC

I have been playing around with validation metrics recently, been using `validation_metrics` from the example script <https://github.com/numerai/example-scripts/blob/master/utils.py> and I’ve noticed that the values which I get are very different from model diagnostic available on the website. For example validation sharpe is `0.83` on website, but calculated via the `validation_metrics` it’s `0.58`.  
Does anyone know, how are the metrics on the website calculated? How can I replicate the performance and risks metrics calculated on the tournament website locally?

---

### Post #2 — **chanes** | 2023-01-24 00:36 UTC

Hey bigcube. Can you send me a specific diagnostics ID you are having issues with? I just tried to reproduce my validation sharpe using the code from example-scripts and it matches exactly what I see on the website.

---

### Post #3 — **tessier_ashpool** | 2023-01-25 06:25 UTC _(reply to #2)_

I have tested the validation metrics for the example script vs what numbers are shown on the website.  
So to reproduce, go to <https://github.com/numerai/example-scripts> and run the `example_model.py`. The results are as following (I have changed only that we should calculate all metrics).

![Screenshot 2023-01-25](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/594763176fdb8230043cbc6596e93d0f3a9c1d3d_2_690x22.png)

The model for which the validation data has been submitted is `preds_model_target_neutral_riskiest_50` and as you can locally calculated sharpe is `0.976964`  
but when I uploaded the validation file on the website I’ve got something like this

[![Screenshot 2023-01-25 690x455](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/052faa39199d6e76e3acb7f1685de53dc18ee23f_2_690x455.png)Screenshot 2023-01-25 690x455748×494 39.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/052faa39199d6e76e3acb7f1685de53dc18ee23f.png> "Screenshot 2023-01-25 690x455")

The sharpe is ` 0.9278` which is clearly different from the locally calculated one, same with other metrics. This is quite confusing, as I’m not sure what the reason is.

---

### Post #4 — **shatteredx** | 2023-01-25 14:21 UTC _(reply to #3)_

Website diagnostics only calculates metrics on validation eras 857 to 961.

If you’re calculating validation metrics locally, it’s going to be different if you do it on the entire validation dataset. It should nearly match if you only calculate them on eras 857 to 961.

---

### Post #5 — **tessier_ashpool** | 2023-01-25 14:48 UTC _(reply to #4)_

Indeed, that was the missing link - using the range from the plot, thank you!

![Screenshot 2023-01-25](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/10f0b0b2b68358ca55b81edb0d2a4a755b8df9d4_2_690x18.png)
