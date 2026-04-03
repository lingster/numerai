---
title: "L2 regularization in MLPs and noisy domains"
category: Data Science
url: https://forum.numer.ai/t/l2-regularization-in-mlps-and-noisy-domains/3848
created_at: 2021-07-26T13:34:13.118000+00:00
last_posted_at: 2021-07-27T00:54:25.641000+00:00
posts_count: 5
views: 833
tags: []
---

# L2 regularization in MLPs and noisy domains

---

### Post #1 — **neosbrother** | 2021-07-26 13:34 UTC

I’m trying to apply MLPs to Numerai and keep running into an issue where many models converge to the same place (~ -0.00311). These networks output a constant value for all samples (near 0.5, but not quite) and the weights in the layer(s) with L2 regularization applied are all very close to 0. This problem came up more and more as I tried to increase the depth of the network.

I believe the problem is happening because of L2 regularization and the noisy nature of Numerai data. L2 acts as a kind of weight decay and the noisy data helps push the weights back and forth around 0 enough that eventually, one by one, they all converge to near 0. Removing L2 regularization always resolves this problem, though it also leads to poor performance (corr is cut roughly in half without L2).

I thought increasing the learning rate would help avoid this problem as it would force larger weight updates and keep them away from 0, but I found the opposite to be true. Also, the problem seems to be more frequent with smaller (more traditional) batch sizes below 512. Intuition would be that smaller batches would help as the stochastic nature of the data would help bounce the weights around more, but I’m finding best results on larger batch sizes (~4k). Both of these observations are counter to what I would expect, so am I missing something here?

If L2 regularization really is to blame, what is right solution? I tried replacing L2 with batch normalization, but that performs much worse than L2. Using large batch sizes doesn’t really seem like the right solution, but it’s the best I have right now.

---

### Post #2 — **by256** | 2021-07-26 14:31 UTC

> and the weights in the layer(s) with L2 regularization applied are all very close to 0

Sounds like you are assigning too high a weight to the regularization term.

L2 regularization literally regresses the weights to 0, so if you are weighting this term too high in your loss, you would observe 0s for your weights.

I would try to decrease the L2 regularization factor and see if that helps.

---

### Post #3 — **restrading** | 2021-07-26 17:57 UTC

Keep in mind you are scored on correlation. It is the relative order that matters, not the absolute dispersion around mean. It should not be a big concern.

---

### Post #4 — **neosbrother** | 2021-07-26 20:53 UTC _(reply to #2)_

I was using the default for the regularization term in keras (0.01). I have since tried reducing this by 10/100x and while it did work in one configuration (for 100x reduction only), it came at the cost of a big performance drop. It was essentially like not doing L2 reg at all.

---

### Post #5 — **neosbrother** | 2021-07-27 00:54 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/restrading/48/2928_2.png) restrading:

> Keep in mind you are scored on correlation. It is the relative order that matters, not the absolute dispersion around mean. It should not be a big concern.

It’s literally outputting the same value for every single data point. This leads to a correlation of about -0.003
