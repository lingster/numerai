---
title: "On what data do I need to send my predictions ('validation', 'test', 'live')?"
category: Tournament
url: https://forum.numer.ai/t/on-what-data-do-i-need-to-send-my-predictions-validation-test-live/1964
created_at: 2021-02-22T21:33:37.655000+00:00
last_posted_at: 2025-10-03T21:14:07.672000+00:00
posts_count: 13
views: 1876
tags: []
---

# On what data do I need to send my predictions ('validation', 'test', 'live')?

---

### Post #1 — **wtd** | 2021-02-22 21:33 UTC

The tournament data has 3 different types: ‘validation’, ‘test’, ‘live’

When submitting my predictions to a tournament, do I need to use all 3, or can I just send it in one of them (to reduce file size)?

---

### Post #2 — **lliwmc** | 2021-02-22 21:48 UTC

Your predictions should be based on the live data not training data or validation data

I think thats is what you mean I’m not sure I quite understand the question fully now looking back on it

Will

---

### Post #3 — **wtd** | 2021-02-22 21:52 UTC _(reply to #2)_

Thank you. What I mean is that the `data_type` field in the tournament.csv file, has 3 types: ‘validation’, ‘test’, ‘live’.

When I want to submit my predictions I run my model on the tournament data and get the predictions, write a CSV file with it and send it to numerai. Do I need to do it to all the 3 types?

---

### Post #4 — **wigglemuse** | 2021-02-22 22:14 UTC _(reply to #3)_

All of them. You are sending them a submission file with the same number of rows (and with the same row ids) that are in the “tournament” data file. Look at the “example_predictions.csv” file. Just like that, except with your predictions instead.

---

### Post #5 — **lliwmc** | 2021-02-22 22:30 UTC _(reply to #4)_

This

Sorry completely misread, going back to reading rather than posting!! Been a long monday its 10.27pm in uk and thats clearly past my bed time…

---

### Post #6 — **asteeber** | 2021-02-25 20:03 UTC

I believe you can submit a file with only the “live” data_type tag and still earn payouts from what you stake (not 100% certain on this). But the trade off is that you can’t see predicted performance before Thursday when results for the round are posted. I think NumerAI uses the test/validation data to gauge how well your model might do.

---

### Post #7 — **themicon** | 2021-02-25 20:11 UTC _(reply to #6)_

For Numerai signals you can submit only the live data_type, for the classic tournament you need to upload your predictions for the entire tournament file, which contains live, validation and test.

---

### Post #8 — **seunghoans** | 2021-02-28 01:43 UTC _(reply to #6)_

> I think NumerAI uses the test/validation data to gauge how well your model might do.

Does this mean that if I set all of the ‘test’ and ‘validation’ predictions as ‘0’ and only predict live data, I get lower score? And I am also curious if I’d better predict validation data or just copy the given target values.

---

### Post #9 — **wigglemuse** | 2021-02-28 02:00 UTC _(reply to #8)_

You can do whatever you want with the validation data (you won’t get validation diagnostics that mean anything though, of course). If you are just going to play games with it, you might as well use it as additional training data. But if you don’t predict the test data, you are just being a jerk (although it is true you get no feedback from it). Well, at least if you are staking, as they rely on that info at least some of the time. (And if a lot of people made a habit of that, they’d be forced to make the checks on submissions more draconian. And we don’t want that. Been there, done that.)

---

### Post #10 — **asteeber** | 2021-02-28 02:26 UTC _(reply to #8)_

No, I believe NumerAI payouts depend only on the live data predictions. If you want to use NumerAI’s built-in model predicted performance measures then you should predict the validation and test data

---

### Post #11 — **wigglemuse** | 2022-09-23 12:57 UTC

Somebody liked one of my previous posts on this thread today, so I’d just like to point out that this information is outdated, and you no longer need to submit anything but the live era each week. (No more “test”)

---

### Post #12 — **ryo_matsuzaka** | 2022-09-23 13:09 UTC _(reply to #11)_

> Somebody …

Thanks. That’s me.

---

### Post #15 — **zurkin** | 2025-10-03 21:14 UTC _(reply to #11)_

“…you no longer need to submit anything but the live era each week.”, could you please tell when can I see the scores for the daily predictions? could you provide links to demonstrate a submission and its scores?
