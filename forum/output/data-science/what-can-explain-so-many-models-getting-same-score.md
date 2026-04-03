---
title: "What can explain so many models getting same score?"
category: Data Science
url: https://forum.numer.ai/t/what-can-explain-so-many-models-getting-same-score/7094
created_at: 2024-03-10T00:17:50.489000+00:00
last_posted_at: 2025-11-14T05:37:22.165000+00:00
posts_count: 10
views: 2172
tags: []
---

# What can explain so many models getting same score?

---

### Post #1 — **coffee_ai** | 2024-03-10 00:17 UTC

Are there example models that many people are being submitted on? Very high frequency of exact same score.

---

### Post #2 — **andralienware** | 2024-03-13 15:34 UTC

Some people buy predictions from other people on numerbay

---

### Post #3 — **invalid_datatype** | 2024-03-19 19:16 UTC

correlations could be analyzed to find repetitions of the same model. I think those models should probably be penalized, because they do not contribute new information to the overall meta prediction.

---

### Post #4 — **shatteredx** | 2024-03-19 20:06 UTC _(reply to #1)_

Yeah there are example predictions as well as example models from the tutorial notebooks which have a lot of identical scores.

---

### Post #5 — **thinkdevdo** | 2024-03-20 05:08 UTC _(reply to #3)_

They split MMC among them if they are equal predictions, this is a penalization. If they have the same corr but different predictions, there’s no reason to penalize.

---

### Post #6 — **eleven_sigma** | 2024-03-21 14:58 UTC _(reply to #3)_

Why penalize them? I can stack N NMR to one model or N/2 to two models using the same prediction. The second option is better for me if in future I want to use two differents models. Stacking all to one model is less flexible.  
MM is built taking into account the overall NMR staked to each prediction, so where is the problem? They CONTRIBUTE with new information, the more important information, someone is confident enough to put the skin in the game.

---

### Post #7 — **eleven_sigma** | 2024-03-21 15:00 UTC _(reply to #5)_

This would be the case if the MMC was computed with leave one out strategy, but that is very expensive in CPUs. MMC is computed with your model vs the MM (which include your model), so MMC is independent of your NMR is all-in or shared by 2 o 10 models.

---

### Post #9 — **rustydata** | 2024-08-28 18:49 UTC

Imagine the market behaves very reliably, so much so that most models basically suggest something like index weighting, or maybe in a market like this past year, a well modeled portfolio might look a lot like popular ETFs. If we arent **correct in contradicting** the majority of models, we arent adding anything to be rewarded; hedge funds dont need models that just suggest matching the VGT portfolio allocation.

And that may be part of what’s been happening in the last few weeks. Since the yen-carry unwind started, there has been something of a divergence in CORR and MMC, which kinda points to the models [that had previously been doing well] not making incorrect predictions, but whose predictions are no longer adding any value. Lots of reasons for this, not least of all the fact that every MM is also pricing in the same stuff, all investors are being cautious, and the options market reflects that in premium pricing. If the delta of predicted expected value to (strike + premium) doesnt present an opportunity over, or just reinforces HOLD, the prediction isnt that valuable.

If we are predicting that the price will be well within the implied volatility range, the prediction doesn’t add much. If we do predict some strong movement, it has to be far enough outside center of the implied volatility for the fund to be able to realize a meaningful benefit (buy side goal of getting an appealing delta between strike+premium and the expected value). On top of just correctly contradicting the other models, there is also a bit of a need to contradict the rest of the entire market. Worth repeating: **hedge funds** usually arent just trying to match ETFs but rather **benchmark against them**. (Why pay a fund 2 and 20 if they arent beating VGT/MGK? Why reward models that ended up modeling those?)

Here’s an example of the way a shift may have played out these past few months.  
IDK - being clear on that; this is at best a plausible story

If the overall strategy was _just_ buying for alpha, predictions where we **correctly contradict market expectations of volatility** hold the most potential for reward. Thats probably balanced by using predictions to determine opportunity for sell-side pricing - what likely covered by the premium. If most models predicted a mostly flat/sideways market into the next fed meeting, it would make sense to put a bit more exposure onto the sell side. Usually, a reliable way to generate some income in an otherwise boring market, but exogenous shocks could definitely change that.

[un-fancy cyrus_v4_20 model](<https://numer.ai/rusty7>)

Note the change between June, when momentum indicators were driving trading - a bit range-bound, concentrated, going from overbought to oversold. Until politics, and then the fed, became the focus (“rotation?”). So the models that did great focusing heavily on momentum started dropping in mmc. I have been working to update my models since realizing they needed to be. Even still, there is that clear inflection in early august with the carry unwind. Model accuracy took a clear _temporary hit_ , but even after establishing a new slope up (good predictions, but clearly in a different way), the mmc decline continues because there’s a 1 month lag not just on what we predict, but _logically,_ realizing gains or losses on the positions also have an additional 20-trading-day/1-month lag. _Say_ it takes 20 days to enter the position based on the prediction. Ok, they get it. Then it takes 20 days from then to exit based on the past 20 and next 20 predictions and market trading opportunity or lack thereof. And then in this case specifically, even if we were updating our models, we are using a minimum 20-day target, so we didnt even start uploading models that reflected the change in fundamental drivers until the last week or so. It gets much harder exiting positions based on a different set of theses than what motivated their entry. Sell side is often harder than buy - ask anyone that _didnt_ get rich trading options. I wouldnt be surprised if signals became _the adult in the room_ for a week or so.

---

### Post #11 — **ruhiparveen** | 2025-05-06 06:42 UTC

Yes, many models are submitted on platforms like Kaggle, and popular models like XGBoost, LightGBM, or neural networks like CNNs often lead to high-frequency, similar scores.

---

### Post #12 — **jakasspeech2** | 2025-11-14 05:37 UTC _(reply to #7)_

![](https://avatars.discourse-cdn.com/v4/letter/e/8797f3/48.png) eleven_sigma:

> This would be the case if the MMC was computed with leave one out strategy, but that is very expensive in CPUs. MMC is computed with your model vs the MM (which include your model), so MMC is independent of your NMR is all-in or shared by 2 o 10 models.

So, whether I share my NMR with 2 friends or 10, the MMC doesn’t care.
