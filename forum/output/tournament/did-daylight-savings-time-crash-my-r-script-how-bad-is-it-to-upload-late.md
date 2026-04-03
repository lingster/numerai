---
title: "Did Daylight Savings Time Crash My R Script? How bad is it to upload late?"
category: Tournament
url: https://forum.numer.ai/t/did-daylight-savings-time-crash-my-r-script-how-bad-is-it-to-upload-late/2383
created_at: 2021-03-15T17:50:31.431000+00:00
last_posted_at: 2021-03-15T18:05:59.371000+00:00
posts_count: 2
views: 557
tags: []
---

# Did Daylight Savings Time Crash My R Script? How bad is it to upload late?

---

### Post #1 — **asteeber** | 2021-03-15 17:50 UTC

I was a bit dismayed on Sunday morning when I checked my R console to see that my script (which takes ~20 hours to run) crashed. I have tested this script dozens of times with no issues before. I had 24 hours before my submission was due, so I ran the script again hoping it was a fluke. I had to wake up at 5:30 CDT this morning to make sure it completed and thankfully it did! Submission was on time, _whew_.

One of my hypotheses is that the change in time screwed up my Windows instance which then killed R.gui. Logs showed it was due to a HungAppTimeout which occurred at precisely 4:00am (an hour after the time change). Here are some snapshots of my CPU usage:

[![crash](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/d58952f3b5860dfdbc42c5cd6c64eaa9068f200f_2_690x414.jpeg)crash1800×1080 169 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d58952f3b5860dfdbc42c5cd6c64eaa9068f200f.jpeg> "crash")

I know this doesn’t have much to do with Numerai but I thought it was worth sharing. Perhaps I need to migrate to a Linux machine…

This whole incident did bring up a related question though. How badly are you penalized if your submission is late? Is it binary (either late or not) or does it get worse the later it is?

---

### Post #2 — **wigglemuse** | 2021-03-15 18:05 UTC

You are either on-time or late (or didn’t submit at all, same as late for rep purposes). The penalty is your score (again, only for rep purposes) is filled is as -0.10 for that round. There is a single round of forgiveness, so if you have your full 20 rounds filled in and then you miss one, you get the score for the example predictions instead for that round (could actually be better than your model in many cases!). If you are staked and submit late, there is no burn or anything of your stake – it is simply not in play that round.
