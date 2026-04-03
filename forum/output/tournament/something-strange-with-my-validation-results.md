---
title: "Something strange with my validation results"
category: Tournament
url: https://forum.numer.ai/t/something-strange-with-my-validation-results/7445
created_at: 2024-05-04T02:54:45.935000+00:00
last_posted_at: 2024-05-10T10:34:10.671000+00:00
posts_count: 3
views: 416
tags: []
---

# Something strange with my validation results

---

### Post #1 — **invalid_datatype** | 2024-05-04 02:54 UTC

Hello all,

I am testing a new model and in order to get the most rapid use from the fewest training sessions, I am training on eras [-300:] and validating on 100 eras into the past. Does this seem like a valid approach? The model has only trained to an MSE loss of 0.11 over a batch size of 300, so it is not very good, but things may be promising.

Upon plotting cumulative correlation for the eras [-400:-300], I see a distinct change in the prediction correlations around era -350, approximately era 757. My model has never seen this data though.

Did something change with the way features were calculated around this time? Was this normal market volatility? If anyone has any ideas, it will be great to read them.

There are several other features of interest in this plot, but this is the main thing of interest for me right now.

Thank you!!  


[![Capture](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/6dc7d64d0592592eb441074ae7b31b3048e5415f_2_576x500.png)Capture834×723 37.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6dc7d64d0592592eb441074ae7b31b3048e5415f.png> "Capture")

---

### Post #2 — **invalid_datatype** | 2024-05-05 23:11 UTC

After a bit more training (final MSE = 0.08, batch size 300), here is what the curve looks like now. Perhaps if I train on a larger portion of the dataset, I can predict the two large drawdowns. Overall though, it seems like I can run this model for ~50 weeks. I hope it pans out.

Top plot is the same as above, bottom plot is Pearson’s Corr vs. Era into the past

[![cap2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c54a867cd6c0d1653c56bb8d1dcce86133e5cc8a_2_333x500.png)cap2837×1255 65.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c54a867cd6c0d1653c56bb8d1dcce86133e5cc8a.png> "cap2")

---

### Post #3 — **invalid_datatype** | 2024-05-10 10:34 UTC _(reply to #2)_

Okay. Well, I was correct in that things looked strange. I discovered some problems with the code I wrote. Fixed the issues, trained the model for 1 epoch on the entire validation dataset. Here are the update plots for scoring on the ‘training’ dataset, which I am confident has not been seen by the model. These are the last 200 eras, so 375-574. This behaves a lot better across time now.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/af0a933e31a9a452f83deff7d47fe341785fcfd4_2_346x500.png)image863×1246 103 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/af0a933e31a9a452f83deff7d47fe341785fcfd4.png> "image")
