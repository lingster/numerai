---
title: "Digging into Sunshine Data"
category: Data Science
url: https://forum.numer.ai/t/digging-into-sunshine-data/6078
created_at: 2023-01-28T21:47:00.644000+00:00
last_posted_at: 2023-02-08T16:47:55.065000+00:00
posts_count: 5
views: 1088
tags: []
---

# Digging into Sunshine Data

---

### Post #1 — **dzheng1887** | 2023-01-28 21:47 UTC

From what I recall, there was not a way to identify assets in the numerai data. Was this to help protect the numerai data assets?

Otherwise, can anyone inform me if it is possible to identify the same asset over time through ordering somehow or via some score matching? Or if the data folks at numerai can give us the asset id on these rows, that would be great.

I would mainly be interested in this to measure the volatility of my predictions. Now that I think more about it, perhaps a lot of assets move in and out of the most outside prediction buckets because of random volatility in my model rather than some true change in the asset. I believe my predictions are usually pretty tight in the middle and the outside recommendations may be too unstable. However, I think others have mentioned that this is where most TC/Corr can be earned. For example, I’d like to track one asset over time as it changes buckets in the target and I’d like to observe what buckets my prediction recommends.

It would also be nice to have this to perform some sequence models. I’m too lazy to get my own data for signals. Thanks.

---

### Post #2 — **profricecake** | 2023-01-30 00:39 UTC

I don’t expect that anyone at Numerai will give you any of the data you’re asking for. However, I have found that if you compare all samples in era X with all samples in era X+1 you can generally find the one that is surprisingly similar to all the others. In an L2 norm sense.

---

### Post #3 — **dzheng1887** | 2023-01-30 04:04 UTC _(reply to #2)_

Thanks for the tip. I was thinking that could be the case for 90% of assets. Confirmation from others help.

---

### Post #4 — **dzheng1887** | 2023-01-31 19:19 UTC _(reply to #3)_

for each asset (in the 1000s) in each era, need to calculate the L2 norm of the difference between that asset and the next era asset. Do this for 1000 eras… So 1000^3 comparisons are needed to completely map it out.

Any other ideas? I’ll probably make a function to do one asset at a time from start to end. Maybe I’ll just have it running in the background

---

### Post #5 — **profricecake** | 2023-02-08 16:47 UTC _(reply to #4)_

I’d start with a recent era and compare every sample in that to the previous era. Identify which ones have clear matches, and ignore the others (I believe the set of securities considered in each era changes, so some will have no obvious close match). Then iterate.

I recommend leveraging a GPU to compute these norms in parallel.
