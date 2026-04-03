---
title: "New Data Source: IEX Cloud (free-ish)"
category: Signals
url: https://forum.numer.ai/t/new-data-source-iex-cloud-free-ish/3038
created_at: 2021-04-23T21:21:44.852000+00:00
last_posted_at: 2021-04-29T15:38:07.451000+00:00
posts_count: 2
views: 1680
tags: []
---

# New Data Source: IEX Cloud (free-ish)

---

### Post #1 — **jorijnsmit** | 2021-04-23 21:21 UTC

Decided to give Signals a try and follow the current De-Fi hype… APY APY APY. So the idea is very simple: what is the annual percentage yield for a stock, based on its price and dividends?

I found a nice endpoint on IEX Cloud’s API: <https://iexcloud.io/docs/api/#dividends-basic>. The fields `amount` and `frequency`, combined with the daily price, being all we need.

IEX Cloud is free-ish, meaning there is a free account but it’s limited in endpoints and calls per month. However, they also provide a sandbox mode which you can call as much as you want. Some data in sandbox mode is obfuscated but not all. Also, a subscription for $9/month (~0.15NMR?!) is not the end of the world.

Anyway there’s two Python wrappers for the API: <https://github.com/addisonlynch/iexfinance> and <https://github.com/iexcloud/pyEX>.

I was able to create a proof of concept for this APY signal and decided to open source it as an example script. Liam was actually so crazy to accept it into the official repo! <https://github.com/numerai/example-scripts/tree/master/signals/iexcloud>

Curious to hear if other Numeratis have experience with IEX Cloud. I am also very open to comments and feedback on the signal itself, so far the results for this rough version are not bad: <https://signals.numer.ai/gosuto_test>

[![Screenshot 2021-04-23 at 23.24.35](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/795a9d06cf177448114f8eb10ce8ca1768570dd6_2_214x500.png)Screenshot 2021-04-23 at 23.24.35480×1118 45.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/795a9d06cf177448114f8eb10ce8ca1768570dd6.png> "Screenshot 2021-04-23 at 23.24.35")

---

### Post #2 — **one5hot76** | 2021-04-29 15:38 UTC

I was digging into yahoo finance this week and I believe they have all the data you speak of. They are also free. They have a python library, which I like. Thanks for sharing.
