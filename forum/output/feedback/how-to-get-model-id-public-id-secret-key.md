---
title: "How to get model_id, public_id, secret_key"
category: Feedback
url: https://forum.numer.ai/t/how-to-get-model-id-public-id-secret-key/757
created_at: 2020-08-08T05:28:01.992000+00:00
last_posted_at: 2020-08-25T19:04:03.507000+00:00
posts_count: 6
views: 2689
tags: []
---

# How to get model_id, public_id, secret_key

---

### Post #1 — **sharkdeng** | 2020-08-08 05:28 UTC

Hello, i just encountered numer.ai today. When running the first submission. I got this question
    
    
    # Get your API keys and model_id from https://numer.ai/submit
    public_id = "REPLACEME"
    secret_key = "REPLACEME"
    model_id = "REPLACEME"
    napi = numerapi.NumerAPI(public_id=public_id, secret_key=secret_key)
    

How to get the public_id, secret_key, and model_id?

Thank you

---

### Post #2 — **sharkdeng** | 2020-08-08 05:35 UTC

I found one [post](<http://forum.numer.ai/t/multi-model-support/563/2>) and submit successfully, but how to check my submissions?

---

### Post #3 — **jrb** | 2020-08-08 07:25 UTC

Welcome to the tournament [@sharkdeng](</u/sharkdeng>)!

You can create API keys from your [account settings](<https://numer.ai/account>) page (Log into numerai, click on the gear icon on the top right and then click on **Settings** in the menu). Once you’re on that page, click on “Create API Key” under “Automation”.

You can get the model_id for your model(s) from the [models](<https://numer.ai/models>) page (Also accessible from the gear icon on the top right of the page). You can also get _model_id_ for your models from the API. I recommend reading the [numerapi docs](<https://numerapi.readthedocs.io/en/stable/>) for that.

You can check your latest submission from the [tournament](<https://numer.ai/tournament>) page. You can also get it via the API. Everything accesible via the website is also available via the API, except for the API keys.

---

### Post #4 — **jnolan9** | 2020-08-25 14:06 UTC

Does anyone have any more detail about what syntax is necessary to use the API? I have tried this:
    
    
    public_id = "REPLACEME"
    secret_key = "REPLACEME"
    model_id = "REPLACEME"
    napi = numerapi.NumerAPI(public_id=public_id, secret_key=secret_key)
    

In a couple of different ways and I keep getting back:

ERROR numerapi.base_api: Your session is invalid or has expired.

thanks

---

### Post #5 — **pschork** | 2020-08-25 18:44 UTC _(reply to #4)_

This typically means that you have the `public_id` and `secret_key` swapped.

---

### Post #6 — **jnolan9** | 2020-08-25 19:04 UTC _(reply to #5)_

I tried that, tried all caps, I am still seeing the same thing, not any type of login failure or anything like that. Are there any type of extended diags available with that command?
