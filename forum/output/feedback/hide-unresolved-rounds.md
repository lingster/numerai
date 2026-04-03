---
title: "Hide unresolved rounds"
category: Feedback
url: https://forum.numer.ai/t/hide-unresolved-rounds/4761
created_at: 2022-01-09T18:00:20.469000+00:00
last_posted_at: 2022-01-11T05:18:14.683000+00:00
posts_count: 3
views: 689
tags: []
---

# Hide unresolved rounds

---

### Post #1 — **jay1100** | 2022-01-09 18:00 UTC

Would it be possible to hide the unresolved rounds and also not include those into the calculation of the statistics (e.g. 3 Month return). The unresolved rounds keep changing up and down a lot. This introduces quite a bit of anxiety. Just from the unresolved rounds the 3 month return can go up or down by 10 percentage points. And this is changing on a daily basis. It makes no sense to look at this noise. But because it is everywhere on the numerai website it is hard to ignore it. We are predicting targets 20 days into the future. It makes no sense to look at the results 10 days into the future. The model was not trained to do this so we should also not look at it and get confused and annoyed by it.  
Therefore I would recommend to not show it.

---

### Post #2 — **wigglemuse** | 2022-01-09 18:20 UTC

I do want to see the in-progress stuff in general, but yeah it doesn’t really make sense to have unresolved rounds affecting leaderboard rankings and stats for returns when they are not finalized. (And as we’ve seen, the first two weeks of a round are practically meaningless.) It would be nice to see a “real leaderboard” of only settled rounds.

---

### Post #3 — **profricecake** | 2022-01-11 05:18 UTC

I like that the daily scores/graphs present what might or might not happen in the unresolved rounds, but I agree it makes sense to remove unresolved rounds from the 3 month and 1 year return calculations.

If the 1 day change calculation remains the same, aka, it continues to include the volatile unresolved daily scores, this change might have the negative effect of introducing some cognitive friction into the UI. After all, the 1 day column would be based on unresolved rounds while the 3 mo/1 yr columns wouldn’t. But I’m sure there’s a good solution, even something as simple as an asterisk or popup for the 1 day column that says “includes unresolved rounds”.
