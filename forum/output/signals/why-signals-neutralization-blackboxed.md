---
title: "Why signals neutralization blackboxed?"
category: Signals
url: https://forum.numer.ai/t/why-signals-neutralization-blackboxed/4452
created_at: 2021-11-03T12:26:39.883000+00:00
last_posted_at: 2021-12-08T15:27:35.004000+00:00
posts_count: 2
views: 870
tags: []
---

# Why signals neutralization blackboxed?

---

### Post #1 — **put** | 2021-11-03 12:26 UTC

In signals, the submitted predictions are neutralized by Numerai. The reward is calculated based on the neutralized correlation value.  
However, the neutralization vector is not known to the users.  
This appears to make unnecessary effort.  
Most of the predictions of our model may have been neutralized and potentially disappeared.  
In other words, it feels like there is no point in building models to maximize the predictions for the targets provided.

I am particularly curious if well-known features such as RSI and MACD are being neutralized.  
If so, features that correlate well with them should not be included directly in the model or should be neutralized beforehand.  
I believe that this will improve the generalization and contribute to the metamodel because the dimensionality can be reduced significantly.

Right now I have about 30 models submitted, and I am struggling with the situation that the correlations in the CV at hand do not correlate with the correlations in Numerai’s evaluation tool. So, I staked equally to my models.  
Then what should I maximize?  
It’s like a blind dart, isn’t it?

It seems to me that if I know the neutralization vector, I can CV with the neutralized correlations in advance.

I’m not trying to criticize or attack.  
I’m sorry if I hurt someone.  
Perhaps there is something I am not understanding well.  
I would be happy if you could give me something constructive to go on.

---

### Post #2 — **bluesapphire** | 2021-12-08 15:27 UTC

I’m new here - but I think the neutralization vector uses and hence has insights into their linear risk model, which Numerai is holding close to their chest.
