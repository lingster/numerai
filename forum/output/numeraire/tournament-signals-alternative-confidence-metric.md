---
title: "Tournament/Signals Alternative Confidence Metric"
category: Numeraire
url: https://forum.numer.ai/t/tournament-signals-alternative-confidence-metric/5027
created_at: 2022-03-07T06:20:47.756000+00:00
last_posted_at: 2022-03-07T14:10:37.645000+00:00
posts_count: 3
views: 765
tags: []
---

# Tournament/Signals Alternative Confidence Metric

---

### Post #1 — **ganon** | 2022-03-07 06:20 UTC

Hi Numerai & Numerati!

Have you ever wondered how Numerai data scientists are feeling about the tournament on a day-to-day basis? Well, wonder no more! I’ve gone and collected data on NMR flow in and out of tournament addresses to get a better idea of how they were feeling. Also, I just want to point out that I know NMR stake sizing is a great metric for gauging confidence (that’s a big reason why it exists), but this is a bit different since I only look at how participants move NMR in and out of the tournament. In other words, NMR payouts are excluded, unlike stake sizing!

Now, more specifically on what I did. For every day this year so far, I looked at the deposits and withdraws that occurred and grouped them into days (using UTC to define the cutoffs.) I excluded NMR deposits into tournament addresses from the following addresses since they are used by Numerai themselves to pay stakes and some other stuff:

[“0x1776e1f26f98b1a5df9cd347953a26dd3cb46671”, “0x1248c66bb94607cf6b80d3aec3e62a9fe421e210”, “0xb1544C7f5D81E93A51a84382d08C6c2bd952e859”, “0x0000000000377D181A0ebd08590c6B399b272000”, “0x67b18F10C0Ff8C76e28a383B404E8e6FDEfe2050”]

Here is what I found. Looks like data scientists are mostly confident in the tournament this year:

[![NMR_Tournament_Flow](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/111bd977b4daea7a5ce1bbfbabacd78197e4b824.png)NMR_Tournament_Flow403×278 18.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/111bd977b4daea7a5ce1bbfbabacd78197e4b824.png> "NMR_Tournament_Flow")

This does beg new questions. For example, how spread out are these withdraws and deposits? Are they from a few big players or players of all sizes? Did a rapid NMR price adjustment or another event cause a big deposit or withdraw event?

Okay, that’s all for now. I have some more stuff in the works, but if you liked this or have any suggestions, please let me know!

---

### Post #2 — **autratec** | 2022-03-07 10:57 UTC

Can u also share the analysis of signal ?

---

### Post #3 — **ganon** | 2022-03-07 14:10 UTC _(reply to #2)_

Ah, so since tournament addresses are shared between the classic version and signals, I can only get a combined confidence metric. So the above graph is for both the classic tournament and signals; sorry if I didn’t make that clear. Maybe it’s better to call it a Numerai confidence metric then?
