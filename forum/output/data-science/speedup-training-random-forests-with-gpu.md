---
title: "Speedup training Random Forests with GPU"
category: Data Science
url: https://forum.numer.ai/t/speedup-training-random-forests-with-gpu/4057
created_at: 2021-09-09T09:39:03.074000+00:00
last_posted_at: 2021-09-09T15:31:27.677000+00:00
posts_count: 6
views: 1429
tags: []
---

# Speedup training Random Forests with GPU

---

### Post #1 — **nyuton** | 2021-09-09 09:39 UTC

Hi,

After the first shock caused by the size of the new dataset I started looking for solutions.  
My most successful models are Random Forest based models, which were trained on a 6 core CPU. The new dataset makes this approach impossible.

Luckly I found cuML, which is an ML libary which implements algorithms with GPU support.  
Now I can train on GPU.

6 core CPU vs RTX3090 ~ 100x speed improvement. I haven’t measured it, but it’s in that ballpark.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/95397977523363a29a6bccac0cc6b785fadba3da.png) [RAPIDS | GPU Accelerated Data Science](<https://rapids.ai/>)

### [RAPIDS | GPU Accelerated Data Science](<https://rapids.ai/>)

Open source GPU accelerated data science libraries

Enjoy!

---

### Post #2 — **yxbot** | 2021-09-09 14:52 UTC

Thanks for sharing! How do you find the installation process? I remember having a look but I think the it strictly required to use their provided docker image, which put me off. maybe I should have a look.

A very good alternative would be XGB-GPU powered RF:  
<https://xgboost.readthedocs.io/en/latest/tutorials/rf.html>

---

### Post #3 — **nyuton** | 2021-09-09 15:29 UTC _(reply to #2)_

You can install it with Conda:

[RAPIDS Docs](<https://docs.rapids.ai/install/>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/3748e19c37cb9f611dfd8e3d3f20180daaee0259_2_690x345.png)

### [Installation Guide - RAPIDS Docs](<https://docs.rapids.ai/install/>)

Guide to installing RAPIDS

Also works fine on Windows with WSL

---

### Post #4 — **yxbot** | 2021-09-09 15:30 UTC _(reply to #3)_

nice, will check - thanks

---

### Post #5 — **nyuton** | 2021-09-09 15:30 UTC

By the way rapids.ai can do a lot more algorithms on GPU.

---

### Post #6 — **yxbot** | 2021-09-09 15:31 UTC _(reply to #5)_

yeah, I know, lots of their DS team are kaggler friends - they have been reworking the whole sklearn suits
