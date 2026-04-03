---
title: "Numerai Compute not consistent Timing"
category: Tournament
url: https://forum.numer.ai/t/numerai-compute-not-consistent-timing/4503
created_at: 2021-11-14T22:49:34.062000+00:00
last_posted_at: 2021-11-14T22:49:34.164000+00:00
posts_count: 1
views: 524
tags: []
---

# Numerai Compute not consistent Timing

---

### Post #1 — **thekizoch** | 2021-11-14 22:49 UTC

Hi,

On this [page](<https://docs.numer.ai/tournament/compute>), the following is stated:

> Timing
> 
> The webhook url assigned to your Prediction Nodes are automatically registered with your Numerai Models. Numerai will execute those webhooks on Saturday at 19:00 UTC (an hour after the round starts). If we haven’t successfully received …

However, I just got an email for round 288 that the Compute was triggerred at 18:10 UTC. This difference makes a difference to me, as I load data to another cloud provider, and I can’t guarantee it will load in ten minutes.

So what is the true timing? 19:00 or 18:10 UTC?
