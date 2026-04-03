---
title: "Making sense of era number"
category: Tournament
url: https://forum.numer.ai/t/making-sense-of-era-number/1314
created_at: 2020-12-15T16:27:24.961000+00:00
last_posted_at: 2021-04-04T09:56:36.788000+00:00
posts_count: 4
views: 2395
tags: []
---

# Making sense of era number

---

### Post #1 — **loracle** | 2020-12-15 16:27 UTC

Has anyone tried to understand how the era number are assigned ?  
In the last tournament data, the validation eras go from 121 to 132 and each era are spaced by one month. For now, easy.  
Then we get to the test eras, which are numbered from 575 to 842, now those are spaced by a week, and assuming the test era 575 = 121 + 1w, 576 = 121 + 2w, 577 = 121 + 3w, I suppose that 578 is equivalent to era 133 in month.  
Knowing that, we can convert week number to month number by doing (wEra - 46) / 4, which for 578 gives us indeed 133.  
Now, we can convert the test era range to month era, and observe that it goes from 133 to (852 - 46) / 4 = 201 + 2w  
All good, we keep going forward in the dataset, and we now find a validation segment, spanning 197 to 212.  
**That is weird** , that would mean we have the era 197, 198, 199, 200 and 201 both in test and validation.  
What is happening here ?

We keep going, and now find a test segment, spanning 927 to 936, which to month era gives us 220 + 1w to 222 + 2w.  
**That is weird** , that would mean we have a hole from 213 to 219, where did those era go ?

Can anyone help me make sense of those two observations ? Their interpretation are important in how I validate my model.  
Thanks !

---

### Post #2 — **krizmanic** | 2020-12-16 15:36 UTC

We’re not meant to know what real time correlates to what era. It’s all part of the obfuscation of the real data. That said, some good theories have ping ponged around the forum and chat on the subject.

---

### Post #3 — **loracle** | 2020-12-16 15:47 UTC

I see ! It does seem like they are open about the fact that the eras follow each other in time, according to this post [Validation 2 Announcement](<http://forum.numer.ai/t/validation-2-announcement/166>)  
But it would be nice to know if there is any hole, or duplicates in the eras as indicated by the numbers.

---

### Post #4 — **rpica** | 2021-04-04 09:56 UTC

Maybe basic follow-up question … if validation eras correspond to a month, and the test/live eras to a different time-span (week), wouldn’t the relation features->target change? as a different time span is considered in the row, and the target is some sort of aggregated value of the performance of that stock’s row?
