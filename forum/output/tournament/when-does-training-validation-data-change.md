---
title: "When does training/validation data change?"
category: Tournament
url: https://forum.numer.ai/t/when-does-training-validation-data-change/2351
created_at: 2021-03-13T23:53:56.459000+00:00
last_posted_at: 2021-03-13T23:56:43.950000+00:00
posts_count: 2
views: 865
tags: []
---

# When does training/validation data change?

---

### Post #1 — **quantized** | 2021-03-13 23:53 UTC

When, if ever, does training and validation data change? I had assumed it changes week on week, but after setting up my model workflow for the first time this round, and seeing that my diagnostics are identical to last round, I came on to the forum and found posts mentioning that it doesn’t change.

Presumably, if it does change, we are alerted, in order that we can re-train?

Thanks.

---

### Post #2 — **wigglemuse** | 2021-03-13 23:56 UTC

It doesn’t change very often. Validation data is _updated_ once in a while, training data stays the same. Right now they are working on a 10x feature explosion – that will be the next big change presumably (which will be backward compatible), and yes they’ll be plenty of announcements and discussions about that.
