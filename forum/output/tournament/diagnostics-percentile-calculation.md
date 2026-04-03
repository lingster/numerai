---
title: "Diagnostics percentile calculation"
category: Tournament
url: https://forum.numer.ai/t/diagnostics-percentile-calculation/2481
created_at: 2021-03-21T15:58:25.736000+00:00
last_posted_at: 2021-03-22T07:41:29.488000+00:00
posts_count: 3
views: 779
tags: []
---

# Diagnostics percentile calculation

---

### Post #1 — **quantized** | 2021-03-21 15:58 UTC

Does anyone know how diagnostics percentiles are calculated? I have a Sharpe of 1.2879 which claims to be 100%, but I know it is lower than many other Sharpes out there. So it can’t be using the actual distribution of diagnostics.

I found [this post](<http://forum.numer.ai/t/coloring-validation-metrics/1269>). My percentiles agree on the basis of some of those numbers but not on others.

Not that it matters a great deal, although this could be giving false hope to folks out there whose models are not as good as they appear on the diagnostics (and I appreciate this is only validation diagnostics and nothing to do with live).

Thanks!

---

### Post #2 — **asteeber** | 2021-03-22 04:37 UTC

I’m not certain but if I had to guess it probably compares your Sharpe with the distribution of actual Sharpes from past rounds.

Say the average Sharpe is 0.5 and the standard deviation is 0.25 (fake numbers obviously). Your predicted Sharpe is 3+ standard deviations away from the average so one minus the pvalue would be like 0.9999 (or 100%). If your predicted Sharpe is 0.75, you’d get 0.83333 (or 83%).

Again, just guessing here.

---

### Post #3 — **quantized** | 2021-03-22 07:41 UTC _(reply to #2)_

Thanks, it doesn’t seem to be that either looking at my figures.
