---
title: "Neutralization output in [-5, 5] range?"
category: Data Science
url: https://forum.numer.ai/t/neutralization-output-in-5-5-range/6324
created_at: 2023-04-25T12:01:24.741000+00:00
last_posted_at: 2023-04-26T19:35:33.809000+00:00
posts_count: 3
views: 676
tags: []
---

# Neutralization output in [-5, 5] range?

---

### Post #1 — **again** | 2023-04-25 12:01 UTC

Hi,

I’m trying to use the _example_model_advanced.py_ available at [GitHub - numerai/example-scripts: The official example scripts for the Numerai Data Science Tournament](<https://github.com/numerai/example-scripts>). However, what I see is that the _neutralize_ function outputs is in range [-5, 5] - is this to be expected? or is there a bug in the example code? If it is to be expected then is there some additional processing applicable before using the output of neutralization in place of predictions which are expected in [0, 1] range? What am I missing?

E.g. when running _describe_ on the prediction column in [this line](<https://github.com/numerai/example-scripts/blob/master/example_model_advanced.py#L117>) I am getting:  
count 686769.000000  
mean 0.006763  
std 1.000001  
min -4.321063  
25% -0.671214  
50% 0.004776  
75% 0.679364  
max 4.316229  
Name: preds_model_target, dtype: float64

Thank you,  
A

---

### Post #2 — **mdo** | 2023-04-26 18:04 UTC

That is expected behavior from the neutralize function. You can see that the neutralized predictions are ranked to be in [0, 1] [here](<https://github.com/numerai/example-scripts/blob/6b72e4aebbd906d4f727360f4cd0052ef08a97fc/example_model_advanced.py#L132>)

---

### Post #3 — **again** | 2023-04-26 19:35 UTC _(reply to #2)_

Thank you so much for this reply - it made my day!

I thought the line you pointed to has something to do with ensembling and didn’t even consider it to be related.

Have a great day!
