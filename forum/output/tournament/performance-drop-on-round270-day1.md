---
title: "Performance drop on round270 day1"
category: Tournament
url: https://forum.numer.ai/t/performance-drop-on-round270-day1/3697
created_at: 2021-07-01T22:26:16.844000+00:00
last_posted_at: 2021-07-07T08:06:51.281000+00:00
posts_count: 11
views: 1309
tags: []
---

# Performance drop on round270 day1

---

### Post #1 — **autratec** | 2021-07-01 22:26 UTC

Just received round 270 day 1 performance today, the model CORR and MMC dropped to very low level. I am confused with this resut, considing similar model used to generate predictions in previous rounds, and those old prediction still maintain 0.05+ CORR on 1july.

Why this could happen that same model can create such big difference on the same date in different rounds ?

I check the leader board and saw the similar pattern. Pls suggest your thoughts.

---

### Post #2 — **rigrog** | 2021-07-02 00:35 UTC

Just another random day, in Numerailand. Tomorrow will be another one.

---

### Post #3 — **autratec** | 2021-07-02 01:22 UTC _(reply to #2)_

Thanks for the sharing. Let’s wait for tomorrow.

---

### Post #4 — **restrading** | 2021-07-02 04:20 UTC

It’s still 4 weeks till round resolution, day 1 scores are very noisy, don’t be bothered by it.

---

### Post #5 — **restrading** | 2021-07-02 04:23 UTC

[@autratec](</u/autratec>) [Relationship of daily round correlations to final round correlations - #10 by jrai](<http://forum.numer.ai/t/relationship-of-daily-round-correlations-to-final-round-correlations/1176/10>)

---

### Post #6 — **bob_watson** | 2021-07-02 14:03 UTC

The problem of a weak signal in a lot of noise. Takes several days to average down the noise and the signal to start to correlate. Good robust models should see a slow solid linear rise over the 4 weeks (unlike mine which are buffeted around by chance and with luck end on a high)

---

### Post #7 — **jrai** | 2021-07-02 14:33 UTC _(reply to #6)_

Even “good” models won’t necessarily see a slow solid linear rise over the 4 weeks. I do think there’s still a lot to be learned about the intraround movement (mostly volatility) of a model’s daily scores, but no reason to think that it should be a slow linear rise

---

### Post #8 — **bob_watson** | 2021-07-02 15:07 UTC _(reply to #7)_

Yes I was thinking of a rather over-idealized situation

---

### Post #9 — **evanhennis** | 2021-07-05 20:39 UTC

Where are you seeing these updated values?

Also, wouldn’t the randomness of the stock market cause these issues as well?

---

### Post #10 — **autratec** | 2021-07-07 06:58 UTC _(reply to #9)_

after comparing the performance from 1JUL to 6JUL in other models in other round, i start to realize that all the model facing certain down turn in that period. And it lead to my following understanding:

  1. daily score is an accumulated score from round stating date to end. It is same like floating gain or lose situation.
  2. the score in the day 1 will be very close to zero as the calculation just started.



So we need to be patient to wait the market gradually aligned with prediction and score result move up daily.

---

### Post #11 — **themicon** | 2021-07-07 08:06 UTC _(reply to #10)_

The final score for a round is NOT a sum of the individual daily scores. Only the score on the last day of round close is what matters.

Please read the post that was linked to above: [Relationship of daily round correlations to final round correlations - #10 by jrai](<http://forum.numer.ai/t/relationship-of-daily-round-correlations-to-final-round-correlations/1176/10>)
