---
title: "Fund's recent performance"
category: Numeraire
url: https://forum.numer.ai/t/funds-recent-performance/6660
created_at: 2023-09-07T13:00:40.991000+00:00
last_posted_at: 2024-09-17T21:48:55.113000+00:00
posts_count: 6
views: 2883
tags: []
---

# Fund's recent performance

---

### Post #1 — **ojymbxlu1bg** | 2023-09-07 13:00 UTC

Ever since 22 October, the fund’s volatility skyrocketed, and since March it has been on a massive drawdown. I’m guessing the increased volatility is from the addition of daily predictions (and trades?).

Could someone explain this situation?

---

### Post #2 — **sneaky** | 2023-09-07 18:31 UTC

Richard said in one interview that they increased the metamodels exposure to more volatility right before the big drawdown. It would have fell either way, but the higher volatility certainly didn’t help.

---

### Post #4 — **ojymbxlu1bg** | 2023-09-08 19:08 UTC _(reply to #2)_

Thanks, that’s quite reassuring.

Do you know if there is any available historical data on the corr. scores of the meta-model? I’m trying to see if there is a “performance degradation” of the models submitted or if it’s just a “below EV” period.

---

### Post #5 — **sneaky** | 2023-09-08 19:13 UTC _(reply to #4)_

Do you mean corr meta-model with target? You can calculate it on your own if you download the historical meta_model predictions here <https://numer.ai/data/v4.2> `napi.download_dataset("v4.2/meta_model.parquet", "meta_model.parquet")`

---

### Post #6 — **spammyspam** | 2024-09-17 13:22 UTC

Is there any updates to how the fund is doing now? I see the performance stats are no longer on the website now

---

### Post #7 — **rustydata** | 2024-09-17 21:48 UTC _(reply to #6)_

My hunch is that they got hit badly during the yen carry fallout. The nature of the predictions - the 20 day lag, and the 0, .25, .5, .75, 1.0 grain, and the fact that many people arent ranking or neutralizing their predictions was probably telling the fund to generate income during a period of range-bound price action, meaning they we’re over exposed short volatility. In any normal market, selling puts below the price range would have been low-risk income. But the way we pass predictions, there is probably going to be a bias towards mischaracterizing that risk. And from what I can see, the new dataset is _overfitting_ the neutralization.

In a model that generally performs well, neutralization has no effect until after the carry trade unwind, or when they would have trained for metamodels and neutralization for v5. The release post said that it was neutralized differently to reflect the goals of the fund. They told us they want to reward something other than what we predominately predict. We can also see this in recent the divergence of CORR and MMC. Ive suspected this is from losses still being realized.

The questions Im trying to figure out is what to model going forward. I wonder if adding granularity to the predictions might help and adding shorter-window targets. _If I were_ managing the use of numerous predictions to trade, Id still want my 1, 5, and 15m. Id imagine some features are lags of others, and some targets are just lags and leads of others, but I cant help but wonder how we’d treat the data if we could be more intentional.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/64ae59f7236919fb71974c6bad1fdc3e60102521_2_690x413.png)image1000×600 38.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/64ae59f7236919fb71974c6bad1fdc3e60102521.png> "image")
