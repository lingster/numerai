---
title: "Why this error occurring even though I am using id's from example prediction file"
category: Tournament
url: https://forum.numer.ai/t/why-this-error-occurring-even-though-i-am-using-ids-from-example-prediction-file/733
created_at: 2020-07-29T10:52:05.550000+00:00
last_posted_at: 2020-08-31T17:38:18.268000+00:00
posts_count: 6
views: 1960
tags: []
---

# Why this error occurring even though I am using id's from example prediction file

---

### Post #1 — **falsemodel** | 2020-07-29 10:52 UTC

{“ok”: false, “code”: “invalid_submission_ids”, “message”: “ids must match ids in tournament data exactly, including ordering”}

---

### Post #2 — **wigglemuse** | 2020-07-30 23:06 UTC

Including the top header? Are you just trying to submit the examples or you’ve replaced the predictions or what?

---

### Post #3 — **falsemodel** | 2020-08-02 15:16 UTC

Top header was just fine. I just replaced the prediction numbers with new one. Anyway this seems to be a bug , Just submitted new prediction this week with same script and it just worked fine.

---

### Post #4 — **jeremy_berros** | 2020-08-30 21:04 UTC

Same issue here with my submission today using ids from numerai_tournament_data.csv. Tried both the API and manual Upload. Still same outcome.

---

### Post #5 — **krizmanic** | 2020-08-31 14:08 UTC

I’ve only had that happen 2 ways that I can remember.

  1. Submitting predictions on an old tournament_data.csv file
  2. Shuffling the output data relative to the input data, in the past at least, order seemed to matter.



The easiest double-check is to take the example predictions (from the correct week, of course) and look for any structural differences between your output file and that file.

---

### Post #6 — **jeremy_berros** | 2020-08-31 17:38 UTC _(reply to #5)_

Thanks for the response. I figured it out. I forgot to add validation data before submitting. Thanks again
