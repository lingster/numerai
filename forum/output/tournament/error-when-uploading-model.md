---
title: "Error when uploading model"
category: Tournament
url: https://forum.numer.ai/t/error-when-uploading-model/6815
created_at: 2023-11-21T07:05:56.126000+00:00
last_posted_at: 2024-10-26T13:17:03.534000+00:00
posts_count: 6
views: 1413
tags: []
---

# Error when uploading model

---

### Post #1 — **bcb** | 2023-11-21 07:05 UTC

When i try to upload my newest models i have the following error:
    
    
    |11/21/2023 7:39:47 AM|File "/usr/local/lib/python3.10/pickle.py", line 331, in _getattribute|
    | --- | --- |
    |11/21/2023 7:39:47 AM|raise AttributeError("Can't get attribute {!r} on {!r}"|
    |11/21/2023 7:39:47 AM|AttributeError: Can't get attribute '_function_setstate' on <module 'cloudpickle.cloudpickle' from '/usr/local/lib/python3.10/site-packages/cloudpickle/cloudpickle.py'>|
    

What is wrong here? Anyone else having this issue?

---

### Post #2 — **dl10yr** | 2023-12-03 05:08 UTC

I had the same error.  
I downgraded cloudpickle to 2.2.1 and solved this error.

---

### Post #3 — **bcb** | 2023-12-04 09:26 UTC _(reply to #2)_

That solved the issue, thanks!

---

### Post #4 — **scholle** | 2024-03-01 21:36 UTC

i get the same error even after downgrading to 2.2.1. i tried 2.1.0, 2.2.1, 3.0.0 . any ideas?

cheers

EDIT: I solved it… 2.2.1 does indeed work, my downgrade had not worked properly… If you encounter a similar issue, you can check what package version is actually loaded by running

> import cloudpickle  
>  print(cloudpickle.__version__)

---

### Post #8 — **kpap** | 2024-10-25 08:18 UTC

Bumping this up as I’m getting the same error when trying to submit triggered when a sklearn model is part of predict.

Is there a known issue with sklearn’s model persistence using cloudpickle? I see that cloudpickle offers no forward compatibility guarantees - could that cause issues during submission?

---

### Post #9 — **kpap** | 2024-10-26 13:17 UTC _(reply to #8)_

hmm sweet, figured it out, downgrading to 2.1.0 works if I use TPU runtime. It was bringing dependency conflicts when running in CPU. Resolved ![:robot:](http://forum.numer.ai/images/emoji/twitter/robot.png?v=12)
