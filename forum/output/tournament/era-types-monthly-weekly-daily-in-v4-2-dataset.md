---
title: "Era types (monthly, weekly, daily) in V4.2 dataset"
category: Tournament
url: https://forum.numer.ai/t/era-types-monthly-weekly-daily-in-v4-2-dataset/6731
created_at: 2023-10-15T11:45:50.485000+00:00
last_posted_at: 2023-10-15T14:36:35.571000+00:00
posts_count: 2
views: 505
tags: []
---

# Era types (monthly, weekly, daily) in V4.2 dataset

---

### Post #1 — **eleven_sigma** | 2023-10-15 11:45 UTC

It’s not clear which eras where monthly (if any in V4.2 dataset), weekly or daily.  
This is crucial for apply the embargo according the type. Embargo of 4 or 5 is enough for weekly eras and 20 days responses, but if eras are daily we need to use 20 or a bit more of embargo.  
Has someone the ranges of monthly, weekly and daily eras in V4.2?

---

### Post #2 — **wigglemuse** | 2023-10-15 14:36 UTC

The interval between eras in the train & validation datasets is weekly, always (it is the weekend round) – the live weekday rounds never make it into those files. So each era starts a week after the previous one. The duration of each is a function of the target(s) you are using because that determines how many others are overlapping and “sharing” in that same target, either 20day (4 weeks) or 60day (12 weeks). (Of course we are scored on a 20d target for live rounds.)
