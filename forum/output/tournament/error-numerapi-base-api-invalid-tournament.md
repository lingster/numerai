---
title: "ERROR numerapi.base_api: invalid tournament"
category: Tournament
url: https://forum.numer.ai/t/error-numerapi-base-api-invalid-tournament/1042
created_at: 2020-10-10T07:32:54.670000+00:00
last_posted_at: 2020-10-13T06:36:22.648000+00:00
posts_count: 4
views: 1093
tags: []
---

# ERROR numerapi.base_api: invalid tournament

---

### Post #1 — **wentixiaogege** | 2020-10-10 07:32 UTC

Why is below erroes happened? for the record,I can upload the submission.csv direct using the upload button, so the file should be ok,but using the code get below erroes  
,code is from：<https://www.kaggle.com/carlolepelaars/how-to-get-started-with-numerai>

You already have the newest data! Current round is: 232  
232  
2020-10-10 15:27:06,659 INFO numerapi.base_api: uploading predictions…  
2020-10-10 15:29:11,151 ERROR numerapi.base_api: invalid tournament  
Traceback (most recent call last):  
File “D:/PycharmProjects/numerai/upload.py”, line 97, in   
napi.upload_predictions(“submission.csv”, tournament=tournament)  
File “D:\Program_Files\Anaconda3\lib\site-packages\numerapi\numerapi.py”, line 960, in upload_predictions  
create = self.raw_query(create_query, arguments, authorization=True)  
File “D:\Program_Files\Anaconda3\lib\site-packages\numerapi\base_api.py”, line 125, in raw_query  
raise ValueError(err)  
ValueError: invalid tournament

---

### Post #2 — **uuazed** | 2020-10-12 18:57 UTC

In that example script there is a mixup between `round` and `tournament`. round is the number of the weekly round, tournament is an integer that defines the tournament you want to participate in. That is basically irrelevant right now, because there is only one tournament active (that used to be different in the past).  
to fix your script, just do `napi.upload_predictions("submissions")` (so no `tournament` parameter) and you should be fine.

Tell me how it went!

---

### Post #3 — **wentixiaogege** | 2020-10-13 02:45 UTC _(reply to #2)_

Thanks very much for your answer , I will give a try recently~

---

### Post #4 — **wentixiaogege** | 2020-10-13 06:36 UTC _(reply to #3)_

man,you are correct~~ thanks again
