---
title: "Chat License Revoked"
category: Feedback
url: https://forum.numer.ai/t/chat-license-revoked/4868
created_at: 2022-01-29T09:00:14.299000+00:00
last_posted_at: 2022-01-29T22:58:28.884000+00:00
posts_count: 10
views: 793
tags: []
---

# Chat License Revoked

---

### Post #1 — **scirpus** | 2022-01-29 09:00 UTC

I am getting a “Secure Connection Failed” [SSL Server Test: community.numer.ai (Powered by Qualys SSL Labs)](<https://www.ssllabs.com/ssltest/analyze.html?d=community.numer.ai>)

---

### Post #2 — **quantverse** | 2022-01-29 10:05 UTC

Same here. Please fix the certificate.

---

### Post #3 — **wigglemuse** | 2022-01-29 15:27 UTC

I’m having that problem in Firefox (and so are others), but not other browsers. If you uncheck “Query OCSP responder servers to confirm the current validity of certificates” in firefox, you can get around it for now.

---

### Post #4 — **restrading** | 2022-01-29 15:40 UTC _(reply to #3)_

My iOS app client cannot connect

---

### Post #5 — **wigglemuse** | 2022-01-29 19:32 UTC

Now it doesn’t work in any browser…hopefully it is the fix coming through…

---

### Post #6 — **pschork** | 2022-01-29 20:16 UTC

Alternate DNS is [rocketchat.numer.ai](<https://rocketchat.numer.ai>)

We run rocketchat via snap release and after trying all sorts of mitigations rocketchat-caddy refused to re-request a new cert `community.numer.ai`.

---

### Post #7 — **wigglemuse** | 2022-01-29 20:30 UTC _(reply to #6)_

Can you set up a forward ?

---

### Post #8 — **pschork** | 2022-01-29 20:47 UTC _(reply to #7)_

It’s setup just not working ![:persevere:](http://forum.numer.ai/images/emoji/twitter/persevere.png?v=10) for the native app. Web redirect works fine.

---

### Post #9 — **pschork** | 2022-01-29 20:56 UTC

Looks like DNS TTLs needed to clear out. Rocketchat native app is handling the redirect now.

---

### Post #10 — **restrading** | 2022-01-29 22:58 UTC _(reply to #9)_

On native app logging out and in again with the new domain works
