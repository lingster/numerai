---
title: "How can I use the tournament data as a time series"
category: Tournament
url: https://forum.numer.ai/t/how-can-i-use-the-tournament-data-as-a-time-series/2176
created_at: 2021-03-06T11:26:42.511000+00:00
last_posted_at: 2021-03-10T02:44:45.900000+00:00
posts_count: 5
views: 1143
tags: []
---

# How can I use the tournament data as a time series

---

### Post #1 — **aldente** | 2021-03-06 11:26 UTC

I wanna know if the row entries are actual ticks or not, and whether the targets are the values for this particular time, or is it the resulting target after a tick with the given features?

Assuming the features are a function of time and the target is also a function of time, is the data related as follows?  
Features(t) → target(t)  
OR  
Features(t) → target(t+1)

---

### Post #2 — **wigglemuse** | 2021-03-06 16:47 UTC

You can’t really do time-series with this data. You can’t match up rows from different periods. The target is 4 weeks (20 trading days) in the future relative to the features – that’s what you are predicting.

---

### Post #3 — **aldente** | 2021-03-07 07:59 UTC _(reply to #2)_

But are the rows chronologically ordered?

---

### Post #4 — **wigglemuse** | 2021-03-07 14:50 UTC

The eras are chronologically ordered. The rows within each era are of the same time period. Each row is a different stock, so there is no time ordering within an era – an era is a snapshot of time of X number of stocks (X = number of rows in era). The row order within an era (i.e. the order of the stocks) should be considered random. And as I said, there is no way to link up a specific stock row in one era to the same stock in a different era (and it might not even be there anyway – the exact selection of stocks isn’t the same in each era either.)

---

### Post #5 — **aldente** | 2021-03-10 02:44 UTC _(reply to #4)_

Alright, thank you for the explanation.
