---
title: "Information Coefficient (IC) added to Signals"
category: Announcements
url: https://forum.numer.ai/t/information-coefficient-ic-added-to-signals/5089
created_at: 2022-03-15T17:09:11.846000+00:00
last_posted_at: 2022-03-15T17:09:11.942000+00:00
posts_count: 1
views: 1217
tags: []
---

# Information Coefficient (IC) added to Signals

---

### Post #1 — **_liamhz** | 2022-03-15 17:09 UTC

A new metric has been added to [Signals](<https://signals.numer.ai/>): Information Coefficient (IC)

IC is defined as the spearman correlation of your unneutralized submission with raw returns.

You can’t stake on IC, but it may give you new insights into the behavior of your models. Additionally, we plan to add IC to diagnostics soon.

Some models to look at with interesting IC scores

  * [apprentice_key](<https://signals.numer.ai/apprentice_key>), a Numerai internal model that is built on features that we neutralize to. Its corr is close to zero, but its IC is quite high
  * [FactorOverflow](<https://signals.numer.ai/factoroverflow>), a user model that has a highly correlated IC and Corr over recent rounds



We look forward to seeing how you use this new metric.
