---
title: "ValueError: Failed to complete validation of upload!"
category: Tournament
url: https://forum.numer.ai/t/valueerror-failed-to-complete-validation-of-upload/4466
created_at: 2021-11-06T19:07:10.125000+00:00
last_posted_at: 2021-11-06T21:28:43.865000+00:00
posts_count: 4
views: 894
tags: []
---

# ValueError: Failed to complete validation of upload!

---

### Post #1 — **mundan** | 2021-11-06 19:07 UTC

`ValueError: Failed to complete validation of upload!`

That’s the error I’m getting when trying to upload the example diagnostics as of nov 6.

`ValueError: AttributeError module 'aiobotocore' has no attribute 'AioSession'`

This error arises when trying to upload example predictions.

can anyone confirm? I’m using google colab

---

### Post #2 — **anthill** | 2021-11-06 19:22 UTC

I am seeing that error as well. I was able to manually upload the CSV of my prediction, though.

---

### Post #3 — **mundan** | 2021-11-06 19:29 UTC

Apparently fix is on the way ![:slight_smile:](//forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) (according to @ark in rocketchat)

---

### Post #4 — **objectscience** | 2021-11-06 21:28 UTC

I think they have this sorted now, give it another try when you have time.
