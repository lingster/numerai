---
title: "Is there a live model to track the example model of the new testset?"
category: Tournament
url: https://forum.numer.ai/t/is-there-a-live-model-to-track-the-example-model-of-the-new-testset/4231
created_at: 2021-10-01T18:35:29.111000+00:00
last_posted_at: 2021-10-01T21:20:28.360000+00:00
posts_count: 2
views: 576
tags: []
---

# Is there a live model to track the example model of the new testset?

---

### Post #1 — **nyuton** | 2021-10-01 18:35 UTC

Is there a live model to track the example model of the new testset?

---

### Post #2 — **rigrog** | 2021-10-01 21:20 UTC

Over on the chat, someone said integration_test_7 switched to new (“super massive”) data on round 282, and then… switched back? Weird, if true.

Perhaps you could compare performance of “integration_test_N” (for every “N”) against performance of example_predictions.csv (legacy version, and super-massive version). Just use 2 of your 50 model slots, to submit those (unstaked) from your account.

Or instead of example_predictions.csv, you could run the example code that’s supposed to produce it.

Of course, if you were doing that, you would no longer _need_ integration_test_whatever.
