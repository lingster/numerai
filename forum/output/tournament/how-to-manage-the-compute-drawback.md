---
title: "How to manage the compute drawback"
category: Tournament
url: https://forum.numer.ai/t/how-to-manage-the-compute-drawback/4167
created_at: 2021-09-20T13:07:49.098000+00:00
last_posted_at: 2021-12-21T14:30:05.247000+00:00
posts_count: 8
views: 1026
tags: []
---

# How to manage the compute drawback

---

### Post #1 — **hemanthh17** | 2021-09-20 13:07 UTC

I wanted to use google colab but it is overwhelmed with the processing and is crashing as I use the free version. I cannot afford pro or a GPU/TPU.  
Are there any alternate resources?

---

### Post #2 — **autratec** | 2021-09-21 03:11 UTC

I am still using google colab. the best way is reducing the computing needs, like change data type from double to int.

---

### Post #3 — **degerhan** | 2021-09-21 13:52 UTC

You can have a 25GB RAM and 4-core instance with colab-free starting with this notebook: [colab-4core-25GB.ipynb (github.com)](<https://gist.github.com/degerhan/e442221577c75e15d529b5c896f06d19>)

All it really does is set the “machine_shape”: “hm” metadata field in the notebook. Hat tip to either jrb or jordi, I think I copied it from a notebook shared by them at one time.

---

### Post #4 — **hemanthh17** | 2021-09-21 14:20 UTC _(reply to #3)_

What exactly am I supposed to do I get the same output kinda but do not understand what’s the purpose and effect.

---

### Post #5 — **hemanthh17** | 2021-09-21 14:20 UTC _(reply to #2)_

Sorry buddy didn’t work

---

### Post #6 — **degerhan** | 2021-09-21 14:25 UTC _(reply to #4)_

You get a 25GB colab instance when you open that notebook Double the memory of regular colab, check the available RAM in the resources bar. This seems sufficient to at least get started with the new int8_data.

---

### Post #7 — **hemanthh17** | 2021-09-21 14:54 UTC _(reply to #6)_

Hey buddy,  
Gotcha!! Thanks a lot for sharing!!

---

### Post #8 — **nitish** | 2021-12-21 14:30 UTC

This works like a charm! Thanks [@degerhan](</u/degerhan>)
