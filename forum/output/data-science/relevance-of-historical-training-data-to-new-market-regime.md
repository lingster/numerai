---
title: "Relevance of historical training_data to new market regime"
category: Data Science
url: https://forum.numer.ai/t/relevance-of-historical-training-data-to-new-market-regime/1039
created_at: 2020-10-08T06:57:13.744000+00:00
last_posted_at: 2020-10-11T21:32:07.870000+00:00
posts_count: 6
views: 1334
tags: []
---

# Relevance of historical training_data to new market regime

---

### Post #1 — **kkk** | 2020-10-08 06:57 UTC

Maybe a naive question here ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) It appears that for each round the _training_data_ is identical, and how can the model to be trained in order to cope with the nouvel pattern/regime of the market as the historical data is deemed to lose gradually its relevance and to make the validation / backtest less effective, for instance, the covid-19 scenario (it’s likely that the training data set does not cover this era).  
What’s the reason that numerai does not update the training set regularly ?

---

### Post #2 — **jzv82** | 2020-10-10 20:51 UTC

I was think about the same thing. It would make sense to have all past eras before current round for train/validation. What’s the reason not to expand train/validation data each round?

This would allow to make better regime change models and perform rolling (aka sliding) cross-validation and model training.

---

### Post #3 — **crystal_sphere** | 2020-10-11 19:57 UTC _(reply to #2)_

Tournament data is actually updated regularly, but as test eras, i.e. without the targets provided. If targets were provided, Numerai would not be able to use the test eras for out-of-sample validation of the submitted predictions.

---

### Post #4 — **jzv82** | 2020-10-11 20:00 UTC _(reply to #3)_

Well, fine, you can leave the last N eras for oos validation and still increasing training data in an expanding way, right?

---

### Post #5 — **crystal_sphere** | 2020-10-11 21:07 UTC

Numerai founder and CEO Richard Craib stated that the plan is to release updated validation data every 6 months.

Source: [Fireside Chat 2020 Q4](<https://youtu.be/mbwMXUzPot4?t=1640>)

---

### Post #6 — **wigglemuse** | 2020-10-11 21:32 UTC

Richard said recently that they will probably be releasing new validation data every 6 months, so that’s something.
