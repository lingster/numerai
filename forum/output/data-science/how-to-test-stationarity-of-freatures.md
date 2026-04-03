---
title: "How to test stationarity of Freatures?"
category: Data Science
url: https://forum.numer.ai/t/how-to-test-stationarity-of-freatures/1213
created_at: 2020-11-22T05:11:40.107000+00:00
last_posted_at: 2020-11-22T12:39:41.252000+00:00
posts_count: 2
views: 1115
tags: []
---

# How to test stationarity of Freatures?

---

### Post #1 — **6inchroastbeef** | 2020-11-22 05:11 UTC

Hello guys this is my first time using Nuemrai. I wonder how to test the stationarity of Features since there are only 5 values [0,0.25,0.5,0.75,1] for each features. I am not sure if the traditional way like ADF test works here. Thank you for your idea in advance!

---

### Post #2 — **voidcentury** | 2020-11-22 12:39 UTC

One direction could be looking at changes per era in correlations of a feature with other features and the target.
