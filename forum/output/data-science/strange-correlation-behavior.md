---
title: "Strange correlation behavior"
category: Data Science
url: https://forum.numer.ai/t/strange-correlation-behavior/4837
created_at: 2022-01-22T17:44:20.497000+00:00
last_posted_at: 2022-01-22T20:45:19.832000+00:00
posts_count: 3
views: 957
tags: []
---

# Strange correlation behavior

---

### Post #1 — **mrquantsalot** | 2022-01-22 17:44 UTC

I was watching this NNTaleb video on correlation (<https://www.youtube.com/watch?v=o9Ac85xdjE4>) and he talks about how correlation is often not a good metric for measuring dependence between variables.

Here’s the example:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/477ca3547f0c09af6fc590924b90b988448465f0.png)image360×464 19.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/477ca3547f0c09af6fc590924b90b988448465f0.png> "image")

Any nonlinear model can use x to predict y. The takeaway could be not to use correlation to decide what features to include.

---

### Post #2 — **of_s** | 2022-01-22 20:08 UTC

It is critical to discern between correlation and dependence…  
<https://cran.r-project.org/web/packages/NNS/vignettes/NNSvignette_Correlation_and_Dependence.html>

---

### Post #3 — **gammarat** | 2022-01-22 20:45 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/df705f/48.png) mrquantsalot:

> The takeaway could be not to use correlation to decide what features to include.

I think a better takeaway is just that correlation is limited and should be used judiciously. If you take your triangle example (or Taleb’s—thanks for posting the video, btw) you’ll note that while a single correlation doesn’t produce any useful information, two correlations (one on each leg of the triangle) would. That then introduces a new question, how to partition the domain under analysis into suitable “regimes” where simple methods suffice.

The regime question surfaces here from time to time, and it’s one I do find fascinating. In practical terms, one might think of regimes in the Tournament as eras in which a specific set of features might correlate well with the targets, while a different regime would consist of eras in which a different set of features would do so. If one could identify the regime of an era before inverting the features to estimating targets, then Bob’s-yer-uncle you’ll be rich ![:laughing:](http://forum.numer.ai/images/emoji/twitter/laughing.png?v=12).
