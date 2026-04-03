---
title: "Relation of Eras with time periods"
category: Tournament
url: https://forum.numer.ai/t/relation-of-eras-with-time-periods/371
created_at: 2020-05-10T11:53:19.656000+00:00
last_posted_at: 2020-05-10T13:36:06.033000+00:00
posts_count: 2
views: 1680
tags: []
---

# Relation of Eras with time periods

---

### Post #1 — **correlator** | 2020-05-10 11:53 UTC

I would like to clarify a doubt, which might seem basic but for a beginner like me it is something I have difficulty understanding.  
Are eras sequential in time moving forward? If not what is the significance of era numbers?  
For example, can we say that era1 in training corresponds to sometime in say 2008 and era 120 corresponds to say 2018.  
From what I understand, training and validation eras are monthly whereas test and live eras are weekly. Is there a relation between weekly era numbers and monthly era numbers?

---

### Post #2 — **quantnosticator** | 2020-05-10 13:36 UTC

Yes, eras are time periods of one month, and they are sequential. At least in the training set they are sequential, I’d have to double-check if the new validation2 set in the middle of the test set is maintaining that – I suspect so or it wouldn’t be in the middle. The eras are all monthly (in the sense that the targets all resolve after 4 weeks) but the test set (and live data) is overlapping weekly.

The era numbers don’t refer to anything specific that we are given knowledge of as users ,and I don’t think it is absolutely guaranteed that there are no gaps in time in the training and valset1 (eras 1-132), but there probably aren’t. Anyway, you can only make rough guesses as to how it lines up with reality. I bet we could figure it out actually as there are some definite eras that you can figure being as big events or crashes – nobody has lined up the eras with a timeline and made a convincing public case of it, but that doesn’t mean it couldn’t be done.
