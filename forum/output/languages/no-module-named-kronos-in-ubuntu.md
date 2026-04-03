---
title: "No module named 'kronos' in ubuntu"
category: Other Languages
url: https://forum.numer.ai/t/no-module-named-kronos-in-ubuntu/5709
created_at: 2022-09-22T11:11:13.470000+00:00
last_posted_at: 2022-09-28T12:17:07.780000+00:00
posts_count: 3
views: 577
tags: []
---

# No module named 'kronos' in ubuntu

---

### Post #1 — **pavanbbva** | 2022-09-22 11:11 UTC

I’m using AWS (ubuntu instance) and django.

In ubuntu, I did `sudo pip install django-kronos`.

But, When `sudo python3 manage.py runserr --settings=health.settings`
    
    
    Import Error: No module named 'kronos'   
    

happens.

Kronos works well in locals. Why I get the error in ubuntu??

---

### Post #2 — **themicon** | 2022-09-22 14:38 UTC

Maybe use pip3?  
As in: sudo pip3 install django-kronos

---

### Post #3 — **pavanbbva** | 2022-09-28 12:17 UTC

if we can get Kronos to a position where it’s plausible for a fairly knowledgeable Ubuntu sysadmin-type user to install it and start playing with it, then people will just have a play with it. If we require people using [kronos] to come to the party with a high spec, new, clean, dedicated box, then we’re going to have fewer people trying it out.  
([Kronos Workforce | A Complete overview of Kronos Workforce in detail](<https://hkrtrainings.com/what-is-kronos-workforce>))
