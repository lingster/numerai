---
title: "NoneType error on Upload_Prediction"
category: Tournament
url: https://forum.numer.ai/t/nonetype-error-on-upload-prediction/2475
created_at: 2021-03-21T08:03:46.340000+00:00
last_posted_at: 2021-05-31T05:19:24.871000+00:00
posts_count: 14
views: 1067
tags: []
---

# NoneType error on Upload_Prediction

---

### Post #1 — **evanhennis** | 2021-03-21 08:03 UTC

I am using Google Colab and I am getting a [‘NoneType’ object is not subscriptable] when calling the [upload_predictions] method. I know that my model_id value is correct since I use it early to set up my connection. Any ideas?

---

### Post #2 — **ml_is_lyf** | 2021-03-21 09:37 UTC

Hard to say exactly what’s going on without the full stack trace. But your code should look something like this:
    
    
    # Get your API keys and model_id from https://numer.ai/notebook
    public_id = "REPLACEME"
    secret_key = "REPLACEME"
    model_id = "REPLACEME"
    napi = numerapi.NumerAPI(public_id=public_id, secret_key=secret_key)
    # Upload your predictions
    predictions_df.to_csv("predictions.csv", index=False)
    submission_id = napi.upload_predictions("predictions.csv", model_id=model_id)
    

Here’s what it means for an object to be subscriptable:

[stackoverflow.com](<https://stackoverflow.com/questions/216972/what-does-it-mean-if-a-python-object-is-subscriptable-or-not>) [ ![Alistair](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7f052a8328e33cd23ad01638e7ea1e234a188124.png) ](<https://stackoverflow.com/users/11324/alistair>)

####  [What does it mean if a Python object is "subscriptable" or not?](<https://stackoverflow.com/questions/216972/what-does-it-mean-if-a-python-object-is-subscriptable-or-not>)

**python, terminology**

asked by [ Alistair ](<https://stackoverflow.com/users/11324/alistair>) on [09:08PM - 19 Oct 08 UTC](<https://stackoverflow.com/questions/216972/what-does-it-mean-if-a-python-object-is-subscriptable-or-not>)

So it sounds like it is trying to iterate over something (probably the data), and something is going wrong there. So make sure your predictions.csv is in the correct format, probably something wrong about it.

---

### Post #3 — **evanhennis** | 2021-03-21 15:17 UTC _(reply to #2)_

I will take a look at that. The web upload worked just fine so there must be something that the code is checking. I will test a few things the next time I submit my predictions.

---

### Post #4 — **evanhennis** | 2021-03-21 17:14 UTC

I changed the format of my csv and it still isn’t working. It does appear to be an issue with authorization as I get this error:

ERROR numerapi.utils: Oops, something went wrong: Invalid return character or leading space in header: Authorization

---

### Post #5 — **ml_is_lyf** | 2021-03-21 17:25 UTC _(reply to #4)_

Sounds like there’s something wrong with your keys and/or model-id then. Print the values and make sure they’re what you expect they are. Applying strip to them might allow it to work, if it does it means you’ve got spaces and/or newline characters in your variables.

<https://www.w3schools.com/python/ref_string_strip.asp>

---

### Post #6 — **evanhennis** | 2021-03-21 17:47 UTC

I will give that a shot. I removed my numeric id columns and used the correct id column and that still didn’t work.

---

### Post #7 — **asteeber** | 2021-03-22 04:26 UTC

Try just uploading the CSV manually to the NumerAI site, that way you have something in before submissions close for round 256. If it’s accepted then you know that something is wrong with your code and you should troubleshoot that during the week.

If it’s not accepted then you know something is wrong with your CSV. Make sure you’re predicting the most recent dataset (the number of rows changes in the tournament dataset every week). Also make sure your columns are labeled exactly as shown in the example predictions CSV and format everything exactly like the example.

Good luck!

---

### Post #8 — **evanhennis** | 2021-03-22 19:43 UTC

Going through the web site worked fine. Do you know where the “official” documentation is for the submission? I have seen it a few places.

My csv file has “id” and “prediction” as the column headers and then the data. Is that correct? The example python script shows it just writing out the predictions.

---

### Post #9 — **evanhennis** | 2021-03-22 20:00 UTC

I want to thank everyone for their help. It appears that my private keys had “\n” at the end of them.

I am now getting the “session is invalid or has expired” so I will give it another shot for 257

---

### Post #10 — **wigglemuse** | 2021-03-22 20:20 UTC _(reply to #9)_

You still have this whole week to upload 256 – it will just be late (can’t stake, doesn’t count for rep). You’ll still get scores though.

---

### Post #11 — **evanhennis** | 2021-03-22 20:40 UTC _(reply to #10)_

Sorry, I wasn’t very clear. I was able to upload through the web site. When I said “give it another shot” I mean give my Colab notebook another shot to upload.

---

### Post #12 — **wigglemuse** | 2021-03-22 20:42 UTC _(reply to #11)_

Righto. If your submission was late though, you can overwrite it (even with the same thing) so you could still work on that if you wanted. Or create another model on your account to play with…

---

### Post #13 — **asteeber** | 2021-03-23 06:51 UTC _(reply to #9)_

It’s those small little bugs that are the most annoying, haha! Glad you were able to diagnose the problem

---

### Post #14 — **polskyedd** | 2021-05-31 05:19 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/evanhennis/48/702_2.png) evanhennis:

> [‘NoneType’ object is not subscriptable]

The error is self-explanatory. You are trying to **subscript an object** which you think is a list or dict, but actually is None. This means that you tried to do:

`None[something]`

[NoneType](<http://net-informations.com/python/err/nonetype.htm>) is the type of the **None object** which represents a lack of value, for example, a function that does not explicitly return a value will **return None** . In general, the error means that you attempted to **index an object** that doesn’t have that functionality. You might have noticed that the method **sort()** that only modify the list have no return value printed – they return the default None. This is a **design principle** for all mutable data structures in Python.
