---
title: "Suggestion of add in equity id in Tournament"
category: Tournament
url: https://forum.numer.ai/t/suggestion-of-add-in-equity-id-in-tournament/3589
created_at: 2021-06-12T11:52:19.092000+00:00
last_posted_at: 2021-06-12T23:35:25.612000+00:00
posts_count: 5
views: 611
tags: []
---

# Suggestion of add in equity id in Tournament

---

### Post #1 — **autratec** | 2021-06-12 11:52 UTC

Hi Numerai admin, as a newbie after check your data, i feel it is necessary to add in equity id in the data file for better pattern recognition and prediction.

The current method of data and result is more like using a picture to look the word. it is one dimension. just like find the path in the forest on the ground. but , if equity id can be provided, we can connect same feature with different era data and link back to target equity. So we start to view the world in 2D. it is more easy to find the path in the plane, rather than on the ground.

please consider to include that data element in the data set. i have done a similar prediction experiment before, and it is pretty sure that the result will be dramatically improved, when we moving towards to 2d to look the world.

---

### Post #2 — **ml_is_lyf** | 2021-06-12 12:19 UTC

Hey, if I understand rightly, your suggesting that say MSFT should have the same unique identifier in every era? If that is what you mean, unfortunately, I don’t think they’d ever do that. The reason why the data we are given is anonymized and obfuscated is because this data is really expensive. They buy it from data vendors who make their money by collecting data and selling it. If the Numerai team allowed us to identify equities across eras, it’d make it a lot easier to figure out what the features are, and even if the equities had an anonymous id, you could start to figure out which id corresponds to which stock. The data vendors don’t want their data in the public domain, as then no one would buy it from them, so its important its kept anonymous so that the Numerai dataset can only be understood by the Numerai team.

---

### Post #3 — **autratec** | 2021-06-12 12:36 UTC

I hope anonymous id per equity will be provided, which will help increase the prediction success ratio. Using 2D data: feature + time will be more easy to build working model.

---

### Post #4 — **chaotician** | 2021-06-12 18:08 UTC

Yes, I agree. By placing an equity(asset) id, quants will be able to do real time series analysis which IMO better represents the prediction problem at hand. The way the data is currently presented, it favors Bayesian vs. Frequentist approach. Frequentist approach is used in most AI/ML algos. and offers better pattern recognition capabilities as now we have two dimensions ,time and space (magnitude).

---

### Post #5 — **mic** | 2021-06-12 23:35 UTC

Signals is the tournament you want.

<https://signals.numer.ai/tournament>
