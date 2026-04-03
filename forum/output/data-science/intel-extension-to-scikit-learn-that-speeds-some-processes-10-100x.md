---
title: "Intel Extension to Scikit-learn that speeds some processes 10-100x"
category: Data Science
url: https://forum.numer.ai/t/intel-extension-to-scikit-learn-that-speeds-some-processes-10-100x/4447
created_at: 2021-11-01T16:52:54.237000+00:00
last_posted_at: 2021-11-01T16:52:54.364000+00:00
posts_count: 1
views: 964
tags: []
---

# Intel Extension to Scikit-learn that speeds some processes 10-100x

---

### Post #1 — **oholiab** | 2021-11-01 16:52 UTC

Intel has released an extension to Scikit-learn that speeds up some workloads 10-100x. Of course, this only works on Intel chips, but could be useful for those of us using scikit for our numerai models.

<https://intel.github.io/scikit-learn-intelex/>

The modifications to code are minimal:
    
    
    from sklearnex import patch_sklearn
    patch_sklearn()
