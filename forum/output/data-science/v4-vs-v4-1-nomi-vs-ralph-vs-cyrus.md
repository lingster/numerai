---
title: "V4 vs V4.1, Nomi vs Ralph vs Cyrus"
category: Data Science
url: https://forum.numer.ai/t/v4-vs-v4-1-nomi-vs-ralph-vs-cyrus/6331
created_at: 2023-04-26T17:21:24.988000+00:00
last_posted_at: 2023-05-02T13:48:29.866000+00:00
posts_count: 3
views: 1237
tags: []
---

# V4 vs V4.1, Nomi vs Ralph vs Cyrus

---

### Post #1 — **master_key** | 2023-04-26 17:21 UTC

I was asked a question in [our discord](<https://discord.gg/numerai>) about why the benchmark model trained on [Nomi](<https://numer.ai/lg_lgbm_v4_nomi20>) has much higher TC than the model trained on [Cyrus](<https://numer.ai/lg_lgbm_v41_cyrus20>). And if this is true, then why do we think Cyrus is the better target?

I think this is an important question and I don’t want the answer to be lost in a discord thread.

To explain what could be going on here I gathered a few summary metrics on 6 different models.

The models are each combination of datasets v4/[v4.1](<http://forum.numer.ai/t/super-massive-data-sunshine/5977/23>) and targets Nomi/Ralph/Cyrus.

I then show the [CORR20V2](<http://forum.numer.ai/t/target-cyrus-new-primary-target/6303/21>) (the Numerai Corr with Cyrus) for each of these models over the last 1 year, as well as over the last 9 years.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/75b98b192cfbeed7a47c0f56b8d190aef0034fa2_2_636x500.jpeg)image1252×984 259 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/75b98b192cfbeed7a47c0f56b8d190aef0034fa2.jpeg> "image")

What’s interesting is that over the last year, indeed models trained on Cyrus don’t look better than models trained on Nomi or Ralph, even though Cyrus is the target all of the models are being scored against. This could explain how the current TC reputation could be lower for the v4.1 Cyrus model than the v4 Nomi model.

However if you look over the last 9 years, we see that the v4.1 model trained on Cyrus is the best in Sharpe and Corr, and is 2nd in Maximum Drawdown. This much longer period of great performance is why we believe Cyrus is a better target in general, and why we think models trained on it will have higher TC in the long run.

We really don’t know though, and that’s why we have 36 different targets. It’s almost certainly better to build multiple models on multiple targets and ensemble them in some way, building a model that is robust and will do well in any case.

---

### Post #2 — **joakim** | 2023-04-27 05:43 UTC

How do Nomi, Ralph, and Cyrus differ in terms of construction? Is there a risk that Cyrus has been ‘overly tweaked’ to work well on historical data, but may not generalize as well on future data compared to Nomi and Ralph?

---

### Post #3 — **halsmith99** | 2023-05-02 13:48 UTC

which feature set was used to generate these results with >1.5 sharpe?

my best ensemble on medium features is only 1.25.

apologies if answered on discord having trouble accessing.
