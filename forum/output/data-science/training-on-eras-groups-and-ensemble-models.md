---
title: "Training on eras groups and ensemble models"
category: Data Science
url: https://forum.numer.ai/t/training-on-eras-groups-and-ensemble-models/848
created_at: 2020-08-25T09:06:45.209000+00:00
last_posted_at: 2021-05-14T01:22:05.094000+00:00
posts_count: 4
views: 2536
tags: []
---

# Training on eras groups and ensemble models

---

### Post #1 — **olivepossum** | 2020-08-25 09:06 UTC

I’ve been doing some experiments with the idea of training on eras groups and ensemble models.

Taking into account the training dataset has 120 eras (so, 120 sequential months as far as I understood) I join continuous eras in groups of 12 and train them together.

An ensemble model is trained for each group of eras and then performance is evaluated by predicting on the validation data with each of those models. Finally, predictions are averaged.

Each ensemble model is composed by a XGBoostRegressor, a CatBoostRegressor and a LightGBMRegressor.

Models of each ensemble model, are optimized separately using 3 splits kfold cross-validation and no shuffling.

The idea came up after reading some [sample scripts](<https://github.com/numerai/example-scripts/blob/master/Cross_Validation_and_Model_Optimization.ipynb>) and other [resources](<https://towardsdatascience.com/a-guide-to-the-hardest-data-science-tournament-on-the-planet-748f46e83690>).

Details are [published on a Colab notebook](<https://colab.research.google.com/drive/1W4XNv9vwsMLnoKPgWti8JzHrXhE1-YjK#scrollTo=tCdoumbycX_k>)

Any feedback is welcome!

---

### Post #2 — **jorijnsmit** | 2020-08-29 10:08 UTC

Is ensembling a good idea by default? I can imagine situations in which one of the three models outperforms the ensembled model. Maybe you could compare metrics before deciding on using a single or ensembled model for submitting predictions?

---

### Post #4 — **ryendu** | 2021-05-13 21:13 UTC

Yes, in my opinion, ensembleing is a great Idea in general. I experimented with training mini-simple just dense/linear neural nets on the tournament data, and ensembling them all together and I found that the average loss for each neural net is about 0.3-0.05 depending on the learning rate, but the loss of the mean of all the neural net’s predictions are always less than 0.05. This can be exaggerated and most clearly seen with higher learning rates where the average loss for all the neural nets were about 0.3 while the loss for the mean of all the predictions of the neural nets were always less than 0.05. And just incase I sound confusing, the difference between the average loss for each neural net and the loss of the average of the predictions is that the average loss for each neural net is the loss for each neural net averaged while the loss of the average of the predictions of the neural nets is the loss of the ensemble’s averaged prediction.

---

### Post #5 — **ryendu** | 2021-05-14 01:22 UTC _(reply to #4)_

Now that I think about it some more, isn’t Numerai’s meta model just a more complex ensemble?
