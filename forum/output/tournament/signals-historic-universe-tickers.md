---
title: "Signals - Historic universe tickers"
category: Tournament
url: https://forum.numer.ai/t/signals-historic-universe-tickers/3280
created_at: 2021-05-13T02:57:58.491000+00:00
last_posted_at: 2021-05-14T02:07:39.523000+00:00
posts_count: 4
views: 728
tags: []
---

# Signals - Historic universe tickers

---

### Post #1 — **sirbradflies** | 2021-05-13 02:57 UTC

Hi,

Is it possible to get the historic version of the Signals ticker mapping (e.g. 2010, 2011, …) to avoid survivorship bias? I am just realizing how wrong is to use the current ticker map to train the model…

I could not find this topic referred else and it would be very helpful to have the past mappings or maybe a free source where we can find the top 5000 global public companies by market capitalization by year.

Thanks!

---

### Post #2 — **richai** | 2021-05-13 06:01 UTC

Have you tried downloading the example files (near upload button)? In the folder, there is a file called example_signal_upload.csv. This file contains tickers for the whole validation data since 2013/01/04 - all these historical tickers wouldn’t have survivorship bias; these were all the things in our universe at those times. Is this what you need?

---

### Post #3 — **sirbradflies** | 2021-05-14 01:52 UTC _(reply to #2)_

Hi Richard,  
I missed that file, thanks!

I did a quick check of the file and I did not see in the past years some companies that got delisted afterwards (e.g. Blockbuster BBI). Am I missing something? I would have expected to see them in the historic universe.

Thanks again

---

### Post #4 — **sirbradflies** | 2021-05-14 02:07 UTC _(reply to #3)_

Nevermind, I did a sanity check with Lehman Brothers (LEH US) and it stops on September 2008 as expected. This is exactly what I was looking for.
