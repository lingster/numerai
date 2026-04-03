---
title: "Diagnostic Tool"
category: Tournament
url: https://forum.numer.ai/t/diagnostic-tool/6261
created_at: 2023-04-01T04:22:04.519000+00:00
last_posted_at: 2023-04-08T11:07:43.350000+00:00
posts_count: 3
views: 801
tags: []
---

# Diagnostic Tool

---

### Post #1 — **silvark** | 2023-04-01 04:22 UTC

I am having trouble using the diagnostic tool. I have tried running it on two decently size portions of the validation dataset, with 100k and 300k rows.

On the 100k rows, I got the error:

Your upload seems to be invalid:

high_invalid_ticker_count: Looks like your upload had 0.12311111640032944% of the correct IDs.Make sure you’re predicting on the newest Validation data for round 449.

on the 300k rows, I got the error:

Your upload seems to be invalid:

high_invalid_ticker_count: Looks like your upload had 0.10259259700027454% of the correct IDs.Make sure you’re predicting on the newest Validation data for round 449.

These percentages don’t make sense to me at all, since the percentage went down when I used a larger chunk of the validation data. It seems like I should be expecting something more in the 1-10% range.

Also, It would be nice if you didn’t have to run the diagnostic on the entire validation set, right? With 32 gigs of memory it would still require predicting in chunks and then combining the results.

Alternatively, when I try to use the diagnostic tool with the example predictions, I get the message stating that the visualization is being prepared and that It will just be a minute, but it never actually loads.

Is it worth my time to predict on the entirety of the validation data and then try to run diagnostics on that?

Does anyone have a workflow where they make use of the diagnostic tool in any way?

---

### Post #2 — **ark** | 2023-04-03 18:01 UTC

Hi, this error is actually a bit misleading and you’re right that the percentage should be 10x higher. It does make sense that submitting more tickers would lead to a lower invalid ticker rate if your additional predictions were mostly valid. I would recommend taking a closer look at the example preds we give out to ensure your predictions match up correctly.

---

### Post #3 — **silvark** | 2023-04-08 11:07 UTC

Thanks for the reply! I got it working when using the complete dataset. Thanks for the help!
