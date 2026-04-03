---
title: "Signals Diagnostics Scoring Issue Post Mortem"
category: Signals
url: https://forum.numer.ai/t/signals-diagnostics-scoring-issue-post-mortem/5906
created_at: 2022-12-02T20:51:11.275000+00:00
last_posted_at: 2022-12-02T20:51:11.384000+00:00
posts_count: 1
views: 539
tags: []
---

# Signals Diagnostics Scoring Issue Post Mortem

---

### Post #1 — **chanes** | 2022-12-02 20:51 UTC

Hi all,

This week, I added new Signals scores to diagnostics (FNCv4, RIC, CORRv4, ICv2). In the process, I noticed differences between how diagnostics did scores vs. live scoring.

I made the diagnostics code match live scoring, but my understanding of the live scoring process was incorrect. The live scoring process includes a ranking step before filling nans, but that step runs in a separate part of our pipeline that I wasn’t aware of.

So the bottom line is: live scores are correct, but the current diagnostics scores are missing the crucial ranking step before filling nans.

This bug affects any Signals diagnostic submitted between now and my initial update on 2022-11-28 at 22:00 UTC.

I pushed the fix to prod and will be backfilling any diagnostics submitted since I pushed my initial update.

Special thanks to rocket chat users murky and PeterS. I’ll send NMR bug bounties to both.

Please let me know if you have any questions, feedback, or suggestions about this issue or the updates to Signals diagnostics.
