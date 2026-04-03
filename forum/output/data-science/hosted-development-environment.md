---
title: "Hosted Development Environment"
category: Data Science
url: https://forum.numer.ai/t/hosted-development-environment/2407
created_at: 2021-03-17T02:41:11.205000+00:00
last_posted_at: 2021-03-20T00:49:28.384000+00:00
posts_count: 7
views: 925
tags: []
---

# Hosted Development Environment

---

### Post #1 — **evanhennis** | 2021-03-17 02:41 UTC

Is anyone using a hosted environment (Colab, etc.) for their models? I am using the default Colab with 12GB of memory and it is a pain.

---

### Post #2 — **krm** | 2021-03-17 14:00 UTC

try out Kaggle notebooks

---

### Post #3 — **evanhennis** | 2021-03-17 20:01 UTC

I will check that out. I think it has the same memory footprint as Google Colab.

---

### Post #4 — **surajp** | 2021-03-17 20:28 UTC

Colab works great! We just need to optimize the code (this does take a lot of time).

My primary problem was limited amount of memory but I managed to get everything done under 3.0 GB.

---

### Post #5 — **evanhennis** | 2021-03-18 01:19 UTC

I can get everything loaded from the files to my processed data frames. But, after that I can’t release the memory. I have to restart the session and then load the data frames with int16 columns and I am good the rest of the way

---

### Post #6 — **krm** | 2021-03-19 12:55 UTC

<https://colab.research.google.com/drive/1D6krVG0PPJR2Je9g5eN_2h6JP73_NUXz> This is the notebook that [@surajp](</u/surajp>) linked in rocket chat. Should give you a P100 and more RAM/Storage

---

### Post #7 — **ml_is_lyf** | 2021-03-20 00:49 UTC _(reply to #6)_

Wow, this is really cool. Did some digging in the raw notebook, and it looks like adding
    
    
    "machine_shape": "hm"
    

does the magic. Sure enough, found a tutorial on how you can do it with your own notebooks. Handy if you’ve already got some existing notebooks you want to add this feature to.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0f95de5840ff0771b84ea77cfa42a1e98b4f1614.png) [Medium – 16 May 20](<https://satyajitghana.medium.com/how-to-upgrade-to-25gb-ram-in-google-colab-possibly-w-tesla-p100-gpu-for-free-115e7679f5de> "11:26AM - 16 May 2020")

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6d09d9bd7608a076751a02a7d1f011a842663c60.png)

### [How to upgrade to 25GB RAM in Google Colab possibly w/ Tesla P100 GPU for Free](<https://satyajitghana.medium.com/how-to-upgrade-to-25gb-ram-in-google-colab-possibly-w-tesla-p100-gpu-for-free-115e7679f5de>)

I’ll keep this simple and sweet

Reading time: 2 min read
