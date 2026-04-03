---
title: "Tournament Targets and Target Types"
category: Tournament
url: https://forum.numer.ai/t/tournament-targets-and-target-types/2218
created_at: 2021-03-07T19:01:24.946000+00:00
last_posted_at: 2021-03-07T19:35:06.505000+00:00
posts_count: 3
views: 1335
tags: []
---

# Tournament Targets and Target Types

---

### Post #1 — **jx0rd** | 2021-03-07 19:01 UTC

Hey, I’m new to numerai and was confused about a few things.

Firstly, why do we have a `target` field for the `numerai_tournament_data.csv`?

I thought the numerai tournament data was data of the next 4 weeks, and we’re submitting predictions about what those values will be? If so, why and how do we currently have `target` data?

Secondly, the target data of the training and tournament data are the values `[0., 0.25, 0.5, 0.75, 1.]`. Why in the example [Making your first submission on Numerai - Colaboratory (google.com)](<https://colab.research.google.com/github/numerai/example-scripts/blob/master/making-your-first-submission-on-numerai.ipynb>) is the example submission submitting values from around `0.45` to `0.55` as the target data. Do these values get rounded to the nearest value, i.e. `0.45` would become `0.5`, or if the targets you submit are in the range `0.45` to `0.5`, do these get normalized to the range `0` to `1` to match the training data values?

Thanks

---

### Post #2 — **asteeber** | 2021-03-07 19:25 UTC

There is validation data in the tournament dataset which includes target values, thus there being a target column. Target data for data_types “test” and “live” are filled with “x”

The obfuscated values represent movements within those signals. When ran through a machine learning algorithm they are taken as continuous variables. These algorithms average out values when they are continuous which is why you get values really close to 0.5 (you can expect to see an average of 0.5 when you randomly sample a uniform distribution between 0 and 1, which is kinda what is happening).

NumerAI gauges your performance based on correlation, so even if your predictions are really close to 0.5, the relative distance from 0.5 of your predictions is used to calculate your correlation score.

---

### Post #3 — **wigglemuse** | 2021-03-07 19:35 UTC

You get scored on RANKING correlation (per era). So only the relative ordering of your predictions matter. If an era was only 5 rows and you submitted predictions:

0.1, 0.2, 0.3, 0.4, 0.5

that would be _exactly_ the same as submitting:

0.491, 0.492, 0.493, 0.494, 0.495

because when converted to ranks they’d both be 1 2 3 4 5

And you don’t want to submit only 5 discrete values despite the target only having 5 values. Any ties in your predictions are broken automatically by the scoring method (by row order, which is essentially random) so don’t purposefully round them down to only 5 discrete values as you’re just then removing signal from your predictions.
