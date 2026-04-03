---
title: "Re-training vs training online"
category: Data Science
url: https://forum.numer.ai/t/re-training-vs-training-online/1494
created_at: 2021-01-19T15:55:49.371000+00:00
last_posted_at: 2021-01-19T18:06:30.478000+00:00
posts_count: 2
views: 1287
tags: []
---

# Re-training vs training online

---

### Post #1 — **goldnumberone** | 2021-01-19 15:55 UTC

I finally was able to get a basic machine learning model trained on the tournament data (using TensorFlow). I would like to know if I should train the model again when the next data set is released or if I should use the already trained model and use “online” training to feed it more data.

Should my model be discrete or continuous? Has anyone found better/worse performance from week to week from completely re-training?

---

### Post #2 — **wigglemuse** | 2021-01-19 18:06 UTC

The training and validation data doesn’t change week-to-week. (Once in a while new validation data is added – you’ll see an announcement in rocketchat when that happens.) So there is no reason to re-train all the time. The only new data each week is the “eraX,live” data which we are actually scored on for the round.
