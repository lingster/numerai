---
title: "Feature Neutral Correlation Added to the Tournament Site"
category: Announcements
url: https://forum.numer.ai/t/feature-neutral-correlation-added-to-the-tournament-site/1669
created_at: 2021-02-09T22:03:07.813000+00:00
last_posted_at: 2021-02-09T22:03:07.889000+00:00
posts_count: 1
views: 5573
tags: []
---

# Feature Neutral Correlation Added to the Tournament Site

---

### Post #1 — **_liamhz** | 2021-02-09 22:03 UTC

Numerai is pleased to announce the addition of feature neutral correlation (FNC) to the tournament site.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/cb26f83ac6d8a0fe6b3539523d0f96eab9f68706_2_624x401.png)1600×1031 265 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/cb26f83ac6d8a0fe6b3539523d0f96eab9f68706.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/df819814993e589185aad6a816bbc3ff6a1d3d9d_2_288x271.png)584×548 36.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/df819814993e589185aad6a816bbc3ff6a1d3d9d.png>)

With this release, users can now sort the leaderboard by FNC, and view anybody’s FNC reputation and rank.

FNC is your model’s correlation with the target, after its predictions have been neutralized to all of Numerai’s features.

A model that is overly reliant on a small set of features will have a low FNC, but might still have a high correlation in the short term. However, it is also more likely to burn significantly in the long term.

A model that uses a diverse set of features and is still correlated with the targets will have a high FNC, and is more likely to have consistent performance over the long term.

Check out the [page on FNC](<https://docs.numer.ai/tournament/feature-neutral-correlation>) in the Numerai docs for a code sample of how we calculate this metric, and [jrb’s post on model diagnostics](<http://forum.numer.ai/t/model-diagnostics-feature-exposure/899>) for an in-depth explanation of FNC, feature exposure, and associated code samples.
