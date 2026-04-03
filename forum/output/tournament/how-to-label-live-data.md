---
title: "How to label live data"
category: Tournament
url: https://forum.numer.ai/t/how-to-label-live-data/4999
created_at: 2022-02-28T22:15:26.332000+00:00
last_posted_at: 2022-03-01T18:10:20.539000+00:00
posts_count: 5
views: 873
tags: []
---

# How to label live data

---

### Post #1 — **sneaky** | 2022-02-28 22:15 UTC

Hello there,

I came up with a method that should enable us to further train on live eras.

The problem: live data has no labels, thus we cannot train on it.  
The solution:  
1) cluster eras (for example my solution [here](<http://forum.numer.ai/t/clustering-eras/4863/7>))  
2) train a model on each era cluster separately in order to bias the model to its cluster  
3) separately upload the predictions of the trained models  
4) for every live era choose the model with the highest score and its predictions are now labels of the era  
The idea: to create a bunch of distinct models and trial the models on the live data to figure which model is the most effective. Then we can assume that this model’s predictions are the best known representation of the era targets.

I started 3 weeks ago, thus I have no results yet. Did anybody try it before me?

---

### Post #2 — **profricecake** | 2022-03-01 01:46 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/4bbf92/48.png) sneaky:

>   4. for every live era choose the model with the highest score and its predictions are now labels of the era
> 


What is your plan for calculating a score for the live eras without targets? Do you mean instead “choose the model corresponding to the nearest era cluster for the given live era, predict with it, and consider those predictions as the new targets for that live era”?

If I’m right about that being your plan, let’s assume your models get single-digit correlation percentages like most seem to do around here. Then you’re creating targets for the live era that are honestly not very accurate. If you train models on those eras I wouldn’t be very confident about any results you see.

The Numerai folks did say they were going to release target info for live eras in March. Maybe the best move would be to wait and train against the true targets when they appear? That’s my plan.

---

### Post #3 — **sneaky** | 2022-03-01 09:40 UTC _(reply to #2)_

Didn’t know they plan to do that ![:thinking:](http://forum.numer.ai/images/emoji/twitter/thinking.png?v=10). In that case it is definitely better to use real targets if you want to optimize for correlation.

I am not sure that you understood what I meant. The model would be chosen by its score from the live predictions. For example I would upload N distinct models for round X, then wait 4 weeks, harvest results, choose the most successful model, use its prediction as a base for calculating labels of the X round.

I don’t think that the inaccuracy would be problem if you have enough models. But have no data to back my claim yet.

---

### Post #4 — **wigglemuse** | 2022-03-01 16:29 UTC

You can test your version in a walk-forward manner on old data and see how it goes. But yes, we are just a few weeks or less away from getting a bunch more data with targets anyway. (I think MikeP said 60% more, plus will we get resolved targets weekly going forward sounds like.)

---

### Post #5 — **profricecake** | 2022-03-01 18:10 UTC _(reply to #3)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/4bbf92/48.png) sneaky:

> I would upload N distinct models for round X, then wait 4 weeks, harvest results, choose the most successful model, use its prediction as a base for calculating labels of the X round.

Oh I definitely didn’t understand what you meant. This makes sense and is much clearer - thank you! But yes, I do think that if they come through with the new targets as advertised, this approach may not be necessary.
