---
title: "Does the daily data require new models?"
category: Tournament
url: https://forum.numer.ai/t/does-the-daily-data-require-new-models/5789
created_at: 2022-10-25T17:21:00.592000+00:00
last_posted_at: 2023-03-01T16:41:21.514000+00:00
posts_count: 3
views: 926
tags: []
---

# Does the daily data require new models?

---

### Post #1 — **lowvolmeanreversion** | 2022-10-25 17:21 UTC

I didn’t hear anything about new data, so I’m going to assume that any old models are compatible with daily submissions. Basically, everything is exactly the same as before, but we now have additional rounds Tuesday - Friday. Wanted to confirm my understanding before staking anything on the new rounds.

---

### Post #2 — **shatteredx** | 2022-10-25 18:13 UTC

No difference in models. Daily live data has the same features.

Only thing that broke on my pipeline was downloading v2 numerai_tournament_data.csv which is not updated for daily rounds.

Need to use api live data v2 instead:  
`napi.download_dataset('v2/numerai_live_data.csv', f"live_{current_round}_v2.csv")`

---

### Post #3 — **jnolan9** | 2023-03-01 16:41 UTC _(reply to #2)_

If anyone has issues with that line of code, I was able to get it to work this way:

napi.download_dataset(‘v2/numerai_live_data.csv’, f"live_{‘current-round’}_v2.csv")
