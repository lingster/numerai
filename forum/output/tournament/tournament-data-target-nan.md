---
title: "Tournament Data Target 'NaN'"
category: Tournament
url: https://forum.numer.ai/t/tournament-data-target-nan/4636
created_at: 2021-12-16T17:26:03.152000+00:00
last_posted_at: 2021-12-16T17:35:27.658000+00:00
posts_count: 3
views: 774
tags: []
---

# Tournament Data Target "NaN"

---

### Post #1 — **anonai** | 2021-12-16 17:26 UTC

I recently downloaded training and tournament data. The training data was OK, however for the “target” column in tournament data entire column had values of “NAN”. Is this happening for anyone else?

---

### Post #2 — **wigglemuse** | 2021-12-16 17:31 UTC

That’s because those are the values you are to predict, so they are not provided, i.e. using “training” to make a model, and predict “tournament” data. (Only the final era in there is actually used to score you though.)

---

### Post #3 — **anonai** | 2021-12-16 17:35 UTC

Got it, thank you for your help.
