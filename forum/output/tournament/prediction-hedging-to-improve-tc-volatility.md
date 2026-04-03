---
title: "Prediction Hedging to Improve TC Volatility"
category: Tournament
url: https://forum.numer.ai/t/prediction-hedging-to-improve-tc-volatility/5391
created_at: 2022-05-11T23:44:48.716000+00:00
last_posted_at: 2022-05-25T04:46:50.101000+00:00
posts_count: 5
views: 857
tags: []
---

# Prediction Hedging to Improve TC Volatility

---

### Post #1 — **dzheng1887** | 2022-05-11 23:44 UTC

I am curious if anyone has given this thought, but if TC is the gradient of the returns with respect to my stake, is there a way to adjust my predictions to reduce the noise in that gradient? For example, for assets with volatile future returns, predict those at 0.5 but for stable positive returns predict with 1.0 and stable negative returns predict with 0.0

---

### Post #2 — **wigglemuse** | 2022-05-12 00:06 UTC

Your predictions are still uniformly rank normalized for TC – never the raw values – so any adjustments you make come down to reshuffling the order of your predictions. Ensembling predictions that get uncorrelated TC may be the way to go, but it is hard to get a handle on empirically when we can’t test directly and have limited data to make guesses.

---

### Post #3 — **yxbot** | 2022-05-23 22:00 UTC

I am spreading my TC allocations on models that 1) uncorrelated with each other on the predictions, and 2) generated on average significant positive TC - in my case with avg TC > 0.01.

For me, the big uncertainly is how useful is historical TCs as reference, and how does regime change impacts TC scores

---

### Post #4 — **dzheng1887** | 2022-05-24 00:55 UTC

I think the regime change would also generally affect corr as well.

As like any statistic that is more volatile, you’ll just have to be more cautious looking at the current evidence. Rely on a prior a bit more. I think it is correct in expectation.

---

### Post #5 — **yxbot** | 2022-05-25 04:46 UTC _(reply to #4)_

regime change definitely affect corr, however since we can directly work to optimise corr, and generally have better understanding how corr behave across longer timeframe, not to mention the v4 data allow you to calculate corr for much longer period, it is just more workable ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

I think as time moves, with more models and more track records, on we would have better understanding on TCs as well
