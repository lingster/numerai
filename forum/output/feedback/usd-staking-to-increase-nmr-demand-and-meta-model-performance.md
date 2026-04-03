---
title: "USD staking to increase NMR demand and Meta Model performance"
category: Feedback
url: https://forum.numer.ai/t/usd-staking-to-increase-nmr-demand-and-meta-model-performance/8212
created_at: 2025-12-26T15:09:32.708000+00:00
last_posted_at: 2025-12-26T15:09:32.756000+00:00
posts_count: 1
views: 98
tags: []
---

# USD staking to increase NMR demand and Meta Model performance

---

### Post #1 — **dev0n** | 2025-12-26 15:09 UTC

## Problem

Tournament participants must accept NMR price risk alongside model performance risk. These risks are unrelated, yet NMR volatility often dominates whether someone profits from participation.

This bundling has two consequences:

  1. **Weaker meta model.** Current participants stake less than their true model confidence warrants, and some skilled modelers (e.g., Kaggle GMs Richard has spoken with) don’t participate at all.
  2. **Suppressed NMR demand.** Lower staking means less buy pressure.



## Proposed Solution

Numerai offers USD staking on top of the existing NMR system:

  * User deposits USD
  * Numerai purchases NMR **on the open market** (not from treasury) and stakes it on their behalf
  * User’s USD value is locked at deposit-time exchange rate
  * On withdrawal, user receives USD at that same rate (Numerai absorbs NMR price movement)
  * Burns reduce withdrawable balance as normal



## Why Open Market Purchases Matter

If Numerai used treasury NMR instead of buying on the open market, new participant demand would never reach the market. This could depress NMR price, push more participants toward USD staking, and create a death spiral.

Open market purchases preserve NMR demand dynamics while removing friction for risk-averse participants.

## Stakeholder Impacts

Stakeholder | Impact  
---|---  
**Numerai** | Better meta model from increased + higher-confidence staking  
**NMR holders** | Price support from real buy pressure  
**Current participants** | Option to remove price risk; stake sizes can reflect true model confidence  
**New participants** | Removes crypto exposure barrier to entry
