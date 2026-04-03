---
title: "Numerisle: a new community app predicting next round performances"
category: Tournament
url: https://forum.numer.ai/t/numerisle-a-new-community-app-predicting-next-round-performances/8198
created_at: 2025-10-23T16:53:51.655000+00:00
last_posted_at: 2025-11-11T17:27:36.300000+00:00
posts_count: 4
views: 383
tags: []
---

# Numerisle: a new community app predicting next round performances

---

### Post #1 — **nmrdragon** | 2025-10-23 16:53 UTC

Hi, I would like to introduce my Numerisle Unstaker website (<https://www.numerisle.fun/>) which can predict, how much you will earn or lose in the next round, so you can stake or unstake. It is based on a powerful lightGBM model I have been building for some time and according to my tests, it should have an interesting accuracy. Currently it is a very simple table of several leading models, which will be updated every day. I plan to add models and also the two remaining tournaments. A live test to check the live performance should be added in the coming days. I might also create some subscription service (like emails or notifications saying things like “Hey, in the next round, you will lose around 6 NMR if you don’t unstake.”). I hope it will help you to make more and avoid losses and also strengthen the meta model by making us stake more on models, that perform well.

---

### Post #2 — **nmrdragon** | 2025-10-23 16:56 UTC

**Numerisle news:**

  * A simple API, that will tell you every day, what model you should submit to your most-staked slot (if the model prediction is not pre-computed, it will make it on demand), it could help you automate things.



Example usage:

import requests  
individual_models = [“model1”, “model2”, “model3”]  
response = requests.post(“[https://www.numerisle.fun/api/try-models”](<https://www.numerisle.fun/api/try-models%E2%80%9D>), json={  
“usernames”: individual_models,  
“tournament”: “numerai”})  
best_model = response.json()[“best_model”][“username”]

  * Much more models (like thousands) will be usually available. Maybe not right now, as I am sometimes using fewer models for testing purposes.
  * Searching on the website based on your username, so you can see all your models.
  * Live test: overall and also for individual models, will show you the accuracy of Numerisle for resolved and also resolving rounds.



Thanks for trying it out on <https://www.numerisle.fun/> and your eventual feedback!

---

### Post #3 — **nmrdragon** | 2025-11-05 09:16 UTC

I am semi-decided to end with the Numerisle project. It is an interesting one and I think it has a lot of potential to change the Numerai community, Numerbay, improve meta models and more, but few of you seem really interested and I have some projects with a larger profit potential waiting. And also it would be very time-consuming to build it all.

Here I would like to reveal my final vision in case it inspires someone.

So I have models for predicting all tournaments’ models and meta models, API, website, etc. This is just a single thing called Numerisle Unstaker, to which I wanted to add also an advisor for which Numerbay model to subscribe to and for each model also n most similar models and predictions for them.

I planned to scale it into a Numerisle Platform, which would contain this as a small pretty standalone service + Numerisle Library. It would all be based on predicting performance of the models and reverse engineering past predictions, mostly for ensembling purposes (for example predicted performance + past predictions = well suited for suggesting wildly good ensembles).

Numerisle Library: it is a place where you would put your read-only Numerai key and it would fetch your models’ predictions regularly. For each model, you could choose either:

  0. don’t fetch at all

  1. private (only you can see your predictions, insights about the predictions + suggested ensembling with open predictions (see 2) or Numerbay-available predictions)

  2. public (open predictions for anyone to submit or ensemble with, could help new Numerai people and who knows, maybe even more experienced ones could ensemble with it)

  3. for partners (most interesting option, it would suggest creating groups, where ensemble / n members would yield more profit than submitting alone, each partner would get the final ensemble)

  4. Numerisle Masters (donate your prediction to a common ensemble (something like our own meta model, but not based on averaging, but rather some ML over predicted results and insights about ensembling of past predictions of the individual models) and get rewarded based on how much it helped (the more valuable contribution, the more rows of your set of predictions you get alignment report for), alignment report: a slightly obfuscated information about how to modify each of your predictions to be more in line with our meta model one)




So if anyone interested, it would be awesome to build something like this and maybe Numerai or COE could sponsor something like this a bit. I think model and cross-model insights (like predicting model results or ensembling success) have a very high potential for all three tournaments and it’s a shame that something like this doesn’t exist yet.

Predicting model performance, smart cross-user ensembling and other forms of cooperation should be definitely used more, as they are basically different, but still valuable, paths to Numerai success.

---

### Post #4 — **nmrdragon** | 2025-11-11 17:27 UTC

![:rocket:](https://emoji.discourse-cdn.com/twitter/rocket.png?v=15) New Features:

  * Now it can work with some round data missing (uses monte carlo imputation; the predictions are then marked with orange or red dot)
  * Individual model stats: you can look, how well the predictions perform for YOUR models (you can search the models by an owner name btw).
  * Most similar and most dissimilar models on individual model pages. Shows also their average. Who wouldn’t want similar models to have good predictions?
  * Ensembling: suggests what models you could ensemble with, which is good mostly for yours + Numerbay models. This one is my favorite new function. It takes some time to compute everything, but some of the ensembles are crazy good!



![:rocket:](https://emoji.discourse-cdn.com/twitter/rocket.png?v=15) Results  
Numerisle already has a few weeks of resolving data, which is hundreds, resp. thousands of data points. Let’s take a look at the performance metrics.

  * Classic Tournament: This is the worst-peforming one so far, even though it has the most data. The only positive thing is the adjusted correlation, which is positive. That means the correlation is better than it would be if we always predicted a recent rolling average. Other metrics are pretty bad. Average round profit of models, that got a STAKE recommendation: -0.055%. UNSTAKE: 0.150%. Let’s hope it will be better.
  * Signals Tournament: Both correlation and adjusted correlation are positive. Average round profit of models, that got a STAKE recommendation: 0.051%. UNSTAKE: 0.027%.
  * Crypto Tournament: This one has the best results so far. Great correlations and everything. Average round profit of models, that got a STAKE recommendation: 0.195%. UNSTAKE: -0.138%.  
I think overally, the results are slightly encouraging, but not that much. Also the amount of available data is not yet that high and first resolving round or small stratum data decreases the data quality significantly.



I am looking forward to collecting more data in the coming days. Thank you for your eventual interest.

You will find the app here: [www.numerisle.fun](<https://www.numerisle.fun>)
