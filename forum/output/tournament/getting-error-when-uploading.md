---
title: "Getting error when uploading"
category: Tournament
url: https://forum.numer.ai/t/getting-error-when-uploading/3416
created_at: 2021-05-24T13:54:10.552000+00:00
last_posted_at: 2021-05-24T14:09:30.963000+00:00
posts_count: 4
views: 544
tags: []
---

# Getting error when uploading

---

### Post #1 — **develuse** | 2021-05-24 13:54 UTC

API internal server error. For the Signals tournament.  
FIle is like:  
|ticker|signal|  
|A|0.49999672|  
|AA|0.5000031|  
|AAL|0.49999571|  
|AAOI|0.25014299|

---

### Post #2 — **develuse** | 2021-05-24 13:59 UTC

Also with  
ticker,signal  
A,0.49999672  
AA,0.5000031  
AAL,0.49999571  
AAOI,0.25014299  
AAON,0.49999538  
AAP,0.49999762

---

### Post #3 — **develuse** | 2021-05-24 14:01 UTC

I see probably  
OSIS,#VALUE!  
and e34  
Causing the error for the API

---

### Post #4 — **develuse** | 2021-05-24 14:09 UTC _(reply to #3)_

And confirm that it was the values from open office export
