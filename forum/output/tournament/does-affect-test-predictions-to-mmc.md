---
title: "Does affect test predictions to MMC?"
category: Tournament
url: https://forum.numer.ai/t/does-affect-test-predictions-to-mmc/4790
created_at: 2022-01-15T10:47:26.791000+00:00
last_posted_at: 2022-01-15T17:10:56.406000+00:00
posts_count: 2
views: 579
tags: []
---

# Does affect test predictions to MMC?

---

### Post #1 — **eleven_sigma** | 2022-01-15 10:47 UTC

I’m working in a model in which prediction process is extremely slow, so I think fill all the test predictions with 0.5 and only compute live era.  
Does it affect to the MMC in some way? And to the Meta Model contribution?  
I don’t know if test predictions are used in the metamodel process.

---

### Post #2 — **wigglemuse** | 2022-01-15 17:10 UTC

They were never used as part of your score or any visible stat, or trading by the fund, or anything that directly had an effect. They were used to generate internal backtest estimates of how out-of-sample (i.e. live) performance would hold up (since it is data you don’t have the targets for). But it is shortly to be discontinued (in March 2022) altogether – we are going to get those targets – and you won’t have to submit test predictions at all any more. So at this point…I’d say don’t worry about it.
