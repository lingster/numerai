---
title: "Creating features from currency-exposed metrics"
category: Signals
url: https://forum.numer.ai/t/creating-features-from-currency-exposed-metrics/6257
created_at: 2023-03-30T23:03:24.848000+00:00
last_posted_at: 2023-04-10T18:19:24.591000+00:00
posts_count: 2
views: 713
tags: []
---

# Creating features from currency-exposed metrics

---

### Post #1 — **quantverse** | 2023-03-30 23:03 UTC

Dear quants!

What is your preferred way to deal with currency related metrics, like market capitalization (size factor) when creating features?  
The problem is that you end up with stocks from multiple exchanges / currencies mixed in the era, so for instance mixing USD and JPY stocks will mess with ranking / bucketing for these features carrying the currency exposure.

What is your preferred way to deal with this?

I can see two options:

  * (pre)ranking per currency / exchange
  * normalizing (calculate everything in USD using forex rates)



What do you think?

---

### Post #2 — **lcrmorin** | 2023-04-10 18:19 UTC

Using forex rate as a factor and transforming everything into log_returns seems the best way to go in the context of ML.
