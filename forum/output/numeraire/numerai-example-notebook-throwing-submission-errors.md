---
title: "Numerai Example Notebook Throwing Submission Errors"
category: Numeraire
url: https://forum.numer.ai/t/numerai-example-notebook-throwing-submission-errors/5572
created_at: 2022-07-16T19:03:51.591000+00:00
last_posted_at: 2022-07-17T00:14:20.380000+00:00
posts_count: 2
views: 693
tags: []
---

# Numerai Example Notebook Throwing Submission Errors

---

### Post #1 — **13wayblackbird** | 2022-07-16 19:03 UTC

I’m trying to complete my first submission, before trying other ways of modeling using the Numerai example notebook in Google Colab at <https://numer.ai/notebook>.

However, each time I try to submit, I get the following error:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/7b72809954c3efd5109207ee0fa272f6e4645bc8_2_690x313.png)image1406×638 69.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7b72809954c3efd5109207ee0fa272f6e4645bc8.png> "image")

I haven’t changed the default code except for inserting my own keys and ID for the submission. What else do I need to change?

Thanks!  
Brandon

---

### Post #2 — **shatteredx** | 2022-07-17 00:14 UTC

My initial guess would be you ran your code right before the round change today so it submitted last week’s live data. Live data changes every Saturday at 18:00 UTC.

Try deleting the runtime and running it again so that it downloads this rounds live data.
