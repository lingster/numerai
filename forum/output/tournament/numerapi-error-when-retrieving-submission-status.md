---
title: "Numerapi error when retrieving submission status"
category: Tournament
url: https://forum.numer.ai/t/numerapi-error-when-retrieving-submission-status/3891
created_at: 2021-08-02T07:42:31.808000+00:00
last_posted_at: 2021-08-02T10:36:41.721000+00:00
posts_count: 3
views: 622
tags: []
---

# Numerapi error when retrieving submission status

---

### Post #1 — **rpica** | 2021-08-02 07:42 UTC

Hello,  
Lately get an error when trying to get the status of a model’s submission:
    
    
    import numerapi
    
    napi = numerapi.NumerAPI(public_id=PUBLIC_ID, secret_key=SECRET_KEY)
    model_id = napi.get_models()['rpica']
    napi.submission_status(model_id)
    
    
    
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File ".../lib/python3.8/site-packages/numerapi/numerapi.py", line 711, in submission_status
        data = self.raw_query(query, args, authorization=True)
      File ".../lib/python3.8/site-packages/numerapi/base_api.py", line 121, in raw_query
        raise ValueError(err)
    ValueError: Cannot query field "consistency" on type "Submission".
    

Is this happening to everyone? Is there an easy fix?

Thank you!

---

### Post #2 — **rpica** | 2021-08-02 08:02 UTC

The terrible quickfix I found is to delete in `numerapi.py`, `submission_status` function, in the query string declaration the lines for consistency and concordance.

I don’t know what those are for but with that change it doesn’t break …

---

### Post #3 — **uuazed** | 2021-08-02 10:36 UTC

Upgrading numerapi should fix your issue: `pip install --upgrade numerapi`
