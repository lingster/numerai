---
title: "Value of weak models"
category: Numeraire
url: https://forum.numer.ai/t/value-of-weak-models/1405
created_at: 2021-01-02T09:45:12.616000+00:00
last_posted_at: 2021-01-02T17:22:03.619000+00:00
posts_count: 3
views: 1211
tags: []
---

# Value of weak models

---

### Post #1 — **nyuton** | 2021-01-02 09:45 UTC

Even some simple models can generate some (low) correlation with ~0 MMC (Like some sample scripts available online)

As long as the correlation is positive, the hedge fund pays out some money for these submission even though they will certainly not imporve trading performance of the hedge fund.

Why is it good for the hedge fund to pay for these low performing models?  
While one low performing models certainly won’t break the bank, if 100s of weaks models show up, it can add up to a significant sum.

Maybe I just don’t understand the whole business model.  
Can someone please help?

---

### Post #2 — **restrading** | 2021-01-02 10:12 UTC

If a model is indeed low performing, the stake will burn. If it is weakly positive, it has some predictive power and may add to the diversity of the meta model.  
Even if a model may seem weak, I believe the meta model does not use it directly, but rather builds a model on top of all staked models to make better predictions.  
Similar to how ensemble works, multiple weak models form a stronger model overall.

---

### Post #3 — **wigglemuse** | 2021-01-02 17:22 UTC

Weak models will get bad scores, and will burn their stakes, thereby disincentivizing weak models in favor of better ones. So the general answer to both of your related questions (one in a different thread) is: THE STAKING MECHANISM. If you are bad, you lose. If you are good, you are rewarded. If you are good and unique, you are even more rewarded. So…people will try to create good & unique models.
