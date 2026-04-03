---
title: "How often do you re-train your model?"
category: Data Science
url: https://forum.numer.ai/t/how-often-do-you-re-train-your-model/8164
created_at: 2025-08-01T01:52:39.355000+00:00
last_posted_at: 2026-03-21T21:40:28.874000+00:00
posts_count: 9
views: 1257
tags: []
---

# How often do you re-train your model?

---

### Post #1 — **spn30n** | 2025-08-01 01:52 UTC

My model performed well on the first few weeks, and then the performance degraded. I wonder how often should we re-train our model to incorporate the new data.

---

### Post #2 — **anthill** | 2025-08-01 17:32 UTC

How sensitive you are to the most recent data may depend on your specific model. Some models do best with up-to-date data, others are looking more for stable signals that don’t change much over time. Models that use more stable signals would ideally have less volatility and so be less susceptible to drawdowns.

But ultimately you can figure out what works best for your model by doing step-forward training. Backtest on the validation data by training on the “freshest” data for a particular validation era, vs. data that is a few weeks old and see which does better.

---

### Post #3 — **bguberfain** | 2025-08-07 09:52 UTC

I retrain my model weekly

---

### Post #4 — **svendaj** | 2025-08-08 14:54 UTC

I retrain weekly, namely because it’s for free. I am fully automated on Kaggle platform, so it costs me nothing and I can focus on experimentation. If there were some costs related, I would certainly think twice about retraining frequency.

The frequency of retraining is almost like trying to time the market - a futile effort. For example, my best public model [JOS_KAGGLE_SUNSHINE Profile - Numerai](<https://numer.ai/jos_kaggle_sunshine>) has been trained 10 months ago (no retraining since) and has reasonable 1Y return of 61.7% and its CORR20 performance is at #152 of the models leaderboard.

---

### Post #5 — **jakasspeech2** | 2025-12-21 09:14 UTC _(reply to #4)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/svendaj/48/3285_2.png) svendaj:

> I retrain weekly, namely because it’s for free. I am fully automated on Kaggle platform, so it costs me nothing and I can focus on experimentation. If there were some costs related, I would certainly think twice about retraining frequency.
> 
> The frequency of retraining is almost like trying to time the market - a futile effort. For example, my best public model has been trained 10 months ago (no retraining since) and has reasonable 1Y return of 61.7% and its CORR20 performance is at #152 of the models leaderboard.

You could ensemble the static model with the weekly one to balance long term stability with short term adaptation

---

### Post #7 — **gammarat** | 2026-02-05 08:19 UTC

When the data or formats are changed enough so that I have to. Numerai seems to change those just about every time I get some model running well enough to put money down on it.![:man_shrugging:](https://emoji.discourse-cdn.com/twitter/man_shrugging.png?v=15) On the bright side, every time I have to adapt to new formats/data, I substantially change my approaches, and I do find that entertaining. I’m in the middle of building new ones for each of the competitions,so it’ll be awhile before they’r up and running.

---

### Post #8 — **svendaj** | 2026-02-17 22:47 UTC

Some experimental data on the topic: [When to Retrain a Model — A Casuistic Analysis - Tournament - Numerai Forum](<https://forum.numer.ai/t/when-to-retrain-a-model-a-casuistic-analysis/8253>)

---

### Post #9 — **digitalforensicfocus** | 2026-03-02 21:00 UTC _(reply to #4)_

Thats an awsome rate of return. Where can I subscribe.

---

### Post #10 — **svendaj** | 2026-03-21 21:40 UTC _(reply to #9)_

Easy. Here: [Numerai](<https://numer.ai/>) ![:smiling_face_with_sunglasses:](https://emoji.discourse-cdn.com/twitter/smiling_face_with_sunglasses.png?v=15)
