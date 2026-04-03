---
title: "Distance analysis using Facebook AI Similarity Search (faiss)"
category: Data Science
url: https://forum.numer.ai/t/distance-analysis-using-facebook-ai-similarity-search-faiss/4205
created_at: 2021-09-26T11:26:43.692000+00:00
last_posted_at: 2021-09-28T06:27:17.764000+00:00
posts_count: 3
views: 871
tags: []
---

# Distance analysis using Facebook AI Similarity Search (faiss)

---

### Post #1 — **jmnum** | 2021-09-26 11:26 UTC

I was looking for close data points between training, validation and live data. It didn’t work ![:frowning:](http://forum.numer.ai/images/emoji/twitter/frowning.png?v=9) but I’m a bit surprised that the validation data isn’t closer to the training data.

It may not be of any help, but here is a colab notebook: [Colab : Distance analysis](<https://colab.research.google.com/drive/1kpkLKq463ZgnC5_oFGkUouSyqDBd14pZ?usp=sharing>)

---

### Post #2 — **eleven_sigma** | 2021-09-27 19:51 UTC

Should be interesting to do an intra-era analysis and see if there are eras with more similar points and others without them.  
Perhaps live era you selected belongs to a group of eras with high distance between points.

---

### Post #3 — **gbrecht** | 2021-09-28 06:27 UTC

If I read the notebook correctly, you compared the whole training data to the whole validation data.  
Would it not be more interesting to compare each era of the validation set to all eras of the training set (per era)?  
If by that way you could determine the training era that is closest to the validation (or later live) era, you could time which train-era-model to use on the live data
