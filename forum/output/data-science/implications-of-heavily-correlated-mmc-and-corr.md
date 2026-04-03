---
title: "Implications of heavily correlated MMC and CORR?"
category: Data Science
url: https://forum.numer.ai/t/implications-of-heavily-correlated-mmc-and-corr/8072
created_at: 2025-05-26T16:59:56.856000+00:00
last_posted_at: 2025-06-05T16:07:54.356000+00:00
posts_count: 4
views: 401
tags: []
---

# Implications of heavily correlated MMC and CORR?

---

### Post #1 — **pharus** | 2025-05-26 16:59 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/777fa14a57624bbaaf49f4c69fde47a3faabddab.png)image422×472 24.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/777fa14a57624bbaaf49f4c69fde47a3faabddab.png> "image")

Does this imply the prediction is ‘unique’? Maybe even random/irrelevant?  
Is this model worth examining more?

Love to hear any thoughts about this.

---

### Post #2 — **wigglemuse** | 2025-05-26 17:18 UTC

Being correlated is not strange (generally going up & down at the same time), but having the same actual numerical values between the two is a bit more unusual as they are totally different things. That said, it isn’t especially interesting unless those scores are higher and it does it for a much longer time. I’ve had models track like that for months, and then diverge. What does it mean? Nothing special that I can see. If cumulative mmc is actually beating cumulative corr numerically over a long period (while still being good), that sounds like an interesting model. This one is too short of a time to say anything – just random probably.

---

### Post #3 — **pharus** | 2025-05-26 18:01 UTC _(reply to #2)_

Ah, thanks for your insights!

---

### Post #4 — **zentratech** | 2025-06-05 16:07 UTC _(reply to #3)_

i agree wigglemuse! how did this go
