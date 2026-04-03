---
title: "TC inconsistency between frontend and API"
category: Tournament
url: https://forum.numer.ai/t/tc-inconsistency-between-frontend-and-api/6008
created_at: 2023-01-06T12:19:48.216000+00:00
last_posted_at: 2023-01-10T21:38:23.355000+00:00
posts_count: 7
views: 734
tags: []
---

# TC inconsistency between frontend and API

---

### Post #1 — **kowalot** | 2023-01-06 12:19 UTC

Hey,

I can’t deal with some inconsistency I found between the data presented on the front-end and the data available in the API.

The items marked in yellow match, while the TC has a different value in the API.

[![frontend_era_326](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e0c7ded6736972ab481dc5f32fcab6c2e14d83d4_2_690x66.png)frontend_era_3261134×110 18 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e0c7ded6736972ab481dc5f32fcab6c2e14d83d4.png> "frontend_era_326")

[![api_tournament_era_326](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dcab7c83b099af69237b9d4883ac5f715c0cb438.png)api_tournament_era_3261039×528 43.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dcab7c83b099af69237b9d4883ac5f715c0cb438.png> "api_tournament_era_326")

I found many such TC glitches for rounds below 336 era.  
This spoils the results of my long-term tests of the model. Any idea what is the problem here?

---

### Post #2 — **wigglemuse** | 2023-01-06 16:33 UTC

Interesting. Was your payout actually negative for that round? If you look at the round page for 326 ([Numerai](<https://numer.ai/round/326>)), it shows the two positive values for both corr & tc yet the negative payout. What’s real? (I’d bring this up in support over on rocketchat to get some attention.)

---

### Post #3 — **mlivako** | 2023-01-08 08:18 UTC

I can see the same TC inconsistency for my models from round 335 back. Payout match

[![Screenshot 2023-01-08 090953](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3072e808b9950e5e27d412123cd4fe7e6da12aed_2_690x74.png)Screenshot 2023-01-08 0909531102×119 13.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3072e808b9950e5e27d412123cd4fe7e6da12aed.png> "Screenshot 2023-01-08 090953")

  


[![Screenshot 2023-01-08 091112](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/ced3d069022b797cf94175011ee33fa07989208f_2_690x68.png)Screenshot 2023-01-08 0911121012×100 14.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/ced3d069022b797cf94175011ee33fa07989208f.png> "Screenshot 2023-01-08 091112")

---

### Post #4 — **ark** | 2023-01-09 21:36 UTC _(reply to #3)_

Hey all, thanks for bringing this to our attention, I looked into this and found the inconsistency that [@kowalot](</u/kowalot>) reported is related to a backfill for 60d TC I did a while back. The values shown by v3UserProfile (and the round detail page that mlivako shows) are from this backfill, so this is a display issue and did not affect the final payout.

This is why [@kowalot](</u/kowalot>) sees positive corr/TC but negative payout, in reality round 326 the 20d TC used for paying out pl18_piorun was -0.05083876272117207 which would explain the negative payout.

I’ll be deleting these excess scores to bring these displays in line with reality.

[@kowalot](</u/kowalot>) I’ve sent your model pl18_piorun a .1 NMR bounty for finding the bug, thanks again for reporting!

---

### Post #5 — **kowalot** | 2023-01-10 09:57 UTC _(reply to #4)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/ark/48/3156_2.png) ark:

> I’ll be deleting these excess scores to bring these displays in line with reality.

Thx!!! Can you also confirm the fix to the API results (v3UserProfile/ roundModelPerformances)? I still see positive TC for round 326.

---

### Post #6 — **ark** | 2023-01-10 21:01 UTC _(reply to #5)_

These should be patched now, thank you for your patience!

---

### Post #7 — **kowalot** | 2023-01-10 21:38 UTC _(reply to #6)_

Thanks!!! Yep I see it.
