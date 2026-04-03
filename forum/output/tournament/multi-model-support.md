---
title: "Multi model support"
category: Tournament
url: https://forum.numer.ai/t/multi-model-support/563
created_at: 2020-06-17T17:43:00.482000+00:00
last_posted_at: 2020-06-17T22:18:18.118000+00:00
posts_count: 2
views: 1880
tags: []
---

# Multi model support

---

### Post #1 — **correlator** | 2020-06-17 17:43 UTC

What’s the significance of model-id while submitting? Can it be any string that I can use to identify my model?  
If I want to submit 2 models (with different stakes) what’s the procedure for that?

p.s. I am familiar with multi model support but don’t know how to use it.

---

### Post #2 — **mytwocents** | 2020-06-17 22:18 UTC

The model_id identifies your model to numerai. Model name is to model_id what hostname is to IP address.

In Python, I do this:
    
    
    import numerapi
    
    napi = numerapi.NumerAPI(public_id=public_id, secret_key=secret_key)
    napi.upload_predictions(path_to_predictions, model_id=model_id)
    

I get **public_id** from <https://numer.ai/account>, upon clicking the **VIEW API KEYS** button. **secret_key** was shown once when I created my webhook. I assume you have to destroy and recreate the submit webhook to get a new secret key. (In practice I store these things in Google Cloud Secret Manager.)  
**model_id** is the UUID for your model which is obtained from <https://numer.ai/models>.

To manage your stake, use
    
    
    napi.stake_increase(nmr=nmr_amount, model_id=model_id)
    napi.stake_decrease(nmr=nmr_amount, model_id=model_id)
    

I don’t know how to delete a pending stake change using the API.
