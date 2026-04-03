---
title: "Participant-centric model benchmark"
category: Tournament
url: https://forum.numer.ai/t/participant-centric-model-benchmark/5938
created_at: 2022-12-14T21:41:45.790000+00:00
last_posted_at: 2022-12-15T16:54:19.599000+00:00
posts_count: 3
views: 616
tags: []
---

# Participant-centric model benchmark

---

### Post #1 — **kayeffnumeraitor** | 2022-12-14 21:41 UTC

Hello again everyone,

When using the diagnostics page you end up with some insights about the model provided you trained your model only on the vanilla train set. While they certainly may give good feedback about your model quality (apart from TC, but lets not dive into that), what I always found lacking is that they are metrics useful from the viewpoint of Numerai, but not from the viewpoint of a tournament participant.

Since the only metric that we are able to back-test AND stake on right now is CORR, I will assume that the participant will stake on CORR only.

A numerai participant staking on CORR obviously will be burned if the correlation of their predictions are less than zero, and rewarded if greater than zero. So then the question is: How can the particpant minimize the probability of being burned and maximize the probability of getting a reward in any given round?

For that reason the metric that I use for my models is the following: Evaluate the ranked correlation on all validation eras, assume that the per era correlation follows a gaussian distribution, and calculate the probability for having a per era correlation greater than zero.

As a benchmark, I compare it to the example predictions over the same period, and also to random predictions. Here is such a result from one of my latest models:

[![benchmark](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/55092547112580f9d9549b9529002fc25a841868_2_690x388.png)benchmark1152×648 47 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/55092547112580f9d9549b9529002fc25a841868.png> "benchmark")

This result tells me, under the assumption that future eras behave similar to the ones in the validation set, in ~85 % of the weekly eras my model should receive positive correlation, which also is comparable to the example predictions.

---

### Post #2 — **murkyautomata** | 2022-12-15 07:23 UTC

If you’re assuming your correlation follows a gaussian, then your negative corr probability is a function of your sharpe ratio.

---

### Post #3 — **kayeffnumeraitor** | 2022-12-15 16:54 UTC _(reply to #2)_

Yes, but at least for me sharpe ratio is less intuitive than the probability of receiving positive results per round.
