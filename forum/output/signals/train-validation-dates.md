---
title: "Train/validation dates"
category: Signals
url: https://forum.numer.ai/t/train-validation-dates/3341
created_at: 2021-05-18T13:38:30.958000+00:00
last_posted_at: 2021-05-19T13:12:56.781000+00:00
posts_count: 4
views: 757
tags: []
---

# Train/validation dates

---

### Post #1 — **quantized** | 2021-05-18 13:38 UTC

I’m new to Signals and am developing a model. I notice the _train_ data is all quite old, up to about 2012, with _validation_ being data since 2012. Is there a reason for this? Ideally I’d like to train on more recent data due to the type of signal I’m developing. Maybe I’m missing something here?

---

### Post #2 — **minou** | 2021-05-19 12:33 UTC

Unlike the main competition, the data in the historical file isn’t essential to use. The target you submit (a continuous value centered around 0.5) is based on the expected return between day 2 and day 6 after the Friday date, and you can use any data you like to come up with a signal. If you plan to derive from traditional OHLC/OHLCV market data, you might use a data source such as y-finance, and train/validate over any segments of the data you wish. Submitting values derived directly from some data without involving a model could also be effective, e.g. if you had a source of short term sentiment data, simply centering and scaling that might suffice.

---

### Post #3 — **quantized** | 2021-05-19 12:59 UTC

Thanks for that. I guess if I don’t use the published validation data I won’t get any metrics from Numerai, but that doesn’t matter if I’ve done my own train/test splitting from data I’ve got from yfinance or elsewhere. Or would I get some metrics?

---

### Post #4 — **minou** | 2021-05-19 13:12 UTC _(reply to #3)_

There are only diagnostics if submitting signals based on validation data. Depending on preference, that info could be useful to have as a comparison of models or merely an unnecessary complication. Unlike the main competition, validation takes a while to be produced for signals (up to 15 mins mentioned in the docs IIRC), so that might sway against using it. Purely personal preference though.
