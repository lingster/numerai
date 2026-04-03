---
title: "Which trading session correspond to today's scores?"
category: Tournament
url: https://forum.numer.ai/t/which-trading-session-correspond-to-todays-scores/7052
created_at: 2024-02-22T13:04:48.269000+00:00
last_posted_at: 2024-03-08T17:14:50.358000+00:00
posts_count: 4
views: 447
tags: []
---

# Which trading session correspond to today's scores?

---

### Post #1 — **eleven_sigma** | 2024-02-22 13:04 UTC

Today’s scores are from (one, two, three?)… trading sessions ago

---

### Post #2 — **wigglemuse** | 2024-02-22 17:38 UTC

2 trading days. So scores that come out Thursday are from Tuesday’s market.

---

### Post #4 — **rpica** | 2024-03-08 11:42 UTC _(reply to #2)_

Does it make sense to use external data to the tournament? It would be something common for each era, of course, since we don’t know who is who in terms of stock. But global indicators could help the model figure out aspects of the current regime … maybe?

Edit: I’m asking here because it came up thinking on the correspondence between numerai and real-world market (so also eras and a time in the past where stock market data is available).

---

### Post #5 — **wigglemuse** | 2024-03-08 17:14 UTC _(reply to #4)_

In signals where you know what’s what, it seems like it definitely could. But in the main tournament, seems tough to know how to react to such things. You could make it a variable that you are training with (but it would be common to entire eras so you’d have to be training with many eras at a time – which personally I don’t do) and then you could examine if the model gives it any importance, stuff like that. In theory most things you could think of to add are probably baked into the data already in some fashion.
