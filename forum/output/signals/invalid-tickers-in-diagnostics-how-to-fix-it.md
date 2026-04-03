---
title: "Invalid Tickers in Diagnostics: How to fix it?"
category: Signals
url: https://forum.numer.ai/t/invalid-tickers-in-diagnostics-how-to-fix-it/3650
created_at: 2021-06-24T14:47:17.441000+00:00
last_posted_at: 2021-06-24T19:36:05.920000+00:00
posts_count: 5
views: 1058
tags: []
---

# Invalid Tickers in Diagnostics: How to fix it?

---

### Post #1 — **aqsmith08** | 2021-06-24 14:47 UTC

When I have a new signal, I typically submit it over as many weeks as possible to see how it looks across a long time period in the Numerai Signals diagnostics. I’ve noticed that the “Invalid Tickers” seems to be pretty high and I cannot figure out why that might be.

Here’s an example:  


[![Screenshot from 2021-06-24 08-43-16](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/de22cdcba480c24d89cfac6edc8cea12ca89ff4f.png)Screenshot from 2021-06-24 08-43-16310×241 7.77 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/de22cdcba480c24d89cfac6edc8cea12ca89ff4f.png> "Screenshot from 2021-06-24 08-43-16")

My one thought is that the Numerai ticker universe changes over time, and some tickers may not have existed in the past. Any ideas on how to eliminate “Invalid Tickers” and does this impact my diagnostic scores at all? Thanks.

---

### Post #2 — **mugamma** | 2021-06-24 15:06 UTC

What header are you using? I found that switching from `ticker` to `numerai_ticker` did wonders for my match rate.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/c57346/48.png) [Tips on mismatched ticker names?](<http://forum.numer.ai/t/tips-on-mismatched-ticker-names/3555/2>) [Signals](</c/signals/10>)

> Turns out my issue was in the header. I had ticker instead of numerai_ticker like the example code. Changing to numerai_ticker gave me 100% live tickers matched. The documentation on this should be clarified. It currently says the following which does not mention a numerai_ticker option nor explain whatever the semantic difference is. A cusip, sedol, or ticker column - values must be valid tickers associated with the ticker type in the header. [https://docs.numer.ai/numerai-signals/signals-o…](<https://docs.numer.ai/numerai-signals/signals-overview#submissions>)

---

### Post #3 — **aqsmith08** | 2021-06-24 15:16 UTC _(reply to #2)_

Oh interesting! I’m currently using `bloomberg_ticker` for the column header. I’ll re-name that column and submit to see if that improves it. Thank you! (And I’ll update this thread if it does.)

---

### Post #4 — **aqsmith08** | 2021-06-24 16:35 UTC _(reply to #3)_

Update: It didn’t seem to fix anything. I’m going to investigate the tickers that I’m using in my submission dataframe and compare it to the tickers in the Numerai [universe file](<https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/universe/latest.csv>) and check for discrepancies.

---

### Post #5 — **aqsmith08** | 2021-06-24 19:36 UTC _(reply to #4)_

Update: The tickers used in my submission dataframe seem to match the tickers in the Numerai universe file (linked in the comment above). I still can’t figure out why I’m receiving so many “Invalid Tickers” in the diagnostics.

Would love help if someone has an idea. Thanks.
