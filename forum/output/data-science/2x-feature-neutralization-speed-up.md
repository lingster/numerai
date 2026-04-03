---
title: "2x Feature Neutralization Speed Up"
category: Data Science
url: https://forum.numer.ai/t/2x-feature-neutralization-speed-up/4473
created_at: 2021-11-08T09:19:24.840000+00:00
last_posted_at: 2021-12-09T01:38:34.061000+00:00
posts_count: 6
views: 1841
tags: []
---

# 2x Feature Neutralization Speed Up

---

### Post #1 — **by256** | 2021-11-08 09:19 UTC

Here’s a simple linear algebra trick to speed up feature neutralization (I got a 2x speed up on my machine but this will vary depending on your hardware).

In the feature neutralization function provided by Numerai, simply replace the line
    
    
    scores -= proportion * (exposures @ (np.linalg.pinv(exposures) @ scores))
    

with
    
    
    scores -= proportion * (exposures @ np.linalg.lstsq(exposures, scores)[0])
    

**The two are equivalent, since finding the least squares solution to Ax = b is equivalent to taking the pseudo-inverse of A then matrix multiplying by b, which is slower and less numerically stable due to the pseudo-inverse.**

This simple test in numpy shows that they’re equivalent:
    
    
    import numpy as np
    
    M, N, = 2000, 40
    
    A = np.random.normal(size=(M, N))
    b = np.random.normal(size=(M,1))
    
    x_pinv = np.linalg.pinv(A) @ b
    x_lstsq = np.linalg.lstsq(A, b)[0]
    
    print(np.all(np.isclose(x_pinv, x_lstsq)))
    

This should return `True`, and their mean-squared error is around 1e-33.

---

### Post #2 — **jefferythewind** | 2021-11-09 11:35 UTC

This is great. I was just thinking how I could speed up this neutralization code, and this looks perfect. Something I noticed in the code I pulled down from github is that they have converted the numbers to float 32 datatype for this step, probably to save time. So that actually is going to also be less accurate that what you’re suggesting. Without the conversion, the datatype should be float 64. With your version it is still running pretty quickly.

---

### Post #3 — **gbrecht** | 2021-11-09 20:55 UTC

This code generates the following warning. Not that I mind it, it is just that I do not know where to pass the `rcond` parameter into and I do not know whether I want the current or future behaviour …
    
    
    FutureWarning: `rcond` parameter will change to the default of machine precision times ``max(M, N)`` where M and N are the input matrix dimensions.
    To use the future default and silence this warning we advise to pass `rcond=None`, to keep using the old, explicitly pass `rcond=-1`.
      scores -= proportion * (exposures @ np.linalg.lstsq(exposures, scores)[0])

---

### Post #4 — **by256** | 2021-11-09 21:16 UTC _(reply to #3)_

[@gbrecht](</u/gbrecht>)

The `rcond` param is passed to `np.linalg.lstsq`, so the line becomes
    
    
    scores -= p * (exposures @ (np.linalg.lstsq(exposures, scores, rcond=None)[0]))
    

The difference between the new and old behaviour is explained in the [np.linalg.lstsq](<https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html>) docs. I trust that the numpy overlords know what they’re doing, so I’m personally using the new default behaviour.

Hope this helps!

---

### Post #5 — **bluesapphire** | 2021-12-08 15:35 UTC

Thanks for catching this.

I’m an old timer - and back then, we had been forbidden to ever invert a matrix and then multiply by b. That’s numerically far less stable than a backsolve (and even within backsolve, there are several choices of factorizations, some more applicable than others). There’s too many ‘packages’ these days for anyone to care to learn all that ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

---

### Post #6 — **bluesapphire** | 2021-12-09 01:38 UTC _(reply to #4)_

You may wanna try np.linalg.solve() - this is their backsolve, with a factorization such as LU, that avoids inverting the matrix.
