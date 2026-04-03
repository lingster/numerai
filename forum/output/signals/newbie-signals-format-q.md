---
title: "Newbie Signals Format Q"
category: Signals
url: https://forum.numer.ai/t/newbie-signals-format-q/1578
created_at: 2021-02-07T22:40:13.082000+00:00
last_posted_at: 2021-02-18T17:01:03.736000+00:00
posts_count: 3
views: 1187
tags: []
---

# Newbie Signals Format Q

---

### Post #1 — **kamici** | 2021-02-07 22:40 UTC

Hopefully noob questions are allowed. I have a series of questions starting with the more stupid ones (I have read the medium post).

  1. What exactly are the units of Signal between 0 and 1? Just a relative confidence in which stocks will go up?
  2. What is the time frame of the Signal? I get that it says 6 days ignoring the first 2, but does that mean you’re optimizing for prediction 6 days into the future and that’s it? What about very long term strategies? How is that supposed to play out?
  3. What if a strategy is specific to a specific sector? Say you’ve trained your data to work with… copper mining companies and can predict the movement of their values well. How does this translate to submitting signals? It seems like the signals have to be for the entire universe of stocks? At least from what I can tell from the sample upload csv?

---

### Post #2 — **debugyeh** | 2021-02-17 14:34 UTC

From what i’ve figured out from fairly sparse information.

  1. 0-.05 = sell 0.5-1 (buy) though I don’t think you can submit a 0 or a 1, it has to be a floating point between the two. 0.5 is neutral.

  2. It’s for basically the next week, you submit at the weekend for the coming week, that’s how long the signals are supposed to be for.

  3. For signals, it’s distinct from the tournament, you have to submit at least 10 tickers. The tournament, seems to want the entire universe, but i’m unsure, that’s actually a question i have.

---

### Post #3 — **notmushtime** | 2021-02-18 17:01 UTC _(reply to #2)_

“The tournament, seems to want the entire universe”

I like this sentence.
