---
title: "Stock tickers in dataset?"
category: Tournament
url: https://forum.numer.ai/t/stock-tickers-in-dataset/6718
created_at: 2023-10-10T11:54:57.782000+00:00
last_posted_at: 2023-10-11T01:53:15.723000+00:00
posts_count: 4
views: 544
tags: []
---

# Stock tickers in dataset?

---

### Post #1 — **wowo86** | 2023-10-10 11:54 UTC

Hi, from what I see there’s no way to say which row corresponds with given stock (even anonymized). How then it’s possible to create good quality model without applying Time Series algos?

---

### Post #2 — **numerologist** | 2023-10-10 19:49 UTC

Welcome to the forum.

> How then it’s possible to create good quality model without applying Time Series algos?

There are sets of machine learning problems that don’t require time series modeling. You might want to check out the example model to see for yourself how it works: [example-scripts/example_model.ipynb at master · numerai/example-scripts · GitHub](<https://github.com/numerai/example-scripts/blob/master/example_model.ipynb>)

---

### Post #3 — **wowo86** | 2023-10-10 20:42 UTC

I’ve ran example model and even tried some neural nets attempts. But wouldn’t it be easier to treat it with time series algos, given the fact that this is a typical use case for those?

---

### Post #4 — **numerologist** | 2023-10-11 01:53 UTC

It might, but we’ll never know. ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) Because this is part of the data obfuscation process, the only way they could release it to us for free.
