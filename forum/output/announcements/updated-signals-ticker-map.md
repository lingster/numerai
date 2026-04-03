---
title: "Updated Signals Ticker Map"
category: Announcements
url: https://forum.numer.ai/t/updated-signals-ticker-map/2239
created_at: 2021-03-08T16:19:23.057000+00:00
last_posted_at: 2024-07-29T23:03:25.147000+00:00
posts_count: 4
views: 2131
tags: []
---

# Updated Signals Ticker Map

---

### Post #1 — **_liamhz** | 2021-03-08 16:19 UTC

The Signals ticker map has been updated! Many Yahoo tickers were corrected, and the tickers listed now matches the current Signals universe.

Grab the file here: <https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/signals_ticker_map_w_bbg.csv>

This ticker map will be updated every week at round open to have all of the tickers in the latest Signals universe.

Note: There are 51 tickers in the file which haven’t been mapped to Yahoo tickers, and have NaNs in their column. We’ll have a fix out for this soon.

---

### Post #2 — **sirbradflies** | 2023-04-18 15:58 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/_liamhz/48/1368_2.png) _liamhz:

> updated every week at round open to have all of the tickers in the l

Hi, is this mapping still updated on a weekly basis? I am asking because I see some mappings that don’t work (e.g. ticker “META” → yahoo “FB”).  
Thanks

---

### Post #3 — **joakim** | 2024-07-28 23:03 UTC _(reply to #2)_

Hi [@ark](</u/ark>) and [@master_key](</u/master_key>) is this Signals ticker map file still maintained and updated weekly? Cheers.

---

### Post #4 — **ark** | 2024-07-29 23:03 UTC _(reply to #3)_

Although it’s still listed in the dataset API, the file is technically deprecated and may be removed in the future. I would try to avoid using it if possible.
