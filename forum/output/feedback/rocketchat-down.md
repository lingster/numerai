---
title: "RocketChat Down?"
category: Feedback
url: https://forum.numer.ai/t/rocketchat-down/4251
created_at: 2021-10-04T03:56:57.476000+00:00
last_posted_at: 2021-10-04T20:22:04.277000+00:00
posts_count: 8
views: 939
tags: []
---

# RocketChat Down?

---

### Post #1 — **restrading** | 2021-10-04 03:56 UTC

RocketChat is very slow for me and is unusable. Is this happening to anyone else?

---

### Post #2 — **aventurine** | 2021-10-04 04:03 UTC

yes its bad right now

---

### Post #3 — **scirpus** | 2021-10-04 13:46 UTC _(reply to #2)_

It is still Kaputt - not a great look for Numerai - it looks like their diagnostics and alerts could do with a revamp.

---

### Post #4 — **scirpus** | 2021-10-04 16:11 UTC

The Rocket Chat is now fully functional again

---

### Post #5 — **wigglemuse** | 2021-10-04 16:52 UTC

It is coming up now, but very very slowly.

---

### Post #6 — **scirpus** | 2021-10-04 17:19 UTC _(reply to #5)_

I may have exaggerated the health of rocket chat I am afraid ;(

---

### Post #7 — **qeintelligence** | 2021-10-04 18:23 UTC

![:stethoscope:](http://forum.numer.ai/images/emoji/twitter/stethoscope.png?v=9) I feel no pulse here, I guess this is that monday thing for rocket chat, just like for facebook and whatsapp…

---

### Post #8 — **pschork** | 2021-10-04 20:22 UTC

Slowness was related to mongodb resource contention which triggered client retries, which triggered rate-limiting. Took a while to root cause, but Rocketchat should be 100% recovered and much snappier than before.
