---
title: "Submissions for round 285 failing"
category: Tournament
url: https://forum.numer.ai/t/submissions-for-round-285-failing/4300
created_at: 2021-10-10T00:50:19.715000+00:00
last_posted_at: 2021-11-18T01:57:56.106000+00:00
posts_count: 12
views: 1104
tags: []
---

# Submissions for round 285 failing

---

### Post #1 — **m98008** | 2021-10-10 00:50 UTC

I’m trying to submit my predictions for round 285 (data version 2) with the same code as last week, but get this error: “ValueError: Invalid submission values. Values must be between 0 and 1 exclusive.”. My value are positively between 0 and 1 (actuall even between 0.25 and 0.8). I get the same error using csv, df, or manual upload.

Does anyone else have the same issue?

PS. Submissions seem to work for data version 1.

---

### Post #2 — **nooberai** | 2021-10-10 08:02 UTC

I vaguely remember getting this error because the predictions had too many decimals, so you could look into that.

---

### Post #3 — **m98008** | 2021-10-10 08:09 UTC _(reply to #2)_

Thank you, that did not work. It’s weird because I don’t think I changed anything. Am I the only one with this problem?

---

### Post #4 — **m98008** | 2021-10-10 17:23 UTC _(reply to #3)_

Found the issue - apparently, my cache had a bug not overwriting the tournament file with the latest version. It seems that the length of the tournament file has changed from round 284 (by 1). This presumably caused the somewhat cryptic error message.

---

### Post #5 — **nick_richers** | 2021-10-10 19:26 UTC

I had same problem because a couple of my predictions was equal to `1.0000000000002`, even if I performed a minmax transform at the end of pipeline, double check it

---

### Post #6 — **gammarat** | 2021-10-11 00:49 UTC

I would suggest using two calls to [argsort](<https://numpy.org/doc/stable/reference/generated/numpy.argsort.html>) (I think that’s the Python function) rather than normal rescaling to create the submissions, as from what I understand that’s what’s done anyway. E.g.

suppose R is your calculated result. Then calculate

R1=np.argsort(R)  
R2=(np.argsort(R1)+0.5)/length(R1)

and submit based on R2 rather than a rescaled version of R. (my syntax is probably screwy since I don’t speak Python, but if you catch my drift…) I’m assuming the array is zero-based indexing, not 1 based.

This gives you uniformly spaced values in (0,1), and you don’t need to keep more than four or five decimal places.

---

### Post #7 — **datacryptoanalytics** | 2021-11-15 18:20 UTC

I’m having the same problem using python.

I couldn’t solve it yet, if anyone has any more tips please help us.
    
    
    2021-11-15 13:49:57,116 INFO numerapi.base_api: uploading predictions...
    2021-11-15 13:50:18,460 ERROR numerapi.base_api: Invalid submission values. Values must be between 0 and 1 exclusive.
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-14-486540d4909b> in <module>()
    ----> 1 napi.upload_predictions("fastai_prediction.csv", model_id = "418bae42-0000-0000-0000-bc395f1d35e8")
    
    1 frames
    /usr/local/lib/python3.7/dist-packages/numerapi/base_api.py in raw_query(self, query, variables, authorization)
        124             err = self._handle_call_error(result['errors'])
        125             # fail!
    --> 126             raise ValueError(err)
        127         return result
        128 
    
    ValueError: Invalid submission values. Values must be between 0 and 1 exclusive.

---

### Post #8 — **autratec** | 2021-11-17 10:53 UTC _(reply to #7)_

Did u try manual upload and is it working ?

---

### Post #9 — **datacryptoanalytics** | 2021-11-17 18:21 UTC _(reply to #8)_

I tried and it didn’t work

---

### Post #10 — **objectscience** | 2021-11-17 23:16 UTC

This might get more attention in the support channel in chat. I’d try there so it can get resolved before the next round.

---

### Post #11 — **wigglemuse** | 2021-11-17 23:48 UTC

Well, what about the actual error that it is giving? What are the min and max values of your predictions? If there are any at 0 or below or 1 or above, they are invalid – please note that 0 and 1 themselves are invalid (must be between).

---

### Post #12 — **rigrog** | 2021-11-18 01:57 UTC _(reply to #11)_

Maybe exact 0.0 and 1.0 are _supposed_ to be invalid. But I submit predictions with those, and they’re accepted.

I have accidentally entered < 0.0, and > 1.0, and that was _not_ accepted.
