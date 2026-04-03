---
title: "Another proposal to merge CORR & MMC: A Dynamic Payout Scheme"
category: Tournament
url: https://forum.numer.ai/t/another-proposal-to-merge-corr-mmc-a-dynamic-payout-scheme/630
created_at: 2020-07-07T20:18:56.864000+00:00
last_posted_at: 2020-07-08T10:06:52.905000+00:00
posts_count: 2
views: 1027
tags: []
---

# Another proposal to merge CORR & MMC: A Dynamic Payout Scheme

---

### Post #1 — **alfa137** | 2020-07-07 20:18 UTC

**Motivation:**  
If models with MMC>0 have Mean(CORR)=0.0318 and Mean(MMC)=0.015 and you demand models with high MMC, the multiplier of MMC should be at least twice the multiplier of CORR. That is to say:  
_Payout = w CORR + (2-w) MMC ; such that w <0.667_  
Why? Because improving CORR by _+2d_ is easier than improving MMC by _+d_. This is in average terms, in marginal terms it can change a little bit.

**Proposal:**  
1.- Start with this initial scheme:  
_Payout = w CORR + (2-w) MMC ; such that w=0.65_  
2.- Adjust _“w”_ depending on the marginal improvement of the average CORR and MMC over time.  
3.- In this way the payout scheme can be changed for every tour in order to give an incentive to the submission of high MMC models.

---

### Post #2 — **alfa137** | 2020-07-08 10:06 UTC

Here is an example:

Current situation:  
Mean(CORR) = 0.0318  
Mean(MMC) = 0.015  
In two months:  
Mean(CORR) = 0.0418  
Mean(MMC) = 0.0175  
Marginal values:  
Delta(CORR) = 0.0418 - 0.0318 = 0.01  
Delta(MMC) = 0-0175 - 0.015 = 0.0025  
New _“w”_ :  
_w 0.01 = (2-w) 0.0025 = > w = 0.4_

**An alternative** to avoid too much fluctuations or negative marginal values would be to consider **total value instead of marginal values** :

_w 0.0418 = (2-w) 0.0175 = > w = 0.6_

In general, _w = 2/(1+Mean(CORR)/Mean(MMC))_  
with this particular cases:  
Mean(MMC) = 0 => w=0 => payout = 2 MMC ; the current MMC competition  
Mean(MMC)=Mean(CORR) => w=1 => payout = CORR + MMC ; the master_key proposal  
Mean(CORR)=0 => w=2 => payout = 2 CORR ; all the incentive goes to CORR since mean=0
