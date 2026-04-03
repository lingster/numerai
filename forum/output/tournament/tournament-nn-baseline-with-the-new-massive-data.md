---
title: "Tournament NN baseline with the new massive data"
category: Tournament
url: https://forum.numer.ai/t/tournament-nn-baseline-with-the-new-massive-data/4305
created_at: 2021-10-10T12:04:05.453000+00:00
last_posted_at: 2021-10-19T16:52:08.938000+00:00
posts_count: 4
views: 1416
tags: []
---

# Tournament NN baseline with the new massive data

---

### Post #1 — **katsu1110** | 2021-10-10 12:04 UTC

Hi, I published an end-to-end (from data loading to submission) kaggle notebook for the Numerai Tournament. Although a kaggle notebook has only ca. 16GB RAM, a bit of tricks make it possible to use the massive data in it.

This notebook uses a multi-layer perceptron with multi-outputs to take advantage of multiple targets of the new data.

[[Numerai] NN baseline with new massive data](<https://www.kaggle.com/code1110/numerai-nn-baseline-with-new-massive-data>)

Hopefully this notebook helps those who have troubles with dealing with the massive data. Have fun!

---

### Post #2 — **autratec** | 2021-10-18 11:25 UTC

Katsu1110 san, thanks for sharing the source code again. Btw if feel using xgb will be more reliable than NN.

---

### Post #3 — **katsu1110** | 2021-10-18 14:24 UTC _(reply to #2)_

Thanks for your feedback. It is nice for Numerai to have different model predictions, so go for your idea!

---

### Post #4 — **rdr91h** | 2021-10-19 16:52 UTC _(reply to #3)_

The two top numerai signals models are based in NN
