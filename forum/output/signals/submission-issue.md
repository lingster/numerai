---
title: "Submission Issue"
category: Signals
url: https://forum.numer.ai/t/submission-issue/5897
created_at: 2022-11-28T11:19:17.603000+00:00
last_posted_at: 2022-11-28T13:52:36.667000+00:00
posts_count: 2
views: 521
tags: []
---

# Submission Issue

---

### Post #1 — **mrlatter** | 2022-11-28 11:19 UTC

Hi there,

Potentially a dumb question/obvious answer so apologies in advance…

I am new to Numerai and have managed to successfully upload 2 consecutive weeks of submissions. However, when I try to submit my signals this week I am getting the error message _“submission must have non-zero standard deviation”_

I have checked the std dev of the signal and it is 0.01 but this is the same as the previous week’s uploads that have been successful.

Anyone else experienced this issue?

Thanks,  
J

---

### Post #2 — **taori** | 2022-11-28 13:52 UTC

I am not sure what’s wrong, but it seems that numerai cares only about ranking. So you can submit the ranked predictions, which should solve your issue e.g.:
    
    
    ranked_predictions = prediction_dataframe.rank(pct=True)
