---
title: "ERROR! Values must be between 0 and 1 exclusive"
category: Tournament
url: https://forum.numer.ai/t/error-values-must-be-between-0-and-1-exclusive/2976
created_at: 2021-04-20T08:59:04.100000+00:00
last_posted_at: 2021-04-20T09:03:53.227000+00:00
posts_count: 2
views: 792
tags: []
---

# ERROR! Values must be between 0 and 1 exclusive

---

### Post #1 — **falsemodel** | 2021-04-20 08:59 UTC

I am getting strange error saying “Invalid submission values. Values must be between 0 and 1 exclusive.” even though there is no number in negative or >1 in my submission file.

I am currently limiting my predictions to 4th decimal place. Also tried with several different places but still no luck.

Any idea what could be a issue here ?  
Thanks in advance

---

### Post #2 — **themicon** | 2021-04-20 09:03 UTC

Make sure you have no values that are 0.0000 or 1.0000 (if you are using 4 decimal places).

Also, the actual values of your predictions don’t matter, it’s the relative ordering that actually matters, so using something like “preds = minmax_scale(preds, feature_range=(0.25,0.75))” would solve your problem.
