---
title: "How often is the training and validation data updated?"
category: Tournament
url: https://forum.numer.ai/t/how-often-is-the-training-and-validation-data-updated/2081
created_at: 2021-02-28T19:58:40.131000+00:00
last_posted_at: 2021-03-01T14:39:59.382000+00:00
posts_count: 4
views: 1318
tags: []
---

# How often is the training and validation data updated?

---

### Post #1 — **v_newbie** | 2021-02-28 19:58 UTC

Hi guys, I’ve just joined Numerai couple of days ago and I found that the training and validation data of round 252 and 253 are the same. Does anyone know how often the training and validation data are updated please?

---

### Post #2 — **wigglemuse** | 2021-02-28 20:40 UTC

The training data never updates. That’s it. However, we do get a handful of new validation eras once in a while (once or twice a year maybe). They said they were gonna add some every six months, but it doesn’t look like they are actually gonna hold to that. There is a feature expansion in the pipeline though – i.e. not more training rows, but more features per row. A whole lot more (10x what we have now). There will be a big announcement about that when the time comes…

---

### Post #3 — **v_newbie** | 2021-03-01 08:54 UTC _(reply to #2)_

Thanks a lot! I’ve thought the data is constantly updated and worried that we need to re-train the model once a while…wondering how can the data keep the information up to date if it’s never updated…looking forward to the big announcement!

---

### Post #4 — **wigglemuse** | 2021-03-01 14:39 UTC

The training data represents 10 years, but the newest of it is at least a several years old. (There is also another 2 1/2 years worth of validation data, some of which is pretty recent.) The idea is to make a general model that works well…forever, I guess, and not just fit (overfit) to the most recent time periods. Whether or not that is a wise setup is open to debate, but that’s the way it is.
