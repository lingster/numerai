---
title: "How about staking on FNC?"
category: Feedback
url: https://forum.numer.ai/t/how-about-staking-on-fnc/3590
created_at: 2021-06-12T17:54:10.202000+00:00
last_posted_at: 2021-06-12T22:57:12.858000+00:00
posts_count: 4
views: 858
tags: []
---

# How about staking on FNC?

---

### Post #1 — **rigrog** | 2021-06-12 17:54 UTC

Numerai incentivized CORR first, then MMC later on, believing them to measure something that improves Numerai’s metamodel (and hence the hedge fund’s performance).

So now you’re talking up FNC (“you” being Numerai folks, if you’re reading this), encouraging us to value this statistic. If you really mean it, please consider incentivizing FNC as a staking option, as you’ve already done with MMC.

---

### Post #2 — **sneaky** | 2021-06-12 20:08 UTC

You can stake on FNC. FNC is Feature neutral correlation. If you neutralize your predictions against the features before upload, then the CORR will be FNC. <https://docs.numer.ai/tournament/feature-neutral-correlation> here you can find everything you need.

---

### Post #3 — **rigrog** | 2021-06-12 22:21 UTC _(reply to #2)_

Thanks for that link, I think I have a better idea what FNC is.

If I do normalize my predictions, and then neutralize them w.r.t. the features (as shown in that piece of code):

  1. Is my new (Spearman rank-order) CORR, now the same as my old FNC?

  2. Are my _new_ CORR and FNC equal to each other?

  3. Assuming (1) is true, anyone whose FNC is consistently higher than his CORR already has incentive to do that neutralizing. Then if (2) is also true, we should see many participants with CORR = FNC.

---

### Post #4 — **sneaky** | 2021-06-12 22:57 UTC

As I understand it : 1) yes, 2) don’t know, but my intuition is no, I would guess that you can find another linear relationships with residuals 3) pple tried different levels of neutralization and the result was that it is not good to neutralize 100%. I did experiments as well and also found 100% neutralized models underperforming.
