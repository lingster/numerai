---
title: "Does make sense a neutralization with proportion 1?"
category: Data Science
url: https://forum.numer.ai/t/does-make-sense-a-neutralization-with-proportion-1/4123
created_at: 2021-09-15T09:53:39.725000+00:00
last_posted_at: 2021-09-15T14:29:06.542000+00:00
posts_count: 2
views: 654
tags: []
---

# Does make sense a neutralization with proportion 1?

---

### Post #1 — **eleven_sigma** | 2021-09-15 09:53 UTC

Why use a feature for training and then remove all its linear effect from the predictions?  
In theory only interaction effects with other features will remains in the predictions.  
Is there any justification dropping al the main effect and leave the interactions?  
Why not the simplest strategy of drop the feature at all of the model?

---

### Post #2 — **of_s** | 2021-09-15 14:29 UTC

I’m not sold on the benefits of neutralization in this tournament, and would be open to changing my mind if Numerai supported this procedure with data for pre- and post-neutralized scores in Signals.
