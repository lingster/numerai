---
title: "Why can't we stake on FNC?"
category: Tournament
url: https://forum.numer.ai/t/why-cant-we-stake-on-fnc/4884
created_at: 2022-02-02T20:42:10.911000+00:00
last_posted_at: 2022-02-03T13:41:13.908000+00:00
posts_count: 10
views: 809
tags: []
---

# Why can't we stake on FNC?

---

### Post #1 — **smilence666** | 2022-02-02 20:42 UTC

Does anyone know the reason behind that we can’t stake on FNC?

My model seems to be ranked consistently high (in terms of percentile) on FNC but not necessarily for other metrics. Any suggestions to improve it and tilt to corr/mmc from FNC?

---

### Post #2 — **restrading** | 2022-02-03 04:27 UTC

Why not neutralize your predictions and stake on that?

---

### Post #3 — **wigglemuse** | 2022-02-03 04:38 UTC _(reply to #2)_

Neutralizing yourself is an option (and maybe a good one if FNC is good but Corr is bad as the poster says here), but you’re operating at a significantly reduced scale (in terms of magnitude) and your MMC will probably suffer when we are having high-scoring rounds for non-neutralized models. If they want to encourage good FNC models, they should neutralize everybody’s models (since they do anyway) and pay on that (at maybe 2x or more), and then also compute MMC (or TC or whatever) post-neutralization apples-to-apples so it is a fair fight. Right now they are encouraging high corr unneutralized models even though they (from what I can gather) neutralize them for actual trading use. Seems like straight corr should be on the chopping block…

---

### Post #4 — **smilence666** | 2022-02-03 04:50 UTC _(reply to #2)_

it will reduce the correlation. i think i got the answer from wigglemuse. thanks anyway.

---

### Post #5 — **smilence666** | 2022-02-03 04:51 UTC _(reply to #3)_

thanks for the detailed answer! it seems i should neutralize to less features - i guess neutralizing to too many reduce my corr but make the FNC pretty good compared to others.

---

### Post #6 — **wigglemuse** | 2022-02-03 04:52 UTC

I think scoring/payouts will definitely be moving in this direction one way or another though. We’ll see what the next iteration of TC looks like…

---

### Post #7 — **smilence666** | 2022-02-03 04:54 UTC _(reply to #6)_

yeah, definitely looking forward to the evolving of the scoring / payout functions. But thank you for the great points on the scale part. although my std decreases more than the sacrifice of corr, it may not be always optimal to neutralize to too many, especially given we can’t leverage up the stake on the corr LOL.

---

### Post #8 — **wigglemuse** | 2022-02-03 04:58 UTC

I stopped worrying about neutralization and FNC because it clearly pays more to go for straight high corr. Once they start paying for FNC I will optimize for FNC. And I’ll be fine with that (if they put a multiplier on it, that is).

---

### Post #9 — **restrading** | 2022-02-03 05:20 UTC _(reply to #4)_

FNC by definition is calculated on predictions neutralized on all features.

---

### Post #10 — **smilence666** | 2022-02-03 13:41 UTC _(reply to #8)_

Yes, that would be a great strategy.
