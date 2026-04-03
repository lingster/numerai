---
title: "Tips on mismatched ticker names?"
category: Signals
url: https://forum.numer.ai/t/tips-on-mismatched-ticker-names/3555
created_at: 2021-06-07T03:15:24.342000+00:00
last_posted_at: 2021-07-02T23:23:31.266000+00:00
posts_count: 5
views: 1106
tags: []
---

# Tips on mismatched ticker names?

---

### Post #1 — **mugamma** | 2021-06-07 03:15 UTC

I just started submitting Signals predictions, and keep getting “Live Tickers 1969/5389” after submitting. Reviewing the submitted file and a freshly pulled universe file from

<https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/universe/latest.csv>

I don’t see any differences in what I’m submitting, nor does the `uniq` command. I didn’t see anything obvious comparing to the example submission file either. How should I go about figuring out what is off?

---

### Post #2 — **mugamma** | 2021-06-08 02:34 UTC

Turns out my issue was in the header. I had `ticker` instead of `numerai_ticker` like the example code. Changing to `numerai_ticker` gave me 100% live tickers matched.

The documentation on this should be clarified. It currently says the following which does not mention a `numerai_ticker` option nor explain whatever the semantic difference is.

> A `cusip`, `sedol`, or `ticker` column - values must be valid tickers associated with the ticker type in the header.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/90e8adeb4f6f03ac5b052087372c6555fb93d298_2_500x500.png) [docs.numer.ai](<https://docs.numer.ai/numerai-signals/signals-overview#submissions>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/32b3e8aa5391fe8f83bc813ffa7c27cdf492f134.png)

### [Overview | Numerai Docs](<https://docs.numer.ai/numerai-signals/signals-overview#submissions>)

Everything you need to know about Numerai Signals.

---

### Post #3 — **ihab** | 2021-07-02 22:38 UTC _(reply to #2)_

Hello [@mugamma](</u/mugamma>) I am having a similar issue even after I changed the ticker column header name. May I ask you what data provider you’re using? thank you.

---

### Post #4 — **mugamma** | 2021-07-02 22:54 UTC _(reply to #3)_

I’m getting the tickers out of the universe file linked above. Specifically, looping over those and generating rows. Not over some other source and trying to map over.

Try grabbing the example prediction file and submit that as a sanity check, then compare that file to what you are generating.

---

### Post #5 — **ihab** | 2021-07-02 23:23 UTC _(reply to #4)_

Thank you for your response [@mugamma](</u/mugamma>) that is a very good idea. And where you are getting your historical price data for your universe?
