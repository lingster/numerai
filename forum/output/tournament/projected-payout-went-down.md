---
title: "Projected Payout went down"
category: Tournament
url: https://forum.numer.ai/t/projected-payout-went-down/4433
created_at: 2021-10-31T14:17:20.463000+00:00
last_posted_at: 2021-10-31T15:11:43.702000+00:00
posts_count: 4
views: 691
tags: []
---

# Projected Payout went down

---

### Post #1 — **notacat** | 2021-10-31 14:17 UTC

Hey guys, I’m new to this tournament and I definitely do not understand everything about it yet. I am trying to see how my models perform over time, but these past two days of results are throwing me off.

On Oct 29 my correlation was listed as 97.3 with MMC at 94.3.  
On Oct 30 my correlation was listed as 95.7 with MMC at 93.4.

However, my projected payout went from .08 to .07. Why would that decrease? Am I understanding the performance incorrectly? I was interpreting these two days as pretty good performance of my model.

Thanks ahead for your help.

[![question](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/fa9bca906a0e2a13f14b1a8e82df8e1dca0ab155_2_690x303.png)question943×415 26.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fa9bca906a0e2a13f14b1a8e82df8e1dca0ab155.png> "question")

---

### Post #2 — **wigglemuse** | 2021-10-31 14:56 UTC

The reason it is “projected” is because it is just the current estimate of what it is going to be at round resolution, which isn’t until 4 weeks after the start date. Basically, everyday your model is checked against the current state of things and you are shown the corr/mmc/payout stats based on that. But only the last day – 4 weeks, 20 trading days later – actually matters and the payout for the last day only will be your actual payout. Everything before is just something to look at. And the scores can change quite significantly over that time – the scores on the first few days or week of a round don’t mean much at all. (But if those 90%+ percentages hold up, those are very good scores indeed. What it is “good” on an absolute level changes from round to round, but obviously if you are up in the 90 percentiles you are killing it.)

---

### Post #3 — **gammarat** | 2021-10-31 15:06 UTC

[@wigglemuse](</u/wigglemuse>) covers most of it (the projected payout is only a rough estimate based on the current scores), but also note that payout is based on the actual Corr and MMC (depending how you stake), not the rank. Your Corr value dropped between Oct 29 and Oct 30 while MMC stayed fixed, so you should expect your projected payout to drop as well.

See here: [Payout documentation](<https://docs.numer.ai/tournament/learn#payouts>)

---

### Post #4 — **notacat** | 2021-10-31 15:11 UTC

That explains it very well for me. A lot of things just clicked for me after reading your explanations. Thank you [@wigglemuse](</u/wigglemuse>) and [@gammarat](</u/gammarat>) .
