---
title: "Open round info using API"
category: Signals
url: https://forum.numer.ai/t/open-round-info-using-api/6432
created_at: 2023-06-06T12:48:28.409000+00:00
last_posted_at: 2023-08-26T20:47:46.285000+00:00
posts_count: 2
views: 709
tags: []
---

# Open round info using API

---

### Post #1 — **fasec** | 2023-06-06 12:48 UTC

I was wondering if it’s possible to get open round info for Signals tournament using the API? There is a function called '`check_round_open` in the base APi but it’s not possible to choose which tournament status it should return. I assume it only returns the round info for the base tournament. Maybe I could try to use the `check_new_round` function because it’s possibe to define the tournament id with that. Haven’t tried that yet.

It would be necessary to get the open round info from the API because the tournament sometimes opens at different times.

Here’s a link to the API docs if anyone is interested: <https://numerapi.readthedocs.io/en/latest/api/numerapi.html#module-numerapi.numerapi>

---

### Post #2 — **uuazed** | 2023-08-26 20:47 UTC

The trick is to use `api = numerapi.SignalsAPI()`. With that, the signals tournament ID is used automatically.
