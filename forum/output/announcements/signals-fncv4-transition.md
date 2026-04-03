---
title: "Signals FNCV4 Transition"
category: Announcements
url: https://forum.numer.ai/t/signals-fncv4-transition/6337
created_at: 2023-05-01T23:31:08.745000+00:00
last_posted_at: 2023-05-01T23:31:08.871000+00:00
posts_count: 1
views: 1224
tags: []
---

# Signals FNCV4 Transition

---

### Post #1 — **master_key** | 2023-05-01 23:31 UTC

On June 3, all Signals CORR20 stakes will automatically transition to FNCV4, scored on [Numerai Corr](<https://docs.numer.ai/tournament/correlation-corr#calculation>). This will only apply to rounds opening on or after June 3.

All Signals scores besides the current CORR20 now use Numerai Corr, including the FNCV4 you will find on the leaderboard today.

The goal of Signals is to reward models built on data which Numerai doesn’t already have available in the Numerai Tournament. So the difference between CORR20 and FNCV4 is that FNCV4 neutralizes predictions to more features than CORR20 does as we’ve added more features to Numerai.

CORR20 reputations and FNCV4 reputations are quite similar already, with a correlation of 0.946.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d37af0d255b13ca8ea227647d06e6b10b53add37_2_673x500.jpeg)image1852×1374 104 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d37af0d255b13ca8ea227647d06e6b10b53add37.jpeg> "image")

Currently, the Signals website scores are confusing because of these scores we’ve been meaning to get rid of. This change will allow us to improve the clarity surrounding Signals scores by deleting CORR20 and CORR20V2.

The scores other than TC will then be only:

  * FNCV4 - Correlation of users neutralized submissions with target_20d_factor_feat_neutral

  * CORRV4 - Correlation of users unneutralized submissions with target_20d_factor_feat_neutral

  * IC - Correlation of users unneutralized submissions with binned raw returns target_20d_raw_return

  * RIC - Correlation of users unneutralized submissions with target_20d_factor_neutral
